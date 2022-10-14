' ==================================================================================================
'
'                 Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description: Example for Wrapped UFUNC (NXOpen.NET)
'

Option Strict Off
Imports System
Imports System.Math
Imports System.IO
Imports System.Runtime.InteropServices
Imports NXOpen
Imports NXOpen.UF

Module EX_Facet

    Dim testName As String = "EX_Facet"
    Dim theSession As Session
    Dim theUfSession As UFSession
    Dim stream As StreamWriter

    Dim UF_FACET_PARAM_VERSION_CURR As Integer = -2
    Dim UF_FACET_NULL_FACET_ID As Integer = -1
    Dim UF_FACET_IS_CONVEX As Integer = -1
    Dim UF_FACET_IS_CONCAVE As Integer = 1

    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        stream = New StreamWriter(testName + ".log")

        Dim prtFileName As String = New String(testName + ".prt")
        Dim prtFile As FileInfo = New FileInfo(prtFileName)
        prtFile = New FileInfo(prtFileName)

        stream.WriteLine("Log Entry : ")
        stream.WriteLine("--Log entry goes here--")

        If prtFile.Exists() Then
            stream.WriteLine("Remove " + prtFileName + " EX_Curve_CreateArc.prt file from <Project Folder> !!")
            stream.WriteLine(prtFileName + " already exists. !!")
            stream.WriteLine("End of Log File")
            stream.Close()
            Return
        End If

        Dim nError As Integer = Execute(stream, theUfSession)
        stream.WriteLine("End of Log File")
        stream.Close()
    End Sub

    Sub UFInitParams(ByRef _params As UFFacet.Parameters)
        Dim silh_view_direction() As Double = {0.0, 0.0, 1.0}
        _params.version = UF_FACET_PARAM_VERSION_CURR
        _params.max_facet_edges = 3
        _params.specify_surface_tolerance = False
        _params.surface_dist_tolerance = 0.0
        _params.surface_angular_tolerance = 0.0
        _params.specify_curve_tolerance = False
        _params.curve_dist_tolerance = 0.0
        _params.curve_angular_tolerance = 0.0
        _params.curve_max_length = 1000.0
        _params.specify_convex_facets = True
        _params.specify_max_facet_size = False
        _params.max_facet_size = 0.0
        _params.number_storage_type = 1
        _params.specify_parameters = False
        _params.specify_view_direction = False
        _params.silh_view_direction = silh_view_direction
        _params.silh_chord_tolerance = 0.0
        _params.store_face_tags = False
    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As UFSession) As Integer
        Dim PartTag As Tag
        Dim units As Integer = UFConstants.ENGLISH
        Dim PartName As String

        theUfSession.Part.[New](testName, units, PartTag)
        theUfSession.Part.AskPartName(PartTag, PartName)
        'stream.WriteLine("New Part File Created :- " + PartName)

        theUfSession.Assem.SetWorkPart(PartTag)

        Dim retcod As Integer
        Dim faceted_model As Tag

        retcod = example1(faceted_model)

        If retcod = 0 Then
            retcod = example3(faceted_model)
        End If
        theUfSession.Modl.Update()
        theUfSession.Part.Save()
    End Function

    Function example1(ByRef new_faceted_model As Tag) As Integer
        Dim corner_point As Double() = {0.0, 0.0, 0.0}
        Dim edge_lengths As String() = {"10", "30", "40"}
        Dim block_feature_tag As Tag
        Dim block_tag As Tag
        Dim faceted_model As Tag
        Dim up_to_date As Boolean = True
        Dim blend_feature As Tag
        Dim edge_list As Tag()
        Dim tag_of_solid As Tag
        Dim i As Integer
        Dim facet_models As Tag()
        Dim n_facet_models As Integer
        Dim faceting_params As UFFacet.Parameters = New UFFacet.Parameters

        new_faceted_model = Tag.Null

        theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign, corner_point, edge_lengths, block_feature_tag)
        theUfSession.Modl.AskFeatBody(block_feature_tag, block_tag)
        UFInitParams(faceting_params)
        theUfSession.Facet.AskDefaultParameters(faceting_params)
        theUfSession.Facet.FacetSolid(block_tag, faceting_params, faceted_model)

        If faceted_model <> Tag.Null Then
            theUfSession.Facet.AskSolidOfModel(faceted_model, tag_of_solid)
            If block_tag <> tag_of_solid Then
                stream.WriteLine("**ERR: Failed find solid from facet model")
                stream.WriteLine()
                Return 1
            End If
            theUfSession.Facet.AskModelsOfSolid(block_tag, n_facet_models, facet_models)

            ' Just check that the association between the solid and 
            ' the new faceted model has been established.
            For i = 0 To (n_facet_models - 1)
                If facet_models(i) = faceted_model Then
                    stream.WriteLine("Faceted model is attached to solid")
                    stream.WriteLine()
                End If
            Next i

            ' Now blend all of the edges of the block.
            theUfSession.Modl.AskBodyEdges(block_tag, edge_list)
            theUfSession.Modl.CreateBlend("2.0", edge_list, 0, 0, 0, 0.0, blend_feature)

            '**************************************
            ' This method is not mapped...
            '**************************************
            'UF_MODL_delete_list(&edge_list)

            theUfSession.Modl.Update()
            theUfSession.Facet.IsModelUpToDate(faceted_model, up_to_date)

            If up_to_date = True Then
                stream.WriteLine("**ERR: Faceted model is up to date")
                stream.WriteLine()
                Return 1
            End If

            theUfSession.Facet.AskModelParameters(faceted_model, faceting_params)

            'Set the number of sides for facets to four and use that
            'when refaceting the solid.
            faceting_params.max_facet_edges = 4
            theUfSession.Facet.UpdateModel(faceted_model, faceting_params)
            theUfSession.Facet.IsModelUpToDate(faceted_model, up_to_date)

            If up_to_date <> True Then
                stream.WriteLine("**ERR: Model is not up to date")
                stream.WriteLine()
                Return 1
            End If

            'Finally, disassociate the faceted model from
            'the generating solid.

            theUfSession.Facet.DisassocFromSolid(faceted_model)
            new_faceted_model = faceted_model
        Else
            Return 1
        End If

        Return 0
    End Function
    Function example3(ByVal model As Tag) As Integer

        Dim num_facets_in_model As Integer = 0
        Dim max_vertices_in_facet As Integer = 0
        Dim vertex_array_size As Integer = 0
        Dim plane_normal As Double() = {0, 0, 0}
        Dim d_coefficient As Double = 0
        Dim facet_id As Integer = 0
        Dim facet_no As Integer = 0
        Dim i As Integer = 0
        Dim j As Integer = 0

        theUfSession.Facet.AskNFacetsInModel(model, num_facets_in_model)
        theUfSession.Facet.AskMaxFacetVerts(model, max_vertices_in_facet)

        stream.WriteLine("Model contains {0} facets ", num_facets_in_model)
        stream.WriteLine()
        stream.WriteLine("Maxmium vertices in any facet is {0}", max_vertices_in_facet)
        stream.WriteLine()
        facet_id = UF_FACET_NULL_FACET_ID
        theUfSession.Facet.CycleFacets(model, facet_id)

        While facet_id <> UF_FACET_NULL_FACET_ID
            Dim num_vertices_in_facet As Integer = 0
            Dim verts_in_facet As Integer = 0
            Dim facet_convexity As Boolean = 0

            theUfSession.Facet.AskNumVertsInFacet(model, facet_id, num_vertices_in_facet)
            stream.WriteLine("UFFacet {0} has {1} vertices", facet_no, num_vertices_in_facet)
            facet_no = facet_no + 1
            stream.WriteLine()
            theUfSession.Facet.AskPlaneEquation(model, facet_id, plane_normal, d_coefficient)
            stream.WriteLine(" UFFacet normal ({0}, {1}, {2}) d_coeff {3}", plane_normal(0).ToString("N10"), plane_normal(1).ToString("N10"), plane_normal(2).ToString("N10"), d_coefficient.ToString("N10"))
            stream.WriteLine()

            theUfSession.Facet.IsFacetConvex(model, facet_id, facet_convexity)
            Dim facet_convexity_value As String
            If facet_convexity = True Then
                facet_convexity_value = "IS"
            Else
                facet_convexity_value = "IS NOT"
            End If
            stream.WriteLine(" UFFacet {0} convex", facet_convexity_value)
            stream.WriteLine()

            Dim facet_vertices(num_vertices_in_facet, 2) As Double
            Dim facet_normals(num_vertices_in_facet, 2) As Double

            For i = 0 To (num_vertices_in_facet - 1)
                For j = 0 To 2
                    facet_vertices(i, j) = 0
                    facet_normals(i, j) = 0
                Next j
            Next i

            theUfSession.Facet.AskVerticesOfFacet(model, facet_id, num_vertices_in_facet, facet_vertices)
            theUfSession.Facet.AskNormalsOfFacet(model, facet_id, num_vertices_in_facet, facet_normals)

            For i = 0 To (num_vertices_in_facet - 1)
                Dim vertex_convexity As Integer
                stream.WriteLine("  Vertex {0}: ({1}, {2}, {3})", i, facet_vertices(i, 0).ToString("N10"), facet_vertices(i, 1).ToString("N10"), facet_vertices(i, 2).ToString("N10"))
                stream.WriteLine()
                stream.WriteLine("    Normal ({0}, {1}, {2})", facet_normals(i, 0).ToString("N10"), facet_normals(i, 1).ToString("N10"), facet_normals(i, 2).ToString("N10"))
                stream.WriteLine()
                theUfSession.Facet.AskVertexConvexity(model, facet_id, i, vertex_convexity)
                Dim vertex_convexity_value As String
                If vertex_convexity = UF_FACET_IS_CONVEX Then
                    vertex_convexity_value = "IS CONVEX"
                ElseIf vertex_convexity = UF_FACET_IS_CONCAVE Then
                    vertex_convexity_value = "IS CONCAVE"
                Else
                    vertex_convexity_value = "CONVEXITY IS NOT DETERMINED"
                End If

                stream.WriteLine("    Vertex convexity = {0}", vertex_convexity_value)
                stream.WriteLine()
            Next i
            theUfSession.Facet.CycleFacets(model, facet_id)
        End While
        Return 0
    End Function
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = UFConstants.UF_UNLOAD_IMMEDIATELY
    End Function

End Module
