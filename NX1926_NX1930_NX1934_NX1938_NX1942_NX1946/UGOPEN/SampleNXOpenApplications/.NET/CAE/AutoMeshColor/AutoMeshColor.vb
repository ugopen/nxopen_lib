' NX 6.0.2.8
' AutoMeshColor.vb - Change element display color based on mesh, collector, physical or material
'
' 
'
'------------------------------------------------------------
Option Strict Off
Imports System
Imports System.IO
Imports System.Collections

Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.CAE
Imports NXOpen.Utilities
Imports NXOpen.BlockStyler

Module AutoMeshColor
    Dim theSession As Session = Session.GetSession()
    Dim theUFSession As NXOpen.UF.UFSession = UFSession.GetUFSession()
    Dim theLW As NXOpen.ListingWindow = theSession.ListingWindow()
    Dim theUI As NXOpen.UI = NXOpen.UI.GetUI()

    ' Define colors to loop through. The NX color palette is included at the bottom of this file
    Dim myColorWheel() As Integer = {181, 31, 186, 36, 78, 6, 211, 103, 108, 11}

    Dim myColorOptions() As String = {"Mesh", "Mesh Collector", "Physical Property", "Material Property"}
    Dim DEBUG As Integer = 0

    Sub Main()
        ' Setup session and part variables        

        Dim basePart As BasePart = theSession.Parts.BaseWork
        If basePart Is Nothing Then Return

        theLW.Open()

        ' Launch the NX Dialog to determine which way to edit colors
        Dim theenumBlock As enumBlock = Nothing
        Try

            theenumBlock = New enumBlock(basePart)
            ' The following method shows the dialog immediately
            theenumBlock.Show()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally

            If theenumBlock IsNot Nothing Then theenumBlock.Dispose()

        End Try
    End Sub

    Sub DoIt(ByVal basePart As BasePart, ByVal myColorOption As Integer, ByVal myListOption As Integer)
        DEBUG = myListOption
        'DEBUG = 2

        Dim objectTag As Tag
        Dim NULLTAG As Tag = NXOpen.Tag.Null
        Dim IdxC As Integer = 0

        Dim myMeshTag As Tag
        Dim myMeshColor As New Hashtable()
        Dim myCollectorTag As Tag
        Dim myCollectorColor As New Hashtable()
        Dim myPhysicalTag As Tag
        Dim myPhysicalColor As New Hashtable()
        Dim myMaterialTag As Tag
        Dim myMaterialColor As New Hashtable()

        theUFSession.Obj.CycleObjsInPart(basePart.Tag, NXOpen.UF.UFConstants.UF_sfem_mesh_type, objectTag)

        Do While objectTag <> NULLTAG
            Dim nxobject As NXObject = NXOpen.Utilities.NXObjectManager.Get(objectTag)
            Dim objType As Integer = 0
            Dim objSubType As Integer = 0

            If DEBUG > 1 Then theLW.WriteLine(vbNewLine)

            theUFSession.Obj.AskTypeAndSubtype(objectTag, objType, objSubType)

            If objSubType = NXOpen.UF.UFConstants.UF_sfem_generic_mesh_subtype Then
                Dim mesh As CAE.Mesh = CType(nxobject, CAE.Mesh)

                myMeshTag = mesh.Tag
                Dim myMeshName As String = mesh.Name
                Dim myMeshType As String = Nothing

                If myColorOption = 0 Then
                    If Not myMeshColor.ContainsKey(myMeshTag) Then
                        myMeshColor.Add(myMeshTag, myColorWheel(IdxC))
                        If DEBUG Then theLW.WriteLine("Mesh named: " + myMeshName + " Color set to: " + myMeshColor(myMeshTag).ToString())
                        If DEBUG > 1 Then theLW.WriteLine("Tag: " + myMeshTag.ToString())

                        IdxC = IdxC + 1
                        If IdxC >= myColorWheel.Length Then IdxC = 0
                    End If

                    mesh.Color = myMeshColor(myMeshTag)
                    theUFSession.Sf.DisplayMesh(myMeshTag)
                End If

                If myColorOption > 0 Then
                    Dim myCollector As CAE.MeshCollector = Nothing
                    myCollector = GetMeshCollector(mesh, myMeshType)

                    Dim myCollectorName As String

                    If myCollector Is Nothing Then
                        myCollectorTag = 0
                        myCollectorName = "None"
                        If DEBUG Then theLW.WriteLine("Can't get collector for " + myMeshType + " mesh named " + myMeshName + " because there is no mesh builder for this mesh")
                    Else
                        myCollectorTag = myCollector.Tag
                        myCollectorName = myCollector.Name
                    End If

                    Dim myPhysical As CAE.NamedPropertyTable = Nothing
                    Dim myType As String = Nothing
                    Dim myPhysicalName As String
                    Dim myMaterialName As String

                    If DEBUG > 1 Then theLW.WriteLine("Getting Physical Property for collector " + myCollectorName)

                    GetMeshCollectorPhysical(myCollector, myPhysical, myType)

                    If myPhysical Is Nothing Then
                        myPhysicalTag = 0
                        myPhysicalName = "None"
                        myMaterialTag = 0
                        myMaterialName = "None"

                        If DEBUG > 1 Then theLW.WriteLine("Can't get Material Properties for collector " + myCollectorName + " containing " + myMeshType + " mesh named " + myMeshName + " because there is no Physical Property table for this mesh")

                    Else
                        myPhysicalTag = myPhysical.Tag
                        myPhysicalName = myPhysical.Name

                        If DEBUG > 1 Then theLW.WriteLine("Getting Material Properties for collector " + myCollectorName + " which references a Physical Table named " + myPhysical.Name + " which is type " + myType)

                        Dim myMaterialOptions As MaterialOptions

                        If myType = "Laminate" Then
                            Dim myLaminate As CAE.Laminate = CType(myPhysical, CAE.Laminate)
                            myMaterialTag = myLaminate.Tag
                            myMaterialName = myLaminate.Name
                            If DEBUG > 1 Then theLW.WriteLine(myPhysical.Name + " is a Laminate property " + myLaminate.Name + " Coloring as a no material property")
                        Else
                            myMaterialOptions = myPhysical.PropertyTable.GetPhysicalMaterialPropertyValue("material")

                            If myMaterialOptions.Material Is Nothing Then
                                If myMaterialOptions.MaterialInherited Then
                                    myMaterialTag = -1
                                    myMaterialName = "Inherited"
                                Else
                                    myMaterialTag = 0
                                    myMaterialName = "None"
                                End If
                            Else
                                myMaterialTag = myMaterialOptions.Material.Tag
                                myMaterialName = myMaterialOptions.Material.Name
                            End If
                        End If
                    End If

                    If myColorOption = 1 Then
                        If Not myCollectorColor.ContainsKey(myCollectorTag) Then
                            myCollectorColor.Add(myCollectorTag, myColorWheel(IdxC))
                            If DEBUG Then theLW.WriteLine("Meshes with Collector named: " + myCollectorName + " Color set to: " + myCollectorColor(myCollectorTag).ToString())

                            '' Modify the mesh collector color
                            'NXOpen.UF.UFObj.SetColor(myCollectorTag, myColorWheel(IdxC))
                            'theUFSession.Obj.SetColor(myCollectorTag, myColorWheel(IdxC))

                            IdxC = IdxC + 1
                            If IdxC >= myColorWheel.Length Then IdxC = 0

                        End If
                    End If

                    If myColorOption = 2 Then
                        If Not myPhysicalColor.ContainsKey(myPhysicalTag) Then
                            myPhysicalColor.Add(myPhysicalTag, myColorWheel(IdxC))
                            If DEBUG Then theLW.WriteLine("Meshes with Physical named: " + myPhysicalName + " Color set to: " + myPhysicalColor(myPhysicalTag).ToString())

                            '' Modify the mesh collector color
                            'NXOpen.UF.UFObj.SetColor(myPhysicalTag, myColorWheel(IdxC))
                            'theUFSession.Obj.SetColor(myPhysicalTag, myColorWheel(IdxC))

                            IdxC = IdxC + 1
                            If IdxC >= myColorWheel.Length Then IdxC = 0

                        End If
                    End If

                    If myColorOption = 3 Then
                        If Not myMaterialColor.ContainsKey(myMaterialTag) Then
                            myMaterialColor.Add(myMaterialTag, myColorWheel(IdxC))
                            If DEBUG Then theLW.WriteLine("Meshes with Material named: " + myMaterialName + " Color set to: " + myMaterialColor(myMaterialTag).ToString())

                            '' Modify the mesh collector color
                            'NXOpen.UF.UFObj.SetColor(myMaterialTag, myColorWheel(IdxC))
                            'theUFSession.Obj.SetColor(myMaterialTag, myColorWheel(IdxC))

                            IdxC = IdxC + 1
                            If IdxC >= myColorWheel.Length Then IdxC = 0

                        End If
                    End If
                End If


                ' Modify the color of the individual mesh since the collector color cannot be changed above
                If myColorOption = 1 Then mesh.Color = myCollectorColor(myCollectorTag)
                If myColorOption = 2 Then mesh.Color = myPhysicalColor(myPhysicalTag)
                If myColorOption = 3 Then mesh.Color = myMaterialColor(myMaterialTag)
                theUFSession.Sf.DisplayMesh(myMeshTag)

            End If

            theUFSession.Obj.CycleObjsInPart(basePart.Tag, NXOpen.UF.UFConstants.UF_sfem_mesh_type, objectTag)
        Loop

        If DEBUG Then
            If myColorOption = 0 Then theLW.WriteLine(" Part has " + myMeshColor.Count.ToString() + " Meshes " + vbNewLine + vbNewLine)
            If myColorOption = 1 Then theLW.WriteLine(" Part has " + myCollectorColor.Count.ToString() + " Collectors " + vbNewLine + vbNewLine)
            If myColorOption = 2 Then theLW.WriteLine(" Part has " + myPhysicalColor.Count.ToString() + " Physical Tables " + vbNewLine + vbNewLine)
            If myColorOption = 3 Then theLW.WriteLine(" Part has " + myMaterialColor.Count.ToString() + " Material Tables " + vbNewLine + vbNewLine)
        End If

    End Sub

    Public Function GetMeshCollector(ByRef mesh As CAE.Mesh, ByRef type As String) As CAE.MeshCollector

        Dim meshCollector As CAE.MeshCollector = Nothing
        type = Nothing

        Dim theSession As Session = Session.GetSession()
        Dim basePart As BasePart = mesh.OwningPart()

        Dim elementTypeBuilder As CAE.ElementTypeBuilder = Nothing
        Dim builder As Builder = Nothing

        If TypeOf basePart Is CAE.FemPart Then

            Dim femPart As CAE.FemPart = CType(basePart, CAE.FemPart)
            Dim fEModel As CAE.FEModel = CType(femPart.BaseFEModel(), CAE.FEModel)
            Dim meshManager As CAE.MeshManager = CType(fEModel.Find("MeshManager"), CAE.MeshManager)

            'theLW.WriteLine("Mesh Name: " + mesh.Name)

            If TypeOf mesh Is CAE.Mesh0d Then

                'theLW.WriteLine("Type is Mesh0d ")

                Dim mesh0dBuilder As CAE.Mesh0dBuilder = meshManager.CreateMesh0dBuilder(CType(mesh, CAE.Mesh0d))
                elementTypeBuilder = mesh0dBuilder.ElementType()
                builder = mesh0dBuilder
                type = "Mesh0d"

            ElseIf TypeOf mesh Is CAE.Mesh1d Then

                'theLW.WriteLine("Type is Mesh1d ")

                Dim mesh1dBuilder As CAE.Mesh1dBuilder = meshManager.CreateMesh1dBuilder(CType(mesh, CAE.Mesh1d))
                elementTypeBuilder = mesh1dBuilder.ElementType()
                builder = mesh1dBuilder
                type = "Mesh1d"

            ElseIf TypeOf mesh Is CAE.Mesh2d Then

                'theLW.WriteLine("Type is Mesh2d ")

                Dim mesh2dBuilder As CAE.Mesh2dBuilder = meshManager.CreateMesh2dBuilder(CType(mesh, CAE.Mesh2d))
                elementTypeBuilder = mesh2dBuilder.ElementType()
                builder = mesh2dBuilder
                type = "Mesh2d"

            ElseIf TypeOf mesh Is CAE.Mesh3d Then

                'theLW.WriteLine("Type is Mesh3d ")

                Dim mesh3dBuilder As CAE.Mesh3dTetBuilder = meshManager.CreateMesh3dTetBuilder(CType(mesh, CAE.Mesh3d))
                elementTypeBuilder = mesh3dBuilder.ElementType()
                builder = mesh3dBuilder
                type = "Mesh3d"

            ElseIf TypeOf mesh Is CAE.Mesh2dFree Then

                'theLW.WriteLine("Type is Mesh2dFree ")

                Dim mesh2dBuilder As CAE.Mesh2dBuilder = meshManager.CreateMesh2dBuilder(CType(mesh, CAE.Mesh2d))
                elementTypeBuilder = mesh2dBuilder.ElementType()
                builder = mesh2dBuilder
                type = "Mesh2dFree"

            ElseIf TypeOf mesh Is CAE.SweptMesh Then

                'theLW.WriteLine("Type is SweptMesh ")

                Dim mesh3dHexBuilder As CAE.Mesh3dHexBuilder = meshManager.CreateMesh3dHexBuilder(CType(mesh, CAE.SweptMesh))
                elementTypeBuilder = mesh3dHexBuilder.ElementType()
                builder = mesh3dHexBuilder
                type = "SweptMesh"

            ElseIf TypeOf mesh Is CAE.Mesh Then

                'theLW.WriteLine("Type is Mesh ")

                'Dim mesh3dHexBuilder As CAE.Mesh3dHexBuilder = meshManager.CreateMesh3dHexBuilder(CType(mesh, CAE.SweptMesh))
                'elementTypeBuilder = mesh3dHexBuilder.ElementType()
                'builder = mesh3dHexBuilder
                type = "Mesh"

            End If

            If elementTypeBuilder IsNot Nothing Then
                meshCollector = elementTypeBuilder.DestinationCollector.ElementContainer
            End If

            If builder IsNot Nothing Then
                builder.Destroy()
            End If
        End If

        Return meshCollector

    End Function

    Public Sub GetMeshCollectorPhysical(ByRef meshCollector As CAE.MeshCollector, ByRef physical As CAE.NamedPropertyTable, ByRef type As String)
        theLW.Open()
        physical = Nothing
        type = Nothing

        If meshCollector Is Nothing Then
            Return
        End If

        Dim baseFemPart As CAE.BaseFemPart = Nothing
        Dim iFEModel As CAE.IFEModel = Nothing

        Dim basePart As BasePart = meshCollector.OwningPart()

        If TypeOf basePart Is CAE.BaseFemPart Then baseFemPart = CType(basePart, CAE.BaseFemPart)

        Dim baseFEModel As CAE.BaseFEModel = baseFemPart.BaseFEModel()

        Dim meshManager As CAE.MeshManager = CType(baseFEModel.MeshManager(), CAE.MeshManager)
        Dim meshCollectorBuilder As CAE.MeshCollectorBuilder = meshManager.CreateCollectorBuilder(meshCollector, "")

        Dim propTable As CAE.PropertyTable = meshCollectorBuilder.PropertyTable()

        If propTable IsNot Nothing Then
            Dim propCnt As Integer = propTable.GetPropertyCount
            Dim propIdx As Integer = 0

            If DEBUG > 1 Then theLW.WriteLine("property count =  " + propCnt.ToString())

            Do While propIdx < propCnt

                Dim propName As String = propTable.GetPropertyNameByIndex(propIdx)
                If DEBUG > 1 Then theLW.WriteLine("propName = " + propName)
                Dim propType As String = TestPropType(propTable, propName)
                If DEBUG > 1 Then theLW.WriteLine("propType = " + propType)

                If (String.Compare(propType, "NamedPropertyTable") = 0) Then
                    physical = propTable.GetNamedPropertyTablePropertyValue(propName)

                    If physical IsNot Nothing Then
                        If DEBUG > 1 Then theLW.WriteLine("Name = " + physical.Name)
                        type = physical.DescriptorType
                        If DEBUG > 1 Then theLW.WriteLine("type = " & type)
                        propIdx = propCnt
                    End If

                End If
                propIdx = propIdx + 1

            Loop

        End If

        meshCollectorBuilder.Destroy()
    End Sub

    Public Function TestPropType(ByRef pt As CAE.PropertyTable, ByRef p As String) As String
        Try
            pt.GetAxisPropertyValue(p)

            Return "Axis"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetBooleanPropertyValue(p)
            Return "Boolean"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetCaeSectionPropertyValue(p)
            Return "CaeSection"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetCoordinateSystemPropertyValue(p)
            Return "CoordinateSystem"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        'Try
        '    pt.GetDateTimePropertyValue(p)
        '    Return "DateTime"

        'Catch ex As ApplicationException
        '    ' Ignore failures 
        'End Try
        Try
            pt.GetDoublePropertyValue(p)
            Return "Double"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try

            pt.GetFieldWrapperPropertyValue(p)
            Return "FieldWrapper"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetIntegerArrayPropertyValue(p)
            Return "IntegerArray"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetIntegerPropertyValue(p)
            Return "Integer"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetMatrixPropertyValue(p)
            Return "Matrix"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetNamedPropertyTableArrayPropertyValue(p)
            Return "NamedPropertyTableArray"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetNamedPropertyTablePropertyValue(p)
            Return "NamedPropertyTable"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetPhysicalMaterialPropertyValue(p)
            Return "PhysicalMaterial"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetPointPropertyValue(p)
            Return "Point"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetReferencePropertyValue(p)
            Return "Reference"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try

            pt.GetScalarArrayPropertyValue(p)
            Return "ScalarArray"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetScalarFieldPropertyValue(p)
            Return "ScalarField"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetScalarFieldWrapperPropertyValue(p)
            Return "ScalarFieldWrapper"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try

            pt.GetScalarPropertyValue(p)
            Return "Scalar"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetScalarTablePropertyValue(p)
            Return "ScalarTable"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetStringPropertyValue(p)
            Return "String"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetTextPropertyValue(p)
            Return "Text"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetVectorFieldWrapperPropertyValue(p)
            Return "VectorFieldWrapper"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try
        Try
            pt.GetVectorPropertyValue(p)
            Return "Vector"

        Catch ex As ApplicationException
            ' Ignore failures 
        End Try

        Return Nothing

    End Function

    Public Sub GetPropTablePropNames(ByRef propTable As CAE.PropertyTable)

        If propTable Is Nothing Then
            theLW.WriteLine("property table is empty ")
        End If

        If propTable IsNot Nothing Then
            Dim propCnt As Integer = propTable.GetPropertyCount
            Dim propIdx As Integer = 0

            theLW.WriteLine("property count =  " + propCnt.ToString())

            Do While propIdx < propCnt


                Dim propName As String = propTable.GetPropertyNameByIndex(propIdx)
                theLW.WriteLine("property [" + propIdx.ToString() + "] is named = " + propName + " " & TestPropType(propTable, propName))
                propIdx = propIdx + 1

            Loop

        End If
    End Sub

    '==============================================================================
    '  WARNING!!  This file is overwritten by the Block Styler while generating
    '  the automation code. Any modifications to this file will be lost after
    '  generating the code again.
    '
    '       Filename:  D:\NX\NX_Open\FE_Color\enumBlock.vb
    '
    '        This file was generated by the NX Block Styler
    '        Created by: tsbernar
    '              Version: NX 6
    '              Date: 01-30-2009  (Format: mm-dd-yyyy)
    '              Time: 13:32 (Format: hh-mm)
    '
    '==============================================================================

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
    'Option Strict Off
    'Imports System
    'Imports NXOpen
    'Imports NXOpen.BlockStyler

    '------------------------------------------------------------------------------
    'Represents Block Styler application class
    '------------------------------------------------------------------------------
    Public Class enumBlock
        'class members
        Private Shared theSession As Session
        Private Shared theUI As UI
        Public Shared theenumBlock As enumBlock
        Public m_colorOption As Integer
        Public m_listOption As Integer
        Public m_basePart As BasePart = Nothing
        Private theDialogName As String
        Private theDialog As NXOpen.BlockStyler.BlockDialog
        Private group0 As NXOpen.BlockStyler.UIBlock ' Block type: Group
        Private enum0 As NXOpen.BlockStyler.UIBlock ' Block type: Enumeration
        Private group01 As NXOpen.BlockStyler.UIBlock ' Block type: Group
        Private toggle0 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle


