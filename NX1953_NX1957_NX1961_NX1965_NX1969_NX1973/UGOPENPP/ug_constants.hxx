/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX constant definitions.

================================================================================

*/

#ifndef UG_CONSTANTS_INCLUDED
#define UG_CONSTANTS_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <uf_part.h>
#include <uf_obj.h>

#ifndef SUPPORT_MORE_LINE_FONTS

#define SUPPORT_MORE_LINE_FONTS   (1)

#endif

// This enum defines the part units available during an Open API session.
enum UgUnits
{
    Millimeters  = UF_PART_METRIC,              // The part is in millimeters
    Inches       = UF_PART_ENGLISH              // The part is in inches
};


//  Constants of type UgColor should no longer be used.
//
//  UgColor constants such as Blue and Green define color indices. In 
//  releases prior to NX3, each defined index referenced the indicated 
//  color in the default color definition file (CDF) provided with NX. 
//  For example, the default CDF assigned blue to color index Blue (1), 
//  green to color index Blue (2), etc.
//
//  Beginning with NX3, the default CDF does not assign these colors 
//  to these indices. The default CDF assigns pale/light colors to 
//  color indices 1 through 15 instead of the familiar legacy colors 
//  (green, blue, cyan, etc.). Using UgColor constants with the default 
//  CDF will not produce the expected color.
// 
//  Instead of using the constants, call one of the following functions 
//  to obtain the color index that references the desired color.  
//      UF_DISP_ask_closest_color
//      UF_DISP_ask_closest_color_in_part
//      UF_DISP_ask_closest_color_in_displayed part
//
enum UgColor 
{
    Blue         = UF_OBJ_BLUE,                 // The color blue      
    Green        = UF_OBJ_GREEN,                // The color green
    Cyan         = UF_OBJ_CYAN,                 // The color cyan
    Red          = UF_OBJ_RED,                  // The color red
    Magenta      = UF_OBJ_MAGENTA,              // The color magenta
    Yellow       = UF_OBJ_YELLOW,               // The color yellow
    White        = UF_OBJ_WHITE,                // The color white
    Olive        = UF_OBJ_OLIVE,                // The color olive
    Pink         = UF_OBJ_PINK,                 // The color pink
    Brown        = UF_OBJ_BROWN,                // The color brown
    Orange       = UF_OBJ_ORANGE,               // The color orange
    Purple       = UF_OBJ_PURPLE,               // The color purple
    DarkRed      = UF_OBJ_DARK_RED,             // The color dark red
    Aquamarine   = UF_OBJ_AQUAMARINE,           // The color aquamarine
    Gray         = UF_OBJ_GRAY,                 // The color gray
    ColorMax     = UF_OBJ_MAX_COLOR             // Max color 
};

// This enum defines the line fonts available during an Open API session.
#if SUPPORT_MORE_LINE_FONTS
enum UgLineFont
{
    Solid = UF_OBJ_FONT_SOLID,           // The solid line font     
    Dashed = UF_OBJ_FONT_DASHED,          // The dashed line font
    Phantom = UF_OBJ_FONT_PHANTOM,         // The phantom line font
    CenterLine = UF_OBJ_FONT_CENTERLINE,      // The centerline line font
    Dotted = UF_OBJ_FONT_DOTTED,          // The dotted line font
    LongDashed = UF_OBJ_FONT_LONG_DASHED,     // The long dashed line font
    DottedDashed = UF_OBJ_FONT_DOTTED_DASHED,    // The dotted dashed line font    
    UgLineFont_8 = UF_OBJ_LINE_FONT_8,   // Undulating
    UgLineFont_9 = UF_OBJ_LINE_FONT_9,  // Zigzag
    UgLineFont_10 = UF_OBJ_LINE_FONT_10,  // Dash double dotted
    UgLineFont_11 = UF_OBJ_LINE_FONT_11   // Railway
};
#else
enum UgLineFont
{
    Solid        = UF_OBJ_FONT_SOLID,           // The solid line font     
    Dashed       = UF_OBJ_FONT_DASHED,          // The dashed line font
    Phantom      = UF_OBJ_FONT_PHANTOM,         // The phantom line font
    CenterLine   = UF_OBJ_FONT_CENTERLINE,      // The centerline line font
    Dotted       = UF_OBJ_FONT_DOTTED,          // The dotted line font
    LongDashed   = UF_OBJ_FONT_LONG_DASHED,     // The long dashed line font
    DottedDashed = UF_OBJ_FONT_DOTTED_DASHED    // The dotted dashed line font    
};
#endif
// This enum defines the line widths available during an Open API session.
enum UgLineWidth 
{
    Normal       = UF_OBJ_WIDTH_NORMAL,         // The normal line width
    Thick        = UF_OBJ_WIDTH_THICK,          // The thick line width
    Thin         = UF_OBJ_WIDTH_THIN,           // The thin line width
    Width_1      = UF_OBJ_WIDTH_1,
    Width_2      = UF_OBJ_WIDTH_2,
    Width_3      = UF_OBJ_WIDTH_3,
    Width_4      = UF_OBJ_WIDTH_4,
    Width_5      = UF_OBJ_WIDTH_5,
    Width_6      = UF_OBJ_WIDTH_6,
    Width_7      = UF_OBJ_WIDTH_7,
    Width_8      = UF_OBJ_WIDTH_8,
    Width_9      = UF_OBJ_WIDTH_9
};

#endif  // UG_CONSTANTS_INCLUDED
