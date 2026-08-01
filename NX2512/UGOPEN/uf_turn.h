/*****************************************************************************
 *            Copyright (c) 2001 EDS PLM Solutions
 *                      Unpublished - All Rights Reserved                       
 * File Name: uf_turn.h
 *
 * 
 *
 * File description:
 *    This file contains the information required to use the UF_TURN module.
 *    This module allows the TURN User Function programmer to interface
 *    with the current CAM session object and the current CAM Object Parameter
 *    Templates object (OPT). See the documentation of the below functions for
 *    a description of the functionality provided by these objects.
 *
 *    For a sample CAM application, please refer to ufd_cam_turn_autoprog.c
 *    in the UGOPEN kit.
 *
 ******************************************************************************/
#ifndef UF_TURN_H_INCLUDED
#define UF_TURN_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_param_indices.h>
#include <uf_cambnd.h>
#include <uf_cam_errors.h>            /* CAM error defines */
#include <libufun_cam_exports.h>


/******************************** Defines *************************************/

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Public Typedefs ********************************/

/*
 * Types for cut region detection in turning.
 */
enum UF_TURN_cut_regions_location_e
{
  UF_TURN_CUT_REGIONS_LOCATED_UNDEFINED = 0,
  UF_TURN_CUT_REGIONS_LOCATED_ON_NEAR_SIDE_OF_CENTERLINE,
  UF_TURN_CUT_REGIONS_LOCATED_ON_FAR_SIDE_OF_CENTERLINE,
  UF_TURN_CUT_REGIONS_LOCATED_ON_BOTH_SIDES_OF_CENTERLINE
};

typedef enum  UF_TURN_cut_regions_location_e UF_TURN_cut_regions_location_t,
             *UF_TURN_cut_regions_location_p_t;

/************************* Public Function Definitions ************************/


/************************************************************************
 *      This routine performs a scan for cut regions representing the
 *      remaining material that can be cut by the currently active turning
 *      tool with respect to the operation referenced and part and blank
 *      geometry specified. The user must configure tool, geometry data and
 *      operation parameters prior to calling this function.
 *      It will return the status value 0 if cut regions could be detected,
 *      and an error code, if no cut regions have been found.
 *
 * Return :
 *           Return code :
 *           = 0 :   successful - admissible cut regions could be detected
 *           > 0 :   failing error number
 *           < 0 :   failing error number
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_ask_cut_regions_exist
(
    tag_t  oper_tag,  /* <I> Tag of the operation for which
                             cut regions are to be found */
    int    *number_of_cut_regions_found,  /* <O> Number of cut regions
                                                 found or 0, if none found */
    double *total_area_of_cut_regions_found,  /* <O> Sums cross-sectional area
                                                     of cut regions found */
    UF_TURN_cut_regions_location_p_t cut_regions_location, /* <O> Reports
                         location of cut regions found relative to centerline */
    char   **message  /* <O> Informational message both for
                             successful detection as for error case */
);

/************************************************************************ 
 *      In some cases there may be multiple non-connected cut regions
 *      representing the remaining material that can be cut by the currently
 *      active turning tool with respect to the operation referenced and part
 *      and blank geometry specified. 
 *      Function 'UF_TURN_ask_cut_region_of_index' finds out, whether a cut
 *      region with positive integer index 'index_of_cut_region' exists, and if
 *      so, returns its cross-sectional area and a Cut Region Selection Point
 *      (in coordinates described relative to ACS) that uniquely identifies 
 *      the indexed cut region.
 *
 *      The user must configure tool, geometry data and operation parameters
 *      prior to calling this function. 
 *      It will return the status value 0 if cut regions could be detected, 
 *      and an error code, if no cut regions have been found. 
 * 
 * Return : 
 *           Return code : 
 *           = 0 : successful - admissible cut regions could be found 
 *           > 0 : failing error number 
 *           < 0 : failing error number 
 * 
 * Environment : Internal  and  External 
 * See Also: 
 * History :  created in V19.0. 
 * 
 ************************************************************************/ 
