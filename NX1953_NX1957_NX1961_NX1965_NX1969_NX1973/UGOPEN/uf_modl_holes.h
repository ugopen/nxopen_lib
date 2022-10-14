/*****************************************************************************
             Copyright (c) 1999-2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about holes.

*****************************************************************************/

#ifndef UF_MODL_HOLES_H_INCLUDED
#define UF_MODL_HOLES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Changes the type of hole feature. New fields are initialized to zero. If
you want to change these fields, you need to edit their expressions.

Environment: Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_hole_type
(
    tag_t   hole_feature,               /* <I>
                                        Hole feature
                                        */
    UF_MODL_hole_type_e_t new_hole_type /* <I>
                                        New hole type. Valid types are:
                                        UF_SIMPLE_HOLE
                                        UF_COUNTER_BORE_HOLE
                                        UF_COUNTER_SUNK_HOLE
                                        */
);

/****************************************************************************
Creates a c-bore hole. The Origin indicates where the center of the
C-Bore hole is located on the link-face. Interactively, this is the face
chosen to place the hole in, and the location of the pick is used as the
origin. The Open API programmer inputs this information. The
C-Bore and Hole Diameters, C-Bore and Hole Depths, and Hole
Tip Angle control the size. The Direction Vector has to be
perpendicular to the link-face, opposite the face normal. If a thru
face is indicated, then the Hole Depth is ignored. The output of this
function is the object identifier associated to the c-bore hole.

The "Face for the RPO constraint" parameter, face_li, can accept a datum plane.
You can pass in the tag of the datum plane feature or datum plane body. For
relative datums the parent body is used as the target. For an absolute datum
the target body must be set by calling UF_MODL_active_part.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_c_bore_hole(
double  location[3] ,/* <I>
                     Hole location.
                     */
double  direction[3] ,/* <I>
                      Hole direction.
                      */
const char * diameter1 ,/* <I>
                        Hole diameter.
                        */
const char * depth1 ,/* <I>
                     Hole depth.
                     */
const char * diameter2 ,/* <I>
                        C-bore diameter.
                        */
const char * depth2 ,/* <I>
                     C-bore depth.
                     */
const char * angle ,/* <I>
                    Hole tip angle.
                    */
tag_t  face_li ,/* <I>
                Face for the RPO constraint.
                */
tag_t  face_t1 ,/* <I>
                Face for thru face.
                */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created C bore hole
                        */
);

/********************************************************************
Gets simple hole parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_simple_hole_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It was used to determine
          whether to return the right-hand side or both sides
          of an expression. Currently, both sides of an
          expression are returned.
          */
char **diameter ,/* <OF>
                 Hole diameter.  This must be freed by calling
                 UF_free.
                 */
char **depth ,/* <OF>
              Hole depth for a none thru hole.  This must be
              freed by calling UF_free.
              */
char **tip_angle ,/* <OF>
                  Tip angle.  This must be freed by calling
                  UF_free.
                  */
int *thru_flag  /* <O>
                A thru flag can be TRUE or FALSE, if set to
                TRUE then there is no depth to the hole.
                */
);

/********************************************************************
Gets countersunk hole parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_c_sunk_hole_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char ** diameter1 ,/* <OF>
                   Countersunk diameter.  This must be freed
                   by calling UF_free.
                   */
char ** diameter2 ,/* <OF>
                   Hole diameter.  This must be freed
                   by calling UF_free.
                   */
char ** depth1 ,/* <OF>
                Hole depth for a none thru hole.  This must be freed
                by calling UF_free.
                */
char ** csink_angle ,/* <OF>
                     Countersunk angle.  This must be freed
                     by calling UF_free.
                     */
char ** tip_angle ,/* <OF>
                   Tip angle.  This must be freed
                   by calling UF_free.
                   */
int * thru_flag  /* <O>
                 A thru flag can be TRUE or FALSE, if set to
                 TRUE then there is no depth to the hole.
                 */
);

/******************************************************************
Gets counterbore hole parameters.

Environment: Internal  and  External

See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_c_bore_hole_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It used to determine whether
           to return the right-hand side or both sides of an
           expression. Currently, both sides of an expression
           are returned.
           */
