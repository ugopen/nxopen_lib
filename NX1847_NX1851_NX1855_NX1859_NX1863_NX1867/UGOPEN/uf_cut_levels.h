/*******************************************************************************
                Copyright (c) 2004 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
******************************************************************************
 *****************************************************************************
 *
 *    
 * 
 *
 * File description:
 *
 * This file contains the Open C API interface to cut levels in CAM.
 *
 * Cut levels can be used in both Cavity Mill and ZLevel machining to define
 * the levels at which the cuts take place.
 *
 * The CAM cut levels routines in this file enable you to:
 *   . Make a local copy of the cut levels for the user to look at.
 *   . Change the range type
 *   . Add levels defined by either a geometry tag or a z level.
 *   . Delete levels
 *   . Reset levels to their default settings.
 *
 * There are 4 parameters that are relevant to this functionality
 * (defined in the file uf_param_indices.h):
 *
 * UF_PARAM_CUTLEV_RANGE_TYPE
 *   Possible values are:
 *     UF_PARAM_clv_range_auto_generate -  cut levels defined by the system
 *                                         at horizontal regions of the part.
 *                                         Any changes will cause the type to
 *                                         be changed to 'user_defined'.
 *     UF_PARAM_clv_range_user_defined  -  cut levels are defined by user
 *     UF_PARAM_clv_range_single        -  Single cut range. Levels can not
 *                                         be added or removed with this type.
 *                                         This is the only type for which
 *                                         top off functionality can be
 *                                         requested.
 *   This is a read only parameter value and can only be changed with the
 *   UF_CUT_LEVELS_set_range_type function.
 *
 * UF_PARAM_CUTLEV_RANGE_SUBDIV_TYPE
 *   Possible values are:
 *     UF_PARAM_clv_top_off_mode_off -  Don't top off horizontal surfaces.
 *     UF_PARAM_clv_top_off_mode_on  -  Do top off horizontal surfaces.
 *   This type is only considered when the range type above is set to 'single'.
 *
 * UF_PARAM_CUTLEV_TOP_OFF_MODE
 *   Possible values are:
 *     UF_PARAM_clv_range_subdiv_equalise -  subdivide each cut range into
 *                                           equal steps such that the depth
 *                                           per cut of that range is not
 *                                           exceeded.
 *     UF_PARAM_clv_range_subdiv_bottoms_only
 *                                        -  cut at range bottoms only.
 *                                           The ranges are not subdivided.
 *   Note: the cut levels returned by the functionality supplied in this file
 *   are the range ends. The subdivided levels are only used when the toolpath
 *   is being generated.
 *
 * UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH
 *   The global cut depth used for subdividing the ranges. This is the value
 *   used for both 'auto generate' and 'single' range type and is the default
 *   value for 'user defined' range type. Note that only 'user defined' range
 *   type can have different cut depths for different ranges.
 *
 ******************************************************************************/
#ifndef UF_CUT_LEVELS_H_INCLUDED
#define UF_CUT_LEVELS_H_INCLUDED


#include <uf.h>
#include <uf_defs.h>
#include <uf_param_indices.h>
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

/* Data structure for a single cut level. */
struct UF_CUT_LEVEL_single_s
{
    tag_t entity_tag;       /* Tag id of the face or point entity
                               used to define the current cut level.
                               This can be NULL if the level was
                               defined by an explicit z level. */
    
    double z_level;         /* The z distance of the cut level from the
                               origin along the normal of the cut levels. */
    
    double local_cut_depth; /* The max depth per cut value to be
                               used for the range between this cut
                               level and the one above it. */
};
typedef struct UF_CUT_LEVEL_single_s UF_CUT_LEVEL_single_t;

/* Data structure for all cut levels. */
struct UF_CUT_LEVELS_s
{
    int num_levels;                        /* The number of cut levels. */

    UF_CUT_LEVEL_single_t *cut_levels;     /* <len:num_levels>An array of the individual
                                              cut levels. */

