/***************************************************************************
             Copyright (c) 1998 - 2002,2003,2004,2005,2006,2010 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved

  

File Description :

NX Open typedefs and macros that are specific to the DRF module.


 ***************************************************************************/

#ifndef UF_DRF_TYPES_INCLUDED
#define UF_DRF_TYPES_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_cfi.h>
#include <uf_obj_types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define SYMBOL_NAME_SIZE          8  /* maximum symbol name size, not
                                        including "\0"      */

#define MAX_ID_SYM_TEXT_LENGTH   20  /* maximum id symbol text length */
#define NUM_INT_LEADER_PTS        7  /* number of intermediate leader points */
#define FILL_PAT_TYPE_SOLID      10  /* area fill pattern type 10 is solid fill
                                     */
#define TEXT_BUFFER_LENGTH       20  /* text buffer length, not including "\0"*/
#define NUM_REAL_PARMS           70  /* number of real parameters */
#define NUM_INT_PARMS           100  /* number of integer parameters */
#define MAX_CENTERLINE_OBJECTS  100  /* maximum number of centerline objects */                                     
#define MAX_TEXT_LENGTH         300  /* maximum text length, not including "\0"
                                     */
#define MAX_BOUNDARY_OBJECTS   1024  /* maximum number of objects in hatch
                                        boundary       */

/* Method for circular centerline */
#define UF_DRF_center_point       1  /* Center Point Method  */
#define UF_DRF_thru_3_points      2  /* Thru 3 Points Method */

/* Method for calculating offset distance */
#define UF_DRF_off_distance       1  /* Offset Distance Method */
#define UF_DRF_off_position       2  /* Offset Position Method */

#define UF_DRF_DECIMAL_PLACES_MAX 9  /* The number of decimal places */

#define UF_DRF_MAX_HATCH_FILE_NAME_LEN (UF_CFI_MAX_FILE_NAME_BUFSIZE-1)
/*  */
#define SYMBOL_FILE_NAME_SIZE (UF_CFI_MAX_FILE_NAME_BUFSIZE-1) /* Maximum symbol file name size (not including '\0') */
#define MAX_LINE_LENGTH         (MAX_LINE_BUFSIZE - 1) /* maximum line length, not including "\0"*/
/*  */ 


#define UF_DRF_MAX_FONT_NCHARS 16
#define UF_DRF_MAX_FONT_BUFSIZE (NX_BUFSIZE(UF_DRF_MAX_FONT_NCHARS))

/* 
  UF_DRF_MAX_HATCH_MATERIAL_NAME, SYMBOL_FILE_NAME_SIZE and  UF_DRF_MAX_HATCH_FILE_NAME_LEN 
  are being deprecated because NX is moving to support multibyte characters. 

  User written programs should start using the new definitions for file names:
  UF_DRF_MAX_HATCH_MATERIAL_NAME_BUFSIZE should be used for buffer allocations and memory
                    allocations, e.g. char my_fspec[UF_CFI_MAX_FILE_NAME_BUFSIZE];
  UF_DRF_MAX_HATCH_MATERIAL_NAME_NCHARS  should be used to limit the number of characters in
                    a symbol file name.  NX code will enforce these limits.
  UF_CFI_MAX_FILE_NAME_BUFSIZE should be used for buffer allocations and memory
                    allocations, e.g. char my_fspec[UF_CFI_MAX_FILE_NAME_BUFSIZE];
  UF_CFI_MAX_FILE_NAME_NCHARS  should be used to limit the number of characters in
                    a symbol file name.  NX code will enforce these limits.

  New routines have been added which will help in this transition:
  UF_TEXT_count_characters() will count the number of characters in a string.
  UF_TEXT_terminate_chars() will terminate a C string after the given
  number of characters.
*/
#define UF_DRF_MAX_HATCH_MATERIAL_NAME_NCHARS 30
#define UF_DRF_MAX_HATCH_MATERIAL_NAME_BUFSIZE NX_BUFSIZE(UF_DRF_MAX_HATCH_MATERIAL_NAME_NCHARS)

/*  */
#define UF_DRF_MAX_HATCH_MATERIAL_NAME (UF_DRF_MAX_HATCH_MATERIAL_NAME_BUFSIZE-1)
/*  */ 

/* Chamfer Dimension : dimension form */
enum UF_DRF_chamfer_dimension_form_e
{
    UF_DRF_CHAMFER_FORM_SYMBOL = 1,
    UF_DRF_CHAMFER_FORM_SIZE,
    UF_DRF_CHAMFER_FORM_SIZEANGLE,
    UF_DRF_CHAMFER_FORM_ANGLESIZE
};
typedef enum UF_DRF_chamfer_dimension_form_e UF_DRF_chamfer_dimension_form_t;

/* Chamfer Dimension : stub type */
enum UF_DRF_chamfer_dimension_stub_type_e
{
    UF_DRF_CHAMFER_TEXTABOVE_LEADER_NOSTUB = 1,
    UF_DRF_CHAMFER_TEXTAFTER_LEADER_NOSTUB,
    UF_DRF_CHAMFER_TEXTABOVE_STUB,
    UF_DRF_CHAMFER_TEXTAFTER_STUB
};
typedef enum UF_DRF_chamfer_dimension_stub_type_e UF_DRF_chamfer_dimension_stub_type_t;

/* Chamfer Dimension : leader type */
enum UF_DRF_chamfer_dimension_leader_type_e
{
    UF_DRF_CHAMFER_PERPENDICULAR_LEADER = 1,
    UF_DRF_CHAMFER_PARALLEL_LEADER,
    UF_DRF_CHAMFER_LINEAR_CHAMFER_DIM
};
typedef enum UF_DRF_chamfer_dimension_leader_type_e UF_DRF_chamfer_dimension_leader_type_t;

/* Chamfer Dimension : symbol type */
enum UF_DRF_chamfer_dimension_symbol_type_e
{
    UF_DRF_CHAMFER_NONE_SYMBOL = 1,
    UF_DRF_CHAMFER_PREFIX_SYMBOL,
    UF_DRF_CHAMFER_SUFFIX_SYMBOL
};
typedef enum UF_DRF_chamfer_dimension_symbol_type_e UF_DRF_chamfer_dimension_symbol_type_t;

struct UF_DRF_chamfer_dimension_data_s
{
    UF_DRF_chamfer_dimension_form_t        form;
    UF_DRF_chamfer_dimension_stub_type_t   stub_type;
    UF_DRF_chamfer_dimension_leader_type_t leader_type;
    UF_DRF_chamfer_dimension_symbol_type_t symbol_type;
    char                                  *symbol_name;
    double                                 space_factor;
};
typedef struct UF_DRF_chamfer_dimension_data_s UF_DRF_chamfer_dimension_data_t, *UF_DRF_chamfer_dimension_data_p_t;

/* Centerline forms */
enum UF_DRF_valid_cline_form_e{
        UF_DRF_linear_cline = 1,     /* Linear Centerline */
        UF_DRF_cpt_cline_fcir,       /* Full Circular Centerline -
                                        Center Point Method */
        UF_DRF_cpt_cline_pcir,       /* Partial Circular Centerline -
                                        Center Point Method */
        UF_DRF_cpt_cline_fbolt,      /* Full Bolt Circle Centerline -
                                        Center Point Method */
        UF_DRF_cpt_cline_pbolt,      /* Partial Bolt Circle Centerline -
                                        Center Point Method */
        UF_DRF_3pt_cline_fcir,       /* Full Circular Centerline -
                                        3 Point Method */
        UF_DRF_3pt_cline_pcir,       /* Partial Circular Centerline -
                                        3 Point Method */
        UF_DRF_3pt_cline_fbolt,      /* Full Bolt Circle Centerline -
                                        3 Point Method */
        UF_DRF_3pt_cline_pbolt,      /* Partial Bolt Circle Centerline -
                                        3 Point Method */
        UF_DRF_offcyl_cline_off,     /* Offset Cylindrical Centerline -
                                        Keyed-in Offset Distance */
        UF_DRF_offcyl_cline_obj,     /* Offset Cylindrical Centerline -
                                        Calculate Offset Distance from Object */
        UF_DRF_symmetrical_cline,    /* Symmetrical Centerline */
        UF_DRF_offctrpt_nx,          /* Offset Center Point, x-axis -
                                        Distance from Arc Normal */
        UF_DRF_offctrpt_cx,          /* Offset Center Point, x-axis -
                                        Distance from Arc Center */
        UF_DRF_offctrpt_fx,          /* Offset Center Point, x-axis -
                                        Calculate (Find) Distance */
        UF_DRF_offctrpt_ny,          /* Offset Center Point, y-axis -
                                        Distance from Arc Normal */
        UF_DRF_offctrpt_cy,          /* Offset Center Point, y-axis -
                                        Distance from Arc Center */
        UF_DRF_offctrpt_fy,          /* Offset Center Point, y-axis -
                                        Calculate (Find) Distance */
        UF_DRF_block_cline           /* Block Centerline */
};
typedef enum UF_DRF_valid_cline_form_e UF_DRF_valid_cline_form_t;

/* Area Fill material types */
enum UF_DRF_valid_material_e{
        UF_DRF_corkfeltfiber = 1,
        UF_DRF_soundinsulation,
        UF_DRF_concrete,
        UF_DRF_earth,
        UF_DRF_rock,
        UF_DRF_sand,
        UF_DRF_liquids,
        UF_DRF_woodacrossgrain,
        UF_DRF_woodwithgrain
};
typedef enum UF_DRF_valid_material_e UF_DRF_valid_material_t;

/* Area Fill: UF_drafting_entity_type, UF_draft_area_fill_subtype */
struct UF_DRF_areafill_s {
        UF_DRF_valid_material_t material; /* area fill material type
                                             material is defined by the
                                             UF_DRF_valid_material_t
                                          */
        double                  scale;    /* area fill scale             */
        double                  angle;    /* area fill angle, in radians */
        double                  tolerance;  /* area fill tolerance */
};
typedef struct UF_DRF_areafill_s UF_DRF_areafill_t, *UF_DRF_areafill_p_t;

/* id symbol types */
enum UF_DRF_id_symbol_type_e{
        UF_DRF_sym_circle = 1,            /* circle               */
        UF_DRF_sym_divcir,                /* divided circle       */
        UF_DRF_sym_square,                /* square               */
        UF_DRF_sym_divsqr,                /* divided square       */
        UF_DRF_sym_hexagon,               /* hexagon              */
        UF_DRF_sym_divhex,                /* divided hexagon      */
        UF_DRF_sym_triup,                 /* triangle, point up   */
        UF_DRF_sym_tridown,               /* triangle, point down */
        UF_DRF_sym_datum,                 /* datum target         */
        UF_DRF_sym_roundbox,              /* rounded box          */
        UF_DRF_sym_underline,             /* underline            */
        UF_DRF_sym_maximum
} ;
typedef enum UF_DRF_id_symbol_type_e UF_DRF_id_symbol_type_t;

/* Dimension reference display option */
enum UF_DRF_reference_symbol_type_e{
    UF_DRF_NO_REFERENCE_SYMBOL = 0,
    UF_DRF_WITH_REFERENCE_SYMBOL
};
typedef enum UF_DRF_reference_symbol_type_e UF_DRF_reference_symbol_type_t;

/* Dimension inspection display option */
enum UF_DRF_inspection_type_e{
    UF_DRF_NO_INSPECTION = 0,
    UF_DRF_WITH_INSPECTION
};
typedef enum UF_DRF_inspection_type_e UF_DRF_inspection_type_t;

enum UF_DRF_trim_dim_line_style_e
{
    UF_DRF_DONT_TRIM_DIM_LINE = 0,
    UF_DRF_TRIM_DIM_LINE
};
typedef enum UF_DRF_trim_dim_line_style_e UF_DRF_trim_dim_line_style_t;

/* object associativity types */
enum UF_DRF_assoc_type_e{
        UF_DRF_assoc_type_none = 0,
        UF_DRF_end_point,
        UF_DRF_arc_center,                /* object must be an arc */
        UF_DRF_tangency,                  /* object must be an arc */
        UF_DRF_intersection,
        UF_DRF_dwg_pos,
        UF_DRF_utility_symbol = 9,
        UF_DRF_smart_point,               /* Used only for UF_DRAW section
                                           * line associativities.
                                           */
        UF_DRF_on_annotation,             /* object must be an annotation*/
        UF_DRF_on_stub,                   /* object must be an annotation*/
        UF_DRF_assoc_type_maximum
};
typedef enum UF_DRF_assoc_type_e UF_DRF_assoc_type_t;

/* object associativity modifiers */
#define UF_DRF_first_end_point         1  /* first end point, associativity
                                             type is UF_DRF_end_point */
#define UF_DRF_last_end_point          2  /* last end point,  associativity
                                             type is UF_DRF_end_point */

/******************************************************************************
 * object specification structure                                             *
 ******************************************************************************/
struct UF_DRF_object_s {
        tag_t               object_tag; /* tag of associated object
                                         depending on object_assoc_type, object
                                         may be a point, line, arc, conic,
                                         cubic spline, B curve, pattern, solid
                                         curve, utility symbol (centerline),
                                         annotation, or ignored
                                        */
        tag_t               object_view_tag; /* tag of member view of
                                             object_tag
                                             */
        UF_DRF_assoc_type_t object_assoc_type; /* object associativity type
                                               UF_DRF_end_point
                                               UF_DRF_arc_center
                                               object must be an arc
                                               UF_DRF_tangency
                                               object must be an arc
                                               UF_DRF_intersection
                                               UF_DRF_dwg_pos
                                               UF_DRF_utility_symbol
                                               UF_DRF_on_annotation
                                               UF_DRF_on_stub
                                               */

        int                 object_assoc_modifier; /* object associativity modifier
                                  - if object_assoc_type = UF_DRF_end_point,
                                    UF_DRF_first_end_point on object or
                                    UF_DRF_last_end_point on object.
                                  - if object_assoc_type = UF_DRF_tangency,
                                      parameter percentage (0 - 100) to compute
                                      approximate tangent point on object
                                  - if object_assoc_type = UF_DRF_arc_center,
                                      UF_DRF_intersection, UF_DRF_dwg_pos,
                                      UF_DRF_utility_symbol, modifier is ignored
                               */
        tag_t               object2_tag; /* - if object_assoc_type =
                                         UF_DRF_intersection,
                                         tag of second object of intersection
                                         and second object must reside in
                                         member view of object_view_tag
                                         described above
                                         - if object_assoc_type =
                                            UF_DRF_end_point,
                                            UF_DRF_arc_center,
                                            UF_DRF_tangency,
                                            UF_DRF_dwg_pos,
                                            UF_DRF_utility_symbol,
                                            second object is ignored
                                         */
        double              assoc_dwg_pos[2]; /* if object_assoc_type = UF_DRF_dwg_pos,
                                    assoc_dwg_pos[0] = x drawing abs coordinate
                                    assoc_dwg_pos[1] = y drawing abs coordinate
                                   if object_assoc_type = UF_DRF_intersection,
                                    intersection closest to assoc_dwg_pos
                                   if object_assoc_type = UF_DRF_end_point,
                                    UF_DRF_arc_center, UF_DRF_tangency,
                                    or UF_DRF_utility_symbol, assoc_dwg_pos is
                                    ignored */
} ;
typedef struct UF_DRF_object_s UF_DRF_object_t, *UF_DRF_object_p_t;

/* leader mode */
enum UF_DRF_leader_mode_e{
        UF_DRF_without_leader = 1,        /* without leader        */
        UF_DRF_with_leader                /* with leader           */
};
typedef enum UF_DRF_leader_mode_e UF_DRF_leader_mode_t;

/* leader type */
enum UF_DRF_leader_type_e{
        UF_DRF_leader_type_none = 1,      /* none                  */
        UF_DRF_leader_type_line,          /* leader line           */
        UF_DRF_leader_type_ext_line,      /* leader extension line */
        UF_DRF_leader_type_datum,         /* Datum leader line -
                                             GD&T symbols only
                                          */
        UF_DRF_leader_type_maximum
};
typedef enum UF_DRF_leader_type_e UF_DRF_leader_type_t;

