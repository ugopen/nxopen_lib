' NX 6.0.3.6
' GroupUnmeshedCaeFaces.vb - Create groups of unmeshed and meshed CAE polygon faces
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
'Imports NXOpen.UI
Imports NXOpen.Utilities

Module GroupUnmeshed

    Dim theSession As Session = Session.GetSession()
    Dim theUFSession As NXOpen.UF.UFSession = UFSession.GetUFSession()
    Dim theLW As NXOpen.ListingWindow = theSession.ListingWindow()
    Dim theUI As NXOpen.UI = NXOpen.UI.GetUI()
    Dim theNXMessageBox As NXMessageBox = theUI.NXMessageBox

    Dim DEBUG As Integer = 0

    Sub Main()

        ' Setup session and part variables        
        Dim basePart As BasePart = theSession.Parts.BaseWork

        ' Check to see if this is a cae part (.fem or .sim)
        If basePart Is Nothing Then
            theNXMessageBox.Show("Group Unmeshed - *** ERROR ***", NXMessageBox.DialogType.Error, "There is no active work part. Exiting")
            Return
        End If

        If (Not TypeOf basePart Is CAE.CaePart) Then
            theNXMessageBox.Show("Group Unmeshed - *** ERROR ***", NXMessageBox.DialogType.Error, "The work part is not a .fem or .sim. Please start execution with the work file set to a .fem or .sim")
            Return
        End If

        theLW.Open()
        theLW.WriteLine("Starting Group Unmeshed...")
        theUFSession.Ui.SetStatus("Starting Group Unmeshed")

        Dim StartTime As Date = Now
        theLW.WriteLine(vbNewLine + "Start Time: " + StartTime.ToLongTimeString)

        CyclePartCaeFaces(basePart)

        'Report processing time
        Dim EndTime As Date = Date.Now
        Dim difference As TimeSpan = EndTime.Subtract(StartTime)

        theLW.WriteLine(vbNewLine + "End Time: " + EndTime.ToLongTimeString)
        theLW.WriteLine("  Total processing time: " + Math.Round(difference.TotalSeconds).ToString + " seconds" + vbNewLine)

        theLW.WriteLine(vbNewLine + "Group Unmeshed Finished..." + vbNewLine)
        theUFSession.Ui.SetStatus("Group Unmeshed finished")

    End Sub

    Sub CyclePartCaeFaces(ByRef basePart As BasePart)

        Dim caeWorkPart As CAE.CaePart = CType(basePart, CAE.CaePart)

        Dim UnrelatedFaceTags As New ArrayList
        Dim RelatedFaceTags As New ArrayList

        Dim objCnt As Integer = 0
        Dim objectTag As Tag
        Dim NULLTAG As Tag = NXOpen.Tag.Null

        theUFSession.Obj.CycleObjsInPart(caeWorkPart.Tag, NXOpen.UF.UFConstants.UF_caegeom_type, objectTag)

        Do While objectTag <> NULLTAG
            Dim nxobject As NXObject = NXOpen.Utilities.NXObjectManager.Get(objectTag)
            Dim objType As Integer = 0
            Dim objSubType As Integer = 0

            theUFSession.Obj.AskTypeAndSubtype(objectTag, objType, objSubType)

            If objSubType = NXOpen.UF.UFConstants.UF_caegeom_face_subtype Then

                ' Get current face object
                Dim face() As CAE.CAEFace = Nothing
                face(0) = CType(nxobject, CAE.CAEFace)
                objCnt = objCnt + 1
                If DEBUG Then theLW.WriteLine("CAE Face [" + objCnt.ToString() + "] Obj Type = [" + nxobject.GetType.ToString() + "] ")

                ' Create a dummy builder to select elements related to the face
                Dim method As CAE.RelatedElemMethod = caeWorkPart.SmartSelectionMgr.CreateRelatedElemMethod(face, False)
                Dim dummyBuilder As CAE.ShowOnlyBuilder = caeWorkPart.ShowHideMgr.CreateShowOnlyBuilder()
                dummyBuilder.Selection.Add(method)
                method.Dispose()

                ' Get the number of elements related to the face
                Dim iRelatedElements As Integer = dummyBuilder.Selection.Size
                dummyBuilder.Destroy()
                If DEBUG Then theLW.WriteLine("    Face has " + iRelatedElements.ToString + " related elements")

                ' Sort faces into related to/not related to element groups
                If (iRelatedElements = 0) Then
                    UnrelatedFaceTags.Add(face(0).Tag)
                Else
                    RelatedFaceTags.Add(face(0).Tag)
                End If

            End If

            theUFSession.Obj.CycleObjsInPart(caeWorkPart.Tag, NXOpen.UF.UFConstants.UF_caegeom_type, objectTag)

        Loop

        Dim caePartFile As String = caeWorkPart.FullPath
        Dim anyOf As Char() = "/\".ToCharArray()
        Dim caePartName As String = Right(caePartFile, (caePartFile.Length - caePartFile.LastIndexOfAny(anyOf)) - 1)

        theLW.WriteLine(vbNewLine + vbTab + caePartName + " has " + objCnt.ToString() + " CAE faces")

        ' Create a group of faces not related to elements
        Dim iUnrelatedFaces As Integer = UnrelatedFaceTags.Count
        If (iUnrelatedFaces > 0) Then
            CreateCaeGroup(caeWorkPart, UnrelatedFaceTags, "Faces unrelated to elements")
            theLW.WriteLine(vbTab + vbTab + "- Faces with no related elements:  " + iUnrelatedFaces.ToString)
        End If

        ' Create a group of faces related to elements
        Dim iRelatedFaces As Integer = RelatedFaceTags.Count
        If (iRelatedFaces > 0) Then
            CreateCaeGroup(caeWorkPart, RelatedFaceTags, "Faces related to elements")
            theLW.WriteLine(vbTab + vbTab + "- Faces with related elements:     " + iRelatedFaces.ToString)
        End If

    End Sub

    Sub CreateCaeGroup(ByRef basePart As BasePart, ByVal objTags As ArrayList, ByVal groupName As String)

        Dim objCount As Integer = objTags.Count
        If (objCount > 0) Then

            Dim GroupObjects(objCount - 1) As TaggedObject
            Dim entityCount As Integer = 0
            For Each faceTag As Tag In objTags
                GroupObjects(entityCount) = NXObjectManager.Get(faceTag)
                entityCount += 1
            Next

            Dim caeWorkPart As CAE.CaePart = CType(basePart, CAE.CaePart)
            Dim caeGroup As CAE.CaeGroup = caeWorkPart.CaeGroups.CreateGroup(groupName, GroupObjects)

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


