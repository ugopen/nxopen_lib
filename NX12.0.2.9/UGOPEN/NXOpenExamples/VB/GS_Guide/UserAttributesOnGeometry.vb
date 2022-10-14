Imports NXOpen

Module NXJournal
  Sub Main ()

    Dim theSession = Session.GetSession()

    Guide.InfoWriteLine("Outputting list of user attributes on geometry in the work part:")
    Dim bodies = theSession.Parts.Work.Bodies
    For Each body in bodies
      PrintAttributes(body) 
      Dim edges = body.GetEdges()
      For Each edge in edges
        PrintAttributes(edge)
      Next edge
      Dim faces = body.GetFaces()
      For Each face in faces
        PrintAttributes(face)
      Next face
    Next body
    lw.WriteLine("")

  End Sub

  Sub PrintAttributes (obj As NXObject)
    Dim attributes = obj.GetUserAttributes()
    For Each attribute in attributes
      Guide.InfoWriteLine(attribute.Title & " = " & attribute.StringValue)
    Next attribute
  End Sub
End Module








