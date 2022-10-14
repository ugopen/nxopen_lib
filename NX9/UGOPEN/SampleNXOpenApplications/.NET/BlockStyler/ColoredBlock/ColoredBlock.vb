'=============================================================================
'
'                   Copyright (c) 2008 Siemens PLM Solutions
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
'  1.  Help on how to load and display your Block Styler dialog in NX
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
Public Class ColoredBlock
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theColoredBlock As ColoredBlock
    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private group0 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private blockHeight As NXOpen.BlockStyler.UIBlock' Block type: Double
    Private blockWidth As NXOpen.BlockStyler.UIBlock' Block type: Double
    Private blockLength As NXOpen.BlockStyler.UIBlock' Block type: Double
    Private blockOrigin As NXOpen.BlockStyler.UIBlock' Block type: Specify Point
    Private blockColor As NXOpen.BlockStyler.UIBlock' Block type: Color Picker
    '------------------------------------------------------------------------------
    'Bit Option for Property: SnapPointTypesEnabled
    '------------------------------------------------------------------------------
    Public Shared ReadOnly              SnapPointTypesEnabled_UserDefined =     1
    Public Shared ReadOnly                 SnapPointTypesEnabled_Inferred =     2
    Public Shared ReadOnly           SnapPointTypesEnabled_ScreenPosition =     4
    Public Shared ReadOnly                 SnapPointTypesEnabled_EndPoint =     8
    Public Shared ReadOnly                 SnapPointTypesEnabled_MidPoint =    16
    Public Shared ReadOnly             SnapPointTypesEnabled_ControlPoint =    32
    Public Shared ReadOnly             SnapPointTypesEnabled_Intersection =    64
    Public Shared ReadOnly                SnapPointTypesEnabled_ArcCenter =   128
    Public Shared ReadOnly            SnapPointTypesEnabled_QuadrantPoint =   256
    Public Shared ReadOnly            SnapPointTypesEnabled_ExistingPoint =   512
    Public Shared ReadOnly             SnapPointTypesEnabled_PointonCurve =  1024
    Public Shared ReadOnly           SnapPointTypesEnabled_PointonSurface =  2048
    Public Shared ReadOnly         SnapPointTypesEnabled_PointConstructor =  4096
    Public Shared ReadOnly     SnapPointTypesEnabled_TwocurveIntersection =  8192
    Public Shared ReadOnly             SnapPointTypesEnabled_TangentPoint = 16384
    Public Shared ReadOnly                    SnapPointTypesEnabled_Poles = 32768
    '------------------------------------------------------------------------------
    'Bit Option for Property: SnapPointTypesOnByDefault
    '------------------------------------------------------------------------------
    Public Shared ReadOnly          SnapPointTypesOnByDefault_UserDefined =     1
    Public Shared ReadOnly             SnapPointTypesOnByDefault_Inferred =     2
    Public Shared ReadOnly       SnapPointTypesOnByDefault_ScreenPosition =     4
    Public Shared ReadOnly             SnapPointTypesOnByDefault_EndPoint =     8
    Public Shared ReadOnly             SnapPointTypesOnByDefault_MidPoint =    16
    Public Shared ReadOnly         SnapPointTypesOnByDefault_ControlPoint =    32
    Public Shared ReadOnly         SnapPointTypesOnByDefault_Intersection =    64
    Public Shared ReadOnly            SnapPointTypesOnByDefault_ArcCenter =   128
    Public Shared ReadOnly        SnapPointTypesOnByDefault_QuadrantPoint =   256
    Public Shared ReadOnly        SnapPointTypesOnByDefault_ExistingPoint =   512
    Public Shared ReadOnly         SnapPointTypesOnByDefault_PointonCurve =  1024
    Public Shared ReadOnly       SnapPointTypesOnByDefault_PointonSurface =  2048
    Public Shared ReadOnly     SnapPointTypesOnByDefault_PointConstructor =  4096
    Public Shared ReadOnly SnapPointTypesOnByDefault_TwocurveIntersection =  8192
    Public Shared ReadOnly         SnapPointTypesOnByDefault_TangentPoint = 16384
    Public Shared ReadOnly                SnapPointTypesOnByDefault_Poles = 32768
    
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialogName = "ColoredBlock.dlx"
            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
            theDialog.AddDialogShownHandler(AddressOf dialogShown_cb)
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            Throw ex
        End Try
    End Sub
