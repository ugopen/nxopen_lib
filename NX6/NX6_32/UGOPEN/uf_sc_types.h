/*==================================================================================================

                    Copyright (c) 2002-2006-2004 Unigraphics Solutions Inc.
                             Unpublished - All rights reserved
====================================================================================================



File description:

    Smart containers and section builders data structures and types

==================================================================================================*/

#ifndef UF_SC_TYPES_H_INCLUDED
#define UF_SC_TYPES_H_INCLUDED

#include <uf_defs.h>
#ifdef __cplusplus
extern "C" {
#endif

#define     UF_SC_EDGE_DUMB_EDGES            0
#define     UF_SC_EDGE_CHAIN_EDGES           1
#define     UF_SC_EDGE_TANGENT_EDGES         2
#define     UF_SC_EDGE_FACE_EDGES            3
#define     UF_SC_EDGE_BODY_EDGES            4
#define     UF_SC_EDGE_FEATURE_EDGES         5
#define     UF_SC_EDGE_SHBNDARY_EDGES        6
#define     UF_SC_EDGE_BOUNDARY_EDGES        7
#define     UF_SC_EDGE_VERTEX_EDGES          8
#define     UF_SC_EDGE_VERTEX_TANGENT_EDGES  9
#define     UF_SC_EDGE_INTERSECT_EDGES      10
#define     UF_SC_EDGE_MSEEDTAN_EDGES       11
#define     UF_SC_MAX_EDGES                 12

#define     UF_SC_FACE_DUMB_FACES      (UF_SC_MAX_EDGES + 1)
#define     UF_SC_FACE_REGION_FACES    (UF_SC_MAX_EDGES + 2)
#define     UF_SC_FACE_TANGENT_FACES   (UF_SC_MAX_EDGES + 3)
#define     UF_SC_FACE_FEATURE_FACES   (UF_SC_MAX_EDGES + 4)
#define     UF_SC_FACE_BODY_FACES      (UF_SC_MAX_EDGES + 5)
#define     UF_SC_FACE_ADJACENT_FACES  (UF_SC_MAX_EDGES + 6)
#define     UF_SC_FACE_CONNECTED_BLEND_FACES (UF_SC_MAX_EDGES + 7)
#define     UF_SC_FACE_ALL_BLEND_FACES       (UF_SC_MAX_EDGES + 8)
#define     UF_SC_FACE_RIB_FACES             (UF_SC_MAX_EDGES + 9)
#define     UF_SC_FACE_SLOT_FACES            (UF_SC_MAX_EDGES + 10)
#define     UF_SC_FACE_BOSS_POCKET_FACES     (UF_SC_MAX_EDGES + 11)
#define     UF_SC_FACE_MERGED_RIB_FACES       (UF_SC_MAX_EDGES + 12)
#define     UF_SC_MAX_FACES            (UF_SC_MAX_EDGES + 13)

#define     UF_SC_CURVE_DUMB_CURVES           (UF_SC_MAX_FACES + 1)
#define     UF_SC_CURVE_FEATURE_CURVES        (UF_SC_MAX_FACES + 2)
#define     UF_SC_CURVE_FEAT_CHAIN_CURVES     (UF_SC_MAX_FACES + 3)
#define     UF_SC_CURVE_FEAT_TANGENT_CURVES   (UF_SC_MAX_FACES + 4)
#define     UF_SC_CURVE_FOLLOW_FILLET_CURVES  (UF_SC_MAX_FACES + 5)
#define     UF_SC_CURVE_FEAT_POINTS           (UF_SC_MAX_FACES + 6)
#define     UF_SC_CURVE_REGION_BOUNDARY       (UF_SC_MAX_FACES + 7)
#define     UF_SC_MAX_CURVES                  (UF_SC_MAX_FACES + 8)

#define     UF_SC_BODY_DUMB_BODIES (UF_SC_MAX_CURVES + 1)
#define     UF_SC_MAX_BODY         (UF_SC_MAX_CURVES + 2)

#define     UF_SC_INVALID_TYPE     (UF_SC_MAX_BODY)

typedef union UF_SC_input_data_s *UF_SC_input_data_p_t;

struct UF_SC_EDGE_dumb_data_s
{
    int         num_edges;
    tag_t      *edges;
};
typedef struct UF_SC_EDGE_dumb_data_s
               UF_SC_EDGE_dumb_data_t, *UF_SC_EDGE_dumb_data_p_t;

struct UF_SC_EDGE_chain_data_s
{
    tag_t       start_edge;
    tag_t       end_edge;
    logical     from_start;             /* whether the chain starts from the start
                                           point of the start edge */
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_chain_data_s
               UF_SC_EDGE_chain_data_t, *UF_SC_EDGE_chain_data_p_t;

struct UF_SC_EDGE_tangent_data_s
{
    tag_t       start_edge;
    tag_t       end_edge;              /* it is optional */
    logical     from_start;            /* whether the tangent starts from the start
                                          point of the start edge if end edge is provided*/
    double      angle_tol;             /* angle tolerance for tangent edges */
    logical     same_convexity;        /* will only find tangnet edges that has the same convexity if true */
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_tangent_data_s
               UF_SC_EDGE_tangent_data_t, *UF_SC_EDGE_tangent_data_p_t;

struct UF_SC_EDGE_mseedtan_data_s
{
    int         num_seed_edges;
    tag_t      *seed_edges;
    double      angle_tol;             /* angle tolerance for tangent edges */
    logical     same_convexity;        /* will only find tangnet edges that has the same convexity if true */
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_mseedtan_data_s
               UF_SC_EDGE_mseedtan_data_t, *UF_SC_EDGE_mseedtan_data_p_t;

struct UF_SC_EDGE_face_data_s
{
    int         num_faces;
    tag_t      *faces;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_face_data_s
               UF_SC_EDGE_face_data_t, *UF_SC_EDGE_face_data_p_t;

struct UF_SC_EDGE_body_data_s
{
    tag_t      body;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_body_data_s
               UF_SC_EDGE_body_data_t, *UF_SC_EDGE_body_data_p_t;

struct UF_SC_EDGE_feature_data_s
{
    int         num_features;
    tag_t      *features;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_feature_data_s
               UF_SC_EDGE_feature_data_t, *UF_SC_EDGE_feature_data_p_t;

struct UF_SC_EDGE_shbndary_data_s
{
    tag_t      sheet;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_shbndary_data_s
               UF_SC_EDGE_shbndary_data_t, *UF_SC_EDGE_shbndary_data_p_t;

struct UF_SC_EDGE_boundary_data_s
{
    int         num_faces_n_features;
    tag_t      *faces_n_features;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_boundary_data_s
               UF_SC_EDGE_boundary_data_t, *UF_SC_EDGE_boundary_data_p_t;

struct UF_SC_EDGE_intersect_data_s
{
    int         num_faces_n_features1;
    tag_t      *faces_n_features1;
    int         num_faces_n_features2;
    tag_t      *faces_n_features2;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_intersect_data_s
               UF_SC_EDGE_intersect_data_t, *UF_SC_EDGE_intersect_data_p_t;

struct UF_SC_EDGE_vertex_data_s
{
    tag_t       start_edge;            /* the seed edge */
    logical     from_start;            /* =true, start vertex of the start_edge,
                                          =false, end vertex of the start_edge */
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_vertex_data_s
               UF_SC_EDGE_vertex_data_t, *UF_SC_EDGE_vertex_data_p_t;

struct UF_SC_EDGE_vertex_tangent_data_s
{
    tag_t       start_edge;            /* the seed edge */
    logical     from_start;            /* =true, start vertex of the start_edge,
                                          =false, end vertex of the start_edge */
    double      angle_tol;             /* angle tolerance for tangent edges */
    logical     same_convexity;        /* will only find tangnet edges that has the same convexity if true */
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_EDGE_vertex_tangent_data_s
               UF_SC_EDGE_vertex_tangent_data_t, *UF_SC_EDGE_vertex_tangent_data_p_t;

struct UF_SC_FACE_dumb_data_s
{
    int         num_faces;
    tag_t      *faces;
};
typedef struct UF_SC_FACE_dumb_data_s
               UF_SC_FACE_dumb_data_t, *UF_SC_FACE_dumb_data_p_t;

/* For the region of faces, we have two ways to allow you input boundary faces.
   You can either input the individual boundary faces in bndary_faces array or
   you can input boundary faces as rules in bndary_face_data array.

   You must input one type of boudnary faces.

   The input rule data for boundary faces have to be one of the
   UF_SC_FACE_*_data_p_t types.

   If bndary_faces is not NULL, bndary_face_data array will be ignored. The
   bndary_face_data will take effect only if num_bndary_faces = 0 and
   bndary_faces = NULL;
*/
struct UF_SC_FACE_region_data_s
{
    tag_t                 seed_face;
    int                   num_bndary_faces;
    tag_t                *bndary_faces;
    int                   n_bndary_face_data;
    int                  *bndary_face_types;  /* array of int to input rule types */
    UF_SC_input_data_p_t  bndary_face_data;   /* array of input data */
    int                   n_negated_entities;
    tag_t                *negated_entities;
};
typedef struct UF_SC_FACE_region_data_s
               UF_SC_FACE_region_data_t, *UF_SC_FACE_region_data_p_t;

/* For the region of faces, we have two ways to allow you input boundary faces.
   You can either input the individual boundary faces in bndary_faces array or
   you can input boundary faces as rules in bndary_face_data array.

   The boundary data is optional. You can leave both type of boundary data to
   be NULL.

   The input rule data for boundary faces have to be one of the
   UF_SC_FACE_*_data_p_t types.

   If bndary_faces is not NULL, bndary_face_data array will be ignored. The
   bndary_face_data will take effect only if num_bndary_faces = 0 and
   bndary_faces = NULL;
*/
struct UF_SC_FACE_tangent_data_s
{
    tag_t                 seed_face;
    int                   num_bndary_faces;
    tag_t                *bndary_faces;          /* This is optional */
    double                angle_tol;             /* Angle tolerance for tangent faces */
    int                   n_bndary_face_data;
    int                  *bndary_face_types;  /* array of int to input rule types */
    UF_SC_input_data_p_t  bndary_face_data;   /* array of input data */
    int                   n_negated_entities;
    tag_t                *negated_entities;
};
typedef struct UF_SC_FACE_tangent_data_s
               UF_SC_FACE_tangent_data_t, *UF_SC_FACE_tangent_data_p_t;

struct UF_SC_FACE_body_data_s
{
    tag_t      body;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_FACE_body_data_s
               UF_SC_FACE_body_data_t, *UF_SC_FACE_body_data_p_t;

struct UF_SC_FACE_feature_data_s
{
    int         num_features;
    tag_t      *features;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_FACE_feature_data_s
               UF_SC_FACE_feature_data_t, *UF_SC_FACE_feature_data_p_t;

struct UF_SC_FACE_adjacent_data_s
{
    tag_t seed;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_FACE_adjacent_data_s
               UF_SC_FACE_adjacent_data_t, *UF_SC_FACE_adjacent_data_p_t;

struct UF_SC_FACE_connected_blend_data_s
{
    tag_t       seed;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_FACE_connected_blend_data_s
               UF_SC_FACE_connected_blend_data_t, *UF_SC_FACE_connected_blend_data_p_t;

struct UF_SC_FACE_all_blend_data_s
{
    tag_t       body;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_FACE_all_blend_data_s
               UF_SC_FACE_all_blend_data_t, *UF_SC_FACE_all_blend_data_p_t;

struct UF_SC_FACE_rib_faces_data_s
{
    tag_t       seed;
    int         n_negated_entities;
    tag_t      *negated_entities;
    logical     includeBoundaryBlends;
    logical     traverseInteriorLoops;
};
typedef struct UF_SC_FACE_rib_faces_data_s UF_SC_FACE_rib_faces_data_t, *UF_SC_FACE_rib_faces_data_p_t;

struct UF_SC_FACE_merged_rib_faces_data_s
{
    tag_t       seed;
    int         n_negated_entities;
    tag_t      *negated_entities;
    logical     includeBoundaryBlends;
    void        *options;
};
typedef struct UF_SC_FACE_merged_rib_faces_data_s UF_SC_FACE_merged_rib_faces_data_t, *UF_SC_FACE_merged_rib_faces_data_p_t;

struct UF_SC_FACE_slot_faces_data_s
{
    tag_t       seed;
    int         n_negated_entities;
    tag_t      *negated_entities;
    logical     includeBoundaryBlends;
    logical     traverseInteriorLoops;
};
typedef struct UF_SC_FACE_slot_faces_data_s
               UF_SC_FACE_slot_faces_data_t, *UF_SC_FACE_slot_faces_data_p_t;

struct UF_SC_FACE_boss_pocket_faces_data_s
{
    tag_t       seed;
    int         n_negated_entities;
    tag_t      *negated_entities;
    logical     includeBoundaryBlends;
};
typedef struct UF_SC_FACE_boss_pocket_faces_data_s
               UF_SC_FACE_boss_pocket_faces_data_t, *UF_SC_FACE_boss_pocket_faces_data_p_t;

struct UF_SC_CURVE_dumb_data_s
{
    int         num_curves;
    tag_t      *curves;
    logical     allowRefCurves;
};
typedef struct UF_SC_CURVE_dumb_data_s
               UF_SC_CURVE_dumb_data_t, *UF_SC_CURVE_dumb_data_p_t;

struct UF_SC_CURVE_feature_data_s
{
    int         num_features;
    tag_t      *features;
    int         n_negated_entities;
    tag_t      *negated_entities;
    logical     allowRefCurves;
};
typedef struct UF_SC_CURVE_feature_data_s
               UF_SC_CURVE_feature_data_t, *UF_SC_CURVE_feature_data_p_t;

struct UF_SC_CURVE_feat_chain_data_s
{
    int         num_features;
    tag_t      *features;
    tag_t       seed_curve;
    tag_t       end_curve;              /* it is optional */
    logical     from_seed_start;        /* whether the chain starts from the start
                                           point of the seed curve */
    double      gap_tol;
    int         n_negated_entities;
    tag_t      *negated_entities;
    logical     allowRefCurves;
};
typedef struct UF_SC_CURVE_feat_chain_data_s
               UF_SC_CURVE_feat_chain_data_t, *UF_SC_CURVE_feat_chain_data_p_t;

struct UF_SC_CURVE_feat_tangent_data_s
{
    int         num_features;
    tag_t      *features;
    tag_t       seed_curve;
    tag_t       end_curve;             /* it is optional */
    logical     from_seed_start;       /* whether the tangent starts from the start
                                          point of the start curve if end curve is provided*/
    double      gap_angle_tols[2];
    int         n_negated_entities;
    tag_t      *negated_entities;
    logical     allowRefCurves;
};
typedef struct UF_SC_CURVE_feat_tangent_data_s
               UF_SC_CURVE_feat_tangent_data_t, *UF_SC_CURVE_feat_tangent_data_p_t;

struct UF_SC_CURVE_follow_fillet_data_s
{
    int         num_features;
    tag_t      *features;
    int         num_bodies;
    tag_t      *bodies;
    int         num_dumb_curves;
    tag_t      *dumb_curves;
    tag_t       seed_wireframe;
    tag_t       end_wireframe;              /* it is optional */
    logical     from_seed_start;        /* whether the chain starts from the start
                                           point of the seed curve */
    logical     tangent;
    double      seed_point[3];
    double      gap_angle_tols[2];
    logical     allowRefCurves;
    /*Do NOT add negated_entities information for Follow Fillet*/
};
typedef struct UF_SC_CURVE_follow_fillet_data_s
               UF_SC_CURVE_follow_fillet_data_t, *UF_SC_CURVE_follow_fillet_data_p_t;

struct UF_SC_CURVE_region_boundary_data_s
{
    tag_t       seed_obj;
    int         num_curves;
    tag_t       *curves;
    double      seed_point[3];    /* This is the abs pick point on the face */
    double      distance_tol;
    logical     allowRefCurves;
};

typedef struct UF_SC_CURVE_region_boundary_data_s
               UF_SC_CURVE_region_boundary_data_t, *UF_SC_CURVE_region_boundary_data_p_t;


struct UF_SC_CURVE_feature_points_data_s
{
    int         num_features;
    tag_t      *features;
    int         n_negated_entities;
    tag_t      *negated_entities;
};
typedef struct UF_SC_CURVE_feature_points_data_s
               UF_SC_CURVE_feature_points_data_t, *UF_SC_CURVE_feature_points_data_p_t;

struct UF_SC_BODY_dumb_data_s
{
    int         num_bodies;
    tag_t      *bodies;
};
typedef struct UF_SC_BODY_dumb_data_s
               UF_SC_BODY_dumb_data_t, *UF_SC_BODY_dumb_data_p_t;

union UF_SC_input_data_s
{
    UF_SC_EDGE_dumb_data_t              edge_dumb_input;
    UF_SC_EDGE_chain_data_t             edge_chain_input;
    UF_SC_EDGE_tangent_data_t           edge_tangent_input;
    UF_SC_EDGE_mseedtan_data_t          edge_mseedtan_input;
    UF_SC_EDGE_face_data_t              edge_face_input;
    UF_SC_EDGE_body_data_t              edge_body_input;
    UF_SC_EDGE_feature_data_t           edge_feature_input;
    UF_SC_EDGE_shbndary_data_t          edge_shbndary_input;
    UF_SC_EDGE_boundary_data_t          edge_boundary_input;
    UF_SC_EDGE_intersect_data_t         edge_intersect_input;
    UF_SC_EDGE_vertex_data_t            edge_vertex_input;
    UF_SC_EDGE_vertex_tangent_data_t    edge_vertex_tangent_input;
    UF_SC_FACE_dumb_data_t              face_dumb_input;
    UF_SC_FACE_region_data_t            face_region_input;
    UF_SC_FACE_tangent_data_t           face_tangent_input;
    UF_SC_FACE_body_data_t              face_body_input;
    UF_SC_FACE_feature_data_t           face_feature_input;
    UF_SC_FACE_adjacent_data_t          face_adjacent_input;
    UF_SC_FACE_connected_blend_data_t   face_connected_blend_input;
    UF_SC_FACE_all_blend_data_t         face_all_blend_input;
    UF_SC_FACE_rib_faces_data_t         face_rib_faces_input;
    UF_SC_FACE_slot_faces_data_t        face_slot_faces_input;
    UF_SC_FACE_boss_pocket_faces_data_t       face_boss_pocket_faces_input;
    UF_SC_FACE_merged_rib_faces_data_t         face_merged_rib_faces_input;
    UF_SC_CURVE_dumb_data_t             curve_dumb_input;
    UF_SC_CURVE_feature_data_t          curve_feature_input;
    UF_SC_CURVE_feat_chain_data_t       curve_feat_chain_input;
    UF_SC_CURVE_feat_tangent_data_t     curve_feat_tangent_input;
    UF_SC_CURVE_follow_fillet_data_t    curve_follow_fillet_input;
    UF_SC_CURVE_feature_points_data_t   curve_feature_points_input;
    UF_SC_BODY_dumb_data_t              body_dumb_input;
    UF_SC_CURVE_region_boundary_data_t  curve_region_boundary_input; 
};
typedef union UF_SC_input_data_s
              UF_SC_input_data_t;

struct UF_SC_section_output_data_s
{
    tag_t             output_object ; /* The tag of the object that constructs the section */
    tag_t             start_connected_object ; /* The object the connected to the above objects,
                                                  at the start_point */
    double            start_point[3] ;
    tag_t             end_connected_object ;   /* The other object the connected to the above objects,
                                                  at the end_point */
    double            end_point[3] ;
};
typedef struct UF_SC_section_output_data_s
               UF_SC_section_output_data_t , * UF_SC_section_output_data_p_t ;

struct UF_SC_section_data_s
{
    int                            n_rules ;
    int                          * rule_types ;    /* <len:n_rules> */
    UF_SC_input_data_t           * rules ;         /* <len:n_rules> */
    double                         chaining_tolerance ;
    double                         distance_tolerance ;
    double                         angle_tolerance ;
    tag_t                          start_connector ;        /* for stop at intersection: define the   */
    tag_t                          end_connector ;          /* for stop at intersection */
    double                         help_point[3] ;          /* for stop at intersection */
    double                         intersection_point_1[3] ;/* for stop at intersection */
    double                         intersection_point_2[3] ;/* for stop at intersection */
    int                            n_output_objects ;       /* for UF_MODL_ask_section,
                                                               the ouput objects, their start and
                                                               end collectors, and the endpoints
                                                               of the resulting curves */
    UF_SC_section_output_data_t  * output_objects ;   /* <len:n_output_objects> */
};
typedef struct UF_SC_section_data_s
               UF_SC_section_data_t , * UF_SC_section_data_p_t ;

#ifdef __cplusplus
}
#endif

#endif /* UF_SC_TYPES_H_INCLUDED */