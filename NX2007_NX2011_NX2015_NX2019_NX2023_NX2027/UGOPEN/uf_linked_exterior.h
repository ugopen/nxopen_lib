/*****************************************************************************
             Copyright (c) 2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open API modeling routines to create, edit and inquire about linked exterior

*****************************************************************************/

#ifndef UF_LINKED_EXTERIOR
#define UF_LINKED_EXTERIOR


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/************************************************************************
 *  This function identifies Exterior Faces from the array of bodies using
 *  a hidden line solution. The context of the bodies is determined from
 *  the xforms given.
 *
 * See Also: UF_MODL_create_linked_exterior
 *           UF_MODL_ask_linked_exterior
 *           UF_MODL_edit_linked_exterior
 *           UF_MODL_identify_exterior_using_rays
 *
 * Environment : Internal and External
 *
 * History : Released in V18.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_identify_exterior_using_hl (
       int     num_bodies,        /* <I> Number of tags in the bodies array.    */
       tag_t   *bodies,           /* <I,len:num_bodies>
                                         Array of body tags to identify faces from. */
       tag_t   *xforms,           /* <I,len:num_bodies>
                                         Array of xforms. One for each body,
                                         determines the position of the body
                                         relative to its source geometry.
                                         NULL_TAG implies no transformation.
                                  */
       int     num_dirs,         /* <I> Number of directions */
       double  direction[][3],   /* <I,len:num_dirs> Direction to apply hidden line solution from */
       double  chordal_tol,      /* <I> Chordal tolerance for edges */
       int     resolution,       /* <I> Determines how many hatch lines drawn
                                    per face. May be one of:
                                      UF_LINKED_HL_RES_COARSE
                                      UF_LINKED_HL_RES_NORMAL
                                      UF_LINKED_HL_RES_FINE
                                      UF_LINKED_HL_RES_VERY_FINE
                                  */
       int     *num_faces,        /* <I/O> Number of tags in the faces array.
                                     If input is > 0 will reallocate and add
                                     external faces to existing output arrays
                                  */
       tag_t   **faces,           /* <OF,len:num_faces>
                                          Array of face tags.            */
       int     **body_index       /* <OF,len:num_faces>
                                     Array of indices giving the body/xform
                                     the face came from.
                                   */
   );

/************************************************************************
 *  This function identifies Exterior Faces from the array of transformed
 *  bodies by firing a ray at each face. The context of the bodies is
 *  determined from the xforms given. The code will not fire rays
 *  at input faces already identified as exterior.
 *
 * See Also: UF_MODL_create_linked_exterior
 *           UF_MODL_ask_linked_exterior
 *           UF_MODL_edit_linked_exterior
 *           UF_MODL_identify_exterior_using_hl
 *
 * Environment : Internal and External
 *
 * History : Released in V18.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_identify_exterior_using_rays (
       int     num_bodies,        /* <I> Number of tags in the bodies array.    */
       tag_t   *bodies,           /* <I,len:num_bodies>
                                         Array of body tags to identify faces from. */
       tag_t   *xforms,           /* <I,len:num_bodies>
                                         Array of xforms. One for each body,
                                         determines the position of the body
                                         relative to its source geometry.
                                         NULL_TAG implies no transformation.
                                  */
       double  origin[3],        /* <I> Point to fire rays from from when
                                    ray_type = UF_LINKED_RAY_FROM_POINT
                                  */
       double  chordal_tol,      /* <I> Chordal tolerance for edges */
       int     ray_type,         /* <I> Determines orign of rays fired at each face.
                                     May be one of:
                                      UF_LINKED_RAY_ALONG_NORMS
                                      UF_LINKED_RAY_ABOVE_NORMS
                                      UF_LINKED_RAY_FROM_POINT
                                  */
       int     *num_faces,        /* <I/O> Number of tags in the faces array.
                                     If input is > 0 will reallocate and add
                                     external faces to existing output arrays
                                  */
       tag_t   **faces,           /* <OF,len:num_faces>
                                          Array of exterior faces.             */
       int     **body_index       /* <OF,len:num_faces>
                                          Array of indices giving the body/xform
                                          the face came from.
                                   */
   );

