/*****************************************************************************
             Copyright (c) 2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API enum types & data structures for NX SheetMetal features.
*****************************************************************************/

#ifndef UF_NXSM_TYPES_H_INCLUDED
#define UF_NXSM_TYPES_H_INCLUDED


/*==========================================================================

  ==========================================================================*/

#include <uf_defs.h>
#include <libufun_exports.h>
#include <uf_modl_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/* [HELPSTRING][HELPCONTEXT] */
#define IG_CURVESET_SEPERATOR   IG_CURVESET_SEPARATOR
#define IG_SIDE_INFOSET_SEPERATOR   IG_SIDE_INFOSET_SEPARATOR
/*
 *This is a common enum that comprises of values to be used for various features.
 *Each feature data structure will enumerate valid values that can be used for that feature parameter.
 */
enum UF_NXSM_FEATURE_PROPERTY_CONSTANTS
{
        IG_NULL_CONSTANT  = 0,
        IG_LEFT  = 1,
        IG_RIGHT = 2,
        IG_SYMMETRIC     = 3,
        IG_INSIDE        = 4,
        IG_OUTSIDE       = 5,
        IG_BOTH  = 6,
        IG_NORMAL_SIDEDUMMY       = 7,
        IG_REVERSE_NORMAL_SIDEDUMMY        = 8,
        IG_EXTEND        = 9,
        IG_NOEXTEND      = 10,
        IG_THKINPROFILEPLANE     = 11,
        IG_THK_NORMAL_TO_PROFILE_PLANE       = 12,
        IG_FINITE        = 13,
        IG_TONEXT        = 14,
        IG_TO_END_OF_EDGE   = 14,
        IG_FROM_TO        = 15,
        IG_THROUGH_ALL    = 16,
        IG_THREE_HUNDRED_AND_SIXTY  = 17,
        IG_PARALLEL_DUMMY = 18,
        IG_ANGULAR_DUMMY  = 19,
        IG_NORMAL        = 20,
        IG_THROUGH_AXIS   = 21,
        IG_SINGLE_EDGE    = 22,
        IG_MULTIPLE_EDGES = 23,
        IG_EDGES_BY_LOOP   = 24,
        IG_EDGES_BY_VERTEX = 25,
        IG_ALL   = 26,
        IG_CONCAVE       = 27,
        IG_CONVEX        = 28,
        IG_START = 29,
        IG_END   = 30,
        IG_LINEAR        = 31,
        IG_RADIAL        = 32,
        IG_REGULAR_HOLE   = 33,
        IG_COUNTER_BORE_HOLE       = 34,
        IG_COUNTER_SINK_HOLE       = 35,
        IG_COUNTER_DRILL_HOLE      = 36,
        IG_TAPPED_HOLE    = 37,
        IG_TAPERED_HOLE   = 38,
        IG_CONST_RADIUS_ROUND      = 39,
        IG_VAR_RADIUS_ROUND        = 40,
        IG_CHAMFER_45DEG_SETBACK   = 41,
        IG_CHAMFER_ANGLE_SETBACK   = 42,
        IG_CHAMFER2_SETBACKS      = 43,
        IG_NONE  = 44,
        IG_TAPER_BY_ANGLE  = 45,
        IG_TAPER_BY_RATIO  = 46,
        IG_CLOSED        = 47,
        IG_PROFILE_BASED_CROSSSECTION      = 48,
        IG_EDGE_BASED_CROSSSECTION = 49,
        IG_TANGENT       = 50,
        IG_RECTANGULAR_BEND_RELIEF = 51,
        IG_FILLET_BEND_RELIEF      = 52,
        IG_RIP_BEND_RELIEF = 53,
        IG_BEND_ONLY_CORNER_RELIEF  = 54,
        IG_BEND_AND_FACE_CORNER_RELIEF       = 55,
        IG_RIP_CORNER_RELIEF       = 56,
        IG_NFTYPE        = 57,
        IG_EQUATION_TYPE  = 58,
        IG_PATTERN_MIRROR = 59,
        IG_PATTERN_RECTANGULAR    = 60,
        IG_PATTERN_CIRCULAR       = 61,
        IG_PATTERN_USER_DEFINED    = 62,
        IG_FROM_REFERENCE_END      = 64,
        IG_FROM_NONREFERENCE_END   = 65,
        IG_RND_ROLL_ACROSS_TANGENT_EDGES_ON   = 66,
        IG_RND_ROLL_ACROSS_TANGENT_EDGES_OFF  = 67,
        IG_RND_CAP_ACROSS_SHARP_EDGES        = 68,
        IG_RND_ROLL_ACROSS_SHARP_EDGES       = 69,
        IG_RND_ROLL_ALONG_BLEND_EDGES_ON      = 70,
        IG_RND_ROLL_ALONG_BLEND_EDGES_OFF     = 71,
        IG_TO_KEY_POINT    = 72,
        IG_FLATTEN       = 73,
        IG_AS_CONSTRUCTION        = 74,
        IG_OFFSET        = 75,
        IG_MITRE_PARALLEL_TO_THICKNESS      = 76,
        IG_MITRE_NORMAL_TO_THICKNESS        = 77,
        IG_MITRE_BY_DIST   = 78,
        IG_MITRE_BY_ANGLE  = 79,
        IG_MITRE_REGULAR_CUT       = 80,
        IG_MITRE_MANUFACTURING_CUT = 81,
        IG_PROJECT_OPTION_PROJECT  = 82,
        IG_PROJECT_OPTION_WRAP     = 83,
        IG_LIP   = 84,
        IG_GROOVE        = 85,
        IG_PARTING_FROM_PLANE      = 86,
        IG_PARTING_FROM_SURFACE    = 87,
        IG_PARTING_FROM_EDGE       = 88,
        IG_PARTING_FROM_CURVE      = 89,
        IG_SPLIT_DRAFT    = 90,
        IG_SPLIT_ANGLE1_RIGHT      = 91,
        IG_SPLIT_ANGLE1_LEFT       = 92,
        IG_LOUVERFORMEDENDTYPE   = 93,
        IG_LOUVERLANCEDENDTYPE   = 94,
        IG_LOUVERROUND   = 95,
        IG_LOUVERROUNDNONE       = 96,
        IG_INSIDE_DIMENSION       = 97,
        IG_OUTSIDE_DIMENSION      = 98,
        IG_FULL  = 99,
        IG_BEND  = 100,
        IG_ADD_ROUND      = 101,
        IG_NO_ROUND       = 102,
        IG_CLOSE_FACES    = 103,
        IG_OVERLAP_FACES  = 104,
        IG_TREATMENT_OFF  = 105,
        IG_TREATMENT_INTERSECT    = 106,
        IG_TREATMENT_CIRCLE_CUTOUT = 107,
        IG_STEP_DRAFT     = 108,
        IG_SHOW_BOUNDARIES        = 109,
        IG_REMOVE_BOUNDARIES      = 110,
        IG_CORNER_ROUND   = 111,
        IG_NO_CORNER_ROUND = 112,
        IG_NATURAL       = 113,
        IG_PERIODIC      = 114,
        IG_ROUND_ALL_VERTEX_SETBACK = 115,
        IG_ROUND_SINGLE_VERTEX_SETBACK      = 116,
        IG_ROUND_VERTEX_EDGE_SETBACK        = 117,
        IG_ROUND_SETBACK_IS_ABSOLUTE        = 118,
        IG_ROUND_SETBACK_IS_RELATIVE        = 119,
        IG_CIRCULAR      = 120,
        IG_USHAPED       = 121,
        IG_VSHAPED       = 122,
        IG_PUNCHED_END    = 123,
        IG_LANCED_END     = 124,
        IG_FORMED_END     = 125,
        IG_SWEEP_ALIGN_PARALLEL    = 126,
        IG_SWEEP_ALIGN_NORMAL      = 127,
        IG_ROUND_START_VERTEX_EDGE_SETBACK   = 128,
        IG_ROUND_END_VERTEX_EDGE_SETBACK     = 129,
        IG_SUBTRACT      = 130,
        IG_UNITE = 131,
        IG_INTERSECT     = 132,
        IG_CONTINUOUS    = 133,
        IG_FLANGE_FULLEDGE        = 134,
        IG_FLANGE_CENTER_OF_EDGE    = 135,
        IG_FLANGE_START_ON_END_EDGE  = 136,
        IG_FLANGE_END_ON_END_EDGE    = 137,
        IG_FLANGE_START_FROM_END_EDGE        = 138,
        IG_FLANGE_END_FROM_END_EDGE  = 139,
        IG_FLANGE_FROM_BOTH_ENDS_OF_EDGE      = 140,
        IG_FLANGE_OFFSET  = 141,
        IG_CHAINED_CORNER_RELIEF   = 142,
        IG_TANGENT_INTERIOR       = 143,
        IG_PARALLEL_TO_PLANE       = 144,
        IG_VBOTTOM_DIM_TO_FLAT      = 145,
        IG_VBOTTOM_DIM_TO_V = 146,
        IG_TAPER_DIM_AT_TOP = 147,
        IG_TAPER_DIM_AT_BOTTOM      = 148,
        IG_COUNTER_BORE_PROFILE_IS_AT_TOP     = 149,
        IG_COUNTER_BORE_PROFILE_IS_AT_BOTTOM  = 150,
        IG_TAPER_BY_RL_RATIO        = 151,
        IG_RNDMITERAT_CORNER      = 152,
        IG_RND_ROLL_AROUND_CORNER   = 153,
        IG_RND_PRESERVE_TOPOLOGYON = 154,
        IG_RND_PRESERVE_TOPOLOGY_OFF        = 155,
        IG_STEP_DRAFT_PERPENDICULAR        = 156,
        IG_EXTEND_BEND_RELIEF      = 157,
        IG_EQUAL_OFFSET   = 158,
        IG_UNEQUAL_OFFSET = 159,
        IG_THICKNESS     = 160,
        IG_FACES_TOUCHING_CURVES_ONLY       = 161,
        IG_CURVESET_SEPARATOR     = 162,
        IG_SIDE_INFOSET_SEPARATOR  = 163,
        IG_REGULAR_THREAD = 164,
        IG_STRAIGHT_PIPETHREAD    = 165,
        IG_TAPERED_PIPETHREAD     = 166,
        IG_REMOVE_INTERNAL_BOUNDARIES      = 167,
        IG_REMOVE_EXTERNAL_BOUNDARIES      = 168,
        IG_DELETE_FACEHEAL        = 169,
        IG_ENDCAPS       = 170,
        IG_CURVATURE_CONTINUOUS   = 171,
        IG_NONSYMMETRIC  = 172,
        IG_TREATMENT_DRAFT        = 173,
        IG_TREATMENT_CROWN        = 174,
        IG_CLOSE_CORNER_NONE       = 175,
        IG_CLOSE_CORNER_OPEN       = 176,
        IG_CLOSE_CORNER_CLOSED     = 177,
        IG_CLOSE_CORNER_CIRCLE_CUTOUT       = 178,
        IG_PATTERN_ALONG_CURVE     = 179,
        IG_PATTERN_MOUNTING_BOSS   = 180,
        IG_SM_CLEARANCE_CUTOUT     = 181,
        IG_SM_MIDPLANE_CUTOUT      = 182,
        IG_TREATMENT_U_CUTOUT      = 220,
        IG_TREATMENT_V_CUTOUT      = 221,
        IG_TREATMENT_RECTANGULAR_CUTOUT = 222
    
};
typedef enum UF_NXSM_FEATURE_PROPERTY_CONSTANTS
             UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t;

