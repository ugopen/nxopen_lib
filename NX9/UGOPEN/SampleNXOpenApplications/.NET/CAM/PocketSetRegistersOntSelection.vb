'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION
'         ' This program will edit a pocket selected in the ONT and
  	  ' set adjust and cutom to same as pocket ID.
' ============================================================================

Option Strict Off
Imports System
Imports System.IO
Imports System.Windows.Forms
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module flutelength

    Dim theSession As Session
    Dim theUfSession As UFSession


    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = TheSession.Parts.Work

        Dim setupTag As Tag
        Dim camObjectTag As Tag
        Dim selectedTags() As NXOpen.Tag
        Dim selectedCount As Integer

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            theUfSession.Cam.InitSession()
            theUfSession.Setup.AskSetup(setupTag)

            ' If there is a setup only then we go further
            If setupTag <> 0 Then

                ' Get the selected nodes from the Operation Navigator
                theUfSession.UiOnt.AskSelectedNodes(selectedCount, selectedTags)

                Dim ptr As IntPtr = New System.IntPtr
                Dim cycle_cb_fn As UFNcgroup.CycleCbFT = New UFNcgroup.CycleCbFT(AddressOf cycle_cb)

                Dim i As Integer
                'Loop over the selected nodes to take action
                For i = 0 To selectedCount - 1
                    ' The selected item needs to be checked to take action
                    action(selectedTags(i))
                    ' Now if the selected item is a Group object then we need to cycle objects inside it
                    theUfSession.Ncgroup.CycleMembers(selectedTags(i), cycle_cb_fn, ptr)
                Next i

            End If

        End If
    End Sub

    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean
        Dim answer As Boolean

        ' Every item needs to be checked to take action
        answer = action(camObjectTag)
        Return answer

    End Function

    Function action(ByVal camObjectTag As Tag) As Boolean

        Dim WorkPart As Part = TheSession.Parts.Work
        Dim answer As Boolean

        ' When cycling check if the obejct is a Group
        theUfSession.Ncgroup.IsGroup(camObjectTag, answer)

        ' Only then we need to do something
        If answer = True Then
            Dim objectType As Integer
            Dim objectSubtype As Integer

            'Get the type and subtype of the group object
            theUFSession.Obj.AskTypeAndSubtype(camObjectTag, objectType, objectSubtype)

            'Pockets are type 106 and subtype 2
            If objectType = 106 And objectSubtype = 2 Then
                ' Find the pocket object from the Tag
                Dim pocketObject As NXObject = NXObjectManager.Get(camObjectTag)
                ' Set pocket values
                Dim pocketBuilder As CAM.MachinePocketGroupBuilder

                pocketBuilder = workPart.CAMSetup.CAMGroupCollection.CreateMachinePocketGroupBuilder(pocketObject)
                'Set Adjust Register type to be Same As Pocket
                Dim pocketNumberBuilder As CAM.InheritableIntBuilder = pocketBuilder.PocketIdBuilder
                Dim pocketIdStringBuilder As CAM.InheritableTextBuilder = pocketBuilder.PocketIdStringBuilder
                Dim adjustRegisterBuilder As CAM.InheritableIntBuilder = pocketBuilder.AdjustIdBuilder
                Dim cutcomRegisterBuilder As CAM.InheritableIntBuilder = pocketBuilder.CutcomIdBuilder

                Dim pocketNumber As Integer = pocketNumberBuilder.Value
                pocketIdStringBuilder.Value = pocketNumber.ToString()
                adjustRegisterBuilder.Value = pocketNumber
                cutcomRegisterBuilder.Value = pocketNumber

                'Save the changes made
                pocketBuilder.Commit()

                'Clean up memory
                pocketBuilder.Destroy()

            End If

        End If

        Return True
    End Function

End Module

