#Region "Block Styler Dialog Designer generator code"
        '------------------------------------------------------------------------------
        'Constructor for NX Styler class
        '------------------------------------------------------------------------------
        Public Sub New(ByVal part As BasePart)
            Try

                m_basePart = part
                theSession = Session.GetSession()
                theUI = UI.GetUI()
                theDialogName = "enumBlock.dlx"
                theDialog = theUI.CreateDialog(theDialogName)
                theDialog.AddApplyHandler(AddressOf apply_cb)
                theDialog.AddOkHandler(AddressOf ok_cb)
                theDialog.AddUpdateHandler(AddressOf update_cb)
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
        '        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
        '        2) Invoke the Shared Library through File->Execute->NX Open menu.
        '
        '------------------------------------------------------------------------------
        'Public Shared Sub Main()
        '    Try

        '        theenumBlock = New enumBlock()
        '        ' The following method shows the dialog immediately
        '        theenumBlock.Show()

        '    Catch ex As Exception

        '        '---- Enter your exception handling code here -----
        '        theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        '    Finally
        '        theenumBlock.Dispose()
        '    End Try
        'End Sub
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
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
        End Function

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

            Dim myEnumOptions() As String = myColorOptions

            Try

                group0 = theDialog.TopBlock.FindBlock("group0")
                enum0 = theDialog.TopBlock.FindBlock("enum0")
                group01 = theDialog.TopBlock.FindBlock("group01")
                toggle0 = theDialog.TopBlock.FindBlock("toggle0")

                ' Set the property list 
                Dim propertyList As BlockStyler.PropertyList

                propertyList = group0.GetProperties()
                propertyList.SetString("Label", "Color Elements By")

                propertyList = enum0.GetProperties()
                propertyList.SetLogical("LabelVisibility", 0)
                propertyList.SetEnum("PresentationStyle", 1)
                'propertyList.SetEnum("Value", myEnumOptions.Length)
                propertyList.SetEnumMembers("Value", myColorOptions)

                propertyList = group01.GetProperties()
                propertyList.SetString("Label", "Summary")
                propertyList.SetLogical("Expanded", 0)

                propertyList = toggle0.GetProperties()
                propertyList.SetString("Label", "Write Detailed Summary to List Window")
                propertyList.SetLogical("RetainValue", 0)


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
            Try

                '---- Enter your callback code here -----
                enum0 = theDialog.TopBlock.FindBlock("enum0")
                toggle0 = theDialog.TopBlock.FindBlock("toggle0")

                ' Retrieve the enum0 property list 
                Dim propertyList As BlockStyler.PropertyList
                propertyList = enum0.GetProperties()

                m_colorOption = propertyList.GetEnum("Value")
                'colorOption = propertyList.GetEnumAsString("Value")
                'theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, colorOption)

                propertyList = toggle0.GetProperties()

                m_listOption = propertyList.GetLogical("Value")
                'colorOption = propertyList.GetEnumAsString("Value")
                'theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, listOption)

                DoIt(m_basePart, m_colorOption, m_listOption)

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
            apply_cb = 0
        End Function

        '------------------------------------------------------------------------------
        'Callback Name: update_cb
        '------------------------------------------------------------------------------
        Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
            Try

                If block Is enum0 Then
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
            Try

                '---- Enter your callback code here -----
                apply_cb()

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
            ok_cb = 0
        End Function

    End Class

