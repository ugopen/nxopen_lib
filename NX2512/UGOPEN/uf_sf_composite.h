/*******************************************************************************

   Copyright (c) 1998-2001 Unigraphics Solutions Inc.
                 Unpublished - All rights reserved
________________________________________________________________________________





File description:

   Internal type definitions for UF_SF_COMPOSITE (Scenario Composite Face)
   module.

*******************************************************************************/


#ifndef UF_SF_COMPOSITE_H_INCLUDED
#define UF_SF_COMPOSITE_H_INCLUDED

#include <uf_sf_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************** Default definitions for Meshing attributes ***************/

/* ----------------------------------------------------------------------------
Decription of  UF_SF_COMPOSITE_parameters_s:

1. auto_create_comp_edges: This logical parameter indicates whether composite
                           edges should be created automatically during the
                           creation of composite faces.  For example, during
                           the manual creation of a composite face, if, by
                           compositing the faces together 2 of the bounding
                           edge meet at a vertex that is only used by those 2
                           edges, these 2 edges will be candidates to be
                           composited into a composite edge.  If
                           auto_create_comp_edges == FALSE, no composite edges
                           will be created.  If auto_create_comp_edges == TRUE,
                           the edgew will be composited together if they meet
                           the min_edge_int_angle criteria below.
2. min_edge_int_angle:     This angle (input in degrees) is the criteria by
                           which it is decided whether to composite 2 edges
                           together or not.  If 2 edges share a common vertex,
                           and that vertex is used by only 2 edges, then the
                           angle (beta) between the 2 edges is computed.  If
                           beta > min_edge_int_angle, the edges will be
                           composited together.  If beta <= min_edge_int_angle,
                           the edges will not be composited together.

*****************************************************************************/
struct  UF_SF_COMPOSITE_parameters_s
{
    logical    auto_create_comp_edges;     /* see description above.        */
    int        min_edge_int_angle;         /* see description above.        */
};
typedef struct  UF_SF_COMPOSITE_parameters_s UF_SF_COMPOSITE_parameters_t;


/* ----------------------------------------------------------------------------
Decription of  UF_SF_COMPOSITE_auto_parameters_s:
*
*   1. comp_parameters :-      Parameters used by both manual and auto
*                              compositing.  See description of
*                              UF_SF_COMPOSITE_parameters_t above.
*
*   2. min_edge_size :-        The minimum edge length allowed in the model.
*                              Valid Range: {0.0 < min_edge_size}
*                              Autocompositing will be performed on body_tag in
*                              order to eliminate all edges that are smaller
*                              than min_edge_size.  Note, however, that it is
*                              not guaranteed that all edges smaller than
*                              min_edge_size will be eliminated because doing so
*                              may violate the face_deviation_angle.
*
*   3. sliver_factor :-        The user specified minimum sliver factor.
*                              sliver_factor is a ratio related to the ratio of
*                              surface area divided by circumference which
*                              detect faces that have a small surface area
*                              compared to their curcumference.
*                              Valid Range: {0.0 < sliver_factor <= 1.0} where
*                                  0.000 == a zero surface area surface.
*                                  0.056 == a rectangle 1x1000
*                                  0.175 == a rectangle 1x100
*                                  0.300 == recommended value.
*                                  0.510 == a rectangle 1x10
*                                  0.510 == a rectangle 1x10
*                                  0.886 == a perfect square.
*                                  1.000 == a perfect circle.
*
*   4. min_corner_angle :-     An angle (in degrees) representing the minimum
*                              allowable angle at the corner of a surface.  Any
*                              face with an angle less than this at a corner
*                              will be a candidate for compositing with a
*                              neighbor surface to eliminate this small angle.
*                              Like min_edge_size, however, there is no
*                              guarantee that all corner angles less than
*                              min_corner_angle will be eliminated because
*                              doing so may violate the face_deviation_angle.
*                              Valid Range:  {0.0 <= min_corner_angle <= 90}
*
*   5. face_deviation_angle :- An angle (in degrees) representing the maximum
*                              that the dihedral angle between 2
*                              adjacent faces deviate from 180 degrees and
*                              still be considered a candiate for compositing.
*                              On the edge that is shared by surface1 and
*                              surface2, the surface normals of the 2 surfaces
*                              are compared.  If they deviate from each other
*                              by more than face_deviation_angle, then the
*                              surface will not be composite together unless
*                              necessary to eliminate a face which violates
*                              the sliver_factor.
*                              Valid Range: {0.0 <= face_deviation_angle <= 180}
*
*****************************************************************************/
struct  UF_SF_COMPOSITE_auto_parameters_s
{
    UF_SF_COMPOSITE_parameters_t comp_parameters;
    double        min_edge_size;
    double        sliver_factor;
    int           min_corner_angle;
    int           face_deviation_angle;
};
typedef struct  UF_SF_COMPOSITE_auto_parameters_s UF_SF_COMPOSITE_auto_parameters_t;

#ifdef __cplusplus
}
#endif

#endif  /* UF_SF_COMPOSITE_H_INCLUDED  */
