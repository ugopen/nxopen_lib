/*******************************************************************************
         Copyright (c) 1995-2000,2001,2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:

    Open API support for FACET.

    The subroutines in this chapter provide access to manipulating faceted
    models in NX. The creation of faceted (polyhedral) models is
    intended primarily for use in visualization and for use in the packaging
    components of NX (specifically NX Clearance Analysis).

    NOTE: Parts created before NX5 that contain a facet which is part of a 
    lightweight reference set (or facet reference set), will automatically 
    be converted during part retrieval in NX5 and beyond.  The conversion 
    will take facets that originally had a subtype of 0 (UF_faceted_model_normal_subtype) 
    and convert it to a subtype of 3 (UF_faceted_model_jt_body_subtype).  
    Please be aware of this when cycling thru part files using the object 
    type and subtype.


    The routines in this section allow you to:
      . Add a facet to a faceted model.

      . Inquire the facet adjacent to a specified edge of a specified facet.

      . Inquire the convexity of an edge between two facets.

      . Inquire  the default faceting parameters.

      . Inquire the maximum number of vertices of any facet in the model.

      . Determines faceting parameters when given a faceted model which was
        generated from (and remains associated with a solid).

      . Inquire the faceted model(s) of a specified solid body or face.

      . Inquire the number of facets in a model.

      . Inquire the vertex normals of the facet with the specified facet id.

      . Inquire the parameters of the facet vertices for the specified facet id.

      . Inquire the number of vertices in a facet.

      . Inquire the plane equation of a facet.

      . Inquire the solid model on which a faceted model is based.

      . Inquire the convexity of a vertex in a facet.

      . Inquire the vertices of the facet with the specified facet id.

      . Create an empty faceted model which is not associated with any solid.

      . Iterate over the facets in a faceted model.

      . Delete a facet from a model.

      . Disassociate a faceted model from its generating solid.

      . Produce a faceted model from a solid body or face.

      . Determine if a specified edge appears in a specified facet.

      . Inquire if a facet is convex.

      . Inquire if a faceted model is convex.

      . Inquire if a faceted model is up to date.

      . Indicate that edits to the specified faceted model are now complete.

      . Set a facet as being adjacent to another facet along a specified edge.

      . Set the default faceting parameters for creating faceted models from
        solid bodies and faces.

      . Update a faceted model if it was generated from a solid.

      . Change the location of a vertex in a facet.

    A faceted model consists of a collection of facets each of which is
    identified within the model by a facet_id. Each facet has three or more
    vertices which (for an N sided facet) are numbered 0 to (N-1), these numbers
    are termed vertex_ids. Similarly the edges in a facet are numbered 0 to
    (N-1), and the edge I is that between the vertices I and (I+1)modN, these
    numbers are termed edge_ids. The vertices of the facet are ordered
    anticlockwise when viewed down the facet normal.

    Faceted models can be created in one of two ways:
      1. By faceting a solid body or a face of a solid body. In this case the
         faceted model is associated with the solid object from which it was
         generated (unless this link is broken explicitly); if the solid object
         is modified then the faceted model is marked as out of date, if the
         solid object is deleted then the faceted model is also deleted, and the
         faceted model will be displayed only if the solid model is not
         available to be displayed (for example, the solid object is not in the
         reference set containing the faceted model).

         If a faceted model is out of date, then it can be regenerated from its
         associated solid object. Note that this will happen in any case when
         the part containing the faceted model is saved.

      2. By creating an empty faceted model to which facets are then added, and
         adjacencies between facets are specified.  In this case there is no
         association with any solid object.

    Both of the above techniques are illustrated in the example program
    provided.

    The individual facets in a NX faceted model are planar within the the linear
    modeling tolerance used by NX. This applies regardless of which of the two
    above methods is used to create the faceted model.  Similarly, an angular
    tolerance is used when the convexity of a vertex in a facet, or between two
    facets sharing an edge is computed.

    The CAM users can create the facet models that can be used by the Fixed Axis
    Surface Contouring and Cavity Milling processor as preprocessing data.  Some
    of the default faceting parameter values have to change for such use. Once a
    facet model is created using this module, it can then be marked for use by
    the CAM processors using the module uf_cam_prepro.h

    NX faceted models are occurrenceable and can be added to reference sets.
    They are usable for visualisation and clearance analysis, but cannot be
    dimensioned to, so they are of little use in drafting.

    The functions that are described below are divided into the following
    sections:

      a) Setting and enquiring module parameters
      b) Creating and updating faceted models
      c) Enquiring data from faceted models

*******************************************************************************/
#ifndef UF_FACET_H_INCLUDED
#define UF_FACET_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <string.h>
#include <libufun_exports.h>

/***************************************************************************

  ***************************************************************************/
#define ERROR_FACET_base       1165000