/* leader attachment type */
enum UF_DRF_leader_attach_type_e{
        UF_DRF_leader_attach_object = 1,  /* attached to object */
        UF_DRF_leader_attach_screen,      /* screen position */
        UF_DRF_leader_attach_triangle     /* datum triangle - gd&t symbols only
                                          */
} ;
typedef enum UF_DRF_leader_attach_type_e UF_DRF_leader_attach_type_t;

/* frame corner for UF_DRF_leader_type_t = UF_DRF_leader_type_ext_line */
enum UF_DRF_frame_corner_e{
        UF_DRF_frame_none       = 0,
        UF_DRF_frame_upper_left = 1,
        UF_DRF_frame_upper_right,
        UF_DRF_frame_lower_left,
        UF_DRF_frame_lower_right
} ;
typedef enum UF_DRF_frame_corner_e UF_DRF_frame_corner_t;

/*
  
  The UF_DRF_one_apptext_line_t data type was added specifically so that the
  UF_DRF_text_s struct could contain a pointer to this type.  It is advised that
  users begin to use this new data when defining appended text in the UF_DRF_text_t
  struct to remove the dependence on hard coded size values.

  
*/
typedef char    UF_DRF_one_apptext_line_t[133];

/* text specification
   set the desired TEXT ENTRY MODE preference (with UF_DRF_set_preferences)
   to activate the desired component of the text structure
   MPI[7] TEXT ENTRY MODE
          1 = ONLY AUTOMATIC TEXT
          2 = AUTOMATIC TEXT and APPENDED TEXT
          3 = ONLY MANUAL TEXT
          4 = MANUAL TEXT and APPENDED TEXT

  an example of initializing the appended_text element of the structure in a C++ program:

     UF_DRF_text_t drf_text;
     char appended_text[3][133] = {"Appended Text Line 1",
                                   "Appended Text Line 2",
                                   "Appended Text Line 3"};
     drf_text.lines_app_text = 3;
     drf_text.appended_text = appended_text;

  
  The type of the appended_text field now specifies the length of
  the character string in order to avoid errors from some compilers.
  This has the added benefit of eliminating the cast formerly
  required in the appended_text field assignment above.

  
  Using the new data type here is an example of initializing the appended_text field
  of the UF_DRF_text_t struct in a C++ program:

  UF_DRF_text_t             drf_text;
  UF_DRF_one_apptext_line_t appended_text[] = {"Appended Text Line 1",
                                               "Appended Text Line 2",
                                               "Appended Text Line 3"};
  drf_text.lines_app_text = 3;
  drf_text.appended_text = appended_text;

  This is the preferred method as there is no longer any dependence on the size of 133.
*/
struct UF_DRF_text_s {
    char *                          user_dim_text;  /* user supplied dimension text string */
    int                             lines_app_text; /* number of lines of appended text */
    UF_DRF_one_apptext_line_t *     appended_text;  /* <len:lines_app_text> appended text array */
};
typedef struct UF_DRF_text_s UF_DRF_text_t, *UF_DRF_text_p_t;
/*****************************************************************
 Drafting block types
*****************************************************************/
enum UF_DRF_block_type_e
{
        UF_DRF_LINE_BLOCK,              /* lines                */
        UF_DRF_ARCS_BLOCK,              /* arcs                 */
        UF_DRF_TEXT_BLOCK,              /* text                 */
        UF_DRF_ARROWS_BLOCK,            /* arrows               */
        UF_DRF_ASSOCIATIVITY_BLOCK      /* associativity        */
};
typedef enum UF_DRF_block_type_e UF_DRF_block_type_t;

/*****************************************************************
 User Defined Symbol pen types
*****************************************************************/
enum UF_DRF_ud_symbol_pen_type_e
{
        UF_DRF_UD_SYMBOL_MOVE,          /* move                 */
        UF_DRF_UD_SYMBOL_DRAW           /* draw                 */
} ;
typedef enum UF_DRF_ud_symbol_pen_type_e UF_DRF_ud_symbol_pen_type_t;
/****************************************************************
  Line associativity types
*****************************************************************/
enum UF_DRF_assoc_line_type_e
{
    UF_DRF_ASSOC_LINE_TYPE_NONE,
    UF_DRF_EXISTING_LINE,
    UF_DRF_TWO_POINTS,
    UF_DRF_DWG_LINE,
    UF_DRF_ASSOC_LINE_TYPE_MAX
} ;
typedef enum UF_DRF_assoc_line_type_e UF_DRF_assoc_line_type_t;
/*****************************************************************
 Possible values for leader orientation:
*****************************************************************/
enum UF_DRF_leader_orientation_e{
        UF_DRF_NO_STUB,                 /* without stub          */
        UF_DRF_LEADER_LEFT,             /* left orientation      */
        UF_DRF_LEADER_RIGHT,            /* right orientation     */
        UF_DRF_LEADER_TOP,              /* top orientation       */
        UF_DRF_LEADER_BOTTOM            /* bottom orientation    */
};
typedef enum UF_DRF_leader_orientation_e UF_DRF_leader_orientation_t;
/*****************************************************************
 Possible values for arrowhead type
*****************************************************************/
enum UF_DRF_arrow_type_e{
        UF_DRF_ARROW_CLOSED = 1,            /* closed arrowhead              */
        UF_DRF_ARROW_OPEN,                  /* open arrowhead                */
        UF_DRF_ARROW_CROSS,                 /* cross arrowhead               */
        UF_DRF_ARROW_DOT,                   /* dot arrowhead                 */
        UF_DRF_ARROW_SYM,                   /* origin symbol                 */
        UF_DRF_ARROW_NONE,                  /* none                          */
        UF_DRF_DATUM_ARROW,                 /* Datum symbol                  */
        UF_DRF_ARROW_SOLID_CLOSED,          /* closed solid arrowhead        */
        UF_DRF_ARROW_DOUBLE_CLOSED,         /* closed double arrowhead       */
        UF_DRF_ARROW_DOUBLE_SOLID_CLOSED,   /* closed double solid arrowhead */
        UF_DRF_ARROW_DOUBLE_OPEN,           /* open double arrowhead         */
        UF_DRF_ARROW_INTEGRAL,              /* integral                      */
        UF_DRF_ARROW_BOX,                   /* box                           */
        UF_DRF_ARROW_TOP_OPEN,              /* single side top open arrowhead */
        UF_DRF_ARROW_BOTTOM_OPEN            /* single side bottom open arrowhead */
};
typedef enum UF_DRF_arrow_type_e UF_DRF_arrow_type_t;
/****************************************************************
 Possible value for filled arrowhead
*****************************************************************/
enum UF_DRF_arrow_fill_type_e{
        UF_DRF_ARROW_NO_FILL,            /* filled arrowheads    */
        UF_DRF_ARROW_FILLED              /* no fill arrowheads   */
};
typedef enum UF_DRF_arrow_fill_type_e UF_DRF_arrow_fill_type_t;

/*****************************************************************
 Possible values for combined arrowhead and fill type

 The enum value corresponding to 7 is unused since there is no
 mapping of the datum symbol.
*****************************************************************/
enum UF_DRF_arrowhead_and_fill_type_e{
        UF_DRF_FILLED_DOT          = -1,                  /* filled dot       */
        UF_DRF_FILLED_ARROW        = 0,                   /* filled arrowhead */
        UF_DRF_CLOSED_ARROW        = (int)UF_DRF_ARROW_CLOSED, /* closed arrowhead */
        UF_DRF_OPEN_ARROW          = (int)UF_DRF_ARROW_OPEN,   /* open arrowhead   */
        UF_DRF_CROSS_ARROW         = (int)UF_DRF_ARROW_CROSS,  /* cross arrowhead  */
        UF_DRF_DOT_ARROW           = (int)UF_DRF_ARROW_DOT,    /* dot arrowhead    */
        UF_DRF_ORIGIN_SYMBOL_ARROW = (int)UF_DRF_ARROW_SYM,    /* origin symbol    */
        UF_DRF_NO_ARROW            = (int)UF_DRF_ARROW_NONE,   /* none             */
        UF_DRF_CLOSED_SOLID_ARROW  = (int)UF_DRF_ARROW_SOLID_CLOSED,          /* closed solid arrowhead        */
        UF_DRF_CLOSED_DOUBLE_ARROW = (int)UF_DRF_ARROW_DOUBLE_CLOSED,         /* closed double arrowhead       */
        UF_DRF_CLOSED_DOUBLE_SOLID_ARROW   = (int)UF_DRF_ARROW_DOUBLE_SOLID_CLOSED,   /* closed double solid arrowhead */
        UF_DRF_OPEN_DOUBLE_ARROW           = (int)UF_DRF_ARROW_DOUBLE_OPEN,           /* open double arrowhead         */
        UF_DRF_INTEGRAL_ARROW              = (int)UF_DRF_ARROW_INTEGRAL,              /* integral                      */
        UF_DRF_BOX_ARROW                   = (int)UF_DRF_ARROW_BOX,                    /* box                           */
        UF_DRF_FILLED_BOX          = 14,                  /* filled box              */
        UF_DRF_FILLED_DOUBLE_ARROW = 15                  /* filled double arrowhead */
};
typedef enum UF_DRF_arrowhead_and_fill_type_e UF_DRF_arrowhead_and_fill_type_t;

/*****************************************************************
 Possible value for text type
*****************************************************************/
enum UF_DRF_text_type_e{
        UF_DRF_DIM_TEXT = 1,
        UF_DRF_DUAL_DIM_TEXT,
        UF_DRF_TOLERANCE_TEXT,
        UF_DRF_DUAL_TOLERANCE_TEXT,
        UF_DRF_RAD_DIA_TEXT,
        UF_DRF_TEXT_APP_AT_CREATION,
        UF_DRF_TEXT_APP_AT_EDITING
};
typedef enum UF_DRF_text_type_e UF_DRF_text_type_t;

enum UF_DRF_narrow_dimension_display_type_e{
     UF_DRF_NARROW_DISPLAY_NONE = 0,
     UF_DRF_NARROW_DISPLAY_NO_LEADER,
     UF_DRF_NARROW_DISPLAY_WITH_LEADER_NO_STUB,
     UF_DRF_NARROW_DISPLAY_TEXT_ABOVE_STUB,
     UF_DRF_NARROW_DISPLAY_TEXT_AFTER_STUB
};
typedef enum UF_DRF_narrow_dimension_display_type_e UF_DRF_narrow_dimension_display_type_t;

enum UF_DRF_narrow_dimension_text_orientation_e{
     UF_DRF_NARROW_HORIZONTAL = 0,
     UF_DRF_NARROW_PARALLEL
};
typedef enum UF_DRF_narrow_dimension_text_orientation_e UF_DRF_narrow_dimension_text_orientation_t;

struct UF_DRF_narrow_dimension_info_s
{
    UF_DRF_narrow_dimension_display_type_t      display_type;
    UF_DRF_narrow_dimension_text_orientation_t  text_orientation;
    double                                      leader_angle;
    double                                      text_offset;
};
typedef struct UF_DRF_narrow_dimension_info_s UF_DRF_narrow_dimension_info_t,
                                              *UF_DRF_narrow_dimension_info_p_t;

/*****************************************************************
 This is a structure to hold data in TEXT record.
*****************************************************************/
struct UF_DRF_draft_aid_text_s
{
        int     num_chars;              /* number of characters
               The 132 byte maximum line restriction has been removed.
               string is available as a legacy variable containing the
               line which will still be truncated to 132 bytes.

               Please modify your programs to use full_string instead,
               since string will be removed in a future NX release.

               UF_DRF_free_text will free this string along with other
               variables in the UF_DRF_draft_aid_text_info_t structure.

               Note that the old limit of MAX_LINE_BUFSIZE is the number of
               bytes, NOT the number of characters.  In the default C locale
               these two values will be the same.  However for localized text
               in another locale, there will be multibyte characters. */

        char    string[MAX_LINE_BUFSIZE];      /* Buffer large enough to hold MAX_LINE_NCHARS characters */                                            
        int     num_ints;               /* string physical length */

        int     full_num_chars;         /* number of bytes in full string */
        char    *full_string;           /* full string (not terminated to 132 bytes) */
};

typedef struct UF_DRF_draft_aid_text_s UF_DRF_draft_aid_text_t,
                                       *UF_DRF_draft_aid_text_p_t;
/*****************************************************************
 This is a structure to hold information in drafting aid text
 History - V15.0 change: The text_type field was added.
           NX2.0 change: The text_type was changed to UF_DRF_text_type_t
*****************************************************************/
struct UF_DRF_draft_aid_text_info_s
{
        UF_DRF_text_type_t      text_type; /* Drafting aid text type */
        int                     text_font; /* Drafting aid text character font */
        double                  size;   /* Drafting aid text character size */
        double                  angle;  /* Drafting aid text angle in radians */
        double                  origin[3]; /* x, y, z coordinates of text origin
                                           in the coordinate system of the
                                           drafting object. */
        double                  length; /* Drafting aid text length */
        double                  height; /* Drafting aid text height */
        double                  distance; /* Drafting aid text distance from
                                           origin  (usually the lower  left
                                           corner of the first line of text)
                                           to top of the text box.*/
        double                  aspect_ratio; /* Drafting aid text aspect ratio */
        double                  gap;    /* Drafting aid text character gap */
        double                  line_spacing; /* Drafting aid text line spacing */
        int                     num_lines; /* Number of drafting aid text lines
                                           */
        UF_DRF_draft_aid_text_t *text;     /* <len:num_lines> Drafting aid text data structure
                                              to hold text data
                                           */
};
typedef struct UF_DRF_draft_aid_text_info_s UF_DRF_draft_aid_text_info_t,
                                            *UF_DRF_draft_aid_text_info_p_t;
/*****************************************************************
 This is a structure to hold the User Defined Symbol
 stroke data information.
*****************************************************************/
struct UF_DRF_stroke_info_s
{
        UF_DRF_ud_symbol_pen_type_t
                        pen_status;     /* UF_DRF_UD_SYMBOL_DRAW= draw,
                                           UF_DRF_UD_SYMBOL_MOVE = move */
        int             x_length;       /* Integerized X value in the range
                                           0-127, representing a number from
                                           0 to the symbol length */
        int             y_length;       /* Integerized Y value in the range
                                           0-127, representing a number from
                                           0 to the symbol length */
};
typedef struct UF_DRF_stroke_info_s UF_DRF_stroke_info_t,
                                     *UF_DRF_stroke_info_p_t;

/*****************************************************************
 This structure contains the User Defined Symbol font information.
 
*****************************************************************/
struct UF_DRF_ud_symbol_font_info_s
{
        int             anchor_point;   /* This is integerized x, y value for
                                           anchor point.
                                           bits 0 ~ 6 represent y value and
                                           bits 7 ~ 14 represent x value */
        int             orientation_point; /* this is integerized x, y value for
                                           orientation point.
                                           bits 0 ~ 6 represent y value and
                                           bits 7 ~ 14 represent x value */
        double          factor;         /* User Defined Symbol factor */
        double          length;         /* User Defined Symbol length */
        double          height;         /* User Defined Symbol height */
        int             num_stroke;     /* Number of strokes */
        UF_DRF_stroke_info_t
                        *stroke_info;   /* <len:num_stroke>
                                           Stroke data stored as data structure
                                           UF_DRF_stroke_info_t
                                        */
};
typedef struct UF_DRF_ud_symbol_font_info_s
               UF_DRF_ud_symbol_font_info_t,
               *UF_DRF_ud_symbol_font_info_p_t;
/*****************************************************************************
 *   Line associativity structure                                            *
 *****************************************************************************/
