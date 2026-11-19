/****************************************************************************
*             Copyright (c) 1998-1999,2000 Unigraphics Solutions, Inc.
*                       Unpublished - All Rights Reserved        
*
* 
*
* Example UF_BREP program
* =======================
* 
* The source code below is a working non-trivial example of
* the UF_BREP module.  The program creates a new UG part by using UF_BREP
* to copy solid bodies and sheet bodies from an existing UG part.  For
* each solid body the program:
*      asks for the topology tree,
*      prints an indented listing of the topology tree,
*      makes a copy of the topology tree, including attached geometry,
*      and creates the solid in the new UG part.
*
* Note that for clarity the code below does not always check UG/Open
* return codes, which a real program would always check.  The code does
* not rigorously free application memory or returned UG/Open allocated
* memory.  Also for clarity the code assumes that all body occurrences 
* are loaded.
* 
* Refer to the UG/Open Manual for details on compiling and linking UG/Open
* programs.  On HP Unix the commands might be something like:
* 
*     $UGII_BASE_DIR/ugopen/ufcomp  brep_ex.c
*     $UGII_BASE_DIR/ugopen/uflink -d brep_ex
* 
* 
* The program expects a UG part name as the only argument (omit the .prt
* extension), and produces another UG part whose name has `_new' appended
* to the input file name.
* 
*     brep_ex  cube
* 
* should produce cube_new.prt from cube.prt.
* 
* 
* Brief brep_ex.c routine descriptions...
* 
* main
* ----
*     Driver program that cycles all unblanked solid and sheet bodies
*     in the input part.  For sheet bodies, brep_ex.c calls
*     UF_BREP_make_body with the first face topology.
* 
* PrintTopologyTree
* -----------------
*     Recursively traverses a topology tree to print a depth first,
*     indented topology tree listing showing the topology type name,
*     UG tag (if any), and unique tag of each topology entity.
* 
*     Example partial output for a solid body:
*         Solid, UG tag 370, unique ID 75
*             Shell, UG tag 0, unique ID 179
*                 Face, UG tag 371, unique ID 174
*                     Loop, UG tag 0, unique ID 178
*                         Fin, UG tag 0, unique ID 180
*                             Edge, UG tag 383, unique ID 170
*                                 Vertex, UG tag 0, unique ID 86
*                                 Vertex, UG tag 0, unique ID 88
*                         Fin, UG tag 0, unique ID 185
*                             Edge, UG tag 302, unique ID 162
*                                 Vertex, UG tag 0, unique ID 86
*                                 Vertex, UG tag 0, unique ID 92
*                         Fin, UG tag 0, unique ID 197
*                             Edge, UG tag 258, unique ID 116
*                                 Vertex, UG tag 0, unique ID 94
*                                 Vertex, UG tag 0, unique ID 92
*                         Fin, UG tag 0, unique ID 186
*                             Edge, UG tag 306, unique ID 83
*                                 Vertex, UG tag 0, unique ID 88
*                                 Vertex, UG tag 0, unique ID 94
* 
* CopyTopologyTree
* ----------------
*     Copies a topology tree while doing a recursive depth-first traverse.
*     For each new topology entity:
*         malloc and initialize, e.g., type, oriented child array,
*         attach the geometry from the entity in the original tree.
* 
*     Input  (see diagram below)
*         OldParentTopology  Provides oriented child orientation data.
*         OldChildTopology   Template for creating NewChildTopology.
*         ChildNdx           Which child topology to create.
*         NewParentTopology  Already malloc'd parent of NewChildTopology
*         OldChildTopology->u.user_ptr
*                            Before traversing tree, all user_ptr fields
*                            must be null pointers.
* 
*     Output  (see diagram below)
*         NewChildTopology   Malloc'd topology in new topology tree.
*         NewParentTopology  The ChildNdx'th oriented child now points to
*                            the newly malloc'd NewChildTopology.
*         OldChildTopology->u.user_ptr
*                            Topologies with multiple parents have user_ptr
*                            pointing to corresponding new child.
* 
*     Key components in copying one child topology entity within the context
*     of a topology tree:
* 
*         OldParentTopology                    NewParentTopology
*             ...                                 ...
*             children[i] ---+                    children[i] ---+
*                            |                                   |
*                            |                                   |
*                            V                                   V
*                 OldOrientedChild                    NewOrientedChild
*                     orientation   ------------------>   orientation
*                    *child ---+                         *child ---+
*                              |                                   |
*                              |                                   |
*                              V                                   V
*                     OldChildTopology                    NewChildTopology
*                         type   ------------------------->   type
*                         num_children   ----------------->   num_children
*                         children[...]                       children[]
*                         ...                                 ...
* 
*     Note that the copy topology subroutine uses the user_ptr field in the
*     UF_BREP_topology structure to avoid creating multiple output topology
*     structures for the same input topology structure.  For example, two
*     parent loop topologies, e.g., from two faces, might reference the same
*     edge topology.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <uf.h>
#include <uf_modl.h>
#include <uf_assem.h>
#include <uf_brep.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>


static void PrintTopologyTree (
    UF_BREP_topology_t  *child_topology,
    int                  tree_depth
)

{
    int  i, unique_id, grand_child_ndx;

    for (i=0; i<tree_depth; i++)  printf ("    ");
    switch (child_topology->type)
        {
        case UF_BREP_SOLID_TOPO:     printf ("Solid");    break;
        case UF_BREP_SHEET_TOPO:     printf ("Sheet");    break;
        case UF_BREP_TRIMSURF_TOPO:  printf ("Trimsurf"); break;
        case UF_BREP_SHELL_TOPO:     printf ("Shell");    break;
        case UF_BREP_FACE_TOPO:      printf ("Face");     break;
        case UF_BREP_LOOP_TOPO:      printf ("Loop");     break;
        case UF_BREP_FIN_TOPO:       printf ("Fin");      break;
        case UF_BREP_EDGE_TOPO:      printf ("Edge");     break;
        case UF_BREP_VERTEX_TOPO:    printf ("Vertex");   break;
        default:    break;
        }
    UF_BREP_ask_identifier (child_topology, &unique_id);
    printf (":  UGtag=%d, id=%d\n", child_topology->tag, unique_id);

    for (grand_child_ndx=0;
        grand_child_ndx < child_topology->num_children;
        grand_child_ndx++)
        PrintTopologyTree ( child_topology->children[grand_child_ndx].child,
                             tree_depth+1);
}


static void CopyTopologyTree (
    UF_BREP_topology_t  *OldParentTopology,
    UF_BREP_topology_t  *OldChildTopology,
    int                  ChildNdx,
    UF_BREP_topology_t  *NewParentTopology,
    UF_BREP_topology_t **NewChildTopology
)

{
    int  ChildNdx2;
    UF_BREP_topology_t  *CreatedChildTopology;

    int  StateCount;
    UF_BREP_mapping_t  *Mapping = NULL;
    UF_BREP_geometry_t  Geometry;
    UF_BREP_state_t    *States;
    UF_BREP_options_t  *AttachOptions = NULL;
    UF_BREP_orientation_t  GeomSense;

    if (OldChildTopology->u.user_ptr != NULL)
        {
        NewParentTopology->children[ChildNdx].child       = (struct UF_BREP_topology_s *)OldChildTopology->u.user_ptr;
        NewParentTopology->children[ChildNdx].orientation = OldParentTopology->children[ChildNdx].orientation;
        return;
        }

    *NewChildTopology = (UF_BREP_topology_t *) malloc (sizeof (UF_BREP_topology_t));
    (*NewChildTopology)->type         = OldChildTopology->type;
    (*NewChildTopology)->tag          = 0;
    (*NewChildTopology)->u            = OldChildTopology->u;
    (*NewChildTopology)->extension    = NULL;
    (*NewChildTopology)->num_children = OldChildTopology->num_children;
    (*NewChildTopology)->children     = NULL;
    if (OldChildTopology->num_children > 0)
        {
        (*NewChildTopology)->children =
            (UF_BREP_oriented_child_t *) malloc ((*NewChildTopology)->num_children *
                                                 sizeof (UF_BREP_oriented_child_t));
        }

    if (OldChildTopology->type == UF_BREP_FACE_TOPO    ||
        OldChildTopology->type == UF_BREP_EDGE_TOPO    ||
        OldChildTopology->type == UF_BREP_VERTEX_TOPO)
        {
        UF_BREP_ask_geometry (OldChildTopology, NULL, Mapping,
                              &Geometry, &GeomSense, &StateCount, &States);

        UF_BREP_attach_geometry (*NewChildTopology, &Geometry, GeomSense, AttachOptions,
                                 &StateCount, &States);
        UF_BREP_free_geometry_data (&Geometry, NULL);
        }

    OldChildTopology->u.user_ptr = (*NewChildTopology);
    if (OldParentTopology != NULL)
        {
        NewParentTopology->children[ChildNdx].child       = (*NewChildTopology);
        NewParentTopology->children[ChildNdx].orientation = OldParentTopology->children[ChildNdx].orientation;
        }

    for (ChildNdx2=0;  ChildNdx2 < OldChildTopology->num_children;  ChildNdx2++)
        CopyTopologyTree (OldChildTopology,
                          OldChildTopology->children[ChildNdx2].child,
                          ChildNdx2,
                         *NewChildTopology,
                         &CreatedChildTopology);
}


int main ( int   ArgC, char *ArgV[])

{
    int    PartUnits,
           Type,
           Subtype,
           SolidCount = 0,
           SheetCount = 0;
    tag_t  PartTag,
           NewPartTag,
           NewBodyTag,
           BodyTag = NULL_TAG;
    char   NewPartName[ MAX_FSPEC_BUFSIZE ];

    UF_PART_load_status_t  LoadStatus;

    UF_BREP_topology_t *TopologyRoot,
                       *NewTopologyRoot;
    int                 BrepStateCount;
    UF_BREP_state_t    *BrepStates;


    printf ("\nStarting %s...\n", ArgV[1]);  fflush (stdout);

    if (UF_initialize ())
        { printf ("UF_initialize failure...\n"); exit (1); }

    if (UF_PART_open (ArgV[1], &PartTag, &LoadStatus))
        { printf ("Error:  cannot open %s.prt\n", ArgV[1]); exit (1); }
    UF_PART_ask_units (PartTag, &PartUnits);

    strcpy (NewPartName, ArgV[1]);
    strcat (NewPartName, "_new");
    if (UF_PART_new (NewPartName, PartUnits, &NewPartTag))
        { printf ("Error:  does %s.prt already exist?\n", NewPartName);  exit (1); }

    while (1)
        {
        tag_t  ProtoTag;
        UF_OBJ_disp_props_t  DispProps;
        UF_BREP_topology_t  *MakeBodyRoot;

        UF_OBJ_cycle_objs_in_part (PartTag, UF_solid_type, &BodyTag);
        if (BodyTag == NULL_TAG)  break;

        UF_OBJ_ask_display_properties (BodyTag, &DispProps);
        UF_OBJ_ask_type_and_subtype (BodyTag, &Type, &Subtype);

        if (Subtype != UF_solid_body_subtype  ||
            DispProps.blank_status != UF_OBJ_NOT_BLANKED)  continue;

        ProtoTag = BodyTag;
        if (UF_ASSEM_is_occurrence (BodyTag))
            ProtoTag = UF_ASSEM_ask_prototype_of_occ (BodyTag);

        UF_MODL_ask_body_type (ProtoTag, &Type);
        if      (Type == UF_MODL_SOLID_BODY)  SolidCount++;
        else if (Type == UF_MODL_SHEET_BODY)  SheetCount++;
        else  continue;

        if (UF_BREP_ask_topology (BodyTag,
                                  NULL,
                                 &TopologyRoot,
                                 &BrepStateCount,
                                 &BrepStates))      continue;

        PrintTopologyTree (TopologyRoot, 0);
        CopyTopologyTree (NULL, TopologyRoot, 0, NULL, &NewTopologyRoot);

        MakeBodyRoot = NewTopologyRoot;
        if (Type == UF_MODL_SHEET_BODY)
            while (MakeBodyRoot->type != UF_BREP_FACE_TOPO)
                MakeBodyRoot = MakeBodyRoot->children[0].child;

        UF_BREP_make_body (MakeBodyRoot, &NewBodyTag, &BrepStateCount, &BrepStates);

        UF_BREP_release_topology (TopologyRoot, NULL);
        UF_BREP_release_topology (NewTopologyRoot, (void (*) (void *)) &free);
        }

    UF_PART_save();
    UF_PART_close (NewPartTag, 0, 1);
    UF_PART_close (PartTag, 0, 1);

    UF_terminate ();
    printf ("Attempted solid copies:  %d\n", SolidCount);
    printf ("Attempted sheet copies:  %d\n", SheetCount);
    return (0);
}
