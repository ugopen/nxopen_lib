/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about slots.

*****************************************************************************/

#ifndef UF_MODL_SLOTS_H_INCLUDED
#define UF_MODL_SLOTS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
Creates a ball slot feature using an origin, tool axis, slot direction,
ball diameter, depth, and length. One of two methods of creation is
taken depending on whether you want a thru slot or not.

  1. If you want a defined distance, then input the distance and
     placement face (face_li). Also, set the value of face_t1 and face_t2
     to zero.
  2. If you want to have the slot thru from one face to another, then
     supply the placement face and the two faces from which to
     measure the slot distance.

The output of this function is the object identifier of the ball slot.

The "Face for the RPO constraint" parameter, face_li, can accept a datum plane.
You can pass in the tag of the datum plane feature or datum plane body. For
relative datums the parent body is used as the target. For an absolute datum
the target body must be set by calling UF_MODL_active_part.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_ball_slot(
double  location[3] ,/* <I>
                     Ball slot location.
                     */
double  tool_axis[3] ,/* <I>
                      Ball slot tool axis.
                      */
double  direction[3] ,/* <I>
                      Ball slot direction.
                      */
char * width ,/* <I>
              Ball slot width.
              */
char * depth ,/* <I>
              Ball slot depth.
              */
char * distance ,/* <I>
                 Ball slot distance.
                 */
tag_t  face_li ,/* <I>
                Face for the RPO constraint.
                */
tag_t  face_t1 ,/* <I>
                Face for thru face 1.
                */
tag_t  face_t2 ,/* <I>
                Face for thru face 2.
                */
tag_t * feature_tag  /* <O>
                     Feature object identifier of created ball slot
                     */
);

/******************************************************************************
Changes the type of slot feature. New fields are initialized as
indicated in the table above. If you want to change these fields, you
need to edit their expressions.

Environment: Environment: Internal and External
See Also: 
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_slot_type
(
    tag_t   slot_feature,               /* <I>
                                        Slot feature
                                        */
    UF_MODL_slot_type_e_t new_slot_type /* <I>
                                        New slot type. Valid types are:
                                        UF_RECTANGULAR_SLOT
                                        UF_BALL_END_SLOT, UF_U_SLOT
                                        UF_T_SLOT, UF_DOVE_TAIL_SLOT
                                        */
);

/********************************************************************
Gets U slot parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_u_slot_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier.
                      */
int  edit ,/* <I>
           This is an unused flag. It was used to determine
           whether to return the right-hand side or both sides
           of an expression. Currently, both sides of an
           expression are returned.
           */
char ** width ,/* <OF>
               Slot width.  This must be freed by calling
               UF_free.
               */
char ** depth ,/* <OF>
               Slot depth.  This must be freed by calling
               UF_free.
               */
char ** corner_rad ,/* <OF>
                    Slot corner radius  This must be freed by calling
                    UF_free.
                    */
char ** distance ,/* <OF>
                  Slot distance for a none thru slot.  This must be freed by cal
ling
                  UF_free.
                  */
int * thru_flag  /* <O>
                 A thru flag can be TRUE or FALSE, if set to
                 TRUE then there is no distance to the slot.
                 */
);
/********************************************************************
Gets T-slot parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_t_slot_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier.
                      */
int edit ,/* <I>
          This is an unused flag. It was used to determine
          whether to return the right-hand side or both sides
          of an expression. Currently, both sides of an
          expression are returned.
          */
char ** top_width ,/* <OF>
                   Slot top width.  This must be freed by calling UF_free.
                   */
char ** top_depth ,/* <OF>
                   Slot top depth.  This must be freed by calling UF_free.
                   */
char ** bottom_width ,/* <OF>
                      Slot bottom width.  This must be freed by calling UF_free.
                      */
char ** bottom_depth ,/* <OF>
                      Slot bottom depth.  This must be freed by calling UF_free.
                      */
char ** distance ,/* <OF>
                  Slot distance for a none thru slot.  This must be freed by
                  calling UF_free.
                  */
