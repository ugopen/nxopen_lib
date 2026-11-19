/*******************************************************************************
             Copyright (c) 2000,2004 UGS PLM Solutions
                       Unpublished - All Rights Reserved                       

 

 

*******************************************************************************/

#ifndef UF_OBJ_TYPES_INCLUDED
#define UF_OBJ_TYPES_INCLUDED

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

#define UF_OBJ_DELETED    0
#define UF_OBJ_TEMPORARY  1
#define UF_OBJ_CONDEMNED  2
#define UF_OBJ_ALIVE      3

/* For use with UF_VIEW_ask/set_visualization*/
#define UF_OBJ_COLOR_ORIGINAL (-1)
#define UF_OBJ_FONT_ORIGINAL  (-1)

/*
    UF_OBJ_<COLOR> symbols should no longer be used.
 
    Symbols such as UF_OBJ_BLUE define color indices. In releases
    prior to NX3, each defined index referenced the indicated color 
    in the default color definition file (CDF) provided with NX. For 
    example, the default CDF assigned blue to color index UF_OBJ_BLUE 
    (1), green to color index UF_OBJ_GREEN (2), etc.
 
    Beginning with NX3, the default CDF does not assign these colors 
    to these indices. The default CDF assigns pale/light colors to 
    color indices 1 through 15 instead of the familiar legacy colors 
    (green, blue, cyan, etc.). Using UF_OBJ_<COLOR> symbols with the 
    default CDF will not produce the expected color.
 
    Instead of using UF_OBJ_<COLOR> symbols, call one of the following 
    functions to obtain the color index that references the desired 
    color.  
        UF_DISP_ask_closest_color
        UF_DISP_ask_closest_color_in_part
        UF_DISP_ask_closest_color_in_displayed part
*/

#define UF_OBJ_LEGACY_BLUE             1
#define UF_OBJ_LEGACY_GREEN            2
#define UF_OBJ_LEGACY_CYAN             3
#define UF_OBJ_LEGACY_RED              4
#define UF_OBJ_LEGACY_MAGENTA          5
#define UF_OBJ_LEGACY_YELLOW           6
#define UF_OBJ_LEGACY_WHITE            7
#define UF_OBJ_LEGACY_OLIVE            8
#define UF_OBJ_LEGACY_PINK             9
#define UF_OBJ_LEGACY_BROWN           10
#define UF_OBJ_LEGACY_ORANGE          11
#define UF_OBJ_LEGACY_PURPLE          12
#define UF_OBJ_LEGACY_DARK_RED        13
#define UF_OBJ_LEGACY_AQUAMARINE      14
#define UF_OBJ_LEGACY_GRAY            15
    
#define UF_OBJ_BLUE                   UF_OBJ_LEGACY_BLUE
#define UF_OBJ_GREEN                  UF_OBJ_LEGACY_GREEN
#define UF_OBJ_CYAN                   UF_OBJ_LEGACY_CYAN
#define UF_OBJ_RED                    UF_OBJ_LEGACY_RED
#define UF_OBJ_MAGENTA                UF_OBJ_LEGACY_MAGENTA
#define UF_OBJ_YELLOW                 UF_OBJ_LEGACY_YELLOW
#define UF_OBJ_WHITE                  UF_OBJ_LEGACY_WHITE
#define UF_OBJ_OLIVE                  UF_OBJ_LEGACY_OLIVE
#define UF_OBJ_PINK                   UF_OBJ_LEGACY_PINK
#define UF_OBJ_BROWN                  UF_OBJ_LEGACY_BROWN
#define UF_OBJ_ORANGE                 UF_OBJ_LEGACY_ORANGE
#define UF_OBJ_PURPLE                 UF_OBJ_LEGACY_PURPLE
#define UF_OBJ_DARK_RED               UF_OBJ_LEGACY_DARK_RED
#define UF_OBJ_AQUAMARINE             UF_OBJ_LEGACY_AQUAMARINE
#define UF_OBJ_GRAY                   UF_OBJ_LEGACY_GRAY
 
#define UF_OBJ_MIN_COLOR         1
#define UF_OBJ_MAX_COLOR       216

/* For use with UF_OBJ_ask_display_properties/UF_OBJ_set_blank_status */
#define UF_OBJ_NOT_BLANKED      0
#define UF_OBJ_BLANKED          1

/* For use with UF_OBJ_ask_display_properties/UF_OBJ_set_line_width */
#define UF_OBJ_WIDTH_ORIGINAL   (-1)
#define UF_OBJ_WIDTH_NORMAL     0
#define UF_OBJ_WIDTH_THICK      1
#define UF_OBJ_WIDTH_THIN       2

/* Support new line width types*/

#define UF_MIN_NEW_WIDTH        5

#define UF_OBJ_WIDTH_1          (UF_MIN_NEW_WIDTH + 0)
#define UF_OBJ_WIDTH_2          (UF_MIN_NEW_WIDTH + 1)
#define UF_OBJ_WIDTH_3          (UF_MIN_NEW_WIDTH + 2)
#define UF_OBJ_WIDTH_4          (UF_MIN_NEW_WIDTH + 3)
#define UF_OBJ_WIDTH_5          (UF_MIN_NEW_WIDTH + 4)
#define UF_OBJ_WIDTH_6          (UF_MIN_NEW_WIDTH + 5)
#define UF_OBJ_WIDTH_7          (UF_MIN_NEW_WIDTH + 6)
#define UF_OBJ_WIDTH_8          (UF_MIN_NEW_WIDTH + 7)
#define UF_OBJ_WIDTH_9          (UF_MIN_NEW_WIDTH + 8)
#define UF_OBJ_MAX_WIDTH        (UF_OBJ_WIDTH_9   + 1)

