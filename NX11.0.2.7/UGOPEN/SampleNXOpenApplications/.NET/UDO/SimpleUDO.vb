'=============================================================================
'
'                   Copyright (c) 2012 Siemens PLM Solutions
'                    Unpublished - All rights reserved
'===============================================================================
' This program creates a very simple UDO example. 
' 
' It demonstrates each of the following callbacks: 
' * Display 
' * Selection 
' * Attention Point 
' * Fit 
' * Edit 
' * Information 
' 
' In NX execute this program via: File -> Execute -> NX Open... 
' This program begins by opening a new part (if there were no open parts). 
' Next it will prompt you to select a position on the screen. 
' The screen position will be used as a reference point for the UDO. 
' The UDO will display as a triangle on that point with a name 
' "VB .Net UDO" next to the triangle. 
' 
' This UDO is selectable. If you go to Information->Object and select 
' the UDO you will see custom information output to the listing window from 
' the function myInfoCB defined in this program. 
' 
' You can also edit the location of the UDO. Start by right-clicking 
' on the UDO and selecting "Edit User Defined Object" from the MB3 popup menu. 
' Editing the UDO will invoke the myEditCB function defined in this program. 
' You will be prompted to select a new screen position, and after you make 
' the selection the UDO will move to the new location. 
' 
' This example has limitation that it can be run only once in NX session as journal.
' If we run it twice consecutively, it will raise an error in the second run.
' Because it is going to register same class which is registered 
' in previous journal run. If you want to run the journal multiple 
' times in the same session then you need to change the class name or you can create a dll
' and load it multiple times.
'=============================================================================
'
'=============================================================================

Option Strict Off
Imports System
Imports NXOpen
Imports NXOpenUI
Imports NXOpen.UF

