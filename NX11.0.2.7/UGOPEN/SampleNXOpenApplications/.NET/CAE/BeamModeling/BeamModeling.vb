' NX 7.5.4.3
' BeamSection.vb - This program provides an example of using NX/Open API to replace old beam section user functions.
'
'UFUN name                          Equivalent example function
'
'UF_SF_analyse_thin_section         AskSectionProperties
'UF_SF_analyse_solid_section        AskSectionProperties
'UF_SF_ask_beam_end_mass            PhysicalProperties
'UF_SF_ask_mesh_section             LocateSectionByMesh
'UF_SF_ask_section_data             AskSectionProperties & AskSectionData
'UF_SF_ask_section_offset           AskSectionOffset
'UF_SF_ask_section_properties       AskSectionProperties
'UF_SF_apply_beam_end_mass          PhysicalProperties
'UF_SF_apply_offset                 ApplyOffset
'UF_SF_create_section               CreateStandardBeamSection
'UF_SF_edit_beam_orientation        EditBeamOrientation
'UF_SF_edit_section                 refer to CreateStandardBeamSection
'UF_SF_link_section                 PhysicalProperties
'UF_SF_locate_named_section         LocateSectionByName
'UF_SF_locate_section               LocateSectionByMesh
'UF_SF_unlink_section               PhysicalProperties
'
'Note: This test case covers the following processes (with the FEM set to NX Nastran language)
'      1. Create test model parts, including CAD part, CAE geometries, FEM part, idealized part, meshes
'      2. Create beam sections, including standard section, face-of-solid section, general geometry section, user defined properties section
'      3. Edit beam mesh physical properties, including assigning beam sections to beam mesh, applying beam end mass
'      4. Edit beam mesh associated data, including beam orientation, beam offset
'      5. Query the dimensions of a standard section or the geometric properties (area, centroid, area moments of inertia etc.) of any
'         existing beam section.
'
' 

Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.CAE
Imports NXOpen.Utilities
Imports NXOpen.UF.UFObj
Imports NXOpen.CAE.BeamSection.Properties

