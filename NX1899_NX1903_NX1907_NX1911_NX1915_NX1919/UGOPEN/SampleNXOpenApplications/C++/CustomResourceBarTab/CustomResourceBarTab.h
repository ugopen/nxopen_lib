//----------------------------------------------------------------------------
//   Copyright (c) 2014 Siemens Product Lifecycle Management Software Inc.
//                         All rights reserved
//----------------------------------------------------------------------------
// 
//
// CustomResourceBarTab.h
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

#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/ListingWindow.hxx>

#include <afxwin.h>
#include <WinUser.h>
#include <map>
#include <RichEdit.h>

using namespace std;
using namespace NXOpen;



class CustomResourceBarTab
{
public:

    static Session* theSession;
    static UI* theUI;
    static ListingWindow* listW;
    static HINSTANCE theInst;
    
    typedef std::map<int, int> StlRegisteredTabMap;
    static StlRegisteredTabMap g_TabMap;
    
    typedef std::map<int, HWND> StlChildWindowMap;
    static StlChildWindowMap g_ChildMap;

    CustomResourceBarTab();
    ~CustomResourceBarTab();

    BOOL InitApplication();
    BOOL InitInstance();
    HWND CreateChildWindow(HWND parent_handle);
    int ActivationHandler(int tab_id);

    int GetRegisteredID(int id) const {return g_TabMap[id];}
    void SetRegisteredID(int id, int tab_id) {g_TabMap[id] = tab_id;}
    void RemoveRegisteredID(int id) {g_TabMap.erase(id);}
    int GetLastRegisteredID() const;
    int GetRegisteredNumber(int tab_id) const;

    HWND GetChildWindow(int id) const {return g_ChildMap[id];}
    void SetChildWindow(int id, HWND handle) {g_ChildMap[id] = handle;}
    void RemoveChildWindow(int id) {g_ChildMap.erase(id);}
};