#ifdef __cplusplus
extern "C" {
#endif

/*
    Error codes
*/
#define UF_FACET_ERROR_BASE                 ERROR_FACET_base

#define UF_FACET_err_invalid_model          UF_FACET_ERROR_BASE+1
#define UF_FACET_err_invalid_facet_id       UF_FACET_ERROR_BASE+2
#define UF_FACET_err_invalid_vertex_id      UF_FACET_ERROR_BASE+3
#define UF_FACET_err_invalid_edge_id        UF_FACET_ERROR_BASE+4
#define UF_FACET_err_non_manifold           UF_FACET_ERROR_BASE+5
#define UF_FACET_err_bad_adjacency          UF_FACET_ERROR_BASE+6
#define UF_FACET_err_facet_not_planar       UF_FACET_ERROR_BASE+7
#define UF_FACET_err_edge_not_found         UF_FACET_ERROR_BASE+8
#define UF_FACET_err_insufficient_vertices  UF_FACET_ERROR_BASE+9
#define UF_FACET_err_cannot_edit_occurrence UF_FACET_ERROR_BASE+10
#define UF_FACET_err_invalid_surf_dist_tol  UF_FACET_ERROR_BASE+11
#define UF_FACET_err_invalid_surf_ang_tol   UF_FACET_ERROR_BASE+12
#define UF_FACET_err_invalid_curve_dist_tol UF_FACET_ERROR_BASE+13
#define UF_FACET_err_invalid_curve_ang_tol  UF_FACET_ERROR_BASE+14
#define UF_FACET_err_invalid_curve_max_len  UF_FACET_ERROR_BASE+15
#define UF_FACET_err_invalid_facet_width    UF_FACET_ERROR_BASE+16
#define UF_FACET_err_invalid_num_sides      UF_FACET_ERROR_BASE+17
#define UF_FACET_err_solid_not_available    UF_FACET_ERROR_BASE+18
#define UF_FACET_err_zero_facets_produced   UF_FACET_ERROR_BASE+19
#define UF_FACET_err_body_not_alive         UF_FACET_ERROR_BASE+20
#define UF_FACET_err_invalid_version_number UF_FACET_ERROR_BASE+21
#define UF_FACET_err_vrml_file_not_found    UF_FACET_ERROR_BASE+22
#define UF_FACET_err_unknown_vrml_version   UF_FACET_ERROR_BASE+23
#define UF_FACET_err_not_a_vrml_file        UF_FACET_ERROR_BASE+24
#define UF_FACET_err_vrml_gunzip_fail       UF_FACET_ERROR_BASE+25
#define UF_FACET_err_vrml_parser_fail       UF_FACET_ERROR_BASE+26
#define UF_FACET_err_not_an_stl_file        UF_FACET_ERROR_BASE+27
#define UF_FACET_err_stl_parse_fail         UF_FACET_ERROR_BASE+28
#define UF_FACET_err_stl_invalid_data       UF_FACET_ERROR_BASE+29
#define UF_FACET_err_invalid_face_id        UF_FACET_ERROR_BASE+30
#define UF_FACET_err_invalid_face_tag       UF_FACET_ERROR_BASE+31
#define UF_FACET_err_object_not_supported   UF_FACET_ERROR_BASE+32
#define UF_FACET_err_solid_not_loaded       UF_FACET_ERROR_BASE+33
#define UF_FACET_err_bad_nx_curve_data      UF_FACET_ERROR_BASE+34
#define UF_FACET_err_precise_data_not_avail UF_FACET_ERROR_BASE+35
#define UF_FACET_err_not_solid_body_or_face UF_FACET_ERROR_BASE+36

/* From V14.0, the name of this structure was changed from
   UF_FACET_faceting_params_s to UF_FACET_parameters_s. Programs written prior
   to V14.0 that used this structure must be rewritten.

   Please note the following items:

   . When a solid body is faceted the faceter is always requested to ensure that
     the vertices of facets in adjacent faces match along model edges.

   . A macro (UF_FACET_INIT_PARAMETERS) is provided to initialize the structure
     to some reasonable value. This macro initializes the version field to the
     current version correctly. If this version field is set by the user's
     program, the behavior of the program becomes unpredictable.

   . The CAM users should ensure that the following guidelines are followed when
     faceting to ensure that the model that is generated is marked for use by
     CAM processors. If the model does not meet the minimum faceting parametric
     requirements, the model is not useable for the CAM processors and the
     processors might regenerate the model.

     1.  Set the variables in the UF_FACET_parameters_t structure as follows:
         -  max_facet_edges = 3
         -  number_storage_type = FACET_TYPE_DOUBLE
         -  specify_surface_tolerance = true
         -  surface_dist_tolerance <= 0.0381 (mm)
         -  curve_dist_tolerance  <= 0.0381 (mm)
         -  surface_angular_tolerance <= 0.4
         -  specify_curve_tolerance = true
         -  curve_angular_tolerance <= 0.4
         -  specify_parameters = true
         -  specify_view_direction = true
         -  silh_view_direction[0] = tool_axis i component
         -  silh_view_direction[1] = tool_axis j component
         -  silh_view_direction[2] = tool_axis k component
         -  silh_chord_tolerance <= surface_dist_tolerance/2.0

     2.  Create the facet model on the geometry by using this module.

     3.  Use the function UF_CAM_PREPRO_mark_model_as_cam to mark the facet
         model for recognition by CAM processors.

   UF_FACET_faceting_params_s is used both for representing the default faceting
   parameters, and for the faceting parameters used to facet a particular solid.
   The default faceting parameters are inquired using
   UF_FACET_ask_default_parameters and set with UF_FACET_set_default_parameters.

   At the start of an Open API program the default faceting parameters are:

         max_facet_edges = 3

         specify_surface_tolerance = false

         specify_curve_tolerance = false

         specify_convex_facets = true

         specify_max_facet_size = false

         number_storage_type = UF_FACET_TYPE_FLOAT

         specify_view_direction = false

         specify_parameters = false

         store_face_tags = false

   The following string defined constants specify NULL values for all facet_ids,
   vertex_ids, and edge_ids.

         UF_FACET_NULL_FACET_ID

         UF_FACET_NULL_VERTEX_ID

         UF_FACET_NULL_EDGE_ID

*/

struct UF_FACET_parameters_s
  {
    int     version;                   /* The version of this structure.
                                       If UF_FACET_INIT_PARAMETERS macro
                                       is used this field will be initialized
                                       with the proper value. All calls to
                                       the functions
                                           UF_FACET_ask_default_parameters and
                                           UF_FACET_ask_model_parameters
                                       should be preceeded by the use of the
                                       macro to ensure proper initialization of
                                       this member.
                                       */
    int     max_facet_edges;           /* The maximum number of edges allowed
                                       in the facets that are to be generated.
                                       */
    logical  specify_surface_tolerance;    /* If this value is true, then
                                       values must be specified for
                                       surface_dist_tolerance
                                       and surface_angular_tolerance. If
                                       this value is false then values for
                                       surface_dist_tolerance and
                                       surface_angular_tolerance will be
                                       determined by the system based on the
                                       body box or face box of the solid entity
                                       being faceted.
                                       */
    double  surface_dist_tolerance;    /* This is the maximum distance from
                                       the surface to the facet.
                                       */
    double  surface_angular_tolerance; /* This is the maximum angular variation
                                       in radians of the surface normal
                                       over the facet. A value of zero
                                       indicates no constraint.
                                       */
    logical specify_curve_tolerance;   /* This indicates that values are to be
                                       specified for curve_dist_tolerance
                                       and curve_angular_tolerance and
                                       curve_max_length.  If this value is false
                                       then values for curve_dist_tolerance
                                       and curve_angular_tolerance will be
                                       determined by the system based on the
                                       body box or face box of the solid
                                       entity being faceted, and no restriction
                                       will be placed on the maximum length
                                       of curve that can be represented
                                       by a single facet edge.
                                       */
    double  curve_dist_tolerance;      /* This is the maximum distance between
                                       the facet edge and the curve segment
                                       represented by the facet edge. This
                                       applies only to those facet edges lying
                                       along solid edges.
                                       */
    double  curve_angular_tolerance;   /* This is the maximum angular variation
                                       in radians of the curve tangent along
                                       the curve segment represented by the
                                       facet edge. This applies only to those
                                       facet edges lying along solid edges.
                                       A value of zero indicates no constraint.
                                       */
    double  curve_max_length;
    logical specify_convex_facets;     /* This indicates that the facets
                                       generated by the faceter should all be
                                       convex
                                       */
    logical specify_max_facet_size;    /* This indicates that a maximum width of
                                       facet is to be specified using
                                       max_facet_size. If this field is false
                                       then no maximum facet size is imposed.
                                       */
    double  max_facet_size;            /* This is the maximum width of a facet.
                                       This is only used if
                                       specify_max_facet_size is TRUE.
                                       */
    int     number_storage_type;       /* This indicates whether the real
                                       numbers for facet vertices and facet
                                       normals should be stored as floats
                                       (UF_FACET_TYPE_FLOAT) or as doubles
                                       (UF_FACET_TYPE_DOUBLE). Note that this
                                       option applies only when a faceted model
                                       is being created, and is ignored when the
                                       model is updated.
                                       */
    logical specify_parameters;        /* This indicates that the model will be
                                       created with the parametric information
                                       for each vertex.  Should parameters at
                                       the vertices be obtained for the facets
                                       of the model.
                                       */
    logical specify_view_direction;    /*  Should we use a viewing direction
                                       for denser faceting around
                                       silhouettes.  The denser faceting will
                                       honor the tolerance specified by
                                       silh_chord_tolerance in the silhouette
                                       with respect to the view direction
                                       specified by silh_view_direction vector.
                                       If this is false, there is no special
                                       consideration for any silhouette area.
                                       */
    double  silh_view_direction[3];    /* If use_view_direction is specified,
                                       then this is the view direction to use.
                                        */
    double  silh_chord_tolerance;      /* If use_view_direction is specified
                                       then this is the tolerance which will be
                                       used as a tighter surface tolerance
                                       in the silhouette area specified
                                       by the view direction.
                                       */
    logical  store_face_tags;          /* Should this FACET body record face
                                       tags or not. Note that this must be set
                                       to "true" for the functions
                                       UF_FACET_ask_solid_face_of_face_id,
                                       UF_FACET_ask_solid_face_of_facet, and
                                       UF_FACET_ask_face_id_of_solid_face to
                                       return meaningful results.
                                       */
  };

typedef struct UF_FACET_parameters_s UF_FACET_parameters_t;
typedef struct UF_FACET_parameters_s *UF_FACET_parameters_p_t;
typedef const struct UF_FACET_parameters_s UF_FACET_parameters_c_t;
typedef const struct UF_FACET_parameters_s *UF_FACET_parameters_pc_t;

/*
    Constants.
*/

/*
    Storage types.
*/
#define UF_FACET_TYPE_DOUBLE 1
#define UF_FACET_TYPE_FLOAT  2

/*
    NULL facet and edge ids.
*/
#define UF_FACET_NULL_FACET_ID (~0U)
#define UF_FACET_NULL_EDGE_ID  (~0U)
#define UF_FACET_NULL_FACE_ID  (~0U)

#define UF_FACET_DRAW_INTERIOR     0
#define UF_FACET_DRAW_WIRE         1
#define UF_FACET_DRAW_SILHOUETTE   2

/*
    Convexity values for edges and vertices.
*/
#define UF_FACET_IS_CONVEX                (-1)
#define UF_FACET_IS_CONCAVE                 1
#define UF_FACET_CONVEXITY_NOT_DETERMINED   0

/* Macro to initialize the parameters with the version setting and some basic
  defaults
*/

#define UF_FACET_PARAM_VERSION_CURR  (-2)

#define UF_FACET_INIT_PARAMETERS(__params) {(__params)->version = UF_FACET_PARAM_VERSION_CURR; (__params)->max_facet_edges = 3; (__params)->surface_dist_tolerance = 0.0; (__params)->surface_dist_tolerance = 0.0; (__params)->surface_angular_tolerance   = 0.0;(__params)->surface_angular_tolerance = 0.0;(__params)->specify_curve_tolerance = false;(__params)->curve_dist_tolerance = 0.0;(__params)->curve_angular_tolerance = 0.0;(__params)->curve_max_length = 1000.0;(__params)->specify_convex_facets  = true;(__params)->specify_max_facet_size = false;(__params)->max_facet_size = 0.0;(__params)->number_storage_type = 1;(__params)->specify_parameters = false;(__params)->specify_view_direction = false;(__params)->silh_view_direction[0]  = 0.0;(__params)->silh_view_direction[1] = 0.0;(__params)->silh_view_direction[2] = 1.0;(__params)->silh_chord_tolerance = 0.0;(__params)->store_face_tags = false;}


/*******************************************************************************
     a) Setting and enquiring module parameters
*******************************************************************************/

/*******************************************************************************
Sets the default faceting parameters for creating faceted models from
solid bodies and faces.

Environment: Internal  and  External

See Also:  UF_FACET_ask_default_parameters
           UF_FACET_ask_model_parameters

History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_set_default_parameters(
UF_FACET_parameters_p_t parameters  /* <I>
                                    Default parameters for faceting solids.
                                    */
);