    int num_top_off_levels;                /* The number of top off levels. */
    
    UF_CUT_LEVEL_single_t *top_off_levels; /* <len:num_top_off_levels>An array of the individual top
                                              off levels. */
};
typedef struct UF_CUT_LEVELS_s UF_CUT_LEVELS_t;

/*
   **************************************************************************
   ******************     Functions Relating to Geometry    *****************
   **************************************************************************
*/

/*************************************************************************
Loads the current cut levels for the specified operation into the data
structure UF_CUT_LEVELS_t.

Note that this creates a copy of the current cut levels, and will not
be associative to the part.

Note that top off levels are stored separately from the other cut levels
and that top off levels can not be changed. They are only available if the 
UF_PARAM_CUTLEV_RANGE_TYPE_INDEX parameter is set to UF_PARAM_clv_range_single.
Top off levels are set at levels where there are horizontal (relative to
the tool axis) regions of the part which face upwards. There is no top off
level when it coincides with a cut level.

Will return UF_CAM_ERROR_CUT_LEVELS_NOT_SUPPORTED if cut levels are not
supported for the specified operation.

Environment: Internal or External

See Also:  UF_CUT_LEVELS_free 

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_load
(
    tag_t operation_tag,         /*<I>  The tag of the operation for which the
                                        cut levels are defined. */

    UF_CUT_LEVELS_t **cut_levels_ptr_addr
                                 /*<OF,free:UF_CUT_LEVELS_free> A new data structure containing all of
                                        the cut levels for the specified
                                        operation.  The pointer to the structure
                                        must be NULL on input, or it must be a
                                        valid pointer created using a previous
                                        call to UF_CUT_LEVELS_load. The pointer
                                        must be freed by UF_CUT_LEVELS_free. */
);

/*************************************************************************
Frees the memory associated with a cut levels structure when the user
has finished with it.

Environment: Internal or External

See Also:   UF_CUT_LEVELS_load 

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_free
(
    UF_CUT_LEVELS_t **cut_levels_ptr_addr
                                /* <OF> The data structure create by the call
                                        to UF_CUT_LEVELS_load.  The memory
                                        associated with this structure is freed,
                                        and a NULL pointer is returned. */
);

/*************************************************************************
Set the range type to that specified. This sets the parameter
UF_PARAM_CUTLEV_RANGE_TYPE_INDEX, which is otherwise read only, and
updates the cut levels data structure.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_set_range_type
(
    tag_t operation_tag,        /*<I>  The tag of the operation for which the
                                       cut levels are defined. */

    UF_PARAM_clv_range_type_t range_type, /* <I> The range type to be set. */

    UF_CUT_LEVELS_t *cut_levels  /*<OF> If the data structure created by
                                        a call to UF_CUT_LEVELS_load is
                                        passed in, then it will be updated
                                        to reflect the changes from the new
                                        range type. If NULL is passed in,
                                        then the argument is ignored. */

);

/*************************************************************************
Adds cut levels defined by face and/or point tags to the list of cut levels.

Will return UF_CAM_ERROR_CUT_LEVEL_CHANGE_NOT_MADE if a change could not be
made.

Will return UF_CAM_ERROR_INVALID_CUT_LEVEL_ENTITY if a geometry tag did not
specify a valid face or point.

The range type, as specified by UF_PARAM_CUTLEV_RANGE_TYPE, should not be
UF_PARAM_clv_range_single as levels can not be added to this range type. The
error UF_CAM_ERROR_SINGLE_RANGE_NOT_CHANGED will be returned if this happens.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_add_levels_using_geom
(
    tag_t operation_tag,         /*<I>  The tag of the operation for which the
                                        cut levels are defined. */
    
    int num_to_add,              /*<I>  The number of face and/or point tags
                                        being added. Value must be non
                                        negative.*/

    tag_t *geom_tags,            /*<I>  An array of face and/or point tags
                                        defining the new cut level. If faces
                                        are not horizontal (with respect to
                                        the tool axis), or even flat, then
                                        the heighest z level of the face will
                                        be used for the cut level.*/
    
    double max_depth_per_cut,    /*<I>  The max depth per cut to be used for
                                        subdividing the range above the new
                                        cut levels. A value of zero indicates
                                        that there is no limit. Value must
                                        be non negative.*/
    
    UF_CUT_LEVELS_t *cut_levels  /*<OF> If the data structure created by
                                        a call to UF_CUT_LEVELS_load is
                                        passed in, then it will be updated
                                        to reflect the changes from the
                                        addition. If NULL is passed in,
                                        then the argument is ignored. */
);

