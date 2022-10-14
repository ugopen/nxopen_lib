'----------------------------------------------------------------------------
'                  Copyright (c) 2007 Siemens
'                      All rights reserved
'----------------------------------------------------------------------------
' 
'
' MenuBarVbApp.vb
'
' Description:
'   This is a an example of adding a VB application to NX.
'   In addition to using this source file there are two menu files 
'   (MenuBarDotNetAppButton.men and MenuBarVbApp.men) which are also required.
'   All of the files for this sample reside in the ugopen kit under:
'   SampleNXOpenApplications/.NET/MenuBarDotNetApp.
'
'   Please see the "Adding Custom Applications to NX" chapter of the
'   NX Open Programmer's Guide or search the documentation for
'   "MenuBarDotNetApp" for a detailed description of this example.
'
'   These files are intended to provide a template that can be modified
'   by renaming the files, and renaming the variables and routines
'   to allow you create your own application.
'
'   Additional information on MenuScript can be found in:
'   Additional information on MenuScript can be found in:
'     - the MenuScript User's Guide
'     - the NXOpen Programmer's Guide
'     - the NX Open for .NET Reference Guide (see MenuBar)
'     - any other place in the NX documentation that comes up when
'       you search for "MenuScript" or "MenuBar"
'
'   *** PLEASE NOTE ***
'   The shared library created from this program must be placed in the
'   "application" directory under a directory listed in the file pointed to by the
'   environment variable in UGII_CUSTOM_DIRECTORY_FILE (i.e. the shared library must
'   not be in the "startup" directory).
'
'----------------------------------------------------------------------------
Option Strict Off

Imports NXOpen
Imports NXOpen.UI
Imports NXOpen.Utilities