/*******************************************************************************
Enquires  the default faceting parameters for creating faceted models
from solid bodies and faces.

Environment: Internal  and  External

See Also:  UF_FACET_set_default_parameters
           UF_FACET_ask_model_parameters


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_default_parameters(
UF_FACET_parameters_p_t parameters  /* <O>
                                    Default parameters for faceting solids.
                                    */
);

/*******************************************************************************
     b) Creating and updating faceted models

        Faceted models can either be build by hand or (more usually) generated
        from solids. In the case of models which are generated from solids when
        the solid is modified the faceted model is marked as out-of-date. While
        out-of-date faceted models will be updated automatically when the part
        containing them is saved, functions are also supplied for determining if
        a faceted model is up to date and for updating it if it is not.
*******************************************************************************/

/*******************************************************************************
Produces a faceted model from a solid body or face.
NOTE: The faceted body created is added to the reference set of the
work occurrence if used in context.
Return:
         Return code:
        0 = No error
    not 0 = Error code, which includes
            UF_FACET_err_non_manifold

Environment: Internal  and  External
See Also:  UF_FACET_ask_default_parameters
           UF_FACET_ask_model_parameters
           UF_FACET_is_model_up_to_date
           UF_FACET_update_model


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_facet_solid(
tag_t solid_entity ,/* <I>
                    The solid to be faceted
                    */
