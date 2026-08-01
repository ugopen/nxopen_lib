/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about features such as
    Hole, Boss, Pocket, Pad, Slot, Groove, bounded plane, thicken sheet, .

*****************************************************************************/

#ifndef UF_MODL_FORM_FEATURES_H_INCLUDED
#define UF_MODL_FORM_FEATURES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <uf_modl_holes.h>
#include <uf_modl_pockets.h>
#include <uf_modl_pads.h>
#include <uf_modl_grooves.h>
#include <uf_modl_slots.h>
#include <libufun_exports.h>
#include <uf_retiring.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************************************************
Creates a boss feature using the boss origin, direction, diameter,
height, tip angle, and placement face. The placement face is used to
determine which face the boss is associated to. The output of this
function is the object identifier associated to the boss.
Return: 
   Return code:
      = 0: successful
      > 0: failing error number
      < 0: failing error number

Environment: Internal  and  External
History: For V18.0, a datum plane may be input as the face defining the 
         RPO constraint.
See Also: 
           UF_MODL_ask_boss_parms
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_boss(
double  location[3] ,/* <I>
                     Boss location.
                     */
double  direction[3] ,/* <I>
                      Boss direction.
                      */
char * diame ,/* <I>
              Boss diameter.
              */
char * height ,/* <I>
               Boss height.
               */
char * angle ,/* <I>
              Boss tip angle.
              */
tag_t  face ,/* <I>
             Face for the RPO constraint (may be a datum plane)
             */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created boss
                        */
);


/********************************************************************
Gets boss parameters.

Environment: Internal  and  External

See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_boss_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It used to determine whether
           to return the right-hand side or both sides of an
           expression. Currently, both sides of an expression
           are returned.
           */
char ** diameter ,/* <OF>
                  Boss diameter.  This must be freed by calling
                  UF_free.
                  */
char ** height ,/* <OF>
                Boss height.  This must be freed by calling
                UF_free.
                */
char ** taper_angle  /* <OF>
                     Boss taper angle.  This must be freed by calling
                     UF_free.
                     */
);

/****************************************************************************
Extracts the given face into the work part.  If the face given is in the
work part, then the extracted face is associative to the given face (i.e.
if the given face is moved, the extracted face moves with it).  If the
given face is an occurrence of a face that's not in the work part, then
the face is created without having any associativity.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_extract_face(
tag_t face ,/* <I>
            Face to be extracted.  Can be an occurrence.
            */
int mode ,/* <I>
          Type of extraction to perform.
           0 = new_face should be the same type of face
               as the given face.
           1 = new_face should be a cubic polynomial
               approximation of the given face.
           2 = new_face should be a b-surface
               representation of the given face.
          */
tag_t * sheet_body  /* <O>
                    Sheet body created, this sheet is created in the work
                    part.
                    */
);

/*****************************************************************************
Creates a bounded plane feature from closed string loops obtained
from a string of end-to-end curves. The outside or peripheral loop
forms the sheet boundary. The inner closed loops are holes in the
bounded plane. You can specify either 1 or -1 for the dir[ ] field of
the s_section argument since the direction is not significant for this
routine due to the closed loops. The curves selected must be
co-planar, chainable, and form a closed shape. This function
automatically determines which loop is the periphery.  There can be
only one peripheral loop. The tolerance values determine whether or
not the curves are chainable and co-planar. The output of this
function is the object identifier associated to the feature.

Environment: Internal  and  External
See Also: 
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_bplane(
UF_STRING_p_t s_section ,/* <I>
                         Pointer to the curve list structure.
                         int     num     Total number of curve string loops
                                         (min=1, max=150)
                         int string[ ]   Total number of segment curves
                                         per curve string loop
                                         (min=1, max =402)
                         int dir[ ]      Direction of a curve string
                                          1 = Start to end
                                         -1 = End to start
                         tag_t id[ ]     Identifier of section curve
                         */
double tol[3] ,/* <I>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               [2] = Not used (formerly listed as Intersection)
               */
tag_t * body_obj_id  /* <O>
                     Body object identifier
                     */
);

/******************************************************************************
Returns the creation data with which a bounded plane was created.

Environment: Internal  and  External
See Also:
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bplane(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier
                       */
UF_STRING_p_t s_section ,/* <OF>
                         Pointer to the string list structure. Contains the
                         string loops which define the feature.
                         Use UF_MODL_free_string_list to deallocate memory.
                         */
double tol[2]  /* <O>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_FORM_FEATURES_H_INCLUDED */