'------------------------------------------------------------
'
'  Module MyProject
'
'      Used to demo registration and use of a button's 
'      action callback.
'------------------------------------------------------------
Module MyProject
    Dim theUI As UI = GetUI()
    Dim theSession As Session = Session.GetSession
    Dim lw As ListingWindow = theSession.ListingWindow



    '------------------------------------------------------------------------------
    ' Callback Name: ApplicationInit
    '    Executed when the application is entered.  
    '    It's used to initialize the application's data.
    '
    '    Prints a note to the listing window.
    '------------------------------------------------------------------------------
    Public Function ApplicationInit() As Integer
        ' ---- Enter your callback code here -----
        lw.Open()
        lw.WriteLine(" ")
        lw.WriteLine("Inside My VB Init Callback")
        lw.WriteLine(" ")
        ApplicationInit = 0
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: ApplicationEnter
    '    Executed when the application is selected 
    '    (activated) from the pulldown menu.  
    '    If this is the first time entering the application,
    '    the ApplicationInit callback will get called first to
    '    initialize any data required by this callback.
    '
    '    Prints a note to the listing window.
    '------------------------------------------------------------------------------
    Public Function ApplicationEnter() As Integer
        ' ---- Enter your callback code here -----
        lw.Open()
        lw.WriteLine(" ")
        lw.WriteLine("Inside My VB Enter Callback")
        lw.WriteLine(" ")
        ApplicationEnter = 0
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: ApplicationExit
    '    Executed when the application is exited.  
    '    It's used to free (clean up) the application's data.
    '
    '    Prints a note to the listing window.
    '------------------------------------------------------------------------------
    Public Function ApplicationExit() As Integer
        ' ---- Enter your callback code here -----
        lw.Open()
        lw.WriteLine(" ")
        lw.WriteLine("Inside My VB Exit Callback")
        lw.WriteLine(" ")
        ApplicationExit = 0
    End Function
    
    '------------------------------------------------------------------------------
    ' Callback Name: PrintButtonIdCB
    '   This is a callback method associated with SAMPLE_CSHARP_APP__action1 action button.
    '   This will get executed whenever 'Print Button ID' is selected from the
    '   'Sample C Sharp' menu.
    '   Given a button name (such as SAMPLE_CSHARP_APP_BUTTON1) from the user, the
    '   input button's id gets printed to the listing window.
    '------------------------------------------------------------------------------
    Public Function PrintButtonIdCB(ByVal buttonEvent As NXOpen.MenuBar.MenuButtonEvent) As NXOpen.MenuBar.MenuBarManager.CallbackStatus
        ' ---- Enter your callback code here -----
        lw.Open()
        lw.WriteLine(" ")
        lw.WriteLine("Inside PrintButtonIdCB Callback:")
        Dim buttonName As String


        buttonName = buttonEvent.ActiveButton.ButtonName
        buttonName = InputBox( "Enter name of button you wish to query", "Print Button Id", buttonName)
        
        Dim myButton As MenuBar.MenuButton
        myButton = theUI.MenuBarManager.GetButtonFromName(buttonName)
        If myButton Is Nothing
            lw.WriteLine("    " & buttonName & " button not found")
        Else
            lw.WriteLine("    Button Id for " & buttonName & ": " & myButton.ButtonId)
        End If
        lw.WriteLine(" ")
        PrintButtonIdCB = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: TestCallbackReturnsCB
    '   This is a callback method associated with SAMPLE_CSHARP_APP__action2 action button.
    '   This will get executed whenever 'Test Callback Returns' is selected from the
    '   'Sample C Sharp' menu.
    '   Prompts the user for a number between 0-4.
    '   Tests the return value specified by the user, and prints a note to the
    '   listing window stating which return value was used.    
    '------------------------------------------------------------------------------
    Public Function TestCallbackReturnsCB(ByVal buttonEvent As NXOpen.MenuBar.MenuButtonEvent) As NXOpen.MenuBar.MenuBarManager.CallbackStatus
        ' ---- Enter your callback code here -----
        Dim status As NXOpen.MenuBar.MenuBarManager.CallbackStatus
        status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue
        
        lw.Open()
        lw.WriteLine(" ")
        lw.WriteLine("Inside TestCallbackReturnsCB Callback:")
        
        Dim returnVal As Integer
        returnVal = 0
        returnVal = InputBox("Enter a number between 0 and 4", "Test Callback Returns", returnVal)
        If returnVal = 0
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue")
        Else If returnVal = 1
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Cancel
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.Cancel")
        Else If returnVal = 2
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.OverrideStandard
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.OverrideStandard")
        Else If returnVal = 3
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Warning
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.Warning")
        Else If returnVal = 4
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Error
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.Error")
        Else
            lw.WriteLine("    Invalid Input: must be an integer between 0 and 4")
        End If
        lw.WriteLine(" ")

        TestCallbackReturnsCB = status
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: PrintApplicationIdCB
    '   This is a callback method associated with SAMPLE_CSHARP_APP__action3 action button.
    '   This will get executed whenever 'Print Application ID' is selected from the
    '   'Sample C Sharp' menu.
    '   Prints the application id of the active button.
    '------------------------------------------------------------------------------
    Public Function PrintApplicationIdCB(ByVal buttonEvent As NXOpen.MenuBar.MenuButtonEvent) As NXOpen.MenuBar.MenuBarManager.CallbackStatus
        ' ---- Enter your callback code here -----
        lw.Open()
        lw.WriteLine(" ")
        lw.WriteLine("Inside PrintApplicationIdCB Callback:")
        lw.WriteLine( "    Application Id: " & buttonEvent.ApplicationId )
        lw.WriteLine(" ")

        PrintApplicationIdCB = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: PrintButtonDataCB
    '   This is a callback method associated with SAMPLE_CSHARP_APP__action4 action button.
    '   This will get executed whenever 'Print This Button Data' is selected from the
    '   'Sample C Sharp' menu.
    '   It will print lots of info about the button to the listing window.
    '------------------------------------------------------------------------------
    Public Function PrintButtonDataCB(ByVal buttonEvent As NXOpen.MenuBar.MenuButtonEvent) As NXOpen.MenuBar.MenuBarManager.CallbackStatus
        ' ---- Enter your callback code here -----
        lw.Open()
        lw.WriteLine(" ")
        lw.WriteLine("Inside PrintButtonDataCB Callback:")
    
        lw.WriteLine("    Button Id: " & buttonEvent.ActiveButton.ButtonId )
        lw.WriteLine("    Name: " & buttonEvent.ActiveButton.ButtonName)
        lw.WriteLine("    Button type name: " & buttonEvent.ActiveButton.ButtonTypeName)
        lw.WriteLine("    Menubar Name: " & buttonEvent.MenuBarName)
        lw.WriteLine("    Application Id: " & buttonEvent.ApplicationId )
        Dim ancestors As String()
        ancestors = buttonEvent.GetMenuAncestors()
        Dim temp_str As String
        Dim counter As Integer
        counter = 0
        For Each temp_str In ancestors
            lw.WriteLine("    Ancestor[" & counter & "]: " & temp_str)
            counter = counter + 1
        Next
        lw.WriteLine(" ")

        PrintButtonDataCB = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: PrintToggleStatusCB
    '   This is a callback method associated with SAMPLE_CSHARP_APP__action5 action button.
    '   This will get executed whenever 'Print This Button Data' is selected from the
    '   'Sample C Sharp' menu.
    '   It will print the current status of the toggle
    '------------------------------------------------------------------------------
    Public Function PrintToggleStatusCB(ByVal buttonEvent As NXOpen.MenuBar.MenuButtonEvent) As NXOpen.MenuBar.MenuBarManager.CallbackStatus
        ' ---- Enter your callback code here -----
        lw.Open()
        lw.WriteLine(" ")
        lw.WriteLine("Inside PrintToggleStatusCB Callback:")
        If buttonEvent.ActiveButton.ToggleStatus = MenuBar.MenuButton.Toggle.On Then
            lw.WriteLine("   The toggle is now ON")
        Else
            lw.WriteLine("   The toggle is now OFF")
        End If
    
        lw.WriteLine(" ")
        PrintToggleStatusCB = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue
    End Function
    
    '------------------------------------------------------------------------------
    ' Called when NX starts up and registers the action callbacks for the application
    '------------------------------------------------------------------------------
    Public Function Startup() As Integer
        theUI.MenuBarManager.RegisterApplication("SAMPLE_VB_APP", AddressOf ApplicationInit, AddressOf ApplicationEnter, AddressOf ApplicationExit, True, True, True)
        theUI.MenuBarManager.AddMenuAction("SAMPLE_VB_APP__action1", AddressOf PrintButtonIdCB)
        theUI.MenuBarManager.AddMenuAction("SAMPLE_VB_APP__action2", AddressOf TestCallbackReturnsCB)
        theUI.MenuBarManager.AddMenuAction("SAMPLE_VB_APP__action3", AddressOf PrintApplicationIdCB)
        theUI.MenuBarManager.AddMenuAction("SAMPLE_VB_APP__action4", AddressOf PrintButtonDataCB)
        theUI.MenuBarManager.AddMenuAction("SAMPLE_VB_APP__action5", AddressOf PrintToggleStatusCB)
        Startup = 0
    End Function ' Startup ends


    '------------------------------------------------------------
    '
    '  GetUnloadOption()
    '
    '     Used to tell NX when to unload this library
    '
    '     Available options include:
    '       Session.LibraryUnloadOption.Immediately
    '       Session.LibraryUnloadOption.Explicitly
    '       Session.LibraryUnloadOption.AtTermination
    '
    '     Any programs that register callbacks must use 
    '     AtTermination as the unload option.
    '------------------------------------------------------------
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = Session.LibraryUnloadOption.AtTermination
    End Function



End Module