/*
 *NXSM - SECONDARY TAB FEATURE
 */

/* Data structure for Secondary Tab */
struct UF_NXSM_sec_tab_data_s
{

    tag_t sketch_profile;                         /* sketch tag or section tag of sketch.
                                                    You can either pass sketch tag or create a 
                                                    section for sketch, pass the tag of section.
                                                  * NULL_TAG (default) */

    tag_t placement_face;                         /* Placement face of the base tab for creating secondary tab */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t material_side;
                                                  /* Sketch side on which material will be added
                                                   * IG_LEFT - default
                                                   * IG_RIGHT  */                                                           

};
typedef struct UF_NXSM_sec_tab_data_s UF_NXSM_sec_tab_data_t, *UF_NXSM_sec_tab_data_p_t;


/* Data structure for bend option */
struct UF_NXSM_bend_option_s
{
    char bend_radius[ UF_MAX_EXP_BUFSIZE ];   /* Bend radius */

    logical is_bend_radius_global;         /* flag to use default value. 
                                              TRUE  - 0.1 in /3.0 mm (default)
                                              FALSE - To use user defined bend radius make it FALSE  */

    logical bend_relief;                   /* Bend relief require or not 
                                              TRUE - bend relief require
                                              FALSE - bend relief not require (default) */

    logical extend_bend_relief;            /* flag to to extend bend relief 
                                              TRUE - Extend bend relief to source body
                                              FALSE - default */ 

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t bend_relief_type; 
                                            /* It provides clearance between the bend and the Source Face 
                                             * IG_RECTANGULAR_BEND_RELIEF - for square shape relief(default), 
                                             * IG_FILLET_BEND_RELIEF - for round shape relief 
                                             * IG_RIP_BEND_RELIEF - bend relief not require*/

