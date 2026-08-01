//----------------------------------------------------------------------------
//   Copyright (c) 2014 Siemens Product Lifecycle Management Software Inc.
//                         All rights reserved
//----------------------------------------------------------------------------
// 
//
// CustomResourceBarTab.cpp
//
// Description:
//   This is an example of allowing the third party application to
//   embed their own tools or interactive windows into a tab within the
//   NX resource bar.
//
//   All of the files for this sample reside in the ugopen kit under:
//   SampleNXOpenApplications/Cpp/CustomResourceBarTab/.
//
//   *** PLEASE NOTE ***
//   To load the shared library created from this program during startup, 
//   it must be placed in the "startup" directory under a directory listed in the 
//   file pointed to by the environment variable in UGII_CUSTOM_DIRECTORY_FILE.
//
//----------------------------------------------------------------------------

/* Include files */
#if ! defined ( __hp9000s800 ) && ! defined ( __sgi ) && ! defined ( __sun )
#   include <strstream>
#   include <iostream>
    using std::ostrstream;
    using std::endl;    
    using std::ends;
    using std::cerr;
#else
#   include <strstream.h>
#   include <iostream.h>
#endif

#include <uf.h>
#include <uf_ui.h>
#include <uf_exit.h>

#include "CustomResourceBarTab.h"
#include <NXOpen/NXObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/ResourceBarManager.hxx>

#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session* CustomResourceBarTab::theSession = NULL;
UI* CustomResourceBarTab::theUI = NULL;
ListingWindow* CustomResourceBarTab::listW = NULL;
HINSTANCE CustomResourceBarTab::theInst = NULL;
static CustomResourceBarTab* theCustomResourceBarTab = NULL;
static HWND hAdd = NULL;
static HWND hActivate = NULL;
static HWND hHide = NULL;
static HWND hShow = NULL;
static HWND hRemove = NULL;
static HWND hMain = NULL;
static int tab_count = 0;
CustomResourceBarTab::StlChildWindowMap CustomResourceBarTab::g_ChildMap;
CustomResourceBarTab::StlRegisteredTabMap CustomResourceBarTab::g_TabMap;

static LRESULT CALLBACK WndProc(HWND hwnd, UINT Message, WPARAM wParam, LPARAM lParam);

CustomResourceBarTab::CustomResourceBarTab()
{
    try
    {
        // Initialize the NX Open C++ API environment
        theSession = Session::GetSession();
        theUI = UI::GetUI();

        // Initialize the listing window
        listW = CustomResourceBarTab::theSession->ListingWindow();

        // Get the handle to the specified module
        theInst = GetModuleHandle(_T("CustomResourceBarTab.dll"));
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }
}

CustomResourceBarTab::~CustomResourceBarTab()
{
    DestroyWindow(hMain);
}

BOOL CustomResourceBarTab::InitApplication() 
{ 
    WNDCLASSEX wcx; 

    // Fill in the window class structure with parameters 
    // that describe the main window. 
    wcx.cbSize = sizeof(wcx);            // size of structure 
    wcx.style = CS_HREDRAW | CS_VREDRAW; // redraw if size changes 
    wcx.lpfnWndProc = WndProc;           // points to window procedure 
    wcx.cbClsExtra = 0;                  // no extra class memory 
    wcx.cbWndExtra = 0;                  // no extra window memory 
    wcx.hInstance = theInst;             // handle to instance 
    wcx.hIcon = NULL;                                     // predefined app. icon 
    wcx.hCursor = LoadCursor(NULL, IDC_ARROW);            // predefined arrow 
    wcx.hbrBackground = ::GetSysColorBrush(COLOR_WINDOW); // white background brush 
    wcx.lpszMenuName = NULL;                              // name of menu resource 
    wcx.lpszClassName = L"TestWClass";                    // name of window class 
    wcx.hIconSm = NULL;                                   // no small class icon

    // Register the window class. 
    return RegisterClassEx(&wcx); 
}

BOOL CustomResourceBarTab::InitInstance() 
{       
    HINSTANCE hInst = CustomResourceBarTab::theInst;

    // Create the main window. 
    hMain = CreateWindow( 
        L"TestWClass",       // name of window class 
        L"Main",             // title-bar string 
        WS_CAPTION|WS_SYSMENU|WS_OVERLAPPEDWINDOW, // top-level window
        CW_USEDEFAULT,       // default horizontal position 
        CW_USEDEFAULT,       // default vertical position 
        220,                 // default width 
        250,                 // default height 
        (HWND)NULL,          // no owner if NULL
        (HMENU) NULL,        // use class menu 
        theInst,             // handle to application instance 
        (LPVOID) NULL);      // no window-creation data 

    if (!hMain) 
        return FALSE; 

    ShowWindow(hMain, SW_SHOW); 
    UpdateWindow(hMain);

    return TRUE;
}