extern UFUN_CAMEXPORT int UF_TURN_ask_cut_region_of_index
( 
    tag_t       oper_tag, /* <I> Tag of the operation for which
                                 cut regions are to be found                  */ 
    int         index_of_cut_region, /* <I> Index of Cut Region to query      */ 
  
    double      *area_of_cut_region, /* <O> Cross-sectional area of Cut Region
                                            with index (if existing, 0 else)  */ 
    double      selection_point_for_cut_region[3],  /* <O> Returns coordinates
                                  of cut region selection point relative to ACS
                                  uniquely identifying the indexed Cut Region */
    logical     *cut_region_exists, /* <O> True, if cut region having
                                           'index_of_cut_region' exists       */ 
    char        **message  /* <O> Informational message both for
                                  successful detection as for error case      */
);

/************************************************************************
 *      This routine saves the "spinning shape" of the In-Process Workpiece
 *      (IPW) for the operation referenced. The IPW of an operation represents
 *      the status of the workpiece immediately after the operation has been
 *      cut. The IPW can be thought of assuming its "spinning shape"
 *      whenever the turning machine tool's spindle that holds the workpiece
 *      is rotating.
 *      Function 'UF_TURN_save_spinning_ipw_as_part' will return a zero if
 *      the function is successful, otherwise it returns an error number.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_save_spinning_ipw_as_part
(
    tag_t  oper_tag,  /* <I> Tag of the operation for which cut
                             regions are to be detected */
    char   *filename, /* <I> Name of partfile to save IPW to */
    char   **message  /* <O> Informational message both for case where IPW was
                             successfully saved to disk as for error case */
);

/************************************************************************
 *      This routine creates a teachmode suboperation letting you define
 *      the type of suboperation you want to create and finally adds the
 *      newly created teachmode suboperation to the list of suboperations
 *      contained in the given teachmode operation.
 *
 * Return :
 *           Return code :
 *           = 0 :   successful - suboperation could be created
 *           > 0 :   failing error number
 *           < 0 :   failing error number
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_teachmode_create_subop
(
    tag_t oper_tag,   /* <I> Tag of the teachmode operation for which
                             suboperations should be added */
    UF_PARAM_ttmopr_subop_type_t subop_type, /* <I> Type of the suboperation */
    tag_t *subop_tag, /* <O> Tag of the created suboperation */
    char  **message   /* <O> Informational message both for
                             successful detection as for error case */
);

/************************************************************************
 *      This function converts an angle relative to WCS coordinates
 *      into an angle relative to the spindle orientated coordinate
 *      system.
 *
 * Return :
 *           angle relative to the spindle coordinate system
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT double UF_TURN_map_angle_from_wcs
(
    tag_t  oper_tag,   /* <I> Tag of the operation for which angle should be mapped */
    double wcs_angle   /* <I> angle relative to WCS coordinates */
);/* <NEC> */ 

/************************************************************************
 *      This function converts an angle relative to the spindle coordinate
 *      system into an angle relative to WCS coordinates.
 *
 * Return :
 *           angle relative to WCS coordinates
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT double UF_TURN_map_angle_to_wcs
(
    tag_t  oper_tag,   /* <I> Tag of the operation for which angle should be mapped */
    double scs_angle   /* <I> angle relative to spindle coordinate system */
);/* <NEC> */ 

/************************************************************************
 *      This function converts a tool tracking point relative to WCS
 *      coordinates into a tool tracking point relative to the spindle
 *      orientated coordinate system.
 *
 * Return :
 *           tool tracking point relative to the spindle coordinate system
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_tooltrackingpoint_from_wcs
(
    tag_t oper_tag,             /* <I> Tag of the operation for which the
                                       tool tracking point should be mapped */
    int wcs_tooltrackingpoint   /* <I> tool tracking point relative
                                       to WCS coordinates */
);

/************************************************************************
 *      This function converts a tool tracking point relative to the spindle
 *      coordinate system into a tool tracking point relative to WCS
 *      coordinates.
 *
 * Return :
 *           tool tracking point relative to WCS coordinates
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_tooltrackingpoint_to_wcs
(
    tag_t oper_tag,             /* <I> Tag of the operation for which the
                                       tool tracking point should be mapped */
    int scs_tooltrackingpoint   /* <I> tool tracking point relative to
                                       spindle coordinate system */
);

