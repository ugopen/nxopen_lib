'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                    Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'

Option Strict Off
Imports System
Imports NXOpen
Imports System.Text.RegularExpressions
Imports System.Collections
Imports Microsoft.VisualBasic


Module NXJournal

    ' This class can read the layer_standards.txt file
    ' and create a map that associates each NXOpen class or
    ' UF type and subtype with the corresponding layer, as specified in
    ' the layer_standards.txt file.
    Class LayerToClassMap

        Public Shared ReadOnly AnyUFSubtype As Integer = -1

        ''''''''''
        '      PUBLIC METHODS
        ''''''''''

        ' Constructor
        Public Sub New(ByVal workPart As Part)
            m_part = workPart
            m_NXClassNameLayerMap = New Hashtable
            m_UFTypeToLayerMap = New Hashtable
        End Sub

        ' Reads the layer_standards.txt file.
        ' This function must be called before calling FindLayerForNXClass
        ' or FindLayerForUFType.
        '
        ' The layer_standards.txt file has the format
        ' <start> := <full_layer_spec>*
        ' <full_layer_spec> := <layer_decl><layer_spec>
        ' <layer_decl> := (|layer )(<layer id>|<layer category name>):<end of line>
        ' <layer_spec> := <layer_single_spec>(,<layer_single_spec>)*
        ' <layer_single_spec> := (<nx class name>|<uf type>(.<uf subtype>))
        Public Sub ReadStandardsFile()
            Me.ReadNXClassTree()
            Dim fileStream As System.IO.StreamReader = New System.IO.StreamReader("layer_standards.txt")
            Dim commentRegex As Regex = New Regex("#[^#]*(#|$)")
            Dim layerDeclRegex As Regex = New Regex("^(|layer\s+)(\w+)\s*:$")
            Dim currentLayer As Object = Nothing
            Do
                Dim line As String = fileStream.ReadLine()
                m_lineNumber = m_lineNumber + 1
                If line Is Nothing Then Exit Do
                ' Strip out comments
                line = commentRegex.Replace(line, "")
                line = line.Trim()
                If line = "" Then GoTo EndOfLoop
                Dim match As Match
                ' Check whether the line is a <layer_decl> (layer declaration)
                match = layerDeclRegex.Match(line)
                If match.Success Then
                    currentLayer = Nothing
                    Dim currentLayerStr As String = match.Groups(2).Value
                    ' currentLayerStr must be either an integer or the name of a
                    ' LayerCategory
                    Try
                        Dim currentLayerInt As Integer = Integer.Parse(currentLayerStr)
                        If Layer.Constants.FirstLayer <= currentLayerInt AndAlso currentLayerInt <= Layer.Constants.LastLayer Then
                            currentLayer = currentLayerInt
                        End If
                    Catch ex As FormatException
                        currentLayer = m_part.LayerCategories.FindObject(currentLayerStr)
                    End Try
                    If currentLayer Is Nothing Then ThrowException("Layer " & currentLayerStr & " not found")

                Else
                    If currentLayer Is Nothing Then ThrowException("Expecting line with format ""<layer id or category name>:""")
                    ' the line must be a <layer_spec> 
                    ' (specification of the classes and UF types that should be placed on the layer)
                    ParseLayerSpec(line, currentLayer)
                End If

