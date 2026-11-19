'
'          Copyright (c) 2004 UGS PLM Solutions
'                  All rights reserved
'          Written by V.A.L.

Option Strict Off
Imports System
Imports NXOpen
Imports System.Windows.Forms
Imports Microsoft.VisualBasic

' This interface creates a shape on a sketch
'
' Classes inherit from this interface and implement the Execute function,
' that contains the core functionality that actually creates a specific shape.
Public Interface IShapeCreator

    ' Creates a shape on a sketch
    ' The name and right hand side of the dimensions in the sketch
    ' are specified by dimensionData.
    Sub Execute(ByVal dimensionData() As DimensionData)
End Interface

Module SketchShapeMain

    Sub Main()

        Dim theSession As Session = Session.GetSession()
        Dim theUFSession As NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
        Dim form As Form1 = Nothing

        Try
            If theSession.ActiveSketch Is Nothing Then
                MessageBox.Show("A sketch must be active in order to run this journal")
                Exit Sub
            End If

            Dim shapeCreators() As IShapeCreator = New IShapeCreator() { _
                New KeyholeShapeCreator(theSession, theUFSession), _
                New Shape2Creator(theSession, theUFSession), _
                New SlotShapeCreator(theSession, theUFSession), _
                New Shape4Creator(theSession, theUFSession)}

            Dim bitmapDirectory As String = System.IO.Path.Combine(System.IO.Path.GetDirectoryName(theSession.ExecutingJournal), "images")
            ' The shape creators are used to actually create the shape
            ' after the user has selected the shape and its dimensions
            form = New Form1(bitmapDirectory, shapeCreators)
            form.ShowDialog()
        Catch ex As Exception
            System.Windows.Forms.MessageBox.Show(ex.ToString())
        End Try

        form.Dispose()


    End Sub

End Module

Public Structure DimensionData

    ''''''''''''
    ' Fields used in the form UI and the IShapeCreator
    ''''''''''''

    ' name for the dimension
    Dim name As String
    ' the right hand side for the dimension
    Dim rhs As String

    ''''''''''''
    ' Fields used only in the form UI
    ''''''''''''

    ' the description for the dimension
    Dim description As String
    ' the upper left-hand corner of the dimension on the preview image
    Dim guiPickPoint As System.Drawing.Point
    ' the length and width of the dimension on the preview image
    Dim guiPickPointLengthHeight As System.Drawing.Point

    Public Sub New(ByVal name_ As String, ByVal rhs_ As String, _
    ByVal description_ As String, ByVal pickPointX As Integer, _
    ByVal pickPointY As Integer, ByVal pickPointLength As Integer, _
    ByVal pickPointHeight As Integer)
        name = name_
        rhs = rhs_
        description = description_
        guiPickPoint = New System.Drawing.Point(pickPointX, pickPointY)
        guiPickPointLengthHeight = New System.Drawing.Point(pickPointLength, pickPointHeight)
    End Sub

End Structure



' Form that asks the user to select a shape
Public Class Form1
    Inherits System.Windows.Forms.Form

    ''''''''''
    '      PUBLIC METHODS
    ''''''''''

    ' Sets the IShapeCreator that is run after the user presses
    ' "Create" on the final form.  The IShapeCreator actually
    ' creates the shape on the sketch
    Public Sub SetShapeCreators(ByVal creators() As IShapeCreator)
        m_shapeCreators = creators
    End Sub

#Region " Windows Form Designer generated code "

    Public Sub New(ByVal bitmapDirectory As String, ByVal creators() As IShapeCreator)
        MyBase.New()

        m_BitmapDirectory = bitmapDirectory
        m_shapeCreators = creators

        'This call is required by the Windows Form Designer.
        InitializeComponent()

        'Add any initialization after the InitializeComponent() call

    End Sub

    'Form overrides dispose to clean up the component list.
    Protected Overloads Overrides Sub Dispose(ByVal disposing As Boolean)
        If disposing Then
            If Not (components Is Nothing) Then
                components.Dispose()
            End If
        End If
        MyBase.Dispose(disposing)
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    Friend WithEvents m_SketchSelectComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents m_nextButton As System.Windows.Forms.Button
    Friend WithEvents m_PictureBox As System.Windows.Forms.PictureBox
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
        Dim resources As System.Resources.ResourceManager = New System.Resources.ResourceManager(GetType(Form1))
        Me.m_PictureBox = New System.Windows.Forms.PictureBox
        Me.m_SketchSelectComboBox = New System.Windows.Forms.ComboBox
        Me.Label1 = New System.Windows.Forms.Label
        Me.m_nextButton = New System.Windows.Forms.Button
        Me.SuspendLayout()
        '
        'm_PictureBox
        '
        Me.m_PictureBox.Image = Nothing
        Me.m_PictureBox.Location = New System.Drawing.Point(32, 16)
        Me.m_PictureBox.Name = "m_PictureBox"
        Me.m_PictureBox.Size = New System.Drawing.Size(328, 176)
        Me.m_PictureBox.TabIndex = 0
        Me.m_PictureBox.TabStop = False
        '
        'm_SketchSelectComboBox
        '
        Me.m_SketchSelectComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.m_SketchSelectComboBox.Items.AddRange(New Object() {"Keyhole", "Shape 2", "Slot", "Shape 4"})
        Me.m_SketchSelectComboBox.Location = New System.Drawing.Point(32, 272)
        Me.m_SketchSelectComboBox.Name = "m_SketchSelectComboBox"
        Me.m_SketchSelectComboBox.Size = New System.Drawing.Size(121, 21)
        Me.m_SketchSelectComboBox.TabIndex = 0
        Me.m_SketchSelectComboBox.SelectedIndex = 0
        '
        'Label1
        '
        Me.Label1.Location = New System.Drawing.Point(32, 240)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(120, 16)
        Me.Label1.TabIndex = 2
        Me.Label1.Text = "Pick shape:"
        '
        'm_nextButton
        '
        Me.m_nextButton.Location = New System.Drawing.Point(32, 304)
        Me.m_nextButton.Name = "m_nextButton"
        Me.m_nextButton.TabIndex = 1
        Me.m_nextButton.Text = "Next >"
        '
        'Form1
        '
        Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
        Me.ClientSize = New System.Drawing.Size(384, 343)
        Me.Controls.Add(Me.m_nextButton)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.m_SketchSelectComboBox)
        Me.Controls.Add(Me.m_PictureBox)
        Me.Name = "Form1"
        Me.Text = "Select shape to create"
        Me.ResumeLayout(False)

    End Sub

#End Region

    ''''''''''
    '      PRIVATE METHODS ADDED BY HAND
    ''''''''''

    Private Sub m_SketchSelectComboBox_SelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles m_SketchSelectComboBox.SelectedIndexChanged
        ' Set the preview image to the image for the shape
        Dim newImage As System.Drawing.Image
        Dim newImageName As String = "sk" & (m_SketchSelectComboBox.SelectedIndex + 1).ToString & ".jpg"
        newImage = New System.Drawing.Bitmap(System.IO.Path.Combine(m_BitmapDirectory, newImageName))
        m_PictureBox.Width = newImage.Width
        m_PictureBox.Height = newImage.Height
        m_PictureBox.Image = newImage

    End Sub

    Private Sub m_nextButton_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles m_nextButton.Click
        Me.Hide()

        ' For the dimensions for the selected shape, 
        ' specify the initial name, right hand side, description,
        ' and location of the dimension on the preview image
        Dim dimensionData As DimensionData()
        Select Case Me.m_SketchSelectComboBox.SelectedIndex
            Case 0
                dimensionData = New DimensionData() { _
                    New DimensionData("distance", "2.8", "distance between arc centers", 92, 54, 60, 7), _
                    New DimensionData("radius1", "1.6", "radius of bottom arc", 86, 127, 60, 7), _
                    New DimensionData("radius2", ".6", "radius of top arc", 83, 4, 60, 7) _
                    }
            Case 1
                dimensionData = New DimensionData() { _
                    New DimensionData("length", "8", "length", 134, 154, 40, 7), _
                    New DimensionData("height", "3.3", "height", 277, 88, 40, 7), _
                    New DimensionData("minorRadius", ".33", "minor radius", 26, 42, 60, 7), _
                    New DimensionData("majorRadius", "1.8", "major radius", 147, 9, 60, 7) _
                    }
            Case 2
                dimensionData = New DimensionData() { _
                    New DimensionData("angle", "60", "angle between arc centers", 90, 5, 40, 7), _
                    New DimensionData("majorRadius", "3.0", "major radius", 35, 119, 60, 7), _
                    New DimensionData("minorRadius", ".5", "major radius", 195, 59, 60, 7) _
                    }
            Case 3
                dimensionData = New DimensionData() { _
                    New DimensionData("length", "6.2", "length between circle centers", 128, 13, 40, 7), _
                    New DimensionData("barWidth", ".9", "width of the bar between the circles", 1, 62, 40, 7), _
                    New DimensionData("innerDiameter", "1.8", "inner diameter", 280, 45, 40, 7), _
                    New DimensionData("outerDiameter", "2.9", "outer diameter", 266, 15, 40, 7), _
                    New DimensionData("fillet", ".3", "fillet radius", 135, 90, 40, 7) _
                    }
            Case Else
                Throw New System.Exception("Not supported at this time")

        End Select


        ' Get the shapeCreator for the selected shape
        Dim shapeCreator As IShapeCreator = Nothing
        If Not Me.m_shapeCreators Is Nothing Then
            shapeCreator = m_shapeCreators(Me.m_SketchSelectComboBox.SelectedIndex)
        End If

        ' Show the second form
        Dim form2 As Form = New Form2(Me, Me.m_PictureBox.Image, dimensionData, shapeCreator)
        form2.ShowDialog()
    End Sub

    ''''''''''
    '      PRIVATE DATA
    ''''''''''

    Private m_BitmapDirectory As String

    Private m_shapeCreators() As IShapeCreator

End Class

