'=============================================================================
'
'                   Copyright (c) 2008 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'

'==============================================================================
'  WARNING!!  This file is overwritten by the Block Styler while generating
'  the automation code. Any modifications to this file will be lost after
'  generating the code again.
'==============================================================================
'------------------------------------------------------------------------------
'These imports are needed for the following template code
'------------------------------------------------------------------------------
Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.BlockStyler
Imports NXOpen.UF
'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class HoleCoordinates
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theHoleCoordinates As HoleCoordinates
    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private groupPoint As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private origin As NXOpen.BlockStyler.UIBlock ' Block type: Specify Point
    Private groupXdir As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private xDir As NXOpen.BlockStyler.UIBlock ' Block type: Specify Vector
    Private groupYdir As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private yDir As NXOpen.BlockStyler.UIBlock ' Block type: Specify Vector
    Private groupFace As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private face As NXOpen.BlockStyler.UIBlock ' Block type: Face Collector
    Private groupInfo As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private listBoxInfo As NXOpen.BlockStyler.ListBox ' Block type: List Box
    Private buttonInfo As NXOpen.BlockStyler.UIBlock ' Block type: Button

    'user defined variables
    Dim refaxis1 As DatumAxis
    Dim refaxis2 As DatumAxis
    Dim axispoint As Point
    Dim holeface As Face
    Dim workPart As Part
    Dim displayPart As Part
    Dim point1 As Point
    Dim vectCol(-1) As TaggedObject
    Dim vectCol1(-1) As TaggedObject
    Dim pointCol(-1) As TaggedObject
    Dim faceCol(-1) As TaggedObject
    Dim objects1(-1) As NXObject
    Dim allholesNX5(-1) As String
    Dim allholesNX6(-1) As String
    Dim holelocation As Point3d
    Dim holeCoordinates As Double
    Dim ufsess As UFSession

#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try

            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialogName = "HoleCoordinates.dlx"
            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
            theDialog.AddDialogShownHandler(AddressOf dialogShown_cb)

        Catch ex As Exception
            Throw ex
        End Try
    End Sub