#End Region
    
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
    '            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
    '
    '    You can create the dialog using one of the following way:
    '
    '    1. Journal Replay
    '
    '        1) Replay this file through Tool->Journal->Play Menu.
    '
    '    2. USER EXIT
    '
    '        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
    '        2) Invoke the Shared Library through File->Execute->NX Open menu.
    '
    '------------------------------------------------------------------------------
    Public Shared Sub Main()
        Try
        
            theColoredBlock = New ColoredBlock()
            ' The following method shows the dialog immediately
            theColoredBlock.Show()
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theColoredBlock.Dispose()
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
        
            theDialog.Show
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Method Name: Dispose
    '------------------------------------------------------------------------------
    Public Sub Dispose()
        If theDialog IsNot Nothing Then 
            theDialog.Dispose()
            theDialog = Nothing
        End If
    End Sub
    
    '------------------------------------------------------------------------------
    '---------------------Block Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------
    
    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try
        
            group0 = theDialog.TopBlock.FindBlock("group0")
            blockHeight = theDialog.TopBlock.FindBlock("blockHeight")
            blockWidth = theDialog.TopBlock.FindBlock("blockWidth")
            blockLength = theDialog.TopBlock.FindBlock("blockLength")
            blockOrigin = theDialog.TopBlock.FindBlock("blockOrigin")
            blockColor = theDialog.TopBlock.FindBlock("blockColor")

            ' Set the upper-limits and lower-limits
            Dim blockHeightProps As PropertyList = blockHeight.GetProperties()
            blockHeightProps.SetDouble("MaximumValue", 100000.0)
            blockHeightProps.SetDouble("MinimumValue", 0.001)
            blockHeightProps.SetDouble("Value", 100)
            blockHeightProps.Dispose()
            blockHeightProps = Nothing

            Dim blockWidthProps As PropertyList = blockWidth.GetProperties()
            blockWidthProps.SetDouble("MaximumValue", 100000.0)
            blockWidthProps.SetDouble("MinimumValue", 0.001)
            blockWidthProps.SetDouble("Value", 100)
            blockWidthProps.Dispose()
            blockWidthProps = Nothing

            Dim blockLengthProps As PropertyList = blockLength.GetProperties()
            blockLengthProps.SetDouble("MaximumValue", 100000.0)
            blockLengthProps.SetDouble("MinimumValue", 0.001)
            blockLengthProps.SetDouble("Value", 100)
            blockLengthProps.Dispose()
            blockLengthProps = Nothing

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
        Dim blockFeatureBuilder1 As Features.BlockFeatureBuilder = Nothing

        Try

            Dim workPart As Part = theSession.Parts.Work

            'Get the values from UI Blocks
            Dim blockHeightProps As PropertyList = blockHeight.GetProperties()
            Dim theHeight As Double = blockHeightProps.GetDouble("Value")
            blockHeightProps.Dispose()
            blockHeightProps = Nothing

            Dim blockWidthProps As PropertyList = blockWidth.GetProperties()
            Dim theWidth As Double = blockWidthProps.GetDouble("Value")
            blockWidthProps.Dispose()
            blockWidthProps = Nothing

            Dim blockLengthProps As PropertyList = blockLength.GetProperties()
            Dim theLength As Double = blockLengthProps.GetDouble("Value")
            blockLengthProps.Dispose()
            blockLengthProps = Nothing

            Dim blockOriginProps As PropertyList = blockOrigin.GetProperties()
            Dim originPoint As Point3d = blockOriginProps.GetPoint("Point")
            blockOriginProps.Dispose()
            blockOriginProps = Nothing

            Dim blockColorProps As PropertyList = blockColor.GetProperties()
            Dim color() As Integer = blockColorProps.GetIntegerVector("Value")
            blockColorProps.Dispose()
            blockColorProps = Nothing

            Dim nullFeatures_Feature As Features.Feature = Nothing
            blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(nullFeatures_Feature)
            blockFeatureBuilder1.SetOriginAndLengths(originPoint, theLength.ToString(), theHeight.ToString(), theWidth.ToString())

            Dim feature1 As Features.Feature
            feature1 = blockFeatureBuilder1.CommitFeature()

            'Get the body from Feature
            Dim bodyFeat As NXOpen.Features.BodyFeature = CType(feature1, Features.BodyFeature)
            Dim bodies() As Body = bodyFeat.GetBodies()
            'Apply the color to feature body
            Dim displayModification1 As DisplayModification
            displayModification1 = theSession.DisplayManager.NewDisplayModification()
            displayModification1.ApplyToAllFaces = True
            displayModification1.NewColor = color(0)
            Dim objects1(0) As DisplayableObject
            objects1(0) = bodies(0)
            displayModification1.Apply(objects1)
            displayModification1.Dispose()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            If Not blockFeatureBuilder1 Is Nothing Then
                blockFeatureBuilder1.Destroy()
            End If
        End Try

        apply_cb = errorCode

    End Function
    
End Class