UF_FACET_parameters_p_t parameters ,/* <I>
                                    The parameters to be used to facet
                                    the solid. If NULL is specified
                                    then the defaults are used.
                                    */
tag_t * facet_model  /* <O>
                     The faceted model produced
                     */
);

/*******************************************************************************
Updates a faceted model if it was generated from a solid. This
function returns an error if the faceted model was not generated from
a solid. If NULL is specified for the faceting parameters then those
used to facet the solid previously are used.

If the model is already up to date with the same faceting parameters,
then this function performs no action. If the model is not derived from
a solid then an error is returned.
Return:
         Return code:
        0 = No error
    not 0 = Error code, which includes
            UF_FACET_err_non_manifold

Environment: Internal  and  External

See Also:  UF_FACET_ask_default_parameters
           UF_FACET_ask_model_parameters
           UF_FACET_is_model_up_to_date


History: In V14.0, the parameters argument data type was changed to
         UF_FACET_parameters_p_t.
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_update_model(
tag_t model ,/* <I>
             The faceted model to update.
             */
UF_FACET_parameters_p_t parameters  /* <I>
                                    The parameters to be used for faceting the
                                    model. If NULL is specified then the
                                    original parameters are used.
                                    */
);

/*******************************************************************************
Creates an empty faceted model which is not associated with any solid.

Environment: Internal  and  External

See Also:  UF_FACET_add_facet_to_model
           UF_FACET_model_edits_done


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_create_model(
tag_t object_in_part ,/* <I>
                      An object in the part in which the faceted model is
                      to be created.
                      */
