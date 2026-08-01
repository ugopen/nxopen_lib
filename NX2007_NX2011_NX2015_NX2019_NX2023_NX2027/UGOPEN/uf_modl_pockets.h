/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about pockets.

*****************************************************************************/

#ifndef UF_MODL_POCKETS_H_INCLUDED
#define UF_MODL_POCKETS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************************************************
Gets rectangular pocket parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rect_pocket_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char * length[3],/* <OF>
                Pointer to an array of three character pointers for
                length, width, and depth.  This must be freed by
                calling UF_free.
                */
char ** corner_rad ,/* <OF>
                    Pocket corner radius.  This must be freed by
                    calling UF_free.
                    */
char ** floor_rad ,/* <OF>
                   Pocket floor radius.  This must be freed by
                   calling UF_free.
                   */
char ** taper_angle  /* <OF>
                     Pocket taper angle.  This must be freed by
                     calling UF_free.
                     */
);

/********************************************************************
Gets cylinder pocket parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_cyl_pocket_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object  identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char ** diameter ,/* <OF>
                  Cylinder diameter.  This must be freed by
                  calling UF_free.
                  */
char ** depth ,/* <OF>
               Cylinder depth.  This must be freed by
               calling UF_free.
               */
char ** floor_rad ,/* <OF>
                   Floor radius.  This must be freed by
                   calling UF_free.
                   */
char ** taper_angle  /* <OF>
                     Taper angle.  This must be freed by
                     calling UF_free.
                     */
);

/****************************************************************************
Creates a cylindrical pocket feature using a location, direction,
diameter, depth, floor radius, and taper angle. Along with these items
a placement face is needed to determine which face the pocket is
associated to. The output of this function is the object identifier
associated to the cylindrical pocket.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_cyl_pocket(
double  location[3] ,/* <I>
                     Cylindrical pockets location.
                     */
double  direction[3] ,/* <I>
                      Cylindrical pockets direction.
                      */
char * diame ,/* <I>
              Cylindrical pockets diameter.
              */
char * depth ,/* <I>
              Cylindrical pockets depth.
              */
char * radius ,/* <I>
               Cylindrical pockets floor radius.
               */
char * angle ,/* <I>
              Cylindrical pockets taper angle.
              */
tag_t  face ,/* <I>
             Face for the RPO constraint.
             */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created pocket
                        */
);

/****************************************************************************
Creates a rectangular pocket feature using the location, direction, X
direction, size, corner radius, floor radius and taper angle. Along with
these items a placement face is needed to determine which face the
pocket is associated to. The output of this function is the object
identifier associated to the rectangular pocket.
Return: 
   Return code:
      = 0: successful
      > 0: failing error number
      < 0: failing error number

Environment: Internal  and  External
History: For V18.0, a datum plane may be input as the face defining the 
         RPO constraint.
See Also: 
           UF_MODL_ask_rect_pocket_parms
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_rect_pocket(
double  location[3] ,/* <I>
                     Rectangular pocket location.
                     */
double  direction[3] ,/* <I>
                      Rectangular pocket direction.
                      */
double  x_dir[3] ,/* <I>
                  Rectangular pocket x direction.
                  */
char * len[3] ,/* <I>
               Rectangular pocket size.
               */
char * corner ,/* <I>
               Rectangular pocket corner radius.
               */
char * floor ,/* <I>
              Rectangular pocket floor radius.
              */
char * angle ,/* <I>
              Rectangular pocket taper angle.
              */
tag_t face ,/* <I>
            Face for the RPO constraint (may be a datum plane).
            */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created rect. pocket
                        */
);

/******************************************************************************
Creates a general pocket. Creates Expressions for the taper_angle,
floor_offset, placement_radius, and floor_radius if they are used.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_general_pocket
 UF_MODL_edit_general_pocket
 UF_MODL_free_general_pocket

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_general_pocket(
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   The faces or a face collector used to define the shape of
                                   the pocket at the placement faces. The
                                   first face is used to determine the
                                   target body.
                                   */
UF_MODL_offset_trans_faces_p_t floor_faces ,/* <I>
                                            The faces or a face collector used to define
                                            the floor of the pocket. The floor can either be an
                                            offset or translation of the
                                            specified faces. If it is desired
                                            to have the floor be an offset
                                            or translate of the
                                            placement faces, then just set the
                                            UF_MODL_faces_p_t pointer within
                                            this input structure to the
                                            placement_faces pointer value.
                                            */
UF_MODL_pocketpad_outline_p_t outline ,/* <I>
                                       The definition of the curves used to
                                       define the shape of the pocket.
                                       The shape can be defined by a single set of
                                       curves or section builder at either the placement face or
                                       the floor face, and then the other
                                       curves or section builder are derived with a taper angle.
                                       The shape can also be defined by
                                       specifying curves or section builders at both the
                                       placement face and the floor face.
                                       */
