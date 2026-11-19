'===================================================================================================
'
'        Copyright (c) 2018 Siemens Product Lifecycle Management Software Inc. 
'                            All Rights Reserved.
'
'===================================================================================================
'
'
'    Code Description:
'
'    A simple NX Open VB application program that prints the full version number Of installed 
'    Siemens NX software in the system log file And the listing window. If the messages are
'    successfully printed, then NX Open software automation setup is validated.
'===================================================================================================
'
'    Note:
'
'    NX Development provides programming examples for illustration only.
'    NX Development assumes you are familiar with the programming language
'    demonstrated tn these examples, and the tools used to create and debug NX/Open
'    programs. GTAC support professionals can help explain the functionality Of
'    a particular procedure, but neither GTAC nor NX Development will modify
'    these examples to provide added functionality Or construction procedures.
'===================================================================================================

Imports System
Imports NXOpen

Module NXJournal
    Sub Main(ByVal args() As String)

        ' Get the session
        Dim theSession As NXOpen.Session = NXOpen.Session.GetSession( )

        ' Get the listing window for this session
        Dim listingWindow As NXOpen.ListingWindow = theSession.ListingWindow( )

        ' Open the listing window
        listingWindow.Open( )

        Dim logFile As NXOpen.LogFile = theSession.LogFile( )

        ' Get the name of the system log file
        Dim logFileName As String = logFile.FileName( )

        ' Write a line to the listing window
        listingWindow.WriteLine( "Log File Name: " + logFileName + " created." )

        ' Get the full version name of the installed Siemens NX
        Dim NXFullVersion As String = theSession.GetEnvironmentVariableValue( "NX_FULL_VERSION" )

        If Not String.IsNullOrEmpty( NXFullVersion ) Then

            ' Write a string to the system log file
            logFile.WriteLine( "NX Open software automation setup is validated for release: " + NXFullVersion + "." )

            ' Write a line to the listing window
            listingWindow.WriteFullline( "NX Open software automation setup is validated for release: " + NXFullVersion + "." )

        Else

            ' Write a string to the system log file
            logFile.WriteLine( "Siemens NX installation not verified." )

            ' Write a line to the listing window
            listingWindow.WriteFullline( "Siemens NX installation not verified." )
        End If

        ' Close the stream to the listing window.
        listingWindow.Close( )

        ' ----------------------------------------------
        '   Menu: Tools->Journal->Stop Recording
        ' ----------------------------------------------

    End Sub
End Module