    char bend_relief_depth[ UF_MAX_EXP_BUFSIZE ]; /* Depth of bend relief */

    logical bend_relief_depth_global;         /* flag to use global value. 
                                               * TRUE - 0.1 in /3.0 mm (default) 
                                               * FALSE - To use user defined bend relief width make it FALSE */

    char bend_relief_width[ UF_MAX_EXP_BUFSIZE ];  /* Width of bend relief */

    logical bend_relief_width_global;         /* flag to use global value. 
                                               * TRUE - 0.1 in /3.0 mm (default) 
                                               * FALSE - To use user defined bend relief width make it FALSE */
    
    logical corner_relief;                    /* Corner relief require or not 
                                               * TRUE - bend relief require
                                               * FALSE - bend relief not require (default) */
    
   UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t corner_relief_type; 
                                              /* Corner relief is used to avoid deformation and tear of 
                                                 material during bending process.
                                               * IG_RIP_CORNER_RELIEF  - default,                                                  
                                               * IG_BEND_ONLY_CORNER_RELIEF - relief apply to bend only ,
                                               * IG_BEND_AND_FACE_CORNER_RELIEF - relief apply to bend and face,
                                               * IG_CHAINED_CORNER_RELIEF  - relief apply to bend and chain of faces */  

   char neutral_factor[ UF_MAX_EXP_BUFSIZE ];    /* default value - 0.33333 */

