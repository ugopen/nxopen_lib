' ShowElementPropertyTable.vb

Option Infer On
Imports System
Imports System.Collections.Generic

Imports NXOpen
Imports NXOpen.Selection
Imports NXOpen.UF
Imports NXOpen.UF.UFConstants

Module showConnectedElements

    Dim theSession As Session = Session.GetSession()
    Dim theUI As UI = UI.GetUI()
    Dim theNxMessageBox As NXMessageBox = theUI.NXMessageBox

    Dim theUfSession As UFSession = UFSession.GetUFSession()

    Dim applicationTitle As String = "Show Element Property Table"

    Sub Main()

        Dim caePart As CAE.CaePart = TryCast(theSession.Parts.BaseWork, CAE.CaePart)

        If caePart Is Nothing Then
            theNxMessageBox.Show(applicationTitle, NXMessageBox.DialogType.Error, "Simulation Part must be loaded")
            Return
        End If

        Dim markId1 As NXOpen.Session.UndoMarkId = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, applicationTitle)

        ' -------------------------------------------------------------------------
        ' Select faces 
        ' -------------------------------------------------------------------------
        Dim selObj As TaggedObject = Nothing
        Dim mask(0) As Selection.MaskTriple
        mask(0).Type = UF_pseudo_object_type
        mask(0).Subtype = UF_pseudo_CAE_subtype
        mask(0).SolidBodySubtype = UF_pseudo_CAE_element
        Dim cursor As Point3d

        Dim cue = "Select Element"
        Dim title = "Element Selection"
        Dim sel = theUI.SelectionManager
        Dim resp As Response = sel.SelectTaggedObject(cue, title, SelectionScope.AnyInAssembly, 
            SelectionAction.ClearAndEnableSpecific, False, False, mask, selObj, cursor)

        ' ---------------------------------------------------------------------------
        ' If selection proceeded ok, then create group and add all associated elements 
        ' ---------------------------------------------------------------------------       
        If resp = Response.ObjectSelected Then
            Dim elem = CType(selObj, CAE.FEElement)
            Dim mesh = elem.Mesh
            Guide.InfoWriteLine("Element Mesh: " & mesh.Name)

            Dim meshColl = mesh.MeshCollector
            Guide.InfoWriteLine("Mesh collector: " & meshColl.Name)
            ListMeshCollectorProperties(meshColl)

            Dim propTable = mesh.ElementPropertyTable
            ListPropertyTableProperties(propTable)
        End If

    End Sub

    Public Sub ListPropertyTableProperties(propTable As CAE.PropertyTable)

        Guide.InfoWriteLine("Property Table Neutral Name: " & propTable.DescriptorNeutralName)
        Guide.InfoWriteLine("Property Table Specific Name: " & propTable.DescriptorSpecificName)
        Dim propCount = propTable.GetPropertyCount()
        Guide.InfoWriteLine("Number of properties in table: " & propCount)
        
        For index As Integer = 0 To propCount - 1
            Dim propName = propTable.GetPropertyNameByIndex(index)
            Dim propType = propTable.GetPropertyType(propName)
            Guide.InfoWriteLine("Property: " & propName & " has type " & propType.ToString())
            Select Case propType
                Case CAE.PropertyTable.PropertyType.Integer
                    Dim value = propTable.GetIntegerPropertyValue(propName)
                    Guide.InfoWriteLine(propName & " = " & value)
                Case CAE.PropertyTable.PropertyType.Double
                    Dim value = propTable.GetDoublePropertyValue(propName)
                    Guide.InfoWriteLine(propName & " = " & value)
                Case CAE.PropertyTable.PropertyType.Boolean
                    Dim value = propTable.GetBooleanPropertyValue(propName)
                    Guide.InfoWriteLine(propName & " = " & value.ToString())
                Case CAE.PropertyTable.PropertyType.String
                    Dim value = propTable.GetStringPropertyValue(propName)
                    Guide.InfoWriteLine(propName & " = " & value)
                Case CAE.PropertyTable.PropertyType.Unknown
                    Guide.InfoWriteLine(propName & " is Undefined")
                Case CAE.PropertyTable.PropertyType.NamedPropertyTable
                    Dim npTable = propTable.GetNamedPropertyTablePropertyValue(propName)
                    ListNamedPropertyTable(npTable)
            End Select
            If propType = CAE.PropertyTable.PropertyType.NamedPropertyTable Then
                Dim npTable = propTable.GetNamedPropertyTablePropertyValue(propName)
                ListNamedPropertyTable(npTable)
            End If 
        Next
        Guide.InfoWriteLine("")

    End Sub

    Public Sub ListNamedPropertyTable(npTable As CAE.NamedPropertyTable)
        Guide.InfoWriteLine("Named Property Table: " & npTable.Name)
        Guide.InfoWriteLine("LanguageName: " & npTable.LanguageName & ", SolverName: " & npTable.SolverName)
        ListPropertyTableProperties(npTable.PropertyTable)
    End Sub

    Public Sub ListMeshCollectorProperties(meshColl As CAE.MeshCollector)

        Dim femPart As CAE.FemPart = TryCast(theSession.Parts.BaseWork, CAE.FemPart)

        If femPart Is Nothing Then
            theNxMessageBox.Show(applicationTitle, NXMessageBox.DialogType.Error, "Fem Part must be loaded")
            Return
        End If
        Dim meshMgr = CType(femPart.BaseFEModel.MeshManager, CAE.MeshManager)
        Dim name As String = ""
        Dim meshCollBuilder = meshMgr.CreateCollectorBuilder(meshColl, name)
        Guide.InfoWriteLine("Mesh Collector: " & meshCollBuilder.CollectorName)
        ListPropertyTableProperties(meshCollBuilder.PropertyTable)

    End Sub

    Public Function GetUnloadOption(ByVal dummy As String) As Integer

        'Unloads the image immediately after execution within NX
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately

        '----Other unload options-------
        'Unloads the image when the NX session terminates
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination

        'Unloads the image explicitly, via an unload dialog
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly
        '-------------------------------

    End Function

End Module
