'=============================================================================
'
'   Copyright 2012 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION
        ' Change the default value for fixture offset from 0 to 1.
		' 
		' This program will cycle through all MILL orient and TURN orient 
		' geometry groups in the part, and if fixture offset is 0, set to 1.
		'
		' This change was applied to all template parts in NX 8.5.
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
		theSession.ListingWindow.Open()
		theSession.ListingWindow.WriteLine("--------------------------------------")

    End Sub

    'This is the fucntion that is called on every object encountered in the cycling
    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean
        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)

        Dim answer As Boolean
        Dim WorkPart As Part = theSession.Parts.Work

        ' When cycling check if the object is a Group
        theUfSession.Ncgroup.IsGroup(camObjectTag, answer)

        ' Only then we need to do something
        If answer = True Then
            Dim objectType As Integer
            Dim objectSubtype As Integer

            'Get the type and subtype of the Group
            theUfSession.Obj.AskTypeAndSubtype(camObjectTag, objectType, objectSubtype)
	
            If objectType = 105 Then		' Orient Group
                If objectSubtype = 30 Then		' Mill Orient
					Dim OrientGeomBuilder1 As CAM.MillOrientGeomBuilder
					OrientGeomBuilder1 = workPart.CAMSetup.CAMGroupCollection.CreateMillOrientGeomBuilder(camObject)
					If OrientGeomBuilder1.FixtureOffsetBuilder.Value = 0 Then
						OrientGeomBuilder1.FixtureOffsetBuilder.Value = 1
						theSession.ListingWindow.Open()
						theSession.ListingWindow.WriteLine("Set Fixture Offset = 1 in " & camObject.Name() )
					End If
					OrientGeomBuilder1.Commit()
					OrientGeomBuilder1.Destroy()

				Elseif objectSubtype = 60 Then	' Turn Orient
					Dim OrientGeomBuilder1 As CAM.TurnOrientGeomBuilder
					OrientGeomBuilder1 = workPart.CAMSetup.CAMGroupCollection.CreateTurnOrientGeomBuilder(camObject)
					If OrientGeomBuilder1.FixtureOffsetBuilder.Value = 0 Then
						OrientGeomBuilder1.FixtureOffsetBuilder.Value = 1
						theSession.ListingWindow.Open()
						theSession.ListingWindow.WriteLine("Set Fixture Offset = 1 in " & camObject.Name() )
					End If
					OrientGeomBuilder1.Commit()
					OrientGeomBuilder1.Destroy()
				
				Elseif objectSubtype = 120 Then	' WEDM Orient
					' No changes

				End If
            End If
        End If
        Return True
    End Function

End Module


