struct UF_DRF_line_object_s {
    UF_DRF_assoc_line_type_t    line_assoc_type; /* line associativity type as defined by
                                     UF_DRF_assoc_line_type_t,
                                        UF_DRF_EXISTING_LINE
                                        UF_DRF_TWO_POINTS
                                        UF_DRF_DWG_LINE
                                  */
    UF_DRF_object_t             object1; /* For UF_DRF_EXISTING_LINE this is the
                                     UF_DRF_object_t that contains the line
                                     definition as defined by UF_DRF_object_t.

                                     For UF_DRF_TWO_POINTS this is the
                                     UF_DRF_object_t that contains the first
                                     point definition as defined by
                                     UF_DRF_object_t.

                                     For UF_DRF_DWG_LINE this is the
                                     UF_DRF_object_t that defines the first
                                     endpoint of the line in
                                     object.assoc_dwg_pos.
                                  */

    UF_DRF_object_t             point_object2; /* For UF_DRF_EXISTING_LINE this is unused.

                                     For UF_DRF_TWO_POINTS this is the
                                     UF_DRF_object_t that contains the second
                                     point definition as defined by
                                     UF_DRF_object_t.

                                     For UF_DRF_DWG_LINE this is the
                                     UF_DRF_object_t that defines the second
                                     endpoint of the line in
                                     object.assoc_dwg_pos.
                                  */

} ;
typedef struct UF_DRF_line_object_s UF_DRF_line_object_t,
                                    *UF_DRF_line_object_p_t;

/*****************************************************************
 This is a structure to hold embedded user defined symbol
 History - This structure was originally released in V15.0.
*****************************************************************/
struct UF_DRF_symbol_instance_s
{
    tag_t master;                  /* master symbol                        */
    logical is_gap;                /* TRUE if a gap, else FALSE            */
    double origin[3];              /* symbol origin in csys of annotation  */
    double parameter_on_element;   /* normalized parameter on line or arc  */
    double symbol_length;          /* length of symbol                     */
    double symbol_height;          /* height of symbol                     */
    int creation_mask;             /* symbol creation mask                 */
    int record_number;             /* record number in owning component    */
    int segment_number;            /* segment number of owning component
                                      segment                              */
    logical is_mirrored;           /* TRUE if reflected about its X axis   */
    logical is_reflected;          /* TRUE if reflected about line between
                                      anchor and connection pt             */
};
typedef struct UF_DRF_symbol_instance_s UF_DRF_symbol_instance_t,
                                        *UF_DRF_symbol_instance_p_t;

/*****************************************************************
 This is a structure to hold drafting aid line information
 History - V15.0 change: The following fields were added: sequence_number,
           num_symbols, and symbol_data.
           V17.0 segment_pnts is now dynamically allocated.
                 the minimum size will be its previous fixed size
                 which was MAX_LINE_NCHARS * 6.
*****************************************************************/
struct UF_DRF_draft_aid_line_s
{
        int     sequence_number;        /* array of line sequence
                                           numbers per line*/
        int     num_symbols;            /* number of User Defined
                                           Symbols              */
        UF_DRF_symbol_instance_t
                *symbol_data;           /* User Defined Symbol   */
        int     num_segments;           /* number of lines       */
        double *segment_pnts;           /* x, y, z line segment end points
                                           in the coordinate system of the
                                           drafting object. */
} ;
typedef struct UF_DRF_draft_aid_line_s UF_DRF_draft_aid_line_t,
                                       *UF_DRF_draft_aid_line_p_t;

/*****************************************************************
 This is a structure to hold associativity data
*****************************************************************/
struct UF_DRF_assoc_info_s
{
        tag_t                        assoc_object_tag; /* tag of associated object       */
        tag_t                        assoc_object_view_tag; /* tag of member view of
                                           assoc_object_tag               */
        UF_DRF_assoc_type_t          assoc_type; /* object associativity type      */
        int                          assoc_modifier; /* object associativity modifier  */
} ;
typedef struct UF_DRF_assoc_info_s UF_DRF_assoc_info_t,
                                   *UF_DRF_assoc_info_p_t;
/*****************************************************************
This is a structure to hold arc data
History - V15.0 change: The following fields were added: arc_type,
          sequence_number, num_symbols, and symbol_data.
*****************************************************************/
struct UF_DRF_arc_info_s {
    int                   arc_type;     /* arc type              */
    int                   sequence_number;  /* arc sequence number   */
    double                arc_center [ 3 ]; /* x, y coordinate       */
    double                radius;       /* arc radius            */
    double                start_angle;  /* arc start angle       */
    double                end_angle;    /* arc end angle         */
    int                   num_symbols;  /* number of User Defined
                                           Symbols               */
    UF_DRF_symbol_instance_t
                          *symbol_data; /* <len:num_symbols>User Defined Symbol
                                           data                  */
    int                   num_assoc_objs; /* number of associated
                                           objects               */
    UF_DRF_assoc_info_t   *assoc_objs; /* <len:num_assoc_objs>leader assoc object tag
                                           type, and modifier    */
} ;
typedef struct UF_DRF_arc_info_s UF_DRF_arc_info_t,
                                  *UF_DRF_arc_info_p_t;
/*****************************************************************
 This is a structure to hold arrowhead data
 History - V15.0 change: The sequence_number field was added.
*****************************************************************/
struct UF_DRF_arrow_info_s
{
        int                           sequence_number; /* arrow sequence number */
        UF_DRF_arrow_type_t           arrow_type; /* arrowhead type. See
                                            UF_DRF_arrow_type_t
                                        */
        UF_DRF_arrow_fill_type_t      arrow_fill; /* arrowhead fill. See
                                             UF_DRF_arrow_fill_type_t
                                         */
        double                        arrow_origin[ 3 ]; /* arrowhead origin in the coordinate
                                            system of the drafting object.
                                         */
        double                        arrow_angle; /* arrowhead angle in degs     */
        double                        arrow_include_angle; /* arrowhead include
                                            angle in degs               */
        double                        arrow_height; /* arrowhead height     */
        double                        arrow_width; /* arrowhead width      */
};
typedef struct UF_DRF_arrow_info_s UF_DRF_arrow_info_t,
                                   *UF_DRF_arrow_info_p_t;
/*****************************************************************
 This is a structure to hold information for a leader.
*****************************************************************/
struct UF_DRF_leader_info_s
{
UF_DRF_leader_attach_type_t  leader_attach_type[7]; /* Each leader may have up to 7 intermediate
                                     points.  This is an array of the attachment
                                     types for each of the points.  [0] is the
                                     information for the first point, [1] is
                                     for the second point, etc.
                                     Each element can have one of the values:
                                          UF_DRF_leader_attach_object
                                          UF_DRF_leader_attach_screen
                                          UF_DRF_leader_attach_triangle
                                     Only a GD&T symbol may have the type,
                                     UF_DRF_leader_attach_triangle.
                                  */
int num_linebks;                  /* Number of graphical line elements used
                                     to represent the leader in the display.*/
UF_DRF_draft_aid_line_t *leader_pnts; /* <len:num_linebks>
                                         Array of structures, one for each
                                         of the num_linebks line elements.
                                         Each line element may have multiple
                                         line segments.
                                      */

int num_assoc_objs;                   /* number of associated objects   */
UF_DRF_assoc_info_t *assoc_objs;      /* <len:num_assoc_objs>
                                         Array of leader associated objects,
                                         one structure for each of the
                                         num_assoc_objs objects.
                                      */
} ;
typedef struct UF_DRF_leader_info_s UF_DRF_leader_info_t,
                                    *UF_DRF_leader_info_p_t;
/*****************************************************************
 This is a structure to hold information in label
*****************************************************************/
struct UF_DRF_label_info_s
{
        int                          num_text; /* number of text block  */
        UF_DRF_draft_aid_text_info_t *text_info; /*<len:num_text> text information. See
                                            UF_DRF_draft_aid_text_info_t
                                        */
        int                          num_leaders; /* number of leaders     */
        UF_DRF_leader_info_t         *leader_info; /*<len:num_leaders> leader information. See
                                         UF_DRF_leader_info_t
                                        */
        int                          num_arrows; /* number of arrowheads */
        UF_DRF_arrow_info_t          *arrow_info; /*<len:num_arrows> arrowhead information . See
                                            UF_DRF_arrow_info_t
                                        */
};
typedef struct UF_DRF_label_info_s UF_DRF_label_info_t,
                                   *UF_DRF_label_info_p_t;
/*****************************************************************
 This is a structure to hold information in ID Symbol

*****************************************************************/
struct UF_DRF_id_symbol_info_s
{
        double                       size;
        int                          num_text;    /* number of text block  */
        UF_DRF_draft_aid_text_info_t *text_info;  /* <len:num_text> text information      */
        int                          num_leaders; /* number of leaders     */
        UF_DRF_leader_info_t         *leader_info;/* leader information    */
        int                          num_arrows;  /* number of arrowheads */
        UF_DRF_arrow_info_t          *arrow_info; /* <len:num_arrows> arrowhead information */
};
typedef struct UF_DRF_id_symbol_info_s UF_DRF_id_symbol_info_t,
                                       *UF_DRF_id_symbol_info_p_t;
/*****************************************************************
 This is a structure to hold information in GD&T Symbol
*****************************************************************/
struct UF_DRF_gdt_symbol_info_s
{
    int                          num_text; /* number of text block */
        UF_DRF_draft_aid_text_info_t *text_info; /*<len:num_text> text information     */
        int                          num_leaders; /* number of leaders    */
        UF_DRF_leader_info_t         *leader_info; /*<len:num_leaders> leader information. See
                                             UF_DRF_leader_info_t
                                         */
        int                          num_arrows; /* number of arrowheads */
    UF_DRF_arrow_info_t          *arrow_info; /* <len:num_arrows>arrowhead information. See
                                             UF_DRF_arrow_info_t
                                         */
} ;
typedef struct UF_DRF_gdt_symbol_info_s UF_DRF_gdt_symbol_info_t,
                                        *UF_DRF_gdt_symbol_info_p_t;
/****************************************************************
 This is a structure to hold information for dimension lines
*****************************************************************/
struct UF_DRF_dim_line_info_s
{
        UF_DRF_draft_aid_line_t      *line_pnts; /* dimension lines end
                                           points                */
        int                          num_assoc_objs; /* number of associated
                                           objects               */
        UF_DRF_assoc_info_t          *assoc_objs; /* <len:num_assoc_objs>leader assoc object tag
                                           type, and modifier    */
} ;
typedef struct UF_DRF_dim_line_info_s UF_DRF_dim_line_info_t,
                                      *UF_DRF_dim_line_info_p_t;
/*****************************************************************
 This is a structure to hold information in dimension
*****************************************************************/
struct UF_DRF_dim_info_s
{
        int                          num_text; /* number of text block */
        UF_DRF_draft_aid_text_info_t *text_info; /* <len:num_text>text information. See
                                             UF_DRF_draft_aid_text_info_t
                                         */
        int                          num_lines; /* number of dimension
                                            lines                */
        UF_DRF_dim_line_info_t       *dim_line_info; /*<len:num_lines> dimension line info. See
                                             UF_DRF_dim_line_info_t
                                         */
        int                          num_arcs; /* number of arcs       */
        UF_DRF_arc_info_t            *arc_info; /* <len:num_arcs>arc information. See
                                             UF_DRF_arc_info_t
                                         */
        int                          num_arrows; /* number of arrowheads */
        UF_DRF_arrow_info_t          *arrow_info; /* <len:num_arrows>arrowhead information. See
                                             UF_DRF_arrow_info_t
                                         */
} ;
typedef struct UF_DRF_dim_info_s UF_DRF_dim_info_t, *UF_DRF_dim_info_p_t;

/***************************************************************************
 *  These are the valid settings for appended text location
 ***************************************************************************/
enum UF_DRF_appended_text_location_e{
    UF_DRF_APPENDED_TEXT_BEFORE,    /* Appended text is Before the dimension */
    UF_DRF_APPENDED_TEXT_AFTER,     /* Appended text is After the dimension  */
    UF_DRF_APPENDED_TEXT_ABOVE,     /* Appended text is Above the dimension  */
    UF_DRF_APPENDED_TEXT_BELOW      /* Appended text is Below the dimension  */
};
typedef enum UF_DRF_appended_text_location_e UF_DRF_appended_text_location_t;

/*****************************************************************************
  This is a structure to hold dimension appended text at a particular location
 ****************************************************************************/
struct UF_DRF_appended_text_s
{
        UF_DRF_appended_text_location_t location; /* appended text location */
        int num_lines;                  /* number of lines of appended text */
        char **text;                    /* <len:num_lines> appended text array */
};
typedef struct UF_DRF_appended_text_s UF_DRF_appended_text_t,
                                      *UF_DRF_appended_text_p_t;

/*****************************************************************
 This is a structure to hold information in centerlines
*****************************************************************/
struct UF_DRF_centerline_info_s
{
        int                          num_lines; /* number of centerline
                                            lines                */
        UF_DRF_draft_aid_line_t      *line_info; /* <len:num_lines> centerline line info. See
                                             UF_DRF_draft_aid_line_t
                                         */
        int                          num_arcs; /* number of arcs       */
        UF_DRF_arc_info_t            *arc_info; /* <len:num_arcs> arc information. See
                                             UF_DRF_arc_info_t
                                         */
        int                          num_assoc_objs; /* number of assoc object*/
        UF_DRF_assoc_info_t          *assoc_objs; /*<len:num_assoc_objs> associated object tag,
                                           type, and modifier. See
                                            UF_DRF_assoc_info_t
                                        */
} ;
typedef struct UF_DRF_centerline_info_s UF_DRF_centerline_info_t,
                                        *UF_DRF_centerline_info_p_t;
/*****************************************************************
 Ordinate dimension margin types
*****************************************************************/
enum UF_DRF_orddim_margin_type_e
{
        UF_DRF_ORDHORIZONTAL_MARGIN, /* Horizontal ordinate margin */
        UF_DRF_ORDVERTICAL_MARGIN    /* Vertical ordinate margin */
} ;
typedef enum UF_DRF_orddim_margin_type_e UF_DRF_orddim_margin_type_t;
/*****************************************************************
 Ordinate dimension origin name display type
*****************************************************************/
enum UF_DRF_ordorigin_display_type_e
{
        UF_DRF_ORDORIGIN_UD_SYMBOL,     /* User-Defined symbol */
        UF_DRF_ORDORIGIN_HOR_VER_DIM,    /* Horizontal and vertical
                                            dimensions */
        UF_DRF_ORDORIGIN_HORIZONTAL_DIM, /* Horizontal dimensions only */
        UF_DRF_ORDORIGIN_VERTICAL_DIM,   /* Vertical dimensions only */
        UF_DRF_ORDORIGIN_NAME            /* Ordinate origin name */
} ;
typedef enum UF_DRF_ordorigin_display_type_e UF_DRF_ordorigin_display_type_t;
/*****************************************************************
 Ordinate dimension arrow and line display types
*****************************************************************/
enum UF_DRF_ordarrow_line_type_e
{
        UF_DRF_ORDARROW_LINE_NO_DISPLAY, /* Don't display ordinate dimension
                                            arrow and dimension line */
        UF_DRF_ORDARROW_LINE_DISPLAY     /* Display ordinate dimension
                                            arrow and dimension line */
} ;
typedef enum UF_DRF_ordarrow_line_type_e UF_DRF_ordarrow_line_type_t;