int CustomResourceBarTab::GetLastRegisteredID() const
{
    StlRegisteredTabMap::const_iterator it;

    int tab_id = 0;
    for (int i=tab_count; i>0; i--)
    {
        it = g_TabMap.find(i);
        if (it != g_TabMap.end())
            return it->second;
    }

    return 0;
}

int CustomResourceBarTab::GetRegisteredNumber(int tab_id) const
{
    int tab_num = 0;
    for(StlRegisteredTabMap::const_iterator it = g_TabMap.begin(); it != g_TabMap.end(); ++it)
    {

        if (tab_id == it->second)
            return it->first;
    }

    return tab_num;
}

int CustomResourceBarTab::ActivationHandler(int tab_id)
{
    try
    {
        // Get the WindowHandle object
        WindowHandle *window_handle = CustomResourceBarTab::theUI->ResourceBarManager()->GetWindowHandle(tab_id);
        // Get the real handle
        HWND parent_handle = (HWND)window_handle->GetHandle();
        BOOL is_window = ::IsWindow(parent_handle);

        char msg[256];
        // Open the Print the Information window and print the message.
        CustomResourceBarTab::listW->Open();
        sprintf_s(msg, "Window Handle: %p %s", parent_handle, is_window ? "is a window" : "is not a window");
        CustomResourceBarTab::listW->WriteLine(msg);
        
        // Check if the child window is already created
        HWND child_handle = theCustomResourceBarTab->GetChildWindow(tab_id);
        if (is_window && child_handle == NULL)  
        {
            HWND child_handle = CreateChildWindow(parent_handle);
            theCustomResourceBarTab->SetChildWindow(tab_id, child_handle);
        }
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }
    return 0;
}

HWND CustomResourceBarTab::CreateChildWindow(HWND parent_handle)
{
    RECT rcClient; 
    GetClientRect(parent_handle, &rcClient);
    HWND hChild = NULL;
    HINSTANCE hInst = CustomResourceBarTab::theInst;

    if (parent_handle != NULL)
    {
        // Create the main window. 
        hChild = CreateWindow( 
            L"TestWClass",       // name of window class 
            L"Child",            // title-bar string 
            WS_CHILD|WS_BORDER|WS_VSCROLL|WS_HSCROLL, // child window
            CW_USEDEFAULT,       // default horizontal position 
            CW_USEDEFAULT,       // default vertical position 
            rcClient.right,      // default width
            rcClient.bottom,     // default height 
            (HWND)parent_handle, // parent window or no owner if NULL
            (HMENU) NULL,        // use class menu 
            hInst,               // handle to application instance 
            (LPVOID) NULL);      // no window-creation data 
    }

    if (!hChild) 
        return NULL; 

    ShowWindow(hChild, SW_SHOW); 
    UpdateWindow(hChild);

    return hChild; 
} 

static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133],
            msg[133];

        sprintf_s(msg, "*** ERROR code %d at line %d in %s:\n+++ ",
            irc, line, file);
        UF_get_fail_message(irc, err);

        UF_print_syslog(msg, FALSE);
        UF_print_syslog(err, FALSE);
        UF_print_syslog("\n", FALSE);
        UF_print_syslog(call, FALSE);
        UF_print_syslog(";\n", FALSE);

        if (!UF_UI_open_listing_window())
        {
            UF_UI_write_listing_window(msg);
            UF_UI_write_listing_window(err);
            UF_UI_write_listing_window("\n");
            UF_UI_write_listing_window(call);
            UF_UI_write_listing_window(";\n");
        }
    }

    return(irc);
}