EndOfLoop:
            Loop

        End Sub

        ' Returns the layerObject associated with the NXOpen class with the given name
        ' The layerObject returned is either an Integer for the layer ID or a LayerCategory object
        ' You must call ReadStandardsFile once before calling this method
        Public Function FindLayerForNXClass(ByVal className As String) As Object
            If Not className.StartsWith("NXOpen.") Then Return Nothing
            className = className.Substring(className.LastIndexOf(".") + 1)
            Return Me.m_NXClassNameLayerMap.Item(className)
        End Function

        ' Returns the layerObject associated with the given UF type and subtype
        ' The layerObject returned is either an Integer for the layer ID or an LayerCategory object
        ' You must call ReadStandardsFile once before calling this method
        Public Function FindLayerForUFType(ByVal ufType As Integer, ByVal ufSubtype As Integer) As Object
            Dim layerObj As Object
            layerObj = Me.m_UFTypeToLayerMap.Item(New UfTypeSubtype(ufType, ufSubtype))
            If layerObj Is Nothing Then
                layerObj = Me.m_UFTypeToLayerMap.Item(New UfTypeSubtype(ufType, AnyUFSubtype))
            End If
            Return layerObj
        End Function

        ''''''''''
        '      PRIVATE DATA TYPES
        ''''''''''

        Private Structure UfTypeSubtype
            Dim uftype, ufsubtype As Integer

            Public Sub New(ByVal ty As Integer, ByVal subty As Integer)
                uftype = ty
                ufsubtype = subty
            End Sub
        End Structure


        ''''''''''
        '      PRIVATE METHODS
        ''''''''''

        Private Sub ThrowException(ByVal str As String)
            Throw New System.Exception("Error parsing line number " & m_lineNumber.ToString() & " of layer_standards.txt" & Chr(10) & str)
        End Sub

        ' ReadNXClassTree
        ' Reads the NXOpen class hierarchy into m_NXClassTree
        ' We need to read this data to know:
        '   1. which classes are defined
        '   2. what classes inherit from a given class
        ' When a class is specified in the layer_standards file, we associate
        ' the layer with all classes that inherit from that class.
        ' That is why we need to know what classes inherit from each class.
        Private Sub ReadNXClassTree()
            Dim found As Boolean = False
            Dim assem As System.Reflection.Assembly
            For Each assem In AppDomain.CurrentDomain.GetAssemblies()
                If assem.GetName().Name = "NXOpen" Then
                    found = True
                    Exit For
                End If
            Next
            If Not found Then ThrowException("Could not read NXOpen.dll")

            m_NXClassTree = New Hashtable

            Dim modules As System.Reflection.Module() = assem.GetModules()
            Dim m As System.Reflection.Module
            For Each m In modules

                Dim types() As Type = m.GetTypes()
                Dim t As Type
                For Each t In types
                    If (t.IsClass OrElse t.IsInterface) AndAlso t.ToString().StartsWith("NXOpen.") Then
                        Dim typeName As String = t.ToString()
                        typeName = typeName.Substring(typeName.LastIndexOf(".") + 1)
                        If Not m_NXClassTree.ContainsKey(typeName) Then
                            m_NXClassTree.Add(typeName, New ArrayList)
                        End If

                        ' parents will consist of all classes and interfaces that the current class
                        ' inherits from
                        Dim parents As ArrayList = New ArrayList(t.GetInterfaces())
                        If t.IsClass Then
                            parents.Add(t.BaseType)
                        End If

                        Dim parentType As Type
                        For Each parentType In parents

                            Dim parentTypeName As String = parentType.ToString()
                            If parentTypeName.StartsWith("NXOpen.") Then
                                parentTypeName = parentTypeName.Substring(parentTypeName.LastIndexOf(".") + 1)
                                ' Add typeName to the list of all child classes for
                                ' the parent class
                                Dim parentsChildList As ArrayList = m_NXClassTree.Item(parentTypeName)
                                If parentsChildList Is Nothing Then
                                    parentsChildList = New ArrayList
                                    m_NXClassTree.Add(parentTypeName, parentsChildList)
                                End If
                                parentsChildList.Add(typeName)
                            End If


                        Next


                    End If ' if t is interface or class

                Next ' type t
            Next ' module m

        End Sub

        ' GetDescendentNXClasses
        ' Adds to <descendents> a list of the names of all classes that inherit from
        ' the class named <className>
        Private Sub GetDescendentNXClasses(ByVal className As String, ByRef descendents As ArrayList)
            Dim startRange As Integer
            startRange = descendents.Count()
            If Not m_NXClassTree.ContainsKey(className) Then ThrowException("Class " & className & " not found")
            descendents.AddRange(m_NXClassTree.Item(className))
            Dim endRange As Integer
            endRange = descendents.Count - 1
            Dim ii As Integer
            For ii = startRange To endRange
                GetDescendentNXClasses(descendents.Item(ii), descendents)
            Next

        End Sub

        ' ParseSingleLayerSpec
        ' Part of the parser used by ReadStandardsFile.
        ' Reads a <layer_single_spec>.
        '
        ' Parameters:
        ' className - either the name of an NXOpen class or a UF type
        ' subtypeName - a string in the form ".<uf subtype>" for the UF subtype
        ' currentLayer - the layer object that the class or UF type will be associated with
        Private Sub ParseSingleLayerSpec(ByVal typeName As String, ByVal subtypeName As String, ByVal currentLayer As Object)

            ' className will converted to the name of the NXOpen class or
            ' will be set to Nothing if a UF type has been specified
            Dim className As String = typeName
            Dim ufTypeName As String = Nothing
            Dim ufSubtypeName As String = Nothing
            If subtypeName <> "" Then
                ' A NXOpen class cannot have a subtypeName, so className
                ' must be a UF type
                ufTypeName = className
                className = Nothing
                Dim match As Match = Regex.Match(subtypeName, "\.\s*(\w+)")
                If Not match.Success Then ThrowException("Expecting UF subtype specification with format "".<uf subtype>""")
                ufSubtypeName = match.Groups(1).Value
            End If
            If Not className Is Nothing Then
                className = Char.ToUpper(className.Chars(0)) & className.Substring(1)
                ' If the className is not in the NXOpen class tree,
                ' we will assume it is a UF type instead
                If Not Me.m_NXClassTree.ContainsKey(className) Then
                    ufTypeName = typeName
                    className = Nothing
                End If
            End If

            If className Is Nothing Then
                ' Must be a UF type
                Dim ufTypeId As Integer
                Dim ufSubtypeId As Integer = AnyUFSubtype
                If Not Regex.Match(ufTypeName, "^UF_").Success Then
                    ufTypeName = "UF_" & ufTypeName & "_type"
                End If
                Dim fi As System.Reflection.FieldInfo
                fi = m_UFConst.GetField(ufTypeName)
                If fi Is Nothing Then ThrowException("Could not find NX Automation class or UF type named " & typeName)
                ufTypeId = fi.GetValue(Nothing)

                If Not ufSubtypeName Is Nothing Then
                    If Not Regex.Match(ufSubtypeName, "^UF_").Success Then
                        ufSubtypeName = "UF_" & ufSubtypeName & "_subtype"
                    End If
                    fi = m_UFConst.GetField(ufSubtypeName)
                    If fi Is Nothing Then ThrowException("Could not find UF subtype " & ufSubtypeName)
                    ufSubtypeId = fi.GetValue(Nothing)
                End If

                Me.m_UFTypeToLayerMap.Add(New UfTypeSubtype(ufTypeId, ufSubtypeId), currentLayer)

            Else
                ' Must be an NXOpen class

                ' Associate the currentLayer with the class and all subclasses that inherit 
                ' from it, unless the subclass has already been associated with a layer
                ' through another rule that is more specific to the class.
                '
                ' For example, suppose Arc inherits from Conic, Conic inherits from Curve, Curve inherits from
                ' DisplayableObject, and className is Curve and
                ' currentLayer is layer A.
                ' If Arc has not been associated with a layer, then associate it with
                ' layer A.  If Arc has been associated with layer B through a 
                ' rule that associates DisplayableObject with layer B, then overwrite
                ' that association, since the rule associating DisplayableObject with B
                ' is less class-specific than the rule associating Curve with A.
                ' But if Arc has been associated with a layer B through a
                ' rule that associates Conic with layer B, do not overwrite that
                ' association, since the rule associating Conic with B
                ' is more class-specific than the rule associating Curve with A.
                Dim layerOfParent As Object = m_NXClassNameLayerMap.Item(className)
                Dim classAndDescendents As ArrayList = New ArrayList
                classAndDescendents.Add(className)
                Me.GetDescendentNXClasses(className, classAndDescendents)
                Dim descendentClassName As String
                For Each descendentClassName In classAndDescendents
                    ' If the class has not been associated with a layer, create
                    ' an association
                    If Not m_NXClassNameLayerMap.ContainsKey(descendentClassName) Then
                        m_NXClassNameLayerMap.Add(descendentClassName, currentLayer)

                        ' ElseIf the class has been association with a layer through a
                        ' rule that is less class-specific, overwrite the association.
                        '
                        ' The purpose of the 
                        ' "ElseIf m_NXClassNameLayerMap.Item(descendentClassName).Equals(layerOfParent)"
                        ' is to make sure that the subclass
                        ' has not been associated with a different layer through a specification
                        ' that is more specific to the class.
                    ElseIf m_NXClassNameLayerMap.Item(descendentClassName).Equals(layerOfParent) Then
                        m_NXClassNameLayerMap.Item(descendentClassName) = currentLayer
                    End If
                Next

            End If


        End Sub


        ' ParseLayerSpec
        ' Part of the parser used by ReadStandardsFile.
        ' Reads a <layer_spec>.
        Private Sub ParseLayerSpec(ByVal line As String, ByVal currentLayer As Object)
            Static Dim layerSpecRegex As Regex = New Regex("^(\w+)(\s*\.\s*\w*)?")
            Dim match As Match = layerSpecRegex.Match(line)
            If Not match.Success Then ThrowException("Expecting specification of which classes are in the layer" & Chr(10) & _
               "having the format <layer spec>,(<layer spec>)*")
            ParseSingleLayerSpec(match.Groups(1).Value, match.Groups(2).Value, currentLayer)
            line = line.Substring(match.Index + match.Length)
            line = line.Trim()
            If line = "" Then Exit Sub
            If Not line.Chars(0) = "," Then ThrowException("Expecting "","" or end-of-line")
            line = line.Substring(1).Trim()
            If line = "" Then Exit Sub
            ParseLayerSpec(line, currentLayer)

        End Sub

        ' Prints out the contents of the m_NXClassTree
        ' Used for debugging purposes only
        Private Sub PrintNXClassTree(ByVal cout As ListingWindow)
            cout.Open()
            Dim keys As ICollection = m_NXClassTree.Keys()
            Dim key As String
            For Each key In keys
                cout.WriteLine(key)
                Dim value As ArrayList = m_NXClassTree(key)
                Dim ii
                For ii = 0 To value.Count() - 1
                    cout.WriteLine("   " + CType(value(ii), String))
                Next
            Next
            cout.Close()
        End Sub

        ''''''''''
        '      PRIVATE DATA
        ''''''''''

        Private m_part As Part ' the work part

        ' m_NXClassNameLayerMap
        ' A map associating the name of a NXOpen class with
        ' the layer that objects of that class should be placed in.
        ' The map consists of key-value pairs:
        ' (className, layerObject)
        ' where className is the class name, e.g. "Line",
        ' and layerObject is either an integer for the layer ID or
        ' a LayerCategory object
        Private m_NXClassNameLayerMap As Hashtable

        ' m_UFTypeToLayerMap
        ' A map associating a UF type and subtype with
        ' the layer that objects with that type and subtype should be placed in.
        ' The map consists of key-value pairs:
        ' (ufTypeSubtype, layerObject)
        ' where ufTypeSubtype is a UfTypeSubtype pair 
        ' and layerObject is either an integer for the layer ID or
        ' a LayerCategory object.
        ' AnyUFSubtype is used for the ufSubtype to match any UF subtype.
        Private m_UFTypeToLayerMap As Hashtable

        ' m_NXClassTree
        ' Contains a representation of the inheritance hierarchy of all the
        ' NXOpen classes.
        ' It consists of key-value pairs:
        ' (className, subclassNames)
        ' where subclassNames is a list containing the name of each class that directly
        ' inherits from the class named className.
        Private m_NXClassTree As Hashtable

        Private m_UFConst As Type = GetType(NXOpen.UF.UFConstants)

        ' m_lineNumber
        ' the line number of the line in the layer_standards.txt file
        ' currently being parsed
        Private m_lineNumber As Integer

    End Class

    ' Contains a list of pairs
    ' (layerId, objsToMove)
    ' where layerId is a layer ID and objsToMove are the objects to move to that layer
    Class ListsOfObjectsToMove

        Public Sub New()
            m_lists = New SortedList
        End Sub

        ' Add objToMove to the list for layerId
        Public Sub Add(ByVal layerId As Integer, ByVal objToMove As NXObject)
            Dim list As ArrayList = m_lists.Item(layerId)
            If list Is Nothing Then
                list = New ArrayList
                m_lists.Item(layerId) = list
            End If
            list.Add(objToMove)
        End Sub

        ' Cycles through the lists contained in this object.
        ' Each time GetNextList is called, a new list is returned.
        ' If there are no more lists, layerId is set to -1
        '
        ' objs is the list for the layer with ID layerId
        Public Sub GetNextList(ByRef layerId As Integer, ByRef objs() As DisplayableObject)
            If m_nextKeyIndex >= m_lists.Count Then
                layerId = -1
                objs = Nothing
                Exit Sub
            End If
            layerId = m_lists.GetKey(m_nextKeyIndex)
            Dim list As ArrayList = m_lists.GetByIndex(m_nextKeyIndex)
            objs = list.ToArray(GetType(DisplayableObject))
            m_nextKeyIndex = m_nextKeyIndex + 1

        End Sub

        Private m_lists As SortedList
        Private m_nextKeyIndex As Integer = 0
    End Class

    ' Returns the layer where the obj should be placed, and returns -1 if the object should not be moved
    Function FindLayerToMoveObjectTo(ByVal obj As NXObject, ByVal nxopenSession As NXOpen.UF.UFSession, ByVal layerToClassMap As LayerToClassMap) As Integer
        Dim currentLayerId As Integer = CType(obj, Object).Layer
        Dim correctLayerId As Integer = -1
        Dim correctLayer As Object = layerToClassMap.FindLayerForNXClass(obj.GetType.ToString())
        If correctLayer Is Nothing Then
            Dim ufType As Integer
            Dim ufSubtype As Integer
            nxopenSession.Obj.AskTypeAndSubtype(obj.Tag, ufType, ufSubtype)
            correctLayer = layerToClassMap.FindLayerForUFType(ufType, ufSubtype)
        End If

        If correctLayer Is Nothing Then Return -1
        If TypeOf correctLayer Is Integer Then
            ' Only change the layer if the object is not in the correct layer
            If currentLayerId <> CInt(correctLayer) Then
                correctLayerId = CInt(correctLayer)
            End If
        Else
            ' If the object is not already in the LayerCategory, then
            ' return the first layer in the LayerCategory
            Dim layerCategory As Layer.Category = CType(correctLayer, Layer.Category)
            Dim members() As Integer = layerCategory.GetMemberLayers()
            If members.Length > 0 AndAlso Array.IndexOf(members, currentLayerId) < 0 Then
                correctLayerId = members(0)
            End If
        End If

        Return correctLayerId

    End Function

    Sub Main()

        Dim theSession As Session = Session.GetSession()
        Dim nxopenSession As NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
        Dim workPart As Part = theSession.Parts.Work

        Dim layerToClassMap As LayerToClassMap = New LayerToClassMap(workPart)
        layerToClassMap.ReadStandardsFile()


        Dim listsOfObjectsToMove As ListsOfObjectsToMove = New ListsOfObjectsToMove
        Dim objs() As NXObject = workPart.Layers.GetAllObjectsOnLayer(workPart.Layers.WorkLayer)
        Dim obj As NXObject
        Dim sketchesOnWorkLayer As ArrayList = New ArrayList
        For Each obj In objs
            ' Unfortunately, sketches need to be treated as a special case.  The reason
            ' is that if the curves that belong to the sketch are moved after the sketch,
            ' the curves will be moved to a different layer than the sketch.
            ' So, sketches must be moved after the curves that are on them.
            If TypeOf obj Is Sketch Then
                sketchesOnWorkLayer.Add(obj)
            Else
                Dim correctLayerId As Integer = _
                   FindLayerToMoveObjectTo(obj, nxopenSession, layerToClassMap)
                ' correctLayerId is -1 if the object should not be moved
                If correctLayerId <> -1 Then
                    listsOfObjectsToMove.Add(correctLayerId, obj)
                End If
            End If

        Next

        theSession.SetUndoMark(Session.MarkVisibility.Visible, "Move to layer by company standards")

        Dim layerId As Integer
        Dim objsToMove() As DisplayableObject
        Do
            listsOfObjectsToMove.GetNextList(layerId, objsToMove)
            ' layerId is -1 if there are no more lists in listsOfObjectsToMove
            If layerId = -1 Then Exit Do
            workPart.Layers.MoveDisplayableObjects(layerId, objsToMove)
        Loop

        MoveSketches(workPart, sketchesOnWorkLayer, layerToClassMap)

    End Sub

    Sub MoveSketches(ByVal workPart As Part, ByVal sketchesOnWorkLayer As ArrayList, ByVal layerToClassMap As LayerToClassMap)
        ' Find the layer object for Sketch
        Dim layerObj As Object = layerToClassMap.FindLayerForNXClass("NXOpen.Sketch")
        If layerObj Is Nothing Then
            layerObj = layerToClassMap.FindLayerForUFType(NXOpen.UF.UFConstants.UF_sketch_type, NXOpen.UF.UFConstants.UF_v13_sketch_subtype)
        End If
        If layerObj Is Nothing Then Exit Sub

        ' Get the layerId and members of the LayerCategory (if any) where
        ' sketches should be moved to
        Dim layerId As Integer
        Dim layerMembers() As Integer = Nothing
        If TypeOf layerObj Is Integer Then
            layerId = CInt(layerObj)
        Else
            layerMembers = CType(layerObj, Layer.Category).GetMemberLayers()
            If layerMembers.Length = 0 Then Exit Sub
            layerId = layerMembers(0)
        End If

        Dim sketchesToMove As ArrayList = New ArrayList
        Dim sketch As Sketch

        For Each sketch In sketchesOnWorkLayer
            ' If sketches should be moved to a layer category and the sketch is already
            ' in a layer that is in the layer category, move the sketch to the layer
            ' that it is currently on.  The reason for doing this is so that the curves
            ' that are on the sketch get moved to the layer where the sketch is located.
            '
            ' Otherwise, add the sketch to sketchesToMove.  Those sketches will be
            ' moved to layerId (the first layer in the layer category).
            If Not layerMembers Is Nothing AndAlso Array.IndexOf(layerMembers, sketch.Layer) >= 0 Then
                workPart.Layers.MoveDisplayableObjects(sketch.Layer, New DisplayableObject() {sketch})
            Else
                sketchesToMove.Add(sketch)
            End If
        Next

        If sketchesToMove.Count > 0 Then
            Dim objsToMove() As DisplayableObject = sketchesToMove.ToArray(GetType(DisplayableObject))
            workPart.Layers.MoveDisplayableObjects(layerId, objsToMove)
        End If

    End Sub


End Module

