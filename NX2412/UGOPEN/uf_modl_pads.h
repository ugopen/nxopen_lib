/*******************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open API modeling routines to create, edit and inquire about pads.

*****************************************************************************/

#ifndef UF_MODL_PADS_H_INCLUDED
#define UF_MODL_PADS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************************************************
Gets rectangular pad parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rect_pad_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It was used to determine
           whether to return the right-hand side or both sides
           of an expression. Currently, both sides of an
           expression are returned.
           */
char * size[3] ,/* <OF>
                Pad size (length , width , height).
                */
char ** corner_rad ,/* <OF>
                    Pad corner radius.  This must be freed by
                    calling UF_free.
                    */
char ** taper_angle  /* <OF>
                     Pad taper angle.  This must be freed by
                     calling UF_free.
                     */
);/* <RETIRE_DOTNET> */

/********************************************************************
In order to provide appropriate .NET binding for UF_MODL_ask_rect_pad_parms,  
UF_MODL_ask_rect_pad_parms_1 is introduced. 

Note: C/C++ users can continue to use UF_MODL_ask_rect_pad_parms. 

For documentation, refer to documentation of UF_MODL_ask_rect_pad_parms.

History: Originally released in NX9
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rect_pad_parms_1(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It was used to determine
           whether to return the right-hand side or both sides
           of an expression. Currently, both sides of an
           expression are returned.
           */
int *pad_length,/* <O> 
                Pad size length */
char *** size,/* <OF,len:pad_length>
                Pad size (length , width , height).
                */
char ** corner_rad ,/* <OF>
                    Pad corner radius.  This must be freed by
                    calling UF_free.
                    */
char ** taper_angle  /* <OF>
                     Pad taper angle.  This must be freed by
                     calling UF_free.
                     */
);

/****************************************************************************
Creates a rectangular pad feature using a location, direction, X
direction, size, corner radius and taper angle. Along with these items
a placement face is needed to determine which face the pad is
associated to. The output of this function is the object identifier
associated to the rectangular pad.
Return: 
   Return code:
      = 0: successful
      > 0: failing error number
      < 0: failing error number

Environment: Internal  and  External
History: For V18.0, a datum plane may be input as the face defining the 
         RPO constraint.
See Also: 
          UF_MODL_ask_rect_pad_parms 
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_rect_pad(
double  location[3] ,/* <I>
                     Rectangular pad location.
                     */
double  direction[3] ,/* <I>
                      Rectangular pad direction.
                      */
double  x_dir[3] ,/* <I>
                  Rectangular pad x direction.
                  */
char * size[3] ,/* <I>
                Rectangular pad size.
                */
char * radius ,/* <I>
               Rectangular pad corner radius.
               */
char * angle ,/* <I>
              Rectangular pad taper angle.
              */
tag_t  face ,/* <I>
             Face for the RPO constraint (may be a datum plane).
             */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created rect. pad
                        */
);

/******************************************************************************
Creates a general pad. Expressions are created for the taper_angle,
top_offset, placement_radius, and top_radius if they are used.

Environment: Internal  and  External
See Also: UF_MODL_ask_general_pad
          UF_MODL_edit_general_pad
          UF_MODL_free_general_pad

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_general_pad(
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   The faces or a face collector used to define the shape of
                                   the pad at the placement faces. The first
                                   face is used to determine the target
                                   body.
                                   */
UF_MODL_offset_trans_faces_p_t top_faces ,/* <I>
                                          The faces or a face collector used to define
                                          the top of the pad.
                                          The top can either be an offset or
                                          translation of the specified faces.
                                          If it is desired to have the top be
                                          an offset or translate of the
                                          placement faces, then just set the
                                          UF_MODL_faces_p_t pointer within
                                          this input structure to the
                                          placement_faces pointer value.
                                          */
UF_MODL_pocketpad_outline_p_t outline ,/* <I>
                                       The definition of the curves used to
                                       define the shape of the pad. The shape
                                       can be defined by a single set of curves
                                       or section builder 
                                       at either the placement face or the top
                                       face, and then the other curves or section builder are
                                       derived with a taper angle. The shape
                                       can also be defined by specifying curves or section builders
                                       at both the placement face and the top
                                       face.
                                       */
UF_MODL_parm_p_t placement_radius ,/* <I>
                                   The specification of the radius desired
                                   between the side of the pad and the
                                   placement face.
                                   */
UF_MODL_parm_p_t top_radius ,/* <I>
                             The specification of the radius desired
                             between the side of the pad and the top
                             of the pad.
                             */