Module BeamSection

    Structure SectionProp

        Dim neutralName As String
        Dim myValue As Double
        Dim myUnit As Unit

    End Structure



    Dim theSession As Session = Session.GetSession()
    Dim workFemPart As CAE.FemPart
    Dim fEModel As CAE.FEModel

    Dim theLW As NXOpen.ListingWindow = theSession.ListingWindow()

    '-----------------------------------------------------------------------------------
    'The main function
    '
    'Remark:
    '   
    '-----------------------------------------------------------------------------------
    Public Sub Main()

        theLW.Open()

        CreateFemPart()

        workFemPart = CType(theSession.Parts.BaseWork, CAE.FemPart)
        fEModel = CType(workFemPart.FindObject("FEModel"), CAE.FEModel)

        Dim sectionTags() As Tag = BeamSectionOperation()

        Dim meshManager As CAE.MeshManager = CType(fEModel.Find("MeshManager"), CAE.MeshManager)

        Dim mesh1 As CAE.Mesh = CType(meshManager.FindObject("Mesh[1d_mesh(1)]"), CAE.Mesh)
        PhysicalProperties(mesh1, sectionTags(0))
        MeshAssociatedDataOperation(mesh1)

        Dim mesh2 As CAE.Mesh = CType(meshManager.FindObject("Mesh[1d_mesh(2)]"), CAE.Mesh)
        PhysicalProperties(mesh2, sectionTags(1))
        MeshAssociatedDataOperation(mesh2)

        Dim mesh3 As CAE.Mesh = CType(meshManager.FindObject("Mesh[1d_mesh(3)]"), CAE.Mesh)
        PhysicalProperties(mesh3, sectionTags(2))
        MeshAssociatedDataOperation(mesh3)

        Dim mesh4 As CAE.Mesh = CType(meshManager.FindObject("Mesh[1d_mesh(4)]"), CAE.Mesh)
        PhysicalProperties(mesh4, sectionTags(3))
        MeshAssociatedDataOperation(mesh4)

    End Sub

    Public Function GetUnloadOption(ByVal dummy As String) As Integer

        'Unloads the image when the NX session terminates
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination

        '----Other unload options-------
        'Unloads the image immediately after execution within NX
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately

        'Unloads the image explicitly, via an unload dialog
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly
        '-------------------------------

    End Function

    '-----------------------------------------------------------------------------------
    'This function provides the example of creating section and querying beam section properties
    '
    'Remark:
    '   
    '-----------------------------------------------------------------------------------
    Function BeamSectionOperation()

        Dim sectionTags() As Tag = CreateSections()

        Dim namedSection As CAE.BeamSection
        namedSection = LocateSectionByName("tube instance")

        AskSectionProperties(sectionTags(0)) 'Query properties of the standard section

        BeamSectionOperation = sectionTags

    End Function

    '-----------------------------------------------------------------------------------
    'This function provides an example of how to create beam sections, including standard
    ' beam section( solver built-in section),face-of-solid section and general 
    ' geometry section (replaces user-defined thin wall section that existed before NX7.5)
    '
    'Remark:
    '   
    '-----------------------------------------------------------------------------------
    Function CreateSections()

        Dim sectionTags(3) As Tag

        Dim sectionType As String = "Tube"   'In the documentation, this is called Descriptor Name
        Dim sectionName As String = "tube instance"

        Dim outerRadius As SectionProp
        outerRadius.neutralName = "ro" ' See documentation to get the neutral names for displayed names like "D1M1", "DIM2" etc.
        outerRadius.myValue = "1"
        outerRadius.myUnit = CType(workFemPart.UnitCollection.FindObject("CentiMeter"), Unit)

        Dim innerRadius As SectionProp
        innerRadius.neutralName = "ri"
        innerRadius.myValue = "0.5"
        innerRadius.myUnit = CType(workFemPart.UnitCollection.FindObject("CentiMeter"), Unit)

        Dim tubeProps(2) As SectionProp
        tubeProps(0) = outerRadius
        tubeProps(1) = innerRadius

        sectionTags(0) = CreateStandardBeamSection(sectionType, sectionName, tubeProps)


        sectionTags(1) = CreateFaceOfSoildBeamSection()

        sectionTags(2) = CreateGeneralGeometryBeamSection()

        Dim area As SectionProp
        area.neutralName = "Solid Area"
        area.myValue = "200"
        area.myUnit = CType(workFemPart.UnitCollection.FindObject("MilliMeter"), Unit)

        Dim inertiaY As SectionProp
        inertiaY.neutralName = "Iy"
        inertiaY.myValue = "200"
        inertiaY.myUnit = CType(workFemPart.UnitCollection.FindObject("MilliMeterFourth"), Unit)

        Dim propSectionProps(2) As SectionProp
        propSectionProps(0) = area
        propSectionProps(1) = inertiaY

        Dim stressRecoveryPoints(3) As Point2d
        stressRecoveryPoints(0) = New Point2d(0.5, 1.0)
        stressRecoveryPoints(1) = New Point2d(2.0, 3.1)
        stressRecoveryPoints(2) = New Point2d(4.0, 5.5)

        sectionTags(3) = CreateUserDefinedPropertiesBeamSection(sectionName, propSectionProps, stressRecoveryPoints)

        CreateSections = sectionTags

    End Function

    '-----------------------------------------------------------------------------------
    'This function is the replacement of UFSf.CreateSection, for creating a statdard section specifying dimensions.
    '
    'Remark:
    '   If you need to create face-of-solid section or general geometry section (from sketch),
    '   please call CreateFaceOfSoildBeamSection or CreateGeneralGeometryBeamSection respectively.
    '-----------------------------------------------------------------------------------
    Function CreateStandardBeamSection(ByVal sectionType As String, ByVal sectionName As String, ByVal sectionProps() As SectionProp)

        Dim nullCAE_StandardBeamSection As CAE.StandardBeamSection = Nothing

        Dim standardBeamSectionBuilder As CAE.StandardBeamSectionBuilder
        standardBeamSectionBuilder = fEModel.BeamSections.CreateStandardBeamSectionBuilder(nullCAE_StandardBeamSection)

        standardBeamSectionBuilder.DescriptorName = sectionType

        Dim propertyTable As CAE.PropertyTable = standardBeamSectionBuilder.PropertyTable

        standardBeamSectionBuilder.SectionName = sectionName

        For index As Integer = 0 To UBound(sectionProps) - LBound(sectionProps) - 1
            Dim dimPropName As String = sectionProps(index).neutralName
            Dim dimValue As Double = sectionProps(index).myValue
            Dim dimUnit As Unit = sectionProps(index).myUnit
            propertyTable.SetScalarWithDataPropertyValue(dimPropName, dimValue.ToString(), dimUnit)
        Next

        Dim standardBeamSection As StandardBeamSection = standardBeamSectionBuilder.Commit()

        standardBeamSectionBuilder.Destroy()

        ' an example showing how to query the dimension value for a standard beam section
        QueryTubeBeamSectionDimensions(standardBeamSection.Tag)

        CreateStandardBeamSection = standardBeamSection.Tag

    End Function

    Function QueryTubeBeamSectionDimensions(ByVal sectionTag As Tag)

        Dim standardBeamSection As StandardBeamSection = NXObjectManager.Get(sectionTag)

        theLW.WriteLine(" ")
        theLW.WriteLine("Information from Function <QueryTubeBeamSectionDimensions>:")
        theLW.WriteLine("section name:          " + standardBeamSection.Name)

        Dim propertyTable As CAE.PropertyTable = standardBeamSection.PropertyTable

        Dim numProperties As Integer = propertyTable.GetPropertyCount()

        ' In this case, "ro", "ri" are the neutral names of beam section dimensions
        ' "DIM1", "DIM2" are the display names of the beam section dimensions in the specified solver (NXNastran, in this example)
        ' Please refer to the illustrations on NX beam section dialogs or NX Online help to understand what the dimension represents
        ' and  to the related NX CAE NXOPEN documentation to know the mapping between neutral names
        ' and display names

        For index As Integer = 0 To numProperties - 1
            Dim propName As String = propertyTable.GetPropertyNameByIndex(index)

            If (propName = "ro") Then

                Dim dimUnit As Unit = Nothing
                Dim dimValue As Double = 0

                ' note: the dim value returned is a CAE formatted value, which means it may not be equal to
                ' your input. in this case, the CAE base unit is "Millimeter", so the returned dimValue is "10"
                ' instead of "1"
                propertyTable.GetScalarWithDataPropertyValue(propName, dimValue, dimUnit)
                Dim msg As String = "Outer radius(DIM1) = " + dimValue.ToString() + " MilliMeter"
                theLW.WriteLine(msg)

            ElseIf (propName = "ri") Then

                Dim dimUnit As Unit = Nothing
                Dim dimValue As Double = 0
                propertyTable.GetScalarWithDataPropertyValue(propName, dimValue, dimUnit)
                Dim msg As String = "Inner radius(DIM2) = " + dimValue.ToString() + " MilliMeter"
                theLW.WriteLine(msg)
            Else

                'Do nothing

            End If

        Next

    End Function

    '-----------------------------------------------------------------------------------
    'This function is to create solid beam section
    '-----------------------------------------------------------------------------------
    Function CreateFaceOfSoildBeamSection() As Tag

        Dim nullCAE_UserDefinedSolidBeamSection As CAE.UserDefinedSolidBeamSection = Nothing

        Dim userDefinedSolidBeamSectionBuilder As CAE.UserDefinedSolidBeamSectionBuilder
        userDefinedSolidBeamSectionBuilder = fEModel.BeamSections.CreateUserDefinedSolidBeamSectionBuilder(nullCAE_UserDefinedSolidBeamSection)

        userDefinedSolidBeamSectionBuilder.DescriptorName = "User Defined Solid"

        userDefinedSolidBeamSectionBuilder.SectionName = "Face of Solid(1)"
        Dim cAEBody As CAE.CAEBody = CType(workFemPart.FindObject("CAE_Body(1)"), CAE.CAEBody)
        Dim cAEFace As CAE.CAEFace = CType(cAEBody.FindObject("CAE_Face(2)"), CAE.CAEFace)
        userDefinedSolidBeamSectionBuilder.SolidFace.Value = cAEFace

        userDefinedSolidBeamSectionBuilder.DirectionType = CAE.BeamSection.DirectionOption.Horizontal

        Dim point1Coord As Point3d = New Point3d(0, 2, 0.0)
        Dim point1 As Point = workFemPart.Points.CreatePoint(point1Coord)

        Dim point2Coord As Point3d = New Point3d(1, 1, 1)
        Dim point2 As Point = workFemPart.Points.CreatePoint(point2Coord)

        Dim direction As Direction
        direction = workFemPart.Directions.CreateDirection(point1, point2, SmartObject.UpdateOption.AfterModeling)
        userDefinedSolidBeamSectionBuilder.ReferenceVector = direction


        Dim points(3) As Point2d
        points(0) = New Point2d(-1, 24)
        points(1) = New Point2d(-25, 0)
        points(2) = New Point2d(-1, -24)
        points(3) = New Point2d(25, 0)
        userDefinedSolidBeamSectionBuilder.SetUserDefinedStressRecoveryPoints(points)

        Dim userDefinedSolidBeamSection As UserDefinedSolidBeamSection
        userDefinedSolidBeamSection = userDefinedSolidBeamSectionBuilder.Commit()

        userDefinedSolidBeamSectionBuilder.Destroy()

        CreateFaceOfSoildBeamSection = userDefinedSolidBeamSection.Tag

    End Function

    '-----------------------------------------------------------------------------------
    'This function is to create general geometry beam section
    '-----------------------------------------------------------------------------------
    Function CreateGeneralGeometryBeamSection()

        Dim nullCAE_GeneralGeometryBeamSection As CAE.GeneralGeometryBeamSection = Nothing

        Dim generalGeometryBeamSectionBuilder As CAE.GeneralGeometryBeamSectionBuilder
        generalGeometryBeamSectionBuilder = fEModel.BeamSections.CreateGeneralGeometryBeamSectionBuilder(nullCAE_GeneralGeometryBeamSection)

        generalGeometryBeamSectionBuilder.DescriptorName = "General Geometry"
        generalGeometryBeamSectionBuilder.SectionName = "General Geometry(1)"


        Dim sketchCurves As CAE.SketchCurves = CType(workFemPart.SketchCurves.FindObject("SketchCurves[SKETCH_000]"), CAE.SketchCurves)

        generalGeometryBeamSectionBuilder.Sketch = sketchCurves


        Dim generalGeometryBeamSection As GeneralGeometryBeamSection = generalGeometryBeamSectionBuilder.Commit()

        generalGeometryBeamSectionBuilder.Destroy()

        CreateGeneralGeometryBeamSection = generalGeometryBeamSection.Tag

    End Function


    '-----------------------------------------------------------------------------------
    'This function is to create user defined properties beam section
    '-----------------------------------------------------------------------------------
    Function CreateUserDefinedPropertiesBeamSection(ByVal sectionName As String, ByVal sectionProps() As SectionProp, ByVal stressRecoveryPoints() As Point2d)

        Dim nullCAE_StandardBeamSection As CAE.StandardBeamSection = Nothing

        Dim standardBeamSectionBuilder As CAE.StandardBeamSectionBuilder
        standardBeamSectionBuilder = fEModel.BeamSections.CreateStandardBeamSectionBuilder(nullCAE_StandardBeamSection)

        standardBeamSectionBuilder.DescriptorName = "Key In"

        Dim propertyTable As CAE.PropertyTable
        propertyTable = standardBeamSectionBuilder.PropertyTable

        standardBeamSectionBuilder.SectionName = "User Defined Properties(1)"

        For index As Integer = 0 To UBound(sectionProps) - LBound(sectionProps) - 1

            Dim dimPropName As String = sectionProps(index).neutralName
            Dim dimValue As Double = sectionProps(index).myValue
            Dim dimUnit As Unit = sectionProps(index).myUnit
            propertyTable.SetScalarWithDataPropertyValue(dimPropName, dimValue.ToString(), dimUnit)
        Next

        standardBeamSectionBuilder.SetUserDefinedStressRecoveryPoints(stressRecoveryPoints)

        Dim propertiesSection As StandardBeamSection
        propertiesSection = standardBeamSectionBuilder.Commit()

        standardBeamSectionBuilder.Destroy()
        CreateUserDefinedPropertiesBeamSection = propertiesSection.Tag

    End Function

    '-----------------------------------------------------------------------------------
    'This function is to locate a section given its name.
    '-----------------------------------------------------------------------------------
    Function LocateSectionByName(ByVal SectionName As String)

        Dim namedSection As CAE.BeamSection
        namedSection = CType(fEModel.BeamSections.FindObject("BeamSection[" + SectionName + "]"), CAE.BeamSection)     'the replacement of UF_SF_locate_named_section

        theLW.WriteLine(" ")
        theLW.WriteLine("Information From Function <LocateSectionByName>:")

        If namedSection Is Nothing Then
            theLW.WriteLine("Section " + "(" + sectionName + ")" + " is not found")
        Else
            theLW.WriteLine("Section " + "(" + sectionName + ")" + " is found")
        End If

        LocateSectionByName = namedSection

    End Function

    '-----------------------------------------------------------------------------------
    'This function is to locate fore section and aft section for given mesh.
    '-----------------------------------------------------------------------------------
    Function LocateSectionByMesh(ByVal mesh As Mesh)

        Dim sectionTags(2) As Tag

        Dim meshCollector As MeshCollector = CType(mesh.MeshCollector, MeshCollector)
        Dim meshCollectorPropTab As PropertyTable = meshCollector.ElementPropertyTable
        Dim meshColPhysPropTab As PhysicalPropertyTable = CType(meshCollectorPropTab.GetNamedPropertyTablePropertyValue("Beam Property"), PhysicalPropertyTable)
        Dim beamPropPropTab As PropertyTable = meshColPhysPropTab.PropertyTable
        Dim beamSectionOptions As CAE.BeamSectionOptions = beamPropPropTab.GetCaeSectionPropertyValue("section")

        Dim beamForeSection As CAE.BeamSection = beamSectionOptions.BeamForeSection  'the replacement of UF_SF_ask_mesh_section & UF_SF_locate_section
        sectionTags(0) = beamForeSection.Tag

        theLW.WriteLine(" ")
        theLW.WriteLine("Information From Function <LocateSectionByMesh>:")
        theLW.WriteLine("Fore Section of " + mesh.name.ToString + "  :" + beamForeSection.Name.ToString)

        LocateSectionByMesh = sectionTags

    End Function

    '-----------------------------------------------------------------------------------
    'This function is to query evaluated section properties.
    '-----------------------------------------------------------------------------------
    Sub AskSectionProperties(ByVal sectionTag As Tag)

        Dim queriedStandardBeamSectionProperties As CAE.BeamSection.Properties
        Dim standardBeamSection As StandardBeamSection = NXObjectManager.Get(sectionTag)
        queriedStandardBeamSectionProperties = standardBeamSection.SectionProperties   'the replacement of UF_SF_ask_section_properties & UF_SF_analyse_solid_section & UF_SF_analyse_thin_section


        Dim area As Double = queriedStandardBeamSectionProperties.Area
        Dim Iyy As Double = queriedStandardBeamSectionProperties.MomentInertiaYY
        Dim Iyz As Double = queriedStandardBeamSectionProperties.MomentInertiaYZ
        Dim Izz As Double = queriedStandardBeamSectionProperties.MomentInertiaZZ
        Dim principalAngle As Double = queriedStandardBeamSectionProperties.PrincipalAngle
        Dim principalMomentInertiaYY As Double = queriedStandardBeamSectionProperties.PrincipalMomentInertiaYY
        Dim principalMomentInertiaZZ As Double = queriedStandardBeamSectionProperties.PrincipalMomentInertiaZZ
        Dim torsionCoefficient As Double = queriedStandardBeamSectionProperties.TorsionCoefficient
        Dim warpingCoefficient As Double = queriedStandardBeamSectionProperties.WarpingCoefficient
        Dim yEccentricity As Double = queriedStandardBeamSectionProperties.YEccentricity
        Dim zEccentricity As Double = queriedStandardBeamSectionProperties.ZEccentricity

        theLW.WriteLine(" ")
        theLW.WriteLine("Information from Function <AskSectionProperties>")
        theLW.WriteLine("The evaluated section properties of beam section (" + standardBeamSection.Name + "):")
        theLW.WriteLine("Area:                      " + area.ToString)
        theLW.WriteLine("Iyy:                       " + Iyy.ToString)
        theLW.WriteLine("Iyz:                       " + Iyz.ToString)
        theLW.WriteLine("Izz:                       " + Izz.ToString)
        theLW.WriteLine("PrincipalAngle:            " + principalAngle.ToString)
        theLW.WriteLine("PrincipalMomentInertiaYY:  " + principalMomentInertiaYY.ToString)
        theLW.WriteLine("PrincipalMomentInertiaZZ:  " + principalMomentInertiaZZ.ToString)
        theLW.WriteLine("TorsionCoefficient:        " + torsionCoefficient.ToString)
        theLW.WriteLine("WarpingCoefficient:        " + warpingCoefficient.ToString)
        theLW.WriteLine("YEccentricity:             " + yEccentricity.ToString)
        theLW.WriteLine("ZEccentricity:             " + zEccentricity.ToString)


    End Sub

    '-----------------------------------------------------------------------------------
    'This function performs the operation on beam mesh collector physical properties, including
    'assign beam section and apply beam end mass
    'Remark:
    '   
    '-----------------------------------------------------------------------------------
    Sub PhysicalProperties(ByRef mesh As CAE.Mesh, ByVal sectionTag As Tag)

        Dim meshCollector As MeshCollector = CType(mesh.MeshCollector, MeshCollector)
        Dim meshCollectorPropTab As PropertyTable = meshCollector.ElementPropertyTable
        Dim meshColPhysPropTab As PhysicalPropertyTable = CType(meshCollectorPropTab.GetNamedPropertyTablePropertyValue("Beam Property"), PhysicalPropertyTable)
        Dim beamPropPropTab As PropertyTable = meshColPhysPropTab.PropertyTable

        Dim beamSectionOptions As BeamSectionOptions = workFemPart.NewBeamSectionOptions()

        beamSectionOptions.BeamSectionTapered = False

        Dim beamSection As CAE.BeamSection = NXObjectManager.Get(sectionTag)

        beamSectionOptions.BeamForeSection = beamSection    'the replacement of UF_SF_link_section

        'to remove the section assignment
        'beamSectionOptions.BeamForeSection = Nothing    'the replacement of UF_SF_unlink_section

        beamPropPropTab.SetCaeSectionPropertyValue("section", beamSectionOptions)
        beamSectionOptions.Dispose()

        Dim meshLinkedSectionTags() As Tag
        meshLinkedSectionTags = LocateSectionByMesh(mesh)


        Dim nonstructureUnit As Unit = CType(workFemPart.UnitCollection.FindObject("KilogramPerMilliMeter"), Unit)
        beamPropPropTab.SetScalarWithDataPropertyValue("beam nonstructural mass, end a", "3", nonstructureUnit)  'the replacement of UF_SF_apply_beam_end_mass

        Dim queriedMassValue As Double
        Dim queriedMassUnit As Unit
        beamPropPropTab.GetScalarWithDataPropertyValue("beam nonstructural mass, end a", queriedMassValue, queriedMassUnit)  'the replacement of UF_SF_ask_beam_end_mass

    End Sub

    '-----------------------------------------------------------------------------------
    'This function performs various operations on beam mesh associated data.
    '
    'Remark:
    '   
    '-----------------------------------------------------------------------------------
    Sub MeshAssociatedDataOperation(ByRef mesh As Mesh)

        Dim meshElementPropTab As PropertyTable = mesh.ElementPropertyTable

        Dim femPart As CAE.FemPart = CType(workFemPart, CAE.FemPart)

        EditBeamOrientation(meshElementPropTab, femPart)

        ApplyOffset(meshElementPropTab, femPart)
        AskSectionOffset(meshElementPropTab)

        AskSectionData(meshElementPropTab)


    End Sub

    '-----------------------------------------------------------------------------------
    'This function is to edit beam orientation. Due to the rework done in NX7.5, this function
    'is not the exact equivalent replacement of UFSf.EditBeamOrientation. Please refer to NX online 
    'help to understand the parameters needed for beam orientation
    'Remark:
    '   
    '-----------------------------------------------------------------------------------
    Sub EditBeamOrientation(ByRef meshAssociatedData As PropertyTable, ByVal femPart As FemPart)

        Dim beamSectionOrientationOptions As CAE.BeamSectionOrientationOptions
        beamSectionOrientationOptions = femPart.NewBeamSectionOrientationOptions()

        beamSectionOrientationOptions.MethodType = CAE.BeamSectionOrientationOptions.Method.ByVector

        beamSectionOrientationOptions.DirectionType = CAE.BeamSection.DirectionOption.Horizontal

        Dim point1Coord As Point3d = New Point3d(0, 0, 0.0)
        Dim point1 As Point = workFemPart.Points.CreatePoint(point1Coord)

        Dim point2Coord As Point3d = New Point3d(1, 1, 1)
        Dim point2 As Point = workFemPart.Points.CreatePoint(point2Coord)

        Dim direction As Direction
        direction = workFemPart.Directions.CreateDirection(point1, point2, SmartObject.UpdateOption.AfterModeling)
        beamSectionOrientationOptions.Vector = direction

        Dim fEElement As CAE.FEElement = CType(fEModel.Find("Element[8]"), CAE.FEElement)
        beamSectionOrientationOptions.OrientedElement = fEElement

        meshAssociatedData.SetSectionOrientationPropertyValue("section_orientation", beamSectionOrientationOptions)

        beamSectionOrientationOptions.Dispose()

    End Sub

    '-----------------------------------------------------------------------------------
    'This function is to apply beam offset. Due to the rework done in NX7.5, this function
    'is not the equivalent replacement of UFSf.ApplyOffset. Please refer to NX online help
    'to understand the parameters needed for beam offset 
    '-----------------------------------------------------------------------------------
    Sub ApplyOffset(ByRef meshAssociatedData As PropertyTable, ByVal femPart As FemPart)

        Dim beamSectionOffsetOptions As BeamSectionOffsetOptions
        beamSectionOffsetOptions = femPart.NewBeamSectionOffsetOptions()

        beamSectionOffsetOptions.IsOffsetSpecified = True

        beamSectionOffsetOptions.SameEndOffsets = True

        beamSectionOffsetOptions.OffsetMethodType = beamSectionOffsetOptions.Method.Neutral


        Dim unit As Unit = CType(workFemPart.UnitCollection.FindObject("MilliMeter"), Unit)
        Dim expression As Expression
        expression = workFemPart.Expressions.CreateSystemExpressionWithUnits("2.0", unit)

        Dim foreoffsets As CAE.BeamSectionOffsetOptions.Offset
        foreoffsets.YEccentric = 0.0
        foreoffsets.ZEccentric = 0.0
        foreoffsets.OffsetX = expression
        foreoffsets.OffsetY = expression
        foreoffsets.OffsetZ = expression
        beamSectionOffsetOptions.ForeOffset = foreoffsets


        meshAssociatedData.SetSectionOffsetPropertyValue("section_offset", beamSectionOffsetOptions)

        beamSectionOffsetOptions.Dispose()

    End Sub


    '-----------------------------------------------------------------------------------
    'This function is to query beam offset from given mesh. Due to the rework done in NX7.5
    'it is not an exact equivalent replacement of UFSf.AskSectionOffset
    '-----------------------------------------------------------------------------------
    Sub AskSectionOffset(ByRef meshAssociatedData As PropertyTable)

        Dim beamSectionOffsetOptions As BeamSectionOffsetOptions = meshAssociatedData.GetSectionOffsetPropertyValue("section_offset")

        Dim foreOffset As BeamSectionOffsetOptions.Offset = beamSectionOffsetOptions.ForeOffset

        Dim aftOffset As BeamSectionOffsetOptions.Offset = beamSectionOffsetOptions.AftOffset

    End Sub


    '-----------------------------------------------------------------------------------
    'This function is to query beam orientation data and beam offset data from beam mesh 
    'associated data. Due to the rework done in NX7.5, it is not the exact equivalent replacement of UFSf.AskSectionData.
    'Please refer to the NX Open documentation for further help
    '-----------------------------------------------------------------------------------
    Sub AskSectionData(ByVal meshAssociatedData As PropertyTable)

        Dim queriedBeamSectionOrientationOptions As CAE.BeamSectionOrientationOptions
        queriedBeamSectionOrientationOptions = meshAssociatedData.GetSectionOrientationPropertyValue("section_orientation")

        AskSectionOffset(meshAssociatedData)

    End Sub


    '-----------------------------------------------------------------------------------
    'This function is to prepare the test model - this is accomplished via recoding a journal, and is included here
    ' for completeness, so that any one can create a model to then know how the foregoing functions
    ' work on beam sections.
    '
    'Remark:
    '   
    '-----------------------------------------------------------------------------------
    Sub CreateFemPart()

        ' ----------------------------------------------
        '   Menu: File->New...
        ' ----------------------------------------------
        Dim markId1 As Session.UndoMarkId
        markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim fileNew1 As FileNew
        fileNew1 = theSession.Parts.FileNew()

        theSession.SetUndoMarkName(markId1, "##84New Dialog")

        Dim markId2 As Session.UndoMarkId
        markId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "##84New")

        fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"

        fileNew1.ApplicationName = "ModelTemplate"

        fileNew1.Units = Part.Units.Millimeters

        fileNew1.NewFileName = "test.prt"

        fileNew1.MasterFileName = ""

        fileNew1.UseBlankTemplate = False

        fileNew1.MakeDisplayedPart = True

        Dim nXObject1 As NXObject
        nXObject1 = fileNew1.Commit()

        Dim workPart As Part = theSession.Parts.Work

        Dim displayPart As Part = theSession.Parts.Display

        theSession.DeleteUndoMark(markId2, Nothing)

        fileNew1.Destroy()

        Dim markId3 As Session.UndoMarkId
        markId3 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Enter Modeling")

        ' ----------------------------------------------
        '   Menu: Insert->Sketch Curve->Rectangle...
        ' ----------------------------------------------
        Dim markId4 As Session.UndoMarkId
        markId4 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

        Dim markId5 As Session.UndoMarkId
        markId5 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Rectangle")

        Dim datumAxis1 As DatumAxis = CType(workPart.Datums.FindObject("DATUM_CSYS(0) Y axis"), DatumAxis)

        Dim direction1 As Direction
        direction1 = workPart.Directions.CreateDirection(datumAxis1, Sense.Forward, SmartObject.UpdateOption.WithinModeling)

        Dim datumPlane1 As DatumPlane = CType(workPart.Datums.FindObject("DATUM_CSYS(0) XZ plane"), DatumPlane)

        Dim datumCsys1 As Features.DatumCsys = CType(workPart.Features.FindObject("DATUM_CSYS(0)"), Features.DatumCsys)

        Dim point1 As Point = CType(datumCsys1.FindObject("POINT 1"), Point)

        Dim xform1 As Xform
        xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction1, point1, SmartObject.UpdateOption.WithinModeling, 0.625, False, False)

        Dim cartesianCoordinateSystem1 As CartesianCoordinateSystem
        cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, SmartObject.UpdateOption.WithinModeling)

        Dim nullFeatures_Feature As Features.Feature = Nothing

        Dim datumCsysBuilder1 As Features.DatumCsysBuilder
        datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(nullFeatures_Feature)

        datumCsysBuilder1.Csys = cartesianCoordinateSystem1

        datumCsysBuilder1.DisplayScaleFactor = 1.25

        Dim feature1 As Features.Feature
        feature1 = datumCsysBuilder1.CommitFeature()

        datumCsysBuilder1.Destroy()

        Dim nullSketch As Sketch = Nothing

        Dim sketchInPlaceBuilder1 As SketchInPlaceBuilder
        sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(nullSketch)

        Dim origin1 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal1 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane1 As Plane
        plane1 = workPart.Planes.CreatePlane(origin1, normal1, SmartObject.UpdateOption.WithinModeling)
        sketchInPlaceBuilder1.PlaneReference = plane1

        Dim datumPlane2 As DatumPlane = CType(workPart.Datums.FindObject("DATUM_CSYS(1) YZ plane"), DatumPlane)

        plane1.SetMethod(PlaneTypes.MethodType.Distance)

        Dim objects(0) As NXObject
        objects(0) = datumPlane2
        plane1.SetGeometry(objects)
        plane1.SetFlip(False)
        plane1.SetReverseSide(False)

        Dim planeExpression1 As Expression = plane1.Expression
        planeExpression1.RightHandSide = "0"

        plane1.SetAlternate(PlaneTypes.AlternateType.One)
        plane1.Evaluate()

        Dim datumAxis2 As DatumAxis = CType(workPart.Datums.FindObject("DATUM_CSYS(1) X axis"), DatumAxis)

        Dim direction2 As Direction
        direction2 = workPart.Directions.CreateDirection(datumAxis2, Sense.Forward, SmartObject.UpdateOption.WithinModeling)
        sketchInPlaceBuilder1.AxisReference = direction2

        Dim datumCsys2 As Features.DatumCsys = CType(feature1, Features.DatumCsys)

        Dim point2 As Point = CType(datumCsys2.FindObject("POINT 1"), Point)

        sketchInPlaceBuilder1.SketchOrigin = point2

        sketchInPlaceBuilder1.PlaneOption = Sketch.PlaneOption.ExistingPlane

        sketchInPlaceBuilder1.OriginOption = NXOpen.OriginMethod.SpecifyPoint

        theSession.Preferences.Sketch.CreateInferredConstraints = True

        theSession.Preferences.Sketch.ContinuousAutoDimensioning = True

        theSession.Preferences.Sketch.DimensionLabel = Preferences.SketchPreferences.DimensionLabelType.Expression

        theSession.Preferences.Sketch.TextSizeFixed = True

        theSession.Preferences.Sketch.FixedTextSize = 4.0

        theSession.Preferences.Sketch.DisplayObjectColor = False

        Dim nXObject2 As NXObject
        nXObject2 = sketchInPlaceBuilder1.Commit()

        sketchInPlaceBuilder1.Destroy()

        Dim sketch1 As Sketch = CType(nXObject2, Sketch)

        sketch1.Activate(Sketch.ViewReorient.False)

        theSession.SetUndoMarkVisibility(markId5, "Create Rectangle", Session.MarkVisibility.Visible)

        ' ----------------------------------------------
        ' Creating rectangle using By 2 Points method 
        ' ----------------------------------------------
        Dim startPoint1 As Point3d = New Point3d(0.0, 165.0, 48.0)
        Dim endPoint1 As Point3d = New Point3d(0.0, 190.0, 48.0)
        Dim line1 As Line
        line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)

        Dim startPoint2 As Point3d = New Point3d(0.0, 190.0, 48.0)
        Dim endPoint2 As Point3d = New Point3d(0.0, 190.0, 27.0)
        Dim line2 As Line
        line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)

        Dim startPoint3 As Point3d = New Point3d(0.0, 190.0, 27.0)
        Dim endPoint3 As Point3d = New Point3d(0.0, 165.0, 27.0)
        Dim line3 As Line
        line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)

        Dim startPoint4 As Point3d = New Point3d(0.0, 165.0, 27.0)
        Dim endPoint4 As Point3d = New Point3d(0.0, 165.0, 48.0)
        Dim line4 As Line
        line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)

        theSession.ActiveSketch.AddGeometry(line1)

        theSession.ActiveSketch.AddGeometry(line2)

        theSession.ActiveSketch.AddGeometry(line3)

        theSession.ActiveSketch.AddGeometry(line4)

        Dim geom1 As Sketch.ConstraintGeometry
        geom1.Geometry = line1
        geom1.PointType = Sketch.ConstraintPointType.None
        geom1.SplineDefiningPointIndex = 0
        Dim sketchGeometricConstraint1 As SketchGeometricConstraint
        sketchGeometricConstraint1 = theSession.ActiveSketch.CreateHorizontalConstraint(geom1)

        Dim conGeom1_1 As Sketch.ConstraintGeometry
        conGeom1_1.Geometry = line1
        conGeom1_1.PointType = Sketch.ConstraintPointType.None
        conGeom1_1.SplineDefiningPointIndex = 0
        Dim conGeom2_1 As Sketch.ConstraintGeometry
        conGeom2_1.Geometry = line2
        conGeom2_1.PointType = Sketch.ConstraintPointType.None
        conGeom2_1.SplineDefiningPointIndex = 0
        Dim sketchGeometricConstraint2 As SketchGeometricConstraint
        sketchGeometricConstraint2 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)

        Dim conGeom1_2 As Sketch.ConstraintGeometry
        conGeom1_2.Geometry = line2
        conGeom1_2.PointType = Sketch.ConstraintPointType.None
        conGeom1_2.SplineDefiningPointIndex = 0
        Dim conGeom2_2 As Sketch.ConstraintGeometry
        conGeom2_2.Geometry = line3
        conGeom2_2.PointType = Sketch.ConstraintPointType.None
        conGeom2_2.SplineDefiningPointIndex = 0
        Dim sketchGeometricConstraint3 As SketchGeometricConstraint
        sketchGeometricConstraint3 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)

        Dim conGeom1_3 As Sketch.ConstraintGeometry
        conGeom1_3.Geometry = line3
        conGeom1_3.PointType = Sketch.ConstraintPointType.None
        conGeom1_3.SplineDefiningPointIndex = 0
        Dim conGeom2_3 As Sketch.ConstraintGeometry
        conGeom2_3.Geometry = line4
        conGeom2_3.PointType = Sketch.ConstraintPointType.None
        conGeom2_3.SplineDefiningPointIndex = 0
        Dim sketchGeometricConstraint4 As SketchGeometricConstraint
        sketchGeometricConstraint4 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)

        Dim conGeom1_4 As Sketch.ConstraintGeometry
        conGeom1_4.Geometry = line4
        conGeom1_4.PointType = Sketch.ConstraintPointType.None
        conGeom1_4.SplineDefiningPointIndex = 0
        Dim conGeom2_4 As Sketch.ConstraintGeometry
        conGeom2_4.Geometry = line1
        conGeom2_4.PointType = Sketch.ConstraintPointType.None
        conGeom2_4.SplineDefiningPointIndex = 0
        Dim sketchGeometricConstraint5 As SketchGeometricConstraint
        sketchGeometricConstraint5 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)

        Dim dimObject1_1 As Sketch.DimensionGeometry
        dimObject1_1.Geometry = line1
        dimObject1_1.AssocType = Sketch.AssocType.StartPoint
        dimObject1_1.AssocValue = 0
        dimObject1_1.HelpPoint.X = 0.0
        dimObject1_1.HelpPoint.Y = 0.0
        dimObject1_1.HelpPoint.Z = 0.0
        Dim nullNXObject As NXObject = Nothing

        dimObject1_1.View = nullNXObject
        Dim dimObject2_1 As Sketch.DimensionGeometry
        dimObject2_1.Geometry = line1
        dimObject2_1.AssocType = Sketch.AssocType.EndPoint
        dimObject2_1.AssocValue = 0
        dimObject2_1.HelpPoint.X = 0.0
        dimObject2_1.HelpPoint.Y = 0.0
        dimObject2_1.HelpPoint.Z = 0.0
        dimObject2_1.View = nullNXObject
        Dim dimOrigin1 As Point3d = New Point3d(0.0, 177.5, 35.3810022185667)
        Dim nullExpression As Expression = Nothing

        Dim sketchDimensionalConstraint1 As SketchDimensionalConstraint
        sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, nullExpression, Sketch.DimensionOption.CreateAsAutomatic)

        Dim sketchHelpedDimensionalConstraint1 As SketchHelpedDimensionalConstraint = CType(sketchDimensionalConstraint1, SketchHelpedDimensionalConstraint)

        Dim dimension1 As Annotations.Dimension
        dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension

        Dim expression1 As Expression
        expression1 = sketchHelpedDimensionalConstraint1.AssociatedExpression

        Dim dimObject1_2 As Sketch.DimensionGeometry
        dimObject1_2.Geometry = line2
        dimObject1_2.AssocType = Sketch.AssocType.StartPoint
        dimObject1_2.AssocValue = 0
        dimObject1_2.HelpPoint.X = 0.0
        dimObject1_2.HelpPoint.Y = 0.0
        dimObject1_2.HelpPoint.Z = 0.0
        dimObject1_2.View = nullNXObject
        Dim dimObject2_2 As Sketch.DimensionGeometry
        dimObject2_2.Geometry = line2
        dimObject2_2.AssocType = Sketch.AssocType.EndPoint
        dimObject2_2.AssocValue = 0
        dimObject2_2.HelpPoint.X = 0.0
        dimObject2_2.HelpPoint.Y = 0.0
        dimObject2_2.HelpPoint.Z = 0.0
        dimObject2_2.View = nullNXObject
        Dim dimOrigin2 As Point3d = New Point3d(0.0, 177.381002218567, 37.5)
        Dim sketchDimensionalConstraint2 As SketchDimensionalConstraint
        sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, nullExpression, Sketch.DimensionOption.CreateAsAutomatic)

        Dim sketchHelpedDimensionalConstraint2 As SketchHelpedDimensionalConstraint = CType(sketchDimensionalConstraint2, SketchHelpedDimensionalConstraint)

        Dim dimension2 As Annotations.Dimension
        dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension

        Dim expression2 As Expression
        expression2 = sketchHelpedDimensionalConstraint2.AssociatedExpression

        theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False

        theSession.ActiveSketch.Update()

        theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True

        Dim geoms1(3) As SmartObject
        geoms1(0) = line1
        geoms1(1) = line2
        geoms1(2) = line3
        geoms1(3) = line4
        theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)

        Dim geoms2(3) As SmartObject
        geoms2(0) = line1
        geoms2(1) = line2
        geoms2(2) = line3
        geoms2(3) = line4
        theSession.ActiveSketch.UpdateDimensionDisplay(geoms2)

        ' ----------------------------------------------
        '   Menu: File->Finish Sketch
        ' ----------------------------------------------
        theSession.ActiveSketch.Deactivate(Sketch.ViewReorient.False, Sketch.UpdateLevel.Model)

        ' ----------------------------------------------
        '   Menu: Insert->Design Feature->Cone...
        ' ----------------------------------------------
        Dim markId6 As Session.UndoMarkId
        markId6 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim nullFeatures_Cone As Features.Cone = Nothing

        Dim coneBuilder1 As Features.ConeBuilder
        coneBuilder1 = workPart.Features.CreateConeBuilder(nullFeatures_Cone)

        coneBuilder1.BaseDiameter.RightHandSide = "50"

        coneBuilder1.TopDiameter.RightHandSide = "0"

        coneBuilder1.Height.RightHandSide = "25"

        coneBuilder1.HalfAngle.RightHandSide = "45"

        coneBuilder1.BooleanOption.Type = GeometricUtilities.BooleanOperation.BooleanType.Create

        Dim targetBodies1(0) As Body
        Dim nullBody As Body = Nothing

        targetBodies1(0) = nullBody
        coneBuilder1.BooleanOption.SetTargetBodies(targetBodies1)

        theSession.SetUndoMarkName(markId6, "Cone Dialog")

        Dim unit1 As Unit
        unit1 = coneBuilder1.TopDiameter.Units

        Dim expression3 As Expression
        expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("p4_x=77.2588308102052", unit1)

        Dim scalar1 As Scalar
        scalar1 = workPart.Scalars.CreateScalarExpression(expression3, Scalar.DimensionalityType.None, SmartObject.UpdateOption.WithinModeling)

        Dim expression4 As Expression
        expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("p5_y=99.6275241200693", unit1)

        Dim scalar2 As Scalar
        scalar2 = workPart.Scalars.CreateScalarExpression(expression4, Scalar.DimensionalityType.None, SmartObject.UpdateOption.WithinModeling)

        Dim expression5 As Expression
        expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("p6_z=0", unit1)

        Dim scalar3 As Scalar
        scalar3 = workPart.Scalars.CreateScalarExpression(expression5, Scalar.DimensionalityType.None, SmartObject.UpdateOption.WithinModeling)

        Dim point3 As Point
        point3 = workPart.Points.CreatePoint(scalar1, scalar2, scalar3, SmartObject.UpdateOption.WithinModeling)

        Dim axis1 As Axis
        axis1 = coneBuilder1.Axis

        axis1.Point = point3

        Dim markId7 As Session.UndoMarkId
        markId7 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Cone")

        Dim nXObject3 As NXObject
        nXObject3 = coneBuilder1.Commit()

        theSession.DeleteUndoMark(markId7, Nothing)

        theSession.SetUndoMarkName(markId6, "Cone")

        Dim expression6 As Expression = coneBuilder1.TopDiameter

        Dim expression7 As Expression = coneBuilder1.Height

        Dim expression8 As Expression = coneBuilder1.HalfAngle

        Dim expression9 As Expression = coneBuilder1.BaseDiameter

        coneBuilder1.Destroy()

        ' ----------------------------------------------
        '   Menu: File->New...
        ' ----------------------------------------------
        Dim markId8 As Session.UndoMarkId
        markId8 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim fileNew2 As FileNew
        fileNew2 = theSession.Parts.FileNew()

        theSession.SetUndoMarkName(markId8, "##84New Dialog")

        Dim markId9 As Session.UndoMarkId
        markId9 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "##84New")

        fileNew2.TemplateFileName = "FemNxNastranMetric.fem"

        fileNew2.ApplicationName = "CaeFemTemplate"

        fileNew2.Units = Part.Units.Millimeters

        fileNew2.NewFileName = "fem.fem"

        fileNew2.MasterFileName = ""

        fileNew2.UseBlankTemplate = False

        fileNew2.MakeDisplayedPart = True

        Dim nXObject4 As NXObject
        nXObject4 = fileNew2.Commit()

        workPart = Nothing
        Dim workFemPart As CAE.FemPart = CType(theSession.Parts.BaseWork, CAE.FemPart)

        displayPart = Nothing
        Dim displayFemPart As CAE.FemPart = CType(theSession.Parts.BaseDisplay, CAE.FemPart)

        theSession.DeleteUndoMark(markId9, Nothing)

        fileNew2.Destroy()

        Dim markId10 As Session.UndoMarkId
        markId10 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        theSession.SetUndoMarkName(markId10, "New FEM Dialog")

        ' ----------------------------------------------
        '   Dialog Begin New FEM
        ' ----------------------------------------------
        Dim markId11 As Session.UndoMarkId
        markId11 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Start")

        theSession.SetUndoMarkName(markId11, "Geometry Options Dialog")

        ' ----------------------------------------------
        '   Dialog Begin Geometry Options
        ' ----------------------------------------------
        Dim markId12 As Session.UndoMarkId
        markId12 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Geometry Options")

        theSession.DeleteUndoMark(markId12, Nothing)

        theSession.SetUndoMarkName(markId11, "Geometry Options")

        theSession.DeleteUndoMark(markId11, Nothing)

        Dim markId13 As Session.UndoMarkId
        markId13 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "New FEM")

        Dim femPart1 As CAE.FemPart = CType(workFemPart, CAE.FemPart)

        Dim femCreationOptions1 As CAE.FemCreationOptions
        femCreationOptions1 = femPart1.NewFemCreationOptions()

        Dim femSynchronizeOptions1 As CAE.FemSynchronizeOptions
        femSynchronizeOptions1 = femPart1.NewFemSynchronizeOptions()

        femSynchronizeOptions1.SynchronizePointsFlag = True
        femSynchronizeOptions1.SynchronizeCoordinateSystemFlag = True
        femSynchronizeOptions1.SynchronizeLinesFlag = True
        femSynchronizeOptions1.SynchronizeArcsFlag = True
        femSynchronizeOptions1.SynchronizeSplinesFlag = True
        femSynchronizeOptions1.SynchronizeConicsFlag = True
        femSynchronizeOptions1.SynchronizeSketchCurvesFlag = True

        Dim femPart2 As CAE.FemPart = CType(workFemPart, CAE.FemPart)

        Dim part1 As Part = CType(nXObject1, Part)

        Dim bodies1(0) As Body
        Dim body1 As Body = CType(part1.Bodies.FindObject("CONE(3)"), Body)

        bodies1(0) = body1
        Dim description1(-1) As String

        femCreationOptions1.SetCadData(part1, "fem_i.prt")
        femCreationOptions1.SetGeometryOptions(CAE.FemPart.UseBodiesOption.VisibleBodies, bodies1, femSynchronizeOptions1)
        femCreationOptions1.SetSolverOptions("NX NASTRAN", "Structural", NXOpen.CAE.BaseFemPart.AxisymAbstractionType.None)
        femCreationOptions1.SetDescription(description1)
        femPart2.FinalizeCreation(femCreationOptions1)

        femSynchronizeOptions1.Dispose()
        femCreationOptions1.Dispose()

        theSession.DeleteUndoMark(markId13, Nothing)

        Dim markId14 As Session.UndoMarkId
        markId14 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Enter Advanced Simulation")

        ' ----------------------------------------------
        '   Menu: Insert->Curve->Lines and Arcs->Line Point-Point...
        ' ----------------------------------------------
        Dim markId15 As Session.UndoMarkId
        markId15 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim nullFeatures_AssociativeLine As Features.AssociativeLine = Nothing

        Dim associativeLineBuilder1 As Features.AssociativeLineBuilder
        associativeLineBuilder1 = workFemPart.BaseFeatures.CreateAssociativeLineBuilder(nullFeatures_AssociativeLine)

        Dim origin2 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal2 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane2 As Plane
        plane2 = workFemPart.Planes.CreatePlane(origin2, normal2, SmartObject.UpdateOption.WithinModeling)

        Dim section1 As Section
        section1 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim unit2 As Unit
        unit2 = associativeLineBuilder1.Limits.StartLimit.Distance.Units

        Dim expression10 As Expression
        expression10 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim section2 As Section
        section2 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression11 As Expression
        expression11 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        associativeLineBuilder1.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder1.Limits.StartLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder1.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder1.Limits.EndLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder1.Limits.EndLimit.Distance.RightHandSide = "0"

        associativeLineBuilder1.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder1.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder1.Limits.FullCircle = False

        theSession.SetUndoMarkName(markId15, "Line Point-Point Dialog")

        Dim scaleAboutPoint1 As Point3d = New Point3d(116.300714622425, 14.4680314841295, 0.0)
        Dim viewCenter1 As Point3d = New Point3d(-116.300714622425, -14.4680314841295, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)

        Dim scaleAboutPoint2 As Point3d = New Point3d(93.0405716979402, 11.5744251873036, 0.0)
        Dim viewCenter2 As Point3d = New Point3d(-93.0405716979401, -11.5744251873036, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)

        Dim scaleAboutPoint3 As Point3d = New Point3d(74.4324573583522, 9.25954014984285, 0.0)
        Dim viewCenter3 As Point3d = New Point3d(-74.4324573583521, -9.25954014984285, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.8, scaleAboutPoint3, viewCenter3)

        Dim scaleAboutPoint4 As Point3d = New Point3d(93.0405716979402, 11.5744251873036, 0.0)
        Dim viewCenter4 As Point3d = New Point3d(-93.0405716979401, -11.5744251873036, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.8, scaleAboutPoint4, viewCenter4)

        Dim scaleAboutPoint5 As Point3d = New Point3d(116.300714622425, 14.4680314841295, 0.0)
        Dim viewCenter5 As Point3d = New Point3d(-116.300714622425, -14.4680314841295, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.8, scaleAboutPoint5, viewCenter5)

        Dim scaleAboutPoint6 As Point3d = New Point3d(145.375893278032, 18.0850393551618, 0.0)
        Dim viewCenter6 As Point3d = New Point3d(-145.375893278031, -18.0850393551618, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.8, scaleAboutPoint6, viewCenter6)

        Dim scaleAboutPoint7 As Point3d = New Point3d(183.024076166421, 21.736826148031, 0.0)
        Dim viewCenter7 As Point3d = New Point3d(-183.024076166421, -21.736826148031, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.8, scaleAboutPoint7, viewCenter7)

        Dim scaleAboutPoint8 As Point3d = New Point3d(228.780095208027, 27.1710326850388, 0.0)
        Dim viewCenter8 As Point3d = New Point3d(-228.780095208026, -27.1710326850388, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.8, scaleAboutPoint8, viewCenter8)

        Dim scaleAboutPoint9 As Point3d = New Point3d(285.975119010033, 33.9637908562985, 0.0)
        Dim viewCenter9 As Point3d = New Point3d(-285.975119010033, -33.9637908562985, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.8, scaleAboutPoint9, viewCenter9)

        Dim scaleAboutPoint10 As Point3d = New Point3d(357.468898762541, 42.4547385703731, 0.0)
        Dim viewCenter10 As Point3d = New Point3d(-357.468898762541, -42.4547385703731, 0.0)
        workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.8, scaleAboutPoint10, viewCenter10)

        Dim expression12 As Expression
        expression12 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-960", unit2)

        Dim scalar4 As Scalar
        scalar4 = workFemPart.Scalars.CreateScalarExpression(expression12, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression13 As Expression
        expression13 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-235", unit2)

        Dim scalar5 As Scalar
        scalar5 = workFemPart.Scalars.CreateScalarExpression(expression13, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression14 As Expression
        expression14 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim scalar6 As Scalar
        scalar6 = workFemPart.Scalars.CreateScalarExpression(expression14, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim origin3 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim xDirection1 As Vector3d = New Vector3d(1.0, 0.0, 0.0)
        Dim yDirection1 As Vector3d = New Vector3d(0.0, 1.0, 0.0)
        Dim xform2 As Xform
        xform2 = workFemPart.Xforms.CreateXform(origin3, xDirection1, yDirection1, SmartObject.UpdateOption.AfterModeling, 1.0)

        Dim cartesianCoordinateSystem2 As CartesianCoordinateSystem
        cartesianCoordinateSystem2 = workFemPart.CoordinateSystems.CreateCoordinateSystem(xform2, SmartObject.UpdateOption.AfterModeling)

        Dim point4 As Point
        point4 = workFemPart.Points.CreatePoint(cartesianCoordinateSystem2, scalar4, scalar5, scalar6, SmartObject.UpdateOption.AfterModeling)

        associativeLineBuilder1.StartPoint.Value = point4

        Dim expression15 As Expression
        expression15 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-470", unit2)

        Dim scalar7 As Scalar
        scalar7 = workFemPart.Scalars.CreateScalarExpression(expression15, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression16 As Expression
        expression16 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-815", unit2)

        Dim scalar8 As Scalar
        scalar8 = workFemPart.Scalars.CreateScalarExpression(expression16, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression17 As Expression
        expression17 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim scalar9 As Scalar
        scalar9 = workFemPart.Scalars.CreateScalarExpression(expression17, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim origin4 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim xDirection2 As Vector3d = New Vector3d(1.0, 0.0, 0.0)
        Dim yDirection2 As Vector3d = New Vector3d(0.0, 1.0, 0.0)
        Dim xform3 As Xform
        xform3 = workFemPart.Xforms.CreateXform(origin4, xDirection2, yDirection2, SmartObject.UpdateOption.AfterModeling, 1.0)

        Dim cartesianCoordinateSystem3 As CartesianCoordinateSystem
        cartesianCoordinateSystem3 = workFemPart.CoordinateSystems.CreateCoordinateSystem(xform3, SmartObject.UpdateOption.AfterModeling)

        Dim point5 As Point
        point5 = workFemPart.Points.CreatePoint(cartesianCoordinateSystem3, scalar7, scalar8, scalar9, SmartObject.UpdateOption.AfterModeling)

        associativeLineBuilder1.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder1.Limits.EndLimit.Distance.RightHandSide = "759.275970909129"

        associativeLineBuilder1.Limits.EndLimit.Distance.RightHandSide = "759.275970909129"

        associativeLineBuilder1.EndPoint.Value = point5

        Dim markId16 As Session.UndoMarkId
        markId16 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Line Point-Point")

        associativeLineBuilder1.Associative = True

        Dim nXObject5 As NXObject
        nXObject5 = associativeLineBuilder1.Commit()

        theSession.DeleteUndoMark(markId16, Nothing)

        Dim markId17 As Session.UndoMarkId
        markId17 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Line Point-Point")

        theSession.SetUndoMarkName(markId15, "Line Point-Point")

        theSession.SetUndoMarkVisibility(markId15, Nothing, Session.MarkVisibility.Visible)

        associativeLineBuilder1.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression11)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        section2.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression10)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Dim objects1(0) As NXObject
        objects1(0) = plane2
        Dim nErrs1 As Integer
        nErrs1 = theSession.UpdateManager.AddToDeleteList(objects1)

        section1.Destroy()

        theSession.DeleteUndoMark(markId17, Nothing)

        Dim markId18 As Session.UndoMarkId
        markId18 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Start")

        Dim associativeLineBuilder2 As Features.AssociativeLineBuilder
        associativeLineBuilder2 = workFemPart.BaseFeatures.CreateAssociativeLineBuilder(nullFeatures_AssociativeLine)

        Dim origin5 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal3 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane3 As Plane
        plane3 = workFemPart.Planes.CreatePlane(origin5, normal3, SmartObject.UpdateOption.WithinModeling)

        Dim section3 As Section
        section3 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression18 As Expression
        expression18 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim section4 As Section
        section4 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression19 As Expression
        expression19 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        associativeLineBuilder2.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder2.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder2.StartAngle.RightHandSide = "0"

        associativeLineBuilder2.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder2.EndAngle.RightHandSide = "0"

        associativeLineBuilder2.Limits.StartLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder2.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder2.Limits.EndLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder2.Limits.EndLimit.Distance.RightHandSide = "759.275970909129"

        associativeLineBuilder2.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Inferred

        associativeLineBuilder2.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Inferred

        associativeLineBuilder2.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder2.Limits.EndLimit.Distance.RightHandSide = "0"

        associativeLineBuilder2.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder2.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder2.Limits.FullCircle = False

        theSession.SetUndoMarkName(markId18, "Line Point-Point Dialog")

        ' ----------------------------------------------
        '   Dialog Begin Line Point-Point
        ' ----------------------------------------------
        associativeLineBuilder2.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression19)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        section4.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression18)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Dim objects2(0) As NXObject
        objects2(0) = plane3
        Dim nErrs2 As Integer
        nErrs2 = theSession.UpdateManager.AddToDeleteList(objects2)

        section3.Destroy()

        theSession.UndoToMark(markId18, Nothing)

        theSession.DeleteUndoMark(markId18, Nothing)

        ' ----------------------------------------------
        '   Menu: Insert->Curve->Lines and Arcs->Line Point-Point...
        ' ----------------------------------------------
        Dim markId19 As Session.UndoMarkId
        markId19 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim associativeLineBuilder3 As Features.AssociativeLineBuilder
        associativeLineBuilder3 = workFemPart.BaseFeatures.CreateAssociativeLineBuilder(nullFeatures_AssociativeLine)

        Dim origin6 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal4 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane4 As Plane
        plane4 = workFemPart.Planes.CreatePlane(origin6, normal4, SmartObject.UpdateOption.WithinModeling)

        Dim section5 As Section
        section5 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression20 As Expression
        expression20 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim section6 As Section
        section6 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression21 As Expression
        expression21 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        associativeLineBuilder3.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder3.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder3.StartAngle.RightHandSide = "0"

        associativeLineBuilder3.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder3.EndAngle.RightHandSide = "0"

        associativeLineBuilder3.Limits.StartLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder3.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder3.Limits.EndLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder3.Limits.EndLimit.Distance.RightHandSide = "759.275970909129"

        associativeLineBuilder3.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Inferred

        associativeLineBuilder3.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Inferred

        associativeLineBuilder3.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder3.Limits.EndLimit.Distance.RightHandSide = "0"

        associativeLineBuilder3.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder3.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder3.Limits.FullCircle = False

        theSession.SetUndoMarkName(markId19, "Line Point-Point Dialog")

        Dim expression22 As Expression
        expression22 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-685", unit2)

        Dim scalar10 As Scalar
        scalar10 = workFemPart.Scalars.CreateScalarExpression(expression22, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression23 As Expression
        expression23 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-270", unit2)

        Dim scalar11 As Scalar
        scalar11 = workFemPart.Scalars.CreateScalarExpression(expression23, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression24 As Expression
        expression24 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim scalar12 As Scalar
        scalar12 = workFemPart.Scalars.CreateScalarExpression(expression24, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim origin7 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim xDirection3 As Vector3d = New Vector3d(1.0, 0.0, 0.0)
        Dim yDirection3 As Vector3d = New Vector3d(0.0, 1.0, 0.0)
        Dim xform4 As Xform
        xform4 = workFemPart.Xforms.CreateXform(origin7, xDirection3, yDirection3, SmartObject.UpdateOption.AfterModeling, 1.0)

        Dim cartesianCoordinateSystem4 As CartesianCoordinateSystem
        cartesianCoordinateSystem4 = workFemPart.CoordinateSystems.CreateCoordinateSystem(xform4, SmartObject.UpdateOption.AfterModeling)

        Dim point6 As Point
        point6 = workFemPart.Points.CreatePoint(cartesianCoordinateSystem4, scalar10, scalar11, scalar12, SmartObject.UpdateOption.AfterModeling)

        associativeLineBuilder3.StartPoint.Value = point6

        Dim expression25 As Expression
        expression25 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-315", unit2)

        Dim scalar13 As Scalar
        scalar13 = workFemPart.Scalars.CreateScalarExpression(expression25, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression26 As Expression
        expression26 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-705", unit2)

        Dim scalar14 As Scalar
        scalar14 = workFemPart.Scalars.CreateScalarExpression(expression26, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression27 As Expression
        expression27 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim scalar15 As Scalar
        scalar15 = workFemPart.Scalars.CreateScalarExpression(expression27, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim origin8 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim xDirection4 As Vector3d = New Vector3d(1.0, 0.0, 0.0)
        Dim yDirection4 As Vector3d = New Vector3d(0.0, 1.0, 0.0)
        Dim xform5 As Xform
        xform5 = workFemPart.Xforms.CreateXform(origin8, xDirection4, yDirection4, SmartObject.UpdateOption.AfterModeling, 1.0)

        Dim cartesianCoordinateSystem5 As CartesianCoordinateSystem
        cartesianCoordinateSystem5 = workFemPart.CoordinateSystems.CreateCoordinateSystem(xform5, SmartObject.UpdateOption.AfterModeling)

        Dim point7 As Point
        point7 = workFemPart.Points.CreatePoint(cartesianCoordinateSystem5, scalar13, scalar14, scalar15, SmartObject.UpdateOption.AfterModeling)

        associativeLineBuilder3.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder3.Limits.EndLimit.Distance.RightHandSide = "571.073550429365"

        associativeLineBuilder3.Limits.EndLimit.Distance.RightHandSide = "571.073550429365"

        associativeLineBuilder3.EndPoint.Value = point7

        Dim markId20 As Session.UndoMarkId
        markId20 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Line Point-Point")

        associativeLineBuilder3.Associative = True

        Dim nXObject6 As NXObject
        nXObject6 = associativeLineBuilder3.Commit()

        theSession.DeleteUndoMark(markId20, Nothing)

        Dim markId21 As Session.UndoMarkId
        markId21 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Line Point-Point")

        theSession.SetUndoMarkName(markId19, "Line Point-Point")

        theSession.SetUndoMarkVisibility(markId19, Nothing, Session.MarkVisibility.Visible)

        associativeLineBuilder3.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression21)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        section6.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression20)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Dim objects3(0) As NXObject
        objects3(0) = plane4
        Dim nErrs3 As Integer
        nErrs3 = theSession.UpdateManager.AddToDeleteList(objects3)

        section5.Destroy()

        theSession.DeleteUndoMark(markId21, Nothing)

        Dim markId22 As Session.UndoMarkId
        markId22 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Start")

        Dim associativeLineBuilder4 As Features.AssociativeLineBuilder
        associativeLineBuilder4 = workFemPart.BaseFeatures.CreateAssociativeLineBuilder(nullFeatures_AssociativeLine)

        Dim origin9 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal5 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane5 As Plane
        plane5 = workFemPart.Planes.CreatePlane(origin9, normal5, SmartObject.UpdateOption.WithinModeling)

        Dim section7 As Section
        section7 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression28 As Expression
        expression28 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim section8 As Section
        section8 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression29 As Expression
        expression29 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        associativeLineBuilder4.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder4.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder4.StartAngle.RightHandSide = "0"

        associativeLineBuilder4.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder4.EndAngle.RightHandSide = "0"

        associativeLineBuilder4.Limits.StartLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder4.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder4.Limits.EndLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder4.Limits.EndLimit.Distance.RightHandSide = "571.073550429365"

        associativeLineBuilder4.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Inferred

        associativeLineBuilder4.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Inferred

        associativeLineBuilder4.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder4.Limits.EndLimit.Distance.RightHandSide = "0"

        associativeLineBuilder4.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder4.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder4.Limits.FullCircle = False

        theSession.SetUndoMarkName(markId22, "Line Point-Point Dialog")

        ' ----------------------------------------------
        '   Dialog Begin Line Point-Point
        ' ----------------------------------------------
        associativeLineBuilder4.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression29)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        section8.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression28)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Dim objects4(0) As NXObject
        objects4(0) = plane5
        Dim nErrs4 As Integer
        nErrs4 = theSession.UpdateManager.AddToDeleteList(objects4)

        section7.Destroy()

        theSession.UndoToMark(markId22, Nothing)

        theSession.DeleteUndoMark(markId22, Nothing)

        ' ----------------------------------------------
        '   Menu: Insert->Curve->Lines and Arcs->Line Point-Point...
        ' ----------------------------------------------
        Dim markId23 As Session.UndoMarkId
        markId23 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim associativeLineBuilder5 As Features.AssociativeLineBuilder
        associativeLineBuilder5 = workFemPart.BaseFeatures.CreateAssociativeLineBuilder(nullFeatures_AssociativeLine)

        Dim origin10 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal6 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane6 As Plane
        plane6 = workFemPart.Planes.CreatePlane(origin10, normal6, SmartObject.UpdateOption.WithinModeling)

        Dim section9 As Section
        section9 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression30 As Expression
        expression30 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim section10 As Section
        section10 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression31 As Expression
        expression31 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        associativeLineBuilder5.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder5.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder5.StartAngle.RightHandSide = "0"

        associativeLineBuilder5.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder5.EndAngle.RightHandSide = "0"

        associativeLineBuilder5.Limits.StartLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder5.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder5.Limits.EndLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder5.Limits.EndLimit.Distance.RightHandSide = "571.073550429365"

        associativeLineBuilder5.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Inferred

        associativeLineBuilder5.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Inferred

        associativeLineBuilder5.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder5.Limits.EndLimit.Distance.RightHandSide = "0"

        associativeLineBuilder5.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder5.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder5.Limits.FullCircle = False

        theSession.SetUndoMarkName(markId23, "Line Point-Point Dialog")

        Dim expression32 As Expression
        expression32 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-560", unit2)

        Dim scalar16 As Scalar
        scalar16 = workFemPart.Scalars.CreateScalarExpression(expression32, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression33 As Expression
        expression33 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-115", unit2)

        Dim scalar17 As Scalar
        scalar17 = workFemPart.Scalars.CreateScalarExpression(expression33, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression34 As Expression
        expression34 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim scalar18 As Scalar
        scalar18 = workFemPart.Scalars.CreateScalarExpression(expression34, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim origin11 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim xDirection5 As Vector3d = New Vector3d(1.0, 0.0, 0.0)
        Dim yDirection5 As Vector3d = New Vector3d(0.0, 1.0, 0.0)
        Dim xform6 As Xform
        xform6 = workFemPart.Xforms.CreateXform(origin11, xDirection5, yDirection5, SmartObject.UpdateOption.AfterModeling, 1.0)

        Dim cartesianCoordinateSystem6 As CartesianCoordinateSystem
        cartesianCoordinateSystem6 = workFemPart.CoordinateSystems.CreateCoordinateSystem(xform6, SmartObject.UpdateOption.AfterModeling)

        Dim point8 As Point
        point8 = workFemPart.Points.CreatePoint(cartesianCoordinateSystem6, scalar16, scalar17, scalar18, SmartObject.UpdateOption.AfterModeling)

        associativeLineBuilder5.StartPoint.Value = point8

        Dim expression35 As Expression
        expression35 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-155", unit2)

        Dim scalar19 As Scalar
        scalar19 = workFemPart.Scalars.CreateScalarExpression(expression35, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression36 As Expression
        expression36 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-580", unit2)

        Dim scalar20 As Scalar
        scalar20 = workFemPart.Scalars.CreateScalarExpression(expression36, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression37 As Expression
        expression37 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim scalar21 As Scalar
        scalar21 = workFemPart.Scalars.CreateScalarExpression(expression37, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim origin12 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim xDirection6 As Vector3d = New Vector3d(1.0, 0.0, 0.0)
        Dim yDirection6 As Vector3d = New Vector3d(0.0, 1.0, 0.0)
        Dim xform7 As Xform
        xform7 = workFemPart.Xforms.CreateXform(origin12, xDirection6, yDirection6, SmartObject.UpdateOption.AfterModeling, 1.0)

        Dim cartesianCoordinateSystem7 As CartesianCoordinateSystem
        cartesianCoordinateSystem7 = workFemPart.CoordinateSystems.CreateCoordinateSystem(xform7, SmartObject.UpdateOption.AfterModeling)

        Dim point9 As Point
        point9 = workFemPart.Points.CreatePoint(cartesianCoordinateSystem7, scalar19, scalar20, scalar21, SmartObject.UpdateOption.AfterModeling)

        associativeLineBuilder5.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder5.Limits.EndLimit.Distance.RightHandSide = "616.644143732834"

        associativeLineBuilder5.Limits.EndLimit.Distance.RightHandSide = "616.644143732834"

        associativeLineBuilder5.EndPoint.Value = point9

        Dim markId24 As Session.UndoMarkId
        markId24 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Line Point-Point")

        associativeLineBuilder5.Associative = True

        Dim nXObject7 As NXObject
        nXObject7 = associativeLineBuilder5.Commit()

        theSession.DeleteUndoMark(markId24, Nothing)

        Dim markId25 As Session.UndoMarkId
        markId25 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Line Point-Point")

        theSession.SetUndoMarkName(markId23, "Line Point-Point")

        theSession.SetUndoMarkVisibility(markId23, Nothing, Session.MarkVisibility.Visible)

        associativeLineBuilder5.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression31)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        section10.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression30)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Dim objects5(0) As NXObject
        objects5(0) = plane6
        Dim nErrs5 As Integer
        nErrs5 = theSession.UpdateManager.AddToDeleteList(objects5)

        section9.Destroy()

        theSession.DeleteUndoMark(markId25, Nothing)

        Dim markId26 As Session.UndoMarkId
        markId26 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Start")

        Dim associativeLineBuilder6 As Features.AssociativeLineBuilder
        associativeLineBuilder6 = workFemPart.BaseFeatures.CreateAssociativeLineBuilder(nullFeatures_AssociativeLine)

        Dim origin13 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal7 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane7 As Plane
        plane7 = workFemPart.Planes.CreatePlane(origin13, normal7, SmartObject.UpdateOption.WithinModeling)

        Dim section11 As Section
        section11 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression38 As Expression
        expression38 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim section12 As Section
        section12 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression39 As Expression
        expression39 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        associativeLineBuilder6.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder6.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder6.StartAngle.RightHandSide = "0"

        associativeLineBuilder6.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder6.EndAngle.RightHandSide = "0"

        associativeLineBuilder6.Limits.StartLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder6.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder6.Limits.EndLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder6.Limits.EndLimit.Distance.RightHandSide = "616.644143732834"

        associativeLineBuilder6.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Inferred

        associativeLineBuilder6.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Inferred

        associativeLineBuilder6.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder6.Limits.EndLimit.Distance.RightHandSide = "0"

        associativeLineBuilder6.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder6.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder6.Limits.FullCircle = False

        theSession.SetUndoMarkName(markId26, "Line Point-Point Dialog")

        ' ----------------------------------------------
        '   Dialog Begin Line Point-Point
        ' ----------------------------------------------
        associativeLineBuilder6.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression39)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        section12.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression38)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Dim objects6(0) As NXObject
        objects6(0) = plane7
        Dim nErrs6 As Integer
        nErrs6 = theSession.UpdateManager.AddToDeleteList(objects6)

        section11.Destroy()

        theSession.UndoToMark(markId26, Nothing)

        theSession.DeleteUndoMark(markId26, Nothing)

        ' ----------------------------------------------
        '   Menu: Insert->Curve->Lines and Arcs->Line Point-Point...
        ' ----------------------------------------------
        Dim markId27 As Session.UndoMarkId
        markId27 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim associativeLineBuilder7 As Features.AssociativeLineBuilder
        associativeLineBuilder7 = workFemPart.BaseFeatures.CreateAssociativeLineBuilder(nullFeatures_AssociativeLine)

        Dim origin14 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal8 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane8 As Plane
        plane8 = workFemPart.Planes.CreatePlane(origin14, normal8, SmartObject.UpdateOption.WithinModeling)

        Dim section13 As Section
        section13 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression40 As Expression
        expression40 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim section14 As Section
        section14 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression41 As Expression
        expression41 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        associativeLineBuilder7.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder7.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder7.StartAngle.RightHandSide = "0"

        associativeLineBuilder7.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder7.EndAngle.RightHandSide = "0"

        associativeLineBuilder7.Limits.StartLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder7.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder7.Limits.EndLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder7.Limits.EndLimit.Distance.RightHandSide = "616.644143732834"

        associativeLineBuilder7.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Inferred

        associativeLineBuilder7.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Inferred

        associativeLineBuilder7.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder7.Limits.EndLimit.Distance.RightHandSide = "0"

        associativeLineBuilder7.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder7.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder7.Limits.FullCircle = False

        theSession.SetUndoMarkName(markId27, "Line Point-Point Dialog")

        Dim expression42 As Expression
        expression42 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-400", unit2)

        Dim scalar22 As Scalar
        scalar22 = workFemPart.Scalars.CreateScalarExpression(expression42, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression43 As Expression
        expression43 = workFemPart.Expressions.CreateSystemExpressionWithUnits("55", unit2)

        Dim scalar23 As Scalar
        scalar23 = workFemPart.Scalars.CreateScalarExpression(expression43, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression44 As Expression
        expression44 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim scalar24 As Scalar
        scalar24 = workFemPart.Scalars.CreateScalarExpression(expression44, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim origin15 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim xDirection7 As Vector3d = New Vector3d(1.0, 0.0, 0.0)
        Dim yDirection7 As Vector3d = New Vector3d(0.0, 1.0, 0.0)
        Dim xform8 As Xform
        xform8 = workFemPart.Xforms.CreateXform(origin15, xDirection7, yDirection7, SmartObject.UpdateOption.AfterModeling, 1.0)

        Dim cartesianCoordinateSystem8 As CartesianCoordinateSystem
        cartesianCoordinateSystem8 = workFemPart.CoordinateSystems.CreateCoordinateSystem(xform8, SmartObject.UpdateOption.AfterModeling)

        Dim point10 As Point
        point10 = workFemPart.Points.CreatePoint(cartesianCoordinateSystem8, scalar22, scalar23, scalar24, SmartObject.UpdateOption.AfterModeling)

        associativeLineBuilder7.StartPoint.Value = point10

        Dim expression45 As Expression
        expression45 = workFemPart.Expressions.CreateSystemExpressionWithUnits("30", unit2)

        Dim scalar25 As Scalar
        scalar25 = workFemPart.Scalars.CreateScalarExpression(expression45, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression46 As Expression
        expression46 = workFemPart.Expressions.CreateSystemExpressionWithUnits("-435", unit2)

        Dim scalar26 As Scalar
        scalar26 = workFemPart.Scalars.CreateScalarExpression(expression46, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim expression47 As Expression
        expression47 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim scalar27 As Scalar
        scalar27 = workFemPart.Scalars.CreateScalarExpression(expression47, Scalar.DimensionalityType.Length, SmartObject.UpdateOption.AfterModeling)

        Dim origin16 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim xDirection8 As Vector3d = New Vector3d(1.0, 0.0, 0.0)
        Dim yDirection8 As Vector3d = New Vector3d(0.0, 1.0, 0.0)
        Dim xform9 As Xform
        xform9 = workFemPart.Xforms.CreateXform(origin16, xDirection8, yDirection8, SmartObject.UpdateOption.AfterModeling, 1.0)

        Dim cartesianCoordinateSystem9 As CartesianCoordinateSystem
        cartesianCoordinateSystem9 = workFemPart.CoordinateSystems.CreateCoordinateSystem(xform9, SmartObject.UpdateOption.AfterModeling)

        Dim point11 As Point
        point11 = workFemPart.Points.CreatePoint(cartesianCoordinateSystem9, scalar25, scalar26, scalar27, SmartObject.UpdateOption.AfterModeling)

        associativeLineBuilder7.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder7.Limits.EndLimit.Distance.RightHandSide = "651.920240520265"

        associativeLineBuilder7.Limits.EndLimit.Distance.RightHandSide = "651.920240520265"

        associativeLineBuilder7.EndPoint.Value = point11

        Dim markId28 As Session.UndoMarkId
        markId28 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Line Point-Point")

        associativeLineBuilder7.Associative = True

        Dim nXObject8 As NXObject
        nXObject8 = associativeLineBuilder7.Commit()

        theSession.DeleteUndoMark(markId28, Nothing)

        Dim markId29 As Session.UndoMarkId
        markId29 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Line Point-Point")

        theSession.SetUndoMarkName(markId27, "Line Point-Point")

        theSession.SetUndoMarkVisibility(markId27, Nothing, Session.MarkVisibility.Visible)

        associativeLineBuilder7.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression41)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        section14.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression40)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Dim objects7(0) As NXObject
        objects7(0) = plane8
        Dim nErrs7 As Integer
        nErrs7 = theSession.UpdateManager.AddToDeleteList(objects7)

        section13.Destroy()

        theSession.DeleteUndoMark(markId29, Nothing)

        Dim markId30 As Session.UndoMarkId
        markId30 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Start")

        Dim associativeLineBuilder8 As Features.AssociativeLineBuilder
        associativeLineBuilder8 = workFemPart.BaseFeatures.CreateAssociativeLineBuilder(nullFeatures_AssociativeLine)

        Dim origin17 As Point3d = New Point3d(0.0, 0.0, 0.0)
        Dim normal9 As Vector3d = New Vector3d(0.0, 0.0, 1.0)
        Dim plane9 As Plane
        plane9 = workFemPart.Planes.CreatePlane(origin17, normal9, SmartObject.UpdateOption.WithinModeling)

        Dim section15 As Section
        section15 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression48 As Expression
        expression48 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        Dim section16 As Section
        section16 = workFemPart.Sections.CreateSection(0.02413, 0.0254, 0.5)

        Dim expression49 As Expression
        expression49 = workFemPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)

        associativeLineBuilder8.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder8.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder8.StartAngle.RightHandSide = "0"

        associativeLineBuilder8.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder8.EndAngle.RightHandSide = "0"

        associativeLineBuilder8.Limits.StartLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder8.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder8.Limits.EndLimit.LimitOption = GeometricUtilities.CurveExtendData.LimitOptions.AtPoint

        associativeLineBuilder8.Limits.EndLimit.Distance.RightHandSide = "651.920240520265"

        associativeLineBuilder8.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Inferred

        associativeLineBuilder8.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Inferred

        associativeLineBuilder8.Limits.StartLimit.Distance.RightHandSide = "0"

        associativeLineBuilder8.Limits.EndLimit.Distance.RightHandSide = "0"

        associativeLineBuilder8.StartPointOptions = Features.AssociativeLineBuilder.StartOption.Point

        associativeLineBuilder8.EndPointOptions = Features.AssociativeLineBuilder.EndOption.Point

        associativeLineBuilder8.Limits.FullCircle = False

        theSession.SetUndoMarkName(markId30, "Line Point-Point Dialog")

        ' ----------------------------------------------
        '   Dialog Begin Line Point-Point
        ' ----------------------------------------------
        associativeLineBuilder8.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression49)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        section16.Destroy()

        Try
            ' Expression is still in use.
            workFemPart.Expressions.Delete(expression48)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Dim objects8(0) As NXObject
        objects8(0) = plane9
        Dim nErrs8 As Integer
        nErrs8 = theSession.UpdateManager.AddToDeleteList(objects8)

        section15.Destroy()

        theSession.UndoToMark(markId30, Nothing)

        theSession.DeleteUndoMark(markId30, Nothing)

        ' ----------------------------------------------
        '   Menu: Insert->Mesh->1D Mesh...
        ' ----------------------------------------------
        Dim markId31 As Session.UndoMarkId
        markId31 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim fEModel1 As CAE.FEModel = CType(workFemPart.FindObject("FEModel"), CAE.FEModel)

        Dim meshManager1 As CAE.MeshManager = CType(fEModel1.Find("MeshManager"), CAE.MeshManager)

        Dim nullCAE_Mesh1d As CAE.Mesh1d = Nothing

        Dim mesh1dBuilder1 As CAE.Mesh1dBuilder
        mesh1dBuilder1 = meshManager1.CreateMesh1dBuilder(nullCAE_Mesh1d)

        Dim nullCAE_MeshCollector As CAE.MeshCollector = Nothing

        mesh1dBuilder1.ElementType.DestinationCollector.ElementContainer = nullCAE_MeshCollector

        mesh1dBuilder1.FlipDirectionOption = False

        theSession.SetUndoMarkName(markId31, "1D Mesh Dialog")

        mesh1dBuilder1.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim expression50 As Expression
        expression50 = mesh1dBuilder1.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression50.RightHandSide = "10"

        mesh1dBuilder1.PropertyTable.SetScalarPropertyValue("mesh density number", expression50)

        mesh1dBuilder1.PropertyTable.SetBooleanPropertyValue("merge nodes bool", True)

        Dim expression51 As Expression
        expression51 = mesh1dBuilder1.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression51, unit2, "0.00254")

        mesh1dBuilder1.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression51)

        mesh1dBuilder1.PropertyTable.SetBooleanPropertyValue("use mid nodes bool", False)

        mesh1dBuilder1.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim line5 As Line = CType(workFemPart.Lines.FindObject("ENTITY 3 4 1"), Line)

        Dim point12 As Point3d = New Point3d(-581.729652128536, -682.74857503153, 0.0000000000000150990331349021)
        Dim added1 As Boolean
        added1 = mesh1dBuilder1.SelectionList.Add(line5, workFemPart.ModelingViews.WorkView, point12)

        Dim markId32 As Session.UndoMarkId
        markId32 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "1D Mesh")

        mesh1dBuilder1.ElementType.ElementDimension = CAE.ElementTypeBuilder.ElementType.Beam

        mesh1dBuilder1.ElementType.ElementTypeName = "CBEAM"

        Dim destinationCollectorBuilder1 As CAE.DestinationCollectorBuilder
        destinationCollectorBuilder1 = mesh1dBuilder1.ElementType.DestinationCollector

        destinationCollectorBuilder1.ElementContainer = nullCAE_MeshCollector

        destinationCollectorBuilder1.AutomaticMode = True

        mesh1dBuilder1.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim expression52 As Expression
        expression52 = mesh1dBuilder1.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression52.RightHandSide = "10"

        mesh1dBuilder1.PropertyTable.SetScalarPropertyValue("mesh density number", expression52)

        mesh1dBuilder1.PropertyTable.SetBooleanPropertyValue("merge nodes bool", True)

        Dim expression53 As Expression
        expression53 = mesh1dBuilder1.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression53, unit2, "0.00254")

        mesh1dBuilder1.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression53)

        Dim expression54 As Expression
        expression54 = mesh1dBuilder1.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression54.RightHandSide = "10"

        mesh1dBuilder1.PropertyTable.SetScalarPropertyValue("mesh density number", expression54)

        Dim expression55 As Expression
        expression55 = mesh1dBuilder1.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression55, unit2, "0.00254")

        mesh1dBuilder1.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression55)

        Dim id1 As Session.UndoMarkId
        id1 = theSession.NewestVisibleUndoMark

        Dim nErrs9 As Integer
        nErrs9 = theSession.UpdateManager.DoUpdate(id1)

        Dim meshes1() As CAE.Mesh
        meshes1 = mesh1dBuilder1.CommitMesh()

        theSession.DeleteUndoMark(markId32, Nothing)

        theSession.SetUndoMarkName(id1, "1D Mesh")

        mesh1dBuilder1.Destroy()

        Dim markId33 As Session.UndoMarkId
        markId33 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim mesh1dBuilder2 As CAE.Mesh1dBuilder
        mesh1dBuilder2 = meshManager1.CreateMesh1dBuilder(nullCAE_Mesh1d)

        Dim meshCollector1 As CAE.MeshCollector = CType(meshManager1.FindObject("MeshCollector[Beam Collector(1)]"), CAE.MeshCollector)

        mesh1dBuilder2.ElementType.DestinationCollector.ElementContainer = meshCollector1

        mesh1dBuilder2.FlipDirectionOption = False

        theSession.SetUndoMarkName(markId33, "1D Mesh Dialog")

        mesh1dBuilder2.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim expression56 As Expression
        expression56 = mesh1dBuilder2.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression56.RightHandSide = "10"

        mesh1dBuilder2.PropertyTable.SetScalarPropertyValue("mesh density number", expression56)

        mesh1dBuilder2.PropertyTable.SetBooleanPropertyValue("merge nodes bool", True)

        Dim expression57 As Expression
        expression57 = mesh1dBuilder2.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression57, unit2, "0.00254")

        mesh1dBuilder2.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression57)

        mesh1dBuilder2.PropertyTable.SetBooleanPropertyValue("use mid nodes bool", False)

        ' ----------------------------------------------
        '   Dialog Begin 1D Mesh
        ' ----------------------------------------------
        mesh1dBuilder2.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim line6 As Line = CType(workFemPart.Lines.FindObject("ENTITY 3 3 1"), Line)

        Dim point13 As Point3d = New Point3d(-372.489840281599, -637.410593182445, -0.000000000000049737991503207)
        Dim added2 As Boolean
        added2 = mesh1dBuilder2.SelectionList.Add(line6, workFemPart.ModelingViews.WorkView, point13)

        Dim markId34 As Session.UndoMarkId
        markId34 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "1D Mesh")

        mesh1dBuilder2.ElementType.ElementDimension = CAE.ElementTypeBuilder.ElementType.Beam

        mesh1dBuilder2.ElementType.ElementTypeName = "CBEAM"

        Dim destinationCollectorBuilder2 As CAE.DestinationCollectorBuilder
        destinationCollectorBuilder2 = mesh1dBuilder2.ElementType.DestinationCollector

        destinationCollectorBuilder2.ElementContainer = nullCAE_MeshCollector

        destinationCollectorBuilder2.AutomaticMode = True

        mesh1dBuilder2.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim expression58 As Expression
        expression58 = mesh1dBuilder2.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression58.RightHandSide = "10"

        mesh1dBuilder2.PropertyTable.SetScalarPropertyValue("mesh density number", expression58)

        mesh1dBuilder2.PropertyTable.SetBooleanPropertyValue("merge nodes bool", True)

        Dim expression59 As Expression
        expression59 = mesh1dBuilder2.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression59, unit2, "0.00254")

        mesh1dBuilder2.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression59)

        Dim expression60 As Expression
        expression60 = mesh1dBuilder2.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression60.RightHandSide = "10"

        mesh1dBuilder2.PropertyTable.SetScalarPropertyValue("mesh density number", expression60)

        Dim expression61 As Expression
        expression61 = mesh1dBuilder2.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression61, unit2, "0.00254")

        mesh1dBuilder2.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression61)

        Dim id2 As Session.UndoMarkId
        id2 = theSession.NewestVisibleUndoMark

        Dim nErrs10 As Integer
        nErrs10 = theSession.UpdateManager.DoUpdate(id2)

        Dim meshes2() As CAE.Mesh
        meshes2 = mesh1dBuilder2.CommitMesh()

        theSession.DeleteUndoMark(markId34, Nothing)

        theSession.SetUndoMarkName(id2, "1D Mesh")

        mesh1dBuilder2.Destroy()

        Dim markId35 As Session.UndoMarkId
        markId35 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim mesh1dBuilder3 As CAE.Mesh1dBuilder
        mesh1dBuilder3 = meshManager1.CreateMesh1dBuilder(nullCAE_Mesh1d)

        mesh1dBuilder3.ElementType.DestinationCollector.ElementContainer = meshCollector1

        mesh1dBuilder3.FlipDirectionOption = False

        theSession.SetUndoMarkName(markId35, "1D Mesh Dialog")

        mesh1dBuilder3.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim expression62 As Expression
        expression62 = mesh1dBuilder3.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression62.RightHandSide = "10"

        mesh1dBuilder3.PropertyTable.SetScalarPropertyValue("mesh density number", expression62)

        mesh1dBuilder3.PropertyTable.SetBooleanPropertyValue("merge nodes bool", True)

        Dim expression63 As Expression
        expression63 = mesh1dBuilder3.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression63, unit2, "0.00254")

        mesh1dBuilder3.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression63)

        mesh1dBuilder3.PropertyTable.SetBooleanPropertyValue("use mid nodes bool", False)

        ' ----------------------------------------------
        '   Dialog Begin 1D Mesh
        ' ----------------------------------------------
        mesh1dBuilder3.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim line7 As Line = CType(workFemPart.Lines.FindObject("ENTITY 3 2 1"), Line)

        Dim point14 As Point3d = New Point3d(-208.569220612284, -518.494598556267, -0.000000000000014210854715202)
        Dim added3 As Boolean
        added3 = mesh1dBuilder3.SelectionList.Add(line7, workFemPart.ModelingViews.WorkView, point14)

        Dim markId36 As Session.UndoMarkId
        markId36 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "1D Mesh")

        mesh1dBuilder3.ElementType.ElementDimension = CAE.ElementTypeBuilder.ElementType.Beam

        mesh1dBuilder3.ElementType.ElementTypeName = "CBEAM"

        Dim destinationCollectorBuilder3 As CAE.DestinationCollectorBuilder
        destinationCollectorBuilder3 = mesh1dBuilder3.ElementType.DestinationCollector

        destinationCollectorBuilder3.ElementContainer = nullCAE_MeshCollector

        destinationCollectorBuilder3.AutomaticMode = True

        mesh1dBuilder3.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim expression64 As Expression
        expression64 = mesh1dBuilder3.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression64.RightHandSide = "10"

        mesh1dBuilder3.PropertyTable.SetScalarPropertyValue("mesh density number", expression64)

        mesh1dBuilder3.PropertyTable.SetBooleanPropertyValue("merge nodes bool", True)

        Dim expression65 As Expression
        expression65 = mesh1dBuilder3.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression65, unit2, "0.00254")

        mesh1dBuilder3.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression65)

        Dim expression66 As Expression
        expression66 = mesh1dBuilder3.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression66.RightHandSide = "10"

        mesh1dBuilder3.PropertyTable.SetScalarPropertyValue("mesh density number", expression66)

        Dim expression67 As Expression
        expression67 = mesh1dBuilder3.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression67, unit2, "0.00254")

        mesh1dBuilder3.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression67)

        Dim id3 As Session.UndoMarkId
        id3 = theSession.NewestVisibleUndoMark

        Dim nErrs11 As Integer
        nErrs11 = theSession.UpdateManager.DoUpdate(id3)

        Dim meshes3() As CAE.Mesh
        meshes3 = mesh1dBuilder3.CommitMesh()

        theSession.DeleteUndoMark(markId36, Nothing)

        theSession.SetUndoMarkName(id3, "1D Mesh")

        mesh1dBuilder3.Destroy()

        Dim markId37 As Session.UndoMarkId
        markId37 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim mesh1dBuilder4 As CAE.Mesh1dBuilder
        mesh1dBuilder4 = meshManager1.CreateMesh1dBuilder(nullCAE_Mesh1d)

        mesh1dBuilder4.ElementType.DestinationCollector.ElementContainer = meshCollector1

        mesh1dBuilder4.FlipDirectionOption = False

        theSession.SetUndoMarkName(markId37, "1D Mesh Dialog")

        mesh1dBuilder4.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim expression68 As Expression
        expression68 = mesh1dBuilder4.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression68.RightHandSide = "10"

        mesh1dBuilder4.PropertyTable.SetScalarPropertyValue("mesh density number", expression68)

        mesh1dBuilder4.PropertyTable.SetBooleanPropertyValue("merge nodes bool", True)

        Dim expression69 As Expression
        expression69 = mesh1dBuilder4.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression69, unit2, "0.00254")

        mesh1dBuilder4.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression69)

        mesh1dBuilder4.PropertyTable.SetBooleanPropertyValue("use mid nodes bool", False)

        ' ----------------------------------------------
        '   Dialog Begin 1D Mesh
        ' ----------------------------------------------
        mesh1dBuilder4.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim line8 As Line = CType(workFemPart.Lines.FindObject("ENTITY 3 1 1"), Line)

        Dim point15 As Point3d = New Point3d(-71.1920634384641, -319.688113756169, -0.000000000000035527136788005)
        Dim added4 As Boolean
        added4 = mesh1dBuilder4.SelectionList.Add(line8, workFemPart.ModelingViews.WorkView, point15)

        Dim markId38 As Session.UndoMarkId
        markId38 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "1D Mesh")

        mesh1dBuilder4.ElementType.ElementDimension = CAE.ElementTypeBuilder.ElementType.Beam

        mesh1dBuilder4.ElementType.ElementTypeName = "CBEAM"

        Dim destinationCollectorBuilder4 As CAE.DestinationCollectorBuilder
        destinationCollectorBuilder4 = mesh1dBuilder4.ElementType.DestinationCollector

        destinationCollectorBuilder4.ElementContainer = nullCAE_MeshCollector

        destinationCollectorBuilder4.AutomaticMode = True

        mesh1dBuilder4.PropertyTable.SetIntegerPropertyValue("mesh density option", 1)

        Dim expression70 As Expression
        expression70 = mesh1dBuilder4.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression70.RightHandSide = "10"

        mesh1dBuilder4.PropertyTable.SetScalarPropertyValue("mesh density number", expression70)

        mesh1dBuilder4.PropertyTable.SetBooleanPropertyValue("merge nodes bool", True)

        Dim expression71 As Expression
        expression71 = mesh1dBuilder4.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression71, unit2, "0.00254")

        mesh1dBuilder4.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression71)

        Dim expression72 As Expression
        expression72 = mesh1dBuilder4.PropertyTable.GetScalarPropertyValue("mesh density number")

        expression72.RightHandSide = "10"

        mesh1dBuilder4.PropertyTable.SetScalarPropertyValue("mesh density number", expression72)

        Dim expression73 As Expression
        expression73 = mesh1dBuilder4.PropertyTable.GetScalarPropertyValue("node coincidence tolerance")

        workFemPart.Expressions.EditWithUnits(expression73, unit2, "0.00254")

        mesh1dBuilder4.PropertyTable.SetScalarPropertyValue("node coincidence tolerance", expression73)

        Dim id4 As Session.UndoMarkId
        id4 = theSession.NewestVisibleUndoMark

        Dim nErrs12 As Integer
        nErrs12 = theSession.UpdateManager.DoUpdate(id4)

        Dim meshes4() As CAE.Mesh
        meshes4 = mesh1dBuilder4.CommitMesh()

        theSession.DeleteUndoMark(markId38, Nothing)

        theSession.SetUndoMarkName(id4, "1D Mesh")

        mesh1dBuilder4.Destroy()

        Dim meshCollectorBuilder1 As MeshCollectorBuilder
        meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(meshCollector1, "Beam Collector")


        Dim caePart1 As CAE.CaePart = CType(workFemPart, CAE.CaePart)

        Dim physicalPropertyTable1 As CAE.PhysicalPropertyTable
        physicalPropertyTable1 = caePart1.PhysicalPropertyTables.CreatePhysicalPropertyTable("PBEAML", "NX NASTRAN - Structural", "NX NASTRAN", "PBEAML1", 5)


        Dim propertyTable1 As CAE.PropertyTable
        propertyTable1 = physicalPropertyTable1.PropertyTable

        ' ----------------------------------------------
        '   Dialog Begin PBEAML

        meshCollectorBuilder1.PropertyTable.SetNamedPropertyTablePropertyValue("Beam Property", physicalPropertyTable1)

        Dim nXObject9 As NXObject
        nXObject9 = meshCollectorBuilder1.Commit()

        meshCollectorBuilder1.Destroy()


    End Sub

End Module

