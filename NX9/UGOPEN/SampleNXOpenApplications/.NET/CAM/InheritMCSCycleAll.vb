'=============================================================================
'
'   Copyright 2009 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION
        ' This program will cycle through all MILL, TURN, and WEDM orient 
		' geometry groups in the part and turn on MCS Inheritance.
		'
		' This fix should be applied to all template parts.
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
        Dim geomRootTag As Tag = Tag.Null

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            theUfSession.Cam.InitSession()
            theUfSession.Setup.AskSetup(setupTag)

            ' If there is a setup only then do we have to go further
            If setupTag <> 0 Then

                Dim ptr As IntPtr = New System.IntPtr
                Dim cycle_cb_fn As UFNcgroup.CycleCbFT = New UFNcgroup.CycleCbFT(AddressOf cycle_cb)

                ' Get the Machine Tool View's Root
                theUfSession.Setup.AskGeomRoot(setupTag, geomRootTag)

                If geomRootTag <> 0 Then
                    'Cycle through the Geometry View and find every object 
                    theUfSession.Ncgroup.CycleMembers(geomRootTag, cycle_cb_fn, ptr)
                End If

            End If

        End If
    End Sub

    'This is the fucntion that is called on every object encountered in the cycling
    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean

        Dim answer As Boolean
        Dim WorkPart As Part = theSession.Parts.Work

        ' When cycling check if the object is a Group
        theUfSession.Ncgroup.IsGroup(camObjectTag, answer)

        ' Only then we need to do something
        If answer = True Then
            Dim objectType As Integer
            Dim objectSubtype As Integer

            'Get the type and subtype of the Orient objects
            theUfSession.Obj.AskTypeAndSubtype(camObjectTag, objectType, objectSubtype)

            'Orient is type 105
            If objectType = 105 Then
                ' Mill Orient is 30, Turn Orient is 60 and WEDM Orient is 120
                If objectSubtype = 30 Or objectSubtype = 120 Then
                    ' Inherit the MCS(index is 59)
                    theUfSession.Param.InheritValue(camObjectTag, 59)
                End If
            End If
        End If
        Return True
    End Function

End Module


















