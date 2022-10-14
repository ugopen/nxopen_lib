Imports NXOpen

Module NXJournal
    Sub Main()

        Dim theSession = Session.GetSession()

        Guide.InfoWriteLine("Outputting list of user attributes on each body in the work part:")
        Dim bodies() As Body = theSession.Parts.Work.Bodies.ToArray()
        For Each aBody As Body In bodies
            Dim attributes() As NXObject.AttributeInformation = aBody.GetUserAttributes()
            For Each attribute As NXObject.AttributeInformation In attributes
                Guide.InfoWriteLine(attribute.Title & " = " & attribute.StringValue)
            Next attribute
        Next aBody
        Guide.InfoWriteLine("")

    End Sub
End Module



