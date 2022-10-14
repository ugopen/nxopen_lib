/*==============================================================================
                Copyright (c) 2001 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
================================================================================
 ******************************************************************************
 *
 * 
 *
 * File description:
 *
 * This file contains the Open API interface to boundary in CAM.
 *
 * The CAM boundary routines in this file enable you to:
 *   . Append boundaries created from a planar face
 *   . Append a single boundary created from a list of curves/edges
 *   . Get boundaries
 *   . Delete all boundaries of a geometry type
 *   . Delete a single boundary
 *   . Get boundary data
 *   . Get boundary application data
 *   . Set boundary application data
 *   . Get boundary items
 *   . Get item entity
 *   . Get item application data
 *   . Set item application data
 *   . Get boundary group application data (offset)
 *   . Set boundary group application data (offset)
 *   . Get item group application data (offset)
 *   . Set item group application data (offset)
 *   . Determine whether boundary geometry is inherited
 *   . Ask item user defined events (ude)
 *   . Append an item ude
 *   . Delete all item ude(s)
 *   . Delete an item ude
 *   . Determine whether an item can accept ude(s)
 *
 ******************************************************************************/
#ifndef UF_CAMBND_H_INCLUDED
#define UF_CAMBND_H_INCLUDED


#include <uf.h>
#include <uf_defs.h>
#include <uf_cam.h>
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
 * An object which is used to access a boundary.
 */
typedef void *UF_CAMBND_boundary_t;

/*
 * An object which is used to access a member of a boundary.
 */
typedef void *UF_CAMBND_item_t;


/*
 * The application data for a boundary and the members:
 *
 * The following information shows the types of application data
 * allowed by the objects and the boundary types.
 * An error code is returned by the functions if a wrong type
 * of application data is set.
 *
 *   Facing Operation Boundary:
 *     Blank Boundary:
 *        Boundary:          Stock, Feedrate
 *        Boundary members:  Stock, Feedrate, Tool Position
 *     Check Boundary:
 *        Boundary:          Stock, Feedrate
 *        Boundary members:  Stock, Feedrate, Tool Position
 *
 *   Planar Mill Operation Boundary: (also Cavity Mill)
 *     Part Boundary:
 *        Boundary:          Stock, Tolerances, Blank Distance, Feedrate
 *        Boundary members:  Stock, Tolerances, Feedrate, Tool Position
 *     Blank Boundary:
 *        Boundary:          Stock, Tolerances, Feedrate
 *        Boundary members:  Stock, Tolerances, Feedrate, Tool Position
 *     Check Boundary:
 *        Boundary:          Stock, Tolerances
 *     Trim Boundary:
 *        Boundary:          Stock, Tolerances
 *
 */
struct UF_CAMBND_app_data_s
{
    int                         has_stock;           /* Stock flag.
                                                        Set to 1 if used, or else set to 0. */
    double                      stock;               /* Stock value. */

    int                         has_tolerances;      /* Tolerance flag.
                                                        Set to 1 if used, or else set to 0. */
    double                      tolerances[2];       /* Tolerance values
                                                        [0] = intol
                                                        [1] = outtol */

    int                         has_feedrate;        /* Feed rate flag.
                                                        Set to 1 if used, or else set to 0. */
    UF_CAM_feedrate_unit_t      feedrate_unit;       /* Feed rate unit. */
    double                      feedrate_value;      /* Feed rate value. */

    int                         has_blank_distance;  /* Blank distance flag.
                                                        Set to 1 if used, or else set to 0. */
    double                      blank_distance;      /* Blank distance value. */

    int                         has_tool_position;   /* Tool position flag.
                                                        Set to 1 if used, or else set to 0. */
    UF_CAM_tool_position_t      tool_position;       /* Tool position value. */

};

typedef struct UF_CAMBND_app_data_s UF_CAMBND_app_data_t,
                                   *UF_CAMBND_app_data_p_t;