   logical neutral_factor_global;             /* flag to use global value. 
                                               * TRUE - Use default value(default) 
                                               * FALSE - To use user defined neutral factor make it FALSE */

};
typedef struct UF_NXSM_bend_option_s UF_NXSM_bend_option_t, *UF_NXSM_bend_option_p_t;



/*
 *NXSM - CLOSED CORNER FEATURE
 */

/* Main Data structure for closed corner */
struct UF_NXSM_closed_corner_data_s
{
    tag_t bend_faces[2];    /*for creating closed corner first time send in two valid bend faces from here.
                              subsequently, send additional valid bend faces while editing so as to add more 
                              corners to be closed.  */

    int n_edges;            /* Actual number of edges in the array "parent_edges".*/

    tag_t* parent_edges;   /* <OF,len:n_edges> array of parent edges
                           NULL - at the time of creating closed corner
                           During "edit", the "ask_feature" method will return the current array of parent edges
                           User can remove any edges from that array if he so desires.
                           Update the "n_edges" variable accordingly to reflect actual number of edges in this array. */
    
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t treatment_type;
                                        /* Type of closed corner treatment - 
                                           IG_TREATMENT_OFF - default
                                           IG_TREATMENT_INTERSECT - intersection at the corner
                                           IG_TREATMENT_CIRCLE_CUTOUT - circular cutout at the corner
                                         */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t closure_type; 
                                        /* Type of closure -
                                           IG_TREATMENT_OFF - default
                                           IG_CLOSE_FACES - close the corner faces
                                           IG_OVERLAP_FACES - overlap the corner faces */
                                        
