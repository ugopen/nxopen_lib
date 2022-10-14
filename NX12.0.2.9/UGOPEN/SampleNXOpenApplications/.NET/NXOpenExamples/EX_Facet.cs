/*=============================================================================

                    Copyright (c) 2004 UGS PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Example for Wrapped UFUNC (NXOpen.NET)
/*  */
using System;
using System.IO;
using System.Runtime.InteropServices;
using NXOpen;
using NXOpen.UF;

namespace NetExample
{
    /// This example will create EX_Facet.prt, EX_Facet.log files
    /// For each facet it prints the position, vertex normal, and vertex convexity for each vertex.
    /// The program prints the report to the log file called "EX_Facet.log".
    public class EX_Facet
    {
        public static FileStream fs; 
        public static StreamWriter w;
        public static UFSession theUfSession;
        private static Session theSession;


        public const int UF_FACET_PARAM_VERSION_CURR = -2;
        public const int UF_FACET_NULL_FACET_ID = -1;
        public const int UF_FACET_IS_CONVEX = -1;
        public const int UF_FACET_IS_CONCAVE = 1;

        static void UFInitParams(ref UFFacet.Parameters __params) 
        {
        
            (__params).version                     = UF_FACET_PARAM_VERSION_CURR;
            (__params).max_facet_edges             = 3;
            (__params).specify_surface_tolerance   = false;
            (__params).surface_dist_tolerance      = 0.0;
            (__params).surface_angular_tolerance   = 0.0;
            (__params).specify_curve_tolerance     = false;
            (__params).curve_dist_tolerance        = 0.0;
            (__params).curve_angular_tolerance     = 0.0;
            (__params).curve_max_length            = 1000.0;
            (__params).specify_convex_facets       = true;
            (__params).specify_max_facet_size      = false;
            (__params).max_facet_size              = 0.0;
            (__params).number_storage_type         = 1;
            (__params).specify_parameters          = false;
            (__params).specify_view_direction      = false;
            (__params).silh_view_direction         = new double[3];
            (__params).silh_view_direction[0]      = 0.0;
            (__params).silh_view_direction[1]      = 0.0;
            (__params).silh_view_direction[2]      = 1.0;
            (__params).silh_chord_tolerance        = 0.0;
            (__params).store_face_tags             = false;
        } 
        
        static int example1( out Tag new_faceted_model )
        {
            //int          ifail;
            
            double[] corner_point= new double[3];
            string[]     edge_lengths = { "10", "30", "40" };
            Tag         block_feature_tag;
            Tag         block_tag;
            Tag         faceted_model;
            bool         up_to_date = true;
            Tag         blend_feature;
            //UfList       edge_list; // = null;
            Tag[]       edge_list;
            Tag         tag_of_solid;
            int          i;
            Tag[] facet_models;
            int          n_facet_models;
            UFFacet.Parameters faceting_params = new UFFacet.Parameters();
            new_faceted_model = Tag.Null;
            
            
            corner_point[0] = 0.0;
            corner_point[1] = 0.0;
            corner_point[2] = 0.0;
            theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign,
                corner_point,
                edge_lengths,
                out block_feature_tag );
            theUfSession.Modl.AskFeatBody(block_feature_tag, out block_tag );
            UFInitParams(ref faceting_params);
            
            theUfSession.Facet.AskDefaultParameters(out faceting_params) ;

            theUfSession.Facet.FacetSolid(block_tag,
                ref faceting_params,
                out faceted_model );
            if ( faceted_model != Tag.Null )
            {
                theUfSession.Facet.AskSolidOfModel(faceted_model, out tag_of_solid );
                if ( block_tag != tag_of_solid )
                {
                    w.WriteLine("**ERR: Failed find solid from facet model\n" );
                    return 1;
                } 
                theUfSession.Facet.AskModelsOfSolid(block_tag,
                    out n_facet_models,
                    out facet_models );
                /*
                   Just check that the association between the solid and 
                   the new faceted model has been established.
                */
                for ( i=0 ; i < n_facet_models ; i++ )
                {
                    if ( facet_models[i] == faceted_model )
                    {
                        w.WriteLine("Faceted model is attached to solid\n" );
                    }
                }
                //UF_free( facet_models );
                /*
                    Now blend all of the edges of the block.
                */
                theUfSession.Modl.AskBodyEdges(block_tag, out edge_list );
                theUfSession.Modl.CreateBlend("2.0", edge_list, 
                    0, 0, 0, 0.0,
                    out blend_feature );
                
                /**************************************/
                //This method is not mapped...//
                /**************************************/
                //UF_MODL_delete_list( &edge_list );

                theUfSession.Modl.Update();
                
                theUfSession.Facet.IsModelUpToDate(faceted_model,
                    out up_to_date );
                if ( up_to_date )
                {
                    w.WriteLine("**ERR: Faceted model is up to date\n" );
                    return 1;
                }
                theUfSession.Facet.AskModelParameters(faceted_model,
                    out faceting_params );
                /*
                   Set the number of sides for facets to four and use that
                   when refaceting the solid.
                */
                faceting_params.max_facet_edges = 4;
                
                theUfSession.Facet.UpdateModel(faceted_model,
                    ref faceting_params );

                theUfSession.Facet.IsModelUpToDate(faceted_model,
                    out up_to_date );
                if (!up_to_date)
                {
                    w.WriteLine("**ERR: Model is not up to date\n" );
                    return 1;
                }
                /*
                    Finally, disassociate the faceted model from
                    the generating solid.
                */
                theUfSession.Facet.DisassocFromSolid(faceted_model );
                new_faceted_model = faceted_model;
            }
            else
            {
                return 1;
            }
            return 0;
        }