int  * thru_flag  /* <O>
                  A thru flag can be TRUE or FALSE, if set to
                  TRUE then there is no distance to the slot.
                  */
);
/********************************************************************
Gets rectangular slot parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rect_slot_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It was used to determine
           whether to return the right-hand side or both sides
           of an expression. Currently, both sides of an
           expression are returned.
           */
char ** width ,/* <OF>
               Slot width.  This must be freed by calling
               UF_free.
               */
char ** depth ,/* <OF>
               Slot depth.  This must be freed by calling
               UF_free.
               */
char ** distance ,/* <OF>
                  Slot distance for a none thru slot.  This
                  must be freed by calling UF_free.
                  */
int * thru_flag  /* <O>
                 A thru flag can be TRUE or FALSE, if set to
                 TRUE then there is no distance to the slot.
                 */
);

/********************************************************************
Gets dove tail slot parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_dovetail_slot_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char ** width ,/* <OF>
               Slot width.  This must be freed by calling
               UF_free.
               */
char ** depth ,/* <OF>
               Slot depth.  This must be freed by calling
               UF_free.
               */
char ** angle ,/* <OF>
               Dove tail angle.  This must be freed by calling
               UF_free.
               */
char ** distance ,/* <OF>
                  Slot distance for a none thru slot.  This must
                  be freed by calling UF_free.
                  */
int  * thru_flag  /* <O>
                  A thru flag can be TRUE or FALSE, if set to
                  TRUE then there is no distance to the slot.
                  */
);

/********************************************************************
Gets ball slot parameters.

Environment: Internal  and  External

See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_ball_slot_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char ** ball_dia ,/* <OF>
                  Ball diameter.  This must be freed by calling
                  UF_free.
                  */
char ** depth ,/* <OF>
               Slot depth.  This must be freed by calling
               UF_free.
               */
char ** distance ,/* <OF>
                  Slot distance for a non-thru slot.  This must
                  be freed by calling UF_free.
                  */
int * thru_flag  /* <O>
                 A thru flag can be TRUE or FALSE, if set to
                 TRUE then there is no distance to the slot.
                 */
);

/****************************************************************************
Creates a dove tail slot feature using an origin, tool axis, slot
direction, width, angle, depth, and length. One of two creation
methods is taken depending on whether you want a thru slot or not.

   1. If you want a defined distance, then input the distance and
      placement face (face_li). Also, set the value of face_t1 and face_t2
      to zero.
   2. If you want to have the slot thru from one face to another, then
      supply the placement face and the two faces from which to
      measure the slot distance.

The "Face for the RPO constraint" parameter, face_li, can accept a datum plane.
You can pass in the tag of the datum plane feature or datum plane body. For
relative datums the parent body is used as the target. For an absolute datum
the target body must be set by calling UF_MODL_active_part.

The output of this function is the object identifier associated to the
dove tail slot.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_dove_tail_slot(
double  location[3] ,/* <I>
                     Dove tailslot location.
                     */
double  tool_axis[3] ,/* <I>
                      Dove tailslot tool axis.
                      */
double  direction[3] ,/* <I>
                      Dove tailslot direction.
                      */
char * width ,/* <I>
              Dove tailslot width.
              */
char * depth ,/* <I>
              Dove tailslot depth.
              */
char * angle ,/* <I>
              Dove tailslot angle.
              */
char * distance ,/* <I>
                 Dove tailslot distance.
                 */
tag_t  face_li ,/* <I>
                Face for the RPO constraint.
                */
tag_t  face_t1 ,/* <I>
                Face for thru face 1.
                */
tag_t  face_t2 ,/* <I>
                Face for thru face 2.
                */
tag_t * feature_tag  /* <O>
                     Feature object identifier of created dovetail-slot
                     */
);

/****************************************************************************
Creates a rectangular slot feature using an origin, tool axis, slot
direction, length, width, and depth. One of two creation methods are
taken depending on whether you want a thru slot or not. If you want a
defined distance, then input the distance and placement face.  Also,
set the value of face_t1 and face_t2 to zero.  But, if you want to have
the slot thru from one face to another, then supply the placement face
and the two faces from which to measure the slot distance.  The
output of this function is the object identifier associated to the
rectangular slot.

The "Face for the RPO constraint" parameter, face_li, can accept a datum plane.
You can pass in the tag of the datum plane feature or datum plane body. For
relative datums the parent body is used as the target. For an absolute datum
the target body must be set by calling UF_MODL_active_part.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_rect_slot(
double  location[3] ,/* <I>
                     Rectangular slot location.
                     */
