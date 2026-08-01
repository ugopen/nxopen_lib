/*******************************************************************************

            Copyright (c) 1998-2000  Unigraphics Solutions Corporation
                            Unpublished - All rights reserved

*******************************************************************************

*******************************************************************************

File description:

This module combined with the faceting module interface (defined in uf_facet.h)
provides the CAM user with the capability to preprocess geometry just as in the
user interface.

Preprocessing data for CAM use in Fixed Axis Machining operations includes the
creation of a faceted model for the user defined geometry.

For preprocessing geometry for CAM purposes, the following steps are recommended
for the user:

1) Create a facet model for the geometry using the interface provided in
   uf_facet.h

   The user should provide the faceting parameters using the following
   guidelines to ensure that the model is valid for use by CAM.

        a)  max_facet_edges = 3
        b)  number_storage_type = FACET_TYPE_DOUBLE
        c)  specify_surface_tolerance = true
        d)  surface_dist_tolerance <= 0.0381 (mm)
        e)  curve_dist_tolerance  <= 0.0381 (mm)
        f)  surface_angular_tolerance <= 0.4
        g)  specify_curve_tolerance = true
        h)  curve_angular_tolerance <= 0.4
        i)  specify_parameters = true
        j)  specify_view_direction = true
        k)  silh_view_direction[0] = tool_axis i component
        l)  silh_view_direction[1] = tool_axis j component
        m)  silh_view_direction[2] = tool_axis k component
        n)  silh_chord_tolerance <= surface_dist_tolerance/2.0


2) Assigning the facet model for CAM by using the functions in this file.

To avoid duplication of interface, the user is required to use uf_facet.h
interface for creating and manipulating faceted models in NX. The faceted
models are standard NX entities in that they can have names and attributes
attached to them. Their type, etc. can be enquired in the usual way and they
are deleted in the usual way.

NX faceted models are occurrenceable and can be added to reference sets. They
are usable for visualisation and clearance analysis, but cannot be dimensioned
to, so they are of little use in drafting.

Errors returned by this module:

   -  UF_CAM_PREPRO_invalid_model : Input Facet Model not valid for CAM
******************************************************************************/
#ifndef UF_CAM_PREPRO_H_INCLUDED
#define UF_CAM_PREPRO_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_cam_exports.h>

#define ERROR_CAM_PREPRO_base  1930000

#ifdef __cplusplus
extern "C" {
#endif

#include <string.h>


/*
    Error codes
*/
#define UF_CAM_PREPRO_ERROR_BASE            ERROR_CAM_PREPRO_base

#define UF_CAM_PREPRO_invalid_model         UF_CAM_PREPRO_ERROR_BASE+1


/******************************************************************************
This function will mark the facet model as a model that can be used for
CAM purposes.  This will inform the CAM preprocessors that the prepro
information is available and that the user intends to use it to
represent the corresponding geometry.

Environment: Internal  and  External
See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_PREPRO_mark_model_as_cam
    (
    tag_t model                 /* <I> The facet model created or updated
                                       using the interface described in
                                       uf_facet.h                         */
    );

/****************************************************************************
 * Initializes the required environment for this module.
 *
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_PREPRO_init_module
(
   void
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CAM_PREPRO_H_INCLUDED */