tag_t * general_pad_tag  /* <O>
                         Object identifier for the general pad
                         feature.
                         */
);

/******************************************************************************
Retrieves the parameters used to create a general pad.

Environment: Internal  and  External
See Also: 
          UF_MODL_create_general_pad
          UF_MODL_edit_general_pad
          UF_MODL_free_general_pad
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_general_pad(
tag_t general_pad_tag ,/* <I>
                       Object identifier of the general pad
                       feature whose parameters are to be
                       retrieved.
                       */
UF_MODL_faces_p_t placement_faces ,/* <OF,free:UF_MODL_free_general_pad>
                                   The faces used to define the shape of
                                   the pad at the placement faces. The
                                   first face is used to determine the
                                   target body.  The caller must allocate
                                   a UF_MODL_faces_t structure and pass a
                                   pointer to that structure.  This will be
                                   filled with allocated data which must be
                                   freed by calling UF_MODL_free_general_pad.
                                   */
UF_MODL_offset_trans_faces_p_t top_faces ,/* <OF>
                                   The definition of the top of the pad.  The
                                   top can either be an offset or translation
                                   of the specified faces. If the top was
                                   an offset or translate of the placement
                                   faces, then the UF_MODL_faces_p_t pointer
                                   within this structure, points to the
                                   placement faces structure.  The caller must
                                   allocate a UF_MODL_offset_trans_faces_t
                                   structure and pass a pointer to that
                                   structure.  This will be filled with
                                   allocated data which must be freed by
                                   calling UF_MODL_free_general_pad.
                                   */
UF_MODL_pocketpad_outline_p_t outline ,/* <OF>
                                   The definition of the curves used to
                                   define the shape of the pad. The
                                   shape can be defined by a single set of
                                   curves at either the placement face or
                                   the top face, and then the other curves
                                   are derived with a taper angle. The
                                   shape can also be defined by specifying
                                   curves at both the placement face and the
                                   top face.  The caller must allocate a
                                   UF_MODL_pocketpad_outline_t structure and
                                   pass a pointer to that structure.  This will
                                   be filled with allocated data which must be
                                   freed by calling UF_MODL_free_general_pad.
                                   */
UF_MODL_parm_p_t placement_radius ,/* <OF>
                                   The specification of the radius desired
                                   between the side of the pad and the
                                   placement face.  The caller must allocate a
                                   UF_MODL_parm_t structure and pass a
                                   pointer to that structure.  This will
                                   be filled with allocated data which must be
                                   freed by calling UF_MODL_free_general_pad.
                                   */
UF_MODL_parm_p_t top_radius  /* <OF>
                             The specification of the radius desired
                             between the side of the pad and the top of the pad.
                             The caller must allocate a UF_MODL_parm_t
                             structure and pass a pointer to that structure.
                             This will be filled with allocated data which must
                             be freed by calling UF_MODL_free_general_pad.
                             */
);

/******************************************************************************
Retrieves the parameters with face collectors and section builders
used to create a general pad.

Environment: Internal  and  External
See Also: 
          UF_MODL_create_general_pad
          UF_MODL_edit_general_pad
          UF_MODL_free_general_pad
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_general_pad1(
tag_t general_pad_tag ,/* <I>
                       Object identifier of the general pad
                       feature whose parameters are to be
                       retrieved.
                       */
UF_MODL_faces_p_t placement_faces ,/* <OF>
                                   The face collector used to define the shape of
                                   the pad at the placement faces. The
                                   first face of the face collector is used to determine the
                                   target body.  The caller must allocate
                                   a UF_MODL_faces_t structure and pass a
                                   pointer to that structure.  This will be
                                   filled with allocated data which must be
                                   freed by calling UF_MODL_free_general_pad.
                                   */
UF_MODL_offset_trans_faces_p_t top_faces ,/* <OF>
                                   The definition of the top of the pad.  The
                                   top can either be an offset or translation
                                   of the specified face collector. If the top was
                                   an offset or translate of the placement
                                   faces, then the UF_MODL_faces_p_t pointer
                                   within this structure, points to the
                                   placement faces structure.  The caller must
                                   allocate a UF_MODL_offset_trans_faces_t
                                   structure and pass a pointer to that
                                   structure.  This will be filled with
                                   allocated data which must be freed by
                                   calling UF_MODL_free_general_pad.
                                   */
