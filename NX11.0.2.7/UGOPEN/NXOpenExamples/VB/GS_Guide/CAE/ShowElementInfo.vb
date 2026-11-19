'showConnectedElements.vb - Recursively select all elements connected to a set
'                           of seed elements
'
'  Description:
'    User will be prompted to select a set of seed elements. The program loops
'    through selecting nodes related to elements, then elements related to nodes
'    until the number of elements in the list does not chenge. A "Show Only" is
'    done using the final list of elements as input.
'
'  This program must be executed in a CAE part.
'
'  Instructions:
'    1) Run this program from within a CAE file in NX Advanced Simulation
'       - Use 'Tools > Journal > Play' to run showConnectedElements.vb
'
'  Known Issues:
'

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

    Dim applicationTitle As String = "Show Connected Elements"

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

            Dim propTable = mesh.ElementPropertyTable
            Guide.InfoWriteLine("Property Table Neutral Name: " & propTable.DescriptorNeutralName)
            Guide.InfoWriteLine("Property Table Specific Name: " & propTable.DescriptorSpecificName)
        End If

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