static BOOL Cls_OnCreate(HWND hwnd, CREATESTRUCT FAR *lpCreateStruct)
{
    WCHAR title[256];
    GetWindowText(hwnd, title, 256); 

    HINSTANCE hInst = CustomResourceBarTab::theInst;

    if (wcscmp(title, _T("Child")) == 0)
    {
        HWND hInsert = CreateWindow(_T("BUTTON"), _T("Insert Text"), WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 10, 140, 30, hwnd, (HMENU)NULL, hInst, NULL);    
        HWND hEdit = CreateWindow(_T("EDIT"), TEXT("Edit"), WS_BORDER|WS_CHILD|WS_VISIBLE|ES_AUTOHSCROLL|ES_AUTOVSCROLL,
            10, 45, 140, 30, hwnd, (HMENU)NULL, hInst, NULL);
        // create the combo box control.
        HWND hComboBox= CreateWindow(WC_COMBOBOX, TEXT("Combo"), CBS_DROPDOWN | CBS_HASSTRINGS | WS_CHILD | WS_OVERLAPPED | WS_VISIBLE | CBS_AUTOHSCROLL ,
            10,80,140,140, hwnd, (HMENU)NULL, hInst, NULL);

        // Load the combobox with item list.  
        TCHAR Planets[9][10] =  
        {
            TEXT("Mercury"), TEXT("Venus"), TEXT("Terra"), TEXT("Mars"), 
            TEXT("Jupiter"), TEXT("Saturn"), TEXT("Uranus"), TEXT("Neptune"), 
            TEXT("Pluto??") 
        };

        TCHAR A[16]; 
        int  k = 0; 
        memset(&A,0,sizeof(A));       
        for (k = 0; k <= 8; k += 1)
        {
            wcscpy_s(A, sizeof(A)/sizeof(TCHAR),  (TCHAR*)Planets[k]);

            // Add string to combobox.
            SendMessage(hComboBox,(UINT) CB_ADDSTRING,(WPARAM) 0,(LPARAM) A); 
        }

        // Send the CB_SETCURSEL message to display an initial item in the selection field  
        SendMessage(hComboBox, CB_SETCURSEL, (WPARAM)2, (LPARAM)0);

        LoadLibrary(TEXT("Riched20.dll"));
        HWND hwndEdit= CreateWindowEx(0, RICHEDIT_CLASS, TEXT("Type here"),
            ES_MULTILINE | WS_VISIBLE | WS_CHILD | WS_BORDER | WS_TABSTOP, 
            10, 115, 140, 140, hwnd, NULL, hInst, NULL);
    }
    else if (wcscmp(title, _T("Main")) == 0)
    {
        hAdd = CreateWindow(_T("BUTTON"), _T("Add New Tab"), WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 10, 180, 30, hwnd, (HMENU)NULL, hInst, NULL);
        hActivate = CreateWindow(_T("BUTTON"), _T("Activate New Tab"), WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 45, 180, 30, hwnd, (HMENU)NULL, hInst, NULL);
        hHide = CreateWindow(_T("BUTTON"), _T("Hide New Tab"), WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 80, 180, 30, hwnd, (HMENU)NULL, hInst, NULL);
        hShow = CreateWindow(_T("BUTTON"), _T("Show New Tab"), WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 115, 180, 30, hwnd, (HMENU)NULL, hInst, NULL);
        hRemove = CreateWindow(_T("BUTTON"), _T("Remove New Tab"), WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 150, 180, 30, hwnd, (HMENU)NULL, hInst, NULL);
    }

    return TRUE;
}