UF_MODL_pocketpad_outline_p_t outline ,/* <OF>
                                   The definition of the curves used to
                                   define the shape of the pad. The
                                   shape can be defined by a single section builder 
                                   at either the placement face or
                                   the top face, and then the other section builder 
                                   is derived with a taper angle. The
                                   shape can also be defined by specifying
                                   section builders at both the placement face and the
                                   top face.  The caller must allocate a
                                   UF_MODL_pocketpad_outline_t structure and
                                   pass a pointer to that structure.  This will
                                   be filled with allocated data which must be
                                   freed by calling UF_MODL_free_general_pad.
                                   */
UF_MODL_parm_p_t placement_radius ,/* <OF>
                                   The specification of the radius desired
                                   between the side of the pad and the
                                   placement face.  The caller must allocate a
                                   UF_MODL_parm_t structure and pass a
                                   pointer to that structure.  This will
                                   be filled with allocated data which must be
                                   freed by calling UF_MODL_free_general_pad.
                                   */
UF_MODL_parm_p_t top_radius  /* <OF>
                             The specification of the radius desired
                             between the side of the pad and the top of the pad.
                             The caller must allocate a UF_MODL_parm_t
                             structure and pass a pointer to that structure.
                             This will be filled with allocated data which must
                             be freed by calling UF_MODL_free_general_pad.
                             */
);

/*******************************************************************************
Edits the various parameters of the general pad and reconstructs it
based on these new parameters.

Environment: Internal  and  External
See Also:
See Also: UF_MODL_create_general_pad
          UF_MODL_ask_general_pad
          UF_MODL_free_general_pad

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_general_pad(
tag_t general_pad_tag ,/* <I>
                       Object identifier of the general pad
                       feature to be modified.
                       */
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   The faces or face collector used to define the shape of
                                   the pad at the placement faces. The first
                                   face is used to determine the target
                                   body.
                                   */
UF_MODL_offset_trans_faces_p_t top_faces ,/* <I>
                                              The definition of the top of the
                                              pad.  The top can either be an
                                              offset or translation of the
                                              specified faces or face collector. If it is
                                              desired to have the top be an
                                              offset or translate of the
                                              placement faces, then just set
                                              the UF_MODL_faces_p_t
                                              pointer within this input i
                                              structure to the
                                              placement_faces pointer value.
                                              */
UF_MODL_pocketpad_outline_p_t outline ,/* <I>
                                       The definition of the curves used to
                                       define the shape of the pad. The shape
                                       can be defined by a single set of curves
                                       or section builder 
                                       at either the placement face or the top
                                       face, and then the other curves 
                                       or section builder are
                                       derived with a taper angle. The shape
                                       can also be defined by specifying 
                                       curves or section builders
                                       at both the placement face and the top
                                       face.
                                       */
UF_MODL_parm_p_t placement_radius ,/* <I>
                                   The specification of the radius desired
                                   between the side of the pad and the
                                   placement face.
                                   */
UF_MODL_parm_p_t top_radius  /* <I>
                             The specification of the radius desired
                             between the side of the pad and the top
                             of the pad.
                             */
);

/******************************************************************************
Frees all the memory associated with the parameters returned from
UF_MODL_ask_general_pad.

Environment: Internal  and  External
See Also: UF_MODL_create_general_pad
          UF_MODL_ask_general_pad
          UF_MODL_edit_general_pad

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_free_general_pad(
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   The faces used to define the shape of
                                   the pad at the placement faces. The
                                   first face is used to determine the
                                   target body.
                                   */
UF_MODL_offset_trans_faces_p_t top_faces ,/* <I>
                                              The definition of the top of the
                                              pad.  The top can either be an
                                              offset or translation of the
                                              specified faces. If it is
                                              desired to have the top be an
                                              offset or translate of the
                                              placement faces, then just set
                                              the UF_MODL_faces_p_t
                                              pointer within this input i
                                              structure to the
                                              placement_faces pointer value.
                                              */

UF_MODL_pocketpad_outline_p_t outline ,/* <I>
                                       The definition of the curves used to
                                       define the shape of the pad. The
                                       shape can be defined by a single set of
                                       curves at either the placement face or
                                       the top face, and then the other curves
                                       are derived with a taper angle. The
                                       shape can also be defined by
                                       specifying curves at both the
                                       placement face and the top face.
                                       */
UF_MODL_parm_p_t placement_radius ,/* <I>
                                   The specification of the radius desired
                                   between the side of the pad and the
                                   placement face.
                                   */
UF_MODL_parm_p_t top_radius  /* <I>
                             The specification of the radius desired
                             between the side of the pad and the
                             top of the pad.
                             */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_PADS_H_INCLUDED */