tag_t * model  /* <O>
               The new faceted model.
               */
);


/*******************************************************************************
Indicates that edits to the specified faceted model are now complete.
This allows the system to delete the temporary data structures which it
creates to facilitate editing. This function should be called after the
program has completed a sequence of editing operations (other than
creation and update) on a faceted model.

Note that if this routine is not called then no harm results, other than
that the program will consume more memory than is necessary.

Environment: Internal  and  External
See Also:  UF_FACET_create_model


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_model_edits_done(
tag_t model  /* <I>
             The model which we have finished editing.
             */
);

/*******************************************************************************
Adds a facet to a faceted model.  The "adjacent_facet_ids" array
contains a facet id for each edge in the new facet. A value
of UF_FACET_NULL_FACET_ID means that that edge of the new
facet is not to be made adjacent to any existing facet. Note
that the adjacent facets must contain an edge corresponding
to that in the new facet, and if they do not then an error is
returned and no facet is created. This function can return the
error code UF_FACET_err_zero_facets_produced when given a
polygon with adjacent duplicate vertices.

Return:
         Return code:
        0 = No error
    not 0 = Error code, which includes
                UF_FACET_err_non_manifold
                UF_FACET_err_bad_adjacency
                UF_FACET_err_facet_not_planar
                UF_FACET_err_zero_facets_produced

Environment: Internal  and  External
See Also:  UF_FACET_del_facet_from_model
           UF_FACET_set_adjacent_facet


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_add_facet_to_model(
tag_t model ,/* <I>
             The model to which the facet is to be added
             */
int num_vertices ,/* <I>
                  The number of vertices in the new facet
                  */
double vertices[][3] ,/* <I,len:num_vertices>
                      The vertices of the new facet. Each element of
                      three double in this argument represents a 3-space
                      (X, Y, Z) position.
                      */
double normals[][3] ,/* <I,len:num_vertices>
                     The vertex normals for the new facet. Each element
                     of three double in this argument represents a
                     3-space (X, Y, Z) normal vector
                     If this is specified as NULL then the facet normal
                     will be computed and used for all of the vertices in
                     the new facet.
                     */
int adjacent_facet_ids[] ,/* <I>
                          The facets which are adjacent to the new facet at
                          each of its edges. If there is no adjacent facet to
                          the edge then UF_FACET_NULL_FACET_ID should
                          be specified for that edge.
                          */
int * new_facet_id  /* <O>
                    The id of the new facet created
                    */
);

/*******************************************************************************
Deletes a facet from a model. This operation leaves a hole in the
faceted model where the facet was deleted, unless the deleted facet
was at the edge of a sheet. If the model previously enclosed space
then it will no longer do so. If required at a future time, the hole can
be patched either by using UF_FACET_add_facet_to_model to add
new facets to the model, or by using UF_FACET_set_adjacent_facet  to
stitch existing facets onto the model.

Environment: Internal  and  External

See Also:  UF_FACET_add_facet_to_model



History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_del_facet_from_model(
tag_t model ,/* <I>
             The model from which the facet is to be deleted.
             */
int facet_id  /* <I>
              The facet id of the facet to be deleted
              */
);

/*******************************************************************************
Deletes all of the facets from a model.

Environment: Internal  and  External

See Also:  UF_FACET_add_facet_to_model



History:
*******************************************************************************/
extern  UFUNEXPORT int UF_FACET_delete_all_facets_from_model(
tag_t   model  /* <I>
               The model from which the facet is to be deleted.
               */
);

/*******************************************************************************
Sets a facet as being adjacent to another facet along a specified edge.
Return:
         Return code:
        0 = No error
    not 0 = Error code, which includes
            UF_FACET_err_bad_adjacency

Environment: Internal  and  External

See Also:  UF_FACET_add_facet_to_model


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_set_adjacent_facet(
tag_t model ,/* <I>
             The model in which the two facets reside
             */
int facet_id ,/* <I>
              The facet for which the adjacent facet is to be
              specified
              */
int edge ,/* <I>
          The edge in facet_id for which and adjacent facet is
          to be specified.
          */
int adjacent_facet_id  /* <I>
                       The adjacent facet.
                       */
);

/*******************************************************************************
Disassociates a faceted model from its generating solid so that it
stands on its own.  The link is established only if the faceted
model was created using UF_FACET_facet_solid.

Environment: Internal  and  External

See Also:  UF_FACET_facet_solid



History:
******************************************************************************/
extern UFUNEXPORT int UF_FACET_disassoc_from_solid(
tag_t model  /* <I>
             The model which is to be disassociated from its
             solid definition.
             */
);

/*******************************************************************************
Determines the adjacencies between the facets of a faceted body. The
routine uses the individual facet definitions and determines which
have shared edges. It is particularly useful where the faceted body has
been constructed using UF_FACET_add_facet_to_model without
specifying the adjacent facets, and may prove convenient when writing
code to import faceted models from elsewhere.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_rebuild_adjacencies(
tag_t model  /* <I>
             The tag of the faceted model
             */
);

/*******************************************************************************
Change the location of a vertex of a facet in a faceted body. Note that
the normals at this vertex are not changed.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_set_vertex_of_facet(
tag_t model,         /* <I>
                        The model.
                     */
int facet_id,        /* <I>
                        The id of the facet.
                     */