LRESULT CALLBACK WndProc(HWND hwnd,     // handle to window
                         UINT Message,  // message identifier
                         WPARAM wParam, // first message parameter
                         LPARAM lParam  // second message parameter
                         )
{
    switch (Message) 
    {
    case WM_CREATE :
        Cls_OnCreate(hwnd, NULL);
        break;
    case WM_DESTROY:
        break;
    case WM_PAINT:
        break;
    case WM_LBUTTONDOWN:
        break;
    case WM_CTLCOLOREDIT:
        break;
    case WM_MOUSEACTIVATE:
        break;
    case WM_SETCURSOR:
        break;
    case WM_CHILDACTIVATE:
        break;
    case WM_COMMAND:                                           
        {
            WCHAR wStr[256];
            HWND hControl = (HWND)lParam;

            // Button clicked in testing dialog
            if(HIWORD(wParam) == BN_CLICKED)            
            {
                GetWindowText(hControl, wStr, 256);
                if (wcscmp(wStr, L"Insert Text") == 0)
                {
                    HWND parent = GetParent(hControl);
                    HWND edit = FindWindowEx(parent, NULL, L"Edit", L"Edit");
                    // Apply button clicked
                    if (edit)
                        SetWindowText(edit, L"This is a Test"); 
                }

                if (hControl == hRemove)    
                {
                    // Remove last added tab
                    int tab_id = theCustomResourceBarTab->GetLastRegisteredID();

                    if (tab_id != 0)
                    {
                        int tab_num = theCustomResourceBarTab->GetRegisteredNumber(tab_id);

                        CustomResourceBarTab::theUI->ResourceBarManager()->Destroy(tab_id); 
                        theCustomResourceBarTab->RemoveRegisteredID(tab_num);
                        theCustomResourceBarTab->RemoveChildWindow(tab_id);
                    }
                }
                else if (hControl == hAdd)    
                {
                    // Add a new tab
                    tab_count++;
                    char title[256];
                    sprintf_s(title, "My Tab %d", tab_count);
                    int tab_id = CustomResourceBarTab::theUI->ResourceBarManager()->ResourceBarManager::Create(title, "computer");
                    // Register a callback
                    CustomResourceBarTab::theUI->ResourceBarManager()->ResourceBarManager::RegisterActivationCallback(tab_id, make_callback(theCustomResourceBarTab, &CustomResourceBarTab::ActivationHandler));
                    theCustomResourceBarTab->SetRegisteredID(tab_count, tab_id); 
                }
                else if (hControl == hShow)    
                {
                    // Show last added tab
                    int tab_id = theCustomResourceBarTab->GetLastRegisteredID();

                    if (tab_id != 0)
                        CustomResourceBarTab::theUI->ResourceBarManager()->SetTabVisibility(tab_id, true);
                } 
                else if (hControl == hHide)    
                {
                    // Hide last added tab
                    int tab_id = theCustomResourceBarTab->GetLastRegisteredID();

                    if (tab_id != 0)
                        CustomResourceBarTab::theUI->ResourceBarManager()->SetTabVisibility(tab_id, false);
                }
                else if (hControl == hActivate)
                {
                    // Activate last added tab
                    int tab_id = theCustomResourceBarTab->GetLastRegisteredID();
                    
                    if (tab_id != 0)
                        CustomResourceBarTab::theUI->ResourceBarManager()->ActivateTab(tab_id);
                }
            }
        } 
        break;
    } /* switch */

    return DefWindowProc(hwnd, Message, wParam, lParam);
}

/*****************************************************************************
**  Activation Methods
*****************************************************************************/
/*  Unigraphics Startup
**      This entry point activates the application at Unigraphics startup */
extern DllExport void ufsta( char *param, int *returnCode, int rlen )
{
    if( UF_CALL(UF_initialize()) ) 
    {
        /* Failed to initialize */
        return;
    }

    if (theCustomResourceBarTab == NULL)
        theCustomResourceBarTab = new CustomResourceBarTab();

    /* TODO: Add your application code here */
    BOOL init = theCustomResourceBarTab->InitApplication();
    if (init)
        init = theCustomResourceBarTab->InitInstance();

    /* Terminate the API environment */
    UF_CALL(UF_terminate());
}

/*****************************************************************************
**  Utilities
*****************************************************************************/

/* Unload Handler
**     This function specifies when to unload your application from Unigraphics.
**     If your application registers a callback (from a MenuScript item or a
**     User Defined Object for example), this function MUST return
**     "UF_UNLOAD_UG_TERMINATE". */
extern int ufusr_ask_unload( void )
{
    // Unload the library when the NX session terminates (UF_UNLOAD_UG_TERMINATE)
    return (int)Session::LibraryUnloadOptionAtTermination;
}

//------------------------------------------------------------------------------
// Method: ufusr_cleanup()
// You have the option of coding the cleanup routine to perform any housekeeping
// chores that may need to be performed. If you code the cleanup routine, it is
// automatically called by NX.
//------------------------------------------------------------------------------
extern void ufusr_cleanup(void)
{
    try
    {
        //---- Enter your callback code here -----
        char msg[256];
        // Open the Print the Information window and print the message.
        CustomResourceBarTab::listW->Open();
        sprintf_s(msg, "ufusr clean up");
        CustomResourceBarTab::listW->WriteLine(msg);

        if (theCustomResourceBarTab != NULL)
        {            
            for(CustomResourceBarTab::StlRegisteredTabMap::const_iterator it = CustomResourceBarTab::g_TabMap.begin(); it != CustomResourceBarTab::g_TabMap.end(); ++it)
            {
                int num = it->first;
                int tab_id = it->second;

                if (tab_id > 0)
                    CustomResourceBarTab::theUI->ResourceBarManager()->Destroy(tab_id);
            }

            delete theCustomResourceBarTab;
            theCustomResourceBarTab = NULL;
        }
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }
}