Module Module1
    Dim theSession As Session = Nothing
    Dim theUI As UI = Nothing
    Dim theUFSession As UFSession = Nothing
    Dim myUDOclass As UserDefinedObjects.UserDefinedClass = Nothing
    '------------------------------------------------------------------------------ 
    ' Callback Name: myDisplayCB 
    ' This is a callback method associated with displaying a UDO. 
    ' This same callback is registered for display, select, fit, and attention point 
    '------------------------------------------------------------------------------ 

    Public Function myDisplayCB(ByVal displayEvent As UserDefinedObjects.UserDefinedDisplayEvent) As Integer

        Try
            ' Get the doubles used to define the selected screen position for this UDO. 
            Dim myUDOdoubles() As Double = displayEvent.UserDefinedObject.GetDoubles()

            ' Use the doubles to define points of a triangle 
            Dim myPoints(3) As Point3d
            myPoints(0).X = myUDOdoubles(0) + 0
            myPoints(0).Y = myUDOdoubles(1) + 0
            myPoints(0).Z = myUDOdoubles(2) + 0

            myPoints(1).X = myUDOdoubles(0) + 100
            myPoints(1).Y = myUDOdoubles(1) + 0
            myPoints(1).Z = myUDOdoubles(2) + 0

            myPoints(2).X = myUDOdoubles(0) + 0
            myPoints(2).Y = myUDOdoubles(1) + 100
            myPoints(2).Z = myUDOdoubles(2) + 0

            myPoints(3).X = myUDOdoubles(0) + 0
            myPoints(3).Y = myUDOdoubles(1) + 0
            myPoints(3).Z = myUDOdoubles(2) + 0

            ' Display the triangle 
            displayEvent.DisplayContext.DisplayPolyline(myPoints)

            ' Display the text next to the triangle 
            Dim myPt As Point3d
            myPt.X = myUDOdoubles(0) + 100
            myPt.Y = myUDOdoubles(1) + 0
            myPt.Z = myUDOdoubles(2) + 0
            displayEvent.DisplayContext.DisplayText("VB .Net UDO", myPt, 0)
        Catch ex As NXException
            ' the display/selection/fit/attention callback is called so many times 
            ' that it's best to print this error handling stuff in the syslog 
            ' any interactive messages in the UI would drive the user crazy ;) 
            theUfSession.UF.PrintSyslog("Caught Exception in myDisplayCB: '" & ex.Message() & "'" & vbCrLf, False)
        End Try

        myDisplayCB = 0
    End Function

    '------------------------------------------------------------------------------ 

    ' Callback Name: myEditCB 
    ' This is a callback method associated with editing a UDO. 
    '------------------------------------------------------------------------------ 

    Public Function myEditCB(ByVal editEvent As UserDefinedObjects.UserDefinedEvent) As Integer
        Try
            Dim myView As NXOpen.View = Nothing
            Dim myCursor As Point3d
            myCursor.X = 0
            myCursor.Y = 0
            myCursor.Z = 0

            ' highlight the current udo we are about to edit 
            ' this is helpful if multiple udo's were on the selection 
            ' list when the user decided to edit them 
            editEvent.UserDefinedObject.Highlight()

            ' ask the user to select a new origin for this UDO 
            Dim myResponse As Selection.DialogResponse = theUI.SelectionManager.SelectScreenPosition("Select New Origin for VB UDO", myView, myCursor)
            ' we are done asking the user for input... unhighlight the udo
            editEvent.UserDefinedObject.Unhighlight()
            ' use the new screen position (if the user picked one) 
            If myResponse = Selection.DialogResponse.Pick Then
                Dim myUDOdoubles(3) As Double
                myUDOdoubles(0) = myCursor.X
                myUDOdoubles(1) = myCursor.Y
                myUDOdoubles(2) = myCursor.Z
                ' store the newly selected origin with the udo 
                editEvent.UserDefinedObject.SetDoubles(myUDOdoubles)

                ' add the udo to the display list manually 
                ' this will force the udo display to regenerate 
                ' immediately and show the changes we just made 
                theUFSession.Disp.AddItemToDisplay(editEvent.UserDefinedObject.Tag())
            End If
        Catch ex As NXException
            Dim theLW As ListingWindow = theSession.ListingWindow
            theLW.Open()
            theLW.WriteLine("Caught Exception in myEditCB: '" & ex.Message() & "'")
        End Try
        myEditCB = 0
    End Function
    '------------------------------------------------------------------------------ 

    ' Callback Name: myInfoCB ' 
    ' This is a callback method associated with querying information for a UDO. 
    ' The information is printed in the listing window. 
    '------------------------------------------------------------------------------ 

    Public Function myInfoCB(ByVal infoEvent As UserDefinedObjects.UserDefinedEvent) As Integer
        Dim theLW As ListingWindow = theSession.ListingWindow
        theLW.Open()
        Try
            theLW.WriteLine(" ")
            theLW.WriteLine("------------------------------------------------------------")
            theLW.WriteLine("Begin Custom Information")
            theLW.WriteLine(" ")
            theLW.WriteLine("UDO Class Name: '" & infoEvent.UserDefinedObject.UserDefinedClass.ClassName & "'")
            theLW.WriteLine("UDO Friendly Name: '" & infoEvent.UserDefinedObject.UserDefinedClass.FriendlyName & "'")
            Dim myUDOdoubles() As Double = infoEvent.UserDefinedObject.GetDoubles()
            theLW.WriteLine("myUDOdoubles(0) = " & myUDOdoubles(0).ToString)
            theLW.WriteLine("myUDOdoubles(1) = " & myUDOdoubles(1).ToString)
            theLW.WriteLine("myUDOdoubles(2) = " & myUDOdoubles(2).ToString)
            theLW.WriteLine(" ")
            theLW.WriteLine("End Custom Information")
        Catch ex As NXException
            theLW.WriteLine("Caught Exception in myInfoCB:'" & ex.Message() & "'")
        End Try
        myInfoCB = 0
    End Function

    '------------------------------------------------------------------------------ 

    ' initUDO 
    ' Checks to see which (if any) of the application's static variables are 
    ' uninitialized, and sets them accordingly. 
    ' Initializes the UDO class and registers all of its callback methods. 
    '------------------------------------------------------------------------------ 

    Public Function initUDO(ByVal alertUser As Boolean) As Integer
        Try
            If theSession Is Nothing Then
                theSession = Session.GetSession()
            End If
            If theUI Is Nothing Then
                theUI = UI.GetUI()
            End If
            If theUFSession Is Nothing Then
                theUFSession = NXOpen.UF.UFSession.GetUFSession()
            End If
            If myUDOclass Is Nothing Then
                If alertUser = True Then
                    MsgBox("Registering VB UDO Class", MsgBoxStyle.OkOnly)
                End If
                ' Define your custom UDO class 
                myUDOclass = theSession.UserDefinedClassManager.CreateUserDefinedObjectClass("Sample_VB_UDO", "Sample VB UDO")
                ' Setup properties on the custom UDO class 
                myUDOclass.AllowQueryClassFromName = UserDefinedObjects.UserDefinedClass.AllowQueryClass.On
                ' Register callbacks for the UDO class 
                myUDOclass.AddDisplayHandler(AddressOf myDisplayCB)
                myUDOclass.AddAttentionPointHandler(AddressOf myDisplayCB)
                myUDOclass.AddFitHandler(AddressOf myDisplayCB)
                myUDOclass.AddSelectionHandler(AddressOf myDisplayCB)
                myUDOclass.AddEditHandler(AddressOf myEditCB)
                myUDOclass.AddInformationHandler(AddressOf myInfoCB)
                ' Add this class to the list of object types available for selection in NX. 
                ' If you skip this step you won't be able to select UDO's of this class, 
                ' even though you registered a selection callback. 
                theUI.SelectionManager.SetSelectionStatusOfUserDefinedClass(myUDOclass, True)
            End If
        Catch ex As NXException
            ' We may be initializing the UDO class during NX Startup 
            ' Print any error messages directly to the syslog 
            If theUFSession Is Nothing Then
                theUFSession = NXOpen.UF.UFSession.GetUFSession()
            End If
            theUfSession.UF.PrintSyslog("Caught Exception in initUDO: '" & ex.Message() & "'" & vbCrLf, False)
        End Try
        initUDO = 0
    End Function
    '------------------------------------------------------------------------------ 

    ' Main (Explicit Activation) 
    ' This entry point is used to activate the application explicitly, as in 
    ' "File->Execute UG/Open->NX Open..." 
    '------------------------------------------------------------------------------ 

    Sub Main()
        Try
            ' initialize the UDO - if we didn't load this library at 
            ' startup, here is our second chance to load it 
            initUDO(True)

            ' if we don't have any parts open create one 
            Dim myBasePart As BasePart = theSession.Parts.BaseDisplay
            If myBasePart Is Nothing Then
                myBasePart = theSession.Parts.NewBaseDisplay("test_vb_udo.prt", BasePart.Units.Millimeters)
            End If

            Dim myView As NXOpen.View = Nothing
            Dim myCursor As Point3d
            myCursor.X = 0
            myCursor.Y = 0
            myCursor.Z = 0
            ' ask the user to select an origin for this UDO 
            Dim myResponse As Selection.DialogResponse = theUI.SelectionManager.SelectScreenPosition("Select Origin of VB UDO", myView, myCursor)
            If myResponse = Selection.DialogResponse.Pick Then
                ' The user selected a point - go ahead and create the udo 
                Dim myUDOmanager As UserDefinedObjects.UserDefinedObjectManager = myBasePart.UserDefinedObjectManager
                Dim firstUDO As UserDefinedObjects.UserDefinedObject = myUDOmanager.CreateUserDefinedObject(myUDOclass)
                ' set the color property of the udo - just for fun :) 
                firstUDO.Color = 36
                ' store the origin selected by the user with the udo 
                Dim myUDOdoubles(3) As Double
                myUDOdoubles(0) = myCursor.X
                myUDOdoubles(1) = myCursor.Y
                myUDOdoubles(2) = myCursor.Z
                firstUDO.SetDoubles(myUDOdoubles)
                ' add the udo to the display list manually 
                ' this will force the udo to display immediately 
                theUFSession.Disp.AddItemToDisplay(firstUDO.Tag())
            End If
        Catch ex As NXException
            Dim theLW As ListingWindow = theSession.ListingWindow
            theLW.Open()
            theLW.WriteLine("Caught Exception in Main: '" & ex.Message() & "'")
        End Try
    End Sub

    '------------------------------------------------------------------------------ 
    ' Startup 
    ' Entrypoint used when program is loaded automatically 
    ' as NX starts up. Note this application must be placed in a 
    ' special folder for NX to find and load it during startup. 
    ' Refer to the NX Open documentation for more details on how 
    ' NX finds and loads applications during startup. 
    '------------------------------------------------------------------------------ 

    Public Function Startup() As Integer
        initUDO(False)
        Startup = 0
    End Function ' Startup ends 

    '------------------------------------------------------------------------------ 

    ' GetUnloadOption 
    ' Make sure you specify AtTermination for the unload option. 
    ' If you unload the library before the NX Session Terminates 
    ' bad things could happen when we try to execute a udo 
    ' callback that no longer exists in the session. 
    '------------------------------------------------------------------------------ 

    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        Return CType(Session.LibraryUnloadOption.AtTermination, Integer)
    End Function
End Module