/*****************************************************************
 Ordinate dimension dog leg display types
*****************************************************************/
enum UF_DRF_dogleg_type_e
{
        UF_DRF_ORDDIMENSION_NO_DOGLEG = 1, /* Ordinate dimension without
                                              dog leg */
        UF_DRF_ORDDIMENSION_DOGLEG         /* Ordinate dimension with dog leg */
} ;
typedef enum UF_DRF_dogleg_type_e UF_DRF_dogleg_type_t;
/****************************************************************
 Ordinate dimension positive quadrant
*****************************************************************/
enum UF_DRF_quadrant_type_e
{
        UF_DRF_QUADRANT_ONE = 1, /* Positive quadrant number one */
        UF_DRF_QUADRANT_TWO,     /* Positive quadrant number two */
        UF_DRF_QUADRANT_THREE,   /* Positive quadrant number three */
        UF_DRF_QUADRANT_FOUR,    /* Positive quadrant number four */
        UF_DRF_QUADRANT_FIVE     /* Positive quadrant number five */
} ;
typedef enum UF_DRF_quadrant_type_e UF_DRF_quadrant_type_t;
/****************************************************************************
 *
 *           Control display of text above the leader stub.
 *  This option applies to Labels.
 *  It also applies to radial type dimensions (radius, diameter, hole,
 *  concentric circle, folded radius) when the Text Alignment is Horizontal
 *  or By Angle. Currently, only options UF_DRF_NO_TEXT_ABOVE_LEADER and
 *  UF_DRF_LEADER_BOTTOM_TEXT_MAX are valid for dimensions.
 *  All options except the first display the text above the leader stub.
 *  Options with 'BOTTOM' display the leader stub below the bottom line of
 *  text.  Options with 'TOP' display the leader stub below the top line of
 *  text.
 *  Options with 'UNDERLINE' will underline all other lines of text.
 *  Options with 'MAX' will extend the stub and optional underlines to the
 *  maximum text length. For options without 'MAX' the stub and optional
 *  underlines will be extended to the length of the text line it is under.
 *
 ****************************************************************************/
enum UF_DRF_text_above_leader_e
{
    UF_DRF_NO_TEXT_ABOVE_LEADER,
    UF_DRF_LEADER_BOTTOM_TEXT_MAX,
    UF_DRF_LEADER_BOTTOM_TEXT_MAX_UNDERLINE,
    UF_DRF_LEADER_BOTTOM_TEXT,
    UF_DRF_LEADER_BOTTOM_TEXT_UNDERLINE,
    UF_DRF_LEADER_TOP_TEXT_MAX,
    UF_DRF_LEADER_TOP_TEXT_MAX_UNDERLINE,
    UF_DRF_LEADER_TOP_TEXT,
    UF_DRF_LEADER_TOP_TEXT_UNDERLINE
} ;
typedef enum UF_DRF_text_above_leader_e UF_DRF_text_above_leader_t;
/*****************************************************************
 This is a structure to hold in folded radius information
*****************************************************************/
struct UF_DRF_folded_radius_info_s
{
        double  fold_location[3]; /* Fold location in wcs coordinates
                                          fold_location [0] = x  value
                                          fold_location [1] = y  value
                                          fold_location [2] = z  value
                                  */
        double  fold_angle;       /* Folded  angle in degrees */
        double  fold_offset;      /* Folded  relative distance */
}  ;
typedef struct UF_DRF_folded_radius_info_s UF_DRF_foldedradius_dim_info_t,
                                          *UF_DRF_folded_radius_info_p_t;
/*****************************************************************
 This is a structure to hold ordinate dimension origin display
 information
*****************************************************************/
struct UF_DRF_orddisp_info_s
{
        UF_DRF_quadrant_type_t          quadrant;     /* positive quadrant */
        UF_DRF_ordorigin_display_type_t name_display; /* Ordinate dimension
                                        origin name display type. See
                                         UF_DRF_ordorigin_display_type_t
                                                      */
        char                            origin_name[MAX_LINE_BUFSIZE]; /* The name of origin */
        UF_DRF_ordarrow_line_type_t     arr_display;  /* Ordinate dimension
                                        arrow and line display types. See
                                         UF_DRF_ordarrow_line_type_t
                                                      */
        int                             symfont;      /* Symbol font */
} ;
typedef struct UF_DRF_orddisp_info_s UF_DRF_orddisp_info_t,
                                     *UF_DRF_orddisp_info_p_t;
/****************************************************************
 This is a structure to hold ordinate dimension origin
 dog leg information
*****************************************************************/
struct UF_DRF_dogleg_info_s
{
        UF_DRF_dogleg_type_t          dogleg_type;   /* Dog leg type. See
                                                      UF_DRF_dogleg_type_t
                                                     */
        double                        dogleg_angle;  /* Dog leg angle in degrees
                                                     */
        double                        dogleg_distance; /* Dog leg distance */
} ;
typedef struct UF_DRF_dogleg_info_s UF_DRF_dogleg_info_t,
                                    *UF_DRF_dogleg_info_p_t;
/*****************************************************************
 This is a structure to hold ordinate dimension information
*****************************************************************/
struct UF_DRF_orddimension_info_s
{
        UF_DRF_dim_info_t             *orddim;
        UF_DRF_orddisp_info_t         orddisp;
        UF_DRF_dogleg_info_t          dogleg;
        double                        dogleg_distance;
        UF_DRF_orddim_margin_type_t   margin_type;
        double                        margin_offset;
} ;
typedef struct UF_DRF_orddimension_info_s UF_DRF_orddimension_info_t,
                                          *UF_DRF_orddimension_info_p_t;
/*************************************************************************
   Assorted Parts Arc Data
  *************************************************************************/
struct UF_DRF_assortpart_arc_s
{
    int    num_arcs;          /* number of arcs                          */
    int    *num_arc_segments; /* <len:num_arcs> array of number of arc segments per arc */
    double *arc_data;         /* arc data
                                 [0,1] 2d arc center in coordinates
                                       of annotation
                                 [2]   arc radius
                                 [3,4] start and end angles in radians
                                       .
                                       .
                                 [2*num_arc_segments+1,
                                  2*num_arc_segments+2] segment angles */
} ;
typedef struct UF_DRF_assortpart_arc_s UF_DRF_assortpart_arc_t,
                                      *UF_DRF_assortpart_arc_p_t;
/*************************************************************************
   Assorted Parts Arrow Data
  *************************************************************************/
struct UF_DRF_assortpart_arrow_s
{
    int    num_arrows;         /* number of arrows                       */
    int    *arrowhead_subtype; /* <len:num_arrows> array of arrowhead subtypes per arrow
                                  1 = CLOSED
                                  2 = OPEN
                                  3 = ARCH CROSS
                                  4 = DOT
                                  5 = ORIGIN SYMBOL
                                  6 = NONE                            */
    double *arrow_data;        /* array of arrow data
                                  [0,1] 2d arrow origin in coordinates
                                        of annotation
                                  [2]   arrow angle in radians         */
} ;
typedef struct UF_DRF_assortpart_arrow_s UF_DRF_assortpart_arrow_t,
                                        *UF_DRF_assortpart_arrow_p_t;
/*************************************************************************
   Assorted Parts Line Data
  *************************************************************************/
struct UF_DRF_assortpart_line_s
{
    int    num_lines;          /* number of lines                           */
    int    *num_line_segments; /* <len:num_lines> array of number of line segments per line */
    double *line_data;         /* 2d array of line points in coordinates
                                  of annotation                           */
} ;
typedef struct UF_DRF_assortpart_line_s UF_DRF_assortpart_line_t,
                                       *UF_DRF_assortpart_line_p_t;
/*************************************************************************
   Assorted Parts Text Data
  *************************************************************************/
struct UF_DRF_assortpart_text_s
{
    int    num_text;        /* number of text components                   */
    int    *num_lines_text; /* <len:num_text> array of number of lines per text component */
    char   **text;          /* <len:num_text> array of text strings                       */
    double *text_origin;    /* <len:num_text> array of 2d origins of text components in
                               coordinates of annotation                 */
} ;
typedef struct UF_DRF_assortpart_text_s UF_DRF_assortpart_text_t,
                                        *UF_DRF_assortpart_text_p_t;
/*************************************************************************
   Symbol Create Data
  *************************************************************************/
struct UF_DRF_symbol_create_data_s
{
    char   symbol_name[SYMBOL_NAME_SIZE + 1]; /* symbol name (8 characters
                                              maximum)
                                              */
    double angle;                             /* angle (in degrees)
                                              */
    double length;                            /* length
                                              */
    double height;                            /* height
                                              */
    tag_t  anchor_tag;                        /* point object representing the
                                              location of the anchor point
                                              */
} ;
typedef struct UF_DRF_symbol_create_data_s UF_DRF_symbol_create_data_t,
                                          *UF_DRF_symbol_create_data_p_t;

/*************************************************************************
   Symbol Data
  *************************************************************************/
struct UF_DRF_symbol_data_s
{
    double anchor_point[3]; /* model space x,y,z of anchor point      */
    double orient_point[3]; /* model space x,y,z of orientation point */
    double angle;           /* symbol angle (in degrees)              */
    double length;          /* symbol length                          */
    double height;          /* symbol height                          */
    tag_t  symbol_font_tag; /* symbol font object tag                 */
} ;
typedef struct UF_DRF_symbol_data_s UF_DRF_symbol_data_t,
                                   *UF_DRF_symbol_data_p_t;

/* UF_DRF_tolerance_type_t specifies the tolerance type for a dimension */
enum UF_DRF_tolerance_type_e
{
     UF_DRF_NO_TOLERANCE = 1,
     UF_DRF_LIMIT_ONE_LINE,
     UF_DRF_LIMIT_TWO_LINES,
     UF_DRF_BILATERAL_ONE_LINE,
     UF_DRF_BILATERAL_TWO_LINES,
     UF_DRF_UNILATERAL_ABOVE,
     UF_DRF_UNILATERAL_BELOW,
     UF_DRF_BASIC_TOL,
     UF_DRF_REFERENCE_TOL,
     UF_DRF_LIMIT_LARGER_FIRST,
     UF_DRF_LIMIT_LARGER_BELOW,
     UF_DRF_NOT_TO_SCALE_TOL,     
     UF_DRF_DIAMETER_REFERENCE_TOL,
     UF_DRF_LIMIT_AND_FIT,
     UF_DRF_BASIC_DIM_NOT_TO_SCALE_TOL,
     UF_DRF_MAX_NUM_TOL
} ;
typedef enum UF_DRF_tolerance_type_e UF_DRF_tolerance_type_t;

/* UF_DRF_text_arrow_placement_t specifies the type of placement for the
   dimension: inferred or manual. */
enum UF_DRF_text_arrow_placement_e
{
     UF_DRF_AUTO_PLACEMENT = 1,
     UF_DRF_PLACEMENT_MANUAL_ARROWS_IN,
     UF_DRF_PLACEMENT_MANUAL_ARROWS_OUT,
     UF_DRF_PLACEMENT_MANUAL_ARROWS_SAME_DIRECTION 
};
typedef enum UF_DRF_text_arrow_placement_e UF_DRF_text_arrow_placement_t;

/* UF_DRF_dimension_extension_line_t specifies whether extension lines are to
   be displayed on each side of the dimension*/
enum UF_DRF_extension_line_display_e
{
     UF_DRF_DISPLAY_TWO_EXT_LINES = 1,
     UF_DRF_DISPLAY_EXT_LINE_1,
     UF_DRF_DISPLAY_EXT_LINE_2,
     UF_DRF_DISPLAY_NO_EXT_LINE
} ;
typedef enum UF_DRF_extension_line_display_e UF_DRF_extension_line_display_t;

/* UF_DRF_dimension_extension_line_t specifies whether arrows are to be
displayed on each side of the dimension
*/
enum UF_DRF_arrow_display_e
{
     UF_DRF_DISPLAY_TWO_ARROWS = 1,
     UF_DRF_DISPLAY_ARROW_1,
     UF_DRF_DISPLAY_ARROW_2,
     UF_DRF_DISPLAY_NO_ARROWS
};
typedef enum UF_DRF_arrow_display_e UF_DRF_arrow_display_t;

/* UF_DRF_dimension_orientation_t specifies the alignment of text relative to
the dimension orientation.  */
enum UF_DRF_dimension_orientation_e
{
     UF_DRF_DIMENSION_TEXT_HORIZONTAL = 1,
     UF_DRF_DIMENSION_TEXT_ALIGNED,
     UF_DRF_DIMENSION_TEXT_OVER_DIMENSION_LINE,
     UF_DRF_DIMENSION_TEXT_BY_ANGLE,
     UF_DRF_DIMENSION_TEXT_PERPENDICULAR,
     UF_DRF_DIMENSION_TEXT_SPLIT_BY_DIMENSION_LINE
} ;
typedef enum UF_DRF_dimension_orientation_e UF_DRF_dimension_orientation_t;

enum UF_DRF_fraction_denominator_e
{
    UF_DRF_FRACTION_DENOM_1  = 1,
    UF_DRF_FRACTION_DENOM_2  = 2,
    UF_DRF_FRACTION_DENOM_4  = 4,
    UF_DRF_FRACTION_DENOM_8  = 8,
    UF_DRF_FRACTION_DENOM_16 = 16,
    UF_DRF_FRACTION_DENOM_32 = 32,
    UF_DRF_FRACTION_DENOM_64 = 64
};
typedef enum  UF_DRF_fraction_denominator_e UF_DRF_fraction_denominator_t;


/* UF_DRF_linear_units_t specifies the supported types of linear units. */
enum UF_DRF_linear_units_e
{
     UF_DRF_MILLIMETERS = 1,
     UF_DRF_METERS,
     UF_DRF_INCHES,
     UF_DRF_ARCHITECTURAL_FEET_INCHES,
     UF_DRF_ENGINEERING_FEET_INCHES
} ;
typedef enum UF_DRF_linear_units_e UF_DRF_linear_units_t;

/* UF_DRF_decimal_point_character_t specifies the decimal point character,
period or comma */
enum UF_DRF_decimal_point_character_e
{
     UF_DRF_DECIMAL_POINT_PERIOD = 1,
     UF_DRF_DECIMAL_POINT_COMMA
} ;
typedef enum UF_DRF_decimal_point_character_e UF_DRF_decimal_point_character_t;

/* UF_DRF_tolerance_location_t specifies the location of the tolerance value
relative to the dimension text */
enum UF_DRF_tolerance_placement_e
{
     UF_DRF_TOLERANCE_BELOW_DIMENSION = 1,
     UF_DRF_TOLERANCE_AFTER_DIMENSION,
     UF_DRF_TOLERANCE_ABOVE_DIMENSION
} ;
typedef enum UF_DRF_tolerance_placement_e UF_DRF_tolerance_placement_t;

/* UF_DRF_angular_format_t specifies the supported formats for angular
display. */
enum UF_DRF_angular_units_e
{
     UF_DRF_FRACTIONAL_DEGREES = 1,
     UF_DRF_WHOLE_DEGREES,
     UF_DRF_DEGREES_MINUTES,
     UF_DRF_DEGREES_MINUTES_SECONDS
} ;
typedef enum UF_DRF_angular_units_e UF_DRF_angular_units_t;

/* suppress zeros for angular dimension only */
enum UF_DRF_angular_suppress_zeros_e
{
    UF_DRF_ANG_DISPLAY_ZEROS = 1,        /* Display all zeros in angular dimension for both nominal and tolerance */
    UF_DRF_ANG_SUPPRESS_LEADING_ZEROS,   /* Suppress leading zeros in angular dimension for both nominal and tolerance */
    UF_DRF_ANG_SUPPRESS_ANY_ZEROS,       /* Suppress any zeros in angular dimension for both nominal and tolerance */
    UF_DRF_ANG_SUPPRESS_TRAILING_ZEROS   /* Suppress trailing zeros for angular dimension for both its nominal and tolerance */
} ;
typedef enum UF_DRF_angular_suppress_zeros_e UF_DRF_angular_suppress_zeros_t;


/* UF_DRF_fraction_type_t specifies the supported format for dimension text. */
enum UF_DRF_fraction_type_e
{
    UF_DRF_DECIMAL                 = 1,
    UF_DRF_HALF_SIZE_FRACTION      = 2,
    UF_DRF_TWO_THIRD_SIZE_FRACTION = 3,
    UF_DRF_FULL_SIZE_FRACTION      = 4
};
typedef enum UF_DRF_fraction_type_e UF_DRF_fraction_type_t;



