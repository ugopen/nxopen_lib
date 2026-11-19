/*****************************************************************************
             Copyright (c) 2000-2004 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open API modeling interface to sketches.

*****************************************************************************/

#ifndef UF_MODL_UGOPENINT_H_INCLUDED
#define UF_MODL_UGOPENINT_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libugopenint_exports.h>
#include <uf_modl_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/*******************************************************************************
Opens the default rpo menu.

Use UF_MODL_default_rpo_menu() to position new style UDF features and during
copy/paste of features.

This function cannot be used to edit positioning of features that are
automatically booleaned to a target solid.

Environment:Internal
See Also:
History: This function was originally released in V15.0.
******************************************************************************/
extern UGOPENINTEXPORT int UF_MODL_default_rpo_menu(
tag_t feature_eid /* <I>
                  Feature to reposition
                  */
);/* <NEC> */

/*******************************************************************************
Opens the default rpo menu for udf instantiation or feature paste.
This function should only be used to position new style UDFs or during
copy/paste of features.

Environment:Internal
See Also:
History: This function was originally released in V17.0.2.
******************************************************************************/
extern UGOPENINTEXPORT int UF_MODL_udf_rpo_menu(
tag_t feature_eid /* <I>
                  Feature to reposition
                  */
);/* <NEC> */

/****************************************************************************
Creates relative positioning constraints.

This function is for internal Open API mode only.  Parameters
target_qualifier[] and tool_qualifier[] allow settings for
specifying which end point of an edge to use. Use
UF_MODL_ask_edge_verts to determine the order of the end points.

For features that are automatically booleaned into the target, this
function should only be called from within a rpo routine as
specified by UF_MODL_register_rpo_routine.

There are three constraint types that are present interactively that do
not appear in the constraint_array[ ]: Point Onto Point, Point Onto
Line, and Line Onto Line.

Point Onto Point - Can require one or two constraint types depending on
what you constrain. For example, to constrain a circular pad onto
a circular cylinder, use PARA_DIST_PARMS and set the constraint value to
"0.0". However, if you wish to constrain rectangular features you may need
to use HORZ_DIST_PARMS and VERT_DIST_PARMS and set both constraint values
to "0.0".

Point Onto Line - Use PERP_DIST_PARMS and set the constraint value to "0.0".

Line Onto Line -  Use PARA_EDGE_PARMS and set the constraint value to "0.0"

When a target or tool edge is an arc, the position must be qualified as
either the arc center or the closest tangency point on the arc.  When the
edge is not an arc, the position must be qualified as either the first or
last endpoint of the edge.

Some features can be positioned using the centerline of the feature.
You may use the centerline of a feature by passing in a NULL_TAG
as the tool edge. The centerline must be qualified as either the
horizontal or vertical centerline, using the first or last endpoint. The
following features allow the centerline to be used as a tool edge: Slot,
Groove, Rectangular Pad, Rectangular Pocket. The Groove feature
has only a vertical centerline.

Environment: Internal
See Also:
 UF_MODL_ask_edge_verts

History: In V13.0, the tangent2arc1 and tangent2arc2 parameters were
         renamed to target_qualifier and tool_qualifier respectively and were
         given string defined constants for values. The object_id_tool was
         modified to accept a NULL_TAG for centerline.
 ***************************************************************************/
extern UGOPENINTEXPORT int UF_MODL_create_rpo_constraints(
tag_t feature_obj_id ,/* <I>
                      Feature to be constrained
                      */
tag_t horz_dir_obj_id ,/* <I>
                       Horizontal direction.
                       */
tag_t vert_dir_obj_id ,/* <I>
                       Vertical direction (if horz_dir_obj_id == 0).
                       */
tag_t obj_id_target[] ,/* <I,len:num_of_constrnts>
                       Array of target edges.
                       */
int target_qualifier[] ,/* <I,len:num_of_constrnts>
                        Array of flags used to qualify the position on each
                        target edge. Valid flags are:
                                UF_MODL_ARC_CENTER
                                UF_MODL_ARC_TANGENT
                                UF_MODL_ENDPOINT_1
                                UF_MODL_ENDPOINT_2
                        */
tag_t obj_id_tool[] ,/* <I,len:num_of_constrnts>
                     Array of tool edges (NULL_TAG for centerline).
                     */
int tool_qualifier[] ,/* <I,len:num_of_constrnts>
                      Array of flags used to qualify the position on each
                      tool edge. Valid flags are:
                      UF_MODL_ARC_CENTER
                      UF_MODL_ARC_TANGENT
                      UF_MODL_ENDPOINT_1
                      UF_MODL_ENDPOINT_2
                      UF_MODL_HORZ_CENTERLINE_PNT_1
                      UF_MODL_HORZ_CENTERLINE_PNT_2
                      UF_MODL_VERT_CENTERLINE_PNT_1
                      UF_MODL_VERT_CENTERLINE_PNT_2
                      */
char * constraint_value[] ,/* <I,len:num_of_constrnts>
                           Array of constraint values.
                           */
char * constraint_array[] ,/* <I,len:num_of_constrnts>
                           Array of constraint type:
                           "ANGL_EDGE_PARMS",
                           "HORZ_DIST_PARMS",
                           "VERT_DIST_PARMS",
                           "PARA_DIST_PARMS",
                           "PARA_EDGE_PARMS" ,
                           "PERP_DIST_PARMS"
                           */
int num_of_constrnts  /* <I>
                      Number of constraints.
                      */
);


