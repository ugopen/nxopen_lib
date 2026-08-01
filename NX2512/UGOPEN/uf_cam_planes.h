/*******************************************************************************
                         Copyright (c) 2001 EDS, Inc.
                      Unpublished - All rights reserved
******************************************************************************
 ******************************************************************************
 *
 * 
 *
 * File description:
 *
 * This file contains the Open C API interface to Special planes in CAM
 *   Currently Clearance and Lower Limit Planes are the only ones supported.
 *
 * The CAM Plane routines in this file enable you to:
 *   . Define, edit, and query the origin and normal of special planes
 *   . Set and ask the status of a special plane
 *   . Set and ask the usage of a special plane
 *    
 ******************************************************************************/
#ifndef UF_CAM_PLANES_H_INCLUDED
#define UF_CAM_PLANES_H_INCLUDED


#include <uf.h>
#include <uf_defs.h>
#include <uf_cam.h>
#include <libufun_cam_exports.h>
#include <uf_param_indices.h>


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

/* **************************************************************************
   ******************      Functions Relating to Planes     *****************
   **************************************************************************
*/

/***************************************************************************
 *
 * Query the origin and normal of a clearance plane
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_ask_clear_plane_data
(
    tag_t      object_tag,        /* <I> the parent object of the plane */ 
    double     origin[3],         /* <O> the 3D origin of the plane */
    double     normal[3]          /* <O> the 3D normal of the plane */ 
    );
 
/***************************************************************************
 *
 * Define/edit the origin and normal of a clearance plane
 * 
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_set_clear_plane_data
(
    tag_t      object_tag,        /* <I> the parent object of the plane */ 
    double     origin[3],         /* <I> the 3D origin of the plane */
    double     normal[3]          /* <I> the 3D normal of the plane */ 
    );

/***************************************************************************
 *
 * Query the status of a clearance plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_ask_clear_plane_status
(
    tag_t                       object_tag, /* <I> the parent object of the plane */ 
    UF_PARAM_clrplane_status_t  *status     /* <O> the status of the plane */
 );

/***************************************************************************
 *
 * Set the status of a clearance plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_set_clear_plane_status
(
    tag_t                       object_tag, /* <I> the parent object of the plane */ 
    UF_PARAM_clrplane_status_t  status      /* <I> the status of the plane */
 );

/***************************************************************************
 *
 * Query the usage of a clearance plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_ask_clear_plane_usage
(
    tag_t                      object_tag, /* <I> the parent object of the plane */ 
    UF_PARAM_clrplane_usage_t  *usage      /* <O> clearance plane usage */
    );

/***************************************************************************
 *
 * Set the usage of a clearance plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_set_clear_plane_usage
(
    tag_t                      object_tag, /* <I> the parent object of the plane */ 
    UF_PARAM_clrplane_usage_t  usage       /* <I> clearance plane usage */
    );

/***************************************************************************
 *
 * Query the tag of a clearance plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_ask_clear_plane_tag
(
    tag_t      object_tag,        /* <I> the parent object of the plane */ 
    tag_t      *target_tag        /* <O> the tag of an UF_xform_type entity
                                         representing the clearance plane */
    );

/***************************************************************************
 *
 * Set the tag of a clearance plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_set_clear_plane_tag
(
    tag_t      object_tag,        /* <I> the parent object of the plane */ 
    tag_t      target_tag         /* <I> the tag of an UF_xform_type entity
                                         representing the clearance plane */
    );

/***************************************************************************
 *
 * Query the origin and normal of a lower limit plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_ask_lower_limit_plane_data
(
    tag_t      object_tag,        /* <I> the parent object of the plane */ 
    double     origin[3],         /* <O> the 3D origin of the plane */
    double     normal[3]          /* <O> the 3D normal of the plane */ 
    );
 
/***************************************************************************
 *
 * Define/edit the origin and normal of a lower limit plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_set_lower_limit_plane_data
(
    tag_t      object_tag,        /* <I> the parent object of the plane */ 
    double     origin[3],         /* <I> the 3D origin of the plane */
    double     normal[3]          /* <I> the 3D normal of the plane */ 
    );

/***************************************************************************
 *
 * Query the status of a lower limit plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_ask_lower_limit_plane_status
(
    tag_t                      object_tag, /* <I> the parent object of the plane */ 
    UF_PARAM_lwplane_status_t  *status     /* <O> the status of the plane */
 );

/***************************************************************************
 *
 * Set the status of a lower limit plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_set_lower_limit_plane_status
(
    tag_t                      object_tag, /* <I> the parent object of the plane */ 
    UF_PARAM_lwplane_status_t  status      /* <I> the status of the plane */
 );

/***************************************************************************
 *
 * Query the usage of a lower limit plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_ask_lower_limit_plane_usage
(
    tag_t                     object_tag, /* <I> the parent object of the plane */ 
    UF_PARAM_lwplane_usage_t  *usage      /* <O> lower limit plane usage */
    );

/***************************************************************************
 *
 * Set the usage of a lower limit plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_set_lower_limit_plane_usage
(
    tag_t                     object_tag, /* <I> the parent object of the plane */ 
    UF_PARAM_lwplane_usage_t  usage       /* <I> lower limit plane usage */
    );

/***************************************************************************
 *
 * Query the tag of a lower limit plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_ask_lower_limit_plane_tag
(
    tag_t      object_tag,        /* <I> the parent object of the plane */ 
    tag_t      *target_tag        /* <O> the tag of an UF_xform_type entity
                                         representing the lower limit plane */
    );

/***************************************************************************
 *
 * Set the tag of a lower limit plane
 *
 * Return :
 *           Return code :
 * 
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAM_set_lower_limit_plane_tag
(
    tag_t      object_tag,        /* <I> the parent object of the plane */ 
    tag_t      target_tag         /* <I> the tag of an UF_xform_type entity
                                         representing the lower limit plane */
    );
                  
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CAM_PLANES_H_INCLUDED */
