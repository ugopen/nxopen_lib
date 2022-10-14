'=============================================================================
'
'      Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc
'                    Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'

'==============================================================================
'  Purpose:  This TEMPLATE file contains VB.NET source to guide you in the
'  construction of your Block application dialog. The generation of your
'  dialog file (.dlx extension) is the first step towards dialog construction
'  within NX.  You must now create a NX Open application that
'  utilizes this file (.dlx).
'
'  The information in this file provides you with the following:
'
'  1.  Help on how to load and display your Block UI Styler dialog in NX
'      using APIs provided in NXOpen.BlockStyler namespace
'  2.  The empty callback methods (stubs) associated with your dialog items
'      have also been placed in this file. These empty methods have been
'      created simply to start you along with your coding requirements.
'      The method name, argument list and possible return values have already
'      been provided for you.
'==============================================================================

'------------------------------------------------------------------------------
'These imports are needed for the following template code
'------------------------------------------------------------------------------
Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.BlockStyler

'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class CreateCylinder_UsingUDB
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Private theDlxFileName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private group0 As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private point0 As NXOpen.BlockStyler.UIBlock ' Block type: Specify Point
    Private vector0 As NXOpen.BlockStyler.UIBlock ' Block type: Specify Vector
    Private group As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private diameter As DimensionUDB
    Private height As DimensionUDB
    '------------------------------------------------------------------------------
    'Bit Option for Property: SnapPointTypesEnabled
    '------------------------------------------------------------------------------
    Public Shared ReadOnly SnapPointTypesEnabled_UserDefined = 1
    Public Shared ReadOnly SnapPointTypesEnabled_Inferred = 2
    Public Shared ReadOnly SnapPointTypesEnabled_ScreenPosition = 4
    Public Shared ReadOnly SnapPointTypesEnabled_EndPoint = 8
    Public Shared ReadOnly SnapPointTypesEnabled_MidPoint = 16
    Public Shared ReadOnly SnapPointTypesEnabled_ControlPoint = 32
    Public Shared ReadOnly SnapPointTypesEnabled_Intersection = 64
    Public Shared ReadOnly SnapPointTypesEnabled_ArcCenter = 128
    Public Shared ReadOnly SnapPointTypesEnabled_QuadrantPoint = 256
    Public Shared ReadOnly SnapPointTypesEnabled_ExistingPoint = 512
    Public Shared ReadOnly SnapPointTypesEnabled_PointonCurve = 1024
    Public Shared ReadOnly SnapPointTypesEnabled_PointonSurface = 2048
    Public Shared ReadOnly SnapPointTypesEnabled_PointConstructor = 4096
    Public Shared ReadOnly SnapPointTypesEnabled_TwocurveIntersection = 8192
    Public Shared ReadOnly SnapPointTypesEnabled_TangentPoint = 16384
    Public Shared ReadOnly SnapPointTypesEnabled_Poles = 32768
    Public Shared ReadOnly SnapPointTypesEnabled_BoundedGridPoint = 65536
    '------------------------------------------------------------------------------
    'Bit Option for Property: SnapPointTypesOnByDefault
    '------------------------------------------------------------------------------
    Public Shared ReadOnly SnapPointTypesOnByDefault_UserDefined = 1
    Public Shared ReadOnly SnapPointTypesOnByDefault_Inferred = 2
    Public Shared ReadOnly SnapPointTypesOnByDefault_ScreenPosition = 4
    Public Shared ReadOnly SnapPointTypesOnByDefault_EndPoint = 8
    Public Shared ReadOnly SnapPointTypesOnByDefault_MidPoint = 16
    Public Shared ReadOnly SnapPointTypesOnByDefault_ControlPoint = 32
    Public Shared ReadOnly SnapPointTypesOnByDefault_Intersection = 64
    Public Shared ReadOnly SnapPointTypesOnByDefault_ArcCenter = 128
    Public Shared ReadOnly SnapPointTypesOnByDefault_QuadrantPoint = 256
    Public Shared ReadOnly SnapPointTypesOnByDefault_ExistingPoint = 512
    Public Shared ReadOnly SnapPointTypesOnByDefault_PointonCurve = 1024
    Public Shared ReadOnly SnapPointTypesOnByDefault_PointonSurface = 2048
    Public Shared ReadOnly SnapPointTypesOnByDefault_PointConstructor = 4096
    Public Shared ReadOnly SnapPointTypesOnByDefault_TwocurveIntersection = 8192
    Public Shared ReadOnly SnapPointTypesOnByDefault_TangentPoint = 16384
    Public Shared ReadOnly SnapPointTypesOnByDefault_Poles = 32768
    Public Shared ReadOnly SnapPointTypesOnByDefault_BoundedGridPoint = 65536