char ** diameter1 ,/* <OF>
                   Counterbore diameter.  This must be freed by
                   calling UF_free.
                   */
char ** diameter2 ,/* <OF>
                   Hole diameter.  This must be freed by
                   calling UF_free.
                   */
char ** depth1 ,/* <OF>
                Counterbore depth.  This must be freed by
                calling UF_free.
                */
char ** depth2 ,/* <OF>
                Hole depth for a none thru hole.  This must be freed by
                calling UF_free.
                */
char ** tip_angle ,/* <OF>
                   Tip angle.  This must be freed by
                   calling UF_free.
                   */
int * thru_flag  /* <O>
                 A thru flag can be TRUE or FALSE, if set to
                 TRUE then there is no depth to the hole.
                 */
);

/********************************************************************
Gets taper hole parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_taper_hole_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It was used to determine
          whether to return the right-hand side or both sides
          of an expression. Currently, both sides of an
          expression are returned.
          */
char **diameter ,/* <OF>
                 Hole diameter.  This must be freed by calling
                 UF_free.
                 */
char **taper_angle ,/* <OF>
                  Taper angle.  This must be freed by calling
                  UF_free.
                  */
char **depth ,/* <OF>
              Hole depth for a none thru hole.  This must be
              freed by calling UF_free.
              */
int *thru_flag  /* <O>
                A thru flag can be TRUE or FALSE, if set to
                TRUE then there is no depth to the hole.
                */
);

/****************************************************************************
Creates a counter-sunk hole. The Origin indicates where the center
of the C-Sunk hole is located on the link-face. Interactively, this is
the face chosen to place the hole in, and the location of the pick is
used as the origin. In Open API, this information is input by the
user. The C-Sunk and Hole Diameters, C-Sunk and Hole Depths,
and Hole Tip Angle control the size. The Direction Vector has to be
perpendicular to the link-face, opposite the face normal. If a thru
face is indicated, then the Hole Depth is ignored. The output of this
function is the object identifier associated to the c-sunk hole.

The "Face for the RPO constraint" parameter, face_li, can accept a datum plane.
You can pass in the tag of the datum plane feature or datum plane body. For
relative datums the parent body is used as the target. For an absolute datum
the target body must be set by calling UF_MODL_active_part.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_c_sunk_hole(
double location[3] ,/* <I>
                    Hole location.
                    */
double direction[3] ,/* <I>
                     Hole direction.
                     */
const char * diameter1 ,/* <I>
                        Hole diameter.
                        */
const char * depth1 ,/* <I>
                     Hole depth.
                     */
const char * diameter2 ,/* <I>
                        C-sunk diameter.
                        */
const char * csink_angle ,/* <I>
                          C-sunk angle.
                          */
const char * angle ,/* <I>
                    Hole tip angle.
                    */
tag_t face_li ,/* <I>
               Face for the RPO constraint.
               */
tag_t face_t1 ,/* <I>
               Face for thru face.
               */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created csunk hole
                        */
);

/****************************************************************************
Creates a simple hole. The Origin indicates where the center of the
simple hole is located on the link-face. Interactively, this is the face
chosen to place the hole in, and the location of the pick is used as the
origin. In Open API, this information is input by the user. The
Diameter, Depth and Tip Angle control the sizing of the hole. The
Direction Vector has to be perpendicular to the link-face, opposite
the face normal. If a thru face is indicated, then the depth is ignored.
The output of this function is the object identifier associated to the
simple hole.

The "Face for the RPO constraint" parameter, face_li, can accept a datum plane.
You can pass in the tag of the datum plane feature or datum plane body. For
relative datums the parent body is used as the target. For an absolute datum
the target body must be set by calling UF_MODL_active_part.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_simple_hole(
double  location[3] ,/* <I>
                     Hole location.
                     */
double  direction[3] ,/* <I>
                      Hole direction.
                      */
const char * diame ,/* <I>
                    Hole diameter.
                    */
const char * depth ,/* <I>
                    Hole depth.
                    */
const char * angle ,/* <I>
                    Hole tip angle.
                    */
tag_t  face_li ,/* <I>
                Face for the RPO constraint.
                */
tag_t  face_t1 ,/* <I>
                Face for thru face.
                */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created simple hole
                        */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_HOLES_H_INCLUDED */