        static int example3( Tag model )
        {
            int          num_facets_in_model;
            int          max_vertices_in_facet;
            int          vertex_array_size;
            
            double[]     plane_normal = new double[3];
            double       d_coefficient;
            int          facet_id;
            int          facet_no = 0;
            int          i;
            
  
            theUfSession.Facet.AskNFacetsInModel(model, out num_facets_in_model );
            theUfSession.Facet.AskMaxFacetVerts(model, out max_vertices_in_facet );

            double doubleVariable=0.0;
            vertex_array_size = 3* max_vertices_in_facet* Marshal.SizeOf(doubleVariable);
            double[,]    facet_vertices = new double[vertex_array_size, 3];
            double[,]    facet_normals = new double[vertex_array_size, 3];

            w.WriteLine("Model contains {0} facets\n", num_facets_in_model );
            w.WriteLine("Maxmium vertices in any facet is {0}\n",
                max_vertices_in_facet );
            facet_id = UF_FACET_NULL_FACET_ID;

            theUfSession.Facet.CycleFacets(model, ref facet_id );
            while ( facet_id != UF_FACET_NULL_FACET_ID )
            {
                int      num_vertices_in_facet;
                int      verts_in_facet;
                bool  facet_convexity;
                theUfSession.Facet.AskNumVertsInFacet(model, facet_id,
                    out num_vertices_in_facet );
                                        
                w.WriteLine("UFFacet {0} has {1} vertices\n", 
                    facet_no++, num_vertices_in_facet );
                theUfSession.Facet.AskPlaneEquation(model,
                    facet_id, 
                    plane_normal,
                    out d_coefficient
                    );
                w.WriteLine(" UFFacet normal ({0}, {1}, {2}) d_coeff {3}\n",
                    plane_normal[0], plane_normal[1],
                    plane_normal[2], d_coefficient );
                theUfSession.Facet.IsFacetConvex(model,
                    facet_id,
                    out facet_convexity );
                w.WriteLine(" UFFacet {0} convex\n", 
                    (facet_convexity) ? "IS" : "IS NOT" );
                theUfSession.Facet.AskVerticesOfFacet(model, 
                    facet_id,
                    out verts_in_facet,
                    facet_vertices
                    );
                theUfSession.Facet.AskNormalsOfFacet(model, 
                    facet_id,
                    out verts_in_facet,
                    facet_normals
                    );
                for ( i=0 ; i < num_vertices_in_facet ; i++ )
                {
                    int vertex_convexity;
                    w.WriteLine("  Vertex {0}: ({1}, {2}, {3})\n",
                        i, facet_vertices[i,0], 
                        facet_vertices[i,1], 
                        facet_vertices[i,2] );
                    w.WriteLine("    Normal ({0}, {1}, {2})\n",
                        facet_normals[i,0],
                        facet_normals[i,1],
                        facet_normals[i,2] );
                    theUfSession.Facet.AskVertexConvexity(model,
                        facet_id,
                        i,
                        out vertex_convexity );
                    w.WriteLine("    Vertex convexity = {0}\n",
                        (vertex_convexity == UF_FACET_IS_CONVEX)  ?
                        "IS CONVEX" :
                        (vertex_convexity == UF_FACET_IS_CONCAVE) ?
                        "IS CONCAVE" :
                        "CONVEXITY IS NOT DETERMINED"
                        );
                }
                theUfSession.Facet.CycleFacets(model, ref facet_id );
            }
            return 0;
        }
        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();
            fs = new FileStream("EX_Facet.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Facet.prt") ) 
            {
                w.WriteLine("Remove EX_Facet.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Facet.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                //theUfSession..Initialize();
                /*
                First create a UFPart in which we will initially create a
                block.
            */
                Tag         part_tag;
                theUfSession.Part.New("EX_Facet",    1 , out part_tag );    
                theUfSession.Assem.SetWorkPart(part_tag);
                int retcod;
                Tag faceted_model;
                retcod = example1(out faceted_model );
                if ( retcod == 0 )
                {
                    retcod = example3( faceted_model );
                }
                theUfSession.Modl.Update();
                theUfSession.Part.Save();
                // theUfSession..Terminate();
            }
            catch(NXException e)
            {   
                w.WriteLine("Exception is: {0}", e.Message);
            }
            w.WriteLine("End of Log File");
            w.Close();

        }
        public static int GetUnloadOption(string dummy)
        {
            return UFConstants.UF_UNLOAD_IMMEDIATELY;
        }
    }
}
