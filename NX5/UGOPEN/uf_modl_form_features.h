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

/******************************************************************************
Thickens the input sheet body based on the offsets specified. The
routine creates expressions for each of the offsets created.


Environment: Internal  and  External
See Also: 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_thicken_sheet(
tag_t sheet_body_tag ,/* <I>
                      Object identifier of the sheet body to be thickened.
                      */
char * first_offset ,/* <I>
                     The offset from the face(s) of the input sheet body
                     that one side of the resultant solid body should be.
                     If positive the offset is applied in the direction of
                     the sheet face normal, if negative the offset is
                     applied in the direction opposite to the sheet face
                     normal.
                     */
char * second_offset ,/* <I>
                      The offset from the face(s) of the input sheet body
                      that the other side of the resultant body should be.
                      If positive the offset is applied in the direction of
                      the sheet face normal, if negative the offset is
                      applied in the direction opposite to the sheet face
                      normal.
                      */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new solid body
                      UF_POSITIVE   = add to active solid body
                      UF_NEGATIVE = subtract from active solid body
                      UF_UNSIGNED = intersect with active solid body
                      */
tag_t * thicken_sheet_tag  /* <O>
                           Object identifier for the thicken sheet feature.
                           */
);


/******************************************************************************
This routine retrieves the parameters used to thicken a sheet body.

Environment: Internal  and  External
See Also: 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_thicken_sheet_parms(
tag_t thicken_sheet_tag ,/* <I>
                         Object identifier for the thicken sheet feature.
                         */
tag_t * sheet_tag ,/* <O>
                   Object identifier of the sheet body that was
                   thickened.
                   */
char ** first_offset ,/* <OF>
                      The value of the offset from the face(s) of the input
                      sheet body that one side of the resultant solid body
                      was. If positive the offset was applied in the
                      direction of the sheet face normal, if negative the
                      offset was applied in the direction opposite to the
                      sheet face normal. Free the memory allocated for
                      this output by calling UF_free(first_offset).
                      */
char ** second_offset  /* <OF>
                       The value of the offset from the face(s) of the input
                       sheet body that the other side of the resultant body
                       was. If positive the offset was applied in the
                       direction of the sheet face normal, if negative the
                       offset was applied in the direction opposite to the
                       sheet face normal. Free the memory allocated for
                       this output by calling UF_free(second_offset).
                       */
);

/******************************************************************************
This routine changes the parameters used to thicken a sheet body.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_redefine_thicken_sheet(
       tag_t thicken_sheet_tag,  /* <I>
                                 Object identifier for the thicken sheet feature
                                 */
       char *first_offset,       /* <I>
                                 String containing first offset value
                                 */
       char *second_offset,      /* <I>
                                 String containing second offset value
                                 */
       tag_t sheet_body_tag,     /* <I>
                                 New sheet body to be thickened.  If NULL then
                                 the present sheet body will be used.
                                 */
       tag_t target_body_tag     /* <I>
                                 New target body.  If  NULL then the present
                                 target body will be used.
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
