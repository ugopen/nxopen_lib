Imports System
Imports NXOpen

' NX Open example demonstrating how to cycle through the 
' PhysicalMaterial objects in the PhysicalMaterialCollection
Module NXOpenSample
    Sub Main ()

        Dim theSession = Session.GetSession()

        Dim materialManager = theSession.Parts.BaseWork.MaterialManager
        
        Dim physMatCollection = materialManager.PhysicalMaterials

        Guide.InfoWriteLine("List of Physical Materials")
        For Each material In physMatCollection
            material.InfoMaterial()
            Guide.InfoWriteLine(material.Name)
        Next material

    End Sub
End Module
