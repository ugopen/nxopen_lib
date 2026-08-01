/*==============================================================================
                Copyright (c) 2001,2002,2003,2005 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
================================================================================
 *****************************************************************************
 *
 *
 * 
 *
 * File description:
 *
 * This file contains the Open API interface to geometry in CAM.
 *
 * The CAM geometry routines in this file enable you to:
 *   . Append entities to CAM geometry
 *   . Get CAM geometry items
 *   . Delete CAM geometry
 *   . Get the item entity
 *   . Get the item application data
 *   . Set the item application data
 *   . Delete a single item from CAM geometry
 *   . Evaluate a surface at a given (u,v) parameter
 *
 ******************************************************************************/
#ifndef UF_CAMGEOM_H_INCLUDED
#define UF_CAMGEOM_H_INCLUDED


#include <uf.h>
#include <uf_defs.h>
#include <uf_cam.h>
#include <uf_param_indices.h>
#include <libufun_cam_exports.h>
#include <uf_modl_types.h>


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
 * An object which is used to access a CAM geometry.
 */
typedef void  *UF_CAMGEOM_item_t;
typedef void  *UF_CAMGEOM_list_t;

/*
 * The application data for CAMGEOM items:
 *
 * The following information shows the types of application data
 * allowed by the objects and the geometry types.
 * An error code is returned by the functions if a wrong type
 * of application data is set.
 *
 *   Mill geometry Group:
 *     Part Geometry:       Offset
 *     Blank Geometry:      None
 *     Check Geometry:      None
 *
 *   Mill area Group:
 *     Part Geometry:       Offset
 *     Check Geometry:      None
 *     Cut area Geometry:   None
 *     Wall Geometry:       None
 *
 *   Facing Operation:
 *     Part Geometry:       None
 *     Check Geometry:      None
 *     Cut area Geometry:   None
 *     Wall Geometry:       None
 *
 *   Cavity Mill Operation:
 *     Part Geometry:       Stock, Tolerances
 *     Blank Geometry:      Stock, Tolerances
 *     Check Geometry:      None
 *
 *   ZLevel Mill Operation:
 *     Part Geometry:       Stock, Tolerances
 *     Check Geometry:      None
 *     Cut area Geometry:   None
 *
 *   Surface Contour Operation:
 *     Part Geometry:       Cut Stock, Tolerances, Feedrate
 *     Check Geometry:      Cut Stock, Tolerances, Avoidance
 *     Cut area Geometry:   None
 *
 */

struct UF_CAMGEOM_app_data_s{

    int                     has_stock;          /* Stock flag.
                                                   Set to 1 if used, or else set to 0. */
    double                  stock;              /* Stock value. */

    int                     has_cut_stock;      /* Cut stock flag.
                                                   Set to 1 if used, or else set to 0. */
    double                  cut_stock[3];       /* Cut stock value:
                                                   cut_stock[0] = initial stock
                                                   cut_stock[1] = final stock
                                                   cut_stock[2] = safe clearance */

    int                     has_tolerances;     /* Tolerance flag.
                                                   Set to 1 if used, or else set to 0. */
    double                  tolerances[2];      /* Tolerance value:
                                                   tolerance[0] = intol
                                                   tolerance[1] = outol */

    int                     has_feedrate;       /* Feed rate flag.
                                                   Set to 1 if used, or else set to 0. */
    UF_CAM_feedrate_unit_t  feedrate_unit;      /* Feed rate unit. */
    double                  feedrate_value;     /* Feed rate value. */

    int                     has_offset;         /* Offset flag.
                                                   Set to 1 if used, or else set to 0. */
    int                     offsetType;         /* Offset type flag.
                                                   0 = distance, 1 = % of tool */
    double                  nominalOffset;      /* distance for offsetType = 0,
                                                   percentage of tool for offsetType = 1 */
    double                  offset;             /* Offset value, either specified or computed. */

    int                     has_avoidance_type; /* Avoidance type flag.
                                                   Set to 1 if used, or else set to 0. */
    UF_CAM_avoidance_type_t avoidance_type;     /* Avoidance type value. */

};

typedef struct UF_CAMGEOM_app_data_s UF_CAMGEOM_app_data_t, *UF_CAMGEOM_app_data_p_t;

/*  custom point types  */
enum UF_CAMGEOM_custom_point_type_e
{
    UF_CAMGEOM_predrill_engage_type,
    UF_CAMGEOM_cut_region_start_type
};
typedef enum UF_CAMGEOM_custom_point_type_e UF_CAMGEOM_custom_point_type_t;

