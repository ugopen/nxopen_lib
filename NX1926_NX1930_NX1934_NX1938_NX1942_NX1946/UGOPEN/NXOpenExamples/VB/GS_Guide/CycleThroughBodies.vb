Imports System
Imports NXOpen

Module NXJournal
    Sub Main ()

        Dim theSession = Session.GetSession()
        Dim theUI = UI.GetUI()
        Guide.InfoWriteLine("Session and UI are created.")
        Guide.InfoWriteLine("")

        Dim workPart = theSession.Parts.Work
        Guide.InfoWriteLine("Outputting list of bodies in work part:")
        Dim bodies = workPart.Bodies
        For Each body in bodies
            Guide.InfoWriteLine("Body: " & body.Name)
        Next body 
        Guide.InfoWriteLine("")

        Guide.InfoWriteLine("Outputting list of user attributes in each body in the work part:")
        For Each body in bodies
            Dim attributes = body.GetUserAttributes()
            For Each attribute in attributes
                Guide.InfoWriteLine(attribute.Title &  " = " & attribute.StringValue)
            Next attribute 
        Next body
        Guide.InfoWriteLine("")

    End Sub
End Module