/*************************************************************************
Adds cut levels defined by explicit z-levels

Will return UF_CAM_ERROR_CUT_LEVEL_CHANGE_NOT_MADE if a change could not be
made.

The range type, as specified by UF_PARAM_CUTLEV_RANGE_TYPE, should not be
UF_PARAM_clv_range_single as levels can not be added to this range type. The
error UF_CAM_ERROR_SINGLE_RANGE_NOT_CHANGED will be returned if this happens.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_add_levels_using_z
(
    tag_t operation_tag,         /*<I>  The tag of the operation for which the
                                        cut levels are defined. */

    int num_to_add,              /*<I>  The number of z-levels being added.
                                        Value must be non negative. */

    double *z_levels,            /*<I,len:num_to_add>  Array of z distances, along the tool axis,
                                        of the cut level from the origin. */

    double max_depth_per_cut,    /*<I>  The max depth per cut to be used for
                                        subdividing the range above the new
                                        cut levels. A value of zero indicates
                                        that there is no limit. Value must
                                        be non negative.*/

    UF_CUT_LEVELS_t *cut_levels  /*<OF> If the data structure created by
                                        a call to UF_CUT_LEVELS_load is
                                        passed in, then it will be updated
                                        to reflect the changes from the
                                        addition. If NULL is passed in,
                                        then the argument is ignored. */
);

/*************************************************************************
Edits an existing cut level using a face or point. Any levels between
the old and new location will be removed.

Will return UF_CAM_ERROR_CUT_LEVEL_CHANGE_NOT_MADE if change could not be
made.

Will return UF_CAM_ERROR_INVALID_CUT_LEVEL_ENTITY if a geometry tag did not
specify a valid face or point.

The range type, as specified by UF_PARAM_CUTLEV_RANGE_TYPE, should not be
UF_PARAM_clv_range_single as levels can not be added to this range type.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_edit_level_using_geom
(
    tag_t operation_tag,         /*<I>  The tag of the operation for which the
                                        cut levels are defined. */

    int edit_level,              /*<I>  The index of the level to be edited
                                        (0 being the top level). */
    
    tag_t geom_tag,              /*<I>  The tag of the face or point defining
                                        the new cut level. */
    
    double max_depth_per_cut,    /*<I>  The max depth per cut to be used for
                                        subdividing the range above the new
                                        cut level. */

    UF_CUT_LEVELS_t *cut_levels  /*<OF> If the data structure created by
                                        a call to UF_CUT_LEVELS_load is
                                        passed in, then it will be updated
                                        to reflect the changes from the
                                        addition. If NULL is passed in,
                                        then the argument is ignored. */
);

/*************************************************************************
Edits an existing cut level defined using an explicit z-level. Any
levels between the old and new location will be removed.

Will return UF_CAM_ERROR_CUT_LEVEL_CHANGE_NOT_MADE if change could not be
made.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_edit_level_using_z
(
    tag_t operation_tag,         /*<I>  The tag of the operation for which the
                                        cut levels are defined. */
    
    int edit_level,              /*<I>  The index of the level to be edited
                                        (0 being the top level). */
    
   double z_level,               /*<I>  The z distance, along the tool axis,
                                        of the cut level from the origin. */

    double max_depth_per_cut,    /*<I>  The max depth per cut to be used for
                                        subdividing the range above the new cut
                                        level. */

    UF_CUT_LEVELS_t *cut_levels  /*<OF> If the data structure created by
                                        a call to UF_CUT_LEVELS_load is
                                        passed in, then it will be updated
                                        to reflect the changes from the
                                        addition. If NULL is passed in,
                                        then the argument is ignored. */
);

