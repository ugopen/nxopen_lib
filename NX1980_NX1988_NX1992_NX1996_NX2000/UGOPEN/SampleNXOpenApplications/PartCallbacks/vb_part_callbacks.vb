'----------------------------------------------------------------------------
'                  Copyright (c) 2007 UGS Corp.
'                      All rights reserved
'-----------------------------------------------------------------------------
' 
'
'  vb_part_callbacks.vb
' 
'  Description:
'      This simple demo registers part callbacks for every available reason
'      via the Visual Basic .Net language.
'      After compiling and linking this demo program, the output library needs
'      to be placed in a folder called startup (for example c:\user_dir\startup).
'      Also the UGII_USER_DIR enviornment variable needs to point to the startup
'      directory's parent folder (for example: UGII_USER_DIR=c:\user_dir).
'      Once you have the startup directory and user dir environment variable
'      set up, start NX.  The part callbacks will be registered at startup.
'      Now anytime you create new, open, save, save as, close, modify, rename,
'      or change the workpart your part callbacks will be executed.
' 
'      To demo all of the available part callbacks at runtime - compile and link
'      execute_all_part_callbacks.c.
'      Then start NX and go to File->Execute->NX Open and select your compiled
'      execute_all_callbacks program.
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
'      Demo class used to register all available part callbacks
'------------------------------------------------------------
Module MyProject

    '-----------------------------------------------------
    ' Used to tell us if we've already registered our callbacks
    '-----------------------------------------------------
    Dim registered As Integer = 0

    '-----------------------------------------------------
    ' The ids of the registered callbacks are used if
    ' you ever want to unregister a callback.
    ' If you plan to register the callback once for
    ' the enitre session, and don't intend to remove them,
    ' (recommended) tracking the id may not be necessary.
    '-----------------------------------------------------
    Dim idPartCreated1 As Integer = 0
    Dim idPartOpened1 As Integer = 0
    Dim idPartSaved1 As Integer = 0
    Dim idPartSavedAs1 As Integer = 0
    Dim idPartClosed1 As Integer = 0
    Dim idPartModified1 As Integer = 0
    Dim idPartRenamed1 As Integer = 0
    Dim idWorkPartChanged1 As Integer = 0
    Dim theSession As Session = Session.GetSession()
    Dim lw As ListingWindow = theSession.ListingWindow

    '-----------------------------------
    ' Called when a new part is created
    ' Prints the name of the created part
    ' to the listing window
    '-----------------------------------
    Sub PartCreated1(ByVal p As BasePart)
        lw.Open()
        lw.WriteLine("    VB created: " & p.FullPath)
        'MsgBox("created1: " & p.FullPath, MsgBoxStyle.OkOnly)
    End Sub

    '-----------------------------------
    ' Called when a part is opened
    ' Prints the name of the opened part
    ' to the listing window
    '-----------------------------------
    Sub PartOpened1(ByVal p As BasePart)
        lw.Open()
        lw.WriteLine("    VB opened: " & p.FullPath)
    End Sub

    '-----------------------------------
    ' Called when a part is saved
    ' Prints the name of the saved part
    ' to the listing window
    '-----------------------------------
    Sub PartSaved1(ByVal p As BasePart)
        lw.Open()
        lw.WriteLine("    VB saved: " & p.FullPath)
    End Sub

    '-----------------------------------
    ' Called when a part is saved as
    ' Prints the name of the saved as part
    ' to the listing window
    '-----------------------------------
    Sub PartSavedAs1(ByVal p As BasePart)
        lw.Open()
        lw.WriteLine("    VB saved as: " & p.FullPath)
    End Sub

    '-----------------------------------
    ' Called when a part is closed
    ' Prints the name of the closed part
    ' to the listing window
    '-----------------------------------
    Sub PartClosed1(ByVal p As BasePart)
        lw.Open()
        lw.WriteLine("    VB closed: " & p.FullPath)
    End Sub

    '-----------------------------------
    ' Called when a part is modified
    ' (for the first time)
    ' Prints the name of the modified part
    ' to the listing window
    '-----------------------------------
    Sub PartModified1(ByVal p As BasePart)
        lw.Open()
        lw.WriteLine("    VB modified: " & p.FullPath)
    End Sub

    '-----------------------------------
    ' Called when a part is renamed
    ' Prints the name of the renamed part
    ' to the listing window
    '-----------------------------------
    Sub PartRenamed1(ByVal p As BasePart)
        lw.Open()
        lw.WriteLine("    VB renamed: " & p.FullPath)
    End Sub

    '-----------------------------------
    ' Called when the workpart changes
    ' Prints the name of old workpart and
    ' new workpart to the listing window
    '-----------------------------------
    Sub WorkPartChanged1(ByVal p As BasePart)
        lw.Open()
        lw.WriteLine("    VB work part changed")

        If p Is Nothing Then
            lw.WriteLine("        Old Work Part: NULL")
        Else
            lw.WriteLine("        Old Work Part: " & p.FullPath)
        End If
        If theSession.Parts.Work Is Nothing Then
            lw.WriteLine("        New Work Part: NULL")
        Else
            lw.WriteLine("        New Work Part: " & theSession.Parts.Work.FullPath)
        End If

    End Sub

    '-----------------------------------------------------
    ' Called when NX starts up
    ' registers the part callbacks with NX
    '-----------------------------------------------------
    Public Function Startup() As Integer
        Dim theUI As UI = UI.GetUI()

        If registered = 0 Then
            'MsgBox("Registering callbacks", MsgBoxStyle.OkOnly)
            idPartCreated1 = theSession.Parts.AddPartCreatedHandler(AddressOf PartCreated1)
            idPartOpened1 = theSession.Parts.AddPartOpenedHandler(AddressOf PartOpened1)
            idPartSaved1 = theSession.Parts.AddPartSavedHandler(AddressOf PartSaved1)
            idPartSavedAs1 = theSession.Parts.AddPartSavedAsHandler(AddressOf PartSavedAs1)
            idPartClosed1 = theSession.Parts.AddPartClosedHandler(AddressOf PartClosed1)
            idPartModified1 = theSession.Parts.AddPartModifiedHandler(AddressOf PartModified1)
            idPartRenamed1 = theSession.Parts.AddPartRenamedHandler(AddressOf PartRenamed1)
            idWorkPartChanged1 = theSession.Parts.AddWorkPartChangedHandler(AddressOf WorkPartChanged1)

            registered = 1
        End If

        Startup = 0

    End Function ' Startup ends

    '------------------------------------------------------------
    '
    '  Main()
    '
    '      Called manually from File->Execute->NX Open
    '
    '------------------------------------------------------------
    Sub Main()

        'Add your code here
        If registered = 0 Then
            MsgBox("Registering VB callbacks", MsgBoxStyle.OkOnly)
            Startup()
        End If

    End Sub

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

