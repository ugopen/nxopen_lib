/*******************************************************************************

             Copyright (c) 2003-2004 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved
********************************************************************************


File Description:

    This file contains the datatypes and error codes for the Tabular Note
    user function module.

********************************************************************************/

#ifndef UF_TABNOT_ERRORS_H_INCLUDED
#define UF_TABNOT_ERRORS_H_INCLUDED

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

#define UF_TABNOT_fit_method_max UF_TABNOT_fit_method_truncate
#define UF_TABNOT_nm_fit_methods UF_TABNOT_fit_method_max
#define UF_TABNOT_APPEND (-1)

typedef enum {
    UF_TABNOT_header_location_none,
    UF_TABNOT_header_location_above,
    UF_TABNOT_header_location_below
} UF_TABNOT_header_location_t;

typedef enum {
    UF_TABNOT_overflow_left = 1,
    UF_TABNOT_overflow_right,
    UF_TABNOT_overflow_next_sheet,
    UF_TABNOT_overflow_up,
    UF_TABNOT_overflow_down
} UF_TABNOT_overflow_direction_t;

typedef enum {
    UF_TABNOT_display_continuation_note_none,
    UF_TABNOT_display_continuation_note_above,
    UF_TABNOT_display_continuation_note_below
} UF_TABNOT_display_continuation_note_t;

typedef enum {
    UF_TABNOT_attach_point_top_left = 1,
    UF_TABNOT_attach_point_top_right,
    UF_TABNOT_attach_point_bottom_left,
    UF_TABNOT_attach_point_bottom_right
} UF_TABNOT_attach_point_t;

/* Text formats */
typedef enum {
    UF_TABNOT_format_text = 1,
    UF_TABNOT_format_float,
    UF_TABNOT_format_fixed,
    UF_TABNOT_format_general,
    UF_TABNOT_format_monetary,
    UF_TABNOT_format_comma,
    UF_TABNOT_format_fraction_half_size,
    UF_TABNOT_format_fraction_three_quarter_size,
    UF_TABNOT_format_fraction_full_size,
    UF_TABNOT_format_percent,
    UF_TABNOT_format_degrees,
    UF_TABNOT_format_degrees_radian_units,
    UF_TABNOT_format_degrees_degree_units,
    UF_TABNOT_format_hex,
    UF_TABNOT_format_logic,
    UF_TABNOT_format_date_dmy,
    UF_TABNOT_format_date_dm,
    UF_TABNOT_format_date_my,
    UF_TABNOT_format_date_mdy,
    UF_TABNOT_format_date_ymd,
    UF_TABNOT_format_date_y4md,
    UF_TABNOT_format_date_dmy_dot,
    UF_TABNOT_format_time_hm,
    UF_TABNOT_format_time_hms,
    UF_TABNOT_format_hidden,
    UF_TABNOT_format_custom
} UF_TABNOT_format_t;

/* Determines how to display a single 0 */
typedef enum {
    UF_TABNOT_zero_display_zero,
    UF_TABNOT_zero_display_dash,
    UF_TABNOT_zero_display_empty
} UF_TABNOT_zero_display_t;

/* Text justification values */
typedef enum {
    UF_TABNOT_just_left,
    UF_TABNOT_just_center,
    UF_TABNOT_just_right,
    UF_TABNOT_just_top = 0,
    UF_TABNOT_just_middle,
    UF_TABNOT_just_bottom
} UF_TABNOT_just_t;

/* Method used to fit text within a cell.  If
   no methods are specified, the fallback
   method is error display (########).        */
typedef enum {
    UF_TABNOT_fit_method_none,
    UF_TABNOT_fit_method_overwrite_border,
    UF_TABNOT_fit_method_auto_size_text,
    UF_TABNOT_fit_method_wrap,
    UF_TABNOT_fit_method_abbreviate,
    UF_TABNOT_fit_method_remove_spaces,
    UF_TABNOT_fit_method_auto_size_row,
    UF_TABNOT_fit_method_auto_size_col,
    UF_TABNOT_fit_method_truncate
} UF_TABNOT_fit_method_t;

/* Sort direction */
typedef enum {
    UF_TABNOT_sort_dir_descending=0,
    UF_TABNOT_sort_dir_ascending
} UF_TABNOT_sort_direction_t;

