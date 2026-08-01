Imports System
Imports NXOpen
Imports NXOpen.Fields

' NX Open example to show how to cycle through the fields in
' a part using the NX Open UF object cycling methods
Module NXOpenSample
    Sub Main ()
        Dim theSession = Session.GetSession()
        Dim baseWorkPart = theSession.Parts.BaseWork
        Dim workSimPart = CType(baseWorkPart, NXOpen.CAE.SimPart)
        ' Field objects are only on sim parts
        If workSimPart Is Nothing
            Return
        End If
        
        Dim fields = GetFields(workSimPart)

        For Each field In fields
            Guide.InfoWriteLine(field.Name)
        Next field

    End Sub
    
    Function GetFields (simPart As NXOpen.CAE.SimPart) As Field()
        ' Use a generic list collection of Fields to store fields as we find them
        Dim fields As New System.Collections.Generic.List(Of Field)
        Dim ufs = NXOpen.UF.UFSession.GetUFSession()
        
        ' Cycle through objects in part file to find fields (UF_part_field_type)
        ' Initialize search with a null tag
        Dim objTag = Tag.Null
        ufs.Obj.CycleObjsInPart(simPart.Tag, NXOpen.UF.UFConstants.UF_part_field_type, objTag)
        ' Use While loop to cycle through objects. 
        ' If cycling function returns a null tag, search has ended.
        While (objTag <> Tag.Null)
            Dim fieldType, fieldSubtype As Integer
            ufs.Obj.AskTypeAndSubtype(objTag, fieldType, fieldSubtype)
            If fieldSubType = NXOpen.UF.UFConstants.UF_part_field_formula_subtype Or
                fieldSubType = NXOpen.UF.UFConstants.UF_part_field_expression_subtype Or
                fieldSubType = NXOpen.UF.UFConstants.UF_part_field_table_subtype Or
                fieldSubType = NXOpen.UF.UFConstants.UF_part_field_link_subtype Or
                fieldSubType = NXOpen.UF.UFConstants.UF_part_field_links_table_subtype Or
                fieldSubType = NXOpen.UF.UFConstants.UF_part_field_reference_subtype Then
                Dim field = CType(NXOpen.Utilities.NXObjectManager.Get(objTag),Field)
                If field.IsUserField Then
                    fields.Add(field)
                End If
            End If
            ' Cycle through objects in part file to find next object of given type
            ufs.Obj.CycleObjsInPart(simPart.Tag, NXOpen.UF.UFConstants.UF_part_field_type, objTag)
        End While
        ' Convert fields stored in list to an array of fields before returning 
        Return fields.ToArray()
    End Function
End Module