#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try

            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDlxFileName = "CreateCylinder_UsingUDB.dlx"
            theDialog = theUI.CreateDialog(theDlxFileName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddOkHandler(AddressOf ok_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
            theDialog.AddDialogShownHandler(AddressOf dialogShown_cb)
            diameter = DimensionUDB.RegisterUserDefinedUIBlock(theDialog, "diameter")
            height = DimensionUDB.RegisterUserDefinedUIBlock(theDialog, "height")

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            Throw ex
        End Try
    End Sub
#End Region
    '-------------------------------------------------------------------------------
    '------------------------------- DIALOG LAUNCHING ---------------------------------
    '
    '    Before invoking this application one needs to open any part/empty part in NX
    '    because of the behavior of the blocks.
    '
    '    Make sure the dlx file is in one of the following locations:
    '        1.) From where NX session is launched
    '        2.) $UGII_USER_DIR/application
    '        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    '            recommended. This variable is set to a full directory path to a file 
    '            containing a list of root directories for all custom applications.
    '            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
    '
    '    You can create the dialog using one of the following way:
    '
    '    1. Journal Replay
    '
    '        1) Replay this file through Tool->Journal->Play Menu.
    '
    '    2. USER EXIT
    '
    '        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    '        2) Invoke the Shared Library through File->Execute->NX Open menu.
    '
    '------------------------------------------------------------------------------
    Public Shared Sub Main()
        Dim theCreateCylinder_UsingUDB As CreateCylinder_UsingUDB = Nothing
        Try

            theCreateCylinder_UsingUDB = New CreateCylinder_UsingUDB()
            ' The following method shows the dialog immediately
            theCreateCylinder_UsingUDB.Show()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            If theCreateCylinder_UsingUDB IsNot Nothing Then
                theCreateCylinder_UsingUDB.Dispose()
                theCreateCylinder_UsingUDB = Nothing
            End If
        End Try
    End Sub
    '------------------------------------------------------------------------------
    ' This method specifies how a shared image is unloaded from memory
    ' within NX. This method gives you the capability to unload an
    ' internal NX Open application or user  exit from NX. Specify any
    ' one of the three constants as a return value to determine the type
    ' of unload to perform:
    '
    '
    '    Immediately : unload the library as soon as the automation program has completed
    '    Explicitly  : unload the library from the "Unload Shared Image" dialog
    '    AtTermination : unload the library when the NX session terminates
    '
    '
    ' NOTE:  A program which associates NX Open applications with the menubar
    ' MUST NOT use this option since it will UNLOAD your NX Open application image
    ' from the menubar.
    '------------------------------------------------------------------------------
    Public Shared Function GetUnloadOption(ByVal arg As String) As Integer
        'Return CType(Session.LibraryUnloadOption.Explicitly, Integer)
        Return CType(Session.LibraryUnloadOption.Immediately, Integer)
        ' Return CType(Session.LibraryUnloadOption.AtTermination, Integer)
    End Function
    '------------------------------------------------------------------------------
    ' Following method cleanup any housekeeping chores that may be needed.
    ' This method is automatically called by NX.
    '------------------------------------------------------------------------------
    Public Shared Sub UnloadLibrary(ByVal arg As String)
        Try


        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'This method shows the dialog on the screen
    '------------------------------------------------------------------------------
    Public Sub Show()
        Try

            theDialog.Show()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Method Name: Dispose
    '------------------------------------------------------------------------------
    Public Sub Dispose()
        If diameter IsNot Nothing Then
            diameter.Dispose()
            diameter = Nothing
        End If
        If height IsNot Nothing Then
            height.Dispose()
            height = Nothing
        End If
        If theDialog IsNot Nothing Then
            theDialog.Dispose()
            theDialog = Nothing
        End If
    End Sub

    '------------------------------------------------------------------------------
    '---------------------Block UI Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------

    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try

            group0 = theDialog.TopBlock.FindBlock("group0")
            point0 = theDialog.TopBlock.FindBlock("point0")
            vector0 = theDialog.TopBlock.FindBlock("vector0")
            group = theDialog.TopBlock.FindBlock("group")

            diameter.SetLabel("Diameter")
            diameter.SetValue(100)

            height.SetLabel("Height")
            height.SetValue(100)

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Callback Name: dialogShown_cb
    'This callback is executed just before the dialog launch. Thus any value set 
    'here will take precedence and dialog will be launched showing that value. 
    '------------------------------------------------------------------------------
    Public Sub dialogShown_cb()
        Try

            '---- Enter your callback code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer
        Dim errorCode As Integer = 0
        Try
            '---- Enter your callback code here -----
            CreateCylinder()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        apply_cb = errorCode
    End Function

    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try

            If block Is point0 Then
                '---- Enter your code here -----

            ElseIf block Is vector0 Then
                '---- Enter your code here -----

            ElseIf block Is diameter.TopBlock Then
                '---- Enter your code here -----

            ElseIf block Is height.TopBlock Then
                '---- Enter your code here -----

            End If

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        update_cb = 0
    End Function

    '------------------------------------------------------------------------------
    'Callback Name: ok_cb
    '------------------------------------------------------------------------------
    Public Function ok_cb() As Integer
        Dim errorCode As Integer = 0
        Try

            '---- Enter your callback code here -----
            errorCode = apply_cb()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        ok_cb = errorCode
    End Function
    '------------------------------------------------------------------------------
    'Callback Name: CreateCylinder
    '------------------------------------------------------------------------------
    Private Sub CreateCylinder()

        Dim workPart As NXOpen.Part = theSession.Parts.Work
        Dim cylinderBuilder1 As Features.CylinderBuilder
        Dim nullFeatures_Feature As Features.Feature = Nothing
        cylinderBuilder1 = workPart.Features.CreateCylinderBuilder(nullFeatures_Feature)

        'Get the point
        Dim pointPropertyList As PropertyList = point0.GetProperties()
        Dim point1 As Point3d = pointPropertyList.GetPoint("Point")
        pointPropertyList.Dispose()
        pointPropertyList = Nothing

        Dim vectorPropertyList As PropertyList = vector0.GetProperties()
        Dim Vector As Vector3d = vectorPropertyList.GetVector("Vector")
        vectorPropertyList.Dispose()
        vectorPropertyList = Nothing
        Dim direction1 As Direction = workPart.Directions.CreateDirection(point1, Vector, SmartObject.UpdateOption.WithinModeling)
        Dim diameter1 As Double = diameter.GetValue("Diameter")

        Dim height1 As Double = height.GetValue("Height")

        cylinderBuilder1.Diameter.RightHandSide = diameter1.ToString()
        cylinderBuilder1.Height.RightHandSide = height1.ToString()

        Dim axis1 As Axis
        axis1 = cylinderBuilder1.Axis

        axis1.Point.SetCoordinates(point1)
        axis1.Direction = direction1

        cylinderBuilder1.Commit()
        cylinderBuilder1.Destroy()

    End Sub

End Class