    const char* treatment_dia;          /* diameter value for the "IG_TREATMENT_CIRCLE_CUTOUT" 
                                           treatment for closed corner */

    const char* overlap_ratio;          /* ratio of overlap for the overlapping faces - 
                                           valid values range from 0.0 to 1.0    */
                                   
    const char* corner_gap;             /* gap in between the closing faces -
                                           valid values range from 0.0 upto the material 
                                           thickness of the body. */
                                   
};
typedef struct UF_NXSM_closed_corner_data_s UF_NXSM_closed_corner_data_t, *UF_NXSM_closed_corner_data_p_t;

/*
 *NXSM - FLANGE FEATURE
 */

/*Enum for flange width option*/
typedef enum
{
    OPTION_NOT_SET = -101,
    CUSTOM_WIDTH_TYPE = -1, /* ==> user has edited the flange sketch manually so it is no longer a pre-configured type */
    FULL_WIDTH_TYPE = 0,
    CENTERED_TYPE,
    AT_END_TYPE,
    FROM_BOTH_ENDS_TYPE,
    FROM_END_TYPE
} UF_NXSM_FLANGE_WIDTH_OPTION_e_t;

/*Data structure for flange sketch*/
struct UF_NXSM_flange_sketch_data_s
{
    UF_NXSM_FLANGE_WIDTH_OPTION_e_t width_option;   /* choose appropriate width_option from UF_NXSM_FLANGE_WIDTH_OPTION_e_t*/
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t dim_option;   /* Indicates whether to measure the dimension from the inside edge or outside edge of the flange.
                                                            valid values -
                                                            IG_OUTSIDE_DIMENSION - default
                                                            IG_INSIDE_DIMENSION
                                                          */
    const char* length;   /* length of the flange*/
    const char* width;    /* width of the flange*/
    double snap_point[3];   /* for AT_END_TYPE / FROM_END_TYPE width option.
                               User can use "UF_MODL_ask_edge_verts" routine
                               to get the end points of the parent edge of flange & send the desired point co-ords to the snap_point*/
    const char* dist_from_end;    /* distance from the end at which the flange would start - FROM_END_TYPE width option.*/
    const char* dist_from_left_end;   /* distance from left end of the edge - FROM_BOTH_ENDS_TYPE width option.*/
    const char* dist_from_right_end;  /* distance from the right end of the edge - FROM_BOTH_ENDS_TYPE width option.*/
    UF_NXSM_FLANGE_WIDTH_OPTION_e_t prev_width_option;      /*width_option value with which the feature was created earlier.
                                                             *"ask_feature" method populates this parameter.
                                                             */
};
typedef struct UF_NXSM_flange_sketch_data_s UF_NXSM_flange_sketch_data_t, *UF_NXSM_flange_sketch_data_p_t;

