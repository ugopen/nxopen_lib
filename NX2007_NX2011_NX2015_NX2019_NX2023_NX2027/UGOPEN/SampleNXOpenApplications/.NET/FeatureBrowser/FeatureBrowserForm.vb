Imports NXOpen

Public Class FeatureBrowserForm
    Inherits System.Windows.Forms.Form

    Private theSession As Session
    Private theUI As UI
    Private featureUpdateUndoMark As Integer = 0
    Private Shared mainForm As Form

    ''' <summary>
    ''' The main entry point for the application.
    ''' </summary>
    ' <STAThread()>
    Public Shared Sub Main()

        Try
            mainForm = New FeatureBrowserForm
            mainForm.Show()
        Catch ex As System.Exception
            System.Diagnostics.Trace.WriteLine("Error in Feature Browser: " & ex.Message)
            MessageBox.Show("Exception: " & ex.Message)
        End Try

    End Sub

#Region " Windows Form Designer generated code "

    Public Sub New()
        MyBase.New()

        'This call is required by the Windows Form Designer.
        InitializeComponent()

        'Add any initialization after the InitializeComponent() call
        Me.theSession = Session.GetSession()
        Me.theUI = UI.GetUI()
        NXOpenUI.FormUtilities.SetApplicationIcon(Me)
        NXOpenUI.FormUtilities.ReparentForm(Me)

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

    Friend WithEvents TreeViewPanel As System.Windows.Forms.Panel
    Friend WithEvents Splitter1 As System.Windows.Forms.Splitter
    Friend WithEvents ListViewPanel As System.Windows.Forms.Panel
    Friend WithEvents Splitter2 As System.Windows.Forms.Splitter
    Friend WithEvents PropertyPanel As System.Windows.Forms.Panel
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents FeatureTreeView As System.Windows.Forms.TreeView
    Friend WithEvents ExpressionListView As System.Windows.Forms.ListView
    Friend WithEvents ObjectPropertyGrid As System.Windows.Forms.PropertyGrid
    Friend WithEvents UpdateButton As System.Windows.Forms.Button
    Friend WithEvents CloseButton As System.Windows.Forms.Button
    Friend WithEvents ExpressionName As System.Windows.Forms.ColumnHeader
    Friend WithEvents ExpressionEquation As System.Windows.Forms.ColumnHeader
    Friend WithEvents ExpressionValue As System.Windows.Forms.ColumnHeader
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
        Me.TreeViewPanel = New System.Windows.Forms.Panel
        Me.FeatureTreeView = New System.Windows.Forms.TreeView
        Me.Splitter1 = New System.Windows.Forms.Splitter
        Me.ListViewPanel = New System.Windows.Forms.Panel
        Me.Label1 = New System.Windows.Forms.Label
        Me.ExpressionListView = New System.Windows.Forms.ListView
        Me.Splitter2 = New System.Windows.Forms.Splitter
        Me.PropertyPanel = New System.Windows.Forms.Panel
        Me.CloseButton = New System.Windows.Forms.Button
        Me.UpdateButton = New System.Windows.Forms.Button
        Me.ObjectPropertyGrid = New System.Windows.Forms.PropertyGrid
        Me.Label2 = New System.Windows.Forms.Label
        Me.ExpressionName = New System.Windows.Forms.ColumnHeader
        Me.ExpressionEquation = New System.Windows.Forms.ColumnHeader
        Me.ExpressionValue = New System.Windows.Forms.ColumnHeader
        Me.TreeViewPanel.SuspendLayout()
        Me.ListViewPanel.SuspendLayout()
        Me.PropertyPanel.SuspendLayout()
        Me.SuspendLayout()
        '
        'TreeViewPanel
        '
        Me.TreeViewPanel.Controls.Add(Me.FeatureTreeView)
        Me.TreeViewPanel.Dock = System.Windows.Forms.DockStyle.Left
        Me.TreeViewPanel.Location = New System.Drawing.Point(0, 0)
        Me.TreeViewPanel.Name = "TreeViewPanel"
        Me.TreeViewPanel.Size = New System.Drawing.Size(200, 519)
        Me.TreeViewPanel.TabIndex = 0
        '
        'FeatureTreeView
        '
        Me.FeatureTreeView.Dock = System.Windows.Forms.DockStyle.Fill
        Me.FeatureTreeView.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.FeatureTreeView.ImageIndex = -1
        Me.FeatureTreeView.Location = New System.Drawing.Point(0, 0)
        Me.FeatureTreeView.Name = "FeatureTreeView"
        Me.FeatureTreeView.SelectedImageIndex = -1
        Me.FeatureTreeView.Size = New System.Drawing.Size(200, 519)
        Me.FeatureTreeView.TabIndex = 0
        '
        'Splitter1
        '
        Me.Splitter1.Location = New System.Drawing.Point(200, 0)
        Me.Splitter1.Name = "Splitter1"
        Me.Splitter1.Size = New System.Drawing.Size(3, 519)
        Me.Splitter1.TabIndex = 1
        Me.Splitter1.TabStop = False
        '
        'ListViewPanel
        '
        Me.ListViewPanel.Controls.Add(Me.Label1)
        Me.ListViewPanel.Controls.Add(Me.ExpressionListView)
        Me.ListViewPanel.Dock = System.Windows.Forms.DockStyle.Top
        Me.ListViewPanel.Location = New System.Drawing.Point(203, 0)
        Me.ListViewPanel.Name = "ListViewPanel"
        Me.ListViewPanel.Size = New System.Drawing.Size(397, 216)
        Me.ListViewPanel.TabIndex = 2
        '
        'Label1
        '
        Me.Label1.Anchor = CType(((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.Label1.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.Location = New System.Drawing.Point(8, 8)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(380, 23)
        Me.Label1.TabIndex = 1
        Me.Label1.Text = "Feature Expressions"
        '
        'ExpressionListView
        '
        Me.ExpressionListView.Anchor = CType((((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Bottom) _
                    Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.ExpressionListView.Columns.AddRange(New System.Windows.Forms.ColumnHeader() {Me.ExpressionName, Me.ExpressionEquation, Me.ExpressionValue})
        Me.ExpressionListView.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.ExpressionListView.FullRowSelect = True
        Me.ExpressionListView.Location = New System.Drawing.Point(8, 40)
        Me.ExpressionListView.MultiSelect = False
        Me.ExpressionListView.Name = "ExpressionListView"
        Me.ExpressionListView.Size = New System.Drawing.Size(380, 168)
        Me.ExpressionListView.TabIndex = 3
        Me.ExpressionListView.View = System.Windows.Forms.View.Details
        '
        'ExpressionName
        '
        Me.ExpressionName.Text = "Name"
        Me.ExpressionName.Width = 75
        '
        'ExpressionEquation
        '
        Me.ExpressionEquation.Text = "Equation"
        Me.ExpressionEquation.Width = 150
        '
        'ExpressionValue
        '
        Me.ExpressionValue.Text = "Value"
        Me.ExpressionValue.Width = 90
        '
        'Splitter2
        '
        Me.Splitter2.Dock = System.Windows.Forms.DockStyle.Top
        Me.Splitter2.Location = New System.Drawing.Point(203, 216)
        Me.Splitter2.Name = "Splitter2"
        Me.Splitter2.Size = New System.Drawing.Size(397, 3)
        Me.Splitter2.TabIndex = 3
        Me.Splitter2.TabStop = False
        '
        'PropertyPanel
        '
        Me.PropertyPanel.Controls.Add(Me.CloseButton)
        Me.PropertyPanel.Controls.Add(Me.UpdateButton)
        Me.PropertyPanel.Controls.Add(Me.ObjectPropertyGrid)
        Me.PropertyPanel.Controls.Add(Me.Label2)
        Me.PropertyPanel.Dock = System.Windows.Forms.DockStyle.Fill
        Me.PropertyPanel.Location = New System.Drawing.Point(203, 219)
        Me.PropertyPanel.Name = "PropertyPanel"
        Me.PropertyPanel.Size = New System.Drawing.Size(397, 300)
        Me.PropertyPanel.TabIndex = 4
        '
        'CloseButton
        '
        Me.CloseButton.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.CloseButton.Location = New System.Drawing.Point(304, 262)
        Me.CloseButton.Name = "CloseButton"
        Me.CloseButton.TabIndex = 3
        Me.CloseButton.Text = "Close"
        '
        'UpdateButton
        '
        Me.UpdateButton.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.UpdateButton.Location = New System.Drawing.Point(208, 262)
        Me.UpdateButton.Name = "UpdateButton"
        Me.UpdateButton.TabIndex = 2
        Me.UpdateButton.Text = "Update"
        '
        'ObjectPropertyGrid
        '
        Me.ObjectPropertyGrid.Anchor = CType((((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Bottom) _
                    Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.ObjectPropertyGrid.CommandsVisibleIfAvailable = True
        Me.ObjectPropertyGrid.LargeButtons = False
        Me.ObjectPropertyGrid.LineColor = System.Drawing.SystemColors.ScrollBar
        Me.ObjectPropertyGrid.Location = New System.Drawing.Point(8, 32)
        Me.ObjectPropertyGrid.Name = "ObjectPropertyGrid"
        Me.ObjectPropertyGrid.Size = New System.Drawing.Size(380, 222)
        Me.ObjectPropertyGrid.TabIndex = 1
        Me.ObjectPropertyGrid.Text = "PropertyGrid1"
        Me.ObjectPropertyGrid.ViewBackColor = System.Drawing.SystemColors.Window
        Me.ObjectPropertyGrid.ViewForeColor = System.Drawing.SystemColors.WindowText
        '
        'Label2
        '
        Me.Label2.Anchor = CType(((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.Label2.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label2.Location = New System.Drawing.Point(8, 8)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(380, 23)
        Me.Label2.TabIndex = 0
        Me.Label2.Text = "Properties"
        '
        'FeatureBrowserForm
        '
        Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
        Me.ClientSize = New System.Drawing.Size(600, 519)
        Me.Controls.Add(Me.PropertyPanel)
        Me.Controls.Add(Me.Splitter2)
        Me.Controls.Add(Me.ListViewPanel)
        Me.Controls.Add(Me.Splitter1)
        Me.Controls.Add(Me.TreeViewPanel)
        Me.Name = "FeatureBrowserForm"
        Me.ShowInTaskbar = False
        Me.Text = "Feature Browser"
        Me.TreeViewPanel.ResumeLayout(False)
        Me.ListViewPanel.ResumeLayout(False)
        Me.PropertyPanel.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub

#End Region

    Private Sub FeatureBrowserForm_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Try
            PopulateTreeView()
        Catch ex As System.Exception
            MessageBox.Show("Form Load Exception: " & ex.Message)
        End Try
    End Sub

    Private Declare Auto Sub SetParent Lib "USER32.DLL" _
        (ByVal child As IntPtr, ByVal newParent As IntPtr)

    Private Sub PopulateTreeView()
        FeatureTreeView.Nodes.Clear()
        Dim sessionParts As PartCollection
        sessionParts = theSession.Parts
        For Each myPart As Part In sessionParts
            If (myPart.IsFullyLoaded) Then
                Dim partNode As PartTreeNode
                partNode = New PartTreeNode(myPart)
                partNode.Text = myPart.Leaf
                FeatureTreeView.Nodes.Add(partNode)
                partNode.Update()
            End If
        Next myPart
    End Sub

    Private Sub PopulateExpressionListView(ByRef exps As IEnumerable)
        ResetExpressionListView()
        ExpressionListView.BeginUpdate()
        For Each myExpression As Expression In exps
            Dim expressionData(2) As String
            expressionData(0) = New String(myExpression.Name)
            expressionData(1) = New String(myExpression.Equation)
            expressionData(2) = New String(myExpression.Value.ToString())
            Dim expItem As ListViewItem
            expItem = New ListViewItem(expressionData)
            expItem.Tag = myExpression
            ExpressionListView.Items.Add(expItem)
            ObjectPropertyGrid.SelectedObject = Nothing
        Next myExpression
        ExpressionListView.View = System.Windows.Forms.View.Details
        ExpressionListView.EndUpdate()
    End Sub

    Private Sub ResetExpressionListView()
        ExpressionListView.Items.Clear()
        ExpressionListView.View = System.Windows.Forms.View.List
        ExpressionListView.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable
        ExpressionListView.MultiSelect = False
    End Sub

    Private Sub ResetFeatures()
        If Not FeatureTreeView.SelectedNode Is Nothing Then
            If TypeOf FeatureTreeView.SelectedNode Is FeatureTreeNode Then
                Dim featureNode As FeatureTreeNode
                featureNode = CType(FeatureTreeView.SelectedNode, FeatureTreeNode)
                If Not featureNode.OwningFeature Is Nothing Then
                    featureNode.OwningFeature.Unhighlight()
                End If
            End If
        End If
    End Sub

    Private Sub CloseButton_Click(ByVal sender As Object, _
                                  ByVal e As System.EventArgs) _
                                  Handles CloseButton.Click
        ResetFeatures()
        Me.Close()
    End Sub

    Private Sub FeatureTreeView_BeforeSelect(ByVal sender As Object, _
                                             ByVal e As System.Windows.Forms.TreeViewCancelEventArgs) _
                                             Handles FeatureTreeView.BeforeSelect
        If TypeOf e.Node Is FeatureTreeNode Then
            If Not FeatureTreeView.SelectedNode Is Nothing Then
                If TypeOf FeatureTreeView.SelectedNode Is FeatureTreeNode Then
                    Dim featureNode As FeatureTreeNode
                    featureNode = CType(FeatureTreeView.SelectedNode, FeatureTreeNode)
                    featureNode.OwningFeature.Unhighlight()
                End If
            End If
        End If
        e.Cancel = False
    End Sub

    Private Sub FeatureTreeView_AfterSelect(ByVal sender As Object, _
                                            ByVal e As System.Windows.Forms.TreeViewEventArgs) _
                                            Handles FeatureTreeView.AfterSelect
        If TypeOf e.Node Is PartTreeNode Then
            Dim partNode As PartTreeNode = CType(e.Node, PartTreeNode)
            partNode.Update()
            PopulateExpressionListView(partNode.OwningPart.Expressions)
        ElseIf TypeOf e.Node Is FeatureTreeNode Then
            Dim featureNode As FeatureTreeNode = CType(e.Node, FeatureTreeNode)
            featureNode.OwningFeature.Highlight()
            PopulateExpressionListView(featureNode.OwningFeature.GetExpressions())
            ObjectPropertyGrid.SelectedObject = featureNode.FeatureSurrogate
        ElseIf TypeOf e.Node Is BodyTreeNode Then
            Dim bodyNode As BodyTreeNode = CType(e.Node, BodyTreeNode)
            bodyNode.OwningBody.Highlight()
            ObjectPropertyGrid.SelectedObject = New BodySurrogate(bodyNode.OwningBody)
        ElseIf TypeOf e.Node Is DisplayableObjectTreeNode Then
            Dim objectNode As DisplayableObjectTreeNode = CType(e.Node, DisplayableObjectTreeNode)
            ObjectPropertyGrid.SelectedObject = objectNode.ObjRef
        End If
    End Sub

    Private Sub ExpressionListView_SelectedIndexChanged(ByVal sender As Object, _
                                                        ByVal e As System.EventArgs) _
                                                        Handles ExpressionListView.SelectedIndexChanged
        If ExpressionListView.SelectedItems.Count > 0 Then
            ObjectPropertyGrid.SelectedObject = _
                New ExpressionSurrogate(CType(ExpressionListView.SelectedItems(0).Tag, Expression))
        End If
    End Sub

    Public Shared Function GetUnloadOption(ByVal arg As String) As Integer
        Dim unloadOption As Integer = Session.LibraryUnloadOption.Explicitly
        Dim theSession As Session = Session.GetSession()
        theSession.LogFile.WriteLine("Sample2.cs: Called GetUnloadOption, returning " & _
                                     unloadOption.ToString())
        Return unloadOption
    End Function

    Public Shared Function UnloadLibrary(ByVal arg As String) As Integer
        Dim theSession As Session
        theSession = Session.GetSession()
        theSession.LogFile.WriteLine("Sample2.cs: Called UnloadLibrary")
        If (Not mainForm Is Nothing) Then
            mainForm.Close()
            mainForm.Dispose()
            mainForm = Nothing
        End If
        Return 0
    End Function

    Private Sub UpdateButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles UpdateButton.Click
        Dim undoMark As Integer
        Try
            Me.theSession.UpdateManager.DoUpdate(undoMark)
        Catch ex As Exception
            Me.theSession.UndoToLastVisibleMark()
        End Try
    End Sub
End Class