UF_MODL_parm_p_t placement_radius ,/* <I>
                                   The specification of the radius desired
                                   between the side of the pocket and the
                                   placement face.
                                   */
UF_MODL_parm_p_t floor_radius ,/* <I>
                               The specification of the radius desired
                               between the side of the pocket and the
                               floor of the pocket.
                               */
tag_t * general_pocket_tag  /* <O>
                            Object identifier for the general
                            pocket feature.
                            */
);

/******************************************************************************
Retrieves the parameters used to create a general pocket.

Environment: Internal  and  External
See Also:
 UF_MODL_create_general_pocket
 UF_MODL_edit_general_pocket
 UF_MODL_free_general_pocket

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_general_pocket(
tag_t general_pocket_tag ,/* <I>
                          Object identifier of the general pocket
                          feature whose parameters are to be
                          retrieved.
                          */
UF_MODL_faces_p_t placement_faces ,/* <OF,free:UF_MODL_free_general_pocket>
                                   The faces used to define the shape of the
                                   pocket at the placement faces. The first face
                                   is used to determine the target body.  The
                                   caller must allocate a UF_MODL_faces_t
                                   structure, and pass in a pointer to that
                                   structure.  The structure will be filled
                                   with allocated data which can be freed by
                                   calling UF_MODL_free_general_pocket.
                                   */
UF_MODL_offset_trans_faces_p_t floor_faces ,/* <OF>
                                   The definition of the floor of the pocket.
                                   The floor can either be an offset or
                                   translation of the specified faces. If the
                                   floor was an offset or translate of the
                                   placement faces, then the UF_MODL_faces_p_t
                                   pointer within this structure, points to the
                                   placement faces structure.  The caller must
                                   allocate a UF_MODL_offset_trans_faces_t
                                   structure, and pass in a pointer to that
                                   structure.  The structure will be filled
                                   with allocated data which can be freed by
                                   calling UF_MODL_free_general_pocket.
                                   */
UF_MODL_pocketpad_outline_p_t outline ,/* <OF>
                                   The definition of the curves used to
                                   define the shape of the pocket. The
                                   shape can be defined by a single set of
                                   curves at either the placement face or
                                   the floor face, and then the other
                                   curves are derived with a taper angle.
                                   The shape can also be defined by specifying
                                   curves at both the placement face and the
                                   floor face.  The caller must allocate a
                                   UF_MODL_pocketpad_outline_t structure, and
                                   pass in a pointer to that structure.  The
                                   structure will be filled with allocated
                                   data which can be freed by calling
                                   UF_MODL_free_general_pocket.
                                   */
UF_MODL_parm_p_t placement_radius ,/* <OF>
                                   The specification of the radius desired
                                   between the side of the pocket and the
                                   placement face.  The caller must allocate a
                                   UF_MODL_parm_p_t structure, and
                                   pass in a pointer to that structure.  The
                                   structure will be filled with allocated
                                   data which can be freed by calling
                                   UF_MODL_free_general_pocket.
                                   */
UF_MODL_parm_p_t floor_radius  /* <OF>
                               The specification of the radius desired
                               between the side of the pocket and the
                               floor of the pocket. The caller must allocate a
                               UF_MODL_parm_p_t structure, and
                               pass in a pointer to that structure.  The
                               structure will be filled with allocated
                               data which can be freed by calling
                               UF_MODL_free_general_pocket.
                               */
);

/******************************************************************************
Retrieves the parameters with face collectors and section builders
used to create a general pocket.

Environment: Internal  and  External
See Also:
 UF_MODL_create_general_pocket
 UF_MODL_edit_general_pocket
 UF_MODL_free_general_pocket

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_general_pocket1(
tag_t general_pocket_tag ,/* <I>
                          Object identifier of the general pocket
                          feature whose parameters are to be
                          retrieved.
                          */
UF_MODL_faces_p_t placement_faces ,/* <OF>
                                   The face collector used to define the shape of the
                                   pocket at the placement faces. The first face
                                   of the collector is used to determine the target body.  The
                                   caller must allocate a UF_MODL_faces_t
                                   structure, and pass in a pointer to that
                                   structure.  The structure will be filled
                                   with allocated data which can be freed by
                                   calling UF_MODL_free_general_pocket.
                                   */
UF_MODL_offset_trans_faces_p_t floor_faces ,/* <OF>
                                   The definition of the floor of the pocket.
                                   The floor can either be an offset or
                                   translation of the specified face collector. If the
                                   floor was an offset or translate of the
                                   placement faces, then the UF_MODL_faces_p_t
                                   pointer within this structure, points to the
                                   placement faces structure.  The caller must
                                   allocate a UF_MODL_offset_trans_faces_t
                                   structure, and pass in a pointer to that
                                   structure.  The structure will be filled
                                   with allocated data which can be freed by
                                   calling UF_MODL_free_general_pocket.
                                   */