/* UF_DRF_dual_dimension_format_t specifies the supported formats for dual
dimension display. */
enum UF_DRF_dual_dimension_format_e
{
     UF_DRF_DUAL_DIMENSION_BELOW = 1,
     UF_DRF_DUAL_DIMENSION_AFTER,
     UF_DRF_DUAL_DIMENSION_ABOVE,
     UF_DRF_DUAL_DIMENSION_BEFORE,
     UF_DRF_NO_DUAL_DIMENSION
} ;
typedef enum UF_DRF_dual_dimension_format_e UF_DRF_dual_dimension_format_t;

#define UF_DRF_DIAMETER_RADIUS_SYMBOL_MAX_NCHARS    27
#define UF_DRF_DIAMETER_RADIUS_SYMBOL_MAX_BUFSIZE   NX_BUFSIZE(UF_DRF_DIAMETER_RADIUS_SYMBOL_MAX_NCHARS)

/*  */
#define UF_DRF_DIAMETER_RADIUS_SYMBOL_MAX_LENGTH         (UF_DRF_DIAMETER_RADIUS_SYMBOL_MAX_BUFSIZE-1)
/*  */

/* UF_DRF_diameter_symbol_t specifies the symbol type for a diameter
dimension symbol*/
enum UF_DRF_diameter_symbol_e
{
     UF_DRF_DIAMETER_USE_DIA = 1,
     UF_DRF_STANDARD_DIAMETER_SYMBOL,
     UF_DRF_USER_DEFINED_DIAMETER_SYMBOL,
     UF_DRF_SPHERICAL_DIAMETER_SYMBOL
} ;
typedef enum UF_DRF_diameter_symbol_e UF_DRF_diameter_symbol_t;

/* UF_DRF_radius_symbol_t specifies the symbol type for a radial dimension
symbol*/
enum UF_DRF_radius_symbol_e
{
     UF_DRF_RADIUS_USE_R = 1,
     UF_DRF_RADIUS_USE_RAD,
     UF_DRF_USER_DEFINED_RADIUS_SYMBOL,
     UF_DRF_RADIUS_USE_SR,
     UF_DRF_RADIUS_USE_CR
} ;
typedef enum UF_DRF_radius_symbol_e UF_DRF_radius_symbol_t;

/* UF_DRF_diameter_radius_placement_t specifies the diameter or radius
symbol placement */
enum UF_DRF_diameter_radius_placement_e
{
     UF_DRF_DIA_RAD_BELOW = 1,
     UF_DRF_DIA_RAD_AFTER,
     UF_DRF_DIA_RAD_ABOVE,
     UF_DRF_DIA_RAD_BEFORE,
     UF_DRF_DIA_RAD_OMIT
} ;
typedef enum UF_DRF_diameter_radius_placement_e
UF_DRF_diameter_radius_placement_t;

/* UF_DRF_area_fill_material_t specifies the material to be represented
   for area fill */
enum UF_DRF_area_fill_material_e
{
     UF_DRF_CORK_FELT           = (int)UF_DRF_corkfeltfiber,
     UF_DRF_SOUND_INSULATION    = (int)UF_DRF_soundinsulation,
     UF_DRF_CONCRETE            = (int)UF_DRF_concrete,
     UF_DRF_EARTH               = (int)UF_DRF_earth,
     UF_DRF_ROCK                = (int)UF_DRF_rock,
     UF_DRF_SAND                = (int)UF_DRF_sand,
     UF_DRF_LIQUIDS             = (int)UF_DRF_liquids,
     UF_DRF_WOOD_ACROSS_GRAIN   = (int)UF_DRF_woodacrossgrain,
     UF_DRF_WOOD_ALONG_GRAIN    = (int)UF_DRF_woodwithgrain,
     UF_DRF_SOLID_FILL
} ;
typedef enum UF_DRF_area_fill_material_e UF_DRF_area_fill_material_t;

/* UF_DRF_section_line_display_t specifies the type of section line display */
enum UF_DRF_section_line_display_e
{
     UF_DRF_NO_SECTION_LINE_DISPLAY,
     UF_DRF_ANSI_SECTION_LINE_DISPLAY,
     UF_DRF_ISO_SECTION_LINE_DISPLAY,
     UF_DRF_ISO128_SECTION_LINE_DISPLAY,
     UF_DRF_JIS_SECTION_LINE_DISPLAY,
     UF_DRF_GB_SECTION_LINE_DISPLAY
} ;
typedef enum UF_DRF_section_line_display_e UF_DRF_section_line_display_t;

/* UF_DRF_section_line_arrowhead_t specifies the type of arrowhead for
   section line display */
enum UF_DRF_section_line_arrowhead_e
{
     UF_DRF_SECTION_LINE_ARROWHEAD_OPEN = 1,
     UF_DRF_SECTION_LINE_ARROWHEAD_CLOSED,
     UF_DRF_SECTION_LINE_ARROWHEAD_FILLED
} ;
typedef enum UF_DRF_section_line_arrowhead_e
              UF_DRF_section_line_arrowhead_t;

/* UF_DRF_vertical_text_just_t specifies the supported vertical justification
   options */
enum UF_DRF_vertical_text_just_e
{
    UF_DRF_TEXT_TOP = 1,
    UF_DRF_TEXT_MIDDLE = 2,
    UF_DRF_TEXT_BOTTOM = 3
} ;
typedef enum UF_DRF_vertical_text_just_e UF_DRF_vertical_text_just_t;

/* UF_DRF_text_just_t specifies the supported horizontal text justifcation
   options */
enum UF_DRF_text_just_e
{
    UF_DRF_TEXT_LEFT   = 1,
    UF_DRF_TEXT_CENTER = 2,
    UF_DRF_TEXT_RIGHT  = 3
};
typedef enum UF_DRF_text_just_e UF_DRF_text_just_t;

/* UF_DRF_align_position_t specifies the site locations in the text box which
   can be used to locate a drafting object */
enum UF_DRF_align_position_e
{
    UF_DRF_ALIGN_TOP_LEFT      = 1,
    UF_DRF_ALIGN_TOP_CENTER    = 2,
    UF_DRF_ALIGN_TOP_RIGHT     = 3,
    UF_DRF_ALIGN_MID_LEFT      = 4,
    UF_DRF_ALIGN_MID_CENTER    = 5,
    UF_DRF_ALIGN_MID_RIGHT     = 6,
    UF_DRF_ALIGN_BOTTOM_LEFT   = 7,
    UF_DRF_ALIGN_BOTTOM_CENTER = 8,
    UF_DRF_ALIGN_BOTTOM_RIGHT  = 9
} ;
typedef enum UF_DRF_align_position_e UF_DRF_align_position_t;

typedef enum
{
    UF_DRF_STACK_ALIGN_ABOVE = 0,
    UF_DRF_STACK_ALIGN_BELOW,
    UF_DRF_STACK_ALIGN_LEFT,
    UF_DRF_STACK_ALIGN_RIGHT
} UF_DRF_stack_align_position_t;

/* UF_DRF_line_width_t specifies the supported line widths 
   Extended enum and validation condition to support new line widths */
enum UF_DRF_line_width_e
{
     UF_DRF_NORMAL =  1,
     UF_DRF_THICK  =  2,
     UF_DRF_THIN   =  3,

     UF_DRF_THICKNESS_ONE = 6,
     UF_DRF_THICKNESS_TWO = 7,
     UF_DRF_THICKNESS_THREE = 8,
     UF_DRF_THICKNESS_FOUR = 9,
     UF_DRF_THICKNESS_FIVE = 10,
     UF_DRF_THICKNESS_SIX = 11,
     UF_DRF_THICKNESS_SEVEN = 12,
     UF_DRF_THICKNESS_EIGHT = 13,
     UF_DRF_THICKNESS_NINE = 14
} ;
typedef enum UF_DRF_line_width_e UF_DRF_line_width_t;

#define  UF_DRF_MIN_NEW_WIDTH    (UF_DRF_THICKNESS_ONE)

#define UF_DRF_is_valid_width( width ) \
    ( (((width) >= (int)UF_DRF_NORMAL) && ((width) <= (int)UF_DRF_THIN)) || \
      (((width) >= (int)UF_DRF_MIN_NEW_WIDTH) && ((width) <= (int)UF_DRF_THICKNESS_NINE)) )

/*  Add some routines to map back and forth between DRF line width
 *  and the OBJ width.
 */
#define UF_DRF_MAP_DRF_LINE_WIDTH_TO_OBJ_WIDTH(width)   ((width) - 1)
#define UF_DRF_MAP_OBJ_WIDTH_TO_DRF_LINE_WIDTH(width)   ((width) + 1)

/* UF_DRF_cfw_t specifies the color, font, and width for a line */
struct UF_DRF_cfw_s
{
     int                 color; /* Color of the line. */
     int                 font;  /* Font of the line. */
     UF_DRF_line_width_t width; /* Width of the line. */
} ;
typedef struct UF_DRF_cfw_s UF_DRF_cfw_t, *UF_DRF_cfw_p_t;

/* UF_DRF_text_cfw_t specifies the color, font, and width for a text */
struct UF_DRF_text_cfw_s
{
    int                  color; /* Text color */
    int                  font;  /* Text font */
    UF_DRF_line_width_t  width; /* Text weight */
};
typedef struct UF_DRF_text_cfw_s UF_DRF_text_cfw_t, *UF_DRF_text_cfw_p_t;
/******************************************************************************
 * UF_DRF_dimension_preferences_t specifies annotation preferences
 * that apply only to dimensions
 *****************************************************************************/
struct UF_DRF_dimension_preferences_s
{
     UF_DRF_tolerance_type_t
             tolerance_type;
     double  upper_tolerance_english;    /* inches */
     double  lower_tolerance_english;    /* inches */
     double  upper_tolerance_metric;     /* millimeters */
     double  lower_tolerance_metric;     /* millimeters */
     double  upper_tolerance_deg;        /* not implemented */
     double  lower_tolerance_deg;        /* not implemented */
     int     dimension_value_dp;         /* number of decimal places for primary
                                            dimension value */
     int     tolerance_value_dp;         /* number of decimal places for primary
                                            tolerance value */
     int     dual_dimension_value_dp;    /* number of decimal places for
                                            secondary dimension value */
     int     dual_tolerance_value_dp;    /* number of decimal places for
                                            secondary tolerance value */
     int     angular_dimension_value_dp; /* not implemented */
     int     angular_tolerance_value_dp; /* not implemented */
     UF_DRF_fraction_denominator_t
             dim_fraction_denominator;   /* fractional precision for primary
                                            dimension and tolerance value */
     UF_DRF_fraction_denominator_t
             dual_fraction_denominator;  /* fractional precision for secondary
                                            primary and tolerance value */
     UF_DRF_text_arrow_placement_t
             text_arrow_placement;       /* automatic placement or manual
                                            placement with arrows in or out */
     UF_DRF_extension_line_display_t
             extension_line_display;     /* number and side for extension
                                            line(s) */
     UF_DRF_arrow_display_t
             arrow_display;              /* number and side for arrow(s) */
     logical line_between_arrows;        /* TRUE if a line is to be displayed
                                            between arrows */
     UF_DRF_dimension_orientation_t
             orientation;                /* orientation of dimension text */
     double  text_angle;                 /* angle of text if orientation
                                            is UF_DRF_DIMENSION_TEXT_BY_ANGLE */
     double baseline_offset;             /* baselinen dimension offset value */
     double chain_offset;                /* chain dimension offset value */
     UF_DRF_narrow_dimension_info_t
             narrow_dimension_data;      /* Narrow dimension preferences */
     UF_DRF_arrowhead_and_fill_type_t
       narrow_dimension_arrowhead_type;  /* Narrow dimension arrowhead type */
     UF_DRF_chamfer_dimension_data_t
       chamfer_dimension_data;           /* chamfer dimension data */
    UF_DRF_inspection_type_t dim_inspection_type;      /* dimension inspection type preference */
    UF_DRF_reference_symbol_type_t dim_reference_type; /* dimension reference type preference */
    UF_DRF_trim_dim_line_style_t  trim_dim_line;       /* Whether to trim dimension line when text cross both extension lines */
};
typedef struct UF_DRF_dimension_preferences_s UF_DRF_dimension_preferences_t,
               *UF_DRF_dimension_preferences_p_t;
/******************************************************************************
 * UF_DRF_dimension_preferences1_t specifies annotation preferences
 * that apply only to dimensions
 *****************************************************************************/
struct UF_DRF_dimension_preferences1_s
{
     UF_DRF_tolerance_type_t
             tolerance_type;
     double  upper_tolerance_english;    /* inches */
     double  lower_tolerance_english;    /* inches */
     double  upper_tolerance_metric;     /* millimeters */
     double  lower_tolerance_metric;     /* millimeters */
     double  upper_tolerance_deg;        /* not implemented */
     double  lower_tolerance_deg;        /* not implemented */
     int     dimension_value_dp;         /* number of decimal places for primary
                                            dimension value */
     int     tolerance_value_dp;         /* number of decimal places for primary
                                            tolerance value */
     int     dual_dimension_value_dp;    /* number of decimal places for
                                            secondary dimension value */
     int     dual_tolerance_value_dp;    /* number of decimal places for
                                            secondary tolerance value */
     int     angular_dimension_value_dp; /* not implemented */
     int     angular_tolerance_value_dp; /* not implemented */
     UF_DRF_fraction_denominator_t
             dim_fraction_denominator;   /* fractional precision for primary
                                            dimension and tolerance value */
     UF_DRF_fraction_denominator_t
             dual_fraction_denominator;  /* fractional precision for secondary
                                            primary and tolerance value */
     UF_DRF_text_arrow_placement_t
             text_arrow_placement;       /* automatic placement or manual
                                            placement with arrows in or out */
     UF_DRF_extension_line_display_t
             extension_line_display;     /* number and side for extension
                                            line(s) */
     UF_DRF_arrow_display_t
             arrow_display;              /* number and side for arrow(s) */
     logical line_between_arrows;        /* TRUE if a line is to be displayed
                                            between arrows */
     UF_DRF_dimension_orientation_t
             orientation;                /* orientation of dimension text */
     double  text_angle;                 /* angle of text if orientation
                                            is UF_DRF_DIMENSION_TEXT_BY_ANGLE */
     double baseline_offset;             /* baselinen dimension offset value */
     double chain_offset;                /* chain dimension offset value */
     UF_DRF_narrow_dimension_info_p_t
             narrow_dimension_data;      /* Narrow dimension preferences */
     UF_DRF_arrowhead_and_fill_type_t
       narrow_dimension_arrowhead_type;  /* Narrow dimension arrowhead type */
     UF_DRF_chamfer_dimension_data_p_t
       chamfer_dimension_data;           /* chamfer dimension data */
    UF_DRF_inspection_type_t dim_inspection_type;      /* dimension inspection type preference */
    UF_DRF_reference_symbol_type_t dim_reference_type; /* dimension reference type preference */
    UF_DRF_trim_dim_line_style_t  trim_dim_line;       /* Whether to trim dimension line when text cross both extension lines */
};
typedef struct UF_DRF_dimension_preferences1_s UF_DRF_dimension_preferences1_t,
               *UF_DRF_dimension_preferences1_p_t;

/*******************************************************************************
 * UF_DRF_line_arrow_preferences_t specifies the preferences that apply
 * to leaders, arrows and extension lines for both dimensions and
 * other annotations.
 ******************************************************************************/
