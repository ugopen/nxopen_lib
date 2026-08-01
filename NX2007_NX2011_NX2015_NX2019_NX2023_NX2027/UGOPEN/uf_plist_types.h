/*******************************************************************************

             Copyright (c) 2003 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved



File description:

    User function parts list datatypes

*******************************************************************************/

#ifndef UF_PLIST_TYPES_H_INCLUDED
#define UF_PLIST_TYPES_H_INCLUDED

#include <uf_defs.h>
#include <uf_tabnot_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/*  NX now supports multi-byte characters which may be larger in size, so MAX_FIELD_STR has been deprecated.  You
      should use MAX_LINE_BUFSIZE instead
*/
/*  */
#define MAX_FIELD_STR_LEN (MAX_LINE_BUFSIZE)
/*  */

/* Possible values for Report mode settings */
#define UF_PLIST_AS_DEFINED 0
#define UF_PLIST_SINGLE     1
#define UF_PLIST_MULTIPLE   2

typedef enum
{
    UF_PLIST_column_type_general,
    UF_PLIST_column_type_callout,
    UF_PLIST_column_type_quantity
} UF_PLIST_column_type_t;

/* Direction that parts list grows */
typedef enum
{
    UF_PLIST_grow_direction_up=1,
    UF_PLIST_grow_direction_down
} UF_PLIST_grow_direction_t ;

/* Method used to show rows that are both locked and deleted */
typedef enum
{
    UF_PLIST_ldr_method_strike_thru=1,
    UF_PLIST_ldr_method_blank,
    UF_PLIST_ldr_method_remove,
    UF_PLIST_ldr_method_ordinary
} UF_PLIST_ldr_method_t;

/* Types of objects used for callout symbols */
typedef enum
{
    UF_PLIST_symbol_type_none=0,
    UF_PLIST_symbol_type_id_symbol_circle,
    UF_PLIST_symbol_type_id_symbol_div_circle,
    UF_PLIST_symbol_type_id_symbol_down_triangle,
    UF_PLIST_symbol_type_id_symbol_up_triangle,
    UF_PLIST_symbol_type_id_symbol_square,
    UF_PLIST_symbol_type_id_symbol_div_square,
    UF_PLIST_symbol_type_id_symbol_hexagon,
    UF_PLIST_symbol_type_id_symbol_div_hexagon,
    UF_PLIST_symbol_type_id_symbol_quad_circle,
    UF_PLIST_symbol_type_id_symbol_rounded_box,
    UF_PLIST_symbol_type_id_symbol_underline
} UF_PLIST_symbol_type_t;

struct UF_PLIST_prefs_s
{
    UF_TABNOT_section_prefs_t section_prefs ; /* Preferences used for creating
                                                 new sections                  */

    UF_PLIST_grow_direction_t grow_direction ;   /* Does the parts list grow
                                                 upward or downward? */ 

    UF_PLIST_ldr_method_t ldr_method ;    /* Method used to show rows that
                                             are both locked and deleted   */

    logical create_new_rows_as_locked ;   /* Should newly created rows
                                             automatically be locked?     */

    char* initial_callout_field ;         /* String used for the first
                                             callout in the parts list. 
                                             Subsequent callouts will be
                                             generated using a sequence
                                             that follows the last 
                                             character of the initial
                                             callout string.  For example,
                                             2 follows 1, B follows A, 
                                             b follows a, etc             */

    int callout_increment ;               /* Value by which the callout
                                             increments                   */

    UF_PLIST_symbol_type_t symbol_type ;  /* Type of object used for auto
                                             creation and placement of
                                             callout symbols */

    char* main_symbol_text ;              /* Format of the string used in
                                             the main callout symbol This
                                             string can contains automatic
                                             text control sequences as
                                             follows: 
                                             $=  - Auto Member - Expands
                                             to the name of the member
                                             $~C - Auto Callout - Expands
                                             to the value of the callout
                                             $~Q - Auto Quantity - Expands
                                             to the value of the first
                                             non-zero quantity field  */

    char* ref_symbol_text ;               /* Format of the string used in
                                             the reference callout symbol
                                             This is in the same format
                                             as main_symbol_text  */

    char* characters_to_skip ;            /* List of callout chars to skip */

    logical auto_update ;                 /* Should the parts list
                                             automatically update when the
                                             model changes?                */

    logical sort_on_update ;              /* Should a sort be done during
                                             update?                      */

    logical highlight_manual_text ;       /* Should manual text be hilited? */

    logical isProtected ;                 /* Should parts list be protected ? */

    logical allowManualRows;             /* Are parts list allow manual row insertion? */
};
typedef struct UF_PLIST_prefs_s
               UF_PLIST_prefs_t, *UF_PLIST_prefs_p_t;


struct UF_PLIST_col_prefs_s
{
    logical is_key_field ;                /* Is this a key field?  A key
                                             field is one that is used to
                                             uniquely identify a row.  It
                                             used to decide whether a new
                                             row gets added or if the
                                             quantity field gets incremented */

    char* default_string ;                /* Default string used for
                                             text in new cells   */

    UF_TABNOT_cell_prefs_t cell_prefs ;   /* Cell preferences for new cells
                                             in this column  */

    logical is_protected;                /* Are cells in column protected? */
};
typedef struct UF_PLIST_col_prefs_s
               UF_PLIST_col_prefs_t, *UF_PLIST_col_prefs_p_t;

struct UF_PLIST_traversal_settings_s
{
    logical master_model;
    logical top_level_only;
    logical leaves_only;
};
typedef struct UF_PLIST_traversal_settings_s
               UF_PLIST_traversal_settings_t, *UF_PLIST_traversal_settings_p_t;

/* Parts List field format structure */
struct UF_PLIST_field_format_s 
{
    int     justification;  /* Text justification for this field:
                               1 - left
                               2 - Center
                               3 - Right
                            */
    char    lead_str[MAX_LINE_BUFSIZE]; /* <len:MAX_LINE_BUFSIZE>
                                            A prefix string that will be
                                            added before every string in
                                            this field.
                                         */
    char    trailing_str[MAX_LINE_BUFSIZE]; /* <len:MAX_LINE_BUFSIZE>
                                                A suffix string that will be
                                                added after every string in 
                                                this field.
                                             */
    int     format_type;    /*  The formatting to use for values in this field:
                                1 - Characters
                                2 - Integer
                                3 - Float
                                4 - Exponential
                            */
    
    int     width;          /*  Number characters for character and Integer
                                formatting.  Number of digits to left of 
                                decimal point for floats and exponential.
                            */
    
    int     precision;      /* Number of digits to right of decimal point 
                               for floats 
                            */
    
};
typedef struct UF_PLIST_field_format_s UF_PLIST_field_format_t;  

#ifdef __cplusplus
}
#endif

#endif /* UF_PLIST_TYPES_H_INCLUDED */
