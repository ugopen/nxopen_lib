' ReassignElements.vb - Move elements into new meshes
'
' 
'
'------------------------------------------------------------
Option Strict Off
Imports System
Imports System.IO
Imports System.Windows.Forms
Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.BlockStyler

Module NXJournal
    Sub Main()

        '------------------------------------------------------------------------------
        ' Setup the Session
        '------------------------------------------------------------------------------
        Dim theSession As Session = Session.GetSession()
        Dim theUFSession As UFSession = UFSession.GetUFSession()
        Dim theUI As NXOpen.UI = NXOpen.UI.GetUI()
        Dim theNXMessageBox As NXMessageBox = theUI.NXMessageBox
        Dim workFemPart As CAE.FemPart = CType(theSession.Parts.BaseWork, CAE.FemPart)
        Dim displayFemPart As CAE.FemPart = CType(theSession.Parts.BaseDisplay, CAE.FemPart)
        Dim femPart1 As CAE.FemPart = CType(workFemPart, CAE.FemPart)

        '------------------------------------------------------------------------------
        ' Find the group and read its contents. Assumptions:
        '       1) This script is executed in a FEM
        '       1) Group is named "ReassignElements"
        '       2) Group contains elements to extract from mesh(es) and put in new mesh(es)
        '------------------------------------------------------------------------------
        Dim caeGroup1 As CAE.CaeGroup = CType(workFemPart.CaeGroups.FindObject("ReassignElements"), CAE.CaeGroup)
        Dim groupEntities() As TaggedObject = caeGroup1.GetEntities()
        Dim elements() As TaggedObject
        Dim nele As Integer
        nele = 0
        For Each grpObj As TaggedObject In groupEntities
            If TypeOf grpObj Is CAE.FEElement Then
                ReDim Preserve elements(nele)
                elements(nele) = grpObj
                nele += 1
            End If
        Next grpObj
        If (nele = 0) Then
            theNXMessageBox.Show("Reassign Elements", NXMessageBox.DialogType.Error, "ReassignElements group has no elements")
            Return
        End If

        '------------------------------------------------------------------------------
        ' Prepare to copy elements - delta is 0.0
        '------------------------------------------------------------------------------
        Dim markId1 As Session.UndoMarkId
        markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")
        theSession.SetUndoMarkName(markId1, "Reassign Elements")
        Dim fEModel1 As CAE.FEModel = CType(workFemPart.FindObject("FEModel"), CAE.FEModel)

        Dim elementTranslateBuilder1 As CAE.ElementTranslateBuilder
        elementTranslateBuilder1 = fEModel1.NodeElementMgr.CreateElementTranslateBuilder()
        elementTranslateBuilder1.ElementDimension = CAE.ElementTranslateBuilder.ElemDimensionType.Any
        elementTranslateBuilder1.NumCopy = 1
        elementTranslateBuilder1.Method = CAE.ElementTranslateBuilder.MethodType.Component
        elementTranslateBuilder1.XDistance.RightHandSide = "0"
        elementTranslateBuilder1.YDistance.RightHandSide = "0"
        elementTranslateBuilder1.ZDistance.RightHandSide = "0"
        elementTranslateBuilder1.Increment = 1

        '------------------------------------------------------------------------------
        ' Set the selected elements to copy
        '------------------------------------------------------------------------------
        Dim objs1(nele - 1) As CAE.SetObject
        Dim i = 0
        While i < nele
            objs1(i).Obj = elements(i)
            objs1(i).SubType = CAE.CaeSetObjectSubType.None
            objs1(i).SubId = 0
            elementTranslateBuilder1.ElementSelection.Selection.Add(objs1(i).obj)
            i += 1
        End While


        '------------------------------------------------------------------------------
        ' Commit the copy and cleanup
        '------------------------------------------------------------------------------
        Dim nXObject1 As NXObject
        nXObject1 = elementTranslateBuilder1.Commit()
        elementTranslateBuilder1.Destroy()

        '------------------------------------------------------------------------------
        ' Delete the original elements, removing orphan nodes
        '------------------------------------------------------------------------------
        Dim elementDeleteBuilder1 As CAE.ElementDeleteBuilder
        elementDeleteBuilder1 = fEModel1.NodeElementMgr.CreateDeleteElementBuilder()
        elementDeleteBuilder1.DeleteDangling = True
        While i < nele
            elementDeleteBuilder1.Element.Selection.Add(objs1(0).obj)
        End While

        Dim nXObject2 As NXObject
        nXObject2 = elementDeleteBuilder1.Commit()
        elementDeleteBuilder1.Destroy()

        '------------------------------------------------------------------------------
        ' Merge nodes
        '------------------------------------------------------------------------------
        Dim num_meshes As Integer = 0 'All meshes
        Dim mesh_tags As NXOpen.Tag = Nothing
        Dim iMerge As Boolean = True 'Do the merge
        Dim dtol As Double = 0.01
        Dim nNodes As Integer
        theUFSession.Sf.CheckModelDuplicateNodes(num_meshes, mesh_tags, imerge, dtol, nNodes)

    End Sub
End Module