struct UF_TABNOT_section_prefs_s
{
    UF_TABNOT_header_location_t header_location;       /* Location to display header */
    double max_height;                                 /* The maximum height of the
                                                          section.  This will determine
                                                          the number of rows contained in
                                                          the section. */

    UF_TABNOT_overflow_direction_t overflow_direction; /* Direction to overflow sections */

    double overflow_spacing;                           /* Distance to offset continuation
                                                          sections (only used when table
                                                          continues on the same sheet) */

    UF_TABNOT_attach_point_t attach_point;             /* Point to which origin is attached */

    logical use_double_width_border;                   /* Should the border be double width? */
    double border_width;                               /* Width of border if use_double_width_border
                                                          is TRUE */
    UF_TABNOT_display_continuation_note_t display_continuation_note; /* Display continuation note flag<DRF30825> */
    char* continuation_note;                             /* Continuation note string */
};
typedef struct UF_TABNOT_section_prefs_s UF_TABNOT_section_prefs_t, *UF_TABNOT_section_prefs_p_t;

struct UF_TABNOT_cell_prefs_s
{
    UF_TABNOT_format_t format;                 /* Cell format */
    int precision;                             /* Precision (# dec places to the
                                                  right of the decimal point)    */
    logical is_a_formula;                      /* Does the formatted text get
                                                  passed to the expression
                                                  subsystem for evaluation    */
    UF_TABNOT_zero_display_t zero_display;     /* The way that a numeric zero
                                                  should display              */
    int text_font;                             /* Index of NX font */
    double text_height;                        /* Height of text in this cell */
    double text_aspect_ratio;                  /* Text aspect ratio */
    double symbolAspectRatio;                  /* Symbol aspect ratio (only available in standard fonts) */
    UF_TABNOT_just_t horiz_just;               /* Horizontal text justification */
    UF_TABNOT_just_t vert_just;                /* Vertical text justification */
    double text_angle;                         /* Text angle in radians */
    double text_slant;                         /* Text slant angle */
    logical is_vertical;                       /* Is text displayed vertical? */
    logical is_italic;                         /* Is text displayed italic? */
    logical strikethru;                        /* Is text stricken thru? */
    double line_space_factor;                  /* Line space factor */
    double char_space_factor;                  /* Character space factor */
    logical is_hidden;                         /* Is display of text suppressed? */
    int text_color;                            /* Text color */
    int text_density;                          /* Text density 1:Normal, 2:Heavy, 3:Thin, 0:Use Default*/
    int bottom_line_cfw[3];                    /* Color/font/width of bottom line */
    int right_line_cfw[3];                     /* Color/font/width of right line
                                                  width follows 1:Normal, 2:Heavy, 3:Thin, 0:Use Default*/
    int nm_fit_methods;                        /* Number of fit methods */
    UF_TABNOT_fit_method_t fit_methods[UF_TABNOT_fit_method_max]; /* Fit methods */
    tag_t referenced_spreadsheet;              /* Referenced spreadsheet */
    int ss_sheet;                              /* Sheet referenced in spreadsheet */
    int ss_row;                                /* Row referenced in spreadsheet */
    int ss_col;                                /* Column referenced in spreadsheet */
    char* prefix;
    char* suffix;
    char* formula_suffix;                      /* This string gets appended to the
                                                  cell text when the text is passed
                                                  to the expression subsystem when
                                                  evaluating the cell as a formula. */
    char* url;
    logical is_protected;                      /* Is cell protected? */
};
typedef struct UF_TABNOT_cell_prefs_s UF_TABNOT_cell_prefs_t, *UF_TABNOT_cell_prefs_p_t;

struct UF_TABNOT_sort_data_s
{
    int sort_index;                            /* Index used to indicate the
                                                  order of precedence one
                                                  column has over another
                                                  when sorting the rows.
                                                  Sorting occurs first using
                                                  the column with a sort_index
                                                  of 1, then on the column
                                                  with a sort_index of 2 and
                                                  so on.  A value of 0 means
                                                  "do not sort on this column".*/
    UF_TABNOT_sort_direction_t sort_direction; /* Direction of the sort */
};
typedef struct UF_TABNOT_sort_data_s UF_TABNOT_sort_data_t, *UF_TABNOT_sort_data_p_t;


