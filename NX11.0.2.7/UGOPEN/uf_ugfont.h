/*===================================================================================*
 *                                                                                   *
 *       Copyright 2011 Siemens Product Lifecycle Management Software Inc.           *
 *                                All Rights Reserved.                               *
 *                                                                                   *
 *===================================================================================*



File description: 

The Open C API interface to functions which will access character font information
in a part.  Most functions require an font table entity tag (FTE tag).  This 
can be obtained by:

   tag_t fte_tag = NULL;
   UF_OBJ_cycle_objs_in_part(part_tag, UF_font_table_type, fte_tag);

The part tag can be for any part, or can be obtained by calling
UF_ASSEM_ask_work_part();

These functions allow you to:
 . Add a font to the Font Table Entity.
 . Query the font header structure for a specified font.
 . Get the font name of a given font index number.
 . Query the number of fonts in the Font Table Entity.
 . Query the font number of an existing font (see UF_UGFONT_add_font).


***************************************************************************/
#ifndef UF_UGFONT_H_INCLUDED
#define UF_UGFONT_H_INCLUDED
/***************************************************************************

  ***************************************************************************/
/*
 *      NOTE: Programmers are invited to maintain this header file by
 *            revising the File description, adding new (appropriate)
 *            function prototypes, removing obsolete or inappropriate
 *            prototypes, including headers which define required types
 *            and of course adding comments.
 */

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/* The following structure defines the font header.  These are
   parameters that effect all of the characters in the font.
*/
struct UF_UGFONT_font_header_s
{
    int version;          /* This is the internal version number.  It
                             identifies the format of the font binary file.
                             Currently this is version 1. */
    int height;           /* This is the height of the font.  This value
                             is the maximum Y value a character in the font
                             may have.  */
    int width;            /* This is the width of the font.  This value is
                             the maximum X value a character in the font
                             may have. */
    int base_height;      /* This is the distance to the base line of the
                             characters.  The base line is the bottom of
                             upper case characters. */
    int waist_height;     /* This is the distance to the waist line of the
                             characters.  The waist line is the top of most
                             lower case characters. */
                             
    int width_type;       /* This is the width type of the font:
                                1 = Fixed width, all characters have the same
                                    width.
                                2 = Variable width, characters vary the width
                                    based on their shape.
                                3 = Variable overlap font, the width of a
                                    character varies by its shape and the shape
                                    of characters around it.
                          */
    int overlap_1;        /* The overlap 1 value */
    int overlap_2;        /* The overlap 2 value */
    int overlap_3;        /* The overlap 3 value */
    double line_spacing;  /* The line spacing of the font.  This defines the
                             distance between two lines of characters. */
    double char_spacing;  /* The character spacing of the font.  This defines
                             the distance between two characters on the same
                             line.
                          */
    double grid_spacing;  /* The grid spacing.  This value is computed when the
                             font was first created, and is the distance 
                             assigned to one unit of the font height or 
                             width. */
    int number_of_chars;  /* This is the total number of characters that are
                             defined in this font. */
};

typedef struct UF_UGFONT_font_header_s UF_UGFONT_font_header_t;

/* This enumerated type provides the various types of fonts that can 
   exist in the Font Table Entity (FTE)
*/
enum UF_UGFONT_type_e
{
    UF_UGFONT_NX = 0,       /* Font is an NX font.  This represents all 
                               fonts prior to NX 7.5. */
    UF_UGFONT_STANDARD = 1, /* Font is a standard system font */
    UF_UGFONT_EMPTY = 10    /* Font does not exist */
};
typedef enum UF_UGFONT_type_e
             UF_UGFONT_type_t, *UF_UGFONT_type_p_t;

/**************************************************************************
Returns the font name of the specified font index number.  The font name
may be NULL.  This can happen if part cleanup has removed a font as being
unused.  The font index number still exists, but since there is not a font 
name, the output font_name will be NULL.  If a font returns a NULL font name,
then it is not a valid font to use.

The user must call UF_free to free the resulting font name.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_ask_font_name(
tag_t fte ,/* <I>
           The tag of the Font Table Entity (FTE).
           */
int  index ,/* <I>
            The font index number
            */
char ** font_name  /* <OF,len:index>
                   The font name. Use UF_free to deallocate
                   memory when done.
                   */
);

/**************************************************************************
Adds a font to the Font Table Entity (FTE) if it does not exist. If the
font already exists, the index of the existing font is returned. This
function returns the font index number for the FTE.  Note that adding a font
will use the first available slot in the FTE (one that has a NULL font name).

This will only add NX fonts.  Use UF_UGFONT_add_standard_font to add
Standard fonts.

Environment: Internal  and  External

See Also: UF_UGFONT_add_standard_font

History: Originally release in V14.0
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_add_font(
tag_t fte ,/* <I>
           The tag of the Font Table Entity (FTE).
           */
