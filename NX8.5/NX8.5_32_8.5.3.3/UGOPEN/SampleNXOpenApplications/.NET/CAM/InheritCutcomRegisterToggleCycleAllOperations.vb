'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION
        ' This program will cycle through all the operations in the part and toggle on
		' inheritance for the cuctom register. 
		' This assures that when the operation changes tool parent, the cuctom register
		' is inherited from the tool, and the output toggle is turned on.
		'
		'This program was run on all template operations in V7.0 to resolve PRs
		' where the cutcom output toggle was not turning on because inheritance had
		' been previously turned off and on in the UI.
' ============================================================================

Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module InheritMCS

    Dim theSession As Session
    Dim theUfSession As UFSession


    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = theSession.Parts.Work

        Dim setupTag As Tag = Tag.Null
        Dim camObjectTag As Tag = Tag.Null
        Dim programRootTag As Tag = Tag.Null

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            theUfSession.Cam.InitSession()
            theUfSession.Setup.AskSetup(setupTag)

            ' If there is a setup only then do we have to go further
            If setupTag <> 0 Then

                Dim ptr As IntPtr = New System.IntPtr
                Dim cycle_cb_fn As UFNcgroup.CycleCbFT = New UFNcgroup.CycleCbFT(AddressOf cycle_cb)

                ' Get the Program View's Root
                theUfSession.Setup.AskProgramRoot(setupTag, programRootTag)

                If programRootTag <> 0 Then
                    'Cycle through the Geometry View and find every object 
                    theUfSession.Ncgroup.CycleMembers(programRootTag, cycle_cb_fn, ptr)
                End If

            End If

        End If
    End Sub

    'This is the fucntion that is called on every object encountered in the cycling
    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean

        Dim answer As Boolean
        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)
        Dim WorkPart As Part = theSession.Parts.Work
        'Dim lw As ListingWindow = theSession.ListingWindow

        ' Open Listing Window. If the listing window is already open this will not do anything
        'lw.Open()

        ' When cycling check if the object is a Group
        theUfSession.Ncgroup.IsGroup(camObjectTag, answer)
		
        ' It is not a group, so keep going
        If answer = False Then
            'Check if the object is an Operation
            If TypeOf camObject Is CAM.Operation Then
                Dim operationType As Integer
                Dim operationSubtype As Integer
                'Get the type and subtype of the operation
                theUFSession.Obj.AskTypeAndSubtype(camObjectTag, operationType, operationSubtype)

                If operationSubtype = 700 Or operationSubtype = 1300 Then ' 700 is WEDM Operation and 1300 is WEDM Machine Control Operation
                    'Do nothing
                    theSession.LogFile.WriteLine("Skipping OperationSubtype " & operationSubtype)
                    'lw.WriteLine("Skipping OperationSubtype " & operationSubtype)

                Else
                    'Edit this operation
                    theUfSession.Param.InheritValue(camObjectTag, UFConstants.UF_PARAM_TL_CUTCOM_REG_TOG)
                    theSession.LogFile.WriteLine("Editing OperationSubtype " & operationSubtype)
                    'lw.WriteLine("Editing OperationSubtype " & operationSubtype)
                End If
			Else
				'Not an Operation - should never get here
				theUfSession.Param.InheritValue(camObjectTag, UFConstants.UF_PARAM_TL_CUTCOM_REG_TOG)
				theSession.LogFile.WriteLine("Editing Non Operation")
				'lw.WriteLine("Editing Non Operation")
            End If
        End If
        Return True
    End Function

End Module


















