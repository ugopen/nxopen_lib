/*******************************************************************************
                Copyright (c) 2001,2002 Unigraphics Solutions, Inc.
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
 * The OPR boundary routines in this file enable you to:
 *   . Get inherited boundary application data
 *   . Set inherited boundary application data
 *   . Get inherited item application data
 *   . Set inherited item application data
 *   . Ask inherited item user defined events (udes)
 *   . Delete all inherited item udes
 *   . Append an inherited item ude
 *   . Delete an inherited item ude
 *   . Determine whether an inherited item can accpet an ude
 *
 ******************************************************************************/
#ifndef UF_OPRBND_H_INCLUDED
#define UF_OPRBND_H_INCLUDED


#include <uf.h>
#include <uf_defs.h>
#include <uf_cam.h>
#include <libufun_cam_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/*
 * An object which is used to access a boundary.
 */
typedef void *UF_OPRBND_boundary_t;

/*
 * An object which is used to access a member of a boundary.
 */
typedef void *UF_OPRBND_item_t;


/*
 * The application data for a inherited boundary and the members:
 *
 * The following information shows the types of application data
 * allowed by the objects and the boundary types.
 * An error code is returned by the functions if a wrong type
 * of application data is set.
 *
 *   Facing Operation Boundary:
 *     Blank Boundary:
 *        Boundary:          Stock, Feedrate
 *        Boundary members:  Stock, Feedrate, Tool Position, User Defined Events (Post Commands)
 *     Check Boundary:
 *        Boundary:          Stock
 *        Boundary members:  Stock
 *
 *   Planar Mill Operation Boundary:
 *     Part Boundary:
 *        Boundary:          Stock, Feedrate
 *        Boundary members:  Stock, Feedrate, Tool Position, User Defined Events (Post Commands)
 *     Blank Boundary:
 *        Boundary:          Stock, Feedrate
 *        Boundary members:  Stock, Feedrate, Tool Position, User Defined Events (Post Commands)
 *     Check Boundary:
 *        Boundary:          Stock
 *        Boundary members:  Stock
 *     Trim Boundary:
 *        Boundary:          Stock
 *
 *   ZLevel Mill Operation Boundary:
 *     Trim Boundary:
 *        Boundary:          Stock
 *
 *   Area Mill Operation Boundary:
 *     Trim Boundary:
 *        Boundary:          Stock
 *
 */
struct UF_OPRBND_app_data_s
{
    int                         has_stock;           /* Stock flag.
                                                        Set to 1 if used, or else set to 0. */
    double                      stock;               /* Stock value. */

    int                         has_feedrate;        /* Feed rate flag.
                                                        Set to 1 if used, or else set to 0. */
    UF_CAM_feedrate_unit_t      feedrate_unit;       /* Feed rate unit. */
    double                      feedrate_value;      /* Feed rate value. */

    int                         has_tool_position;   /* Tool position flag.
                                                        Set to 1 if used, or else set to 0. */
    UF_CAM_tool_position_t      tool_position;       /* Tool position value. */


};

typedef struct UF_OPRBND_app_data_s UF_OPRBND_app_data_t, *UF_OPRBND_app_data_p_t;

enum UF_OPRBND_UDE_set_type_e
{
   UF_OPRBND_UDE_UNDEFINED = 0,
   UF_OPRBND_UDE_START_SET,
   UF_OPRBND_UDE_END_SET
};
typedef enum UF_OPRBND_UDE_set_type_e UF_OPRBND_UDE_set_type_t;

typedef void   *UF_OPRBND_UDE_t;

/***************************************************************************
 *
 * Gets the inherited application data of the boundary.
 *
 * The memory for app_data must be allocated by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ***********************************************************************/
extern UFUN_CAMEXPORT int UF_OPRBND_ask_boundary_app_data
(
    tag_t                     object_tag,       /* <I> the parent object of the boundary */
    UF_CAM_geom_type_t        type,             /* <I> the type of the boundary */
    UF_OPRBND_boundary_t      boundary,         /* <I> the boundary */
    UF_OPRBND_app_data_t      *app_data         /* <O> the application data */
);

/***************************************************************************
 *
 * Sets the inherited boundary application data.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_OPRBND_set_boundary_app_data
(
    tag_t                      object_tag,          /* <I> the parent object of the boundary */
    UF_CAM_geom_type_t         type,                /* <I> the type of the boundary */
    UF_OPRBND_boundary_t       boundary,            /* <I> the boundary */
    UF_OPRBND_app_data_p_t     app_data             /* <I> the application data */
);