/************************************************************************
 *  This function creates an Linked Exterior feature, and its
 *  associated sheet bodies, in the same part as object_in_part.  The
 *  input faces will extracted as one or more, possibly disjoint,
 *  regions.  The xform gives the context for each face.  Adjacent
 *  faces which come from the same body and share an xform will be
 *  joined into single sheet body. Input faces cannot be occurrences.
 *  This feature is implemeted as a feature set which owns hidden
 *  subfeatures similar to Linked Regions. The subfeatures should not be
 *  edited or deleted individually.
 *
 * See Also: UF_MODL_ask_linked_exterior
 *           UF_MODL_edit_linked_exterior
 *           UF_MODL_identify_exterior_using_hl
 *           UF_MODL_identify_exterior_using_rays
 *
 * Environment : Internal and External
 *
 * History : Released in V18.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_create_linked_exterior (
   UF_MODL_linked_ext_p_t  ext_data,     /* <I> Feature data */
   tag_t                    *feature_tag /* <O> Feature tag  */
   );

/************************************************************************
 *  This function reads the data of a Linked Exterior feature.
 *  This feature is implemeted as a feature set which owns hidden
 *  subfeatures similar to Linked Regions. The subfeatures should not be
 *  edited or deleted individually. Bodies are owned by the hidden subfeatures.
 *
 *
 * See Also: UF_MODL_create_linked_exterior
 *           UF_MODL_edit_linked_exterior
 *           UF_MODL_identify_exterior_using_hl
 *           UF_MODL_identify_exterior_using_rays
 *           UF_MODL_ask_all_members_of_set
 *
 * Environment : Internal and External
 *
 * History : Released in V18.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_linked_exterior (
   tag_t                    feature_tag, /* <I> Feature tag  */
   UF_MODL_linked_ext_p_t  ext_data,     /* <OF>
                                         Feature data.  The caller defines
                                         the UF_MODL_linked_ext_t structure,
                                         and pass in a pointer to it.  This
                                         routine will fill in the structure
                                         based on the feature tag.  The caller
                                         is responsible for freeing any data
                                         returned in arrays.
                                         */
   int    *num_groups,   /* <O>  Number of groups this feature owns              */
   tag_t  **groups,      /* <OF,len:num_groups> Groups this feature owns (may be null)          */
   int    *num_subfeats, /* <O>  Number of subfeatures this feature owns         */
   tag_t  **subfeats,    /* <OF,len:num_subfeats> Subfeatures this feature owns (may be null)     */
   double mass_props[47] /* <O>  Mass properties (same as UF_MODL_ask_mass_props_3d)
                                   [0]     = Surface Area
                                   [1]     = Volume
                                   [2]     = Mass
                                   [3-5]   = Center Of Mass (COFM), WCS
                                   [6-8]   = First Moments (centroidal)
                                   [9-11]  = Moments Of Inertia, WCS
                                   [12-14] = Moments Of Inertia (centroidal)
                                   [15]    = Spherical Moment Of Inertia
                                   [16-18] = Inertia Products, WCS
                                   [19-21] = Inertia Products (centroidal)
                                   [22-30] = Principal Axes, WCS
                                   [31-33] = Principal Moments (centroidal)
                                   [34-36] = Radii Of Gyration, WCS
                                   [37-39] = Radii Of Gyration (centroidal)
                                   [40]    = Spherical Radius Of Gyration
                                   [41-45] = Unused
                                   [46]    = Density
                          */
   );

/************************************************************************
 *  This function edits a Linked Exterior feature.
 *
 * See Also: UF_MODL_create_linked_exterior
 *           UF_MODL_ask_linked_exterior
 *           UF_MODL_identify_exterior_using_hl
 *           UF_MODL_identify_exterior_using_rays
 *
 * Environment : Internal and External
 *
 * History : Released in V18.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_linked_exterior (
   tag_t                    feature_tag, /* <I> Feature tag  */
   UF_MODL_linked_ext_p_t  ext_data      /* <I> Feature data */
   );


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_LINKED_EXTERIOR  */