/*
 * The group data for a boundary and the members:
 *
 * The following information shows the group data
 * allowed by the objects and the boundary types.
 * An error code is returned by the functions if a wrong type
 * of group data is set.
 *
 *   Mill Boundary Group:
 *     Part Boundary:
 *        Boundary:          Offset
 *        Boundary members:  Offset
 *     Blank Boundary:
 *        Boundary:          Offset
 *        Boundary members:  Offset
 *     Check Boundary:
 *        Boundary:          Offset
 *        Boundary members:  Offset
 *     Trim Boundary:
 *        Boundary:          Offset
 *        Boundary members:  Offset
 *
 *   Turn Boundary Group:
 *     Part Boundary:
 *        Boundary:          Offset
 *        Boundary members:  Offset
 *     Blank Boundary:
 *        Boundary members:  Offset
 */
struct UF_CAMBND_group_data_s
{
    int                         has_offset;           /* Offset flag.
                                                        Set to 1 if used, or else set to 0. */
    int  offsetType;                                  /* Offset type.
                                                         0 Distance  1 % of tool diameter. */
    double                      offset;               /* Offset value. */
    double nominalOffset;                             /* Percentage of tool diameter for
                                                         offsetType == 1 */
};

typedef struct UF_CAMBND_group_data_s UF_CAMBND_group_data_t,
                                      *UF_CAMBND_group_data_p_t;

/*
 * The data for the boundary:
 *
 * boundary_type   - It indicates whether the boundary is open or closed.
 *                   It is not used when the boundaries are created from
 *                   a face. Boundaries created from a face are always closed.
 * plane_type      - It indicates whether the plane of the boundary is
 *                   defined by the user or defined automatically.
 *                   It is not used when the boundaries are created from
 *                   a face. Boundaries created from a face are always automatic.
 * origin          - It is the origin of the plane.
 *                   It is used only if the plane type is user defined.
 * matrix          - It is the rotation matrix of the plane.
 *                   It is used only if the plane type is user defined.
 * material_side   - It indicates the material side of the boundary.
 * ignore_holes    - It indicates whether the boundaries are to be created
 *                   from the holes in the face, or if the holes are to be ignored.
 * ignore_islands  - It indicates whether the boundaries are to be created
 *                   from the islands in the face, or if the islands are to be ignored.
 * ignore_chamfers - It indicates whether or not to ignore the chamfers and blends
 *                   of the face. Boundaries will be extended to the chamfers and blends
 *                   of the face if this value is set to one.
 * app_data        - It is the application data applied to the boundary.
 *                   Set it to NULL if the boundary has no application data.
 */
struct UF_CAMBND_boundary_data_s
{
    UF_CAM_boundary_type_t      boundary_type;       /* Boundary type. */

    int                         plane_type;          /* Boundary plane type.
                                                        0 = user defined
                                                        1 = automatic */

    double                      origin[3];           /* Origin of the plane.
                                                        It is used only if plane type is 0. */

    double                      matrix[9];           /* The rotation matrix of the plane.
                                                        It is used only if plane type is 0. */

    UF_CAM_material_side_t      material_side;       /* Material side. */

    /* Ignore data are applied only when creating boundaries from a face. */

    int                         ignore_holes;        /* Ignore holes in the face.
                                                        0 = do not ignore holes
                                                        1 = ignore holes */
    int                         ignore_islands;      /* Ignore islands in the face.
                                                        0 = do not ignore islands
                                                        1 = ignore islands */
    int                         ignore_chamfers;     /* Ignore chamfers of the face.
                                                        0 = do not ignore chamfers
                                                        1 = ignore chamfers */

    /* Application data of the boundary. */

    UF_CAMBND_app_data_t        *app_data;           /* Application data applied to
                                                        the boundary.
                                                        NULL = no application data. */
};

typedef struct UF_CAMBND_boundary_data_s UF_CAMBND_boundary_data_t,
                                        *UF_CAMBND_boundary_data_p_t;


