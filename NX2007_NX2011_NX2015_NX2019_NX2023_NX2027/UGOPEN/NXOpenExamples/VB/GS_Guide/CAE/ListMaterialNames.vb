Imports System
Imports NXOpen
Imports System.Xml
Imports System.Collections.Generic

' NX Open example to list out the names of the materials
' stored in a library material database. 
Module xmlTest

  Sub Main()

    Dim theSession = Session.GetSession()

    Dim nxInstallDir = Environment.GetEnvironmentVariable("UGII_BASE_DIR")
    Dim materialsLibFile = System.IO.Path.Combine(nxInstallDir, "UGII", "materials", "physicalmateriallibrary.xml")

    Dim materialNames = New List(Of String)()

    Dim doc As New XmlDocument()
    doc.Load(materialsLibFile)
    Dim root = doc.DocumentElement
    Dim nodeList As XmlNodeList = root.SelectNodes("//Material/BulkDetails/Name")
    
    For Each node In nodeList
      Guide.InfoWriteLine(node.InnerText)
    Next

  End Sub

End Module
