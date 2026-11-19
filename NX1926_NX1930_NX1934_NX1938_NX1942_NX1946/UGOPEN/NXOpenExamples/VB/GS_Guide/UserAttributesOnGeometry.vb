Imports NXOpen

Module NXJournal
    Sub Main()

        Dim theSession = Session.GetSession()

        Guide.InfoWriteLine("Outputting list of user attributes on geometry in the work part:")
        Dim bodies() As Body = theSession.Parts.Work.Bodies.ToArray()
        For Each aBody As Body In bodies
            PrintAttributes(aBody)
            Dim edges = aBody.GetEdges()
            For Each edg As Edge In edges
                PrintAttributes(edg)
            Next edg
            Dim faces = aBody.GetFaces()
            For Each f As Face In faces
                PrintAttributes(f)
            Next f
        Next aBody
        Guide.InfoWriteLine("")

    End Sub

    Sub PrintAttributes(obj As NXObject)
        Dim attributes = obj.GetUserAttributes()
        For Each attribute As NXObject.AttributeInformation In attributes
            Guide.InfoWriteLine(attribute.Title & " = " & attribute.StringValue)
        Next attribute
    End Sub
End Module