struct UF_DRF_line_arrow_preferences_s
{
     UF_DRF_arrowhead_and_fill_type_t
             first_arrow_type;                      /* type and fill status for
                                                       first arrowhead */
     UF_DRF_arrowhead_and_fill_type_t
             second_arrow_type;                     /* type and fill status for
                                                        second arrowhead */
     UF_DRF_vertical_text_just_t
             leader_location;                       /* vertical text alignment
                                                       for leader */
     double  arrowhead_length;                      /* arrowhead length */
     double  arrowhead_included_angle;              /* arrowhead angle */
     double  dot_arrowhead_diameter;                /* dot diameter */
     double  stub_length;                           /* dogleg on label or
                                                       dimension leader */
     double  text_to_line_distance;                 /* distance from text to
                                                       arrow line or stub */
     double  line_past_arrow_distance;              /* distance an extension
                                                       line extends past point
                                                       of arrow */
     double  oblique_extension_line_angle;          /* extension line angle */
     double  first_pos_to_extension_line_distance;  /* distance from object
                                                       being dimensioned to the
                                                       start of 1st extension
                                                       line  or arc */
     double  second_pos_to_extension_line_distance; /* distance from object
                                                       being dimensioned to the
                                                       start of 2nd extension
                                                       line  or arc */
     double  datum_length_past_arrow;               /* length of the datum extension
                                                       line past it's arrow */
     double  text_over_stub_factor;                 /* text over stub spacing
                                                       factor. */

                    /* color, font, width */
     UF_DRF_cfw_t   first_extension_line_cfw;
     UF_DRF_cfw_t   first_arrowhead_cfw;
     UF_DRF_cfw_t   first_arrow_line_cfw;
     UF_DRF_cfw_t   second_extension_line_cfw;
     UF_DRF_cfw_t   second_arrowhead_cfw;
     UF_DRF_cfw_t   second_arrow_line_cfw;
     double         arrow_out_length_factor;
     double         allAroundSymbolSize;            /* size of all around symbol in leader */
};
typedef struct UF_DRF_line_arrow_preferences_s UF_DRF_line_arrow_preferences_t,
               *UF_DRF_line_arrow_preferences_p_t;

/************************************************************
 * UF_DRF_symbol_preferences_t specifies the preferences for
 * each NX symbol type.
 ***********************************************************/
struct UF_DRF_symbol_preferences_s
{
     double         id_symbol_size;
     UF_DRF_cfw_t   id_symbol_cfw;           /* color, font, width */
     UF_DRF_cfw_t   user_defined_symbol_cfw; /* color, font, width */
     UF_DRF_cfw_t   centerline_symbol_cfw;   /* font is not supported */
     UF_DRF_cfw_t   intersection_symbol_cfw; /* color, font, width */
     UF_DRF_cfw_t   target_symbol_cfw;       /* color, font, width */
     UF_DRF_cfw_t   gdt_symbol_cfw;          /* color, font, width */
};
typedef struct UF_DRF_symbol_preferences_s  UF_DRF_symbol_preferences_t,
               *UF_DRF_symbol_preferences_p_t;

/*****************************************************************************
 * UF_DRF_lettering_t specifies the lettering preferences for a single class
 * of lettering text.
 ***************************************************************************/
struct UF_DRF_lettering_s
{
     double       size;                    /* height of character */
     double       character_space_factor;  /* multiplier applied to fonts's
                                              standard character spacing */
     double       aspect_ratio;            /* ratio of length to height for
                                               a character */
     double       line_space_factor;       /* multiplier applied to font's
                                              standard line spacing */
     UF_DRF_text_cfw_t cfw;                /* color, font, width */
};
typedef struct UF_DRF_lettering_s UF_DRF_lettering_t, *UF_DRF_lettering_p_t;

/************************************************************************
 * UF_DRF_lettering_preferences_t specifies the lettering preferences for
 * dimension text, appended text, tolerance text, and general text.
 ***********************************************************************/
struct UF_DRF_lettering_preferences_s
{
     UF_DRF_align_position_t  align_position; /* one of nine site locations in
                                                 the text rectangle used to
                                                 place the text */
     UF_DRF_text_just_t       horiz_text_just;         /* horizontal text
                                                          justification */
     double                   gdt_frame_height_factor; /* GD&T frame height
                                                          factor */
     double                   angle;          /* angle for general text */
     UF_DRF_lettering_t       dimension_text; /* lettering preferences for
                                                 dimension text */
     UF_DRF_lettering_t       appended_text;  /* lettering preferences for
                                                 appended text */
     UF_DRF_lettering_t       tolerance_text; /* lettering preferences for
                                                 tolerance text */
     UF_DRF_lettering_t       general_text;   /* lettering preferences for
                                                  drafting aid text */
     double                   dim_dim_line_space_factor;  /* this controls spacing between bottom most piece of text on the dimension
                                                             and the dimension line when text orientation is
                                                             UF_DRF_DIMENSION_TEXT_OVER_DIMENSION_LINE. This factor is applied to the
                                                             dimension text character size to determine the spacing */
     double                   dim_app_text_space_factor;  /* controls spacing between before appended text and next piece of
                                                             dimension text to its right, and spacing between the after appended
                                                             text and next piece of dimension text to its left. This factor is
                                                             applied to the appended text character size to determine the spacing */
     double                   dim_tol_text_space_factor;  /* controls spacing between dimension main text and after tolerance text.
                                                             this factor is applied to the tolerance text character size to determine
                                                             the spacing */
};
typedef struct UF_DRF_lettering_preferences_s UF_DRF_lettering_preferences_t,
               *UF_DRF_lettering_preferences_p_t;

/***************************************************************************
 * UF_DRF_units_format_preferences_t specifies the preferences for display
 * of linear and angular dimensions and dual dimension format.
 * In v17.0, the data structure has changed. An element controlling the units
 * of the tolerance of angular dimension and an element controlling the zero
 * suppression for angular dimension have been added. The display leading
 * zeros option has been removed.
 **************************************************************************/
struct UF_DRF_units_format_preferences_s
{
     UF_DRF_linear_units_t
              dimension_linear_units;          /* linear units for primary
                                                  value */
     UF_DRF_fraction_type_t
              linear_fraction_type;            /* primary format -
                                                  decimal or fractional */
     UF_DRF_decimal_point_character_t
              decimal_point_character;         /* use period or comma for
                                                  decimal point */
     logical  display_trailing_zeros;          /* if TRUE, display zeros
                                                  trailing a significant digit
                                                  for dimension value */
     UF_DRF_tolerance_placement_t
              dimension_tolerance_placement;   /* placement of tolerance text
                                                  relative to dimension text */
     UF_DRF_angular_units_t
              dimension_angular_format;        /* use decimal or
                                                  degree [minute] [second]
                                                  format for angular nominal format only
                                                */
     UF_DRF_angular_units_t
              dim_angular_format_tolerance;    /* use decimal or
                                                  degree [minute] [second]
                                                  format for angular tolerance format only
                                                */
     UF_DRF_angular_suppress_zeros_t
              angular_suppress_zeros;          /* suppress zero options
                                                  display all zeros, or
                                                  suppress leading zeros, or
                                                  suppress any zeros, or
                                                  suppress trailing zeros for angular dimension only
                                               */
     UF_DRF_dual_dimension_format_t
              dual_dimension_format;           /* set no dual dimension or
                                                  specify placement of dual
                                                  dimension relative to
                                                  primary dimension */
     UF_DRF_linear_units_t
              dual_dimension_units;            /* linear units for secondary
                                                  value */
     UF_DRF_fraction_type_t
              dual_fraction_type;              /* secondary format -
                                                  decimal or fractional */
     logical  dual_convert_tolerance;          /* if TRUE, secondary tolerance
                                                  value will be computed from
                                                  primary tolerance value */
};
typedef struct UF_DRF_units_format_preferences_s
       UF_DRF_units_format_preferences_t, *UF_DRF_units_format_preferences_p_t;

/*******************************************************************************
 * UF_DRF_diameter_radius_preferences_t specifies annotation preferences
 *  that only apply to radial type dimensions
 *****************************************************************************/
struct UF_DRF_diameter_radius_preferences_s
{
     UF_DRF_diameter_symbol_t
           diameter_symbol_type;      /* standard diameter symbol or
                                         user-defined */
     char
     diameter_symbol[UF_DRF_DIAMETER_RADIUS_SYMBOL_MAX_BUFSIZE];
                                      /* text for user-defined diameter symbol*/
     UF_DRF_radius_symbol_t
           radius_symbol_type;        /* standard radius symbol or
                                         user-defined */
     char
     radius_symbol[UF_DRF_DIAMETER_RADIUS_SYMBOL_MAX_BUFSIZE];
                                      /* text for user-defined radius symbol */
     UF_DRF_diameter_radius_placement_t
           diameter_radius_placement; /* placement of diameter/radius symbol
                                          relative to dimension text */
     UF_DRF_text_above_leader_t
           text_above_leader;         /* if option is set to anything other than
                                         UF_DRF_NO_TEXT_ABOVE_LEADER, then
                                         dimension text will be displayed above
                                         the leader stub with the stub extended
                                         to the maximum length of the dimension
                                         text. used with dimension text
                                         orientations of
                                         UF_DRF_TEXT_DIMENSION_HORIZONTAL and
                                         UF_DRF_TEXT_DIMENSION_BY_ANGLE.
                                         for UF_DRF_NO_TEXT_ABOVE_LEADER, the
                                         dimension text displays next to the
                                         leader stub */
     double symbol_to_dimension_text_distance; /* distance between radius/
                                                  diameter symbol and dimension
                                                  text in character spaces */
     double folded_radius_angle;      /* angle of the fold for folded radius
                                         dimensions */
};
typedef struct UF_DRF_diameter_radius_preferences_s
 UF_DRF_diameter_radius_preferences_t, *UF_DRF_diameter_radius_preferences_p_t;


/******************************************************************************
 * UF_DRF_hatch_fill_preferences_t specifies annotation preferences that
   apply to crosshatching and area fill
 ******************************************************************************/
struct UF_DRF_hatch_fill_preferences_s
{
     double  hatch_distance;      /* distance between crosshatch lines */
     double  hatch_angle;         /* inclination angle of crosshatch lines */
     double  hatch_tolerance;     /* controls how closely the system
                                     approximates the boundary along curves */
     char    hatch_file[ UF_CFI_MAX_FILE_NAME_BUFSIZE]; /* name of file containing crosshatch
                                     patterns */
     char    hatch_material[UF_DRF_MAX_HATCH_MATERIAL_NAME_BUFSIZE]; /* name of crosshatch pattern */
     UF_DRF_area_fill_material_t
             area_fill_material;  /* area fill material or pattern style */
     double  area_fill_scale;     /* scale of area fill pattern */
     double  area_fill_angle;     /* rotation angle of area fill pattern */
     int     color;               /* color for crosshatch and area fill lines
                                     or the area fill solid fill color */
     UF_DRF_line_width_t
             width;               /* width for crosshatch and area fill lines */
};
typedef struct UF_DRF_hatch_fill_preferences_s  UF_DRF_hatch_fill_preferences_t,
  *UF_DRF_hatch_fill_preferences_p_t;


/* UF_DRF_retained_state_t defines the states for retained annotations */
enum UF_DRF_retained_state_e
{
    UF_DRF_KEEP_RETAINED_ANNOTATIONS,
    UF_DRF_DELETE_RETAINED_ANNOTATIONS
} ;
typedef enum UF_DRF_retained_state_e UF_DRF_retained_state_t;

/* Methods for specifying original color, font and width for retained
   annotations */
#define UF_DRF_RETAINED_COLOR_ORIGINAL  0
#define UF_DRF_RETAINED_FONT_ORIGINAL   0
#define UF_DRF_RETAINED_WIDTH_ORIGINAL -1

typedef enum
{
    UF_DRF_RENDER_CANNOT_RENDER_SYMBOL = -2,
    UF_DRF_RENDER_CANNOT_RENDER_CHAR,
    UF_DRF_RENDER_OK,
    UF_DRF_RENDER_DRAWN,
    UF_DRF_RENDER_NOT_DRAWN
} UF_DRF_render_text_status_t;


/*****************************************************************************
    Callbacks for UF_DRF_render_text.  Default set is used for other functions.

    Each return either UF_DRF_RENDER_OK or
    UF_DRF_RENDER_CANNOT_RENDER_CHAR (UF_DRF_draw_char_fn_t only) or
    UF_DRF_RENDER_CANNOT_RENDER_SYMBOL (UF_DRF_draw_user_symbol_fn_t only).

    If a cannot render or not drawn status is returned for a user symbol or an
    individual character, the resultant object will be stroked.

    Lines are output as polyline segments bracketed by calls to
    the begin and end line functions.
  *****************************************************************************/
typedef UF_DRF_render_text_status_t (*UF_DRF_begin_line_fn_t)(
    void *client      /* <I> client data                               */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_end_line_fn_t)(
    void *client      /* <I> client data                               */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_set_to_position_fn_t)(
    double in_point[3],     /* <I> 3d point in coord system of annotation */
    void *client,           /* <I> client data                            */
    double out_point[3],    /* <O> internally used                        */
    logical *out_status     /* <O> used by draw_to_position               */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_draw_to_position_fn_t)(
    double in_point[3],       /* <I> 3d point in coord system of annotation */
    double last_out_point[3], /* <I> last output point from set_to_position
                                     or draw_to_position                    */
    logical last_status,      /* <I> last status from set_to_position
                                     or draw_to_position                    */
    void *client,             /* <I> client data                            */
    double out_point[3],      /* <O> internally used                        */
    logical *out_status       /* <O> used by draw_to_position               */
);


typedef UF_DRF_render_text_status_t (*UF_DRF_draw_arc_fn_t)(
    double center[3],     /* <I> center point in coord system of annotation */
    double radius,        /* <I> radius of arc                              */
    double start_param,   /* <I> start angle in radians                     */
    double end_param,     /* <I>   end angle in radians                     */
    void *client          /* <I> client data                                */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_draw_char_fn_t)(
    double origin[3],        /* <I> text_origin coord system of annotation    */
    unsigned char character, /* <I> character (possibly multi-byte)to be drawn */
    void *client             /* <I> client data                            */
);

/* Function called to render a text string using a standard font for UF_DRF_render_table_t
   when the use_standard_font_string_fn UF_DRF_render_table_t flag is set.
   This function should be used with the text mode set to UF_TEXT_ALL_UTF8.
   Data returned by this function may be outside the user's locale mode. */
typedef UF_DRF_render_text_status_t (*UF_DRF_draw_standard_font_string_fn_t)(
    const char* textString,             /* <I> Text string to display.
                                               If the text mode is UF_TEXT_LOCALE then the '#' character
                                               will be returned for each character that is outside the user's
                                               locale mode.
                                               Note that text control sequence symbols displayed using
                                               standard fonts may return characters that are defined outside
                                               the user's locale. */
    const double origin[3],             /* <I> Origin of text baseline */
    int fontId,                         /* <I> Standard font number */
    double textAngle,                   /* <I> Text angle */
    double fontSize,                    /* <I> Character height to use for standard font.  This is the
                                               actual size used when using the FreeType Font library.
                                               Note that this differs from the NX character height. */
    double gapSize,                     /* <I> Size of spacing between characters */
    double aspectRatio,                 /* <I> Aspect ratio to use for display */
    logical suppressKerning,               /* <I> True to not use kerning when rendering */
    logical vertical,                      /* <I> True to draw in vertical direction */
    logical bold,                          /* <I> True if using bold style */
    logical italic,                        /* <I> True if using italic style */
    void *client                        /* <I> Client data */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_draw_user_symbol_fn_t)(
    char *symbol_name,    /* <I> name of user defined symbol to render     */
    double origin[3], /* <I> */
    void *symbol_params, /* <I> */
    void *client          /* <I> client data                               */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_set_cfw_fn_t)(
    UF_DRF_cfw_p_t cfw,   /* <I> new color, line font and line width */
    void *client          /* <I> client data                         */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_push_orientation_fn_t)(
    double matrix[9],     /* <I> orientation matrix */
    void *client          /* <I> client data        */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_pop_orientation_fn_t)(
    void *client          /* <I> client data        */
);

typedef UF_DRF_render_text_status_t (*UF_DRF_fill_region_fn_t)(
    int num_points,        /* <I> number of points in region    */
    double *points,        /* <I,len:num_points> array of 3d points            */
    double fill_dist,      /* <I> fill distance                 */
    double last_pt[3],     /* <O> last on screen point          */
    logical *was_drawn,    /* <O> return TRUE if anything drawn */
    void *client           /* <I> client data                   */
);

