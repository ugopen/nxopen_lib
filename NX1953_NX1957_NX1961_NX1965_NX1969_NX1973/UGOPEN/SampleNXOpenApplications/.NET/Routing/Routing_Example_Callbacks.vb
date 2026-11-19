'===================================================================================================
'               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
'===================================================================================================
'
'    NOTE:  NX Development provides programming examples for illustration only.
'    NX Development assumes you are familiar with the programming language
'    demonstrated in these examples, and the tools used to create and debug NX/Open
'    programs. GTAC support professionals can help explain the functionality of
'    a particular procedure, but neither GTAC nor NX Development will modify
'    these examples to provide added functionality or construction procedures.
'
'File description:
'
'    A Visual Basic module that implements example Routing callbacks.
'
'
'===================================================================================================
Option Strict On
Imports System
Imports NXOpen
Imports NXOpen.Routing
Imports NXOpen.Routing.Electrical
Imports NXOpen.Routing.CustomManager

Module Callbacks

    Dim theSession As Session = Nothing
    Dim listingWindow As ListingWindow = Nothing

    '-----------------------------------------------------------------------------------------------
    ' Called when NX starts up to register the callbacks.
    Function Startup(ByVal args As String()) As Integer

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If listingWindow Is Nothing Then
            listingWindow = theSession.ListingWindow
        End If

        RegisterCallbacks()

        Startup = 0
    End Function

    '------------------------------------------------------------------------------------------
    ' Called from File->Execute->NX Open. Useful for testing.
    Sub Main()

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If listingWindow Is Nothing Then
            listingWindow = theSession.ListingWindow
        End If

        RegisterCallbacks()
    End Sub

    '------------------------------------------------------------------------------------------
    ' Called by both Main And Startup to register the callbacks.
    Sub RegisterCallbacks()

        Dim customManager As CustomManager = theSession.RouteCustomManager()

        customManager.AddCallback(CallbackReason.WireRouteAuto, AddressOf AutorouteCallback)
        customManager.AddCallback(CallbackReason.WireUnroute, AddressOf UnrouteCallback)

    End Sub

    '-----------------------------------------------------------------------------------------------
    Sub AutorouteCallback(ByVal nxObjects As NXObject())
        Echo(vbCrLf + "*** AutorouteCallback called with " + nxObjects.Length.ToString() + " objects.")

        For Each nxObject As NXObject In nxObjects
            If Not TypeOf nxObject Is WireDevice Then
                Echo("  NX Object (Tag " + nxObject.Tag.ToString() + ") is NOT a Wire Device.")
                Continue For
            End If

            Dim wireDevice As WireDevice = CType(nxObject, WireDevice)

            Echo("  Wire Device (Tag " + wireDevice.Tag.ToString() + ") named " + wireDevice.Name + ".")
        Next

        Echo(vbCrLf)

    End Sub

    '-----------------------------------------------------------------------------------------------
    Sub UnrouteCallback(ByVal nxObjects As NXObject())
        Echo(vbCrLf + "*** UnrouteCallback called with " + nxObjects.Length.ToString() + " objects.")

        For Each nxObject As NXObject In nxObjects
            If Not TypeOf nxObject Is WireDevice Then
                Echo("  NX Object (Tag " + nxObject.Tag.ToString() + ") is NOT a Wire Device.")
                Continue For
            End If

            Dim wireDevice As WireDevice = CType(nxObject, WireDevice)

            Echo("  Wire Device (Tag " + wireDevice.Tag.ToString() + ") named " + wireDevice.Name + ".")
        Next

        Echo(vbCrLf)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Writes the given string to the Listing Window and the syslog.
    '
    ' \param[in]
    '      stringToWrite
    '          The string to write.
    Sub Echo(ByVal stringToWrite As String)

        If Not listingWindow.IsOpen Then
            listingWindow.Open()
        End If

        listingWindow.WriteFullline(stringToWrite)

        Dim syslog As LogFile = Session.GetSession().LogFile
        syslog.WriteLine(stringToWrite)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Tells NX when to unload your application.
    ' For Routing callbacks, plugins, And Design Rules, this MUST return AtTermination.
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module
