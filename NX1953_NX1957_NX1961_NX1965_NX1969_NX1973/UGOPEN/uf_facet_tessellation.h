/*******************************************************************************
Copyright 2019 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.



File description:

    Open API support for Tessellations.

    The functions in this API provide access to create tessellations of a given face.
    Tessellations in this API are collections of facets created without modifying
    the NX data model, which gives this API improved performance compared to
    the existing FACET API.

    The functions in this API allow you to:
     - Create a tessellation from a given face.

     - Retrieve the vertices and vertex normals of a given facet from a tessellation.

     - Retrieve the count of facets in a tessellation.

     - Retrieve the face tag used to create the tessellation.

     - Retrieve the errors that occurred during the tessellation.

     - Delete the tessellation and free up the memory allocated.

    A tessellation consists of all the facets generated from a given face,
    each of which is identified within the tessellation by a facet id. It also contains
    the input tag and a list of errors that occurred during faceting.

    Tessellations can be created by using the UF_FACET_tessellate_face,
    by providing a single face and parameters to use to generate the facets for that
    face, in UF_FACET_tessellation_parameters_s. This will create a UF_FACET_tessellation_s.

    The facet behavior is largely the same as in the FACET API.

*******************************************************************************/
#ifndef UF_FACET_TESSELLATION_H_INCLUDED
#define UF_FACET_TESSELLATION_H_INCLUDED

#include <uf_defs.h>
#include <string.h>
#include <libufun_exports.h>
#include <uf_facet.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
    Error codes
*/
#define UF_FACET_tessellation_err_body_fault        UF_FACET_ERROR_BASE+39
#define UF_FACET_tessellation_err_face_fault        UF_FACET_ERROR_BASE+40
#define UF_FACET_tessellation_err_facet_fault       UF_FACET_ERROR_BASE+41
#define UF_FACET_tessellation_err_normal_fault      UF_FACET_ERROR_BASE+42
#define UF_FACET_tessellation_err_thin_face_fault   UF_FACET_ERROR_BASE+43
#define UF_FACET_tessellation_err_mangled_fault     UF_FACET_ERROR_BASE+44

/*
    Structures
*/

/*  UF_FACET_tessellation_parameters_s is used to represent the faceting
parameters used to facet a particular face or body.
*/
struct UF_FACET_tessellation_parameters_s
{
    logical  specify_surface_dist_tolerance;    /* If this value is true, then
                                                values must be specified for
                                                surface_dist_tolerance.
                                                */
    double  surface_dist_tolerance;    /* This is the maximum distance from
                                       the surface to the facet.
                                       */
    logical  specify_surface_angular_tolerance; /* If this value is true, then
                                                values must be specified for
                                                surface_angular_tolerance.
                                                */
    double  surface_angular_tolerance; /* This is the maximum angular variation
                                       in radians of the surface normal
                                       over the facet. A value of zero
                                       indicates no constraint.
                                       */
    logical specify_curve_dist_tolerance;   /* This indicates that values are to be
                                            specified for curve_dist_tolerance.
                                            */
    double  curve_dist_tolerance;      /* This is the maximum distance between
                                       the facet edge and the curve segment
                                       represented by the facet edge. This
                                       applies only to those facet edges lying
                                       along solid edges.
                                       */
    logical specify_curve_angular_tolerance; /* This indicates that values are to be
                                             specified for curve_angular_tolerance.
                                             */
    double  curve_angular_tolerance;   /* This is the maximum angular variation
                                       in radians of the curve tangent along
                                       the curve segment represented by the
                                       facet edge. This applies only to those
                                       facet edges lying along solid edges.
                                       */

    logical specify_max_facet_size;    /* This indicates that a maximum width of
                                       facet is to be specified using
                                       max_facet_size.
                                       */
    double  max_facet_size;            /* This is the maximum width of a facet.
                                       */
};

typedef struct UF_FACET_tessellation_parameters_s UF_FACET_tessellation_parameters_t;
typedef struct UF_FACET_tessellation_parameters_s *UF_FACET_tessellation_parameters_p_t;
typedef const struct UF_FACET_tessellation_parameters_s UF_FACET_tessellation_parameters_c_t;
typedef const struct UF_FACET_tessellation_parameters_s *UF_FACET_tessellation_parameters_pc_t;

/*  UF_FACET_tessellation_error_s represents a single error
that can be retrieved using UF_FACET_ask_errors_during_tessellation.

Depending on the error code either facet_id or face_tag will be non-null.
*/
struct UF_FACET_tessellation_error_s
{
    int code;           /*  The error code that corresponds
                        to the error that occurred
                        */
    int facet_id;       /*  If the error code corresponds to
                        an error that involves a facet, the
                        facet ID will be here.
                        */
    tag_t face_tag;     /*  If the error code corresponds to
                        an error that involves a face, the
                        face tag will be here.
                        */
};