int vertex_in_facet, /*<I>
                       The vertex whose location is being changed.
                     */
double location[3]   /*<I>
                       The new location of the vertex.
                     */
);

/*******************************************************************************
    c) Enquiring data from faceted models

*******************************************************************************/

/*******************************************************************************
Iterates over the facets in a faceted model. The cycle is started using
the code UF_FACET_NULL_FACET_ID and this is also returned
when there are no further facets in the model. Note that although
"facet_id" is an integer, there is no guarantee that "facet_id+1" is a
valid facet id.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_cycle_facets(
tag_t model ,/* <I>
             The faceted model to be cycled.
             */
int * facet_id  /* <I/O>
                On input the id of the current facet in the model.  Pass in
                UF_FACET_NULL_FACET_ID to start the cycle.
                On output the id of the next facet in the model, if there are
                no more facets, UF_FACET_NULL_FACET_ID is returned.
                */
);
/*******************************************************************************
Enquires the number of facets in a model.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_n_facets_in_model(
tag_t model ,/* <I>
             The model.
             */
int * num_facets  /* <O>
                  The number of facets in the model.
                  */
);
/*******************************************************************************
Enquires the maximum number of vertices of any facet in the model.
This routine can be used to ensure that the arrays required by
UF_FACET_ask_vertices_of_facet and UF_FACET_ask_normals_of_facet are
sufficiently large to contain the result.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_max_facet_verts(
tag_t model ,/* <I>
             The model.
             */
int * num_facets  /* <O>
                  The maximum number of facets of any facet in the model.
                  */
);
/*******************************************************************************
Enquires the number of vertices in a facet.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_num_verts_in_facet(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
int * num_vertices  /* <O>
                    The number of vertices in the facet.
                    */
);
/*******************************************************************************
Enquires the vertices of the facet with the specified facet id.
The caller is responsible for assuring that the vertices array is
large enought to hold all of the vertices of the facet.

Environment: Internal  and  External

See Also:  UF_FACET_ask_normals_of_facet
           UF_FACET_ask_max_facet_verts
           UF_FACET_ask_num_verts_in_facet


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_vertices_of_facet(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
int * num_vertices ,/* <O>
                    The number of vertices in the facet.
                    */
double vertices[][3]  /* <O,len:num_vertices>
                      The vertices for this facet. Each element of three
                      double in this argument represents a 3-space
                      (X, Y, Z) position.
                      Note that this is passed by the caller, not allocated
                      by the routine, and the caller is responsible for
                      ensuring that this array is sufficiently long, which
                      can be done by previously calling
                      UF_FACET_ask_num_verts_in_facet or by calling
                      UF_FACET_ask_max_facet_verts.
                      */
 );
/*******************************************************************************
Enquires the vertex normals of the facet with the specified facet id.
The caller is responsible for making sure that the normals array
is large enough to contain all of the normal data.

Environment: Internal  and  External

See Also:  UF_FACET_ask_vertices_of_facet
           UF_FACET_ask_num_verts_in_facet
           UF_FACET_ask_max_facet_verts


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_normals_of_facet(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
int * num_vertices ,/* <O>
                    The number of vertices in the facet.
                    */
double normals[][3]  /* <O,len:num_vertices>
                          The vertex normals for this facet. Each element of
                          three double in this argument represents a 3-space
                          (X, Y, Z) normal vector.
                          Note that this is passed by the caller, not allocated
                          by the routine, and the caller is responsible for
                          ensuring that this array is sufficiently long, which
                          can be done by previously calling
                          UF_FACET_ask_num_verts_in_facet or by calling
                          UF_FACET_ask_max_facet_verts.
                          */
);

/*******************************************************************************
Enquires the vertex parameters of the facet with the specified facet id.
The caller is responsible for making sure that the params array
is large enough to contain all of the parameter data.

Environment: Internal  and  External

See Also:  UF_FACET_ask_vertices_of_facet
           UF_FACET_ask_num_verts_in_facet
           UF_FACET_ask_max_facet_verts

History: Original release was in V14.0.
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_params_of_facet(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
int * num_params ,/* <O>
                  The number of vertices in the facet.
                  */
double params[][3]  /* <O,len:num_params>
                         The vertex parameters for this facet. Each element
                         of three double in this argument represents the
                         parametric values (u,v,t) at a vertex.
                         Note that this is passed by the caller, not allocated
                         by the routine, and the caller is responsible for
                         ensuring that this array is sufficiently long, which
                         can be done by previously calling
                         UF_FACET_ask_num_verts_in_facet or by calling
                         UF_FACET_ask_max_facet_verts.
                         */
);

/*******************************************************************************
Enquires the facet adjacent to a specified edge of a specified facet. If
there is no facet adjacent to the facet edge specified then
UF_FACET_NULL_FACET_ID is returned in adjacent_facet_id and
the contents of edge_id_in_adjacent_facet is undefined.

Environment: Internal  and  External

See Also :  UF_FACET_add_facet_to_model
            UF_FACET_set_adjacent_facet


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_adjacent_facet(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
int edge_id ,/* <I>
             The edge of which the adjacent facet is being
             inquired.
             */
int * adjacent_facet_id ,/* <O>
                         The adjacent facet
                         */
