Imports System
Imports NXOpen

Module NXJournal
  Sub Main ()

    Dim theSession = Session.GetSession()

    Guide.InfoWriteLine("Outputting list of user attributes on the work part:")
    Dim attributes = theSession.Parts.Work.GetUserAttributes()
    For Each attribute in attributes
      Guide.InfoWriteLine(attribute.Title &  " = " & attribute.StringValue)
    Next attribute 
    Guide.InfoWriteLine("")

  End Sub
End Module






