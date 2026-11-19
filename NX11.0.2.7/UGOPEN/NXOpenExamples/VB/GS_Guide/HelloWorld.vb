Imports NXOpen

' Simple NX Open Hello World example
Module NXOpenSample
    Sub Main ()

        Dim theSession = Session.GetSession()
        Guide.InfoWriteLine("Hello, World!")

    End Sub
End Module