/* Main Data structure for flange */
struct UF_NXSM_flange_data_s
{
    tag_t parent_edge;    /* tag of the edge on which flange is to be placed*/
    tag_t sketch_tag;     /* sketch of the flange - send a NULL_TAG for create.
                             flange will create its sketch internally based on various calculations & input sketch data.
                             User can query the feature & get the sketch tag for further modifications to the sketch if so desired.
                          */
    const char* angle;    /* flange angle
                             should have value between 0 to 180 degrees.
                           */
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t material_side;    /* Side on which material will be added with respect to the mould line
                                                                valid values - 
                                                                IG_LEFT - default
                                                                IG_RIGHT
                                                                IG_EXTEND
                                                              */
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t br_type;    /* bend relief type
                                                          valid values -
                                                          IG_RECTANGULAR_BEND_RELIEF - default
                                                          IG_FILLET_BEND_RELIEF     
                                                          IG_BEND_ONLY_CORNER_RELIEF  
                                                          IG_BEND_AND_FACE_CORNER_RELIEF      
                                                          IG_RIP_CORNER_RELIEF     
                                                        */
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t cr_type;    /* corner relief type 
                                                          valid values - 
                                                          IG_RIP_CORNER_RELIEF - default
                                                          IG_BEND_ONLY_CORNER_RELIEF  
                                                          IG_BEND_AND_FACE_CORNER_RELIEF      
                                                        */
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t off_type;       /* offset type.
                                                              valid values -
                                                              IG_NONE - default
                                                              IG_LEFT
                                                              IG_RIGHT
                                                            */
    const char* bend_rad;    /* bend radius for the flange */
    logical use_global_radius_value;   /* false - default
                                          true - if user wants to link his flange to global bend radius value
                                        */
    const char* br_width;   /* bend relief width*/
    logical use_global_br_width_value;   /* false - default
                                            true - if user wants to link his flange to global bend radius value
                                          */
    const char* br_length;  /* bend relief length*/
    logical use_global_br_length_value;   /* false - default
                                             true - if user wants to link his flange to global bend radius value
                                           */
    const char* off_val;    /*offset value*/
    const char* n_factor;       /* neutral factor value */
    logical use_global_nfactor_value;   /* false - default
                                           true - if user wants to link his flange to global bend radius value
                                         */
    logical extend_bend_relief;     /* false - default
                                       true - If user wants bend relief to be extended
                                     */
};
typedef struct UF_NXSM_flange_data_s UF_NXSM_flange_data_t, *UF_NXSM_flange_data_p_t;


/******************************************************************************
Data structure for Mitre cut

Mitre cut is essentially an end treatment to the contour flange feature, which shall 
prevent merging/interference with the existing or newly placed features in sheet metal.  
Sometimes without mitreing we would end up with merging the faces of the adjoining 
contour flange features.
The mitre cut is optional, and can be done in two ways.  Either ?Normal to thickness face?
or ?Normal to source face' which is same as 'Parallel to thickness face?.  
Mitreing is provided at the start or end of contour flange or at both start and end of 
contour flange.
******************************************************************************/
struct UF_NXSM_mitre_cflange_data_s
{
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t   mitre_position; 
                                                /* It indicates the cut location if require, 
                                                  IG_NONE -  no mitre(default)  , 
                                                  IG_START - mitre at start,
                                                  IG_RIGHT - mitre at end,   
                                                 */
                                                                                      
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t  mitre_type_at_start;
                                                 /* Type of cut at the start of contour flange
                                                    IG_MITRE_NORMAL_TO_THICKNESS- normal to thickness face(default) , 
                                                    IG_MITRE_PARALLEL_TO_THICKNESS- normal to source face 
                                                  */ 
                                                          

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_type_at_end;  
                                                 /* Type of cut at the end of contour flange
                                                    IG_MITRE_PARALLEL_TO_THICKNESS- normal to thickness face(default),  
                                                    IG_MITRE_NORMAL_TO_THICKNESS- normal to source face 
                                                  */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_side_at_start;
                                                  /* mitre plane orientation at start of contour flange 
                                                     IG_INSIDE - for cut(default),
                                                     IG_OUTSIDE - for grow       
                                                   */       

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_side_at_end; 
                                                  /* mitre plane orientation at end of contour flange 
                                                     IG_INSIDE - for cut(default), 
                                                     IG_OUTSIDE - for grow      
                                                   */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_by_dist_or_angle_at_start; 
                                                  /* Specify mitre cut by distance or angle 
                                                     IG_MITRE_BY_ANGLE -mitre location by angle(default) 
                                                   */
                                                                           
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_by_dist_or_angle_at_end; 
                                                   /* Specify mitre cut by distance or angle 
                                                      IG_MITRE_BY_ANGLE -mitre location by angle(default) 
                                                    */