struct UF_DRF_render_table_s
{
    UF_DRF_begin_line_fn_t begin_line;
    UF_DRF_end_line_fn_t end_line;
    UF_DRF_set_to_position_fn_t set_to_position;
    UF_DRF_draw_to_position_fn_t draw_to_position;
    UF_DRF_draw_arc_fn_t draw_arc;
    UF_DRF_draw_char_fn_t draw_char;
    UF_DRF_draw_standard_font_string_fn_t draw_standard_font_string;
            /* If the draw_standard_font_string field is not NULL then it
               will get called to display a string that uses a standard font
               instead of using stroke lines to display the standard font string */
    UF_DRF_draw_user_symbol_fn_t draw_user_symbol;
    UF_DRF_set_cfw_fn_t set_cfw;
    UF_DRF_push_orientation_fn_t push_orientation;
    UF_DRF_pop_orientation_fn_t pop_orientation;
    UF_DRF_fill_region_fn_t fill_region;

    double standardFontFunCharSize; /* The character size that corresponds to the font size
                                       passed into the draw_standard_font_string function. */
};
typedef struct UF_DRF_render_table_s
               UF_DRF_render_table_t, *UF_DRF_render_table_p_t;

/*  The following enumerated type is used to define the type of associative
 *  origin on an annotation.
 */
typedef enum
{
    UF_DRF_ORIGIN_DRAG,
    UF_DRF_ORIGIN_RELATIVE_TO_VIEW,
    UF_DRF_ORIGIN_RELATIVE_TO_GEOMETRY,
    UF_DRF_ORIGIN_VERTICALLY_ALIGNED,
    UF_DRF_ORIGIN_HORIZONTALLY_ALIGNED,
    UF_DRF_ORIGIN_ALIGNED_WITH_ARROWS,
    UF_DRF_ORIGIN_AT_A_POINT,
    UF_DRF_ORIGIN_OFFSET_FROM_TEXT,
    UF_DRF_ORIGIN_STACK
} UF_DRF_associative_origin_type_t;

/*  This data structure is used when setting and querying associative origin
 *  information for an annotation.
 */
struct UF_DRF_associative_origin_s
{
    UF_DRF_associative_origin_type_t origin_type;

    /* Used for UF_DRF_ORIGIN_RELATIVE_TO_VIEW */
    tag_t view_eid;          /* View of associativity for the annotation. */

    /* Used for UF_DRF_ORIGIN_RELATIVE_TO_GEOMETRY */
    tag_t view_of_geometry;  /* The member view in  which the absolute model
                              * point lies.  This is used for mapping onto
                              * the drawing. */
    tag_t point_on_geometry; /* Absolute point in absolute space the annotation
                              * is associated with. */

    /* Used for UF_DRF_ORIGIN_VERTICALLY_ALIGNED */
    tag_t vert_annotation;                            /* Annotation to align
                                                       * with. */
    UF_DRF_align_position_t vert_alignment_position;  /* Alignment position on
                                                       * vert_annotation to
                                                       * align to. */

    /* Used for UF_DRF_ORIGIN_HORIZONTALLY_ALIGNED */
    tag_t horiz_annotation;                           /* Annotation to align
                                                       * with. */
    UF_DRF_align_position_t horiz_alignment_position; /* Alignment position on
                                                       * horiz_annotation to
                                                       * align to. */

    /* Used for UF_DRF_ORIGIN_ALIGNED_WITH_ARROWS */
    tag_t aligned_annotation;  /* Alignment annotation */
    int dimension_line;        /* 1 for dimension line 1, 2 for dimension line 2 */

    /* Used for UF_DRF_ORIGIN_AT_A_POINT */
    tag_t associated_view;   /* The member view in  which the absolute model
                              * point lies.  This is used for mapping onto
                              * the drawing.  May be NULL if annotation is
                              * on the model or the point is on the drawing. */
    tag_t associated_point;  /* Origin location of annotation */

    /* Used for UF_DRF_ORIGIN_OFFSET_FROM_TEXT */
    tag_t offset_annotation;                            /* Annotation to align
                                                         * to */
    UF_DRF_align_position_t offset_alignment_position;  /* Alignment position
                                                         * on annotation to
                                                         * align with. */
    double x_offset_factor;                             /* X Offset factor from
                                                         * associated point. */
    double y_offset_factor;                             /* Y Offset factor from
                                                         * associated point. */
    tag_t stack_annotation;                             /* Used for UF_DRF_ORIGIN_STACK */
    UF_DRF_stack_align_position_t stack_alignment_position;
};
typedef struct UF_DRF_associative_origin_s
               UF_DRF_associative_origin_t, *UF_DRF_associative_origin_p_t;

/* enum declaration for type of finish for the weld */
enum UF_DRF_weld_finish_types_e
{
    UF_DRF_WELD_NO_FINISH = 0,         /* No Finish Specified */
    UF_DRF_WELD_CHIP_FINISH,           /* Chipping */
    UF_DRF_WELD_GRIND_FINISH,          /* Grinding */
    UF_DRF_WELD_HAMMER_FINISH,         /* Hammering */
    UF_DRF_WELD_MACHINE_FINISH,        /* Machining */
    UF_DRF_WELD_ROLL_FINISH,           /* Rolling */
    UF_DRF_WELD_PEEN_FINISH            /* Peening */
};
typedef enum UF_DRF_weld_finish_types_e UF_DRF_weld_finish_types_t;

/* enum declaration for contour type of the weld */
enum UF_DRF_weld_contour_types_e
{
    UF_DRF_WELD_NONE = 0,              /* No Contour specified */
    UF_DRF_WELD_CONVEX,                /* Convex Contour */
    UF_DRF_WELD_FLUSH,                 /* Flush Contour */
    UF_DRF_WELD_CONCAVE,               /* Concave Contour */
    UF_DRF_WELD_BLENDED_TOES,          /* Blended Toes ( applicable only
                                          for ISO and DIN ) */
    UF_DRF_WELD_BACKING_PERM,          /* Permanent Backing Strip ( applicable
                                          only for ISO and DIN ) */
    UF_DRF_WELD_BACKING_REMV           /* Removable Backing Strip ( applicable
                                          only for ISO and DIN ) */
};
typedef enum UF_DRF_weld_contour_types_e UF_DRF_weld_contour_types_t;

/* enum declaration for size code */
enum UF_DRF_weld_size_code_e
{
    UF_DRF_WELD_NO_CODE = -1,          /* no size code - applicable for
                                          ANSI and JIS */
    UF_DRF_WELD_CODE_A,                /* size code 'a' */
    UF_DRF_WELD_CODE_C,                /* size code 'c' */
    UF_DRF_WELD_CODE_D,                /* size code 'd' */
    UF_DRF_WELD_CODE_S,                /* size code 's' */
    UF_DRF_WELD_CODE_Z,                /* size code 'z' */
    UF_DRF_WELD_CODE_P                 /* size code 'p' */
};
typedef enum UF_DRF_weld_size_code_e UF_DRF_weld_size_code_t;

/* enum declarations for the weld symbol types */
enum UF_DRF_weld_symbol_types_e
{
    UF_DRF_WELD_NO_SYMBOL = 0,         /* No Symbol specified */
    UF_DRF_WELD_BUTT_WITH_RE_SYMBOL,   /* Butt Weld with Raised Edges */
    UF_DRF_WELD_SQUARE_BUTT_SYMBOL,    /* Groove Square Butt Symbol */
    UF_DRF_WELD_GROOVE_V_SYMBOL,       /* V-Groove Symbol */
    UF_DRF_WELD_V_WITH_BRF_SYMBOL,     /* V Groove with Broad Root Face */
    UF_DRF_WELD_BEVEL_SYMBOL,          /* Bevel Groove Symbol */
    UF_DRF_WELD_BEVEL_WITH_BRF_SYMBOL, /* Bevel with Broad Root Face */
    UF_DRF_WELD_U_SYMBOL,              /* U Groove Symbol */
    UF_DRF_WELD_J_SYMBOL,              /* J Groove Symbol */
    UF_DRF_WELD_FLARE_V_SYMBOL,        /* Flare V Groove Symbol */
    UF_DRF_WELD_FLARE_BEVEL_SYMBOL,    /* Flare Bevel Groove Symbol */
    UF_DRF_WELD_FILLET_SYMBOL,         /* Fillet Weld Symbol */
    UF_DRF_WELD_PLUG_SLOT_SYMBOL,      /* Plug/Slot Weld Symbol */
    UF_DRF_WELD_EDGE_SYMBOL,           /* Edge Weld Symbol */
    UF_DRF_WELD_SPOT_SYMBOL,           /* Spot Weld Symbol */
    UF_DRF_WELD_SEAM_SYMBOL,           /* Seam Weld Symbol */
    UF_DRF_WELD_STP_FLANK_V_SYMBOL,    /* Steep Flanked V Butt Symbol */
    UF_DRF_WELD_STP_FLANK_BEVEL_SYMBOL,/* Steep Flanked Bevel Butt */
    UF_DRF_WELD_BACKING_SYMBOL,        /* Backing Symbol */
    UF_DRF_WELD_STUD_SYMBOL,           /* Stud Weld Symbol */
    UF_DRF_WELD_SURFACING_SYMBOL,      /* Surfacing Symbol */
    UF_DRF_WELD_SURFACE_JOINT_SYMBOL,  /* Surface Joint Symbol */
    UF_DRF_WELD_INCLINED_JOINT_SYMBOL, /* Inclined Joint Symbol */
    UF_DRF_WELD_FOLD_JOINT_SYMBOL      /* Fold Joint Symbol */
};
typedef enum UF_DRF_weld_symbol_types_e UF_DRF_weld_symbol_types_t;

/* enum declaration for extension type */
enum UF_DRF_weld_sym_ext_type_e
{
    UF_DRF_WELD_SYM_EXT_NONE = 0,      /* No Extension */
    UF_DRF_WELD_SYM_EXT_DOG_LEG,       /* Forked tail extension */
    UF_DRF_WELD_SYM_EXT_BOX            /* Closed tail extension */
};
typedef enum UF_DRF_weld_sym_ext_type_e UF_DRF_weld_sym_ext_type_t;

/* enum declaration for identification line response */
enum UF_DRF_weld_ident_line_type_e
{
    UF_DRF_WELD_SYM_NO_IDENT_LINE = 1, /* No Identification line ( as in ANSI
                                          and JIS */
    UF_DRF_WELD_SYM_IDENT_LINE_TOP,    /* Identification line top */
    UF_DRF_WELD_SYM_IDENT_LINE_BOTTOM  /* Identification line bottom */
};
typedef enum UF_DRF_weld_ident_line_type_e UF_DRF_weld_ident_line_type_t;

/***************************************************************************
This is the structure to specify weld symbol information like finish type,
contour type, weld type, angle, number of welds, size and pitch.
****************************************************************************/
struct UF_DRF_weld_sym_info_s
{
    UF_DRF_weld_finish_types_t  finish_type;  /* finish type */
    UF_DRF_weld_contour_types_t contour_type; /* contour type */
    UF_DRF_weld_symbol_types_t  weld_type;    /* weld type */
    UF_DRF_weld_size_code_t     size_code;    /* size code - applicable
                                                 only for ISO and DIN */
    char                        angle[ MAX_LINE_BUFSIZE ]; /* Groove Angle or Countersink
                                                 Angle */
    char                        num_root_depth[ MAX_LINE_BUFSIZE ]; /* Number of Welds or Root
                                                 opening or Depth of Weld as
                                                 the case may be */
    char                        size[ MAX_LINE_BUFSIZE ]; /* size of the weld */
    char                        pitch[ MAX_LINE_BUFSIZE ]; /* pitch of the weld */
};
typedef struct UF_DRF_weld_sym_info_s UF_DRF_weld_sym_info_t,
                                      *UF_DRF_weld_sym_info_p_t;

struct UF_DRF_weld_symbols_s
{
    UF_DRF_weld_sym_info_t        sym_info_top;    /* symbols info for top */
    UF_DRF_weld_sym_info_t        sym_info_bottom; /* symbols info for
                                                      bottom */
    UF_DRF_weld_sym_ext_type_t    extension;       /* extension */
    UF_DRF_weld_ident_line_type_t ident_line_type; /* type of identification
                                                      line */
    int                           peripheral_flag; /* variable indicating
                                                      whether allround symbol
                                                      is required or not.
                                                      If peripheral_flag = 0,
                                                      then no allround symbol.
                                                      If peripheral_flag = 1,
                                                      then allround symbol
                                                      is required */
    int                           field_flag;      /* value for field flag
                                                      field_flag = 0 for weld
                                                      at site;
                                                      field_flag= 1 for weld
                                                      at field */
    int                           staggered_flag;  /* indicates whether weld is
                                                      staggered or not.
                                                      staggered_flag = 0 for
                                                      non-staggered welds;
                                                      staggered_flag = 1 for
                                                      staggered welds */
    int                           center_flag;     /* indicates whether weld to
                                                      be centered with respect
                                                      to reference line.
                                                      Applicable for spot and
                                                      seam welds only.
                                                      center_flag = 0 => donot
                                                      center;
                                                      center_flag = 1 => center
                                                    */
    int                           num_lines;       /* number of lines of
                                                      reference text */
    char                          symbol_standard[ UF_OBJ_NAME_BUFSIZE ]; /* standard for the weld
                                                      symbol.  Has to be one
                                                      among the following :
                                                      ANSI, ISO, DIN, JIS. */
    char                          **reference_text;/* <len:num_lines> multi line reference
                                                      text */
    double                        scale_factor;    /* scale factor to be used
                                                      for creating the welding
                                                      symbol */
};
typedef struct UF_DRF_weld_symbols_s UF_DRF_weld_symbols_t,
                                     *UF_DRF_weld_symbols_p_t;

/* enum declarations for the types of feature annotation which can be inherited
   Currently only UF_DRF_INHERIT_FEATURE_PARAMETERS is supported */
enum UF_DRF_inherit_type_e
{
    UF_DRF_INHERIT_FEATURE_PARAMETERS = 1,
                                       /* Inherit only annotation for feature parameters */
    UF_DRF_INHERIT_POSITIONAL_DIMENSIONS,
                                       /* Inherit only annotation for the feature position */
    UF_DRF_INHERIT_PARAMETERS_AND_POSITIONS
                                       /* Inherit annotation for both feature parameters
                                          and the feature position */
};
typedef enum UF_DRF_inherit_type_e UF_DRF_inherit_type_t;

/*The following enumerated type describes the type of connections for a custom symbol*/
enum UF_DRF_symbol_connection_type_e
{
    UF_DRF_LEFT_LEADER_CONNECTION,     /* Left leader symbol connection type */
    UF_DRF_RIGHT_LEADER_CONNECTION     /* Right leader symbol connection type */
};
typedef enum UF_DRF_symbol_connection_type_e
             UF_DRF_symbol_connection_type_t;


/*Text types for custom symbols*/
enum UF_DRF_custom_symbol_text_type_e
{
    UF_DRF_MANDATORY_TEXT,             /*Text that cannot change*/
    UF_DRF_PARTIALLY_CONTROLLED_TEXT,  /*Text that is controlled via a list, but may be arbitrary*/
    UF_DRF_FULLY_CONTROLLED_TEXT,      /*Text that is controlled solely via a list*/
    UF_DRF_ARBITRARY_TEXT,             /*Text that is completely arbitrary*/
    UF_DRF_INTEGER_TEXT,               /*Text that must be an integer with upper and lower bounds*/
    UF_DRF_REAL_TEXT,                  /*Text that must be a real number with upper and lower bounds*/
    UF_DRF_RULE_TEXT                   /*Text that is driven by KF rule*/
};
typedef enum UF_DRF_custom_symbol_text_type_e
             UF_DRF_custom_symbol_text_type_t;

/*This structure defines a set of intermediate points for a single leader
  of an annotation.*/
