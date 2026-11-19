/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling interface to sketches.

*****************************************************************************/

#ifndef UF_MODL_SKETCH_H_INCLUDED
#define UF_MODL_SKETCH_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <uf_modl_ugopenint.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
This function can be used to redefine the tool and target objects referenced
by a relative positioning constraint of a feature.  The input parameter
constraint is the constraint whose target and tool objects have to be redefined.
All the constraints that have been applied to a feature can be obtained by
using UF_MODL_ask_constraints. Use UF_MODL_ask_constraint_type to verify the
type of constraint.

Parameters tangent2arc1 (target qualifier) and tangent2arc2 (tool_qualifier)
allow settings for specifying which end point of the tool and target objects
to use. Use UF_MODL_ask_edge_verts to determine the order of the end points
for tool or target objects that are edges.

Some features can be positioned using the centerline of the feature.  You may i
use the centerline of a feature by passing in a NULL_TAG as the tool object.
The centerline must be qualified as either the horizontal or vertical
centerline, using the first or last endpoint. The following features allow the
centerline to be used as a tool edge: Slot, Groove, Rectangular Pad, and
Rectangular Pocket. The Groove feature has only a vertical centerline.

Environment: Internal and External.
See Also:
 UF_MODL_ask_constraints
 UF_MODL_ask_constraint_type
 UF_MODL_reattach_dir_ref
 UF_MODL_reattach_target_face
 UF_MODL_reattach_thru_faces
 UF_MODL_reattach_tool_face

History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_redefine_rpo_constraint
(
    tag_t constraint,  /* <I>
                       the constraint being redefined
                       */
    tag_t eid_target,  /* <I>
                       the new target object
                       */
    int tangent2arc1,  /* <I>
                       the target qualifier
                       */
    tag_t eid_tool,    /* <I>
                       the new tool object
                       */
    int tangent2arc2   /* <I>
                       the new tool qualifier
                       */
);

/****************************************************************************
Registers a routine for relative positioning. This allows you to register
a routine into the Open API environment so that you can
constrain a feature during creation time. Subsequently, every time a
form feature is created, this registered routine is called.
To register a routine named user_rpo_routine(), the call is:

UF_MODL_register_rpo_routine(user_rpo_routine)
where user_rpo_routine is defined as:
int user_rpo_routine(tag_t obj_id)

Calling this function will prevent an internal Open API shared library from
being unloaded, and overrides the setting of the user supplied function, 
ufusr_ask_unload.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_register_rpo_routine(
UF_MODL_rpo_f_p_t routine  /* <I>
                           Routine name. You define the routine.  The system
                           calls the routine like this:
                                   error =  routine((tag_t) obj_id)
                           where obj_id is the new feature that was just
                           created. Therefore, you should define the  routine
                           like this:
                                   int routine(tag_t obj_id)
                           and the routine returns an error if it failed. If the
                           returned error is != 0, then the new form feature is
                           deleted and an error is returned..
                           */
);

/****************************************************************************
Returns the currently specified relative position operation (RPO)
routine as a function pointer of type UF_MODL_rpo_f_p_t.  If no
routine is specified, zero is returned.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rpo_routine(
UF_MODL_rpo_f_p_t * user_rpo_routine  /* <I>
                                      Function pointer to the currently
                                      specified relative
                                      position operation (RPO) routine.
                                      */
);

/****************************************************************************
Unregisters a routine for relative positioning.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unregister_rpo_routine( void );

/******************************************************************************
Returns expressions and expression descriptions related to supplied
features rpo dimensions.

Environment: Internal  and  External
See Also:
History:Original Release was in V14.0. V15.0 change: This function was
     renamed from UF_MODL_ask_rpo_desc_of_frec to UF_MODL_ask_rpo_desc_of_feat.

 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rpo_desc_of_feat(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier of created rectangular groove
                       */
int * number_of_exps ,/* <O>
                      Number of expressions returned
                      */
char *** descriptions ,/* <OF,len:number_of_exps> 
                       Array of expression descriptions related to features
                       rpo dimensions. Use UF_free_string_array to deallocate
                       memory when done.
                       */
tag_t ** exps  /* <OF,len:number_of_exps> 
               Array of object identifiers to expressions related to
               features rpo dimensions. Use UF_free to deallocate
               memory when done.
               */
);

/******************************************************************************
Use UF_MODL_ask_rpo_desc_of_feat instead.
Returns expressions and expression descriptions related to supplied
features rpo dimensions.

Environment: Internal  and  External
See Also:
History:Original Release was in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rpo_desc_of_frec(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier of created rectangular groove
                       */
int * number_of_exps ,/* <O>
                      Number of expressions returned
                      */
char *** descriptions ,/* <OF,len:number_of_exps>
                               Array of expression descriptions related to features
                               rpo dimensions. Use UF_free_string_array to deallocate
                               memory when done.
                       */
tag_t ** exps  /* <OF,len:number_of_exps>
               Array of object identifiers to expressions related to
               features rpo dimensions. Use UF_free to deallocate
               memory when done.
               */
);

/******************************************************************************
Gets the sketch feature associated with the sweep.  When a sketch is attached
to the plane of the WCS, it is not a feature, hence this function returns a
NULL_TAG.

Environment: Internal  and  External
See Also:
 UF_MODL_reattach_target_face
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sketch_of_sweep(
tag_t sweep_obj_id ,/* <I>
                    The sweep feature object identifier
                    */
tag_t * sketch_obj_id  /* <O>
                       Pointer to the object identifier of the sketch feature
                       associated with the sweep
                       */
);

/********************************************************************
The routine UF_MODL_ask_constraints has a single feature as input,
and returns a list of constraints. The list can be manipulated by the
UF_MODL_*_list_* routines.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_constraint_type
 UF_MODL_delete_list
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_constraints(
tag_t feature ,/* <I>
               Identifier for the feature.
               */
uf_list_p_t * constraints  /* <OF,free:UF_MODL_delete_list>
                           Address of pointer to the list of constraints for
                           that feature. Use UF_MODL_delete_list to free space
                           allocated for this linked list.
                           */
);

/********************************************************************
The routine UF_MODL_ask_constraint_type returns a character
string describing the type of constraint that was input.
The appropriate constraint inquiry routine to ask for the constraint
values.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_angle_edge
 UF_MODL_ask_horz_dime
 UF_MODL_ask_para_dist
 UF_MODL_ask_para_edge
 UF_MODL_ask_perp_dist
 UF_MODL_ask_vert_dime
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_constraint_type(
tag_t constraint ,/* <I>
                  Constraint to inquire on.
                  */
char ** type  /* <OF>
              Pointer to the character string describing the
              constraint. Use UF_free to deallocate memory
              when done.
              */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_SKETCH_H_INCLUDED */