    char mitre_angle_at_start[ UF_MAX_EXP_BUFSIZE ];  /* Angle in degrees at the start of contour flange */
  
    char mitre_angle_at_end[ UF_MAX_EXP_BUFSIZE ];    /* Angle in degrees at the end of contour flange */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t  mitre_cut_type;  
                                                   /* Type of cut  
                                                      IG_MITRE_REGULAR_CUT - Regular or Clean cut (default),
                                                      IG_MITRE_MANUFACTURING_CUT - manufacturing cut 
                                                    */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t close_corner_type;   
                                                    /* Type of corner
                                                       IG_CLOSE_CORNER_NONE - default,
                                                       IG_CLOSE_CORNER_OPEN - corner open,
                                                       IG_CLOSE_CORNER_CLOSED - corner closed,
                                                       IG_CLOSE_CORNER_CIRCLE_CUTOUT - circular cutout at the corner 
                                                     */

    char close_corner_dia[ UF_MAX_EXP_BUFSIZE ];       /* Diameter of close corner*/ 

};
typedef struct UF_NXSM_mitre_cflange_data_s UF_NXSM_mitre_cflange_data_t, *UF_NXSM_mitre_cflange_data_p_t;


/*
 *NXSM - SECONDARY CONTOUR FLANGE FEATURE
 */

/* Data structure for Secondary contour flange  */
struct UF_NXSM_sec_cflange_data_s
{
    tag_t sketch_section;                          /* Tag of section object created from sketch.
                                                      NULL_TAG (default) */
    
    tag_t ref_edge;                                /* Tag of edge to which flange will be connected */

    tag_t section_edges;                           /* Section tag of edges 
                                                      If NULL_TAG, it is secondary contour flange otherwise chain
                                                      contour flange */  

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t  profile_ref_end; 
                                                   /* It represents the end of the edge where sketch 
                                                        profile is created
                                                      IG_INSIDE - Within the edge (default) */  

    char projection_dist[ UF_MAX_EXP_BUFSIZE ];       /* Distance through which sketch is projected */
    
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t  projection_side;
                                                   /* Whether projection is in the normal direction or opposite to 
                                                      the normal direction of datum plane on which profile is generated 
                                                      IG_LEFT - to normal direction (default)
                                                      IG_RIGHT - opposite to normal direction */
   UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t extent_type;
                                              /* To create secondary contour flange use following options 
                                                 Extent to which profile is to be swept, 
                                                 IG_FINITE - sweep the skecth through specified distance along 
                                                             projection direction(default),
                                                 IG_TO_END_OF_EDGE - sweep along the whole edge   
                                                 IG_SYMMETRIC - sweep the sketch through specfied distance along
                                                                     normal and opposite to normal to plane
                                              
                                                To create chain contour flange use following option
                                                IG_TO_END_OF_EDGE - sweep along the whole edge  */
                                                    

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t bend_parm_type;
                                                   /* IG_NFTYPE(default) */
        
    UF_NXSM_mitre_cflange_data_t mitre_data;       /* Data for mitre cut */

    UF_NXSM_bend_option_t bend_options;            /* Bend data */
};
typedef struct UF_NXSM_sec_cflange_data_s UF_NXSM_sec_cflange_data_t, *UF_NXSM_sec_cflange_data_p_t;

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_NXSM_TYPES_H_INCLUDED */