#End Region

    '------------------------------- DIALOG LAUNCHING ---------------------------------
    '
    '    Before invoking this application one needs to open any part/empty part in NX
    '    because of the behavior of the blocks.
    '
    '    Make sure the dlx file is in one of the following locations:
    '        1.) From where NX session is launched
    '        2.) $UGII_USER_DIR/application
    '        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    '            recommended. This variable is set to a full directory path to a file 
    '            containing a list of root directories for all custom applications.
    '            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
    '
    '    You can create the dialog using one of the following way:
    '
    '    1. Journal Replay
    '
    '        1) Replay this file through Tool->Journal->Play Menu.
    '
    '    2. USER EXIT
    '
    '        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
    '        2) Invoke the Shared Library through File->Execute->NX Open menu.
    '
    '------------------------------------------------------------------------------
    Public Shared Sub Main()
        Try

            theHoleCoordinates = New HoleCoordinates()
            ' The following method shows the dialog immediately
            theHoleCoordinates.Show()

        Catch ex As Exception


            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theHoleCoordinates.Dispose()
        End Try
    End Sub
    Public Shared Function GetUnloadOption(ByVal arg As String) As Integer

        Return CType(Session.LibraryUnloadOption.Immediately, Integer)

    End Function
    '------------------------------------------------------------------------------
    ' Following method cleanup any housekeeping chores that may be needed.
    ' This method is automatically called by NX.
    '------------------------------------------------------------------------------
    Public Shared Sub UnloadLibrary(ByVal arg As String)
        Try


        Catch ex As Exception

            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'This method shows the dialog on the screen
    '------------------------------------------------------------------------------
    Public Sub Show()
        Try

            theDialog.Show()

        Catch ex As Exception

            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Method Name: Dispose
    '------------------------------------------------------------------------------
    Public Sub Dispose()
        If theDialog IsNot Nothing Then
            theDialog.Dispose()
            theDialog = Nothing
        End If
    End Sub

    '------------------------------------------------------------------------------
    '---------------------Block Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------

    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try
            workPart = theSession.Parts.Work
            displayPart = theSession.Parts.Display
            ufsess = NXOpen.UF.UFSession.GetUFSession()

            groupPoint = theDialog.TopBlock.FindBlock("groupPoint")
            origin = theDialog.TopBlock.FindBlock("origin")
            groupXdir = theDialog.TopBlock.FindBlock("groupXdir")
            xDir = theDialog.TopBlock.FindBlock("xDir")
            groupYdir = theDialog.TopBlock.FindBlock("groupYdir")
            yDir = theDialog.TopBlock.FindBlock("yDir")
            groupFace = theDialog.TopBlock.FindBlock("groupFace")
            face = theDialog.TopBlock.FindBlock("face")
            groupInfo = theDialog.TopBlock.FindBlock("groupInfo")
            buttonInfo = theDialog.TopBlock.FindBlock("buttonInfo")
            listBoxInfo = CType(theDialog.TopBlock.FindBlock("listBoxInfo"), NXOpen.BlockStyler.ListBox)

            'User defined code
            setEnablePropForBlock(buttonInfo, False)
            setEnablePropForBlock(xDir, False)
            setEnablePropForBlock(yDir, False)
            setEnablePropForBlock(face, False)

            refaxis1 = Nothing
            refaxis2 = Nothing

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Callback Name: dialogShown_cb
    'This callback is executed just before the dialog launch. Thus any value set 
    'here will take precedence and dialog will be launched showing that value. 
    '------------------------------------------------------------------------------
    Public Sub dialogShown_cb()
        Try

            '---- Enter your callback code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer

        Dim errorCode As Integer = 0

        Try

            If Not refaxis1 Is Nothing And Not refaxis2 Is Nothing Then
                Dim delaxis1 As Features.Feature = CType(workPart.Features.FindObject(refaxis1.JournalIdentifier), Features.Feature)
                Dim delaxis2 As Features.Feature = CType(workPart.Features.FindObject(refaxis2.JournalIdentifier), Features.Feature)
                Array.Resize(objects1, 2)
                objects1(objects1.Length - 2) = delaxis1
                objects1(objects1.Length - 1) = delaxis2
                deletedatumaxis(objects1)
                refaxis1 = Nothing
                refaxis2 = Nothing
            Else
                MsgBox("please define all the inputs")
            End If

        Catch ex As Exception
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

        apply_cb = errorCode

    End Function

    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try

            If block Is origin Then

                Dim originProperties As PropertyList = origin.GetProperties()
                pointCol = originProperties.GetTaggedObjectVector("SelectedObjects")
                deletePropertyList(originProperties)

                axispoint = CType(pointCol(0), Point)
                setEnablePropForBlock(xDir, True)
                If Not refaxis1 Is Nothing Then
                    refaxis1 = editdatumaxis(refaxis1, CType(vectCol(0), Direction), axispoint)
                End If
                If Not refaxis2 Is Nothing Then
                    refaxis2 = editdatumaxis(refaxis2, CType(vectCol1(0), Direction), axispoint)
                End If

            ElseIf block Is xDir Then

                Dim xDirProperties As PropertyList = xDir.GetProperties()
                vectCol = xDirProperties.GetTaggedObjectVector("SelectedObjects")
                deletePropertyList(xDirProperties)
                If refaxis1 Is Nothing Then
                    refaxis1 = datumaxiscreater(axispoint, vectCol(0))
                Else
                    refaxis1 = editdatumaxis(refaxis1, CType(vectCol(0), Direction), axispoint)
                End If
                setEnablePropForBlock(yDir, True)

            ElseIf block Is yDir Then

                Dim yDirProperties As PropertyList = yDir.GetProperties()
                vectCol1 = yDirProperties.GetTaggedObjectVector("SelectedObjects")
                deletePropertyList(yDirProperties)

                If refaxis2 Is Nothing Then
                    refaxis2 = datumaxiscreater(axispoint, vectCol1(0))
                Else
                    refaxis2 = editdatumaxis(refaxis2, CType(vectCol1(0), Direction), axispoint)
                End If
                setEnablePropForBlock(face, True)

            ElseIf block Is face Then

                Dim faceProperties As PropertyList = face.GetProperties()
                faceCol = faceProperties.GetTaggedObjectVector("SelectedObjects")
                deletePropertyList(faceProperties)

                If faceCol.Length > 0 Then
                    holeface = CType(faceCol(0), Face)

                    setEnablePropForBlock(buttonInfo, True)
                ElseIf faceCol.Length = 0 Then
                    holeface = Nothing
                    setEnablePropForBlock(buttonInfo, False)
                End If

            ElseIf block Is listBoxInfo Then

                Dim listBoxInfoProperties As PropertyList = listBoxInfo.GetProperties()
                Dim str() As String = listBoxInfoProperties.GetStrings("ListItems")
                Dim index() As Integer = listBoxInfoProperties.GetIntegerVector("SelectedItems")
                deletePropertyList(listBoxInfoProperties)

                If str(index(0)).Contains("HOLE") Then
                    Dim highlit As Features.Feature = CType(workPart.Features.FindObject(str(index(0))), Features.Feature)
                    If highlit.Equals(Nothing) = False Then
                        If index.Length > 0 Then
                            holeface.Unhighlight()
                            workPart.ModelingViews.WorkView.Regenerate()
                        End If
                        highlit.Highlight()
                    End If
                Else
                    workPart.ModelingViews.WorkView.Regenerate()
                End If

            ElseIf block Is buttonInfo Then

                Dim listBoxInfoProperties As PropertyList = listBoxInfo.GetProperties()
                Dim liststrings1() As String = listBoxInfoProperties.GetStrings("ListItems")
                If liststrings1.Length > 0 Then
                    ReDim liststrings1(-1)
                    listBoxInfoProperties.SetStrings("ListItems", liststrings1)
                End If

                Dim foundholes As Boolean = True
                Dim dir1 As Direction = Nothing
                Dim dir2 As Direction = Nothing
                Try
                    If vectCol.Length > 0 And vectCol1.Length > 0 Then
                        dir1 = CType(vectCol(0), Direction)
                        dir2 = CType(vectCol1(0), Direction)

                        'Checking for perpendicularity between vectors
                        Dim doublearray1() As Double = {dir1.Vector.X, dir1.Vector.Y, dir1.Vector.Z}
                        Dim doublearray2() As Double = {dir2.Vector.X, dir2.Vector.Y, dir2.Vector.Z}
                        Dim result1 As Integer
                        ufsess.Vec3.IsPerpendicular(doublearray1, doublearray2, 0.000001, result1)
                        If result1 = 0 Then
                            MsgBox("Selected Vectors should be perpendicular")
                            Return 0
                        End If

                        If dir1.Vector.Equals(dir2.Vector) = True Then
                            MsgBox("Selected Vectors are parallel")
                        Else
                            dir2.ReverseDirection()
                            If dir1.Vector.Equals(dir2.Vector) = True Then
                                MsgBox("Selected Vectors are parallel")
                                dir2.ReverseDirection()
                            Else

                                Dim selectedFaceEdges() As Edge = holeface.GetEdges

                                If allholesNX5.Length > 0 Then
                                    ReDim allholesNX5(-1)
                                End If
                                If allholesNX6.Length > 0 Then
                                    ReDim allholesNX6(-1)
                                End If

                                For Each seledge As Edge In selectedFaceEdges
                                    Dim journalstring As String = seledge.JournalIdentifier
                                    Dim individualstring() As String = journalstring.Split(" ")
                                    For Each featurestring As String In individualstring
                                        If featurestring.Contains("HOLE") Then
                                            If featurestring.Contains("SIMPLE") Then
                                                Array.Resize(allholesNX5, allholesNX5.Length + 1)
                                                allholesNX5.SetValue(featurestring, allholesNX5.Length - 1)
                                            Else
                                                featurestring = "SIMPLE " & featurestring
                                                Array.Resize(allholesNX6, allholesNX6.Length + 1)
                                                allholesNX6.SetValue(featurestring, allholesNX6.Length - 1)
                                            End If
                                        End If
                                    Next
                                Next
                                If allholesNX5.Length = 0 And allholesNX6.Length = 0 Then
                                    foundholes = False
                                    MsgBox("No hole features found on this face")
                                    Dim tags1(-1) As TaggedObject
                                    Dim faceProperties As PropertyList = face.GetProperties()
                                    faceProperties.SetTaggedObjectVector("SelectedObjects", tags1)
                                    deletePropertyList(faceProperties)
                                    Dim liststrings() As String = listBoxInfoProperties.GetStrings("ListItems")
                                    ReDim liststrings(-1)
                                    listBoxInfoProperties.SetStrings("ListItems", liststrings)

                                    setEnablePropForBlock(buttonInfo, False)


                                Else

                                    If allholesNX5.Length > 0 Then
                                        For Each nx5holes As String In allholesNX5
                                            Dim myfeat As Features.Hole = workPart.Features.FindObject(nx5holes)
                                            holelocation = myfeat.Location
                                            Dim point1 As Point = workPart.Points.CreatePoint(holelocation)
                                            Dim xcoord As Double = holedimension(refaxis1, refaxis2, point1)
                                            Dim ycoord As Double = holedimension(refaxis2, refaxis1, point1)
                                            Dim holedata(2) As String
                                            holedata(0) = myfeat.JournalIdentifier
                                            holedata(1) = "X Coodinate = " & xcoord.ToString
                                            holedata(2) = "Y Coodinate = " & ycoord.ToString
                                            Dim liststrings() As String = listBoxInfoProperties.GetStrings("ListItems")
                                            Array.Resize(liststrings, liststrings.Length + 3)
                                            liststrings.SetValue(holedata(0), liststrings.Length - 3)
                                            liststrings.SetValue(holedata(2), liststrings.Length - 2)
                                            liststrings.SetValue(holedata(1), liststrings.Length - 1)
                                            listBoxInfoProperties.SetStrings("ListItems", liststrings)
                                        Next
                                    End If
                                    If allholesNX6.Length > 0 Then
                                        For Each nx6holes As String In allholesNX6
                                            Dim splitstrings() As String = nx6holes.Split(":")
                                            Dim holestring As String = splitstrings(0) & ")"
                                            Dim myfeat As Features.BodyFeature = workPart.Features.FindObject(holestring)
                                            Dim holepack As Features.HolePackage = CType(myfeat, Features.HolePackage)
                                            Dim holeorigins() As Point3d = Nothing
                                            Dim point1 As Point = workPart.Points.CreatePoint(holepack.Location)
                                            Dim xcoord As Double = holedimension(refaxis1, refaxis2, point1)
                                            Dim ycoord As Double = holedimension(refaxis2, refaxis1, point1)
                                            Dim holedata1(2) As String
                                            holedata1(0) = holepack.JournalIdentifier
                                            holedata1(1) = "X Coodinate = " & xcoord.ToString
                                            holedata1(2) = "Y Coodinate = " & ycoord.ToString
                                            Dim liststrings() As String = listBoxInfoProperties.GetStrings("ListItems")
                                            Array.Resize(liststrings, liststrings.Length + 3)
                                            liststrings.SetValue(holedata1(0), liststrings.Length - 3)
                                            liststrings.SetValue(holedata1(2), liststrings.Length - 2)
                                            liststrings.SetValue(holedata1(1), liststrings.Length - 1)
                                            listBoxInfoProperties.SetStrings("ListItems", liststrings)
                                        Next
                                    End If
                                End If
                            End If
                        End If
                    Else
                        MsgBox(" Vectors not defined, please define the vectors for X and Y direction")
                    End If
                    deletePropertyList(listBoxInfoProperties)
                Catch ex As Exception
                    theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
                End Try
            End If

        Catch ex As Exception

            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        update_cb = 0
    End Function
    Private Function holedimension(ByRef refaxis1 As DatumAxis, ByRef refaxis2 As DatumAxis, ByRef refpoint1 As Point) As Double


        Dim nullNXObject As NXObject = Nothing

        Dim measureDistanceBuilder1 As MeasureDistanceBuilder
        measureDistanceBuilder1 = workPart.MeasureManager.CreateMeasureDistanceBuilder(nullNXObject)

        measureDistanceBuilder1.InfoWindow = False

        measureDistanceBuilder1.AnnotationMode = MeasureBuilder.AnnotationType.ShowDimension

        measureDistanceBuilder1.Mtype = MeasureDistanceBuilder.MeasureType.Minimum

        measureDistanceBuilder1.AnnotationMode = MeasureBuilder.AnnotationType.None

        measureDistanceBuilder1.InfoWindow = False

        Dim datumAxis1 As DatumAxis = refaxis1

        Dim direction1 As Direction
        direction1 = workPart.Directions.CreateDirection(refaxis1, Sense.Forward, SmartObject.UpdateOption.WithinModeling)

        measureDistanceBuilder1.ProjectionVector = direction1


        Dim point1 As Point = refpoint1

        Dim nullXform As Xform = Nothing

        Dim point2 As Point
        point2 = workPart.Points.CreatePoint(point1, nullXform, SmartObject.UpdateOption.AfterModeling)

        Dim nXObject1 As NXObject
        Dim xform1 As Xform
        xform1 = workPart.Xforms.CreateExtractXform(point1, SmartObject.UpdateOption.AfterModeling, False, nXObject1)

        measureDistanceBuilder1.Object1.Value = point2

        measureDistanceBuilder1.Object2.Value = refaxis2

        Dim nullUnit As Unit = Nothing

        Dim measureDistance1 As MeasureDistance
        measureDistance1 = workPart.MeasureManager.NewDistance(nullUnit, point2, refaxis2, direction1, MeasureManager.ProjectionType.Minimum)

        holeCoordinates = measureDistance1.Value

        measureDistanceBuilder1.Object2.Value = Nothing

        measureDistanceBuilder1.Destroy()

        workPart.FacetedBodies.DeleteTemporaryFacesAndEdges()

        Return holeCoordinates

    End Function

    Private Function datumaxiscreater(ByRef point1 As Point, ByRef direction1 As Direction) As DatumAxis

        Dim nullFeatures_Feature As Features.Feature = Nothing

        Dim datumAxisBuilder1 As Features.DatumAxisBuilder
        datumAxisBuilder1 = workPart.Features.CreateDatumAxisBuilder(nullFeatures_Feature)

        datumAxisBuilder1.Type = Features.DatumAxisBuilder.Types.ZcAxis

        datumAxisBuilder1.IsAssociative = True

        datumAxisBuilder1.ResizedEndDistance = 0.0

        datumAxisBuilder1.Type = Features.DatumAxisBuilder.Types.PointAndDir

        datumAxisBuilder1.ResizedEndDistance = 0.0

        datumAxisBuilder1.Point = point1

        datumAxisBuilder1.Vector = direction1

        datumAxisBuilder1.ResizedEndDistance = 50

        Dim nXObject1 As NXObject
        nXObject1 = datumAxisBuilder1.Commit()

        Dim datumaxisfeature1 As Features.DatumAxisFeature = CType(nXObject1, Features.DatumAxisFeature)
        Dim datumaxis1 As DatumAxis = datumaxisfeature1.DatumAxis

        datumAxisBuilder1.Destroy()

        workPart.FacetedBodies.DeleteTemporaryFacesAndEdges()

        datumaxiscreater = datumaxis1
    End Function

    Private Sub deletedatumaxis(ByRef objects1() As NXObject)

        Dim markId3 As Session.UndoMarkId
        markId3 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Delete")

        Dim nErrs1 As Integer
        nErrs1 = theSession.UpdateManager.AddToDeleteList(objects1)

        Dim notifyOnDelete2 As Boolean
        notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
        workPart.ModelingViews.WorkView.Regenerate()

        Dim nErrs2 As Integer
        nErrs2 = theSession.UpdateManager.DoUpdate(markId3)
        theSession.DeleteUndoMark(markId3, Nothing)

    End Sub

    Private Function editdatumaxis(ByRef datumaxis1 As DatumAxis, ByRef vect1 As Direction, ByRef origpoint As Point) As DatumAxis

        Dim allfeaturescol As Features.FeatureCollection = workPart.Features

        Dim markId1 As Session.UndoMarkId
        markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Redefine Feature")

        Dim datumAxisFeature1 As Features.DatumAxisFeature = CType(workPart.Features.FindObject(datumaxis1.JournalIdentifier), Features.DatumAxisFeature)

        datumAxisFeature1.MakeCurrentFeature()

        Dim datumAxisBuilder1 As Features.DatumAxisBuilder
        datumAxisBuilder1 = workPart.Features.CreateDatumAxisBuilder(datumAxisFeature1)

        datumAxisBuilder1.Point = origpoint

        datumAxisBuilder1.Vector = vect1

        Dim nXObject1 As NXObject
        nXObject1 = datumAxisBuilder1.Commit()

        datumAxisBuilder1.Destroy()

        Dim nErrs1 As Integer
        nErrs1 = theSession.UpdateManager.DoUpdate(markId1)

        Dim datumAxisFeature2 As Features.DatumAxisFeature = CType(nXObject1, Features.DatumAxisFeature)

        Dim allfeatures() As Features.Feature = allfeaturescol.ToArray()

        allfeatures(allfeatures.Length - 1).MakeCurrentFeature()

        theSession.DeleteUndoMark(markId1, Nothing)

        workPart.FacetedBodies.DeleteTemporaryFacesAndEdges()

        editdatumaxis = datumAxisFeature2.DatumAxis

    End Function
    Private Sub setEnablePropForBlock(ByVal blk As NXOpen.BlockStyler.UIBlock, ByVal value As Boolean)

        Dim blkProperties As PropertyList = blk.GetProperties()
        blkProperties.SetLogical("Enable", value)
        deletePropertyList(blkProperties)

    End Sub
    Private Sub deletePropertyList(ByRef prop As PropertyList)

        prop.Dispose()
        prop = Nothing

    End Sub

End Class