/************************************************************************
 *      This routine converts a 2D vector relative to WCS coordinates
 *      into a 2D vector relative to the spindle orientated coordinate
 *      system.
 *
 * Return :
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_vec2_from_wcs
(
    tag_t oper_tag,      /* <I> Tag of the operation for which 2D vector should be mapped */
    double wcs_vec2[2],  /* <I> 2D vector relative to WCS coordinates */
    double scs_vec2[2]   /* <O> 2D vector relative to spindle coordinate system */
);

/************************************************************************
 *      This routine converts a 2D vector relative to the spindle coordinate
 *      system into a 2D vector relative to WCS coordinates.
 *
 * Return :
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_vec2_to_wcs
(
    tag_t oper_tag,      /* <I> Tag of the operation for which 2D vector should be mapped */
    double scs_vec2[2],  /* <I> 2D vector relative to spindle coordinate system */
    double wcs_vec2[2]   /* <O> 2D vector relative to WCS coordinates */
);

/************************************************************************
 *      This routine converts a 2D point relative to WCS coordinates
 *      into a point relative to the spindle orientated coordinate
 *      system.
 *
 * Return :
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_pnt2_from_wcs
(
    tag_t oper_tag,      /* <I> Tag of the operation for which 2D point should be mapped */
    double wcs_pnt2[2],  /* <I> 2D point relative to WCS coordinates */
    double scs_pnt2[2]   /* <O> 2D point relative to spindle coordinate system */
);

/************************************************************************
 *      This routine converts a 2D point relative to the spindle coordinate
 *      system into a point relative to WCS coordinates.
 *
 * Return :
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_pnt2_to_wcs
(
    tag_t oper_tag,      /* <I> Tag of the operation for which 2D point should be mapped */
    double scs_pnt2[2],  /* <I> 2D point relative to spindle coordinate system */
    double wcs_pnt2[2]   /* <O> 2D point relative to ACS coordinates */
);

/************************************************************************
 *      This routine converts a 3D vector relative to ACS coordinates
 *      into a 2D vector relative to the spindle coordinate system.
 *
 * Return :
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_vec3_from_acs
(
    tag_t oper_tag,      /* <I> Tag of the operation for which 3D vector should be mapped */
    double acs_vec3[3],  /* <I> 3D vector relative to ACS coordinates */
    double scs_vec2[2]   /* <O> 2D vector relative to spindle coordinate system */
);

/************************************************************************
 *      This routine converts a 2D vector relative to the spindle coordinate
 *      system into a 3D vector relative to ACS coordinates.
 *
 * Return :
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_vec2_to_acs
(
    tag_t oper_tag,      /* <I> Tag of the operation for which 3D vector should be mapped */
    double scs_vec2[2],  /* <I> 2D vector relative to spindle coordinate system */
    double acs_vec3[3]   /* <O> 3D vector relative to ACS coordinates */
);

/************************************************************************
 *      This routine converts a 3D point relative to ACS coordinates
 *      into a 2D point relative to the spindle orientated coordinate system.
 *
 * Return :
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_pnt3_from_acs
(
    tag_t oper_tag,      /* <I> Tag of the operation for which 3D point should be mapped */
    double acs_pnt3[3],  /* <I> 3D point relative to ACS coordinates */
    double scs_pnt2[2]   /* <O> 2D point relative to spindle coordinate system */
);

/************************************************************************
 *      This routine converts a 2D point relative to the spindle coordinate
 *      system into a 3D point relative to ACS coordinates.
 *
 * Return :
 *
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_map_pnt2_to_acs
(
    tag_t oper_tag,      /* <I> Tag of the operation for which 3D point should be mapped */
    double scs_pnt2[2],  /* <I> 2D point relative to spindle coordinate system */
    double acs_pnt3[3]   /* <O> 3D point relative to ACS coordinates */
);

