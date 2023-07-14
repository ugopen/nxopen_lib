Imports Snap, Snap.Create, System.Linq

Public Class CarAssembly

   Public Shared Sub Main()

      ' For a discussion of assemblies concepts, including the code below,
      ' please see Chapter 11 of the SNAP Getting Started Guide.
      ' For interesting results, set your work part to Car_Assembly.prt.
      ' You can find this part in the CarPartFiles folder.

      ' Get the root component of the work part
      Dim workPart As NX.Part = Snap.Globals.WorkPart
      Dim root As NX.Component = workPart.RootComponent


      Description("Children of the root node")
      Dim children As NX.Component() = root.Children
      For Each child As NX.Component In children
         Dim proto As NX.Part = child.Prototype       ' Get the prototype part
         Dim protoName As String = proto.Name         ' Get the part name
         InfoWindow.WriteLine(protoName)              ' Write it out
      Next


      Description("Leaf nodes")
      For Each leaf As NX.Component In root.Leaves
         Dim compName As String = leaf.Name                    ' Name of component
         Dim proto As NX.Part = leaf.Prototype                 ' Get the prototype part
         Dim protoName As String = proto.Name                  ' Get the part name
         InfoWindow.WriteLine(compName & " ; " & protoName)    ' Write it out
      Next


      Description("Descendants with depths")
      For Each comp As NX.Component In root.Descendants
         Dim compName As String, parentName As String
         If comp.IsRoot Then
            compName = "[ROOT]"
            parentName = "[NO PARENT]"
         Else
            compName = comp.Name
            parentName = comp.Parent.Name
         End If

         If comp.Depth = 1 Then parentName = "[ROOT]"

         InfoWindow.Write("Depth: " & comp.Depth.ToString & " ;  ")
         InfoWindow.Write("Component: " & compName & " ;  ")
         InfoWindow.WriteLine("Parent: " & parentName)
      Next

      
      Description("Indented listing of descendents")
      For Each comp As NX.Component In root.Descendants
         Dim indentString As String = Indent(comp.Depth)
         Dim compName As String = comp.Name
         If comp.IsRoot Then compName = "[ROOT]"
         InfoWindow.WriteLine(indentString & compName)
      Next


      Description("Recursive traversal")
      DoSomething(root)


      ' Build list of descendant parts and vendors
      Dim AcmeList As New List(Of NX.Part)
      For Each comp As NX.Component In root.Descendants
         Dim proto As NX.Part = comp.Prototype
         If GetVendor(proto) = "Acme" Then
            AcmeList.Add(proto)
         End If
      Next


      Description("Component positions")
      For Each comp As NX.Component In workPart.RootComponent.Descendants
         Dim location As Snap.Position = comp.Position
         Dim orientation As Snap.Orientation = comp.Orientation
         Dim axisZ As Snap.Vector = orientation.AxisZ
         InfoWindow.Write("comp = " & comp.Name & " ;  ")
         InfoWindow.Write("comp.Position = " & location.ToString("F0") & " ;  ")
         InfoWindow.Write("comp.Orientation.AxisZ = " & axisZ.ToString("F0") & vbCrLf)
      Next


      Description("Occurrence bodies")
      For Each obj As NX.NXObject In workPart.Objects
         If obj.IsOccurrence And obj.ObjectType = NX.ObjectTypes.Type.Body Then
            Dim occName As String = obj.Name
            Dim protoName As String = obj.Prototype.Name
            InfoWindow.Write("Occurrence: " & occName & "  ; ")
            InfoWindow.Write("Owning component: " & obj.OwningComponent.Name & "  ; ")
            InfoWindow.WriteLine("Prototype: " & protoName)
         End If
      Next

   End Sub

   Public Shared Function Indent(level As Integer) As String
      Dim space As Char = " "c
      Return New String(space, 3 * level)     ' Indent 3 spaces for each level
   End Function

   Public Shared Sub DoSomething(comp As NX.Component)
      InfoWindow.WriteLine(comp.Name)
      For Each child As NX.Component In comp.Children
         DoSomething(child)
      Next
   End Sub

   Public Shared Function GetVendor(part As NX.Part) As String
      Return part.GetStringAttribute("Vendor")
   End Function

   Public Shared Sub Description(descriptionText As String)
      InfoWindow.WriteLine(vbCrLf & "==== " & descriptionText & " ===========================")
   End Sub

End Class