UF_MODL_pocketpad_outline_p_t outline ,/* <OF>
                                   The definition of the curves used to
                                   define the shape of the pocket. The
                                   shape can be defined by a single section builder
                                   at either the placement face or
                                   the floor face, and then the other
                                   section builder is derived with a taper angle.
                                   The shape can also be defined by specifying
                                   section builders at both the placement face and the
                                   floor face.  The caller must allocate a
                                   UF_MODL_pocketpad_outline_t structure, and
                                   pass in a pointer to that structure.  The
                                   structure will be filled with allocated
                                   data which can be freed by calling
                                   UF_MODL_free_general_pocket.
                                   */
UF_MODL_parm_p_t placement_radius ,/* <OF>
                                   The specification of the radius desired
                                   between the side of the pocket and the
                                   placement face.  The caller must allocate a
                                   UF_MODL_parm_p_t structure, and
                                   pass in a pointer to that structure.  The
                                   structure will be filled with allocated
                                   data which can be freed by calling
                                   UF_MODL_free_general_pocket.
                                   */
UF_MODL_parm_p_t floor_radius  /* <OF>
                               The specification of the radius desired
                               between the side of the pocket and the
                               floor of the pocket. The caller must allocate a
                               UF_MODL_parm_p_t structure, and
                               pass in a pointer to that structure.  The
                               structure will be filled with allocated
                               data which can be freed by calling
                               UF_MODL_free_general_pocket.
                               */
);

/******************************************************************************
Edits the various parameters of the general pocket and reconstructs it
based on these new parameters.

Environment: Internal  and  External
See Also: 
 UF_MODL_ask_general_pocket
 UF_MODL_create_general_pocket
 UF_MODL_free_general_pocket
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_general_pocket(
tag_t general_pocket_tag ,/* <I>
                          Object identifier of the general pocket
                          feature to be modified.
                          */
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   The faces or collector of faces used to define the shape of
                                   the pocket at the placement faces. The
                                   first face is used to determine the target
                                   body.
                                   */
UF_MODL_offset_trans_faces_p_t floor_faces ,/* <I>
                                                The faces or face collectors used to define
                                                the floor of the pocket. The floor can
                                                either be an offset or
                                                translation of the specified
                                                faces or face collector. If it is desired to have
                                                the floor be an offset or
                                                translate of the placement 
                                                faces, then just set the
                                                UF_MODL_faces_p_t
                                                pointer within this input
                                                structure to the placement_faces
                                                pointer value.
                                                */
UF_MODL_pocketpad_outline_p_t outline ,/* <I>
                                       The definition of the curves used to
                                       define the shape of the pocket. The
                                       shape can be defined by a single set of
                                       curves or section builder at either the placement face or
                                       the floor face, and then the other curves or section builder
                                       are derived with a taper angle. The
                                       shape can also be defined by specifying
                                       curves or section builder at both the placement face and
                                       the floor face.
                                       */
UF_MODL_parm_p_t placement_radius ,/* <I>
                                   The specification of the radius desired
                                   between the side of the pocket and the
                                   placement face.
                                   */
UF_MODL_parm_p_t floor_radius  /* <I>
                               The specification of the radius desired
                               between the side of the pocket and the
                               floor of the pocket.
                               */
);

/******************************************************************************
Frees all the memory associated with the parameters returned from
UF_MODL_ask_general_pocket.  Refer to the description of
UF_MODL_create_general_pocket for an example of how to use this function.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_general_pocket
 UF_MODL_create_general_pocket
 UF_MODL_edit_general_pocket
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_free_general_pocket(
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   The faces used to define the shape of
                                   the pocket at the placement faces. The
                                   first face is used to determine the
                                   target body.
                                   */
UF_MODL_offset_trans_faces_p_t floor_faces ,/* <I>
                                                The definition of the floor of
                                                the pocket. The floor can either
                                                be an offset or translation of
                                                the specified faces. If it is
                                                desired to have the floor
                                                be an offset or translate of the
                                                placement faces, then just set i
                                                the UF_MODL_faces_p_t pointer
                                                within this input structure to
                                                the placement_faces pointer
                                                value.
                                                */
UF_MODL_pocketpad_outline_p_t outline ,/* <I>
                                       The definition of the curves used to
                                       define the shape of the pocket. The
                                       shape can be defined by a single set of
                                       curves at either the placement face or
                                       the floor face, and then the other
                                       curves are derived with a taper angle.
                                       The shape can also be defined by
                                       specifying curves at both the
                                       placement face and the floor face.
                                       */
UF_MODL_parm_p_t placement_radius ,/* <I>
                                   The specification of the radius desired
                                   between the side of the pocket and the
                                   placement face.
                                   */
UF_MODL_parm_p_t floor_radius  /* <I>
                               The specification of the radius desired
                               between the side of the pocket and the
                               floor of the pocket.
                               */
);



#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_POCKETS_H_INCLUDED */
