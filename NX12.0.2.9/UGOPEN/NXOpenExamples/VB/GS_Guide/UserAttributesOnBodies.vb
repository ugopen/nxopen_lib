Imports NXOpen

Module NXJournal
  Sub Main ()

    Dim theSession = Session.GetSession()

    Guide.InfoWriteLine("Outputting list of user attributes on each body in the work part:")
    Dim bodies = theSession.Parts.Work.Bodies
    For Each body in bodies
      Dim attributes = body.GetUserAttributes()
      For Each attribute in attributes
        Guide.InfoWriteLine(attribute.Title &  " = " & attribute.StringValue)
      Next attribute 
    Next body
    Guide.InfoWriteLine("")

  End Sub
End Module