/*************************************************************************
Deletes the specified cut level.

Will return UF_CAM_ERROR_CUT_LEVEL_CHANGE_NOT_MADE if change could not be
made.

The range type, as specified by UF_PARAM_CUTLEV_RANGE_TYPE, should not be
UF_PARAM_clv_range_single as levels can not be deleted with this range type.
The error UF_CAM_ERROR_SINGLE_RANGE_NOT_CHANGED will be returned if this
happens.

Will return UF_CAM_ERROR_CUT_LEVEL_CHANGE_NOT_MADE if deletion could not be
made.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_delete_level
(
    tag_t operation_tag,         /*<I>  The tag of the operation for which the
                                        cut levels are defined. */

    int delete_level,            /*<I>  The index of the cut level to be
                                        deleted (0 being the top level). */

    UF_CUT_LEVELS_t *cut_levels  /*<OF> If the data structure created by
                                        a call to UF_CUT_LEVELS_load is
                                        passed in, then it will be updated
                                        to reflect the changes from the
                                        deletion. If NULL is passed in,
                                        then the argument is ignored. */
);

/*************************************************************************
Returns the data for the specified cut level.

Note this returns the data from the UF_CUT_LEVELS_t object which is not
associative to the part. Use UF_CUT_LEVELS_load to ensure you have an up
to date version of the data.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_ask_level
(
   UF_CUT_LEVELS_t *cut_levels,  /*<I> The loaded cut levels data structure. */

   int index,                    /*<I> The index of the cut level the data is
                                       required for (0 being the top level). */

   UF_CUT_LEVEL_single_t **level_data_ptr_addr
                                 /*<O> Address of the pointer to the data of
                                       the requested single level.
                                       The address must not be NULL on input.
                                       The data includes:
                                       - The tag of the face or point entity 
                                         used to define the current cut 
                                         level. This can be NULL if the level 
                                         was defined by an explicit z level.
                                       - The z distance of the cut level down
                                         from the top cut level. All values
                                         will be non-negative.
                                       - The max depth per cut value to be used
                                         for the range between this cut level
                                         and the one above it. */
);

/*************************************************************************
Returns the data for the specified top off level

Note this returns the data from the UF_CUT_LEVELS_t object which is not
associative to the part. Use UF_CUT_LEVELS_load to ensure you have an up
to date version of the data.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_ask_top_off_level
(
   UF_CUT_LEVELS_t *cut_levels,   /*<I> The loaded cut levels data structure. */

   int index,                     /*<I> The index of the top off level the data
                                        is required for (0 being the top
                                        level). */

   UF_CUT_LEVEL_single_t **level_data_ptr_addr
                                 /*<O> Address of the pointer to the data of
                                       the requested single level.
                                       The address must not be NULL on input.
                                       The data includes:
                                       - The tag of the face or point entity 
                                         used to define the current cut 
                                         level. This can be NULL if the level 
                                         was defined by an explicit z level.
                                       - The z distance of the cut level down
                                         from the top cut level. All values
                                         will be non-negative.
                                       - The max depth per cut value to be used
                                         for the range between this cut level
                                         and the one above it. */
);
    
/*************************************************************************
Resets the cut levels to their default.

Environment: Internal or External

See Also:

History: Released in NX3
*************************************************************************/
extern UFUN_CAMEXPORT int UF_CUT_LEVELS_reset_to_default
(
   tag_t operation_tag   /*<I> The tag of the operation for which the cut
                           levels are defined. */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CUT_LEVELS_H_INCLUDED */