int * edge_id_in_adjacent_facet  /* <O>
                                 The edge in the adjacent facet which is
                                 adjacent to edge_id in facet_id.
                                 */
);
/*******************************************************************************
Determines if a specified edge appears in a specified facet.

Return:
         Return code:
        0 = No error
    not 0 = Error code which includes
            UF_FACET_err_edge_not_found

Environment: Internal  and  External

See Also:  UF_FACET_ask_adjacent_facet


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_find_edge_in_facet(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
double vertex_1[3] ,/* <I>
                    The first vertex in the edge. This is a 3-space
                    (X, Y, Z) position.
                    */
double vertex_2[3] ,/* <I>
                    The second vertex in the edge.  This is a 3-space
                    (X, Y, Z) position.
                    */

int * sense ,/* <O>
             The sense of the edge in the facet. This is:
             0 if the edge appears as vertex_1 -> vertex_2
             1 if the edge appears as vertex_2 -> vertex_1
             */
int * edge_id  /* <O>
               The id of the edge in the facet.
               */
);
/*******************************************************************************
Enquires if a faceted model is up to date.

Environment: Internal  and  External

See Also:  UF_FACET_update_model


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_is_model_up_to_date(
tag_t model ,/* <I>
             The faceted model.
             */
logical * up_to_date  /* <O>
                      Whether or not "model" is up_to_date.
                      */
);
/*******************************************************************************
Enquires the solid model on which a faceted model is based. If the
faceted model is not based on any solid then NULL_TAG is returned.

Environment: Internal  and  External

See Also:  UF_FACET_ask_models_of_solid


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_solid_of_model(
tag_t model ,/* <I>
             The faceted model.
             */
tag_t * solid  /* <O>
               The associated solid. This is NULL_TAG if there is
               no associated model.
               */
);
/*******************************************************************************
Enquire the solid model on which a faceted model is based. If
the faceted model is not based on any solid or if the solid is
excluded by reference set or is in an unloaded component then
NULL_TAG is returned in "solid"

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_available_solid
(
  tag_t     model,              /* <I>
                                The model.
                                */
  tag_t   * solid               /* <O> IF "model has an available
                                defining solid then the tag of that
                                solid, otherwise NULL_TAG".
                                */
);

/******************************************************************************
Enquire the faceted model(s) of a specified solid body or face.

Environment: Internal  and  External

See Also:  UF_FACET_ask_solid_of_model


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_models_of_solid(
tag_t solid ,/* <I>
             A solid body or face
             */
int * n_faceted_models ,/* <O>
                        The number of faceted models associated with
                        "solid".
                        */
tag_t ** faceted_models  /* <OF,len:n_faceted_models>
                         The tags of the faceted models associated with
                         "solid". This space is allocated by the called routine
                         and must be freed by the caller using UF_free.
                         */
);
/*******************************************************************************
Determines faceting parameters when given a faceted model which
was generated from (and remains associated with a solid).

Environment: Internal  and  External

See Also: UF_FACET_facet_solid
          UF_FACET_update_model


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_model_parameters(
tag_t model ,/* <I>
             The model.
             */
UF_FACET_parameters_p_t parameters  /* <O>
                                    The parameters to facet the solid
                                    associated with "model".
                                    */
);
/*******************************************************************************
Enquires the convexity of a vertex in a facet. The convexity values are
UF_FACET_IS_CONVEX, UF_FACET_IS_CONCAVE, and
UF_FACET_CONVEXITY_NOT_DETERMINED; the last of these
indicates that the two edges from the vertex are very nearly colinear
and therefore whether the vertex should be considered convex or
concave is unclear.

Environment: Internal  and  External

See Also:  UF_FACET_ask_edge_convexity


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_vertex_convexity(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
int vertex_in_facet ,/* <I>
                     The vertex for which convexity is being inquired.
                     */
int * convexity  /* <O>
                 The convexity of the vertex
                 */
);
/*******************************************************************************
Enquires the convexity of an edge between two facets. The convexity
values are UF_FACET_IS_CONVEX, UF_IS_FACET_CONCAVE,
and UF_FACET_CONVEXITY_NOT_DETERMINED; the last of
these indicate that the two facets adjacent to the edge are very nearly
coplanar and therefore whether the edge should be considered convex
or concave is unclear. (Note that an ifail is returned if the specified
edge is open.)

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_edge_convexity(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
int edge_in_facet ,/* <I>
                   The edge for which convexity is being inquired.
                   */
int * convexity  /* <O>
                 The convexity of the edge.
                 */
);
/*******************************************************************************
Enquires if a facet is convex. A facet is convex if none of its vertices
are concave.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_is_facet_convex(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
logical * is_convex  /* <O>
                     TRUE = facet has no concave vertices
                     FALSE = facet has concave vertices
                     */
);
/*******************************************************************************
Enquires if a faceted model is convex. A model is convex if none of its
edges are concave.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_is_model_convex(
tag_t model ,/* <I>
             The model
             */
logical * is_convex  /* <O>
                     TRUE if the model has no concave edges and
                     FALSE otherwise.
                     */
);
/*******************************************************************************
Enquire the plane equation of a facet.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_plane_equation(
tag_t model ,/* <I>
             The model
             */
int facet_id ,/* <I>
              The id of the facet.
              */
