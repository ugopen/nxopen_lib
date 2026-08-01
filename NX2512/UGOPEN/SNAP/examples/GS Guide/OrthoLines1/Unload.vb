Public Class Unload

   Public Shared Function GetUnloadOption(ByVal dummy As String) As Integer
      Dim unloadOption As Integer
      unloadOption = Snap.UnloadOption.Immediately       ' After executing
      'unloadOption = Snap.UnloadOption.AtTermination     ' When NX session terminates
      'unloadOption = Snap.UnloadOption.Explicitly        ' Using File-->Unload
      Return unloadOption
   End Function

End Class