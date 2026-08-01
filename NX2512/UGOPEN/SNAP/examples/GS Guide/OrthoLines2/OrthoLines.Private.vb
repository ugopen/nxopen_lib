Partial Public Class OrthoLines
   Inherits Snap.UI.BlockDialog

   Public Shared theOrthoLines As OrthoLines
   Private directionBlock As Snap.UI.Block.Enumeration  ' Block type: Enumeration
   Private offsetBlock As Snap.UI.Block.Double          ' Block type: Double
   Private thinDashedButton As Snap.UI.Block.Button     ' Block type: Button
   Private thickSolidButton As Snap.UI.Block.Button     ' Block type: Button

   Public Sub New(theDlxFileName As String)

      Me.NXOpenBlockDialog = New Snap.UI.BlockDialog(theDlxFileName).NXOpenBlockDialog
      Me.NXOpenBlockDialog.AddApplyHandler(AddressOf ApplyCallback)
      Me.NXOpenBlockDialog.AddOkHandler(AddressOf OkCallback)
      Me.NXOpenBlockDialog.AddUpdateHandler(AddressOf UpdateCallback)
      Me.NXOpenBlockDialog.AddInitializeHandler(AddressOf InitializeCallback)
      Me.NXOpenBlockDialog.AddDialogShownHandler(AddressOf DialogShownCallback)

   End Sub

End Class