double plane_normal[3] ,/* <O>
                        The plane normal for the facet. This is a 3-space
                        (X, Y, Z) normal vector. The (X, Y, Z) of this
                        vector provide the A, B, and C coefficients
                        respectively of the plane equation:
                        Ax + By + Cz +D = 0
                        */
double * d_coefficient  /* <O>
                        The d_coefficient for the plane of the facet. This
                        provides the D coefficient in the above equation.
                        */
);
/*******************************************************************************
Enquire the face id of a face, given its tag.  Output is a pointer to
UF_FACET_NULL_FACE_ID if the face is not present in the model or if
face tags have not been stored (note that face tags are stored only if
"store_face_tags" is set to "true" when faceting a solid).

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_face_id_of_solid_face(
tag_t model,    /* <I>
                The model.
                */
tag_t face_tag, /* <I>
                The solid face tag.
                */
int *face_id    /* <O>
                The face id.
                */
);

/*******************************************************************************
Enquire the solid face tag of a facet.  Output is a pointer to NULL_TAG if the
facet is not associated with any face in the model.  If the facet_id is out of
range for this model an error will occur.

Note that the model must have been faceted with "store_face_tags" set to
"true" for this function to return a meaningful result (otherwise NULL_TAG
will be returned for all facets).

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_solid_face_of_facet(
tag_t model,    /* <I>
                The model
                */
int facet_id,   /* <I>
                The id of the facet.
                */
tag_t *face_tag /* <O>
                The solid face tag.
                */
);


/*******************************************************************************
Enquire the solid face tag of a face, given its id.  If the face id is out of
range for this model, an error will occur.  If face tags have not been stored
and the face id is in range, then NULL_TAG is output. (Note that face tags are
stored only if "store_face_tags" is set to "true" when faceting a solid.)

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_solid_face_of_face_id(
tag_t model,    /* <I>
                The model.
                */
int face_id,    /* <I>
                The id of the face.
                */
tag_t *face_tag /*<O>
                The solid face tag.
                */
);

/*******************************************************************************
Enquire the face id of a facet.  Output is a pointer to UF_FACET_NULL_FACE_ID if
the facet is not associated with any face in the model.  If the facet_id is out
of range for this model an error will occur.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_face_id_of_facet(
tag_t model,    /* <I>
                The model.
                */
int facet_id,   /* <I>
                The id of the facet.
                */
int *face_id    /* <O>
                The id of the face.
                */
);

/*******************************************************************************
Enquire the number of faces in a model.  Typically only useful if the model has
been derived from a solid model.  For models constructed directly, the output
will be zero.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_num_faces(
tag_t model,    /* <I>
                The model.
                */
int *num_faces  /* <O>
                The number of faces in the model.
                */
);

/*******************************************************************************
Enquire the number of facets in a face.  If the face_id is out of range for this
model an error will occur.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_num_facets_in_face(
tag_t model,    /* <I>
                The model.
                */
int face_id,    /* <I>
                The id of the face.
                */
int *num_facets /* <O>
                The number of facets in the face.
                */
);


/*******************************************************************************
Iterates over the facets in a face. The cycle is started using
the code UF_FACET_NULL_FACET_ID and this is also returned
when there are no further facets in the face. Note that although
"facet_id" is an integer, there is no guarantee that "facet_id+1" is a
valid facet id.
If the face_id is outside the range for this model, an error occurs.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_cycle_facets_in_face(
tag_t model,    /* <I>
                The model.
                */
int face_id,    /* <I>
                The face whose facets are to be cycled.
                */
int *facet_id   /* <I/O>
                On input the id of the current facet in the model.  Pass in
                UF_FACET_NULL_FACET_ID to start the cycle.
                On output the id of the next facet in the model, if there are
                no more facets, UF_FACET_NULL_FACET_ID is returned.
                */
);


/*******************************************************************************
Enquire the surface data of a face.  If the face_id is out of range for this
model an error will occur.

Environment: Internal  and  External

See Also:

History: Originally released in NX8.5.1
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_surface_data_for_face(
tag_t  facet_face,            /* <I>
                              The tag of the facet face
                              */
int    *type,                 /* <O>
                              The surface type. The value of this type 
                              corresponds with the type in the 
                              NxOpen::Face::FaceType enum.
                              If not analytic
                              (plane/cylinder/cone/torus/sphere) then this will 
                              be FaceTypeUndefined.
                              */
double pos[3],                /* <O>
                              The origin:
                                3D point:  Point on plane
                                Point on axis(Cylinder, Cone)
                                Centre point(Sphere, Torus)
                              */
double dir[3],                /* <O>
                              The normal direction for planes and axis for
                              others. NA for Sphere.
                              */
double *radius,               /* <O>
                              Radius:
                                Not valid for planes
                                Radius(Cylinder, Sphere, Torus(Major Axis), 
                                Cone(Radius in plane passing through position)
                              */
double *radius_data,          /* <O>
                              Not valid for planes, cylinders, spheres
                              for cones this is the half angle, 
                              for torus it is the minor radius. 
                              */
logical   *sense,                /* <O>
                              The sense of the face with respect to the normal
                              direction
                              */
logical   *from_cached_analytics /* <O>
                              true - If the surface data was obtained from the
                              lightweight analytic data cached in the facet
                              model and false - if it was derived using an
                              inferencing algorithm.
                              */
);
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_FACET_H_INCLUDED */