' Form for user to input the dimension names and right hand side
Public Class Form2
    Inherits System.Windows.Forms.Form

    Private Class DimensionTextBox
        Inherits System.Windows.Forms.TextBox

        Private m_owner As Form2
        Private m_dimId As Integer

        Public Sub New(ByVal owner As Form2, ByVal dimId As Integer, _
        ByVal locationX As Integer, ByVal locationY As Integer)
            m_owner = owner
            m_dimId = dimId
            Me.Size = New System.Drawing.Size(104, 20)
            Me.Location = New System.Drawing.Point(locationX, locationY)
        End Sub

        Protected Overrides Sub OnGotFocus(ByVal e As EventArgs)
            MyBase.OnGotFocus(e)
            ' Highlight the dimension on the preview image
            m_owner.SetHighlightedDimension(m_dimId)

        End Sub

    End Class

    ' Highlights the specified dimension on the preview image
    '
    ' dimId - the location of the dimension data in the DimensionData array
    Public Sub SetHighlightedDimension(ByVal dimId As Integer)
        m_highlightedDimension = dimId
        Me.m_PictureBox.Invalidate()
        Me.m_statusTextBox.Text = Me.m_dimensionData(dimId).description
    End Sub


    Public Sub New(ByVal form1 As Form1, ByVal image As System.Drawing.Image, ByVal dimensionData As DimensionData(), ByVal shapeCreator As IShapeCreator)
        MyBase.New()
        m_form1 = form1
        m_dimensionData = dimensionData

        'This call is required by the Windows Form Designer.
        InitializeComponent()

        'Add any initialization after the InitializeComponent() call
        Me.m_PictureBox.Image = image
        Me.m_PictureBox.Size = image.Size
        m_shapeCreator = shapeCreator
        Dim highlightColor As System.Drawing.Color = System.Drawing.Color.FromArgb(128, 255, 0, 0)
        m_highlightBrush = New System.Drawing.SolidBrush(highlightColor)

    End Sub

    'Form overrides dispose to clean up the component list.
    Protected Overloads Overrides Sub Dispose(ByVal disposing As Boolean)
        If disposing Then
            If Not (components Is Nothing) Then
                components.Dispose()
            End If
        End If
        MyBase.Dispose(disposing)
    End Sub

    Private Sub InitializeComponent()
        Me.m_dimensionTextBoxes = New DimensionTextBox(2 * Me.m_dimensionData.Length) {}
        Dim ii As Integer
        For ii = 0 To Me.m_dimensionData.Length - 1
            m_dimensionTextBoxes(2 * ii) = New DimensionTextBox(Me, ii, 24, 256 + 32 * ii)
            m_dimensionTextBoxes(2 * ii).TabIndex = 2 * ii
            m_dimensionTextBoxes(2 * ii).Text = Me.m_dimensionData(ii).name
            m_dimensionTextBoxes(2 * ii + 1) = New DimensionTextBox(Me, ii, 160, 256 + 32 * ii)
            m_dimensionTextBoxes(2 * ii + 1).TabIndex = 2 * ii + 1
            m_dimensionTextBoxes(2 * ii + 1).Text = Me.m_dimensionData(ii).rhs

        Next
        Me.m_PictureBox = New System.Windows.Forms.PictureBox
        Me.Label1 = New System.Windows.Forms.Label
        Me.Label2 = New System.Windows.Forms.Label
        Me.m_prevButton = New System.Windows.Forms.Button
        Me.m_createButton = New System.Windows.Forms.Button
        Me.m_statusTextBox = New System.Windows.Forms.Label
        Me.SuspendLayout()
        '
        'm_PictureBox
        '
        Me.m_PictureBox.Location = New System.Drawing.Point(16, 16)
        Me.m_PictureBox.Name = "m_PictureBox"
        Me.m_PictureBox.Size = New System.Drawing.Size(160, 152)
        Me.m_PictureBox.TabStop = False
        '
        'Label1
        '
        Me.Label1.Location = New System.Drawing.Point(24, 224)
        Me.Label1.Name = "Label1"
        Me.Label1.Text = "Name"
        '
        'Label2
        '
        Me.Label2.Location = New System.Drawing.Point(160, 224)
        Me.Label2.Name = "Label2"
        Me.Label2.Text = "Value"
        '
        'm_prevButton
        '
        Me.m_prevButton.Location = New System.Drawing.Point(24, 256 + 32 * Me.m_dimensionData.Length + 8)
        Me.m_prevButton.Name = "m_prevButton"
        Me.m_prevButton.TabIndex = 2 * Me.m_dimensionData.Length + 3
        Me.m_prevButton.Text = "< Prev"
        '
        'm_createButton
        '
        Me.m_createButton.Location = New System.Drawing.Point(160, 256 + 32 * Me.m_dimensionData.Length + 8)
        Me.m_createButton.Name = "m_createButton"
        Me.m_createButton.TabIndex = 2 * Me.m_dimensionData.Length + 2
        Me.m_createButton.Text = "Create"
        '
        'm_statusTextBox
        '
        Me.m_statusTextBox.Location = New System.Drawing.Point(24, 256 + 32 * Me.m_dimensionData.Length + 8 + 48)
        Me.m_statusTextBox.Name = "m_statusTextBox"
        Me.m_statusTextBox.Size = New System.Drawing.Size(424, 16)
        Me.m_statusTextBox.TabIndex = 10
        '
        'Form2
        '
        Me.AutoScaleMode = False
        Me.ClientSize = New System.Drawing.Size(384, 341 + 32 * Me.m_dimensionData.Length)
        Me.Controls.Add(Me.m_statusTextBox)
        Me.Controls.Add(Me.m_createButton)
        Me.Controls.Add(Me.m_prevButton)

        For ii = 0 To Me.m_dimensionData.Length - 1
            Me.Controls.Add(Me.m_dimensionTextBoxes(2 * ii))
            Me.Controls.Add(Me.m_dimensionTextBoxes(2 * ii + 1))
        Next
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.m_PictureBox)
        Me.Name = "Form2"
        Me.Text = "Select values for dimensions"
        Me.ResumeLayout(False)

    End Sub

    Private Sub m_PictureBox_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles m_PictureBox.Paint
        ' highlight the dimension
        If m_highlightedDimension >= 0 Then
            Dim dimensionData As DimensionData = m_dimensionData(m_highlightedDimension)
            Dim x, y, length, height As Integer
            x = dimensionData.guiPickPoint.X
            y = dimensionData.guiPickPoint.Y
            length = dimensionData.guiPickPointLengthHeight.X
            height = dimensionData.guiPickPointLengthHeight.Y
            e.Graphics.FillRectangle(m_highlightBrush, x, y, length, height)
        End If

    End Sub

    Private Sub m_prevButton_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles m_prevButton.Click
        ' Go back to Form1
        m_returnToPrevForm = True
        Me.Close()
        m_form1.Show()
    End Sub


    Private Sub Form2_Closing(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles MyBase.Closing
        If Not m_returnToPrevForm Then
            m_form1.Close()
        End If
    End Sub

    Private Sub m_PictureBox_MouseDown(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles m_PictureBox.MouseDown
        ' If the user has clicked on a dimension, highlight the dimension
        ' and change focus to the name text box for the dimension
        Dim ii As Integer
        For ii = 0 To Me.m_dimensionData.Length - 1
            If m_dimensionData(ii).guiPickPoint.X <= e.X AndAlso e.X <= m_dimensionData(ii).guiPickPoint.X + m_dimensionData(ii).guiPickPointLengthHeight.X AndAlso _
            m_dimensionData(ii).guiPickPoint.Y <= e.Y AndAlso e.Y <= m_dimensionData(ii).guiPickPoint.Y + m_dimensionData(ii).guiPickPointLengthHeight.Y Then
                Me.SetHighlightedDimension(ii)
                Me.m_dimensionTextBoxes(2 * ii).SelectAll()
                Me.m_dimensionTextBoxes(2 * ii).Focus()
                Exit Sub
            End If
        Next
    End Sub


    Private Sub m_createButton_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles m_createButton.Click
        Me.Close()
        If Not Me.m_shapeCreator Is Nothing Then
            ' Fill in the DimensionData fields used by IShapeCreator with
            ' the values from the dimension text boxes
            Dim ii As Integer
            For ii = 0 To Me.m_dimensionData.Length - 1
                m_dimensionData(ii).name = Me.m_dimensionTextBoxes(2 * ii).Text
                m_dimensionData(ii).rhs = Me.m_dimensionTextBoxes(2 * ii + 1).Text
            Next

            ' Create the shape in the sketch
            Try
                m_shapeCreator.Execute(Me.m_dimensionData)
            Catch ex As Exception
                MessageBox.Show(ex.ToString())
            End Try

        End If
    End Sub

    '''''''''''
    '    PRIVATE DATA
    '''''''''''

    Private m_highlightedDimension As Integer = -1
    Private m_form1 As Form1
    Private m_dimensionData As DimensionData()
    Private m_shapeCreator As IShapeCreator
    Private m_returnToPrevForm As Boolean = False
    Private m_highlightBrush As System.Drawing.Brush


    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    Friend WithEvents m_PictureBox As System.Windows.Forms.PictureBox
    Private m_dimensionTextBoxes() As DimensionTextBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents m_prevButton As System.Windows.Forms.Button
    Friend WithEvents m_createButton As System.Windows.Forms.Button
    Friend WithEvents m_statusTextBox As System.Windows.Forms.Label

End Class



' This module contains the actual implementation code that creates
' shapes in the sketch
Module ShapeCreators

    ' Represents a 3-dimensional translation and rotation that can be
    ' applied to vectors and points
    Class Transform

        ''''''''''
        '    PUBLIC METHODS
        ''''''''''

        Public Sub New(ByVal translation As Point3d, ByVal rotationMatrix As Matrix3x3)
            m_matrix = rotationMatrix
            m_translation = translation
        End Sub

        ' Applies this transform to a vector
        '
        ' v_out = R * v_in
        '
        ' where R is the rotation matrix for this transform
        Public Function Apply(ByVal vector As Vector3d) As Vector3d
            Dim result As Vector3d
            result.x = m_matrix.xx * vector.x + m_matrix.yx * vector.y + m_matrix.zx * vector.z
            result.y = m_matrix.xy * vector.x + m_matrix.yy * vector.y + m_matrix.zy * vector.z
            result.z = m_matrix.xz * vector.x + m_matrix.yz * vector.y + m_matrix.zz * vector.z
            Return result
        End Function

        ' Applies this transform to a point
        '
        ' point_out = R * point_in + T
        '
        ' where R is the rotation matrix and T is the translation for this transform
        Public Function Apply(ByVal point As Point3d) As Point3d
            Dim result As Point3d
            result.x = m_translation.x + m_matrix.xx * point.x + m_matrix.yx * point.y + m_matrix.zx * point.z
            result.y = m_translation.y + m_matrix.xy * point.x + m_matrix.yy * point.y + m_matrix.zy * point.z
            result.z = m_translation.z + m_matrix.xz * point.x + m_matrix.yz * point.y + m_matrix.zz * point.z
            Return result
        End Function

        ''''''''''
        '    PRIVATE DATA
        ''''''''''

        Private m_matrix As Matrix3x3
        Private m_translation As Point3d

    End Class

    ' An abstract class that each shape creator inherits from
    Public MustInherit Class ShapeCreator

        Public Sub New(ByVal session As Session, ByVal ufSession As NXOpen.UF.UFSession)
            theSession = session
            theUFSession = ufSession
            activeSketch = theSession.ActiveSketch
            workPart = theSession.Parts.Work

            transform = New Transform(activeSketch.Origin, activeSketch.Orientation.Element)
        End Sub

        Protected theSession As Session
        Protected activeSketch As Sketch
        Protected workPart As Part
        Protected transform As transform
        Protected theUFSession As NXOpen.UF.UFSession

    End Class

    ' Creates a keyhole shape
    Public Class KeyholeShapeCreator
        Inherits ShapeCreator
        Implements IShapeCreator


        Public Sub New(ByVal session As Session, ByVal ufSession As NXOpen.UF.UFSession)
            MyBase.New(session, ufSession)
        End Sub

        Public Sub Execute(ByVal dimensionData() As DimensionData) Implements IShapeCreator.Execute

            theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create shape 1")

            ' NX 3.0.0.10
            ' Journal created by vlucas on Fri Mar 05 17:59:27 2004 Eastern Standard Time

            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId1 As Session.UndoMarkId
            ' session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId2 As Session.UndoMarkId
            ' session_UndoMarkId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId2, "Curve", Session.MarkVisibility.Visible)

            Dim point3d1 As Point3d = Transform.Apply(New Point3d(0, 3.14148980532975, 0))
            Dim point3d2 As Point3d = Transform.Apply(New Point3d(-0.0000000000000231657087176179, -3.05851019467025, 0))
            Dim line1 As Line
            line1 = workPart.Curves.CreateLine(point3d1, point3d2)

            activeSketch.AddGeometry(line1, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry1 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint1 As SketchGeometricConstraint
            sketchGeometricConstraint1 = activeSketch.CreateVerticalConstraint(sketch_ConstraintGeometry1)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId3 As Session.UndoMarkId
            ' session_UndoMarkId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId4 As Session.UndoMarkId
            ' session_UndoMarkId4 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId4, "Curve", Session.MarkVisibility.Visible)

            Dim point3d3 As Point3d = Transform.Apply(New Point3d(0.6, 2, 0))
            Dim point3d4 As Point3d = Transform.Apply(New Point3d(0.599999999999995, 0.6, 0))
            Dim line2 As Line
            line2 = workPart.Curves.CreateLine(point3d3, point3d4)

            activeSketch.AddGeometry(line2, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry2 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint2 As SketchGeometricConstraint
            sketchGeometricConstraint2 = activeSketch.CreateVerticalConstraint(sketch_ConstraintGeometry2)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Edit->Mirror...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId5 As Session.UndoMarkId
            ' session_UndoMarkId5 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Mirror Sketch")

            Dim objectArray1(0) As SmartObject
            objectArray1(0) = line2
            Dim objectArray2() As SmartObject
            objectArray2 = activeSketch.MirrorObjects(line1, objectArray1)

            ' ----------------------------------------------
            '   Menu: Insert->Profile...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId6 As Session.UndoMarkId
            ' session_UndoMarkId6 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId7 As Session.UndoMarkId
            ' session_UndoMarkId7 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId7, "Curve", Session.MarkVisibility.Visible)

            Dim point3d5 As Point3d = Transform.Apply(New Point3d(0.599999999999997, 2, 0))
            Dim point3d6 As Point3d = Transform.Apply(New Point3d(-0.00000000000000201409351674322, 2.60000000000001, 0))
            Dim point3d7 As Point3d = Transform.Apply(New Point3d(-0.600000000000021, 2, 0))
            Dim boolean1 As Boolean
            Dim arc1 As Arc
            arc1 = workPart.Curves.CreateArc(point3d5, point3d6, point3d7, False, boolean1)

            activeSketch.AddGeometry(arc1, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry3 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp1 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp1.type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp1.point.x = -0.600000000000021
            sketch_ConstraintGeometryHelp1.point.y = 2.42883864925048
            sketch_ConstraintGeometryHelp1.point.z = 0
            sketch_ConstraintGeometryHelp1.parameter = 0
            sketch_ConstraintGeometryHelp1.point = Transform.Apply(sketch_ConstraintGeometryHelp1.point)

            Dim sketch_ConstraintGeometry4 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(objectArray2(0), Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp2 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp2.type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp2.point.x = -0.600000000000021
            sketch_ConstraintGeometryHelp2.point.y = 2.42883864925048
            sketch_ConstraintGeometryHelp2.point.z = 0
            sketch_ConstraintGeometryHelp2.parameter = 0
            sketch_ConstraintGeometryHelp2.point = Transform.Apply(sketch_ConstraintGeometryHelp2.point)

            Dim sketchTangentConstraint1 As SketchTangentConstraint
            sketchTangentConstraint1 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry3, sketch_ConstraintGeometryHelp1, sketch_ConstraintGeometry4, sketch_ConstraintGeometryHelp2)

            Dim sketch_ConstraintGeometry5 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp3 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp3.type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp3.point.x = 0.599999999999997
            sketch_ConstraintGeometryHelp3.point.y = 2
            sketch_ConstraintGeometryHelp3.point.z = 0
            sketch_ConstraintGeometryHelp3.parameter = 0
            sketch_ConstraintGeometryHelp3.point = Transform.Apply(sketch_ConstraintGeometryHelp3.point)

            Dim sketch_ConstraintGeometry6 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp4 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp4.type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp4.point.x = 0.599999999999997
            sketch_ConstraintGeometryHelp4.point.y = 2
            sketch_ConstraintGeometryHelp4.point.z = 0
            sketch_ConstraintGeometryHelp4.parameter = 0
            sketch_ConstraintGeometryHelp4.point = Transform.Apply(sketch_ConstraintGeometryHelp4.point)

            Dim sketchTangentConstraint2 As SketchTangentConstraint
            sketchTangentConstraint2 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry5, sketch_ConstraintGeometryHelp3, sketch_ConstraintGeometry6, sketch_ConstraintGeometryHelp4)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId8 As Session.UndoMarkId
            ' session_UndoMarkId8 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' ' theSession.DeleteUndoMark(session_UndoMarkId8, "Curve")

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' Dim session_UndoMarkId9 As Session.UndoMarkId
            ' session_UndoMarkId9 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId9, "Curve", Session.MarkVisibility.Visible)

            Dim point3d8 As Point3d = Transform.Apply(New Point3d(-0.600000000000021, 0.6, 0))
            Dim point3d9 As Point3d = Transform.Apply(New Point3d(0, -2.38221734482709, 0))
            Dim point3d10 As Point3d = Transform.Apply(New Point3d(0.599999999999998, 0.6, 0))
            Dim boolean2 As Boolean
            Dim arc2 As Arc
            arc2 = workPart.Curves.CreateArc(point3d8, point3d9, point3d10, False, boolean2)

            activeSketch.AddGeometry(arc2, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId10 As Session.UndoMarkId
            ' session_UndoMarkId10 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' ' theSession.DeleteUndoMark(session_UndoMarkId10, "Curve")

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Profile...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Tools->Constraints->Show/Remove Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId11 As Session.UndoMarkId
            ' session_UndoMarkId11 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry7 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(objectArray2(0), Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry8 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint3 As SketchGeometricConstraint
            sketchGeometricConstraint3 = activeSketch.CreateEqualLengthConstraint(sketch_ConstraintGeometry7, sketch_ConstraintGeometry8)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Tools->Constraints->Show All Constraints
            ' ----------------------------------------------
            activeSketch.VisibilityOfConstraints = Sketch.ConstraintVisibility.All

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: View->Refresh
            ' ----------------------------------------------
            workPart.Views.Refresh()

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId12 As Session.UndoMarkId
            ' session_UndoMarkId12 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry9 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.ArcCenter, 0)
            Dim sketch_ConstraintGeometry10 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp5 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp5.type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp5.point.x = -0.0000000000000113930403739665
            sketch_ConstraintGeometryHelp5.point.y = -1.50851019467025
            sketch_ConstraintGeometryHelp5.point.z = 0
            sketch_ConstraintGeometryHelp5.parameter = 0
            sketch_ConstraintGeometryHelp5.point = Transform.Apply(sketch_ConstraintGeometryHelp5.point)

            Dim sketchHelpedGeometricConstraint1 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint1 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry9, sketch_ConstraintGeometry10, sketch_ConstraintGeometryHelp5)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Inferred...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId13 As Session.UndoMarkId
            ' session_UndoMarkId13 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Inferred...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Inferred...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId14 As Session.UndoMarkId
            ' session_UndoMarkId14 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId15 As Session.UndoMarkId
            ' session_UndoMarkId15 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry1 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry1.geometry = arc1
            sketch_DimensionGeometry1.AssocType = Sketch.AssocType.ArcCenter
            sketch_DimensionGeometry1.AssocValue = 0
            Dim sketch_DimensionGeometry2 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry2.Geometry = arc2
            sketch_DimensionGeometry2.AssocType = Sketch.AssocType.ArcCenter
            sketch_DimensionGeometry2.AssocValue = 0
            Dim point3d11 As Point3d = Transform.Apply(New Point3d(2.714399046297, 0.654872497183542, 0))
            Dim nullExpression As Expression = Nothing
            Dim sketchDimensionalConstraint1 As SketchDimensionalConstraint
            sketchDimensionalConstraint1 = activeSketch.CreateDimension(Sketch.ConstraintType.VerticalDim, sketch_DimensionGeometry1, sketch_DimensionGeometry2, point3d11, nullExpression)

            Dim dimension1 As Annotations.Dimension
            dimension1 = sketchDimensionalConstraint1.AssociatedDimension

            Dim expression1 As Expression
            expression1 = sketchDimensionalConstraint1.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId16 As Session.UndoMarkId
            ' session_UndoMarkId16 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression1.RightHandSide = "2.8"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Inferred...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId17 As Session.UndoMarkId
            ' session_UndoMarkId17 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId18 As Session.UndoMarkId
            ' session_UndoMarkId18 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry3 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry3.Geometry = arc2
            sketch_DimensionGeometry3.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry3.AssocValue = 65
            Dim point3d12 As Point3d = Transform.Apply(New Point3d(2.6005081772216, -2.19239922970142, 0))
            Dim sketchDimensionalConstraint2 As SketchDimensionalConstraint
            sketchDimensionalConstraint2 = activeSketch.CreateRadialDimension(sketch_DimensionGeometry3, point3d12, nullExpression)

            Dim dimension2 As Annotations.Dimension
            dimension2 = sketchDimensionalConstraint2.AssociatedDimension

            Dim expression2 As Expression
            expression2 = sketchDimensionalConstraint2.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId19 As Session.UndoMarkId
            ' session_UndoMarkId19 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression2.RightHandSide = "1.6"

            ' activeSketch.Update()

            ' Dim session_UndoMarkId20 As Session.UndoMarkId
            ' session_UndoMarkId20 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry4 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry4.Geometry = arc1
            sketch_DimensionGeometry4.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry4.AssocValue = 35
            Dim point3d13 As Point3d = Transform.Apply(New Point3d(1.57549035554301, 3.00861712474178, 0))
            Dim sketchDimensionalConstraint3 As SketchDimensionalConstraint
            sketchDimensionalConstraint3 = activeSketch.CreateRadialDimension(sketch_DimensionGeometry4, point3d13, nullExpression)

            Dim dimension3 As Annotations.Dimension
            dimension3 = sketchDimensionalConstraint3.AssociatedDimension

            Dim expression3 As Expression
            expression3 = sketchDimensionalConstraint3.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId21 As Session.UndoMarkId
            ' session_UndoMarkId21 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression3.RightHandSide = ".6"

            ' Change location of arc
            arc2.SetParameters(arc2.Radius, Transform.Apply(New Point3d(0, 0, 0)), arc2.StartAngle, arc2.EndAngle)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Tools->Journal->Stop
            ' ----------------------------------------------

            Dim undoMark As Session.UndoMarkId = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "change dimensions")
            Try
                expression1.SetName(dimensionData(0).name)
                expression2.SetName(dimensionData(1).name)
                expression3.SetName(dimensionData(2).name)
            Catch ex As Exception
                System.Windows.Forms.MessageBox.Show("Undoing change names of expressions because of the following errors:" & Chr(10) & ex.ToString())
                theSession.UndoToMark(undoMark, Nothing)
                activeSketch.Update()
                Exit Sub
            End Try
            theSession.DeleteUndoMark(undoMark, Nothing)
            undoMark = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "change dimensions")
            Try
                expression1.RightHandSide = dimensionData(0).rhs
                expression2.RightHandSide = dimensionData(1).rhs
                expression3.RightHandSide = dimensionData(2).rhs
            Catch ex As Exception
                System.Windows.Forms.MessageBox.Show("Undoing change values of expressions because of the following errors:" & Chr(10) & ex.ToString())
                theSession.UndoToMark(undoMark, Nothing)
                activeSketch.Update()
                Exit Sub
            End Try

            theSession.DeleteUndoMark(undoMark, Nothing)
            activeSketch.Update()

        End Sub

    End Class

    ' Creates shape 2
    Public Class Shape2Creator
        Inherits ShapeCreator
        Implements IShapeCreator


        Public Sub New(ByVal session As Session, ByVal ufSession As NXOpen.UF.UFSession)
            MyBase.New(session, ufSession)
        End Sub

        Public Sub Execute(ByVal dimensionData() As DimensionData) Implements IShapeCreator.Execute

            theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create shape 2")

            ' NX 3.0.0.10
            ' Journal created by vlucas on Fri Mar 05 19:56:32 2004 Eastern Standard Time

            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId1 As Session.UndoMarkId
            ' ' session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId2 As Session.UndoMarkId
            ' session_UndoMarkId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId2, "Curve", Session.MarkVisibility.Visible)

            Dim point3d1 As Point3d = Transform.Apply(New Point3d(0, 1, 0))
            Dim point3d2 As Point3d = Transform.Apply(New Point3d(0, -1, 0))
            Dim line1 As Line
            line1 = workPart.Curves.CreateLine(point3d1, point3d2)

            activeSketch.AddGeometry(line1, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            theUFSession.Sket.SetReferenceStatus(activeSketch.Tag, line1.Tag, NXOpen.UF.UFSket.ReferenceStatus.Reference)

            Dim sketch_ConstraintGeometry1 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint1 As SketchGeometricConstraint
            sketchGeometricConstraint1 = activeSketch.CreateVerticalConstraint(sketch_ConstraintGeometry1)

            ' ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' Dim session_UndoMarkId3 As Session.UndoMarkId
            ' session_UndoMarkId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId3, "Curve", Session.MarkVisibility.Visible)

            Dim point3d3 As Point3d = Transform.Apply(New Point3d(-1, 0, 0))
            Dim point3d4 As Point3d = Transform.Apply(New Point3d(1, 0, 0))
            Dim line2 As Line
            line2 = workPart.Curves.CreateLine(point3d3, point3d4)

            activeSketch.AddGeometry(line2, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            theUFSession.Sket.SetReferenceStatus(activeSketch.Tag, line2.Tag, NXOpen.UF.UFSket.ReferenceStatus.Reference)

            Dim sketch_ConstraintGeometry2 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint2 As SketchGeometricConstraint
            sketchGeometricConstraint2 = activeSketch.CreateHorizontalConstraint(sketch_ConstraintGeometry2)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Tools->Constraints->Show All Constraints
            ' ----------------------------------------------
            activeSketch.VisibilityOfConstraints = Sketch.ConstraintVisibility.All

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId4 As Session.UndoMarkId
            ' session_UndoMarkId4 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry3 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.EndVertex, 0)
            Dim sketchGeometricConstraint3 As SketchGeometricConstraint
            sketchGeometricConstraint3 = activeSketch.CreateFixedConstraint(sketch_ConstraintGeometry3)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId5 As Session.UndoMarkId
            ' session_UndoMarkId5 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry4 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.StartVertex, 0)
            Dim sketchGeometricConstraint4 As SketchGeometricConstraint
            sketchGeometricConstraint4 = activeSketch.CreateFixedConstraint(sketch_ConstraintGeometry4)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId6 As Session.UndoMarkId
            ' session_UndoMarkId6 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry5 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.StartVertex, 0)
            Dim sketchGeometricConstraint5 As SketchGeometricConstraint
            sketchGeometricConstraint5 = activeSketch.CreateFixedConstraint(sketch_ConstraintGeometry5)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId7 As Session.UndoMarkId
            ' session_UndoMarkId7 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry6 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.EndVertex, 0)
            Dim sketchGeometricConstraint6 As SketchGeometricConstraint
            sketchGeometricConstraint6 = activeSketch.CreateFixedConstraint(sketch_ConstraintGeometry6)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Profile...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId8 As Session.UndoMarkId
            ' session_UndoMarkId8 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId9 As Session.UndoMarkId
            ' session_UndoMarkId9 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId9, "Curve", Session.MarkVisibility.Visible)

            Dim point3d5 As Point3d = Transform.Apply(New Point3d(0.5, 1.3, 0))
            Dim point3d6 As Point3d = Transform.Apply(New Point3d(3.3007412794916, 0.224896151364085, 0))
            Dim line3 As Line
            line3 = workPart.Curves.CreateLine(point3d5, point3d6)

            activeSketch.AddGeometry(line3, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId10 As Session.UndoMarkId
            ' session_UndoMarkId10 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId10, "Curve", Session.MarkVisibility.Visible)

            Dim point3d7 As Point3d = Transform.Apply(New Point3d(3.14601150386288, -0.17818869510881, 0))
            Dim nXMatrix1 As NXMatrix = CType(workPart.FindObject("NXMATRIX WCS"), NXMatrix)
            Dim arc1 As Arc
            arc1 = workPart.Curves.CreateArc(point3d7, nXMatrix1, 0.431762315310393, 5.0789081233035, 7.48746249105567)

            activeSketch.AddGeometry(arc1, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry7 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp1 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp1.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp1.Point.X = 3.3007412794916
            sketch_ConstraintGeometryHelp1.Point.Y = 0.224896151364085
            sketch_ConstraintGeometryHelp1.Point.Z = 0
            sketch_ConstraintGeometryHelp1.Parameter = 0
            sketch_ConstraintGeometryHelp1.Point = Transform.Apply(sketch_ConstraintGeometryHelp1.Point)

            Dim sketch_ConstraintGeometry8 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp2 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp2.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp2.Point.X = 3.3007412794916
            sketch_ConstraintGeometryHelp2.Point.Y = 0.224896151364085
            sketch_ConstraintGeometryHelp2.Point.Z = 0
            sketch_ConstraintGeometryHelp2.Parameter = 0
            sketch_ConstraintGeometryHelp2.Point = Transform.Apply(sketch_ConstraintGeometryHelp2.Point)

            Dim sketchTangentConstraint1 As SketchTangentConstraint
            sketchTangentConstraint1 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry7, sketch_ConstraintGeometryHelp1, sketch_ConstraintGeometry8, sketch_ConstraintGeometryHelp2)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId11 As Session.UndoMarkId
            ' session_UndoMarkId11 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId11, "Curve", Session.MarkVisibility.Visible)

            Dim point3d8 As Point3d = Transform.Apply(New Point3d(3.3007412794916, -0.581273541581705, 0))
            Dim point3d9 As Point3d = Transform.Apply(New Point3d(0.5, -1.65637739021762, 0))
            Dim line4 As Line
            line4 = workPart.Curves.CreateLine(point3d8, point3d9)

            activeSketch.AddGeometry(line4, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry9 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line4, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp3 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp3.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp3.Point.X = 3.3007412794916
            sketch_ConstraintGeometryHelp3.Point.Y = -0.581273541581705
            sketch_ConstraintGeometryHelp3.Point.Z = 0
            sketch_ConstraintGeometryHelp3.Parameter = 0
            sketch_ConstraintGeometryHelp3.Point = Transform.Apply(sketch_ConstraintGeometryHelp3.Point)

            Dim sketch_ConstraintGeometry10 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp4 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp4.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp4.Point.X = 3.3007412794916
            sketch_ConstraintGeometryHelp4.Point.Y = -0.581273541581705
            sketch_ConstraintGeometryHelp4.Point.Z = 0
            sketch_ConstraintGeometryHelp4.Parameter = 0
            sketch_ConstraintGeometryHelp4.Point = Transform.Apply(sketch_ConstraintGeometryHelp4.Point)

            Dim sketchTangentConstraint2 As SketchTangentConstraint
            sketchTangentConstraint2 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry9, sketch_ConstraintGeometryHelp3, sketch_ConstraintGeometry10, sketch_ConstraintGeometryHelp4)

            Dim lineRefHoriz As Line
            lineRefHoriz = workPart.Curves.CreateLine(point3d6, point3d8)

            activeSketch.AddGeometry(lineRefHoriz)
            theUFSession.Sket.SetReferenceStatus(activeSketch.Tag, lineRefHoriz.Tag, NXOpen.UF.UFSket.ReferenceStatus.Reference)

            activeSketch.CreateParallelConstraint(New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0), New Sketch.ConstraintGeometry(lineRefHoriz, Sketch.ConstraintPointType.None, 0))
            'activeSketch.CreateMidpointConstraint( _
            '    New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.EndVertex, 0), _
            '    New Sketch.ConstraintGeometry(lineRefHoriz, Sketch.ConstraintPointType.None, 0))


            ' activeSketch.Update()

            ' Dim session_UndoMarkId12 As Session.UndoMarkId
            ' session_UndoMarkId12 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId12, "Curve", Session.MarkVisibility.Visible)

            Dim point3d10 As Point3d = Transform.Apply(New Point3d(-0.114527475229205, -0.0554785845441552, 0))
            Dim arc2 As Arc
            arc2 = workPart.Curves.CreateArc(point3d10, nXMatrix1, 1.71479474101664, 4.34586983746587, 5.0789081233035)

            activeSketch.AddGeometry(arc2, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry11 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp5 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp5.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp5.Point.X = 0.5
            sketch_ConstraintGeometryHelp5.Point.Y = -1.65637739021762
            sketch_ConstraintGeometryHelp5.Point.Z = 0
            sketch_ConstraintGeometryHelp5.Parameter = 0
            sketch_ConstraintGeometryHelp5.Point = Transform.Apply(sketch_ConstraintGeometryHelp5.Point)

            Dim sketch_ConstraintGeometry12 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line4, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp6 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp6.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp6.Point.X = 0.5
            sketch_ConstraintGeometryHelp6.Point.Y = -1.65637739021762
            sketch_ConstraintGeometryHelp6.Point.Z = 0
            sketch_ConstraintGeometryHelp6.Parameter = 0
            sketch_ConstraintGeometryHelp6.Point = Transform.Apply(sketch_ConstraintGeometryHelp6.Point)

            Dim sketchTangentConstraint3 As SketchTangentConstraint
            sketchTangentConstraint3 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry11, sketch_ConstraintGeometryHelp5, sketch_ConstraintGeometry12, sketch_ConstraintGeometryHelp6)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId13 As Session.UndoMarkId
            ' session_UndoMarkId13 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId13, "Curve", Session.MarkVisibility.Visible)

            Dim point3d11 As Point3d = Transform.Apply(New Point3d(-0.72905495045841, -1.65637739021762, 0))
            Dim point3d12 As Point3d = Transform.Apply(New Point3d(-3.91685997167487, -0.432693691867289, 0))
            Dim line5 As Line
            line5 = workPart.Curves.CreateLine(point3d11, point3d12)

            activeSketch.AddGeometry(line5, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry13 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line5, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp7 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp7.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp7.Point.X = -0.72905495045841
            sketch_ConstraintGeometryHelp7.Point.Y = -1.65637739021762
            sketch_ConstraintGeometryHelp7.Point.Z = 0
            sketch_ConstraintGeometryHelp7.Parameter = 0
            sketch_ConstraintGeometryHelp7.Point = Transform.Apply(sketch_ConstraintGeometryHelp7.Point)

            Dim sketch_ConstraintGeometry14 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp8 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp8.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp8.Point.X = -0.72905495045841
            sketch_ConstraintGeometryHelp8.Point.Y = -1.65637739021762
            sketch_ConstraintGeometryHelp8.Point.Z = 0
            sketch_ConstraintGeometryHelp8.Parameter = 0
            sketch_ConstraintGeometryHelp8.Point = Transform.Apply(sketch_ConstraintGeometryHelp8.Point)

            Dim sketchTangentConstraint4 As SketchTangentConstraint
            sketchTangentConstraint4 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry13, sketch_ConstraintGeometryHelp7, sketch_ConstraintGeometry14, sketch_ConstraintGeometryHelp8)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId14 As Session.UndoMarkId
            ' session_UndoMarkId14 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId14, "Curve", Session.MarkVisibility.Visible)

            Dim point3d13 As Point3d = Transform.Apply(New Point3d(-3.79498289817369, -0.115193060452482, 0))
            Dim arc3 As Arc
            arc3 = workPart.Curves.CreateArc(point3d13, nXMatrix1, 0.340089211816567, 1.5707963267949, 4.34586983746587)

            activeSketch.AddGeometry(arc3, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry15 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp9 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp9.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp9.Point.X = -3.91685997167487
            sketch_ConstraintGeometryHelp9.Point.Y = -0.432693691867289
            sketch_ConstraintGeometryHelp9.Point.Z = 0
            sketch_ConstraintGeometryHelp9.Parameter = 0
            sketch_ConstraintGeometryHelp9.Point = Transform.Apply(sketch_ConstraintGeometryHelp9.Point)

            Dim sketch_ConstraintGeometry16 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line5, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp10 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp10.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp10.Point.X = -3.91685997167487
            sketch_ConstraintGeometryHelp10.Point.Y = -0.432693691867289
            sketch_ConstraintGeometryHelp10.Point.Z = 0
            sketch_ConstraintGeometryHelp10.Parameter = 0
            sketch_ConstraintGeometryHelp10.Point = Transform.Apply(sketch_ConstraintGeometryHelp10.Point)

            Dim sketchTangentConstraint5 As SketchTangentConstraint
            sketchTangentConstraint5 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry15, sketch_ConstraintGeometryHelp9, sketch_ConstraintGeometry16, sketch_ConstraintGeometryHelp10)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId15 As Session.UndoMarkId
            ' session_UndoMarkId15 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' ----------------------------------------------
            '   Menu: Insert->Profile...
            ' ----------------------------------------------
            ' theSession.DeleteUndoMark(session_UndoMarkId15, "Curve")

            ' ----------------------------------------------
            '   Menu: Insert->Profile...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId16 As Session.UndoMarkId
            ' session_UndoMarkId16 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId17 As Session.UndoMarkId
            ' session_UndoMarkId17 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId17, "Curve", Session.MarkVisibility.Visible)

            Dim point3d14 As Point3d = Transform.Apply(New Point3d(0.5, 1.3, 0))
            Dim point3d15 As Point3d = Transform.Apply(New Point3d(-0.0160065359780682, 1.39563615855661, 0))
            Dim point3d16 As Point3d = Transform.Apply(New Point3d(-0.532013071956136, 1.3, 0))
            Dim boolean1 As Boolean
            Dim arc4 As Arc
            arc4 = workPart.Curves.CreateArc(point3d14, point3d15, point3d16, False, boolean1)

            activeSketch.AddGeometry(arc4, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry17 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc4, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp11 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp11.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp11.Point.X = 0.144703624215053
            sketch_ConstraintGeometryHelp11.Point.Y = 1.43638550044227
            sketch_ConstraintGeometryHelp11.Point.Z = 0
            sketch_ConstraintGeometryHelp11.Parameter = 0
            sketch_ConstraintGeometryHelp11.Point = Transform.Apply(sketch_ConstraintGeometryHelp11.Point)

            Dim sketch_ConstraintGeometry18 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp12 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp12.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp12.Point.X = 0.144703624215053
            sketch_ConstraintGeometryHelp12.Point.Y = 1.43638550044227
            sketch_ConstraintGeometryHelp12.Point.Z = 0
            sketch_ConstraintGeometryHelp12.Parameter = 0
            sketch_ConstraintGeometryHelp12.Point = Transform.Apply(sketch_ConstraintGeometryHelp12.Point)

            Dim sketchTangentConstraint6 As SketchTangentConstraint
            sketchTangentConstraint6 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry17, sketch_ConstraintGeometryHelp11, sketch_ConstraintGeometry18, sketch_ConstraintGeometryHelp12)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId18 As Session.UndoMarkId
            ' session_UndoMarkId18 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId18, "Curve", Session.MarkVisibility.Visible)

            Dim point3d17 As Point3d = Transform.Apply(New Point3d(-0.532013071956136, 1.3, 0))
            Dim point3d18 As Point3d = Transform.Apply(New Point3d(-3.79498289817369, 0.242316822460833, 0))
            Dim line6 As Line
            line6 = workPart.Curves.CreateLine(point3d17, point3d18)

            activeSketch.AddGeometry(line6, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry19 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line6, Sketch.ConstraintPointType.EndVertex, 0)
            Dim sketch_ConstraintGeometry20 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.StartVertex, 0)
            Dim sketchGeometricConstraint7 As SketchGeometricConstraint
            sketchGeometricConstraint7 = activeSketch.CreateCoincidentConstraint(sketch_ConstraintGeometry19, sketch_ConstraintGeometry20)

            Dim sketch_ConstraintGeometry21 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line6, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp13 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp13.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp13.Point.X = -3.89985022526211
            sketch_ConstraintGeometryHelp13.Point.Y = 0.208324351294315
            sketch_ConstraintGeometryHelp13.Point.Z = 0
            sketch_ConstraintGeometryHelp13.Parameter = 0
            sketch_ConstraintGeometryHelp13.Point = Transform.Apply(sketch_ConstraintGeometryHelp13.Point)

            Dim sketch_ConstraintGeometry22 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp14 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp14.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp14.Point.X = -3.89985022526211
            sketch_ConstraintGeometryHelp14.Point.Y = 0.208324351294315
            sketch_ConstraintGeometryHelp14.Point.Z = 0
            sketch_ConstraintGeometryHelp14.Parameter = 0
            sketch_ConstraintGeometryHelp14.Point = Transform.Apply(sketch_ConstraintGeometryHelp14.Point)

            Dim sketchTangentConstraint7 As SketchTangentConstraint
            sketchTangentConstraint7 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry21, sketch_ConstraintGeometryHelp13, sketch_ConstraintGeometry22, sketch_ConstraintGeometryHelp14)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId19 As Session.UndoMarkId
            ' session_UndoMarkId19 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' ----------------------------------------------
            '   Menu: Insert->Profile...
            ' ----------------------------------------------
            ' theSession.DeleteUndoMark(session_UndoMarkId19, "Curve")

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId20 As Session.UndoMarkId
            ' session_UndoMarkId20 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry23 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc4, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp15 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp15.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp15.Point.X = -0.110931429441157
            sketch_ConstraintGeometryHelp15.Point.Y = 1.39250376117527
            sketch_ConstraintGeometryHelp15.Point.Z = 0
            sketch_ConstraintGeometryHelp15.Parameter = 0
            sketch_ConstraintGeometryHelp15.Point = Transform.Apply(sketch_ConstraintGeometryHelp15.Point)

            Dim sketch_ConstraintGeometry24 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line6, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp16 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp16.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp16.Point.X = -1.44132910334875
            sketch_ConstraintGeometryHelp16.Point.Y = 1.00524757484946
            sketch_ConstraintGeometryHelp16.Point.Z = 0
            sketch_ConstraintGeometryHelp16.Parameter = 0
            sketch_ConstraintGeometryHelp16.Point = Transform.Apply(sketch_ConstraintGeometryHelp16.Point)

            Dim sketchTangentConstraint8 As SketchTangentConstraint
            sketchTangentConstraint8 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry23, sketch_ConstraintGeometryHelp15, sketch_ConstraintGeometry24, sketch_ConstraintGeometryHelp16)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId21 As Session.UndoMarkId
            ' session_UndoMarkId21 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry25 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.ArcCenter, 0)
            Dim sketch_ConstraintGeometry26 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp17 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp17.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp17.Point.X = -0.64
            sketch_ConstraintGeometryHelp17.Point.Y = 0
            sketch_ConstraintGeometryHelp17.Point.Z = 0
            sketch_ConstraintGeometryHelp17.Parameter = 0
            sketch_ConstraintGeometryHelp17.Point = Transform.Apply(sketch_ConstraintGeometryHelp17.Point)

            Dim sketchHelpedGeometricConstraint1 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint1 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry25, sketch_ConstraintGeometry26, sketch_ConstraintGeometryHelp17)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId22 As Session.UndoMarkId
            ' session_UndoMarkId22 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry27 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.ArcCenter, 0)
            Dim sketch_ConstraintGeometry28 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp18 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp18.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp18.Point.X = 0
            sketch_ConstraintGeometryHelp18.Point.Y = -0.44
            sketch_ConstraintGeometryHelp18.Point.Z = 0
            sketch_ConstraintGeometryHelp18.Parameter = 0
            sketch_ConstraintGeometryHelp18.Point = Transform.Apply(sketch_ConstraintGeometryHelp18.Point)

            Dim sketchHelpedGeometricConstraint2 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint2 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry27, sketch_ConstraintGeometry28, sketch_ConstraintGeometryHelp18)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId23 As Session.UndoMarkId
            ' session_UndoMarkId23 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry29 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.ArcCenter, 0)
            Dim sketch_ConstraintGeometry30 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp19 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp19.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp19.Point.X = 0.64
            sketch_ConstraintGeometryHelp19.Point.Y = 0
            sketch_ConstraintGeometryHelp19.Point.Z = 0
            sketch_ConstraintGeometryHelp19.Parameter = 0
            sketch_ConstraintGeometryHelp19.Point = Transform.Apply(sketch_ConstraintGeometryHelp19.Point)

            Dim sketchHelpedGeometricConstraint3 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint3 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry29, sketch_ConstraintGeometry30, sketch_ConstraintGeometryHelp19)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId24 As Session.UndoMarkId
            ' session_UndoMarkId24 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry31 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc4, Sketch.ConstraintPointType.ArcCenter, 0)
            Dim sketch_ConstraintGeometry32 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp20 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp20.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp20.Point.X = 0
            sketch_ConstraintGeometryHelp20.Point.Y = 0.36
            sketch_ConstraintGeometryHelp20.Point.Z = 0
            sketch_ConstraintGeometryHelp20.Parameter = 0
            sketch_ConstraintGeometryHelp20.Point = Transform.Apply(sketch_ConstraintGeometryHelp20.Point)

            Dim sketchHelpedGeometricConstraint4 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint4 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry31, sketch_ConstraintGeometry32, sketch_ConstraintGeometryHelp20)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId25 As Session.UndoMarkId
            ' session_UndoMarkId25 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry33 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line6, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry34 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line3, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint8 As SketchGeometricConstraint
            sketchGeometricConstraint8 = activeSketch.CreateEqualLengthConstraint(sketch_ConstraintGeometry33, sketch_ConstraintGeometry34)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId26 As Session.UndoMarkId
            ' session_UndoMarkId26 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry35 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line6, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry36 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line5, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint9 As SketchGeometricConstraint
            sketchGeometricConstraint9 = activeSketch.CreateEqualLengthConstraint(sketch_ConstraintGeometry35, sketch_ConstraintGeometry36)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId27 As Session.UndoMarkId
            ' session_UndoMarkId27 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry37 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line5, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry38 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line4, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint10 As SketchGeometricConstraint
            sketchGeometricConstraint10 = activeSketch.CreateEqualLengthConstraint(sketch_ConstraintGeometry37, sketch_ConstraintGeometry38)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId28 As Session.UndoMarkId
            ' session_UndoMarkId28 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry39 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc4, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry40 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint11 As SketchGeometricConstraint
            sketchGeometricConstraint11 = activeSketch.CreateEqualRadiusConstraint(sketch_ConstraintGeometry39, sketch_ConstraintGeometry40)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: View->Orient View to Sketch
            ' ----------------------------------------------
            ' Dim session_UndoMarkId29 As Session.UndoMarkId
            ' session_UndoMarkId29 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry41 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry42 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint12 As SketchGeometricConstraint
            sketchGeometricConstraint12 = activeSketch.CreateEqualRadiusConstraint(sketch_ConstraintGeometry41, sketch_ConstraintGeometry42)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Horizontal...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId30 As Session.UndoMarkId
            ' session_UndoMarkId30 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId31 As Session.UndoMarkId
            ' session_UndoMarkId31 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry1 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry1.Geometry = arc3
            sketch_DimensionGeometry1.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry1.AssocValue = 54
            Dim sketch_DimensionGeometry2 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry2.Geometry = arc1
            sketch_DimensionGeometry2.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry2.AssocValue = 52
            Dim point3d19 As Point3d = Transform.Apply(New Point3d(0.0882963265207153, -2.20110128255208, 0))
            Dim nullExpression As Expression = Nothing
            Dim sketchDimensionalConstraint1 As SketchDimensionalConstraint
            sketchDimensionalConstraint1 = activeSketch.CreateDimension(Sketch.ConstraintType.HorizontalDim, sketch_DimensionGeometry1, sketch_DimensionGeometry2, point3d19, nullExpression)

            Dim dimension1 As Annotations.Dimension
            dimension1 = sketchDimensionalConstraint1.AssociatedDimension

            Dim expression1 As Expression
            expression1 = sketchDimensionalConstraint1.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId32 As Session.UndoMarkId
            ' session_UndoMarkId32 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression1.RightHandSide = "8"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Vertical...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId33 As Session.UndoMarkId
            ' session_UndoMarkId33 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId34 As Session.UndoMarkId
            ' session_UndoMarkId34 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry3 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry3.Geometry = arc4
            sketch_DimensionGeometry3.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry3.AssocValue = 55
            Dim sketch_DimensionGeometry4 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry4.Geometry = arc2
            sketch_DimensionGeometry4.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry4.AssocValue = 41
            Dim point3d20 As Point3d = Transform.Apply(New Point3d(4.60402274000865, -0.0946032069864787, 0))
            Dim sketchDimensionalConstraint2 As SketchDimensionalConstraint
            sketchDimensionalConstraint2 = activeSketch.CreateDimension(Sketch.ConstraintType.VerticalDim, sketch_DimensionGeometry3, sketch_DimensionGeometry4, point3d20, nullExpression)

            Dim dimension2 As Annotations.Dimension
            dimension2 = sketchDimensionalConstraint2.AssociatedDimension

            Dim expression2 As Expression
            expression2 = sketchDimensionalConstraint2.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId35 As Session.UndoMarkId
            ' session_UndoMarkId35 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression2.RightHandSide = "3.3"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Radius...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId36 As Session.UndoMarkId
            ' session_UndoMarkId36 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId37 As Session.UndoMarkId
            ' session_UndoMarkId37 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry5 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry5.Geometry = arc3
            sketch_DimensionGeometry5.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry5.AssocValue = 50
            Dim point3d21 As Point3d = Transform.Apply(New Point3d(-3.88503836691141, 1.87314349833229, 0))
            Dim sketchDimensionalConstraint3 As SketchDimensionalConstraint
            sketchDimensionalConstraint3 = activeSketch.CreateRadialDimension(sketch_DimensionGeometry5, point3d21, nullExpression)

            Dim dimension3 As Annotations.Dimension
            dimension3 = sketchDimensionalConstraint3.AssociatedDimension

            Dim expression3 As Expression
            expression3 = sketchDimensionalConstraint3.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId38 As Session.UndoMarkId
            ' session_UndoMarkId38 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression3.RightHandSide = ".33"

            activeSketch.Update()

            ' Dim session_UndoMarkId39 As Session.UndoMarkId
            ' session_UndoMarkId39 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry6 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry6.Geometry = arc4
            sketch_DimensionGeometry6.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry6.AssocValue = 66
            Dim point3d22 As Point3d = Transform.Apply(New Point3d(1.50103755085214, 2.16325999975749, 0))
            Dim sketchDimensionalConstraint4 As SketchDimensionalConstraint
            sketchDimensionalConstraint4 = activeSketch.CreateRadialDimension(sketch_DimensionGeometry6, point3d22, nullExpression)

            Dim dimension4 As Annotations.Dimension
            dimension4 = sketchDimensionalConstraint4.AssociatedDimension

            Dim expression4 As Expression
            expression4 = sketchDimensionalConstraint4.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId40 As Session.UndoMarkId
            ' session_UndoMarkId40 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression4.RightHandSide = "1.8"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Radius...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Tools->Journal->Stop
            ' ----------------------------------------------
            Dim undoMark As Session.UndoMarkId = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "change dimensions")
            Try
                expression1.SetName(dimensionData(0).name)
                expression2.SetName(dimensionData(1).name)
                expression3.SetName(dimensionData(2).name)
                expression4.SetName(dimensionData(3).name)
            Catch ex As Exception
                System.Windows.Forms.MessageBox.Show("Undoing change names of expressions because of the following errors:" & Chr(10) & ex.ToString())
                theSession.UndoToMark(undoMark, Nothing)
                activeSketch.Update()
                Exit Sub
            End Try
            theSession.DeleteUndoMark(undoMark, Nothing)
            undoMark = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "change dimensions")
            Try
                expression1.RightHandSide = dimensionData(0).rhs
                expression2.RightHandSide = dimensionData(1).rhs
                expression3.RightHandSide = dimensionData(2).rhs
                expression4.RightHandSide = dimensionData(3).rhs
            Catch ex As Exception
                System.Windows.Forms.MessageBox.Show("Undoing change values of expressions because of the following errors:" & Chr(10) & ex.ToString())
                theSession.UndoToMark(undoMark, Nothing)
                activeSketch.Update()
                Exit Sub
            End Try

            theSession.DeleteUndoMark(undoMark, Nothing)
            activeSketch.Update()

        End Sub

    End Class

    ' Creates a slot shape
    Public Class SlotShapeCreator
        Inherits ShapeCreator
        Implements IShapeCreator


        Public Sub New(ByVal session As Session, ByVal ufSession As NXOpen.UF.UFSession)
            MyBase.New(session, ufSession)
        End Sub

        Public Sub Execute(ByVal dimensionData() As DimensionData) Implements IShapeCreator.Execute

            theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create shape 3")

            ' NX 3.0.0.10
            ' Journal created by vlucas on Fri Mar 05 20:35:17 2004 Eastern Standard Time

            ' ----------------------------------------------
            '   Menu: Insert->Point...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId1 As Session.UndoMarkId
            ' session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Point")

            Dim point3d2 As Point3d = Transform.Apply(New Point3d(0, 0, 0))
            Dim point2 As Point
            point2 = workPart.Points.CreatePoint(point3d2)

            point2.SetVisibility(SmartObject.VisibilityOption.Visible)

            activeSketch.AddGeometry(point2)

            ' ----------------------------------------------
            '   Dialog Begin Point Constructor
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId2 As Session.UndoMarkId
            ' session_UndoMarkId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId3 As Session.UndoMarkId
            ' session_UndoMarkId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId3, "Curve", Session.MarkVisibility.Visible)

            Dim point3d3 As Point3d = Transform.Apply(New Point3d(0, 0, 0))
            Dim point3d4 As Point3d = Transform.Apply(New Point3d(0.00000000000000351436002694883, 3, 0))
            Dim line1 As Line
            line1 = workPart.Curves.CreateLine(point3d3, point3d4)

            activeSketch.AddGeometry(line1, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry1 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint1 As SketchGeometricConstraint
            sketchGeometricConstraint1 = activeSketch.CreateVerticalConstraint(sketch_ConstraintGeometry1)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId4 As Session.UndoMarkId
            ' session_UndoMarkId4 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry2 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(point2, Sketch.ConstraintPointType.StartVertex, 0)
            Dim sketchGeometricConstraint2 As SketchGeometricConstraint
            sketchGeometricConstraint2 = activeSketch.CreateFixedConstraint(sketch_ConstraintGeometry2)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId5 As Session.UndoMarkId
            ' session_UndoMarkId5 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry3 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.EndVertex, 0)
            Dim sketchGeometricConstraint3 As SketchGeometricConstraint
            sketchGeometricConstraint3 = activeSketch.CreateFixedConstraint(sketch_ConstraintGeometry3)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Arc...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId6 As Session.UndoMarkId
            ' session_UndoMarkId6 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId7 As Session.UndoMarkId
            ' session_UndoMarkId7 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId7, "Curve", Session.MarkVisibility.Visible)

            Dim point3d5 As Point3d = Transform.Apply(New Point3d(0, 0, 0))
            Dim nXMatrix1 As NXMatrix = activeSketch.Orientation
            Dim arc1 As Arc
            arc1 = workPart.Curves.CreateArc(point3d5, nXMatrix1, 2.46431144076571, 1.03301882830311, 2.1766906814918)

            activeSketch.AddGeometry(arc1, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' Dim session_UndoMarkId8 As Session.UndoMarkId
            ' session_UndoMarkId8 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId8, "Curve", Session.MarkVisibility.Visible)

            Dim point3d6 As Point3d = Transform.Apply(New Point3d(0, 0, 0))
            Dim arc2 As Arc
            arc2 = workPart.Curves.CreateArc(point3d6, nXMatrix1, 3.51500911129525, 1.0226325442025, 2.18901947309927)

            activeSketch.AddGeometry(arc2, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Arc...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId9 As Session.UndoMarkId
            ' session_UndoMarkId9 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId10 As Session.UndoMarkId
            ' session_UndoMarkId10 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId10, "Curve", Session.MarkVisibility.Visible)

            Dim point3d7 As Point3d = Transform.Apply(New Point3d(0, 0, 0))
            Dim point3d8 As Point3d = Transform.Apply(New Point3d(1.83174481096266, 3, 0))
            Dim line2 As Line
            line2 = workPart.Curves.CreateLine(point3d7, point3d8)

            activeSketch.AddGeometry(line2, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' Dim session_UndoMarkId11 As Session.UndoMarkId
            ' session_UndoMarkId11 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId11, "Curve", Session.MarkVisibility.Visible)

            Dim point3d9 As Point3d = Transform.Apply(New Point3d(0, 0, 0))
            Dim point3d10 As Point3d = Transform.Apply(New Point3d(-2.03725745627117, 2.86441461896775, 0))
            Dim line3 As Line
            line3 = workPart.Curves.CreateLine(point3d9, point3d10)

            activeSketch.AddGeometry(line3, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId12 As Session.UndoMarkId
            ' session_UndoMarkId12 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry4 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.EndVertex, 0)
            Dim sketch_ConstraintGeometry5 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp1 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp1.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp1.Point.X = -0.957511004447451
            sketch_ConstraintGeometryHelp1.Point.Y = 1.34627487091484
            sketch_ConstraintGeometryHelp1.Point.Z = 0
            sketch_ConstraintGeometryHelp1.Parameter = 0
            sketch_ConstraintGeometryHelp1.Point = Transform.Apply(sketch_ConstraintGeometryHelp1.Point)

            Dim sketchHelpedGeometricConstraint1 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint1 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry4, sketch_ConstraintGeometry5, sketch_ConstraintGeometryHelp1)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId13 As Session.UndoMarkId
            ' session_UndoMarkId13 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry6 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.StartVertex, 0)
            Dim sketch_ConstraintGeometry7 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp2 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp2.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp2.Point.X = 0.879237509262078
            sketch_ConstraintGeometryHelp2.Point.Y = 1.44
            sketch_ConstraintGeometryHelp2.Point.Z = 0
            sketch_ConstraintGeometryHelp2.Parameter = 0
            sketch_ConstraintGeometryHelp2.Point = Transform.Apply(sketch_ConstraintGeometryHelp2.Point)

            Dim sketchHelpedGeometricConstraint2 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint2 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry6, sketch_ConstraintGeometry7, sketch_ConstraintGeometryHelp2)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId14 As Session.UndoMarkId
            ' session_UndoMarkId14 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId15 As Session.UndoMarkId
            ' session_UndoMarkId15 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId16 As Session.UndoMarkId
            ' session_UndoMarkId16 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId17 As Session.UndoMarkId
            ' session_UndoMarkId17 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId18 As Session.UndoMarkId
            ' session_UndoMarkId18 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId19 As Session.UndoMarkId
            ' session_UndoMarkId19 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId20 As Session.UndoMarkId
            ' session_UndoMarkId20 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry1 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry1.Geometry = line2
            sketch_DimensionGeometry1.AssocType = Sketch.AssocType.EndPoint
            sketch_DimensionGeometry1.AssocValue = 0
            Dim sketch_DimensionGeometry2 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry2.Geometry = line3
            sketch_DimensionGeometry2.AssocType = Sketch.AssocType.EndPoint
            sketch_DimensionGeometry2.AssocValue = 0
            Dim point3d11 As Point3d = Transform.Apply(New Point3d(0.123381774831683, 4.65528927345692, 0))
            Dim nullExpression As Expression = Nothing
            Dim sketchDimensionalConstraint1 As SketchDimensionalConstraint
            sketchDimensionalConstraint1 = activeSketch.CreateDimension(Sketch.ConstraintType.AngularDim, sketch_DimensionGeometry1, sketch_DimensionGeometry2, point3d11, nullExpression)

            Dim dimension1 As Annotations.Dimension
            dimension1 = sketchDimensionalConstraint1.AssociatedDimension

            Dim expression1 As Expression
            expression1 = sketchDimensionalConstraint1.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId21 As Session.UndoMarkId
            ' session_UndoMarkId21 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression1.RightHandSide = "60"

            ' activeSketch.Update()

            ' Dim session_UndoMarkId22 As Session.UndoMarkId
            ' session_UndoMarkId22 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry3 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry3.Geometry = line2
            sketch_DimensionGeometry3.AssocType = Sketch.AssocType.EndPoint
            sketch_DimensionGeometry3.AssocValue = 0
            Dim sketch_DimensionGeometry4 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry4.Geometry = line1
            sketch_DimensionGeometry4.AssocType = Sketch.AssocType.EndPoint
            sketch_DimensionGeometry4.AssocValue = 0
            Dim point3d12 As Point3d = Transform.Apply(New Point3d(1.99783566169762, 1.641926695837, 0))
            Dim sketchDimensionalConstraint2 As SketchDimensionalConstraint
            sketchDimensionalConstraint2 = activeSketch.CreateDimension(Sketch.ConstraintType.AngularDim, sketch_DimensionGeometry3, sketch_DimensionGeometry4, point3d12, nullExpression)

            Dim dimension2 As Annotations.Dimension
            dimension2 = sketchDimensionalConstraint2.AssociatedDimension

            Dim expression2 As Expression
            expression2 = sketchDimensionalConstraint2.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId23 As Session.UndoMarkId
            ' session_UndoMarkId23 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression2.RightHandSide = "30"

            activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Angular...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Arc...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId24 As Session.UndoMarkId
            ' session_UndoMarkId24 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId25 As Session.UndoMarkId
            ' session_UndoMarkId25 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' Dim session_UndoMarkId26 As Session.UndoMarkId
            ' session_UndoMarkId26 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId26, "Curve", Session.MarkVisibility.Visible)

            Dim point3d13 As Point3d = Transform.Apply(New Point3d(1.23199562459941, 2.13387901650873, 0))
            Dim point3d14 As Point3d = Transform.Apply(New Point3d(1.9383633651574, 2.3072617865998, 0))
            Dim point3d15 As Point3d = Transform.Apply(New Point3d(1.75750455564763, 3.04408718491545, 0))
            Dim boolean1 As Boolean
            Dim arc3 As Arc
            arc3 = workPart.Curves.CreateArc(point3d13, point3d14, point3d15, False, boolean1)

            activeSketch.AddGeometry(arc3, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry8 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp3 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp3.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp3.Point.X = 2.01660268976505
            sketch_ConstraintGeometryHelp3.Point.Y = 2.87899333867257
            sketch_ConstraintGeometryHelp3.Point.Z = 0
            sketch_ConstraintGeometryHelp3.Parameter = 0
            sketch_ConstraintGeometryHelp3.Point = Transform.Apply(sketch_ConstraintGeometryHelp3.Point)

            Dim sketch_ConstraintGeometry9 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp4 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp4.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp4.Point.X = 2.01660268976505
            sketch_ConstraintGeometryHelp4.Point.Y = 2.87899333867257
            sketch_ConstraintGeometryHelp4.Point.Z = 0
            sketch_ConstraintGeometryHelp4.Parameter = 0
            sketch_ConstraintGeometryHelp4.Point = Transform.Apply(sketch_ConstraintGeometryHelp4.Point)

            Dim sketchTangentConstraint1 As SketchTangentConstraint
            sketchTangentConstraint1 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry8, sketch_ConstraintGeometryHelp3, sketch_ConstraintGeometry9, sketch_ConstraintGeometryHelp4)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' Dim session_UndoMarkId27 As Session.UndoMarkId
            ' session_UndoMarkId27 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId27, "Curve", Session.MarkVisibility.Visible)

            Dim point3d16 As Point3d = Transform.Apply(New Point3d(-1.75750455564763, 3.04408718491545, 0))
            Dim point3d17 As Point3d = Transform.Apply(New Point3d(-1.78649850669228, 2.15189901493332, 0))
            Dim point3d18 As Point3d = Transform.Apply(New Point3d(-1.23199562459941, 2.13387901650873, 0))
            Dim boolean2 As Boolean
            Dim arc4 As Arc
            arc4 = workPart.Curves.CreateArc(point3d16, point3d17, point3d18, False, boolean2)

            activeSketch.AddGeometry(arc4, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry10 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc4, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp5 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp5.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp5.Point.X = -1.24886194426936
            sketch_ConstraintGeometryHelp5.Point.Y = 2.12405195800011
            sketch_ConstraintGeometryHelp5.Point.Z = 0
            sketch_ConstraintGeometryHelp5.Parameter = 0
            sketch_ConstraintGeometryHelp5.Point = Transform.Apply(sketch_ConstraintGeometryHelp5.Point)

            Dim sketch_ConstraintGeometry11 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp6 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp6.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp6.Point.X = -1.24886194426936
            sketch_ConstraintGeometryHelp6.Point.Y = 2.12405195800011
            sketch_ConstraintGeometryHelp6.Point.Z = 0
            sketch_ConstraintGeometryHelp6.Parameter = 0
            sketch_ConstraintGeometryHelp6.Point = Transform.Apply(sketch_ConstraintGeometryHelp6.Point)

            Dim sketchTangentConstraint2 As SketchTangentConstraint
            sketchTangentConstraint2 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry10, sketch_ConstraintGeometryHelp5, sketch_ConstraintGeometry11, sketch_ConstraintGeometryHelp6)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Arc...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId28 As Session.UndoMarkId
            ' session_UndoMarkId28 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry12 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp7 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp7.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp7.Point.X = 0.858878474316268
            sketch_ConstraintGeometryHelp7.Point.Y = 2.30945462013968
            sketch_ConstraintGeometryHelp7.Point.Z = 0
            sketch_ConstraintGeometryHelp7.Parameter = 0
            sketch_ConstraintGeometryHelp7.Point = Transform.Apply(sketch_ConstraintGeometryHelp7.Point)

            Dim sketch_ConstraintGeometry13 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp8 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp8.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp8.Point.X = 1.64663888077475
            sketch_ConstraintGeometryHelp8.Point.Y = 2.0859031548924
            sketch_ConstraintGeometryHelp8.Point.Z = 0
            sketch_ConstraintGeometryHelp8.Parameter = 0
            sketch_ConstraintGeometryHelp8.Point = Transform.Apply(sketch_ConstraintGeometryHelp8.Point)

            Dim sketchTangentConstraint3 As SketchTangentConstraint
            sketchTangentConstraint3 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry12, sketch_ConstraintGeometryHelp7, sketch_ConstraintGeometry13, sketch_ConstraintGeometryHelp8)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId29 As Session.UndoMarkId
            ' session_UndoMarkId29 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry14 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc4, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp9 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp9.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp9.Point.X = -2.01738022826255
            sketch_ConstraintGeometryHelp9.Point.Y = 2.64391374170799
            sketch_ConstraintGeometryHelp9.Point.Z = 0
            sketch_ConstraintGeometryHelp9.Parameter = 0
            sketch_ConstraintGeometryHelp9.Point = Transform.Apply(sketch_ConstraintGeometryHelp9.Point)

            Dim sketch_ConstraintGeometry15 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp10 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp10.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp10.Point.X = -1.39597845411294
            sketch_ConstraintGeometryHelp10.Point.Y = 3.22591587121256
            sketch_ConstraintGeometryHelp10.Point.Z = 0
            sketch_ConstraintGeometryHelp10.Parameter = 0
            sketch_ConstraintGeometryHelp10.Point = Transform.Apply(sketch_ConstraintGeometryHelp10.Point)

            Dim sketchTangentConstraint4 As SketchTangentConstraint
            sketchTangentConstraint4 = activeSketch.CreateTangentConstraint(sketch_ConstraintGeometry14, sketch_ConstraintGeometryHelp9, sketch_ConstraintGeometry15, sketch_ConstraintGeometryHelp10)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Parallel...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId30 As Session.UndoMarkId
            ' session_UndoMarkId30 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Parallel...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Inferred...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId31 As Session.UndoMarkId
            ' session_UndoMarkId31 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId32 As Session.UndoMarkId
            ' session_UndoMarkId32 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry5 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry5.Geometry = point2
            sketch_DimensionGeometry5.AssocType = Sketch.AssocType.StartPoint
            sketch_DimensionGeometry5.AssocValue = 0
            Dim sketch_DimensionGeometry6 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry6.Geometry = arc4
            sketch_DimensionGeometry6.AssocType = Sketch.AssocType.ArcCenter
            sketch_DimensionGeometry6.AssocValue = 0
            Dim point3d19 As Point3d = Transform.Apply(New Point3d(-2.7713444808347, -0.279981719810354, 0))
            Dim sketchDimensionalConstraint3 As SketchDimensionalConstraint
            sketchDimensionalConstraint3 = activeSketch.CreateDimension(Sketch.ConstraintType.ParallelDim, sketch_DimensionGeometry5, sketch_DimensionGeometry6, point3d19, nullExpression)

            Dim dimension3 As Annotations.Dimension
            dimension3 = sketchDimensionalConstraint3.AssociatedDimension

            Dim expression3 As Expression
            expression3 = sketchDimensionalConstraint3.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId33 As Session.UndoMarkId
            ' session_UndoMarkId33 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression3.RightHandSide = "3.0"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Radius...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId34 As Session.UndoMarkId
            ' session_UndoMarkId34 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId35 As Session.UndoMarkId
            ' session_UndoMarkId35 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry7 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry7.Geometry = arc3
            sketch_DimensionGeometry7.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry7.AssocValue = 67
            Dim point3d20 As Point3d = Transform.Apply(New Point3d(3.75365322661002, 2.78083538659098, 0))
            Dim sketchDimensionalConstraint4 As SketchDimensionalConstraint
            sketchDimensionalConstraint4 = activeSketch.CreateRadialDimension(sketch_DimensionGeometry7, point3d20, nullExpression)

            Dim dimension4 As Annotations.Dimension
            dimension4 = sketchDimensionalConstraint4.AssociatedDimension

            Dim expression4 As Expression
            expression4 = sketchDimensionalConstraint4.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId36 As Session.UndoMarkId
            ' session_UndoMarkId36 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression4.RightHandSide = ".5"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Tools->Constraints->Convert To/From Reference...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId37 As Session.UndoMarkId
            ' session_UndoMarkId37 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Convert To/From Reference")

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Tools->Journal->Stop
            ' ----------------------------------------------

            theUFSession.Sket.SetReferenceStatus(activeSketch.Tag, line1.Tag, NXOpen.UF.UFSket.ReferenceStatus.Reference)
            theUFSession.Sket.SetReferenceStatus(activeSketch.Tag, line2.Tag, NXOpen.UF.UFSket.ReferenceStatus.Reference)
            theUFSession.Sket.SetReferenceStatus(activeSketch.Tag, line3.Tag, NXOpen.UF.UFSket.ReferenceStatus.Reference)

            Dim undoMark As Session.UndoMarkId = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "change dimensions")
            Try
                expression1.SetName(dimensionData(0).name)
                expression3.SetName(dimensionData(1).name)
                expression4.SetName(dimensionData(2).name)
            Catch ex As Exception
                System.Windows.Forms.MessageBox.Show("Undoing change names of expressions because of the following errors:" & Chr(10) & ex.ToString())
                theSession.UndoToMark(undoMark, Nothing)
                activeSketch.Update()
                Exit Sub
            End Try
            theSession.DeleteUndoMark(undoMark, Nothing)
            undoMark = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "change dimensions")
            Try
                expression2.RightHandSide = expression1.Name & "/2"
                expression1.RightHandSide = dimensionData(0).rhs
                activeSketch.Update()
                expression3.RightHandSide = dimensionData(1).rhs
                activeSketch.Update()
                expression4.RightHandSide = dimensionData(2).rhs
            Catch ex As Exception
                System.Windows.Forms.MessageBox.Show("Undoing change values of expressions because of the following errors:" & Chr(10) & ex.ToString())
                theSession.UndoToMark(undoMark, Nothing)
                activeSketch.Update()
                Exit Sub
            End Try

            theSession.DeleteUndoMark(undoMark, Nothing)
            activeSketch.Update()


        End Sub

    End Class

    ' Creates shape 4
    Public Class Shape4Creator
        Inherits ShapeCreator
        Implements IShapeCreator


        Public Sub New(ByVal session As Session, ByVal ufSession As NXOpen.UF.UFSession)
            MyBase.New(session, ufSession)
        End Sub

        Public Sub Execute(ByVal dimensionData() As DimensionData) Implements IShapeCreator.Execute

            theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create shape 4")

            ' NX 3.0.0.10
            ' Journal created by vlucas on Fri Mar 05 20:57:10 2004 Eastern Standard Time

            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId1 As Session.UndoMarkId
            ' session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId2 As Session.UndoMarkId
            ' session_UndoMarkId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId2, "Curve", Session.MarkVisibility.Visible)

            Dim point3d1 As Point3d = Transform.Apply(New Point3d(-1, 0, 0))
            Dim point3d2 As Point3d = Transform.Apply(New Point3d(1, 0, 0))
            Dim line1 As Line
            line1 = workPart.Curves.CreateLine(point3d1, point3d2)

            activeSketch.AddGeometry(line1, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry1 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint1 As SketchGeometricConstraint
            sketchGeometricConstraint1 = activeSketch.CreateHorizontalConstraint(sketch_ConstraintGeometry1)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId3 As Session.UndoMarkId
            ' session_UndoMarkId3 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry2 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.StartVertex, 0)
            Dim sketchGeometricConstraint2 As SketchGeometricConstraint
            sketchGeometricConstraint2 = activeSketch.CreateFixedConstraint(sketch_ConstraintGeometry2)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId4 As Session.UndoMarkId
            ' session_UndoMarkId4 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry3 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.EndVertex, 0)
            Dim sketchGeometricConstraint3 As SketchGeometricConstraint
            sketchGeometricConstraint3 = activeSketch.CreateFixedConstraint(sketch_ConstraintGeometry3)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Line...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId5 As Session.UndoMarkId
            ' session_UndoMarkId5 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId6 As Session.UndoMarkId
            ' session_UndoMarkId6 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId6, "Curve", Session.MarkVisibility.Visible)

            Dim point3d3 As Point3d = Transform.Apply(New Point3d(-1.6, 0.4, 0))
            Dim point3d4 As Point3d = Transform.Apply(New Point3d(1.8, 0.4, 0))
            Dim line2 As Line
            line2 = workPart.Curves.CreateLine(point3d3, point3d4)

            activeSketch.AddGeometry(line2, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry4 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint4 As SketchGeometricConstraint
            sketchGeometricConstraint4 = activeSketch.CreateHorizontalConstraint(sketch_ConstraintGeometry4)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' Dim session_UndoMarkId7 As Session.UndoMarkId
            ' session_UndoMarkId7 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId7, "Curve", Session.MarkVisibility.Visible)

            Dim point3d5 As Point3d = Transform.Apply(New Point3d(-1.6, -0.50301800508301, 0))
            Dim point3d6 As Point3d = Transform.Apply(New Point3d(1.8, -0.50301800508301, 0))
            Dim line3 As Line
            line3 = workPart.Curves.CreateLine(point3d5, point3d6)

            activeSketch.AddGeometry(line3, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            Dim sketch_ConstraintGeometry5 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line3, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint5 As SketchGeometricConstraint
            sketchGeometricConstraint5 = activeSketch.CreateHorizontalConstraint(sketch_ConstraintGeometry5)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId8 As Session.UndoMarkId
            ' session_UndoMarkId8 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry6 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry7 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line3, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint6 As SketchGeometricConstraint
            sketchGeometricConstraint6 = activeSketch.CreateEqualLengthConstraint(sketch_ConstraintGeometry6, sketch_ConstraintGeometry7)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Arc...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId9 As Session.UndoMarkId
            ' session_UndoMarkId9 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId10 As Session.UndoMarkId
            ' session_UndoMarkId10 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId10, "Curve", Session.MarkVisibility.Visible)

            Dim point3d7 As Point3d = Transform.Apply(New Point3d(1.8, -0.50301800508301, 0))
            Dim point3d8 As Point3d = Transform.Apply(New Point3d(3.00506339132138, -1.33821771163593, 0))
            Dim point3d9 As Point3d = Transform.Apply(New Point3d(1.8, 0.4, 0))
            Dim boolean1 As Boolean
            Dim arc1 As Arc
            arc1 = workPart.Curves.CreateArc(point3d7, point3d8, point3d9, False, boolean1)

            activeSketch.AddGeometry(arc1, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' Dim session_UndoMarkId11 As Session.UndoMarkId
            ' session_UndoMarkId11 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' ----------------------------------------------
            '   Menu: Insert->Arc...
            ' ----------------------------------------------
            ' theSession.DeleteUndoMark(session_UndoMarkId11, "Curve")

            ' ----------------------------------------------
            '   Menu: Insert->Arc...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId12 As Session.UndoMarkId
            ' session_UndoMarkId12 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId13 As Session.UndoMarkId
            ' session_UndoMarkId13 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId13, "Curve", Session.MarkVisibility.Visible)

            Dim point3d10 As Point3d = Transform.Apply(New Point3d(-1.6, 0.4, 0))
            Dim point3d11 As Point3d = Transform.Apply(New Point3d(-4.40378027091541, 0.104399963319116, 0))
            Dim point3d12 As Point3d = Transform.Apply(New Point3d(-1.6, -0.503018005083011, 0))
            Dim boolean2 As Boolean
            Dim arc2 As Arc
            arc2 = workPart.Curves.CreateArc(point3d10, point3d11, point3d12, False, boolean2)

            activeSketch.AddGeometry(arc2, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Arc...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId14 As Session.UndoMarkId
            ' session_UndoMarkId14 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry8 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry9 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint7 As SketchGeometricConstraint
            sketchGeometricConstraint7 = activeSketch.CreateEqualRadiusConstraint(sketch_ConstraintGeometry8, sketch_ConstraintGeometry9)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId15 As Session.UndoMarkId
            ' session_UndoMarkId15 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry10 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.ArcCenter, 0)
            Dim sketch_ConstraintGeometry11 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp1 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp1.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp1.Point.X = 0.74
            sketch_ConstraintGeometryHelp1.Point.Y = 0
            sketch_ConstraintGeometryHelp1.Point.Z = 0
            sketch_ConstraintGeometryHelp1.Parameter = 0
            sketch_ConstraintGeometryHelp1.Point = Transform.Apply(sketch_ConstraintGeometryHelp1.Point)

            Dim sketchHelpedGeometricConstraint1 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint1 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry10, sketch_ConstraintGeometry11, sketch_ConstraintGeometryHelp1)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId16 As Session.UndoMarkId
            ' session_UndoMarkId16 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry12 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.ArcCenter, 0)
            Dim sketch_ConstraintGeometry13 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometryHelp2 As Sketch.ConstraintGeometryHelp
            sketch_ConstraintGeometryHelp2.Type = Sketch.ConstraintGeometryHelpType.Point
            sketch_ConstraintGeometryHelp2.Point.X = -0.44
            sketch_ConstraintGeometryHelp2.Point.Y = 0
            sketch_ConstraintGeometryHelp2.Point.Z = 0
            sketch_ConstraintGeometryHelp2.Parameter = 0
            sketch_ConstraintGeometryHelp2.Point = Transform.Apply(sketch_ConstraintGeometryHelp2.Point)

            Dim sketchHelpedGeometricConstraint2 As SketchHelpedGeometricConstraint
            sketchHelpedGeometricConstraint2 = activeSketch.CreatePointOnCurveConstraint(sketch_ConstraintGeometry12, sketch_ConstraintGeometry13, sketch_ConstraintGeometryHelp2)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Circle...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId17 As Session.UndoMarkId
            ' session_UndoMarkId17 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId18 As Session.UndoMarkId
            ' session_UndoMarkId18 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId18, "Curve", Session.MarkVisibility.Visible)

            Dim point3d13 As Point3d = Transform.Apply(New Point3d(3.16987036992849, 0, 0))
            Dim nXMatrix1 As NXMatrix = activeSketch.Orientation
            Dim arc3 As Arc
            arc3 = workPart.Curves.CreateArc(point3d13, nXMatrix1, 0.787716150459726, 0, 6.28318530717959)

            activeSketch.AddGeometry(arc3, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId19 As Session.UndoMarkId
            ' session_UndoMarkId19 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry14 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry15 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint8 As SketchGeometricConstraint
            sketchGeometricConstraint8 = activeSketch.CreateConcentricConstraint(sketch_ConstraintGeometry14, sketch_ConstraintGeometry15)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Circle...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId20 As Session.UndoMarkId
            ' session_UndoMarkId20 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId21 As Session.UndoMarkId
            ' session_UndoMarkId21 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Curve")

            ' theSession.SetUndoMarkVisibility(session_UndoMarkId21, "Curve", Session.MarkVisibility.Visible)

            Dim point3d14 As Point3d = Transform.Apply(New Point3d(-2.96987036992849, 2.77555756156289E-17, 0))
            Dim arc4 As Arc
            arc4 = workPart.Curves.CreateArc(point3d14, nXMatrix1, 0.901636046846906, 0, 6.28318530717959)

            activeSketch.AddGeometry(arc4, Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Dialog Begin Sketch Curves
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId22 As Session.UndoMarkId
            ' session_UndoMarkId22 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry16 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry17 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc4, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint9 As SketchGeometricConstraint
            sketchGeometricConstraint9 = activeSketch.CreateConcentricConstraint(sketch_ConstraintGeometry16, sketch_ConstraintGeometry17)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId24 As Session.UndoMarkId
            ' session_UndoMarkId24 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry20 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc4, Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry21 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arc3, Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint11 As SketchGeometricConstraint
            sketchGeometricConstraint11 = activeSketch.CreateEqualRadiusConstraint(sketch_ConstraintGeometry20, sketch_ConstraintGeometry21)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Fillet...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId25 As Session.UndoMarkId
            ' session_UndoMarkId25 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Profile short list")

            ' Dim session_UndoMarkId26 As Session.UndoMarkId
            ' session_UndoMarkId26 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Sketch Fillet")

            Dim nullCurve As Curve = Nothing
            Dim point3d15 As Point3d = Transform.Apply(New Point3d(-1.39791107668335, -0.451509002541505, 0))
            Dim point3d16 As Point3d = Transform.Apply(New Point3d(-1.66857128553343, -0.622114059266163, 0))
            Dim arcArray1() As Arc
            Dim sketchConstraintArray1() As SketchConstraint
            arcArray1 = activeSketch.Fillet(line3, arc2, point3d15, point3d16, 0.3, Sketch.TrimInputOption.True, Sketch.CreateDimensionOption.False, Sketch.AlternateSolutionOption.False, sketchConstraintArray1)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId27 As Session.UndoMarkId
            ' session_UndoMarkId27 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Sketch Fillet")

            Dim point3d18 As Point3d = Transform.Apply(New Point3d(-1.39791107668335, 0.451509002541505, 0))
            Dim point3d19 As Point3d = Transform.Apply(New Point3d(-1.66857128553343, 0.622114059266163, 0))
            Dim arcArray2() As Arc
            Dim sketchConstraintArray2() As SketchConstraint
            arcArray2 = activeSketch.Fillet(line2, arc2, point3d18, point3d19, 0.3, Sketch.TrimInputOption.True, Sketch.CreateDimensionOption.False, Sketch.AlternateSolutionOption.False, sketchConstraintArray2)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId29 As Session.UndoMarkId
            ' session_UndoMarkId29 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Sketch Fillet")

            Dim point3d24 As Point3d = Transform.Apply(New Point3d(1.29076318285452, 0.451509002541505, 0))
            Dim point3d25 As Point3d = Transform.Apply(New Point3d(2.04090704553618, 0.897689825029289, 0))
            Dim arcArray4() As Arc
            Dim sketchConstraintArray4() As SketchConstraint
            arcArray4 = activeSketch.Fillet(line2, arc1, point3d24, point3d25, 0.3, Sketch.TrimInputOption.True, Sketch.CreateDimensionOption.False, Sketch.AlternateSolutionOption.False, sketchConstraintArray4)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId30 As Session.UndoMarkId
            ' session_UndoMarkId30 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Sketch Fillet")

            Dim point3d27 As Point3d = Transform.Apply(New Point3d(1.46159948646762, -0.451509002541505, 0))
            Dim point3d28 As Point3d = Transform.Apply(New Point3d(1.91929943839091, -0.718663728719681, 0))
            Dim arcArray5() As Arc
            Dim sketchConstraintArray5() As SketchConstraint
            arcArray5 = activeSketch.Fillet(line3, arc1, point3d27, point3d28, 0.3, Sketch.TrimInputOption.True, Sketch.CreateDimensionOption.False, Sketch.AlternateSolutionOption.False, sketchConstraintArray5)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Fillet...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Radius...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId31 As Session.UndoMarkId
            ' session_UndoMarkId31 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId32 As Session.UndoMarkId
            ' session_UndoMarkId32 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry1 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry1.Geometry = arcArray1(0)
            sketch_DimensionGeometry1.AssocType = Sketch.AssocType.StartPoint
            sketch_DimensionGeometry1.AssocValue = 0
            Dim point3d30 As Point3d = Transform.Apply(New Point3d(-0.32269079571363, -1.1863632195354, 0))
            Dim nullExpression As Expression = Nothing
            Dim sketchDimensionalConstraint1 As SketchDimensionalConstraint
            sketchDimensionalConstraint1 = activeSketch.CreateRadialDimension(sketch_DimensionGeometry1, point3d30, nullExpression)

            Dim dimension1 As Annotations.Dimension
            dimension1 = sketchDimensionalConstraint1.AssociatedDimension

            Dim expression1 As Expression
            expression1 = sketchDimensionalConstraint1.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId33 As Session.UndoMarkId
            ' session_UndoMarkId33 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId34 As Session.UndoMarkId
            ' session_UndoMarkId34 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry22 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arcArray1(0), Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry23 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arcArray2(0), Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint12 As SketchGeometricConstraint
            sketchGeometricConstraint12 = activeSketch.CreateEqualRadiusConstraint(sketch_ConstraintGeometry22, sketch_ConstraintGeometry23)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId35 As Session.UndoMarkId
            ' session_UndoMarkId35 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry24 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arcArray1(0), Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry25 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arcArray4(0), Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint13 As SketchGeometricConstraint
            sketchGeometricConstraint13 = activeSketch.CreateEqualRadiusConstraint(sketch_ConstraintGeometry24, sketch_ConstraintGeometry25)

            ' activeSketch.Update()

            ' Dim session_UndoMarkId36 As Session.UndoMarkId
            ' session_UndoMarkId36 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Geometric Constraints")

            Dim sketch_ConstraintGeometry26 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arcArray1(0), Sketch.ConstraintPointType.None, 0)
            Dim sketch_ConstraintGeometry27 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry(arcArray5(0), Sketch.ConstraintPointType.None, 0)
            Dim sketchGeometricConstraint14 As SketchGeometricConstraint
            sketchGeometricConstraint14 = activeSketch.CreateEqualRadiusConstraint(sketch_ConstraintGeometry26, sketch_ConstraintGeometry27)

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Inferred...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId37 As Session.UndoMarkId
            ' session_UndoMarkId37 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId38 As Session.UndoMarkId
            ' session_UndoMarkId38 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry2 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry2.Geometry = line2
            sketch_DimensionGeometry2.AssocType = Sketch.AssocType.StartPoint
            sketch_DimensionGeometry2.AssocValue = 0
            Dim sketch_DimensionGeometry3 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry3.Geometry = line3
            sketch_DimensionGeometry3.AssocType = Sketch.AssocType.StartPoint
            sketch_DimensionGeometry3.AssocValue = 0
            Dim point3d31 As Point3d = Transform.Apply(New Point3d(-5.71062921979257, 0.000350333854488392, 0))
            Dim sketchDimensionalConstraint2 As SketchDimensionalConstraint
            sketchDimensionalConstraint2 = activeSketch.CreateDimension(Sketch.ConstraintType.PerpendicularDim, sketch_DimensionGeometry2, sketch_DimensionGeometry3, point3d31, nullExpression)

            Dim dimension2 As Annotations.Dimension
            dimension2 = sketchDimensionalConstraint2.AssociatedDimension

            Dim expression2 As Expression
            expression2 = sketchDimensionalConstraint2.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId39 As Session.UndoMarkId
            ' session_UndoMarkId39 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression2.RightHandSide = ".9"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Diameter...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId40 As Session.UndoMarkId
            ' session_UndoMarkId40 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId41 As Session.UndoMarkId
            ' session_UndoMarkId41 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry4 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry4.Geometry = arc3
            sketch_DimensionGeometry4.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry4.AssocValue = 14
            Dim point3d32 As Point3d = Transform.Apply(New Point3d(5.86856611843905, 0.681035869754707, 0))
            Dim sketchDimensionalConstraint3 As SketchDimensionalConstraint
            sketchDimensionalConstraint3 = activeSketch.CreateDiameterDimension(sketch_DimensionGeometry4, point3d32, nullExpression)

            Dim dimension3 As Annotations.Dimension
            dimension3 = sketchDimensionalConstraint3.AssociatedDimension

            Dim expression3 As Expression
            expression3 = sketchDimensionalConstraint3.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId42 As Session.UndoMarkId
            ' session_UndoMarkId42 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression3.RightHandSide = "1.8"

            ' activeSketch.Update()

            ' Dim session_UndoMarkId43 As Session.UndoMarkId
            ' session_UndoMarkId43 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry5 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry5.Geometry = arc1
            sketch_DimensionGeometry5.AssocType = Sketch.AssocType.Tangency
            sketch_DimensionGeometry5.AssocValue = 69
            Dim point3d33 As Point3d = Transform.Apply(New Point3d(5.60257273337908, 2.50622849325758, 0))
            Dim sketchDimensionalConstraint4 As SketchDimensionalConstraint
            sketchDimensionalConstraint4 = activeSketch.CreateDiameterDimension(sketch_DimensionGeometry5, point3d33, nullExpression)

            Dim dimension4 As Annotations.Dimension
            dimension4 = sketchDimensionalConstraint4.AssociatedDimension

            Dim expression4 As Expression
            expression4 = sketchDimensionalConstraint4.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId44 As Session.UndoMarkId
            ' session_UndoMarkId44 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression4.RightHandSide = "2.9"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Constraints...
            ' ----------------------------------------------
            ' ----------------------------------------------
            '   Menu: Insert->Dimensions->Inferred...
            ' ----------------------------------------------
            ' Dim session_UndoMarkId45 As Session.UndoMarkId
            ' session_UndoMarkId45 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Model from Sketcher")

            ' Dim session_UndoMarkId46 As Session.UndoMarkId
            ' session_UndoMarkId46 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Sketch Dimension")

            Dim sketch_DimensionGeometry6 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry6.Geometry = arc2
            sketch_DimensionGeometry6.AssocType = Sketch.AssocType.ArcCenter
            sketch_DimensionGeometry6.AssocValue = 0
            Dim sketch_DimensionGeometry7 As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
            sketch_DimensionGeometry7.Geometry = arc1
            sketch_DimensionGeometry7.AssocType = Sketch.AssocType.ArcCenter
            sketch_DimensionGeometry7.AssocValue = 0
            Dim point3d34 As Point3d = Transform.Apply(New Point3d(0.00281935155391224, 2.01373233216255, 0))
            Dim sketchDimensionalConstraint5 As SketchDimensionalConstraint
            sketchDimensionalConstraint5 = activeSketch.CreateDimension(Sketch.ConstraintType.HorizontalDim, sketch_DimensionGeometry6, sketch_DimensionGeometry7, point3d34, nullExpression)

            Dim dimension5 As Annotations.Dimension
            dimension5 = sketchDimensionalConstraint5.AssociatedDimension

            Dim expression5 As Expression
            expression5 = sketchDimensionalConstraint5.AssociatedExpression

            ' activeSketch.Update()

            ' Dim session_UndoMarkId47 As Session.UndoMarkId
            ' session_UndoMarkId47 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Edit Sketch Dimension")

            expression5.RightHandSide = "6.2"

            ' activeSketch.Update()

            ' ----------------------------------------------
            '   Menu: Tools->Journal->Stop
            ' ----------------------------------------------

            sketchGeometricConstraint6 = activeSketch.CreateEqualLengthConstraint(sketch_ConstraintGeometry6, sketch_ConstraintGeometry7)
            activeSketch.DeleteObjects(New NXObject() {sketchGeometricConstraint2, sketchGeometricConstraint3})
            activeSketch.CreateFixedConstraint(New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.None, 0))
            activeSketch.CreateCoincidentConstraint( _
                New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.StartVertex, 0), _
                New Sketch.ConstraintGeometry(arc2, Sketch.ConstraintPointType.ArcCenter, 0))
            activeSketch.CreateCoincidentConstraint( _
                New Sketch.ConstraintGeometry(line1, Sketch.ConstraintPointType.EndVertex, 0), _
                New Sketch.ConstraintGeometry(arc1, Sketch.ConstraintPointType.ArcCenter, 0))
            theUFSession.Sket.SetReferenceStatus(activeSketch.Tag, line1.Tag, NXOpen.UF.UFSket.ReferenceStatus.Reference)

            Dim undoMark As Session.UndoMarkId = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "change dimensions")
            Try
                expression1.SetName(dimensionData(4).name)
                expression2.SetName(dimensionData(1).name)
                expression3.SetName(dimensionData(2).name)
                expression4.SetName(dimensionData(3).name)
                expression5.SetName(dimensionData(0).name)
            Catch ex As Exception
                System.Windows.Forms.MessageBox.Show("Undoing change names of expressions because of the following errors:" & Chr(10) & ex.ToString())
                theSession.UndoToMark(undoMark, Nothing)
                activeSketch.Update()
                Exit Sub
            End Try
            theSession.DeleteUndoMark(undoMark, Nothing)
            undoMark = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "change dimensions")
            Try
                expression1.RightHandSide = dimensionData(4).rhs
                expression2.RightHandSide = dimensionData(1).rhs
                expression3.RightHandSide = dimensionData(2).rhs
                expression4.RightHandSide = dimensionData(3).rhs
                expression5.RightHandSide = dimensionData(0).rhs
            Catch ex As Exception
                System.Windows.Forms.MessageBox.Show("Undoing change values of expressions because of the following errors:" & Chr(10) & ex.ToString())
                theSession.UndoToMark(undoMark, Nothing)
                activeSketch.Update()
                Exit Sub
            End Try

            theSession.DeleteUndoMark(undoMark, Nothing)
            activeSketch.Update()
        End Sub

    End Class

End Module