/******************************************************************************
Set the reference object and location for RPO operations. This function can be used to
control where a form feature will be positioned, if RPO is needed for the feature.
For example, if it is called before UF_MODL_create_instantiated_udf, the system will
position the new UDF instance at the given place.

Environment: Internal  and  External
See Also:
History: V17.0
 ******************************************************************************/
extern UGOPENINTEXPORT int  UF_MODL_set_rpo_refernce
(
     tag_t reference,       /* <I>
                            the tag of the reference object, which can be a face or edge
                            */
     double point[3],       /* <I>
                            the point to position a feature
                            */
     int flip               /* <I>
                            flip the direction or not, only valid for edge
                            */
);

/*******************************************************************************
Create a default UDF mapping tool and let users to select mapping objects at
instantiation.

Environment: Internal
History: This function was originally released in NX3.
******************************************************************************/
extern UGOPENINTEXPORT int UF_MODL_udf_default_insert_mapping_tool
(
    tag_t                    udf_define_tag,       /* <I>   UDF definition feature */
    UF_MODL_udf_ref_data_p_t ref_data              /* <I/O> UDF parent data */
);

/*******************************************************************************
Create a default UDF mapping tool and let users to select mapping objects at
editing.

Environment: Internal

History: This function was originally released in NX3.
******************************************************************************/
extern UGOPENINTEXPORT int UF_MODL_udf_default_edit_mapping_tool
(
    tag_t                    udf_insert_tag,       /* <I>   UDF instantiated feature */
    UF_MODL_udf_ref_data_p_t ref_data              /* <I/O> UDF parent data */
);


/*******************************************************************************
Function Description :  This function will create a user interface
                        dialog to allow users to choose a Shape Pattern from a thumbnail list
Return: Error code
Environment: Internal & External
See Also:
 UF_MODL_shape_pattern_init_client_data
 UF_MODL_shape_pattern_free_client_data

History: Originally released in NX503
*******************************************************************************/
extern UGOPENINTEXPORT int UF_MODL_shape_pattern_create_dialog
(
    UF_MODL_shape_pattern_client_dialog_data_p_t pClientData,   /*<I/O> Client Data for Shape Pattern UI*/
    int *response                                               /*<O> UI response: UF_UI_OK or UF_UI_CANCEL*/
);

/*******************************************************************************
The following function will initialize the client data for shape pattern
which is used for UF_MODL_shape_pattern_create_dialog

Return: Error code
Environment: Internal & External
See Also:
 UF_MODL_shape_pattern_free_client_data
History: Originally released in NX503
*******************************************************************************/
extern UGOPENINTEXPORT int UF_MODL_shape_pattern_init_client_data
(
    UF_MODL_shape_pattern_client_dialog_data_p_t pClientData /*<I/O> Shape Pattern data structure
                                                                     to be initialized*/
);

/*******************************************************************************
The following function will free the client data for shape pattern
which is used for UF_MODL_shape_pattern_create_dialog

Return: Error code
Environment: Internal & External
See Also:
 UF_MODL_shape_pattern_init_client_data

History: Originally released in NX503
*******************************************************************************/

extern UGOPENINTEXPORT int UF_MODL_shape_pattern_free_client_data
(
    UF_MODL_shape_pattern_client_dialog_data_p_t pClientData /*<I> Shape Pattern data structure
                                                                   to be freed*/
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_UGOPENINT_H_INCLUDED */