double  tool_axis[3] ,/* <I>
                      Rectangular slot tool axis.
                      */
double  direction[3] ,/* <I>
                      Rectangular slot direction.
                      */
char * width ,/* <I>
              Rectangular slot width.
              */
char * depth ,/* <I>
              Rectangular slot depth.
              */
char * distance ,/* <I>
                 Rectangular slot distance.
                 */
tag_t  face_li ,/* <I>
                Face for the RPO constraint.
                */
tag_t  face_t1 ,/* <I>
                Face for thru face 1.
                */
tag_t  face_t2 ,/* <I>
                Face for thru face 2.
                */
tag_t * feature_tag  /* <O>
                     Feature object identifier of created rectangular slot
                     */
);

/****************************************************************************
Creates a T-slot feature using an origin, tool axis, slot direction,  top
and bottom width, top and bottom depth, and length. One of two
creation methods are taken depending on whether you want a thru
slot or not. If you want a defined distance, then input the distance and
placement face. Also, set the value of face_t1 and face_t2 to zero.
But, if you want to have the slot thru from one face to another, then
supply the placement face and the two faces from which to measure
the slot distance. The output of this function is the object identifier
associated to the T-slot.

The "Face for the RPO constraint" parameter, face_li, can accept a datum plane.
You can pass in the tag of the datum plane feature or datum plane body. For
relative datums the parent body is used as the target. For an absolute datum
the target body must be set by calling UF_MODL_active_part.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_t_slot(
double  location[3] ,/* <I>
                     T slot location.
                     */
double  tool_axis[3] ,/* <I>
                      T slot tool axis.
                      */
double  direction[3] ,/* <I>
                      T slot direction.
                      */
char * t_width ,/* <I>
                T slot top width.
                */
char * t_depth ,/* <I>
                T slot top depth.
                */
char * b_width ,/* <I>
                T slot bottom width.
                */
char * b_depth ,/* <I>
                T slot bottom depth.
                */
char * distance ,/* <I>
                 T slot distance.
                 */
int face_li ,/* <I>
             Face for the RPO constraint.
             */
int  face_t1 ,/* <I>
              Face for thru face 1.
              */
int  face_t2 ,/* <I>
              Face for thru face 2.
              */
tag_t * feature_tag  /* <O>
                     Feature object identifier of created t slot
                     */
);

/****************************************************************************
Creates a U slot feature using an origin, tool axis, slot direction,
width, corner radius, depth, and length. One of two creation methods
are taken depending on whether you want a thru slot or not. If you
want a defined distance, then input the distance and placement face.
Also, set the value of face_t1 and face_t2 to zero. But if you want to
have the slot thru from one face to another, then supply the
placement face and the two faces from which to measure the slot
distance. The output of this function is the object identifier associated
to the U slot.

The "Face for the RPO constraint" parameter, face_li, can accept a datum plane.
You can pass in the tag of the datum plane feature or datum plane body. For
relative datums the parent body is used as the target. For an absolute datum
the target body must be set by calling UF_MODL_active_part.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_u_slot(
double  location[3] ,/* <I>
                     U slot location.
                     */
double  tool_axis[3] ,/* <I>
                      U slot tool axis.
                      */
double  direction[3] ,/* <I>
                      U slot direction.
                      */
char * width ,/* <I>
              U slot width.
              */
char * depth ,/* <I>
              U slot depth.
              */
char * radius ,/* <I>
               U slot corner radius.
               */
char * distance ,/* <I>
                 U slot distance.
                 */
tag_t  face_li ,/* <I>
                Face for the RPO constraint.
                */
tag_t  face_t1 ,/* <I>
                Face for thru face 1.
                */
tag_t  face_t2 ,/* <I>
                Face for thru face 2.
                */
tag_t * feature_tag  /* <O>
                     Feature object identifier of created u slot
                     */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_SLOTS_H_INCLUDED */