struct UF_CAMGEOM_custom_point_s
{
    tag_t point_tag;      /*  tag of defined point - may be null.  */
    double point_acs[3];  /*  point coordinates in Absolute part units.
                              On input, if the point_tag is valid, the
                              coordinates from that entity will be used
                              and this array will be ignored.  On output,
                              this array will be filled with the data from
                              the point tag entity if it is specified,
                              otherwise the data from the operation record
                              will be returned.  */
    double upper_depth;   /*  The upper depth value.  This is only used
                              for cut region start points in Planar and
                              Cavity Milling.  May be 0.0  */
    double lower_depth;   /*  The lower depth value.  This is only used
                              for cut region start points in Planar and
                              Cavity Milling.  May be 0.0  */
    double depth;         /*  The depth value.  This is only used for
                              predrill engage points in Planar and Cavity
                              Milling.  May be 0.0  */
};
typedef struct UF_CAMGEOM_custom_point_s
               UF_CAMGEOM_custom_point_t, *UF_CAMGEOM_custom_point_p_t;


/*
   **************************************************************************
   ******************     Functions Relating to Geometry    *****************
   **************************************************************************
*/

/***************************************************************************
 *
 * Appends a list of geometry entities to the object .
 *
 * The allowed types of entities are the solid body, solid sheet body, face,
 * and curve for the most objects and their geometry types, except the following:
 *
 *     Part Geometry of Facing Operation allows only solid body and solid sheet body.
 *     Cut Area allows only solid sheet body and face.
 *     Trim Geometry is not allowed.
 *
 * If the entity list contains any invalid entities, an error code is returned
 * and no geometry entity is appended.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_append_items
(
    tag_t                   object_tag,       /* <I> the parent object of the
                                                     geometry */
    UF_CAM_geom_type_t      geometry_type,    /* <I> the type of the geometry */
    int                     count,            /* <I> the count of geometry entities */
    tag_t                   *entity_list,     /* <I,len:count> count
                                                     the list of geometry entities */
    UF_CAMGEOM_app_data_p_t *app_data         /* <I,len:count> count
                                                     the list of app_data pointers for
                                                     each geometry entities */
);

/***************************************************************************
 *
 * Gets all the geometry items of given type from the object.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_ask_items
(
    tag_t                 object_tag,       /* <I>  the parent object of the
                                                    geometry */
    UF_CAM_geom_type_t    geometry_type,    /* <I>  the type of the geometry */
    int                   *count,           /* <O>  the count of geometry items */
    UF_CAMGEOM_item_t     **items           /* <OF,len:count> the list of geometry items
                                                    it must be freed using UF_free */
);

/***************************************************************************
 *
 * Gets all the geometry items of a collector in the geometry list and returns
 *   entity occurrences of the underlying geometry.
 *
 * NOTE:  Any app data for the items held by the collector is stored with the
 *        collector and must be accessed using its UF_CAMGEOM_item_t.
 *
 * Environment: Internal and External
 *
 * See Also:
 * History: Released in NX8.0.1
****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAMGEOM_ask_collector_items
(
    UF_CAMGEOM_item_t    object_tag,           /* <I>  geometry item containing a collector */
    int                  *count,               /* <O>  the count of geometry items */
    tag_t                **items              /* <OF,len:count> the list of geometry item tags.
                                                      it must be freed using UF_free */
);

/***************************************************************************
 *
 * Gets the object providing the specified geometry type to the input object.
 *
 * Environment: Internal  and  External
 *
 * Note:  Input object may be either an operation or geometry group
 *
 * See Also:
 * History: Released in NX3.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_ask_geom_provider
(
    tag_t         object_tag,       /* <I>  the object being provided geometry */
    UF_CAM_geom_type_t  geometry_type,    /* <I>  the type of the geometry */
    tag_t *provider_tag             /* <O>  tag of the object providing the
                                            geometry to object  */
);

/***************************************************************************
 *
 * Deletes all the geometry items of the given type from the object.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ***************************************************************************/
extern UFUN_CAMEXPORT int UF_CAMGEOM_delete_geometry
(
    tag_t              object_tag,          /* <I> the parent object of the
                                                   geometry */
    UF_CAM_geom_type_t geometry_type        /* <I> the type of the geometry */
);

/***************************************************************************
 *
 * Gets the geometry entity of the item.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_ask_item_entity
(
    UF_CAMGEOM_item_t     item,             /* <I> the geometry item */
    tag_t                 *entity           /* <O> the item entity */
);

/***************************************************************************
 *
 * Gets the application data of the item.
 *
 * The memory for application data must be allocated by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_ask_item_app_data
(
    UF_CAMGEOM_item_t     item,             /* <I> the geometry item */
    UF_CAMGEOM_app_data_t *app_data         /* <O> the application data of the item */
);