enum UF_CAMBND_UDE_set_type_e
{
   UF_CAMBND_UDE_UNDEFINED = 0,
   UF_CAMBND_UDE_START_SET,
   UF_CAMBND_UDE_END_SET
};
typedef enum UF_CAMBND_UDE_set_type_e UF_CAMBND_UDE_set_type_t;

typedef void   *UF_CAMBND_UDE_t;







/*
   **************************************************************************
   ******************     Functions Relating to Boundary    *****************
   **************************************************************************
*/

/***************************************************************************
 *
 * Appends one or more boundaries that are created from the face to the object.
 *
 * NOTES: 
 *    The face must be planar.
 *
 *    The pointer to the UF_CAMBND_app_data_t structure in the boundary_data
 *      structure must either be NULL or a structure allocated and initialized
 *      by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_append_bnd_from_face
(
    tag_t                       object_tag,         /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t          type,               /* <I> the type of the boundary */
    tag_t                       face,               /* <I> the face tag from which the
                                                           boundary will be created */
    UF_CAMBND_boundary_data_p_t boundary_data       /* <I> the boundary data */
);

/***************************************************************************
 *
 * Appends a single boundary created from edges or curves to the object.
 *
 *  NOTE:
 *    The pointer to the UF_CAMBND_app_data_t structure in the boundary_data
 *      structure must either be NULL or a structure allocated and initialized
 *      by the user.

 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_append_bnd_from_curve
(
    tag_t                          object_tag,      /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t             type,            /* <I> the type of the boundary */
    int                            count,           /* <I> the count of edges/curves */
    tag_t                          *curves,         /* <I,len:count> count
                                                           the edge/curve tags from which
                                                           a boundary will be created */
    UF_CAMBND_boundary_data_p_t    boundary_data,   /* <I> the boundary data */
    UF_CAMBND_app_data_p_t         *app_data        /* <I,len:count> count the application data for each member */
);

/***************************************************************************
 *
 * Deletes all the boundaries of geometry type from the object.
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ***************************************************************************/
extern UFUN_CAMEXPORT int UF_CAMBND_delete_boundaries
(
    tag_t               object_tag,                 /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t  type                        /* <I> the type of the boundary */
);


/***************************************************************************
 *
 * Gets the list of boundaries of geometry type from the object.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_boundaries
(
    tag_t                      object_tag,          /* <I>  the parent object of the
                                                            boundary */
    UF_CAM_geom_type_t         type,                /* <I>  the type of the boundary */
    int                        *count,              /* <O>  the count of boundaries */
    UF_CAMBND_boundary_t       **boundaries         /* <OF,len:count> the list boundary items
                                                            it must be freed using UF_free */
);

/***************************************************************************
 *
 * Deletes a boundary of the boundary type from the object.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_delete_boundary
(
    tag_t                       object_tag,         /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t          type,               /* <I> the type of the boundary */
    UF_CAMBND_boundary_t        boundary            /* <I> the item to be deleted */
);

/***************************************************************************
 *
 * Gets the boundary data without the application data of the boundary.
 *
 * The memory for boundary_data must be allocated by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_boundary_data
(
    UF_CAMBND_boundary_t      boundary,             /* <I> the boundary item */
    UF_CAMBND_boundary_data_t *boundary_data        /* <O> the boundary data */
);

/***************************************************************************
 *
 * Gets the application data of the boundary.
 *
 * The memory for app_data must be allocated by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_boundary_app_data
(
    UF_CAMBND_boundary_t      boundary,             /* <I> the boundary item */
    UF_CAMBND_app_data_t      *app_data             /* <O> the application data */
);

/***************************************************************************
 *
 * Sets the boundary application data.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_set_boundary_app_data
(
    tag_t                      object_tag,          /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t         type,                /* <I> the type of the boundary */
    UF_CAMBND_boundary_t       boundary,            /* <I> the boundary item */
    UF_CAMBND_app_data_p_t     app_data             /* <I> the application data */
);

