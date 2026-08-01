'----------------------------------------------------------------------------
'   Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
'                         All rights reserved
'----------------------------------------------------------------------------
' 
'
' ConfigureContextMenu.vb
'
' Description:
'   This is a an example of customizing context menus in NX.
'   All of the files for this sample reside in the ugopen kit under:
'   SampleNXOpenApplications/DotNET/ConfigureContextMenu/.
'
'   These files are intended to provide a template that can be modified
'   by renaming the files, and renaming the variables and routines
'   to allow you create your own customization.
'
'   *** PLEASE NOTE ***
'   The shared library created from this program must be placed in the
'   "startup" directory under a directory listed in the file pointed to by the
'   environment variable in UGII_CUSTOM_DIRECTORY_FILE.
'
'----------------------------------------------------------------------------
Option Strict Off
    
Imports NXOpen
Imports NXOpen.UI
Imports NXOpen.UF

'------------------------------------------------------------
'  Module ConfigureContextMenu
'
'      Used to demo registration and use of the context
'      menu customization callback.
'------------------------------------------------------------
Module ConfigureContextMenu
    Dim theUI As UI = GetUI()
    Dim theSession As Session = Session.GetSession
    Dim lw As ListingWindow = theSession.ListingWindow
    Dim theUFSession As NXOpen.UF.UFSession = UFSession.GetUFSession

    '------------------------------------------------------------------------------
    ' Callback Name: CustomizeMenu
    '    Executed when a customizable context menu is about to be displayed.  
    '------------------------------------------------------------------------------
    Public Function CustomizeMenu(ByVal menu As NXOpen.MenuBar.ContextMenu,
                                  ByVal props As NXOpen.MenuBar.ContextMenuProperties) As Integer

        ' When in the Modeling application, hide the Delete button in the Graphics Window Context menu.
        Dim moduleId As Integer
        theUFSession.UF.AskApplicationModule(moduleId)
        If moduleId = UFConstants.UF_APP_MODELING And props.Location = "GraphicsWindow" Then
            If menu.HasEntryWithName("UG_EDIT_DELETE")
                Dim deleteMenuEntry = menu.GetEntryWithName("UG_EDIT_DELETE")
                menu.HideEntry(deleteMenuEntry)
            End If
        End If

        ' Find the last visible push-button entry on the menu
        Dim entry As NXOpen.MenuBar.ContextMenuEntry = Nothing
        
        For index = 0 To menu.NumberOfEntries - 1
            Dim entry2 As NXOpen.MenuBar.ContextMenuEntry = menu.GetEntry(index)

            ' Identify the last menu entry which is something that can be
            ' activated and which is visible and sensitive.
            If entry2.EntryType = NXOpen.MenuBar.ContextMenuEntry.Type.PushButton And
                Not entry2.IsHidden And entry2.IsSensitive Then
                entry = entry2
            End If
        Next

        ' Set identified entry as the default and move to the top of the menu.
        If Not IsNothing(entry) Then
            menu.SetDefaultEntry(entry)
            menu.MoveEntry(entry, 0)
        End If

        ' Add an additional menu button for a specific context.
        If props.Context = "Features.Cylinder" Then
            ' Retrieve an NX menu button
            Dim newButton As NXOpen.MenuBar.MenuButton = theUI.MenuBarManager.GetButtonFromName("UG_PREFERENCES_VISUALIZATION")

            Dim subMenu As NXOpen.MenuBar.ContextMenu = menu.AddSubmenu("Custom", -1)
            subMenu.AddMenuButton(newButton, -1)
        End If

        ' Add a label to identify the context menu for Features Cylinder.
        If props.Context = "Features.Cylinder" Then
            menu.AddMenuLabel("Features Cylinder", 0)
        End If

        lw.Open()
        lw.WriteLine("Customize menu for " + props.Context + " in " + props.Location)
        PrintMenu(menu, props, "   ")

        CustomizeMenu = 0
    End Function


    '------------------------------------------------------------------------------
    ' Function PrintMenu
    '    Prints a note and a description of the menu to the listing window.
    '------------------------------------------------------------------------------
    
    Public Sub PrintMenu(ByVal menu As NXOpen.MenuBar.ContextMenu,
                              ByVal props As NXOpen.MenuBar.ContextMenuProperties,
                              ByVal prefix As String)

        For index = 0 To menu.NumberOfEntries - 1
            Dim entry As NXOpen.MenuBar.ContextMenuEntry
            entry = menu.GetEntry(index)
            If entry.EntryType = NXOpen.MenuBar.ContextMenuEntry.Type.Separator Then
                lw.WriteLine(prefix & index & " = ---------------")
            Else
                lw.WriteLine(prefix & index & " = " & entry.Label)
            End If

            If entry.EntryType = NXOpen.MenuBar.ContextMenuEntry.Type.Submenu Then
                PrintMenu(menu.GetSubmenu(index), props, prefix & "  ")
            End If
        Next index

    End Sub

    '------------------------------------------------------------------------------
    ' Called when NX starts up and registers the customize callback for the context 
    ' menu
    '------------------------------------------------------------------------------
    Public Function Startup() As Integer
        theUI.MenuBarManager.RegisterConfigureContextMenuCallback(
                "ConfigureContextMenu.vb", 
                "An example of context menu customization demonstrating various functions.",
                AddressOf CustomizeMenu)
        Startup = 0
    End Function


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