struct UF_DRF_intermediate_points_s
{
    int num_points;      /*The number of intermediate points for this leader.
                           num_points must be greater than or equal to zero.
                           The number of points corresponds directly to the
                           number of points between the stub and the leader
                           terminator.  The ordering of the points is also
                           important.  The first point (points[0][]) describes
                           the closest intermediate point to the leader
                           terminator.  The nth point describes the
                           intermediate point closest to the stub (or
                           annotation if there is no stub.  Here is a sample
                           of a leader with 3 intermediate points and their
                           relative indices.  Note that the stub points are not
                           considered intermediate points:

                                           *(points[2][...])
                                          / \
                                         /   \       *----------------> (terminator)
                           ANN -(stub)--/     \     / (points[0][...])
                                               \   /
                                                \ /
                                                 *(points[1][...])

                         */
    double **points;     /*<len:num_points> A two-dimensional array of doubles.  The first
                           dimension of this array should be equal to num_points.
                           The second dimension of this array is fixed at 3, since
                           each set of three doubles describes a 3 dimensional
                           point in absolute coordinates.*/
};
typedef struct UF_DRF_intermediate_points_s
               UF_DRF_intermediate_points_t, *UF_DRF_intermediate_points_p_t;

/*A structure encapsulating the information needed to create a set of annotation
  leaders for a single annotation.  This structure can specify any number
  of leaders, each with it's own set of intermediate points.*/
struct UF_DRF_leader_s
{
    int num_leaders;                                  /*The number of leaders in the structure*/
    tag_t *leader_terminators;                        /*<len:num_leaders>
                                                        An array of tags for the leader
                                                        terminators.  There must be exactly
                                                        one(1) tag for each leader represented
                                                        in the structure.*/
    UF_DRF_leader_orientation_t leader_orientation;   /*This enumerated type describes the orientation
                                                        of the leader's stub.  For now, UF_DRF_LEADER_TOP
                                                        and UF_DRF_LEADER_BOTTOM are invalid
                                                        arguments for this structure.*/
    UF_DRF_intermediate_points_t *intermediate_points;/* <len:num_leaders> This is an array of intermediate point
                                                        structures.  The number of structures
                                                        in this array should correspond to
                                                        the number of leaders defined in num_leaders.*/

};
typedef struct UF_DRF_leader_s
               UF_DRF_leader_t, *UF_DRF_leader_p_t;

/*This structure defines the text data for a custom symbol*/
struct UF_DRF_custom_symbol_text_s
{
    tag_t note_tag;                             /*This is the tag of the note from which
                                                  this text will be based.  This object
                                                  must be of type UF_drafting_entity_type
                                                  and subtype UF_draft_note_subtype*/
    UF_DRF_custom_symbol_text_type_t text_type; /*The type of text for this structure*/
    char *title;                                /*The title of this text field.
                                                  This title displays in the dialog
                                                  when creating the symbol.*/
    double min_value;                           /*This value is the lower bound for
                                                  UF_DRF_integer_text and UF_DRF_real_text
                                                  types.  For integer text, this value is
                                                  truncated to an integer form. This value
                                                  has no meaning for arbitrary, controlled,
                                                  mandatory, or partially controlled text*/
    double max_value;                           /*This value is the upper bound for
                                                  UF_DRF_integer_text and UF_DRF_real_text
                                                  types.  For integer text, this value is
                                                  truncated to an integer form.  This value
                                                  has no meaning for arbitrary, controlled,
                                                  mandatory, or partially controlled text*/
    double current_value;                       /*This value is the current value defined for
                                                  this text object.  This value only has
                                                  meaning for UF_DRF_real_text and
                                                  UF_DRF_integer_text types.  For integer text,
                                                  this value is truncated to integer format.
                                                  This value must be greater than or equal to
                                                  min_value and less than or equal to max_value.*/
    char **optional_strings;                    /*<len:num_optional_strings>An array of strings in localized format describing
                                                  a list of strings for controlled and partially
                                                  controlled text.  */
    int num_optional_strings;                   /*The number of strings in the array above.*/
    int current_option;                         /*The index of the currently selected string for
                                                  controlled and partialy controlled text.  If
                                                  the text type is UF_DRF_partially_controlled_text
                                                  and the current_option is -1, then this indicates
                                                  that none of the given choices should be used and
                                                  the arbitrary text field will contain the string
                                                  for this text object.*/
    char *simple_text;                          /*The current value for arbitrary or mandatory text.
                                                  This field is only used for the
                                                  UF_DRF_arbitrary_text and UF_DRF_mandatory_text
                                                  types.*/
};
typedef struct UF_DRF_custom_symbol_text_s
               UF_DRF_custom_symbol_text_t, *UF_DRF_custom_symbol_text_p_t;

/*This structure contains the information which defines a leader connection
  for a Custom Symbol.*/
struct UF_DRF_symbol_connection_s
{
    UF_DRF_symbol_connection_type_t connection_type; /*Description of the connection type (e.g. Left or right)*/
    tag_t connection_point;                          /*The tag of the connection point*/
};
typedef struct UF_DRF_symbol_connection_s
               UF_DRF_symbol_connection_t, *UF_DRF_symbol_connection_p_t;

/*This structure contains all the data necessary to create a custom symbol.*/
struct UF_DRF_custom_symbol_s
{
    tag_t *geometry;                        /*<len:num_text>Tags of lines, arcs, splines, crosshatch, and
                                              area fill for symbol definition*/
    int num_geometry;                       /*Number of tags in the curves array above.*/
    UF_DRF_custom_symbol_text_t *text;      /*<len:num_text>Array of symbol text structures for symbol
                                             definition.*/
    int num_text;                           /*Number of text structures in the text
                                              array.*/
    tag_t anchor_point;                     /*Tag of the symbol's anchor point.*/
    UF_DRF_symbol_connection_t *connections;/*<len:num_connections>Array of tags for the symbol's leader
                                              connect points.*/
    int num_connections;                    /*Number of leader connection points.
                                              The number may be 0, 1, or 2*/
    UF_DRF_leader_p_t leader;               /*Pointer to information about the leader*/
    double angle;                           /*The angle of the symbol with respect to
                                              the WCS X-axis*/
    double scale;                           /*The scale of the symbol with respect to
                                              the size of the original geometry*/
    double origin[3];                       /*The origin of the symbol in absolute
                                              coordinates.*/
};
typedef struct UF_DRF_custom_symbol_s
               UF_DRF_custom_symbol_t, *UF_DRF_custom_symbol_p_t;

/*  The following enumerated type is used for setting the user defined
 *  symbols parameters on objects and determines whether the stored values
 *  should be interpreted as "length / height" or "scale / aspect ratio"
 *  parameters.
 */
enum UF_DRF_uds_size_type_e
{
    UF_DRF_LENGTH_HEIGHT,
    UF_DRF_SCALE_ASPECT_RATIO
};
typedef enum UF_DRF_uds_size_type_e UF_DRF_uds_size_type_t;

/*  Structure defining the length / height or scale / aspect ratio parameters
 *  of embedded or standalone symbols.
 */
struct UF_DRF_uds_size_s
{
    UF_DRF_uds_size_type_t
       uds_size_type; /*  If the uds type is set to UF_DRF_LENGTH_HEIGHT, then the following
     *  parameters are interpreted as ?length and height?.  If the uds
     *  type is set to UF_DRF_SCALE_ASPECT_RATIO, then the following
     *  parameters are interpreted as ?scale and aspect ratio?.
     */

    double length_or_scale;
    double height_or_aspect_ratio;
};
typedef struct UF_DRF_uds_size_s
               UF_DRF_uds_size_t, *UF_DRF_uds_size_p_t;

/*  The following enumerated type contains those "point types" supported by
 *  annotation associativities. 
 *
 *  Spline Pole point, Conic Anchor Point, Spline Defining Point and 
 *  Routing Point associativity are not supported via UF.
 */
enum UF_DRF_object_assoc_point_type_e
{
    UF_DRF_NO_POINT_TYPE,
    UF_DRF_CONTROL_POINT_POINT_TYPE,
    UF_DRF_ARC_CENTER_POINT_TYPE,
    UF_DRF_TANGENT_POINT_TYPE,
    UF_DRF_INTERSECTION_POINT_TYPE,
    UF_DRF_SCREEN_POSITION_POINT_TYPE,
    UF_DRF_CYLINDRICAL_FACE_TYPE,
    UF_DRF_POINT_ON_CURVE_POINT_TYPE,
    UF_DRF_OFFSET_CIRCLE_POINT_TYPE,
    UF_DRF_SPLINE_POLE_POINT_TYPE,
    UF_DRF_CONIC_ANCHOR_POINT_TYPE,
    UF_DRF_SPLINE_DEF_POINT_TYPE,
    UF_DRF_ROUTING_POINT_TYPE
};
typedef enum UF_DRF_object_assoc_point_type_e UF_DRF_object_assoc_point_type_t;

/*  The following enumerated type contains those "line types" supported by
 *  annotation associativities.
 */
enum UF_DRF_object_assoc_line_type_e
{
    UF_DRF_NO_LINE_TYPE,
    UF_DRF_EXISTING_LINE_TYPE,
    UF_DRF_POINT_VECTOR_LINE_TYPE,
    UF_DRF_EXTENSION_LINE_TYPE,
    UF_DRF_CENTERLINE_COMPONENT_LINE_TYPE,
    UF_DRF_ENTERED_ANGLE_LINE_TYPE,
    UF_DRF_HORIZONTAL_RIGHT_LINE_TYPE,
    UF_DRF_VERTICAL_UP_LINE_TYPE,
    UF_DRF_HORIZONTAL_LEFT_LINE_TYPE,
    UF_DRF_VERTICAL_DOWN_LINE_TYPE,
    UF_DRF_BASE_LINE_TYPE
};
typedef enum UF_DRF_object_assoc_line_type_e UF_DRF_object_assoc_line_type_t;

/*  The following structures is used to manage the associativities for
 *  drafting entities, dimensions, GD&T display instances, and
 *  Smart Model display instances and callouts.
 */
struct UF_DRF_object_assoc_data_s
{
    tag_t assoc_object_1;  /* Tag of first referenced object */
    tag_t assoc_object_2;  /* Tag of second referenced object (for
                            * intersections)
                            */

    tag_t object_view;     /* Drawing or drafting member view of the
                            * associatied objects.
                            *
                            * NOTE: For intersections, both objects must
                            * lie in the same view.
                            */

    /*  Point / Line options for associativities  */
    UF_DRF_object_assoc_point_type_t point_type;
    UF_DRF_object_assoc_line_type_t line_type;

    /*  Line option data  */
    double base_pt_1[3];             /* Used for line options with 1 point
                                      * (in absolute of work view)
                                      */
    double base_pt_2[3];             /* Used for line options with 2 points
                                      * (in absolute of work view)
                                      */
    double entered_angle;            /* Used for entered angle line method
                                      * (in radians)
                                      */

    /*  Associated position or reference point of the associativity
     *  in absolute coordinates.
     */
    double assoc_point[3];
};
typedef struct UF_DRF_object_assoc_data_s
               UF_DRF_object_assoc_data_t, *UF_DRF_object_assoc_data_p_t;

#define UF_DRF_LEADER_MAX_LEADERS    (7)
#define UF_DRF_LEADER_MAX_INT_POINTS (7)

typedef enum
{
    UF_DRF_LEADER_SIDE_LEFT  = 0,
    UF_DRF_LEADER_SIDE_RIGHT

} UF_DRF_leader_side_e;


struct UF_DRF_gdt_leader_data_s
{
    tag_t                        object;   /* This is the tag of the
                                              associated object.
                                           */
    tag_t                        view;     /* This is the tag of the member
                                              view of the object_tag entity.
                                           */
    double                       point[3]; /* This 3D point is the location
                                              of the terminator (or arrow)
                                              of the leader.
                                           */
    UF_DRF_intermediate_points_t intermediate_points; /* These are the intermediate
                                                         points, if any, between the
                                                         stub and the terminator of the
                                                         leader.
                                                       */
};
typedef struct UF_DRF_gdt_leader_data_s
               UF_DRF_gdt_leader_data_t, *UF_DRF_gdt_leader_data_p_t;


struct UF_DRF_gdt_leader_s
{
    UF_DRF_leader_type_t      leader_type;
    UF_DRF_leader_side_e      leader_side;
    int                       num_leaders;
    UF_DRF_gdt_leader_data_t  leader_data[UF_DRF_LEADER_MAX_LEADERS];

};
typedef struct UF_DRF_gdt_leader_s
               UF_DRF_gdt_leader_t, *UF_DRF_gdt_leader_p_t;

/******************************************************************************
The following structure is used to create, edit and query images on drawing
sheets.

Environment: Internal  and  External

See Also:

 UF_DRF_create_image_from_file
 UF_DRF_create_image
 UF_DRF_init_image_data
 UF_DRF_ask_image_data
 UF_DRF_free_image_data
 UF_DRF_set_image_align_position
 UF_DRF_set_image_aspect_ratio_lock
 UF_DRF_set_image_height
 UF_DRF_set_image_width
 UF_DRF_rotate_image
 UF_DRF_flip_image_about_height
 UF_DRF_flip_image_about_width

History: This structure was originally released in NX2.0.
 ******************************************************************************/
struct UF_DRF_image_data_s
{
    char *image_name;           /* The name of image in the part            */
    tag_t drawing_sheet;        /* The drawing sheet on which to create the
                                 * image or NULL_TAG to create the image on
                                 * the current drawing sheet.               */
    logical aspect_ratio_locked;/* TRUE if the image's aspect ratio
                                 * cannot be changed                        */
    double width;               /* The width of the image in drawing
                                 * sheet units
                                 * 0.0 to use original image length         */
    double height;              /* The height of the image in drawing
                                 * sheet units
                                 * 0.0 to use original image height         */
    UF_DRF_align_position_t alignment_position;
                                /* The location to use when aligning the
                                 * image to another object                  */
    double origin[3];           /* Point in drawing sheet units defining the
                                 * image origin which is located at the
                                 * image alignment_position                 */
    double width_dir[3];        /* Vector defining the direction in which
                                 * the image width is displayed
                                 * Currently, images can only be rotated in
                                 * 90-degree increments so this vector will
                                 * always be parallel or perpendicular to
                                 * the drawing sheet's X-axis               */
    double height_dir[3];       /* Vector defining the direction in which
                                 * the image height is displayed
                                 * Currently, images can only be rotated in
                                 * 90-degree increments so this vector will
                                 * always be parallel or perpendicular to
                                 * the drawing sheet's Y-axis               */
};
typedef struct UF_DRF_image_data_s
               UF_DRF_image_data_t, *UF_DRF_image_data_p_t;

/*A structure encapsulating the information needed to create a set of annotation
  leaders for a single annotation.  This structure can specify any number
  of leaders, each with it's own set of intermediate points. This structure is
  nearly identical to UF_DRF_leader_t except for that it contains the point
  information for the leader terminators in associativity_data */
struct UF_DRF_leader_data_s
{
    int num_leaders;                                  /*The number of leaders in the structure*/
    UF_DRF_object_assoc_data_t *associativity_data;   /* <len:num_leaders> An array containing the information for each
                                                         associativity for that object.  Use UF_free
                                                         to free this array of allocated memory. */
    UF_DRF_leader_orientation_t leader_orientation;   /*This enumerated type describes the orientation
                                                        of the leader's stub.  For now, UF_DRF_LEADER_TOP
                                                        and UF_DRF_LEADER_BOTTOM are invalid
                                                        arguments for this structure.*/
    UF_DRF_intermediate_points_t *intermediate_points;/* <len:num_leaders> This is an array of intermediate point
                                                        structures.  The number of structures
                                                        in this array should correspond to
                                                        the number of leaders defined in num_leaders.*/
};
typedef struct UF_DRF_leader_data_s
               UF_DRF_leader_data_t, *UF_DRF_leader_data_p_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_DRF_TYPES_INCLUDED */