typedef struct UF_FACET_tessellation_error_s UF_FACET_tessellation_error_t;
typedef struct UF_FACET_tessellation_error_s *UF_FACET_tessellation_error_p_t;
typedef const struct UF_FACET_tessellation_error_s UF_FACET_tessellation_error_c_t;
typedef const struct UF_FACET_tessellation_error_s *UF_FACET_tessellation_error_pc_t;

/* This struct is defined somewhere else */
struct UF_FACET_tessellation_s;

typedef struct UF_FACET_tessellation_s UF_FACET_tessellation_t;
typedef struct UF_FACET_tessellation_s *UF_FACET_tessellation_p_t;
typedef const struct UF_FACET_tessellation_s UF_FACET_tessellation_c_t;
typedef const struct UF_FACET_tessellation_s *UF_FACET_tessellation_pc_t;

/*******************************************************************************
Produces a table of facets, a tessellation, from a given face tag.
Requires tessellation parameters as input, as there is no default.

Outputted tessellation can be checked for errors using UFX_FACET_ask_errors_during_tessellation

Return:
         Return code:
        0 = No error
    not 0 = Error code

Environment: Internal  and  External
History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_tessellate_face(
    tag_t face_tag,/* <I>
                   The face to be faceted
                   */
    UF_FACET_tessellation_parameters_p_t parameters,/* <I>
                                                    The parameters to be used to facet
                                                    the given face
                                                    */
    UF_FACET_tessellation_p_t  * tessellation  /* <O>
                                               The tessellation produced
                                               */
);

/*******************************************************************************
Enquires the vertices and vertex normals of the facet with the specified facet id.

Return:
         Return code:
        0 = No error
    not 0 = Error code

Environment: Internal  and  External
History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_facet_data_of_tessellation(
    UF_FACET_tessellation_p_t tessellation,/* <I>
                                           The tessellation to retrieve the
                                           specified facet from.
                                           */
    int facetID,    /* <I>
                    The ID of the facet to retrieve.
                    The range of this value is between 0 and
                    the count returned from UF_FACET_ask_num_facets_in_tessellation.
                    */
    double vertices[3][3],  /* <O>
                            The vertices of the specified facet.
                            */
    double vertex_normals[3][3]  /* <O>
                                 The vertex normals of the specified facet.
                                 */
);

/*******************************************************************************
Returns the count of facets in a tessellation.

Return:
         Return code:
        0 = No error
    not 0 = Error code

Environment: Internal  and  External
History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_num_facets_in_tessellation(
    UF_FACET_tessellation_p_t tessellation,    /* <I>
                                               The tessellation to return the count of facets from.
                                               */
    int *count /* <O>
               The count of facets in the tessellation.
               */
);

/*******************************************************************************
Return the face tag that was used to create the given tessellation.

Return:
         Return code:
        0 = No error
    not 0 = Error code

Environment: Internal  and  External
History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_face_of_tessellation(
    UF_FACET_tessellation_p_t tessellation,    /* <I>
                                               The tessellation to retrieve the face tag from.
                                               */
    tag_t *face_tag /* <O>
                    The face tag used as the input for the given tessellation.
                    */
);

/*******************************************************************************
Produces an array of UF_FACET_tessellation_error_s that contain the errors codes and error data that
occurred when tessellating.

Return:
         Return code:
        0 = No error
    not 0 = Error code

Environment: Internal  and  External
History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_ask_errors_during_tessellation(
    UF_FACET_tessellation_p_t tessellation,    /* <I>
                                               The tessellation to check for errors.
                                               */
    UF_FACET_tessellation_error_p_t * errors, /* <O>
                                              The array of UF_FACET_tessellation_error_s
                                              that contains error codes and error data.
                                              */
    int * error_count    /* <O>
                        Size of the errors array
                        */
);

/*******************************************************************************
Delete the provided tessellation and set the given pointer to nullptr

Return:
         Return code:
        0 = No error
    not 0 = Error code

Environment: Internal  and  External
History:
*******************************************************************************/
extern UFUNEXPORT int UF_FACET_delete_tessellation(
    UF_FACET_tessellation_p_t * tessellation  /* <I>
                                              The tessellation to delete.
                                              Will be set to nullptr.
                                              */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_FACET_TESSELLATION_H_INCLUDED */