/***************************************************************************
 *
 * Gets the members of the boundary.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_boundary_items
(
    UF_CAMBND_boundary_t      boundary,             /* <I>  the boundary */
    int                       *count,               /* <O>  the count of boundary members */
    UF_CAMBND_item_t          **items               /* <OF,len:count> the list of boundary members
                                                            it must be freed using UF_free */
);

/***************************************************************************
 *
 * Gets the application data of the member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_item_entity
(
    UF_CAMBND_item_t          item,                 /* <I> the boundary member */
    tag_t                     *entity               /* <O> the geometry tag of
                                                           the boundary member */
);

/***************************************************************************
 *
 * Gets the application data of the member.
 *
 * The memory for app_data must be allocated by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_item_app_data
(
    UF_CAMBND_item_t             item,              /* <I> the boundary member */
    UF_CAMBND_app_data_t         *app_data          /* <O> the application data of
                                                           the boundary member */
);

/***************************************************************************
 *
 * Sets the application data of the member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V18.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_set_item_app_data
(
    tag_t                      object_tag,          /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t         type,                /* <I> the type of the boundary */
    UF_CAMBND_boundary_t       boundary,            /* <I> the boundary item */
    UF_CAMBND_item_t           item,                /* <I> the boundary member */
    UF_CAMBND_app_data_p_t     app_data             /* <I> the application data of
                                                           the boundary member */
);

/***************************************************************************
 *
 * Gets the group data of the boundary.
 *
 * The memory for group_data must be allocated by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_boundary_group_data
(
    UF_CAMBND_boundary_t      boundary,             /* <I> the boundary item */
    UF_CAMBND_group_data_t   *group_data            /* <O> the boundary group data */
);

/***************************************************************************
 *
 * Sets the boundary group data.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_set_boundary_group_data
(
    tag_t                      object_tag,          /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t         type,                /* <I> the type of the boundary */
    UF_CAMBND_boundary_t       boundary,            /* <I> the boundary item */
    UF_CAMBND_group_data_p_t   group_data           /* <I> the boundary group data */
);

/***************************************************************************
 *
 * Gets the group data of the boundary member.
 *
 * The memory for group_data must be allocated by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_item_group_data
(
    UF_CAMBND_item_t             item,              /* <I> the boundary member */
    UF_CAMBND_group_data_t      *group_data         /* <O> the group data of
                                                           the boundary member */
);

/***************************************************************************
 *
 * Sets the group data of the boundary member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_set_item_group_data
(
    tag_t                      object_tag,          /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t         type,                /* <I> the type of the boundary */
    UF_CAMBND_boundary_t       boundary,            /* <I> the boundary item */
    UF_CAMBND_item_t           item,                /* <I> the boundary member */
    UF_CAMBND_group_data_p_t   group_data           /* <I> the group data of
                                                           the boundary member */
);

/***************************************************************************
 *
 * Sets the group data of the boundary member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_is_inherited
(
    tag_t                       object_tag,  /* <I> the parent object of the
                                                           boundary */
    UF_CAM_geom_type_t          type,        /* <I> the type of the boundary */
    logical                     *response    /* <O> the response, inherited = TRUE,
                                                    not inherited = FALSE */
);

/************************************************************************
 *
 * Prototype for User Defined Events (Post Commands)
 *
 ************************************************************************/

/***************************************************************************
 *
 * Asks the boundary member user defined events.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_ask_item_udes
(
   UF_CAMBND_item_t            item,        /* <I> the boundary member */
   UF_CAMBND_UDE_set_type_t    set_type,    /* <I> the type of the user
                                                   defined events.
                                                   Either Start or End. */
   int                         *num_udes,   /* <O> the count of the
                                                   user defined events */
   UF_CAMBND_UDE_t             **udes       /* <OF,len:num_udes> the list of the user
                                                   defined events */
);

/***************************************************************************
 *
 * Asks the boundary member user defined events for WEDM geometry.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX6.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_WEDM_ask_item_udes
(
   UF_CAMBND_item_t            item,        /* <I> the boundary member */
   UF_CAMBND_UDE_set_type_t    set_type,    /* <I> the type of the user
                                                   defined events.
                                                   Either Start or End. */
   int                         pass_num,     /* <I> pass number for which the
                                                  events are to be known */
   int                         *num_udes,   /* <O> the count of the
                                                   user defined events */
   UF_CAMBND_UDE_t             **udes       /* <O,len:num_udes> the list of the user
                                                   defined events */
);