/***************************************************************************
 *
 * Gets the application data of the inherited member.
 *
 * The memory for app_data must be allocated by the user.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_OPRBND_ask_item_app_data
(
    tag_t                        object_tag,        /* <I> the parent object of the boundary */
    UF_CAM_geom_type_t           type,              /* <I> the type of the boundary */
    UF_OPRBND_boundary_t         boundary,          /* <I> the boundary */
    UF_OPRBND_item_t             item,              /* <I> the boundary member */
    UF_OPRBND_app_data_t         *app_data          /* <O> the application data of
                                                           the boundary member */
);

/***************************************************************************
 *
 * Sets the application data of the inherited member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_OPRBND_set_item_app_data
(
    tag_t                      object_tag,          /* <I> the parent object of the boundary */
    UF_CAM_geom_type_t         type,                /* <I> the type of the boundary */
    UF_OPRBND_boundary_t       boundary,            /* <I> the boundary */
    UF_OPRBND_item_t           item,                /* <I> the boundary member */
    UF_OPRBND_app_data_p_t     app_data             /* <I> the application data of
                                                           the boundary member */
);

/***************************************************************************
 *
 * Gets the user defined events of the inherited member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_OPRBND_ask_item_udes
(
   tag_t                       object_tag,          /* <I> the parent object of the boundary */
   UF_CAM_geom_type_t          type,                /* <I> the type of the boundary */
   UF_OPRBND_boundary_t        boundary,            /* <I> the boundary */
   UF_OPRBND_item_t            item,                /* <I> the boundary member */
   UF_OPRBND_UDE_set_type_t    set_type,            /* <I> the user defined event (ude) types,
                                                           either Start or End */
   int                         *num_udes,           /* <O> the number of user defined events */
   UF_OPRBND_UDE_t             **udes               /* <O> the ude object */
);

/***************************************************************************
 *
 * Deletes all of the user defined events of the inherited member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUN_CAMEXPORT int UF_OPRBND_delete_all_item_udes
(
   tag_t                       object_tag,          /* <I> the parent object of the boundary */
   UF_CAM_geom_type_t          type,                /* <I> the type of the boundary */
   UF_OPRBND_boundary_t        boundary,            /* <I> the boundary */
   UF_OPRBND_item_t            item,                /* <I> the boundary member */
   UF_OPRBND_UDE_set_type_t    set_type             /* <I> the user defined event (ude) types,
                                                           either Start or End */
);

/***************************************************************************
 *
 * Append the user defined events of the inherited member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ***********************************************************************/
extern UFUN_CAMEXPORT int UF_OPRBND_append_item_ude
(
   tag_t                       object_tag,          /* <I> the parent object of the boundary */
   UF_CAM_geom_type_t          type,                /* <I> the type of the boundary */
   UF_OPRBND_boundary_t        boundary,            /* <I> the boundary */
   UF_OPRBND_item_t            item,                /* <I> the boundary member */
   UF_OPRBND_UDE_set_type_t    set_type,            /* <I> the user defined event (ude) types,
                                                           either Start or End */
   char                       *ude_name,            /* <I> the ude name */
   UF_OPRBND_UDE_t            *ude,                 /* <O> the ude object */
   logical                    *response             /* <O> the response.
                                                           Success = TRUE, fail = FALSE */
);

/***************************************************************************
 *
 * Delete the user defined event of the inherited member.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ***********************************************************************/
extern UFUN_CAMEXPORT int UF_OPRBND_delete_item_ude
(
   tag_t                       object_tag,          /* <I> the parent object of the boundary */
   UF_CAM_geom_type_t          type,                /* <I> the type of the boundary */
   UF_OPRBND_boundary_t        boundary,            /* <I> the boundary */
   UF_OPRBND_item_t            item,                /* <I> the boundary member */
   UF_OPRBND_UDE_set_type_t    set_type,            /* <I> the user defined event (ude) types,
                                                           either Start or End */
   UF_OPRBND_UDE_t             ude                  /* <I> the ude object */
);

/***************************************************************************
 *
 * Check if the user defined event can be accepted.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ***********************************************************************/
extern UFUN_CAMEXPORT int UF_OPRBND_can_accept_item_ude
(
   tag_t                       object_tag,          /* <I> the parent object of the boundary */
   UF_CAM_geom_type_t          type,                /* <I> the type of the boundary */
   UF_OPRBND_boundary_t        boundary,            /* <I> the boundary */
   UF_OPRBND_item_t            item,                /* <I> the boundary member */
   UF_OPRBND_UDE_set_type_t    set_type,            /* <I> the user defined event (ude) types,
                                                           either Start or End */
   char                       *ude_name,            /* <I> the ude name */
   logical                    *response             /* <O> the response.
                                                           Can be accpeted = TRUE,
                                                           can not be accpeted = FALSE */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_OPRBND_H_INCLUDED */
