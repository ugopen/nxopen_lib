'=============================================================================
'
'   Copyright 2011 Siemens Product Lifecycle Management Software Inc. 
'                  All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program assign custom data to all part geometry of a mill geometry
'     group or cavity mill operation selected in the operation navigator. 
'
'     The custom data can either be defined by directly entering the numeric
'     value in the dialog used here. Or it can be defined by entering the 
'     name of an attribute that is assigned to the geometry and that holds
'     the actual numeric value for the customer data. Note that within a
'     geometry set, all custom data must be the same value. Thus is the 
'     attributes defined on the individual geometry entities of a geoemtry
'     set have different numeric value, the system will raise an error.
'
'     Prerequisite to run this script is that a mill geometry group or a
'     cavity milling opration is selected in the operation navigator.
'
'     This script can be used as a boiler plate to set other geometry related 
'     custom data values.
' ============================================================================'

'------------------------------------------------------------------------------
'These imports are needed for the following template code
'------------------------------------------------------------------------------
Option Strict Off
Imports System
Imports System.Globalization
Imports NXOpen
Imports NXOpen.BlockStyler
Imports NXOpen.RemoteUtilities
Imports NXOpen.UF
Imports NXOpen.Utilities

'------------------------------------------------------------------------------
'Represents Block Styler application class (dialog)
'------------------------------------------------------------------------------
Public Class AssignCustomDataDialog

    'class members
    Private Shared theSession As Session
    Private Shared theUfSession As UFSession
    Private Shared theUI As UI
    Private theDlxFileName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private typeGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private geometryTypeEnumeration As NXOpen.BlockStyler.UIBlock' Block type: Enumeration
    Private attributeGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private stockAttributeString As NXOpen.BlockStyler.UIBlock' Block type: String
    Private intolAttributeString As NXOpen.BlockStyler.UIBlock' Block type: String
    Private outtolAttributeString As NXOpen.BlockStyler.UIBlock' Block type: String
    Private cutFeedAttributeString As NXOpen.BlockStyler.UIBlock' Block type: String

    '------------------------------------------------------------------------------
    'Constructor for NX Styler class - creates the dialog object
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        

            theUI = UI.GetUI()
            
            'The DLX file path and name
            Dim path As String
            path = theSession.GetEnvironmentVariableValue("UGII_USERFCN")
            theDlxFileName = path + "\SampleNXOpenApplications\.NET\CAM\GeometryAssignCustomDataBasedOnAttributesDialog.dlx"
            
            theDialog = theUI.CreateDialog(theDlxFileName)
            
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddOkHandler(AddressOf ok_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            Throw ex
        End Try
    End Sub
    
    '------------------------------- DIALOG LAUNCHING ---------------------------------
    '
    '    Before invoking this application one needs to open any part/empty part in NX
    '    because of the behavior of the blocks.
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
        Dim customDataDialog As AssignCustomDataDialog = Nothing
        
        Try
        
            theSession = Session.GetSession()
            Dim WorkPart As Part = theSession.Parts.Work

            ' If there is a work part only then we can go further
            If WorkPart IsNot Nothing Then

                ' If there is a setup only then do we have to go further
                If WorkPart.CAMSetup() IsNot Nothing Then

                    theUfSession = UFSession.GetUFSession()

                    customDataDialog = New AssignCustomDataDialog()
                    ' The following method shows the dialog immediately
                    customDataDialog.Show()
                Else
                    theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, "The work part does not have a CAM Setup.")
                End If
            Else
                theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, "No part is open.")
            End If
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            If customDataDialog IsNot Nothing Then 
                customDataDialog.Dispose()
                customDataDialog = Nothing
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
    Public Shared Function UnloadLibrary(ByVal arg As String) As Integer
        Try
        
            Return 0
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function
    
    '------------------------------------------------------------------------------
    'This method shows the dialog on the screen
    '------------------------------------------------------------------------------
    Public Sub Show()
        Try
        
            theDialog.Show
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
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
    '---------------------Block UI Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------
    
    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try
        
            typeGroup = theDialog.TopBlock.FindBlock("typeGroup")
            geometryTypeEnumeration = theDialog.TopBlock.FindBlock("geometryTypeEnumeration")
            attributeGroup = theDialog.TopBlock.FindBlock("attributeGroup")
            stockAttributeString = theDialog.TopBlock.FindBlock("stockAttributeString")
            intolAttributeString = theDialog.TopBlock.FindBlock("intolAttributeString")
            outtolAttributeString = theDialog.TopBlock.FindBlock("outtolAttributeString")
            cutFeedAttributeString = theDialog.TopBlock.FindBlock("cutFeedAttributeString")

        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer
        Dim errorCode as Integer = 0
        Try
        
            '---- Enter your callback code here -----
            'Get the geometry type. The types are defined in DLX file.
            'With the sample DLX, the values can be Part=0, Blank=1, Check=2, CutArea=3, Wall=4.
            Dim propList As BlockStyler.PropertyList = geometryTypeEnumeration.GetProperties
            Dim geomType As Integer = propList.GetEnum("Value")

            'Call sub functions to assign the custom data.
            If geomType = 0 Then
                AssignCustomDataToPart()
            ElseIf geomType = 1 Then
                AssignCustomDataToBlank()
            ElseIf geomType = 2 Then
                AssignCustomDataToCheck()
            ElseIf geomType = 3 Then
                AssignCustomDataToCutArea()
            ElseIf geomType = 4 Then
                AssignCustomDataToWall()
            End If


        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        apply_cb = errorCode
    End Function
    
    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try
        
            If block Is geometryTypeEnumeration Then
            '---- Enter your code here -----
            
            ElseIf block Is stockAttributeString Then
                '---- Enter your code here -----

            ElseIf block Is intolAttributeString Then
            '---- Enter your code here -----
            
            ElseIf block Is outtolAttributeString Then
            '---- Enter your code here -----
            
            ElseIf block Is cutFeedAttributeString Then
            '---- Enter your code here -----
            
            End If
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        update_cb = 0
    End Function
    
    '------------------------------------------------------------------------------
    'Callback Name: ok_cb
    '------------------------------------------------------------------------------
    Public Function ok_cb() As Integer
        Dim errorCode as Integer = 0
        Try
        
            '---- Enter your callback code here -----
            errorCode = apply_cb()
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        ok_cb = errorCode
    End Function
    
    '------------------------------------------------------------------------------
    '---------------------Custom Data Assignment Functions-------------------------
    '------------------------------------------------------------------------------
    ' The functions below are the actual core functions of this example script.
    ' They will take care of going through all the part geometry of the mill
    ' geometry group or cavity mill operation and assigning the custom data

    '------------------------------------------------------------------------------
    ' Function Name: AssignCustomDataToPart
    '
    ' For part geometry, the available custom data depends on the selected object.
    ' For example, a workpiece geometry group has part offset, while a cavity milling 
    ' operation has In/Out tolerances.
    '
    ' Then the sample code here is roughly doing the following steps:
    '
    ' (1) Get the target cam object, create a corresponding builder on it.
    ' (2) Get the part geometry sets, and get the user input from the dialog
    ' (3) For each geometry set, if the given value is a pure number, set the value
    '     as custom data for this set.
    '     If it the given value is an attribute name, then get all geometry entities 
    '     of this set, find the attribute value on the entities and assign that value 
    '     to this set.
    ' (4) Commit the changes to database.
    '------------------------------------------------------------------------------
    Public Function AssignCustomDataToPart() As Integer
        Dim errorCode As Integer = 0
        Try

            Dim selectedTags() As NXOpen.Tag
            Dim selectedCount As Integer = 0

            ' Get the selected nodes from the Operation Navigator
            theUfSession.UiOnt.AskSelectedNodes(selectedCount, selectedTags)

            If selectedCount <> 0 Then

                Dim index As Integer = 0
                While index < selectedCount

                    ' Get the geometry builder for the selected object
                    Dim millGeomBuilder As CAM.ParamBuilder
                    Dim partGeometry As CAM.Geometry
                    millGeomBuilder = GetBuilderFromObject(selectedTags(index), partGeometry)

                    If millGeomBuilder IsNot Nothing And partGeometry IsNot Nothing Then

                        'check if there is any part geometry selected.
                        Dim numItems As Integer = partGeometry.GeometryList.Length
                        If numItems > 0 Then

                            'Get the attribute name which defines the part stock for the geometry.
                            Dim propList As BlockStyler.PropertyList = stockAttributeString.GetProperties
                            Dim partAttrName As String = propList.GetString("Value")

                            'The attribute name may be a pure number. So try to convert it to a double value
                            Dim partStock As Double = 0.0
                            Dim isPartStockPureNumber As Boolean = GetPureValue(partAttrName, partStock)

                            'Get the attribute name which defines the intol for the geometry.
                            propList = intolAttributeString.GetProperties
                            Dim intolAttrName As String = propList.GetString("Value")

                            'The attribute name may be a pure number. So try to convert it to a double value
                            Dim intol As Double = 0.0
                            Dim isIntolPureNumber As Boolean = GetPureValue(intolAttrName, intol)

                            'Get the attribute name which defines the outtol for the geometry.
                            propList = outtolAttributeString.GetProperties
                            Dim outtolAttrName As String = propList.GetString("Value")

                            'The attribute name may be a pure number. So try to convert it to a double value
                            Dim outtol As Double = 0.0
                            Dim isOuttolPureNumber As Boolean = GetPureValue(outtolAttrName, outtol)

                            'Cycle all the geometry sets and assign custom data.
                            For item As Integer = 0 To numItems - 1

                                Dim taggedObject1 As TaggedObject
                                taggedObject1 = partGeometry.GeometryList.FindItem(item)

                                Dim geometrySet1 As CAM.GeometrySet = CType(taggedObject1, CAM.GeometrySet)

                                'Set the part stock (offset) custom data to the geometry set.
                                ' Note that if the geometry set does not support this type of custom data
                                ' it will simply be ignored. There is no error raised.
                                If Not String.IsNullOrWhiteSpace(partAttrName) Then
                                    If isPartStockPureNumber Then
                                        'It is a pure number, set the value.
                                        geometrySet1.CustomPartOffset = True
                                        geometrySet1.PartOffset = partStock
                                    Else
                                        'If it isn't a pure number, then find the attribute which is defined at the 
                                        'geometry entities for the current set and get the value from there.
                                        If GetAttrValueFromSelectedEntities(geometrySet1, PartAttrName, partStock) Then
                                            geometrySet1.CustomPartOffset = True
                                            geometrySet1.PartOffset = partStock

                                        Else
                                            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("The Offset custom data is not assigned for the geometry set ({0}).", Convert.ToString(item + 1)))
                                        End If

                                    End If
                                End If

                                'Set the intol custom data to the geometry set.
                                ' Note that if the geometry set does not support this type of custom data
                                ' it will simply be ignored. There is no error raised.
                                If Not String.IsNullOrWhiteSpace(intolAttrName) Then
                                    If isIntolPureNumber Then
                                        'It is a pure number, set the value.
                                        geometrySet1.CustomTolerance = True
                                        geometrySet1.Intol = intol
                                    Else
                                        'If it isn't a pure number, then find the attribute which is defined at the 
                                        'geometry entities for the current set and get the value from there.
                                        If GetAttrValueFromSelectedEntities(geometrySet1, IntolAttrName, intol) Then
                                            geometrySet1.CustomTolerance = True
                                            geometrySet1.Intol = intol

                                        Else
                                            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("The Intol custom data is not assigned for the geometry set ({0}).", Convert.ToString(item + 1)))
                                        End If
                                    End If
                                End If
                                
                                'Set the outtol custom data to the geometry set.
                                ' Note that if the geometry set does not support this type of custom data
                                ' it will simply be ignored. There is no error raised.
                                If Not String.IsNullOrWhiteSpace(intolAttrName) Then
                                    If isOuttolPureNumber Then
                                        'It is a pure number, set the value.
                                        geometrySet1.CustomTolerance = True
                                        geometrySet1.Outtol = Outtol
                                    Else
                                        'If it isn't a pure number, then find the attribute which is defined at the 
                                        'geometry entities for the current set and get the value from there.
                                        If GetAttrValueFromSelectedEntities(geometrySet1, OuttolAttrName, outtol) Then
                                            geometrySet1.CustomTolerance = True
                                            geometrySet1.Outtol = Outtol

                                        Else
                                            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("The Outtol custom data is not assigned for the geometry set ({0}).", Convert.ToString(item + 1)))
                                        End If

                                    End If
                                End If

                            Next

                            'Commit the changes to database.
                            Dim nXObject1 As NXObject
                            nXObject1 = millGeomBuilder.Commit()

                        End If
                    End If

                    'Destroy the created builder
                    If millGeomBuilder IsNot Nothing Then
                        millGeomBuilder.Destroy()
                    End If

                    ' Increment to the next object
                    index = index + 1
                End While
            End If

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        AssignCustomDataToPart = errorCode

    End Function

    '------------------------------------------------------------------------------
    'Function Name: AssignCustomDataToBlank
    'This is an empty method (stub). Please implement it as your requirement.
    'You can take the AssignCustomDataToPart method as example to do the similar thing
    'for blank geometry.
    '------------------------------------------------------------------------------
    Public Function AssignCustomDataToBlank() As Integer
        Dim errorCode As Integer = 0
        Try

            '---- Enter the custom data assignment for blank code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        AssignCustomDataToBlank = errorCode
    End Function

    '------------------------------------------------------------------------------
    'Function Name: AssignCustomDataToCheck
    'This is an empty method (stub). Please implement it as your requirement.
    'You can take the AssignCustomDataToPart method as example to do the similar thing
    'for check geometry.
    '------------------------------------------------------------------------------
    Public Function AssignCustomDataToCheck() As Integer
        Dim errorCode As Integer = 0
        Try

            '---- Enter the custom data assignment for Check code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        AssignCustomDataToCheck = errorCode
    End Function

    '------------------------------------------------------------------------------
    'Function Name: AssignCustomDataToCutArea
    'This is an empty method (stub). Please implement it as your requirement.
    'You can take the AssignCustomDataToPart method as example to do the similar thing
    'for cut area geometry.
    '------------------------------------------------------------------------------
    Public Function AssignCustomDataToCutArea() As Integer
        Dim errorCode As Integer = 0
        Try

            '---- Enter the custom data assignment for Cut Area code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        AssignCustomDataToCutArea = errorCode
    End Function

    '------------------------------------------------------------------------------
    'Function Name: AssignCustomDataToWall
    'This is an empty method (stub). Please implement it as your requirement.
    'You can take the AssignCustomDataToPart method as example to do the similar thing
    'for wall geometry.
    '------------------------------------------------------------------------------
    Public Function AssignCustomDataToWall() As Integer
        Dim errorCode As Integer = 0
        Try

            '---- Enter the custom data assignment for Wall code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        AssignCustomDataToWall = errorCode
    End Function

    '------------------------------------------------------------------------------
    ' Function Name: GetAttrValueFromSelectedEntities
    '
    ' Get the value defined by the attribute that is assigned to the geometry entities
    '
    ' The setObj is the current geometry set which contains the geometry entities.
    ' 
    ' For any two of the entities, if their values are defined differently for the attribute,
    ' then just return FALSE meaning no appropriate value found!
    '------------------------------------------------------------------------------
    Public Function GetAttrValueFromSelectedEntities(ByVal setObj As CAM.GeometrySet, ByVal attrName As String, ByRef retValue As Double) As Boolean
    
        Dim valueFound As Boolean = False
    
        Try
            If attrName.Length > 0 Then
                'Make sure there is something selected in the set.
                If setObj.Selection.Size > 0 Then
                    Dim attrValue As Double = 0.0
                    'Get selection list
                    Dim objList() As TaggedObject = setObj.Selection.GetArray()
                    Dim numObjs As Integer = Ubound(objList)
                    Dim endLoop As Boolean = False
                    
                    'Cycle all the entities, find the value for the attribute.
                    For item As Integer = 0 To numObjs
                        'Check if exit the loop
                        If endLoop = False Then
                            Dim entity As TaggedObject = objList(item)
                            Dim isCollector As Boolean = False
                            
                            'Try for collector
                            Try
                                Dim collector As ScCollector = CType(entity, ScCollector)
                                'Get all entities in collector
                                Dim selectedEntities() As TaggedObject = collector.GetObjects()
                                Dim numEntity As Integer = Ubound(selectedEntities)

                                isCollector = True
                                If numEntity >= 0 Then
                                    'Cycle each entity.
                                    For count As Integer = 0 To numEntity
                                        If endLoop = False Then
                                            Dim selectedEntity As NXObject = CType(selectedEntities(count), NXObject)
                                            Dim myAttrValue As Double = 0.0
                                            
                                            'Get the attribute value at this entity
                                            If GetAttrValue(selectedEntity, attrName, myAttrValue) = 0 Then
                                                'Check if there is any conflict with other entities.
                                                If valueFound Then
                                                    'If the value is different from previous one, then show error and exit.
                                                    If attrValue <> myAttrValue Then
                                                        theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("At least two of selected entities have set the attribute {0} to different values. Custom Data will not be assigned for geometry set {1}.", attrName, setObj.ToString()))
                                                        'End the loop for searching the attribute values.
                                                        endLoop = True
                                                        'Return value not found to stop assignment.
                                                        valueFound = False
                                                    End If
                                                Else
                                                    'Keep this value since it is the first found value.
                                                    attrValue = myAttrValue
                                                    valueFound = True
                                                End If
                                            End If

                                        End If
                                    Next

                                End If

                            Catch ex As Exception
                                'theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, "Not collector")

                            End Try

                            'Try for non collector entity
                            If isCollector = False Then
                                Dim nonCollector As NXObject = CType(entity, NXObject)
                                Dim myAttrValue As Double = 0.0
                                'Get the attribute value which is defined to the entity.
                                If GetAttrValue(nonCollector, attrName, myAttrValue) = 0 Then
                                    'Check if there is any conflict with other entities.
                                    If valueFound Then
                                        'If the value is different from previous one, then show error and exit.
                                        If attrValue <> myAttrValue Then
                                            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("At least two of selected entities have set the attribute {0} to different values. Custom Data will not be assigned for geometry set {1}.", attrName, setObj.ToString()))
                                            'End the loop for searching the attribute values.
                                            endLoop = True
                                            'Return value not found to stop assignment.
                                            valueFound = False
                                        End If
                                    Else
                                        'Keep this value since it is the first found value.
                                        attrValue = myAttrValue
                                        valueFound = True

                                    End If
                                End If

                            End If
                        End If

                    Next

                    If valueFound Then
                        retValue = attrValue

                    End If
                End If

            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("The custom data is not set to the geometry set ({0}) due to an unexpected exception ({1}).", setObj.ToString(), ex.ToString()))
        End Try
        GetAttrValueFromSelectedEntities = valueFound
    End Function

    '------------------------------------------------------------------------------
    ' Function Name: GetAttrValue
    ' Get the value defined by the attribute of an object
    '------------------------------------------------------------------------------
    Public Function GetAttrValue(ByVal obj As NXObject, ByVal attrName As String, ByRef retValue As Double) As Integer
    
        Dim errorCode As Integer = 0
        Try
            If attrName.Length > 0 Then
                Dim info As NXObject.AttributeInformation
                info = obj.GetUserAttribute(attrName, NXObject.AttributeType.Real, 0)
                retValue = info.RealValue
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("The attribute {0} is not found at object {1}.", attrName, obj.ToString()))
        End Try
        GetAttrValue = errorCode
    End Function

    '------------------------------------------------------------------------------
    'Function Name: GetPureValue
    'Convert the string to a pure number, return true if it is a pure number.
    '------------------------------------------------------------------------------
    Public Function GetPureValue(ByVal attrName As String, ByRef retValue As Double) As Boolean
        Dim isPureNumber As Boolean = False
        If attrName.Length > 0 Then
            Try
                ' NX always uses the period symbol as be decimal separator. Other locales like German 
                ' have a different symbol for this. Thus make sure that we always use the period
                ' when checking if the string is a number.
                Dim formatInfo As NumberFormatInfo = new NumberFormatInfo( )
                formatInfo.NumberDecimalSeparator = "."
                
                retValue = Convert.ToDouble(attrName, formatInfo)
                isPureNumber = True

            Catch ex As Exception
                '---- Enter your exception handling code here -----
                'theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("The attribute {0} is not a numerical value.", attrName))
            End Try
        End If
        GetPureValue = isPureNumber
    End Function


    '------------------------------------------------------------------------------
    'Function Name: GetBuilderFromObject
    'For the given CAM object, get a corresponding builder and the part geometry set.
    '
    'Note: This function only supports mill geometry groups and cavity mill operations.
    '------------------------------------------------------------------------------
    Public Function GetBuilderFromObject(ByVal obj As Tag, ByRef geomSet As CAM.Geometry) As CAM.ParamBuilder

        Dim builder As CAM.ParamBuilder = Nothing

        Dim camObject As NXObject = NXObjectManager.Get(obj)

        Dim WorkPart As Part = theSession.Parts.Work

        ' Check if the given object is a mill geometry group
        If TypeOf camObject Is CAM.FeatureGeometry Then

            Dim millGeomBuilder As CAM.MillGeomBuilder = workPart.CAMSetup.CAMGroupCollection.CreateMillGeomBuilder(camObject)
            builder = millGeomBuilder
            geomSet = millGeomBuilder.PartGeometry

        ElseIf TypeOf camObject Is CAM.Operation Then
            ' Else check if the given object is an operation

            Dim operationType As Integer
            Dim operationSubtype As Integer

            'Get the type and subtype of the operation
            theUFSession.Obj.AskTypeAndSubtype(obj, operationType, operationSubtype)

            If operationSubtype = 260 Then         ' This is a Cavity Milling Operation so create a Cavity Milling Builder
                Dim cavityBuilder As CAM.CavityMillingBuilder = workPart.CamSetup.CAMOperationCollection.CreateCavityMillingBuilder(camObject)
                builder = cavityBuilder
                geomSet = cavityBuilder.PartGeometry
            Else
                theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("The object {0} is not a valid object for this process.", camObject.ToString()))
            End If
        Else

            theUI.NXMessageBox.Show("Assign Custom Data", NXMessageBox.DialogType.Error, String.Format("The object {0} is not a valid object for this process.", camObject.ToString()))
        End If

        Return builder
    End Function

End Class