/***************************************************************************
 *
 * Deletes all boundary member user defined events.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_delete_all_item_udes
(
   UF_CAMBND_item_t            item,        /* <I> the boundary member */
   UF_CAMBND_UDE_set_type_t    set_type     /* <I> the type of the user
                                                   defined events.
                                                   Either Start or End. */
);

/***************************************************************************
 *
 * Deletes all WEDM boundary member user defined events.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX6.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_WEDM_delete_all_item_udes
(
   UF_CAMBND_item_t            item,        /* <I> the WEDM boundary member */
   UF_CAMBND_UDE_set_type_t    set_type     /* <I> the type of the user
                                                   defined events.
                                                   Either Start or End. */
);

/***************************************************************************
 *
 * Appends a boundary member user defined event.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_append_item_ude
(
   UF_CAMBND_item_t            item,        /* <I> the boundary member */
   UF_CAMBND_UDE_set_type_t    set_type,    /* <I> the type of the user
                                                   defined events. */
   char                       *ude_name,    /* <I> the name of the user defined
                                                   event */
   UF_CAMBND_UDE_t            *ude,         /* <O> the object of the user deined
                                                   events */
   logical                    *response     /* <O> the response. success = TRUE,
                                                   fail = FALSE. */
);

/***************************************************************************
 *
 * Appends a WEDM boundary member user defined event.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX6.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_WEDM_append_item_ude
(
   UF_CAMBND_item_t            item,        /* <I> the boundary member */
   int                         pass_num,     /* <I> Pass number */
   UF_CAMBND_UDE_set_type_t    set_type,    /* <I> the type of the user
                                                   defined events. */
   char                       *ude_name,    /* <I> the name of the user defined
                                                   event */
   UF_CAMBND_UDE_t            *ude,         /* <O> the object of the user deined
                                                   events */
   logical                    *response     /* <O> the response. success = TRUE,
                                                   fail = FALSE. */
);

/***************************************************************************
 *
 * Deletes a boundary member user defined event.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_delete_item_ude
(
   UF_CAMBND_item_t            item,        /* <I> the boundary member */
   UF_CAMBND_UDE_set_type_t    set_type,    /* <I> the type of the user
                                                   defined events. */
   UF_CAMBND_UDE_t             ude          /* <I> the object of the user deined
                                                   events */
);

/***************************************************************************
 *
 * Deletes a Wedm boundary member user defined event.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX6.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_WEDM_delete_item_ude
(
   UF_CAMBND_item_t            item,        /* <I> the boundary member */
   int                         pass_num,     /* <I> pass number for which events are
                                                     specified */
   UF_CAMBND_UDE_set_type_t    set_type,    /* <I> the type of the user
                                                   defined events. */
   UF_CAMBND_UDE_t             ude          /* <I> the object of the user deined
                                                   events */
);

/***************************************************************************
 *
 * Determine whether the boundary member can be set the user defined events.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_can_accept_item_ude
(
   UF_CAMBND_item_t            item,       /* <I> the boundary member */
   UF_CAMBND_UDE_set_type_t    set_type,   /* <I> the type of the user
                                                   defined events. */
   char                       *ude_name,   /* <I> the name of the user defined
                                                   event */
   logical                    *response    /* <O> the response.
                                                  Can be set = TRUE,
                                                  can not be set = FALSE */
);

/***************************************************************************
 *
 * Sets the boundary plane.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX4.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMBND_set_boundary_plane
(
    UF_CAMBND_boundary_t boundary,        /* <I> the boundary item */
    double bnd_origin[3],                 /* <I> the plane origin (WCS) */
    double bnd_matrix[9]                  /* <I> the plane matrix */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CAMBND_H_INCLUDED */

