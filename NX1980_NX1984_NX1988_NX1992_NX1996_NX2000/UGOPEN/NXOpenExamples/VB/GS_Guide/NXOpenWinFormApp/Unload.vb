Public Class Unload

   Public Shared Function GetUnloadOption(ByVal dummy As String) As Integer
      Dim unloadOption As Integer
      unloadOption = NXOpen.Session.LibraryUnloadOption.Immediately        ' After executing
      'unloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination     ' When NX session terminates
      'unloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly        ' Using File-->Unload
      Return unloadOption
   End Function

End Class