/***************************************************************************
 *
 * Sets the application data of the item.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_set_item_app_data
(
    tag_t                     object_tag,       /* <I> the parent object of the
                                                       geometry */
    UF_CAM_geom_type_t        geometry_type,    /* <I> the type of the geometry */
    UF_CAMGEOM_item_t         item,             /* <I> the geometry item */
    UF_CAMGEOM_app_data_p_t   app_data          /* <I> the application data of the item */
);

/***************************************************************************
 *
 * Deletes the item from the geometry of the given type.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_delete_item
(
    tag_t                 object_tag,       /* <I> the parent object of the
                                                   geometry */
    UF_CAM_geom_type_t    geometry_type,    /* <I> the type of the geometry */
    UF_CAMGEOM_item_t     item              /* <I> the item to be deleted */
);

/***************************************************************************
 *
 * Evaluates a surface at a input parameter position.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_eval_surface
(
    tag_t                 object_tag,       /* <I> the parent object */
    UF_CAM_geom_type_t    geometry_type,    /* <I> Part, drive, check, etc.  */
    tag_t                 entity,           /* <I> entity to be evaluated */
    double                uv[2],              /* <I> u,v parameter position */
    UF_MODL_SRF_VALUE_p_t srf_value         /* <O> evaluation data structure */
);

/***************************************************************************
 *
 * Returns the parameteric max-min box for a face geom_item
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_ask_item_maxmin
(
    tag_t                 object_tag,       /* <I> the parent object */
    UF_CAM_geom_type_t    geometry_type,    /* <I> Part, drive, check, etc.  */
    tag_t                 entity,           /* <I> entity to be evaluated */
    double               *maxmin            /* <O> u,v maxmin box of face */
);
 
/***************************************************************************
 *
 * Appends a list of custom points to the operation.
 *
 * The data used varies by operation type:
 *   Planar Milling:
 *     Predrill Engage Points:  A single depth value (may be 0.0).
 *     Cut Region Start Points: Upper Depth and Lower Depth values (may be 0.0).
 *   Cavity Milling:
 *     Predrill Engage Points:  A single depth value (may be 0.0).
 *     Cut Region Start Points: Upper Depth and Lower Depth values (may be 0.0).
 *   Face Milling:
 *     Predrill Engage Points:  No depth used.
 *     Cut Region Start Points: No depth used.
 *   Surface Contouring:
 *     Predrill Engage Points:  Not valid.
 *     Cut Region Start Points: No depth used.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_append_custom_points
(
    tag_t                   object_tag,             /* <I> the target operation */
    UF_CAMGEOM_custom_point_type_t   point_type,    /* <I> the type of the point */
    int                     count,                  /* <I> the count of point entities */
    UF_CAMGEOM_custom_point_p_t *point_data         /* <I,len:count> list of point data pointers */
);

/***************************************************************************
 *
 * Gets the list of custom points and their app_data for the operation.
 *
 * The data used varies by operation type:
 *   Planar Milling:
 *     Predrill Engage Points:  A single depth value (may be 0.0).
 *     Cut Region Start Points: Upper Depth and Lower Depth values (may be 0.0).
 *   Cavity Milling:
 *     Predrill Engage Points:  A single depth value (may be 0.0).
 *     Cut Region Start Points: Upper Depth and Lower Depth values (may be 0.0).
 *   Face Milling:
 *     Predrill Engage Points:  Not used.
 *     Cut Region Start Points: Not used
 *   Surface Contouring:
 *     Predrill Engage Points:  Not valid.
 *     Cut Region Start Points: No depth used.
 *
 *  NOTE:
 *    Space for the point data list will be allocated by this function.
 *    It must be freed by the calling program using UF_free on each entry in
 *    the list and then the list pointer itself when the information
 *    is no longer needed.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_ask_custom_points
(
    tag_t                   object_tag,           /* <I> the target operation */
    UF_CAMGEOM_custom_point_type_t   point_type,  /* <I> the type of the point */
    int                     *count,               /* <O> the count of point entities */
    UF_CAMGEOM_custom_point_p_t **point_data      /* <OF,len:count> list of point data pointers for
                                                             each point entity */
);
 
/***************************************************************************
 *
 * Deletes a list of custom points from the operation.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMGEOM_delete_custom_points
(
    tag_t                   object_tag,            /* <I> the target operation */
    UF_CAMGEOM_custom_point_type_t   point_type    /* <I> the type of the point */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CAMGEOM_H_INCLUDED */

