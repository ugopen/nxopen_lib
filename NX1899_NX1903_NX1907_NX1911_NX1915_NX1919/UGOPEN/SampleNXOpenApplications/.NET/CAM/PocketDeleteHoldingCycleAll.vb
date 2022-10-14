'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION
        ' This program will cycle through all the pockets in the part and
	    ' delete all the holding systems in the list.
		'
		' This allows the pockets to accept all tools from the library.
' ============================================================================

Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module pockets

    Dim theSession As Session
    Dim theUfSession As UFSession


    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = TheSession.Parts.Work

        Dim setupTag As Tag
        Dim camObjectTag As Tag
        Dim mctRootTag As Tag

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            theUfSession.Cam.InitSession()
            theUfSession.Setup.AskSetup(setupTag)

            ' If there is a setup only then do we have to go further
            If setupTag <> 0 Then

                Dim ptr As IntPtr = New System.IntPtr
                Dim cycle_cb_fn As UFNcgroup.CycleCbFT = New UFNcgroup.CycleCbFT(AddressOf cycle_cb)

                ' Get the Machine Tool View's Root
                theUfSession.Setup.AskMctRoot(setupTag, mctRootTag)

                If mctRootTag <> 0 Then
                    'Cycle throught the Machine Tool View and find every object 
                    theUfSession.Ncgroup.CycleMembers(mctRootTag, cycle_cb_fn, ptr)
                End If

            End If

        End If
    End Sub

    'This is the fucntion that is called on every object encountered in the cycling
    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean

        Dim answer As Boolean
        Dim WorkPart As Part = TheSession.Parts.Work

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

                ' Define the builder
                Dim pocketBuilder As CAM.MachinePocketGroupBuilder
                pocketBuilder = workPart.CAMSetup.CAMGroupCollection.CreateMachinePocketGroupBuilder(pocketObject)
				
				'Clear the list of holding systems
                pocketBuilder.HoldingSystemsList.Clear(ObjectList.DeleteOption.Delete)

                'Save the changes made
                pocketBuilder.Commit()

                'Clean up memory
                pocketBuilder.Destroy()

            End If

        End If

        Return True
    End Function

End Module


















