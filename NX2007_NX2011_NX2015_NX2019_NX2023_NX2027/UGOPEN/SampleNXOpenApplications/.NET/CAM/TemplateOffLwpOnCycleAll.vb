'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION
'     This program will cycle through all the CAM objects in the part and
'     in Template Settings turn template OFF and Load With Parent ON.
' ============================================================================

 
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module AllCAMObjects

    Dim theSession As Session
    Dim theUfSession As UFSession


    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = TheSession.Parts.Work

        Dim setupTag As Tag
        Dim camObjectTag As Tag
        Dim RootTag As Tag

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            theUfSession.Cam.InitSession()
            theUfSession.Setup.AskSetup(setupTag)

            ' If there is a setup only then do we have to go further
            If setupTag <> 0 Then

                Dim ptr As IntPtr = New System.IntPtr
                Dim cycle_cb_fn As UFNcgroup.CycleCbFT = New UFNcgroup.CycleCbFT(AddressOf cycle_cb)

                ' Get the Program View's Root
                theUfSession.Setup.AskProgramRoot(setupTag, RootTag)
                If RootTag <> 0 Then
                    'Cycle throught this view and find every object 
                    theUfSession.Ncgroup.CycleMembers(RootTag, cycle_cb_fn, ptr)
                End If

                ' Get the Tool View's Root
                theUfSession.Setup.AskMctRoot(setupTag, RootTag)
                If RootTag <> 0 Then
                    'Cycle throught this view and find every object 
                    theUfSession.Ncgroup.CycleMembers(RootTag, cycle_cb_fn, ptr)
                End If

                ' Get the Method View's Root
                theUfSession.Setup.AskMthdRoot(setupTag, RootTag)
                If RootTag <> 0 Then
                    'Cycle throught this view and find every object 
                    theUfSession.Ncgroup.CycleMembers(RootTag, cycle_cb_fn, ptr)
                End If

                ' Get the Geometry View's Root
                theUfSession.Setup.AskGeomRoot(setupTag, RootTag)
                If RootTag <> 0 Then
                    'Cycle throught this view and find every object 
                    theUfSession.Ncgroup.CycleMembers(RootTag, cycle_cb_fn, ptr)
                End If

            End If

        End If
    End Sub

    'This is the fucntion that is called on every object encountered in the cycling
    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean

        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)
        Dim objects(0) As CAM.CAMObject
        objects(0) = camObject

        Dim WorkPart As Part = TheSession.Parts.Work

        'Template Settings -turn template OFF, Turn Load With Parent ON
        WorkPart.CAMSetup.SetTemplateStatus(objects, False, True)
        Return True

    End Function

End Module
