#define ERROR_UF_TABNOT_base                   3500000

#define UF_TABNOT_ERROR_BASE                   ERROR_UF_TABNOT_base
#define UF_TABNOT_ERROR_RANGE                  5000
#define UF_TABNOT_NO_ERRORS                    0

#define UF_TABNOT_invalid_header_location      (ERROR_UF_TABNOT_base + 1)
#define UF_TABNOT_invalid_overflow_direction   (ERROR_UF_TABNOT_base + 2)
#define UF_TABNOT_invalid_attach_point         (ERROR_UF_TABNOT_base + 3)
#define UF_TABNOT_invalid_text_format          (ERROR_UF_TABNOT_base + 4)
#define UF_TABNOT_invalid_zero_display         (ERROR_UF_TABNOT_base + 5)
#define UF_TABNOT_invalid_text_justification   (ERROR_UF_TABNOT_base + 6)
#define UF_TABNOT_invalid_fit_method           (ERROR_UF_TABNOT_base + 7)
#define UF_TABNOT_invalid_precision              (ERROR_UF_TABNOT_base + 8)
#define UF_TABNOT_invalid_text_height            (ERROR_UF_TABNOT_base + 9)
#define UF_TABNOT_invalid_text_aspect_ratio      (ERROR_UF_TABNOT_base + 10)
#define UF_TABNOT_invalid_text_line_space_factor (ERROR_UF_TABNOT_base + 11)
#define UF_TABNOT_invalid_text_char_space_factor (ERROR_UF_TABNOT_base + 12)
#define UF_TABNOT_invalid_density                (ERROR_UF_TABNOT_base + 13)
#define UF_TABNOT_invalid_tabnot_tag             (ERROR_UF_TABNOT_base + 14)
#define UF_TABNOT_invalid_section_tag            (ERROR_UF_TABNOT_base + 15)
#define UF_TABNOT_invalid_row_tag                (ERROR_UF_TABNOT_base + 16)
#define UF_TABNOT_invalid_col_tag                (ERROR_UF_TABNOT_base + 17)
#define UF_TABNOT_invalid_cell_tag               (ERROR_UF_TABNOT_base + 18)
#define UF_TABNOT_invalid_plist_tag              (ERROR_UF_TABNOT_base + 19)
#define UF_TABNOT_invalid_plist_row_tag          (ERROR_UF_TABNOT_base + 20)
#define UF_TABNOT_invalid_plist_col_tag          (ERROR_UF_TABNOT_base + 21)
#define UF_TABNOT_invalid_template_file_name     (ERROR_UF_TABNOT_base + 22)
#define UF_TABNOT_invalid_display_continuation_note  (ERROR_UF_TABNOT_base + 23)
#define UF_TABNOT_invalid_symbol_aspect_ratio      (ERROR_UF_TABNOT_base + 24)

/* error 300-500 reserved for hole table */
#define UF_HOLETABLE_invalid_selection           (UF_TABNOT_ERROR_BASE + 301)
#define UF_HOLETABLE_view_already_selected       (UF_TABNOT_ERROR_BASE + 302)
#define UF_HOLETABLE_invalid_input               (UF_TABNOT_ERROR_BASE + 303)
#define UF_HOLETABLE_TABNOT_NO_ERRORS            (UF_TABNOT_ERROR_BASE + 304)
#define UF_HOLETABLE_TABNOT_internal_error       (UF_TABNOT_ERROR_BASE + 305)
#define UF_HOLETABLE_invalid_ordinate_origin     (UF_TABNOT_ERROR_BASE + 306)
#define UF_HOLETABLE_invalid_selected_object     (UF_TABNOT_ERROR_BASE + 307)
#define UF_HOLETABLE_IGNORED_HOLE                (UF_TABNOT_ERROR_BASE + 308)

/* error 501-700 reserved for bend table */
#define UF_BENDTABLE_zero_columns_error          (UF_TABNOT_ERROR_BASE + 501)


#ifdef __cplusplus
}
#endif

#endif /* UF_TABNOT_ERRORS_H_INCLUDED */
