Imports System
Imports NXOpen

Module NXJournal
    Sub Main ()

        Dim theSession = Session.GetSession()
        Dim theUI = UI.GetUI()

        Dim workPart = theSession.Parts.Work

        Dim bodiesInPart = workPart.Bodies

        For Each body In bodiesInPart
            Dim faces = body.GetFaces
            For Each face In Faces
                face.SetUserAttribute("Surface Finish", -1, "Bead Blasted", Update.Option.Now)
            Next face
        Next body

    End Sub
End Module