int * index ,/* <O>
             Font index number for the specified font
             */
char * font  /* <I>
             The name of the font
             */
);

/**************************************************************************
Adds a standard font to the Font Table Entity (FTE) if it does not exist. 
If the font already exists, the index of the existing font is returned. This
function returns the font index number for the FTE.  Note that adding a font
will use the first available slot in the FTE (one that has a NULL font name).

Environment: Internal  and  External

See Also:

History: Originally release in NX 7.5
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_add_standard_font(
tag_t fte ,/* <I>
           The tag of the Font Table Entity (FTE).
           */
int * index ,/* <O>
             Font index number for the specified font
             */
char * font  /* <I>
             The name of the font
             */
);

/**************************************************************************
Returns the number of entries in the Font Table Entity (FTE).  Each entry
may be a valid font or an entry that has been previously deleted.  The only way
to validate if a font number is usable is to call UF_UGFONT_ask_font_name.
If that returns a non-NULL name, then the font number is valid and can be used.
If UF_UGFONT_ask_font_name returns NULL for the name, then the font number
is not valid (it has been deleted using part cleanup).

Environment: Internal  and  External

See Also:

History: Originally release in V14.0
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_ask_number_of_fonts(
tag_t fte ,/* <I>
           The tag of the Font Table Entity (FTE).
           */
int * num  /* <O>
           The number of font entries in the FTE.  Some of the font entries
           may be currently unused, if part cleanup has been run on the part.
           */
);

/**************************************************************************
Fills in the UF_UGFONT_font_header_s structure with font information 
for a given font. 

This only works for NX fonts.

Environment: Internal  and  External

See Also:

History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_ask_font_header(
tag_t fte, /* <I>
              Tag of the font table entity */
int font,  /* <I> 
              font index */
UF_UGFONT_font_header_t *header /* <O>
                                   filled in UF_UGFONT_font_header_t structure
                                */
);

/**************************************************************************
UF_UGFONT_replace_font 
Change the particular font number to a new name in the Font Table Entry (FTE)

To replace the font type as well as the font name, use UF_UGFONT_replace_font_1.

Environment: Internal  and  External

See Also: UF_UGFONT_replace_font_1

History: This function was originally released in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_replace_font(
tag_t fte, /* <I>
            The tag of the Font Table Entity (FTE)
            */
int index, /* <I>
           Font index number for the old font to replace
           */
const char *const font /* <I>
                  The name of the new font 
                  */
);

/**************************************************************************
UF_UGFONT_replace_font_1 
Change the particular font number to a new name and new type in the 
Font Table Entry (FTE)

Environment: Internal  and  External

See Also:

History: This function was originally released in NX 7.5
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_replace_font_1(
tag_t fte, /* <I>
            The tag of the Font Table Entity (FTE)
            */
int index, /* <I>
           Font index number for the old font to replace
           */
UF_UGFONT_type_t type, /* <I>
                      The type of the new font
                      */
const char *const font /* <I>
                       The name of the new font
                       */
);

/**************************************************************************
UF_UGFONT_ask_font_type
Return the type of a font in the Font Table Entry (FTE)

Environment: Internal  and  External

See Also:

History: This function was originally released in NX 7.5
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_ask_font_type(
tag_t fte, /* <I>
            The tag of the Font Table Entity (FTE)
            */
int index, /* <I>
           Font index number of the font to check on
           */
UF_UGFONT_type_t *type /* <O>
                       The type of the font
                       */
);

/**************************************************************************
UF_UGFONT_ask_font_styles
Return the font styles available for a font in the Font Table Entry (FTE)

Environment: Internal  and  External

See Also:

History: This function was originally released in NX 8.0
 ***************************************************************************/
extern UFUNEXPORT int UF_UGFONT_ask_font_styles(
tag_t fte, /* <I>
            The tag of the Font Table Entity (FTE)
            */
int index, /* <I>
           Font index number of the font to check on
           */
int *num_styles, /* <O>
                 The number of style names in the style_names array.
                 This will be zero if the index input is not that of
                 a font in the Font Table Entity, or if the index is
                 that of an NX Legacy font (not that of a Standard Font).
                 */
char ***styles /* <OF,len:num_styles>
                An array of the names of available styles for the given font.
                This must be freed by the caller, using UF_free.
                */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_UGFONT_H_INCLUDED */
