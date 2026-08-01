/*******************************************************************************
                Copyright (c) 2001 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
================================================================================
 ******************************************************************************
 *
 * 
 *
 * File description:
 *
 * This file contains the Open API interface to HMOP in CAM.
 *
 ******************************************************************************/
#ifndef UF_HMOP_H_INCLUDED
#define UF_HMOP_H_INCLUDED


#include <uf.h>
#include <uf_defs.h>
#include <uf_cam.h>
#include <uf_fbm_geom.h>
#include <libufun_cam_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/*
   **************************************************************************
   ***************************     Definitions    ***************************
   **************************************************************************
*/

/*
   **************************************************************************
   ***************************     Structures     ***************************
   **************************************************************************
*/

/*
   **************************************************************************
   ******************     Functions Relating to HMOP    *****************
   **************************************************************************
*/


/*******************************************************************************

   Return Hole Top of the representative feature object.
   The representative feature is obtained from the geometry
   parent of the operation( which should be of the type FBM_geom ).

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_ask_hole_top

(
   tag_t               hmop_tag,      /* <I> The tag of the hole making operation of interest */
   UF_NCFEAT_t         rep_feature,   /* <I> A representative feature. */
   tag_t               *smart_point   /* <O> Hole Top of rep_feature. */
);

/*******************************************************************************

   Set Hole Top to the representative feature object. The Hole Top tag must be
   associated to an entity of the representative feature object.
   Otherwise, it will return an error.
   The representative feature is obtained from the geometry
   parent of the operation ( which should be of the type FBM_geom ).

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_set_hole_top
(
   tag_t                  hmop_tag,      /* <I> The tag of the hole making operation of interest */
   UF_NCFEAT_t            rep_feature,   /* <I> A representative feature. */
   tag_t                  *smart_point   /*<I> Smart point associated to one of the entities of  rep_feature. */
);

/*******************************************************************************

   Return Hole Axis of the representative feature object.
   The representative feature is obtained from the geometry
   parent of the operation( which should be of the type FBM_geom ).

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_ask_hole_axis
(
   tag_t                 hmop_tag,      /* <I> The tag of the hole making operation of interest */
   UF_NCFEAT_t           rep_feature,   /* <I> A representative feature. */
   tag_t                 *smart_vector  /* <O> Hole Axis of rep_feature. */
);


/*******************************************************************************

   Set Hole Axis to the representative feature object. The Hole Axis tag
   must be associated to an entity of the representative feature object.
   Otherwise, it will return an error.
   The representative feature must be obtained from the geometry
   parent of the operation( which should be of the type FBM_geom ).

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_set_hole_axis
(
   tag_t             hmop_tag,      /* <I> The tag of the hole making operation of interest */
   UF_NCFEAT_t       rep_feature,   /* <I> A representative feature. */
   tag_t             *smart_vector  /* <I> Smart vector associated to one of the entities of  rep_feature. */
);



/*******************************************************************************

   Return Hole Depth of of the representative feature object.
   The representative feature must be obtained from the geometry
   parent of the operation( which should be of the type FBM_geom ).

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_ask_hole_depth
(
   tag_t                 hmop_tag,     /* <I> The tag of the hole making operation of interest */
   UF_NCFEAT_t           rep_feature,  /* <I> A representative feature. */
   tag_t                 *smart_point  /* <O> Hole Depth of rep_feature. */
);

/*******************************************************************************

   Set Hole Depth to the representative feature object. The Hole Depth tag
   must be associated to an entity of the representative feature object.
   Otherwise, it will return an error.
   The representative feature must be obtained from the geometry
   parent of the operation( which should be of the type FBM_geom ).
   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_set_hole_depth
(
   tag_t                  hmop_tag,     /* <I> The tag of the hole making operation of interest */
   UF_NCFEAT_t            rep_feature,  /* <I> A representative feature. */
   tag_t                  *smart_point  /* <I> Smart point associated to one of the entities of rep_feature. */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_HMOP_H_INCLUDED */