End Module

' NX Color Palette
'Index   Name
'-----   ---------------------
'   1    White
'   2    Pale Weak Yellow
'   3    Pale Dull Yellow
'   4    Light Faded Yellow
'   5    Light Hard Yellow
'   6    Yellow
'   7    Pale Weak Cyan
'   8    Pale Weak Green
'   9    Pale Dull Spring
'  10    Light Spring Yellow
'  11    Light Yellow Spring
'  12    Yellow Yellow Spring
'  13    Pale Dull Cyan
'  14    Pale Dull Teal
'  15    Pale Dull Green
'  16    Light Spring Green
'  17    Light Hard Spring
'  18    Spring Spring Yellow
'  19    Light Faded Cyan
'  20    Light Teal Cyan
'  21    Light Teal Green
'  22    Light Faded Green
'  23    Light Green Spring
'  24    Spring Spring Green
'  25    Light Hard Cyan
'  26    Light Cyan Teal
'  27    Light Hard Teal
'  28    Light Green Teal
'  29    Light Hard Green
'  30    Green Green Spring
'  31    Cyan
'  32    Cyan Cyan Teal
'  33    Teal Teal Cyan
'  34    Teal Teal Green
'  35    Green Green Teal
'  36    Green
'  37    Pale Weak Magenta
'  38    Pale Weak Red
'  39    Pale Dull Orange
'  40    Light Orange Yellow
'  41    Light Yellow Orange
'  42    Yellow Yellow Orange
'  43    Pale Weak Blue
'  44    Pale Gray
'  45    Light Weak Yellow
'  46    Light Dull Yellow
'  47    Medium Faded Yellow
'  48    Dark Hard Yellow
'  49    Pale Dull Azure
'  50    Light Weak Cyan
'  51    Light Weak Green
'  52    Light Dull Spring
'  53    Medium Spring Yellow
'  54    Dark Yellow Spring
'  55    Light Azure Cyan
'  56    Light Dull Cyan
'  57    Light Dull Teal
'  58    Light Dull Green
'  59    Medium Spring Green
'  60    Dark Hard Spring
'  61    Light Cyan Azure
'  62    Medium Faded Cyan
'  63    Medium Teal Cyan
'  64    Medium Teal Green
'  65    Medium Faded Green
'  66    Dark Green Spring
'  67    Cyan Cyan Azure
'  68    Dark Hard Cyan
'  69    Dark Cyan Teal
'  70    Dark Hard Teal
'  71    Dark Green Teal
'  72    Dark Hard Green
'  73    Pale Dull Magenta
'  74    Pale Dull Pink
'  75    Pale Dull Red
'  76    Light Orange Red
'  77    Light Hard Orange
'  78    Orange Orange Yellow
'  79    Pale Dull Violet
'  80    Light Weak Magenta
'  81    Light Weak Red
'  82    Light Dull Orange
'  83    Medium Orange Yellow
'  84    Dark Yellow Orange
'  85    Pale Dull Blue
'  86    Light Weak Blue
'  87    Light Gray
'  88    Medium Weak Yellow
'  89    Dark Dull Yellow
'  90    Dark Faded Yellow
'  91    Light Azure Blue
'  92    Light Dull Azure
'  93    Medium Weak Cyan
'  94    Medium Weak Green
'  95    Dark Dull Spring
'  96    Dark Spring Yellow
'  97    Light Hard Azure
'  98    Medium Azure Cyan
'  99    Dark Dull Cyan
' 100    Dark Dull Teal
' 101    Dark Dull Green
' 102    Dark Spring Green
' 103    Azure Azure Cyan
' 104    Dark Cyan Azure
' 105    Dark Faded Cyan
' 106    Dark Teal Cyan
' 107    Dark Teal Green
' 108    Dark Faded Green
' 109    Light Faded Magenta
' 110    Light Pink Magenta
' 111    Light Pink Red
' 112    Light Faded Red
' 113    Light Red Orange
' 114    Orange Orange Red
' 115    Light Violet Magenta
' 116    Light Dull Magenta
' 117    Light Dull Pink
' 118    Light Dull Red
' 119    Medium Orange Red
' 120    Dark Hard Orange
' 121    Light Violet Blue
' 122    Light Dull Violet
' 123    Medium Weak Magenta
' 124    Medium Weak Red
' 125    Dark Dull Orange
' 126    Dark Orange Yellow
' 127    Light Faded Blue
' 128    Light Dull Blue
' 129    Medium Weak Blue
' 130    Dark Gray
' 131    Dark Weak Yellow
' 132    Obscure Dull Yellow
' 133    Light Blue Azure
' 134    Medium Azure Blue
' 135    Dark Dull Azure
' 136    Dark Weak Cyan
' 137    Dark Weak Green
' 138    Obscure Dull Spring
' 139    Azure Azure Blue
' 140    Dark Hard Azure
' 141    Dark Azure Cyan
' 142    Obscure Dull Cyan
' 143    Obscure Dull Teal
' 144    Obscure Dull Green
' 145    Light Hard Magenta
' 146    Light Magenta Pink
' 147    Light Hard Pink
' 148    Light Red Pink
' 149    Light Hard Red
' 150    Red Red Orange
' 151    Light Magenta Violet
' 152    Medium Faded Magenta
' 153    Medium Pink Magenta
' 154    Medium Pink Red
' 155    Medium Faded Red
' 156    Dark Red Orange
' 157    Light Hard Violet
' 158    Medium Violet Magenta
' 159    Dark Dull Magenta
' 160    Dark Dull Pink
' 161    Dark Dull Red
' 162    Dark Orange Red
' 163    Light Blue Violet
' 164    Medium Violet Blue
' 165    Dark Dull Violet
' 166    Dark Weak Magenta
' 167    Dark Weak Red
' 168    Obscure Dull Orange
' 169    Light Hard Blue
' 170    Medium Faded Blue
' 171    Dark Dull Blue
' 172    Dark Weak Blue
' 173    Obscure Gray
' 174    Obscure Weak Yellow
' 175    Blue Blue Azure
' 176    Dark Blue Azure
' 177    Dark Azure Blue
' 178    Obscure Dull Azure
' 179    Obscure Weak Cyan
' 180    Obscure Weak Green
' 181    Magenta
' 182    Magenta Magenta Pink
' 183    Pink Pink Magenta
' 184    Pink Pink Red
' 185    Red Red Pink
' 186    Red
' 187    Magenta Magenta Violet
' 188    Dark Hard Magenta
' 189    Dark Magenta Pink
' 190    Dark Hard Pink
' 191    Dark Red Pink
' 192    Dark Hard Red
' 193    Violet Violet Magenta
' 194    Dark Magenta Violet
' 195    Dark Faded Magenta
' 196    Dark Pink Magenta
' 197    Dark Pink Red
' 198    Dark Faded Red
' 199    Violet Violet Blue
' 200    Dark Hard Violet
' 201    Dark Violet Magenta
' 202    Obscure Dull Magenta
' 203    Obscure Dull Pink
' 204    Obscure Dull Red
' 205    Blue Blue Violet
' 206    Dark Blue Violet
' 207    Dark Violet Blue
' 208    Obscure Dull Violet
' 209    Obscure Weak Magenta
' 210    Obscure Weak Red
' 211    Blue
' 212    Dark Hard Blue
' 213    Dark Faded Blue
' 214    Obscure Dull Blue
' 215    Obscure Weak Blue
' 216    Black