/************************************************************************
 *      This routine computes a box around the curve resulting from the 
 *      cross-sectioned in-process workpiece.
 *      It provides: 
 *      - origin, length and diameter of the workpiece
 *      - two points defining lower left and upper right corner of the box
 *        described in 2D "workplane coordinates" relative to the spindle
 *        coordinate system as well as
 *      - the four corner points of the box in 3D coordinates relative to ACS.
 *
 * Return :
 *      Return code :
 *      = 0 :   successful - min max workpiece box could be created
 *      > 0 :   failing error number
 *      < 0 :   failing error number
 *         
 * Environment : Internal  and  External
 * See Also:
 * History :     created in V19.0
 *
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_TURN_ipw_box
(
    tag_t  oper_tag,                 /* <I> Tag of the operation for which
                                            min max box of IPW has to be created */   
    double *length,                  /* <O> length of the workpiece  */
    double *diameter,                /* <O> diameter of the workpiece  */
    double bottom_left_in_plane[2],  /* <O> bottom left position of workpiece in plane */ 
    double top_right_in_plane[2],    /* <O> top right position of workpiece in plane */ 
    double bottom_left_pnt3[3],      /* <O> bottom left position of workpiece */ 
    double bottom_right_pnt3[3],     /* <O> bottom right position of workpiece */ 
    double top_left_pnt3[3],         /* <O> top left position of workpiece */ 
    double top_right_pnt3[3],        /* <O> top right position of workpiece */
    char   **message                 /* <O> Informational message both for
                                            successful detection as for error case */
);

/***************************************************************************
 *
 * This routine creates a turning blank of type cylinder or tube 
 * (UF_PARAM_turn_workpiece_type_cylinder or UF_PARAM_turn_workpiece_type_tube). 
 * Direction of the blank (UF_PARAM_turn_workpiece_direction_towards_head_stock
 * or UF_PARAM_turn_workpiece_direction_from_head_stock), mounting point for
 * positioning, length, outer and additional inner diameter for tube must be
 * specified as input parameters to this function.
 *
 * Return :
 *      Return code :
 *      = 0 :   successful - turn blank could be created
 *      > 0 :   failing error number
 *      < 0 :   failing error number
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_TURN_create_parametric_blank
(
    tag_t                               object_tag,      /* <I> the parent object of the 
                                                                blank */
    UF_PARAM_turn_workpiece_type_t      workpiece_type,  /* <I> the type of the blank */
    UF_PARAM_turn_workpiece_direction_t direction,       /* <I> the direction of the parametric blank */  
    tag_t                               mounting_point,  /* <I> the mounting point of the parametric blank */      
    double                              length,          /* <I> the length of the parametric blank */
    double                              outer_diameter,  /* <I> the diameter of the parametric blank */
    double                              inner_diameter   /* <I> the inner diameter of the tube blank */
);
/***************************************************************************
 *
 * This routine creates a turning blank from a single boundary from edges/curves
 * (type UF_PARAM_turn_workpiece_type_curves). 
 * The count of edges/curves, the edge/curve tags with boundary and application
 * data and stock values for radial, face and equidistant stock are input
 * parameters for this function.
 *
 * Return :
 *      Return code :
 *      = 0 :   successful - turn blank could be created
 *      > 0 :   failing error number
 *      < 0 :   failing error number
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_TURN_create_blank_from_boundary
(
    tag_t                               object_tag,      /* <I> the parent object of the 
                                                                boundary */
    int                                 count,           /* <I> the count of edges/curves */
    tag_t                               *curves,         /* <I,len:count>
                                                                the edge/curve tags from which  
                                                                a boundary will be created */
    UF_CAMBND_boundary_data_p_t         boundary_data,   /* <I> the boundary data */
    UF_CAMBND_app_data_p_t              *app_data,       /* <I,len:count>
                                                                the application data for each member */
    double                              stock_equi,      /* <I> the equidistant stock for the blank boundary */
    double                              stock_face,      /* <I> the face stock for the blank boundary*/
    double                              stock_radial     /* <I> the radial stock for the blank boundary*/
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_TURN_H_INCLUDED */