#define UF_OBJ_is_valid_width( width ) \
    ( (((width) >= (int)UF_OBJ_WIDTH_NORMAL) && ((width) <= (int)UF_OBJ_WIDTH_THIN)) || \
      (((width) >= (int)UF_MIN_NEW_WIDTH) && ((width) < (int)UF_OBJ_MAX_WIDTH)) )

/* 
   UF_OBJ_is_valid_inherited_width is used to validate line width for an object 
   that can inherit its line width value from another object. In this case,
   line width value of the object is represented by UF_OBJ_WIDTH_ORIGINAL.
   Note that UF_OBJ_WIDTH_ORIGINAL is not a valid setting for all objects.
*/
#define UF_OBJ_is_valid_inherited_width( width ) \
    ( ((width) == UF_OBJ_WIDTH_ORIGINAL) || UF_OBJ_is_valid_width(width) )

/* 
*/

#define UF_OBJ_NAME_NCHARS       128 
#define UF_OBJ_NAME_BUFSIZE      NX_BUFSIZE(UF_OBJ_NAME_NCHARS)
/*
   UF_OBJ_NAME_LEN is being deprecated because NX is moving to support
   multibyte characters.  User written programs should start using the
   new definitions above for object names:
     UF_OBJ_NAME_BUFSIZE should be used for buffer allocations and memory
                         allocations, e.g. char my_obj_name[UF_OBJ_NAME_BUFSIZE]
     UF_OBJ_NAME_NCHARS  should be used to limit the number of characters in
                         a buffer.  NX code will enforce these limits.
   New routines have been added which will help in this transition:
     UF_TEXT_count_characters() will count the number of characters in a string.
     UF_TEXT_truncate() will terminate a C string such that it will fit in a
                        buffer of a given size and not exceed a character count.

   MAX_INFO_NAME_LEN is being deprecated as it is unused.  User written programs
   should be changed to no longer use this definition.
*/
/*  */
#define UF_OBJ_NAME_LEN      (UF_OBJ_NAME_BUFSIZE-1)
#define MAX_INFO_NAME_LEN   (UF_OBJ_NAME_BUFSIZE*3)
/*  */



/* For use with UF_OBJ_ask_display_properties/UF_OBJ_cycle_by_name */
#define UF_OBJ_OK               0
#define UF_OBJ_NAME_NOT_FOUND   1

/* For use with view dependent edits */
#define UF_OBJ_FONT_INVISIBLE     0
#define UF_OBJ_FONT_SOLID         1
#define UF_OBJ_FONT_DASHED        2
#define UF_OBJ_FONT_PHANTOM       3
#define UF_OBJ_FONT_CENTERLINE    4
#define UF_OBJ_FONT_DOTTED        5
#define UF_OBJ_FONT_LONG_DASHED   6
#define UF_OBJ_FONT_DOTTED_DASHED 7

/*  special object types */
#define UF_OBJ_EXPR_TYPE                            65536
#define UF_OBJ_PART_TYPE                            65537

/* Display properties of the object */
struct UF_OBJ_disp_props_s {
        int     layer;                  /* the layer an object resides on */
        int     color;                  /* the color an object possesses */
        int     blank_status;           /* the blank status of an object 
                                           This status is defined by one of 
                                           the two string defined constants:
                                               UF_OBJ_NOT_BLANKED
                                               UF_OBJ_BLANKED
                                        */
        int     line_width;             /* the line width of an object 
                                           Can be one of the following :
                                               UF_OBJ_WIDTH_NORMAL
                                               UF_OBJ_WIDTH_THICK
                                               UF_OBJ_WIDTH_THIN
                                               UF_OBJ_WIDTH_ORIGINAL
                                               UF_OBJ_WIDTH_1 -- UF_OBJ_WIDTH_9
                                        */
        int     font;                   /* the font an object possesses */
        logical highlight_status;       /* the highlight status of an object 
                                            where TRUE indicates that highlight 
                                            is on.
                                        */
}; 

typedef struct UF_OBJ_disp_props_s UF_OBJ_disp_props_t, 
                                  *UF_OBJ_disp_props_p_t;


/******************************************************************************
 *
 *                  Color, Line Font and Width Settings
 *
 *****************************************************************************/

/* Structure used by UF_OBJ_ask_cre_settings and UF_OBJ_ask_def_cre_settings
 * to return color/line font/width settings
 * 
 */
struct UF_OBJ_cre_settings_s {
    int color;
    int line_font;
    int width;
};

typedef struct UF_OBJ_cre_settings_s UF_OBJ_cre_settings_t, 
                                    *UF_OBJ_cre_settings_p_t;


/* Type/Subtype Property Definitions
 *
 *   No Type/Subtype Properties
 */
#define UF_OBJ_no_property  (0)

/*   UF_solid_type Properties
 */
#define UF_OBJ_solid_body_property  (1)
#define UF_OBJ_sheet_body_property  (2)

/*   Translucency is an integer value in the range of
 *   0 (no translucency) to 100 (fully translucent).  It
 *   applies only to object types which may be shaded, such
 *   as solid/sheet bodies, solid/sheet faces, and
 *   faceted representations.
 */
typedef int UF_OBJ_translucency_t, *UF_OBJ_translucency_p_t;




#ifdef __cplusplus
}
#endif

#endif /* UF_OBJ_TYPES_INCLUDED */
