/*==============================================================================

             Copyright (c) 1999-2003 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved
================================================================================
File description:

    This file contains both an internal and external User Function program
    that outputs a part's Geometric Tolerancing data to a tab delimited
    file and/or the information window.  Each row of data output contains
    information on one of the following:
        Datum
        Datum target
        Directed dimension
        Size tolerance
        Single feature control frame
        Upper or lower portion of a composite feature control frame
        Empty tolerance feature

Customization:

    Use the UFD_GDT_REPORT_SETTINGS_FILE environment variable to point to a
    file that defines the list of data to output in the order that it will be
    shown.  This file will contain the title of a column of data to output
    per line.  Only the column titles appearing in the file will be shown.
    Thus, to omit a column simply omit its title from the file.  Note that
    the columns will appear in the order that they are specified in the file.

    The following are valid data column titles:

        Tolerance Number
        Part Name
        Feature Name
        Retained
        Description
        Faces
        Geometric Definition
        Tolerance Type
        Geometry
        Pattern
        Views
        Pulled From
        Parent Feature
        Child Features
        Linked Features
        Pulled From Tolerance
        Callout
        Entire Callout
        Tolerance Band
        Standard Keywords
        User Keywords
        Above App Text
        Below App Text
        Before App Text
        After App Text
        Primary Datum
        Secondary Datum
        Tertiary Datum
        Related Faces
        Nominal Size

    See the ufd_gdt_report_settings.dat file for an example.

    Use the UFD_GDT_REPORT_FILE environment variable to point to the tab
    delimited file to output the data to.  Note that this file will be
    overwritten if it already exists.

    Define the UFD_GDT_REPORT_INFOWIN environment variable to indicate that
    data should be output to the information window.

Build comments:

    To compile the internal User Function program the INTERNAL_UFUN #define
    must be defined.  To compile the external User Function program the
    INTERNAL_UFUN #define must not be defined.


==============================================================================*/

#include <uf_defs.h>
#include <ctype.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <uf.h>
#include <uf_assem.h>
#include <uf_cfi.h>
#include <uf_drf.h>
#include <uf_gdt.h>
#include <uf_modl.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_view.h>

#define  INTERNAL_UFUN
/*---------------------------------------------------------------------------*
 * Macro used for debugging to check the return codes from UF_GDT functions
 *
 * NOTE: This is a noop if it is not compiled with DEBUG defined
 *---------------------------------------------------------------------------*/
#ifdef DEBUG

#define DEBUG_ASSERT( condition ) \
    { if ( !(condition) ) printf( "Assertion failed: (%s)\n", #condition ); }

#define DUMP_ERROR( args ) { print_error args; }

#else

#define DEBUG_ASSERT( condition ) { }
#define DUMP_ERROR( args ) { }

#endif

#define ERROR_CHECK( status, args ) \
    { if ( status != UF_GDT_NO_ERRORS ) DUMP_ERROR( args ); }

#define UFD_GDT_IS_SIZE_TOLERANCE_TYPE( type )               \
    ( ( (type) == UFD_GDT__SIZE_TOLERANCE_TYPE      || \
        (type) == UFD_GDT__WALL_THICKNESS_TYPE || \
        (type) == UFD_GDT__LIMITS_AND_FITS_TOLERANCE_TYPE || \
        (type) == UFD_GDT__DEPTH_TOLERANCE_TYPE ) ? TRUE : FALSE )

/*---------------------------------------------------------------------------*
 * Macro used to obtain the number of elements in a static array
 *---------------------------------------------------------------------------*/
#define NUM_ELEMENTS( array ) ( sizeof( array ) / sizeof( array[0] ) )

/*---------------------------------------------------------------------------*
 * Keyword control character definitions
 *---------------------------------------------------------------------------*/
#define UFD_GDT__KEYWORD_CCHAR      "<*KEYWORD "
#define UFD_GDT__KEYWORD_CCHAR_LEN  strlen( UFD_GDT__KEYWORD_CCHAR )
#define UFD_GDT__ARG_CCHAR          "<*>"
#define UFD_GDT__ARG_CCHAR_LEN      strlen( UFD_GDT__ARG_CCHAR )

/*---------------------------------------------------------------------------*
 * Possible UFD_GDT error codes
 *---------------------------------------------------------------------------*/
#define UFD_GDT__ERR_NO_PART               (101)
#define UFD_GDT__ERR_NO_REPORT_OUTPUT_DATA (102)

/*---------------------------------------------------------------------------*
 * Possible information types to show in report
 *---------------------------------------------------------------------------*/
typedef enum
{
    UFD_GDT__TOLERANCE_NUMBER_INFO,
    UFD_GDT__PART_NAME_INFO,
    UFD_GDT__TOLERANCE_FEATURE_NAME_INFO,
    UFD_GDT__RETAINED_STATUS_INFO,
    UFD_GDT__DESCRIPTION_INFO,
    UFD_GDT__FACES_INFO,
    UFD_GDT__GEOMETRIC_DEFINITION_TYPE_INFO,
    UFD_GDT__TOLERANCE_TYPE_INFO,
    UFD_GDT__GEOMETRY_TYPE_INFO,
    UFD_GDT__PATTERN_TYPE_INFO,
    UFD_GDT__DISPLAY_INSTANCE_VIEWS_INFO,
    UFD_GDT__PULLED_FROM_INFO,
    UFD_GDT__PARENT_TOLERANCE_FEATURE_INFO,
    UFD_GDT__CHILD_TOLERANCE_FEATURES_INFO,
    UFD_GDT__LINKED_TOLERANCE_FEATURES_INFO,
    UFD_GDT__PULLED_FROM_TOLERANCE_NUMBER_INFO,
    UFD_GDT__CALLOUT_STRING_INFO,
    UFD_GDT__ENTIRE_CALLOUT_STRING_INFO,
    UFD_GDT__TOLERANCE_BAND_INFO,
    UFD_GDT__STANDARD_KEYWORDS_INFO,
    UFD_GDT__USER_DEFINED_KEYWORDS_INFO,
    UFD_GDT__ABOVE_APPENDED_TEXT_INFO,
    UFD_GDT__BELOW_APPENDED_TEXT_INFO,
    UFD_GDT__BEFORE_APPENDED_TEXT_INFO,
    UFD_GDT__AFTER_APPENDED_TEXT_INFO,
    UFD_GDT__PRIMARY_DATUM_INFO,
    UFD_GDT__SECONDARY_DATUM_INFO,
    UFD_GDT__TERTIARY_DATUM_INFO,
    UFD_GDT__RELATED_FACES_INFO,
    UFD_GDT__NOMINAL_SIZE_INFO,
    UFD_GDT__DISPLAYED_LOWER_LIMIT_INFO,
    UFD_GDT__DISPLAYED_UPPER_LIMIT_INFO,
    UFD_GDT__NUM_INFO_TYPES
} UFD_GDT__info_type_t, *UFD_GDT__info_type_p_t;

/*---------------------------------------------------------------------------*
 * Constants used to define the type of tolerance being queried
 *---------------------------------------------------------------------------*/
typedef enum
{
    UFD_GDT__NO_TYPE = -1,
    UFD_GDT__EMPTY_FEATURE_TYPE,
    UFD_GDT__DATUM_IDENTIFIER_TYPE,
    UFD_GDT__DATUM_TARGET_POINT_TYPE,
    UFD_GDT__DATUM_TARGET_LINE_TYPE,
    UFD_GDT__DATUM_TARGET_DIA_TYPE,
    UFD_GDT__DATUM_TARGET_RECT_TYPE,
    UFD_GDT__DATUM_TARGET_CYL_TYPE,
    UFD_GDT__DATUM_MULTIPLE_TYPE,
    UFD_GDT__FEATURE_CONTROL_FRAME_TYPE,
    UFD_GDT__SIZE_TOLERANCE_TYPE,
    UFD_GDT__WALL_THICKNESS_TYPE,
    UFD_GDT__DEPTH_TOLERANCE_TYPE,
    UFD_GDT__LIMITS_AND_FITS_TOLERANCE_TYPE,
    UFD_GDT__THREAD_TOLERANCE_TYPE,
    UFD_GDT__ANGULAR_DIRECTED_DIMENSION_TYPE,
    UFD_GDT__LINEAR_DIRECTED_DIMENSION_TYPE
} UFD_GDT__object_type_t, *UFD_GDT__object_type_p_t;

/*---------------------------------------------------------------------------*
 * Possible output values for compare function
 *---------------------------------------------------------------------------*/
typedef enum
{
    UFD_GDT__LESS_THAN    = -1,
    UFD_GDT__EQUAL        =  0,
    UFD_GDT__GREATER_THAN =  1
} UFD_GDT__compare_result_t;

/*---------------------------------------------------------------------------*
 * Structure used to define types of report output available
 *---------------------------------------------------------------------------*/
typedef enum
{
    UFD_GDT__NO_OUTPUT,
    UFD_GDT__FILE_OUTPUT,
    UFD_GDT__INFO_WINDOW_OUTPUT
} UFD_GDT__output_type_t, *UFD_GDT__output_type_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to contain data on where to output the report
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__output_data_s
{
    UFD_GDT__output_type_t type; /* Type of output                        */
    FILE *file;                  /* File pointer only if the type is      */
                                 /* UFD_GDT__FILE_OUTPUT; otherwise, NULL */
    char *delimiter;             /* NULL indicates fixed line columns     */
} UFD_GDT__output_data_t, *UFD_GDT__output_data_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to contain data on how the report is displayed
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__output_list_s
{
    int count;                     /* Number of places to output the report */
    UFD_GDT__output_data_p_t list; /* List of places to output the report   */
} UFD_GDT__output_list_t, *UFD_GDT__output_list_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to contain a single column of data contained in a report row
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__info_data_s
{
    UFD_GDT__info_type_t type; /* Type of information in data string        */
    char *data;                /* Information data string of the given type */
} UFD_GDT__info_data_t, *UFD_GDT__info_data_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to contain the data for a single row in the report
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__object_info_s
{
    tag_t part;                  /* Part containing tolerance feature      */
    tag_t feature;               /* Tolerance feature containing tolerance */
    tag_t tolerance;             /* Tolerance queried                      */
    UFD_GDT__object_type_t tolerance_type;
                                 /* Type of tolerance queried              */
    int   count;                 /* Number of tolerance data fields        */
    UFD_GDT__info_data_p_t list; /* Tolerance data fields for a report row */
} UFD_GDT__object_info_t, *UFD_GDT__object_info_p_t;

/*---------------------------------------------------------------------------*
 * Callback function used to compare two sets of the same type of info data
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if info1 < info2
 *     UFD_GDT__EQUAL        if info1 = info2
 *     UFD_GDT__GREATER_THAN if info1 > info2
 *---------------------------------------------------------------------------*/
typedef UFD_GDT__compare_result_t (*UFD_GDT__compare_f_t)(
    const UFD_GDT__info_data_p_t info1,
    const UFD_GDT__info_data_p_t info2,
    void *client_data
);

/*---------------------------------------------------------------------------*
 * Structure defining a single data field in the report
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__report_field_s
{
    UFD_GDT__info_type_t type;   /* Type of info contained in the field      */
    char                *title;  /* Title of the field                       */
    UFD_GDT__compare_f_t compare;/* Function to use for comparing fields of  */
                                 /* the same type when comparing report rows */
    int                  max_len;/* Largest string length of this data field */
                                 /* the report                               */
} UFD_GDT__report_field_t, *UFD_GDT__report_field_p_t;

/*---------------------------------------------------------------------------*
 * Callback function used to display a single row in the report.
 *---------------------------------------------------------------------------*/
typedef void (*UFD_GDT__output_line_f_t)(
    const int num_fields,                   /* <I>   Number of report fields */
    const UFD_GDT__report_field_p_t fields, /* <I>   List of report fields   */
    const UFD_GDT__object_info_p_t info,    /* <I>   Row data to output      */
    void *client_data                       /* <I/O> Client data             */
);

/*---------------------------------------------------------------------------*
 * Structure used for the list of data defining report rows for the part
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__part_info_s
{
    int alloc;                      /* Number of list elements allocated  */
    int count;                      /* Number of elements in the list     */
    UFD_GDT__object_info_p_t lines; /* List of object data.  Each element */
                                    /* defines a single row in the report */
} UFD_GDT__part_info_t, *UFD_GDT__part_info_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to define a part report
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__report_s
{
    int num_fields;                      /* Number of fields to report on    */
    UFD_GDT__report_field_p_t fields;    /* Fields of report in the order    */
                                         /* that they will appear            */
    UFD_GDT__output_line_f_t output_fun; /* Function to display a single row */
                                         /* the report                       */
    void *client_data;                   /* Data passed to output_fun        */
    UFD_GDT__part_info_t part_info;      /* Report data for each tolerance   */
                                         /* the part                         */
} UFD_GDT__report_t, *UFD_GDT__report_p_t;

/*---------------------------------------------------------------------------*
 * Structure used for passing tolerance feature data between functions that
 * query the data
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__feature_data_s
{
    tag_t part;                 /* Part being queried                       */
    tag_t feature;              /* Tolerance feature being queried          */
    UF_GDT_feature_parms_p_t feature_parms;
                                /* Tolerance feature parms data             */
    UF_GDT_geometric_definition_p_t geom_def;
                                /* Tolerance feature geometric definition   */
    int num_callout_strings;    /* Number of callout strings in the         */
                                /* tolerance feature                        */
    UF_GDT_callout_string_p_t callout_strings;
                                /* List of callout strings in the tolerance */
                                /* feature                                  */
} UFD_GDT__feature_data_t, *UFD_GDT__feature_data_p_t;

/*---------------------------------------------------------------------------*
 * Structure to be used for data caching
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__cached_s
{
    UFD_GDT__report_p_t report; /* Pointer to current report settings */
} UFD_GDT__cached_t, *UFD_GDT__cached_p_t;

/*---------------------------------------------------------------------------*
 *                         Local Function Prototypes
 *---------------------------------------------------------------------------*/
static void print_error( char *msg, int error_code, const char *format, ... );

/*---------------------------------------------------------------------------*
 * Cached data
 *---------------------------------------------------------------------------*/
static UFD_GDT__cached_t UFD_GDT__cached = { NULL };

static UF_GDT_size_tolerance_p_t convert_depth_data_to_size_data(
    UF_GDT_depth_tolerance_p_t depth_tol_data
);

/*---------------------------------------------------------------------------*
 * Get the cached report client data
 *
 * Returns:
 *     Cached report client data
 *---------------------------------------------------------------------------*/
static void *UFD_GDT__ask_client_data( void )
{
    return ( UFD_GDT__cached.report->client_data );
}

/*---------------------------------------------------------------------------*
 * Get the cached report definition
 *
 * Returns:
 *     Cached report structure
 *---------------------------------------------------------------------------*/
static UFD_GDT__report_p_t UFD_GDT__ask_report( void )
{
    return ( UFD_GDT__cached.report );
}

/*---------------------------------------------------------------------------*
 * Cache the current report definition
 *---------------------------------------------------------------------------*/
static void UFD_GDT__set_report(
    UFD_GDT__report_p_t report   /* <I> Report definition to cache */
)
{
    UFD_GDT__cached.report = report;
}

/*---------------------------------------------------------------------------*
 * Reallocate a list of elements of a given byte size
 *
 * Returns:
 *     The reallocated list
 *---------------------------------------------------------------------------*/
static void *realloc_list(
    int   size,      /* <I>   Size (in bytes) of one element in the list    */
    int   increment, /* <I>   Number of elements to add to the list if it   */
                     /*       to be increased in size                       */
    int  *alloc,     /* <I/O> Number of elements allocated for in the list  */
    int   count,     /* <I>   Number of elements in the list                */
    void *list       /* <I>   List of elements to reallocate.               */
                     /*       NOTE: This pointer may be invalid if the list */
                     /*             is reallocated                          */
)
{
    if ( count == *alloc )
    {
        int status;

        *alloc += increment;
        list = UF_reallocate_memory( list, *alloc * size, &status );
        ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );
    }

    return ( list );
}

/*---------------------------------------------------------------------------*
 * Allocate a string of the specified length
 *
 * Returns:
 *     Allocated string initialized to the empty string
 *---------------------------------------------------------------------------*/
static char *alloc_string(
    int  length                 /* <I> Length of string                      */
                                /*     NOTE: '\0' is included in this length */
)
{
    if ( length <= 0 )
        return ( NULL );
    else
    {
        char *str;
        int status;

        str = (char *)UF_allocate_memory( length * sizeof( char ), &status );
        ERROR_CHECK( status, ( "UF_allocate_memory", status, "" ) );

        strcpy( str, "" );

        return ( str );
    }
}

/*---------------------------------------------------------------------------*
 * Allocate a string of the specified length
 *
 * Returns:
 *     Allocated string initialized to the empty string
 *---------------------------------------------------------------------------*/
static char *alloc_char_string(
    int  length,            /* <I> Length of string                          */
                            /*     NOTE: '\0' is not included in this length */
    char fill_char          /* <I> Character to fill string with             */
)
{
    char *str = alloc_string( length + 1 );

    if ( str != NULL )
    {
        int pos;

        for ( pos = 0; pos < length; pos++ )
            str[pos] = fill_char;

        str[length] = '\0';
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Reallocate a string
 *
 * Returns:
 *     Reallocated string of the specified length
 *---------------------------------------------------------------------------*/
static char *realloc_string(
    char *str,                  /* <I> String to reallocate                  */
                                /*     NOTE: This pointer may be invalid     */
                                /*           after the string is reallocated */
    int   length                /* <I> Length of reallocated string          */
                                /*     NOTE: '\0' is included in this length */
)
{
    if ( length <= 0 )
    {
        UF_free( str );
        return ( NULL );
    }
    else
    {
        if ( str == NULL )
            str = alloc_string( length );
        else
        {
            int status;

            str = (char *) UF_reallocate_memory( str, length * sizeof( char ),
                                                 &status );
            ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );
        }

        return ( str );
    }
}

/*---------------------------------------------------------------------------*
 * Copy the input string to a newly allocated string
 *
 * Returns:
 *     Allocated string copy of the input string
 *---------------------------------------------------------------------------*/
static char *copy_string(
    char *str                   /* <I> String to copy */
)
{
    char *copy = NULL;

    if ( str != NULL )
    {
        int length = strlen( str );

        if ( length > 0 )
        {
            copy = alloc_string( length + 1 );
            strcpy( copy, str );
        }
    }
    else
    {
        copy = alloc_string( 1 );
        strcpy( copy, "" );
    }

    return ( copy );
}

/*---------------------------------------------------------------------------*
 * Concatenate three strings
 *
 * Returns:
 *     Reallocated str1 with str2 and str3 concatenated to it
 *---------------------------------------------------------------------------*/
static char *concatenate_strings(
    char *str1, /* <I> String to concatenate to                           */
                /*     NOTE: This pointer may be invalid after the        */
                /*           concatenation is performed since this string */
                /*           will be reallocated                          */
    char *str2, /* <I> String to concatenate to str1                      */
    char *str3  /* <I> String to concatenate to str2                      */
)
{
    char *copy = NULL;
    int length2 = ( str2 == NULL ) ? 0 : strlen( str2 );
    int length3 = ( str3 == NULL ) ? 0 : strlen( str3 );

    if ( length2 == 0 && length3 == 0 )
        copy = str1;
    else
    {
        int length1 = ( str1 == NULL ) ? 0 : strlen( str1 );
        int length  = length1 + length2 + length3 + 1;

        copy = realloc_string( str1, length );

        if ( ( length2 > 0 ) && (str2 != NULL) )
            strcat( copy, str2 );

        if ( ( length3 > 0 ) && (str3 != NULL) )
            strcat( copy, str3 );
    }

    return ( copy );
}

/*---------------------------------------------------------------------------*
 * Remove all leading and trailing spaces from the input line.  Also, allow
 * at most one space in between two non-space characters.
 *
 * Returns:
 *     An allocated copy of the input line with all extra spaces removed.
 *---------------------------------------------------------------------------*/
static char *ask_string_no_extra_spaces(
    char *line                  /* <I> Line to remove extra spaces from */
)
{
    char *str = NULL;
    int beg_pos = 0, end_pos = 0;
    int len, line_len, str_len;
    int last_pos, pos;

    if ( line == NULL )
        return ( NULL );

    line_len = strlen( line );

    for ( pos = 0; pos < line_len; pos++ )
    {
        if ( !isspace( (int) line[pos] ) )
        {
            beg_pos = pos;
            break;
        }
    }

    for ( pos = line_len - 1; pos >= 0; pos-- )
    {
        if ( !isspace( (int) line[pos] ) )
        {
            end_pos = pos + 1;
            break;
        }
    }

    len = end_pos - beg_pos;
    str = alloc_string( len + 1 );
    str_len = 0;

    for ( last_pos = 0, pos = 0; pos < len; last_pos = pos, pos++ )
    {
        if ( !isspace( (int) line[pos] ) || !isspace( (int) line[last_pos] ) )
            str[str_len++] = line[pos];
    }

    str[str_len] = '\0';

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of info data
 * of the same type.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if info1 < info2
 *     UFD_GDT__EQUAL        if info1 = info2
 *     UFD_GDT__GREATER_THAN if info1 > info2
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
static UFD_GDT__compare_result_t compare_characters_no_case(
    const char char1,           /* <I> Character 1 to compare */
    const char char2            /* <I> Character 2 to compare */
)
{
    char upper_char1 = toupper( char1 );
    char upper_char2 = toupper( char2 );

    if ( upper_char1 < upper_char2 )
        return ( UFD_GDT__LESS_THAN );

    else if ( upper_char1 > upper_char2 )
        return ( UFD_GDT__GREATER_THAN );

    else
        return ( UFD_GDT__EQUAL );
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of info data
 * of the same type.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if info1 < info2
 *     UFD_GDT__EQUAL        if info1 = info2
 *     UFD_GDT__GREATER_THAN if info1 > info2
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
static UFD_GDT__compare_result_t compare_strings(
    const char *str1,           /* <I> String 1 to compare                   */
    const char *str2,           /* <I> String 2 to compare                   */
    const int  max_chars        /* <I> Maximum number of character to compare*/
                                /*      < 0 indicates the length of the      */
                                /*          longest string                   */
)
{
    if ( str1 == str2 )
        return ( UFD_GDT__EQUAL );

    else if ( str1 == NULL )
        return ( UFD_GDT__LESS_THAN );

    else if ( str2 == NULL )
        return ( UFD_GDT__GREATER_THAN );

    else
    {
        int pos;
        logical done = FALSE;
        UFD_GDT__compare_result_t result = UFD_GDT__EQUAL;

        for ( pos = 0; !done; pos++ )
        {
            result = compare_characters_no_case( str1[pos], str2[pos] );

            if ( result != UFD_GDT__EQUAL )
                done = TRUE;

            else if ( str1[pos] == '\0' && str2[pos] == '\0' )
                done = TRUE;

            else if ( max_chars >= 0 && pos >= ( max_chars - 1 ) )
                done = TRUE;
        }

        return ( result );
    }
}

/*---------------------------------------------------------------------------*
 * Function to return the number string stripped of leading zeros, its
 * character length and the original number string's character length.
 *---------------------------------------------------------------------------*/
static void ask_number_string(
    char  *str,                 /* <I> String begining with digit character  */
    int    max_chars,           /* <I> Maximum number of character to compare*/
                                /*      < 0 indicates the length of the      */
                                /*          longest string                   */
    char **num_str,             /* <O> Number string stripped of leading     */
                                /*     zeros                                 */
    int   *true_len,            /* <O> Length of number string               */
    int   *len                  /* <O> Length of number string stripped of   */
                                /*     leading zeros                         */
)
{
    int pos;

    *num_str  = str;
    *true_len = 0;

    for ( pos = 0; max_chars < 0 || pos < max_chars; pos++ )
    {
        if ( !isdigit( str[pos] ) )
            break;
        else
            (*true_len)++;
    }

    *len = *true_len;

    for ( pos = 0; pos < ( *true_len - 1 ) && str[pos] == '0'; pos++ )
    {
        (*len)--;
        (*num_str)++;
    }
}

/*---------------------------------------------------------------------------*
 * Compare two strings that may contain numbers.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if str1 < str2
 *     UFD_GDT__EQUAL        if str1 = str2
 *     UFD_GDT__GREATER_THAN if str1 > str2
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
static UFD_GDT__compare_result_t compare_strings_with_number(
    const char *str1,           /* <I> String 1 to compare                   */
    const char *str2,           /* <I> String 2 to compare                   */
    const int  max_chars        /* <I> Maximum number of character to compare*/
                                /*      < 0 indicates the length of the      */
                                /*          longest string                   */
)
{
    if ( str1 == str2 )
        return ( UFD_GDT__EQUAL );

    else if ( str1 == NULL )
        return ( UFD_GDT__LESS_THAN );

    else if ( str2 == NULL )
        return ( UFD_GDT__GREATER_THAN );

    else
    {
        int pos;
        logical done = FALSE;
        UFD_GDT__compare_result_t result = UFD_GDT__EQUAL;

        for ( pos = 0; !done && result == UFD_GDT__EQUAL; pos++ )
        {
            if ( isdigit( str1[pos] ) && isdigit( str2[pos] ) )
            {
                char *num_str1, *num_str2;
                int len1, len2, true_len1, true_len2;

                ask_number_string( (char *) &str1[pos], max_chars - pos,
                                   &num_str1, &true_len1, &len1 );

                ask_number_string( (char *) &str2[pos], max_chars - pos,
                                   &num_str2, &true_len2, &len2 );

                if ( len1 < len2 )
                    result = UFD_GDT__LESS_THAN;

                else if ( len1 > len2 )
                    result = UFD_GDT__GREATER_THAN;

                else
                {
                    result = compare_strings( num_str1, num_str2, len1 );

                    if ( result == UFD_GDT__EQUAL )
                    {
                        if ( true_len1 < true_len2 )
                            result = UFD_GDT__LESS_THAN;

                        else if ( true_len1 > true_len2 )
                            result = UFD_GDT__GREATER_THAN;

                        else
                            pos += true_len1 - 1;
                    }
                }
            }
            else
            {
                result = compare_characters_no_case( str1[pos], str2[pos] );

                if ( result == UFD_GDT__EQUAL )
                {
                    if ( str1[pos] == '\0' && str2[pos] == '\0' )
                        done = TRUE;

                    else if ( max_chars >= 0 && pos >= ( max_chars - 1 ) )
                        done = TRUE;
                }
            }
        }

        return ( result );
    }
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of info data
 * of the same type whose data may contain numbers.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if info1 < info2
 *     UFD_GDT__EQUAL        if info1 = info2
 *     UFD_GDT__GREATER_THAN if info1 > info2
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
static UFD_GDT__compare_result_t compare_info_data_with_number(
    const UFD_GDT__info_data_p_t info1, /* <I>   Info data 1 to compare */
    const UFD_GDT__info_data_p_t info2, /* <I>   Info data 2 to compare */
    void *client_data                   /* <I/O> Client data            */
)
{
    return ( compare_strings_with_number( info1->data, info2->data, -1 ) );
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of info data
 * of the same type.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if info1 < info2
 *     UFD_GDT__EQUAL        if info1 = info2
 *     UFD_GDT__GREATER_THAN if info1 > info2
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
static UFD_GDT__compare_result_t compare_info_data(
    const UFD_GDT__info_data_p_t info1, /* <I>   Info data 1 to compare */
    const UFD_GDT__info_data_p_t info2, /* <I>   Info data 2 to compare */
    void *client_data                   /* <I/O> Client data            */
)
{
    return ( compare_strings( info1->data, info2->data, -1 ) );
}

/*---------------------------------------------------------------------------*
 * Ask the string representation of the info data (i.e. report row) specified
 *
 * Returns:
 *     Allocated string representing a report row
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
static char *ask_fixed_length_line(
    const UFD_GDT__object_info_p_t info,
                                /* <I>   Data defining a report row          */
    const int num_fields,       /* <I>   Number of report fields             */
    const UFD_GDT__report_field_p_t fields
                                /* <I>   List of report fields               */
)
{
    int num, delimiter_len = 0;
    char *line = NULL;

    DEBUG_ASSERT( num_fields == info->count );

    for ( num = 0; num < info->count; num++ )
    {
        char *delimiter_str;

        if ( delimiter_len == 0 )
            delimiter_str = NULL;
        else
            delimiter_str = alloc_char_string( delimiter_len, ' ' );

        line = concatenate_strings( line, delimiter_str, info->list[num].data );

        UF_free( delimiter_str );

        delimiter_len = fields[num].max_len + 1;
        if ( info->list[num].data != NULL )
            delimiter_len -= strlen( info->list[num].data );
    }

    return ( line );
}

/*---------------------------------------------------------------------------*
 * Ask the string representation of the info data (i.e. report row) specified
 *
 * Returns:
 *     Allocated string representing a report row
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
static char *ask_output_line(
    const UFD_GDT__object_info_p_t info,
                                /* <I>   Data defining a report row          */
    const int num_fields,       /* <I>   Number of report fields             */
    const UFD_GDT__report_field_p_t fields,
                                /* <I>   List of report fields               */
    const char *delimiter,      /* <I>   Delimiter to use between report     */
                                /*       fields                              */
    const char *end_of_line,    /* <I>   String to concatenate at the end of */
                                /*       the output report row               */
    void *client_data           /* <I/O> Client data                         */
)
{
    char *line = NULL;

    if ( delimiter == NULL )
        line = ask_fixed_length_line( info, num_fields, fields );
    else
    {
        int num;
        char *delimiter_str = NULL;

        for ( num = 0; num < info->count; num++ )
        {
            line = concatenate_strings( line, delimiter_str, info->list[num].data );
            delimiter_str = (char *) delimiter;
        }
    }

    line = concatenate_strings( line, (char *) end_of_line, NULL );

    return ( line );
}

/*---------------------------------------------------------------------------*
 * Display a row in the report
 *---------------------------------------------------------------------------*/
static void print_output_line(
    const int num_fields,                   /* <I>   Number of report fields */
    const UFD_GDT__report_field_p_t fields, /* <I>   List of report fields   */
    const UFD_GDT__object_info_p_t info,    /* <I>   Data defining a report  */
                                            /*       row                     */
    void *client_data                       /* <I/O> Client data             */
)
{
    UFD_GDT__output_list_p_t data = (UFD_GDT__output_list_p_t) client_data;
    int num;

    for ( num = 0; num < data->count; num++ )
    {
        char *line;

        line = ask_output_line( info, num_fields, fields,
                                data->list[num].delimiter, "\n", client_data );

        if ( data->list[num].type == UFD_GDT__FILE_OUTPUT )
        {
            fprintf( data->list[num].file, "%s", line );
        }
        else if ( data->list[num].type == UFD_GDT__INFO_WINDOW_OUTPUT )
        {
            int status;

            status = UF_UI_write_listing_window( line );
            ERROR_CHECK( status, ( "UF_UI_write_listing_window", status,
                                   "line = %s", line ) );
        }

        UF_free( line );
    }
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of report
 * data defining rows.  Compare the part report rows by cycling through the
 * report fields in ascending order until the fields are no longer equal.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if row1 < row2
 *     UFD_GDT__EQUAL        if row1 = row2
 *     UFD_GDT__GREATER_THAN if row1 > row2
 *---------------------------------------------------------------------------*/
static int compare_rows(
    const void *ptr1,           /* <I> Row 1 data to compare */
    const void *ptr2            /* <I> Row 2 data to compare */
)
{
    void *client_data = UFD_GDT__ask_client_data();
    UFD_GDT__report_p_t report = UFD_GDT__ask_report();
    UFD_GDT__object_info_p_t info1 = (UFD_GDT__object_info_p_t) ptr1;
    UFD_GDT__object_info_p_t info2 = (UFD_GDT__object_info_p_t) ptr2;
    UFD_GDT__compare_result_t result = UFD_GDT__EQUAL;
    int num;

    for ( num = 0; num < report->num_fields; num++ )
    {
        result = (*report->fields[num].compare)( &info1->list[num],
                                                 &info2->list[num],
                                                 client_data );

        if ( result != UFD_GDT__EQUAL )
            break;
    }

    return ( result );
}

/*---------------------------------------------------------------------------*
 * Ask the error message with the associated error code
 *
 * Returns:
 *     The allocated error message
 *---------------------------------------------------------------------------*/
static char *ask_error_msg(
    int error_code
)
{
    char *str = NULL;
    char msg[ MAX_LINE_BUFSIZE ];

    switch ( error_code )
    {
        case UFD_GDT__ERR_NO_PART:
            str = "No part sprecified";
            break;

        case UFD_GDT__ERR_NO_REPORT_OUTPUT_DATA:
            str = "No output data specified";
            break;

        default:
            UF_get_fail_message( error_code, msg );
            str = msg;
            break;
    }

    return ( copy_string( str ) );
}

/*---------------------------------------------------------------------------*
 * Print the error message with the associated error code
 *---------------------------------------------------------------------------*/
static void print_error(
    char *msg,                  /* <I> Message header                   */
    int   error_code,           /* <I> Error code                       */
    const char *format,         /* <I> Format for arguments that follow */
    ...                         /* <I> Arguments for format             */
)
{
    va_list ap;

    if ( error_code == UF_GDT_NO_ERRORS )
        printf( "%s: ", msg );
    else
    {
        char *error_msg = ask_error_msg( error_code );

        printf( "%s: %s\n    ", msg, error_msg );
        UF_free( error_msg );
    }

    va_start( ap, format );

    vprintf( format, ap );

    va_end( ap );

    printf( "\n" );
}

/*---------------------------------------------------------------------------*
 * Add a new tolerance entry to the tolerance information list for the part
 *---------------------------------------------------------------------------*/
static void add_to_part_info_list(
    UFD_GDT__report_p_t      report,     /* <I/O> Report containing part */
                                         /*       tolerance information  */
    UFD_GDT__object_info_p_t object_info /* <I>   Tolerance information  */
)
{
    int num;

    report->part_info.lines = (UFD_GDT__object_info_p_t)
        realloc_list( sizeof(UFD_GDT__object_info_t), 100,
                      &report->part_info.alloc, report->part_info.count,
                      report->part_info.lines );

    report->part_info.lines[report->part_info.count++] = *object_info;

    for ( num = 0; num < report->num_fields; num++ )
    {
        if ( object_info->list[num].data != NULL )
        {
            int len = strlen( object_info->list[num].data );

            if ( len > report->fields[num].max_len )
                report->fields[num].max_len = len;
        }
    }
}

/*---------------------------------------------------------------------------*
 * Initialize the UFD_GDT__object_info structure with the specified data
 *---------------------------------------------------------------------------*/
static void init_info_data(
    UFD_GDT__report_p_t report,  /* <I> Report containing fields to query */
    tag_t part,                  /* <I> Part tag of tolerance feature     */
    tag_t feature,               /* <I> Tolerance feature tag             */
    tag_t tolerance,             /* <I> FCF tag or NULL_TAG               */
    UFD_GDT__object_type_t type, /* <I> Tolerance object type             */
    UFD_GDT__object_info_p_t object_info
                                 /* <O> Initialized internal object data  */
)
{
    int status, num;

    object_info->part           = part;
    object_info->feature        = feature;
    object_info->tolerance      = tolerance;
    object_info->tolerance_type = type;

    object_info->count = report->num_fields;
    object_info->list  = (UFD_GDT__info_data_p_t)
        UF_allocate_memory( object_info->count * sizeof( UFD_GDT__info_data_t ), &status );
    ERROR_CHECK( status, ( "UF_allocate_memory", status, "" ) );

    for ( num = 0; num < report->num_fields; num++ )
    {
        object_info->list[num].type = report->fields[num].type;
        object_info->list[num].data = NULL;
    }
}

/*---------------------------------------------------------------------------*
 * Free the data contained in the UFD_GDT__object_info structure
 *---------------------------------------------------------------------------*/
static void free_info_data(
    UFD_GDT__object_info_p_t object_info /* <O> Object data to free */
)
{
    int num;

    for ( num = 0; num < object_info->count; num++ )
        UF_free( object_info->list[num].data );

    UF_free( object_info->list );

    object_info->part           = NULL_TAG;
    object_info->feature        = NULL_TAG;
    object_info->tolerance      = NULL_TAG;
    object_info->tolerance_type = UFD_GDT__NO_TYPE;
    object_info->count          = 0;
    object_info->list           = NULL;
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of face tags.
 * Compare the faces by their face index.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if face_index1 < face_index2
 *     UFD_GDT__EQUAL        if face_index1 = face_index2
 *     UFD_GDT__GREATER_THAN if face_index1 > face_index2
 *---------------------------------------------------------------------------*/
static int compare_faces_by_index(
    const void *ptr1,           /* <I> Face 1 to compare */
    const void *ptr2            /* <I> Face 2 to compare */
)
{
    tag_p_t face1 = (tag_p_t) ptr1;
    tag_p_t face2 = (tag_p_t) ptr2;
    int face_index1, face_index2;
    int status = UF_GDT_NO_ERRORS;

    status = UF_GDT_ask_face_index( *face1, &face_index1 );
    ERROR_CHECK( status, ( "UF_GDT_ask_face_index", status, "face = %u",
                           *face1 ) );

    status = UF_GDT_ask_face_index( *face2, &face_index2 );
    ERROR_CHECK( status, ( "UF_GDT_ask_face_index", status, "face = %u",
                           *face2 ) );

    if ( face_index1 < face_index2 )
        return ( UFD_GDT__LESS_THAN );
    else if ( face_index1 > face_index2 )
        return ( UFD_GDT__GREATER_THAN );
    else
        return ( UFD_GDT__EQUAL );
}

/*---------------------------------------------------------------------------*
 * Get the string representation of the list of faces specified.  The faces
 * are listed by face index.
 *
 * Returns:
 *     Allocated face list string
 *---------------------------------------------------------------------------*/
static char *ask_face_list(
    int num_faces, /* <I> Number of faces in list */
    tag_p_t faces  /* <I> List of faces           */
)
{
    int num;
    char *delimiter = "";
    char *str = NULL;

    qsort( faces, num_faces, sizeof( tag_t ), compare_faces_by_index );

    for ( num = 0; num < num_faces; num++ )
    {
        int face_index, status;
        char face_index_str[ MAX_LINE_BUFSIZE ];

        status = UF_GDT_ask_face_index( faces[num], &face_index );
        ERROR_CHECK( status, ( "UF_GDT_ask_face_index", status, "face = %u",
                               faces[num] ) );

        sprintf( face_index_str, "%d", face_index );
        str = concatenate_strings( str, delimiter, face_index_str );
        delimiter = " ";
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the name of the geometric definition type specified
 *
 * Returns:
 *     Allocated geometric definition type name
 *---------------------------------------------------------------------------*/
static char *ask_geometric_definition_type(
    UF_GDT_geometric_definition_type_t type /* <I> Geometric definition type */
)
{
    char *type_str = NULL;

    if ( type == UF_GDT_ALL_GEOMETRY )
        type_str = "Geometry";
    else if ( type == UF_GDT_PLANAR_ORIENTATION )
        type_str = "Planar Orientation";
    else if ( type == UF_GDT_PLANAR_CROSS_SECTION )
        type_str = "Planar Cross-Section";
    else if ( type == UF_GDT_REGION )
        type_str = "Region";

    return ( copy_string( type_str ) );
}

/*---------------------------------------------------------------------------*
 * Ask the name of the tolerance type specified
 *
 * Returns:
 *     Allocated tolerance type name
 *---------------------------------------------------------------------------*/
static char *ask_tolerance_type(
    UFD_GDT__object_type_t type /* <I> Type of tolerance */
)
{
    char *type_str = NULL;

    if ( type == UFD_GDT__EMPTY_FEATURE_TYPE )
        type_str = "Empty";
    else if ( type == UFD_GDT__DATUM_IDENTIFIER_TYPE )
        type_str = "Datum";
    else if ( type == UFD_GDT__DATUM_TARGET_POINT_TYPE )
        type_str = "Datum Target Point";
    else if ( type == UFD_GDT__DATUM_TARGET_LINE_TYPE )
        type_str = "Datum Target Line";
    else if ( type == UFD_GDT__DATUM_TARGET_DIA_TYPE )
        type_str = "Diametral Datum Target Area";
    else if ( type == UFD_GDT__DATUM_TARGET_RECT_TYPE )
        type_str = "Rectangular Datum Target Area";
    else if ( type == UFD_GDT__DATUM_TARGET_CYL_TYPE )
        type_str = "Cylindrical Datum Target Area";
    else if ( type == UFD_GDT__DATUM_MULTIPLE_TYPE )
        type_str = "Multiple Datum";
    else if ( type == UFD_GDT__FEATURE_CONTROL_FRAME_TYPE )
        type_str = "Feature Control Frame";
    else if ( type == UFD_GDT__SIZE_TOLERANCE_TYPE )
        type_str = "Size Tolerance";
    else if( type == UFD_GDT__WALL_THICKNESS_TYPE )
        type_str = "Wall Thickness";
    else if( type == UFD_GDT__DEPTH_TOLERANCE_TYPE )
        type_str = "Depth Tolerance";
    else if( type == UFD_GDT__LIMITS_AND_FITS_TOLERANCE_TYPE )
        type_str = "Limits and Fits";
    else if( type == UFD_GDT__THREAD_TOLERANCE_TYPE )
        type_str = "Thread Tolerance";
    else if ( type == UFD_GDT__ANGULAR_DIRECTED_DIMENSION_TYPE )
        type_str = "Angular Directed Dimension";
    else if ( type == UFD_GDT__LINEAR_DIRECTED_DIMENSION_TYPE )
        type_str = "Linear Directed Dimension";

    return ( copy_string( type_str ) );
}

/*---------------------------------------------------------------------------*
 * Ask the name of the geometry type specified
 *
 * Returns:
 *     Allocated geometry type name
 *---------------------------------------------------------------------------*/
static char *ask_geometry_type(
    UF_GDT_feature_type_t type /* <I> Feature type */
)
{
    char *type_str = NULL;

    if ( type == UF_GDT_GENERAL_FEATURE )
        type_str = "General";
    else if ( type == UF_GDT_SLOT_FEATURE )
        type_str = "Slot";
    else if ( type == UF_GDT_TAB_FEATURE )
        type_str = "Tab";
    else if ( type == UF_GDT_HOLE_FEATURE )
        type_str = "Hole";
    else if ( type == UF_GDT_PIN_FEATURE )
        type_str = "Pin";
    else if ( type == UF_GDT_SOCKET_FEATURE )
        type_str = "Socket";
    else if ( type == UF_GDT_BALL_FEATURE )
        type_str = "Ball";
    else if ( type == UF_GDT_ELONGATED_HOLE_FEATURE )
        type_str = "Elongated Hole";
    else if ( type == UF_GDT_PLANE_FEATURE )
        type_str = "Plane";
    else if ( type == UF_GDT_BOUNDED_FEATURE )
        type_str = "Bounded";
    else if ( type == UF_GDT_TAPERED_HOLE_FEATURE )
        type_str = "Tapered Hole";
    else if ( type == UF_GDT_TAPERED_PIN_FEATURE )
        type_str = "Tapered Pin";
    else if ( type == UF_GDT_HOLLOW_TORUS_FEATURE )
        type_str = "Hollow Torus";
    else if ( type == UF_GDT_SOLID_TORUS_FEATURE )
        type_str = "Solid Torus";
    else if ( type == UF_GDT_HOLLOW_REVOLVED_FEATURE )
        type_str = "Hollow Revolved";
    else if ( type == UF_GDT_SOLID_REVOLVED_FEATURE )
        type_str = "Solid Revolved";
    else if ( type == UF_GDT_THICKNESS_GAP_FEATURE )
        type_str = "Thickness_Gap";
    else if( type == UF_GDT_THREAD_FEATURE )
        type_str = "Thread";

    return ( copy_string( type_str ) );
}

/*---------------------------------------------------------------------------*
 * Ask the name of the pattern type specified
 *
 * Returns:
 *     Allocated pattern type name
 *---------------------------------------------------------------------------*/
static char *ask_pattern_type(
    UF_GDT_pattern_type_t type /* <I> Pattern type */
)
{
    char *type_str = NULL;

    if ( type == UF_GDT_NO_PATTERN )
        type_str = "No Pattern";
    else
        type_str = "Pattern";

    return ( copy_string( type_str ) );
}

/*---------------------------------------------------------------------------*
 * Ask the views that contain a display instance of the specified tolerance
 * feature
 *
 * Returns:
 *     Allocated list of views containig a display instance of the tolerance
 *     feature
 *---------------------------------------------------------------------------*/
static char *ask_display_instance_views(
    UFD_GDT__object_type_t obj_type, /* <I> Type of object being queried    */
    tag_t                 feature    /* <I> Feature of object being queried */
)
{
    char *delimiter = NULL;
    char *str = NULL;
    int num, num_instances, status;
    tag_p_t instances;
    logical datum_search;

    datum_search = ( obj_type != UFD_GDT__FEATURE_CONTROL_FRAME_TYPE      &&
                     obj_type != UFD_GDT__SIZE_TOLERANCE_TYPE             &&
                     obj_type != UFD_GDT__WALL_THICKNESS_TYPE             &&
                     obj_type != UFD_GDT__DEPTH_TOLERANCE_TYPE            &&
                     obj_type != UFD_GDT__LIMITS_AND_FITS_TOLERANCE_TYPE  &&
                     obj_type != UFD_GDT__THREAD_TOLERANCE_TYPE           &&
                     obj_type != UFD_GDT__ANGULAR_DIRECTED_DIMENSION_TYPE &&
                     obj_type != UFD_GDT__LINEAR_DIRECTED_DIMENSION_TYPE );

    status = UF_GDT_ask_tol_feat_instance( feature, &num_instances, &instances );
    ERROR_CHECK( status, ( "UF_GDT_ask_tol_feat_instance", status,
                           "feature = %u", feature ) );

    for ( num = 0; num < num_instances; num++ )
    {
        int type, subtype;

        status = UF_OBJ_ask_type_and_subtype( instances[num], &type, &subtype );
        ERROR_CHECK( status, ( "UF_OBJ_ask_type_and_subtype", status,
                               "instance = %u", instances[num] ) );

        if ( !datum_search && subtype == UF_feature_instance_subtype ||
              datum_search && subtype != UF_feature_instance_subtype )
        {
            char view_name[ UF_OBJ_NAME_BUFSIZE ];
            int view_dep;

            status = uc6409( instances[num], &view_dep, view_name );
            ERROR_CHECK( status, ( "uc6409", status,
                                   "instance = %u", instances[num] ) );

            if ( view_dep == 0 )
                str = concatenate_strings( str, delimiter, "Model Views" );
            else
                str = concatenate_strings( str, delimiter, view_name );

            delimiter = ", ";
        }
    }

    UF_free( instances );

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the name of the part specified
 *
 * Returns:
 *     Allocated simple name of part specified
 *---------------------------------------------------------------------------*/
static char *ask_part_name(
    tag_t part               /* <I> Part to query */
)
{
    int part_type = 2;
    int status;
    char dir[ MAX_FSPEC_BUFSIZE ];
    char full_name[ MAX_FSPEC_BUFSIZE ];
    char name[ MAX_FSPEC_BUFSIZE ];

    UF_PART_ask_part_name( part, full_name );

    status = uc4576( full_name, part_type, dir, name );
    ERROR_CHECK( status, ( "uc4576", status, "part name = %u", full_name ) );

    return ( copy_string( name ) );
}

/*---------------------------------------------------------------------------*
 * Ask the name of the part that the input feature was pulled from
 *
 * Returns:
 *     Allocated name of part that feature was pulled from or NULL if the
 *     feature is not a pulled feature
 *---------------------------------------------------------------------------*/
static char *ask_pulled_tolerance_component(
    tag_t feature               /* <I> Feature to query */
)
{
    char *str = NULL;
    int status;
    logical is_pulled;

    status = UF_GDT_is_pulled_tolerance( feature, &is_pulled );
    ERROR_CHECK( status, ( "UF_GDT_is_pulled_tolerance", status,
                           "feature = %u", feature ) );

    if ( is_pulled )
    {
        tag_t component_part, component_part_occ;

        status = UF_GDT_ask_pulled_tolerance_component( feature,
                                                        &component_part_occ );
        ERROR_CHECK( status, ( "UF_GDT_ask_pulled_tolerance_component",
                               status, "feature = %u", feature ) );

        component_part = UF_ASSEM_ask_prototype_of_occ( component_part_occ );
        str = ask_part_name( component_part );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Get the list of the input features' names
 *
 * Returns:
 *     Allocated list of feature names
 *---------------------------------------------------------------------------*/
static char *ask_feature_names(
    char    *delimiter,         /* <I> Delimiter to separate names with */
    int      num_features,      /* <I> Number of features in list       */
    tag_p_t  features           /* <I> Features to return names of      */
)
{
    char *delimiter_str = NULL;
    char *str = NULL;
    int num;

    for ( num = 0; num < num_features; num++ )
    {
        int status;
        UF_GDT_description_p_t data;

        status = UF_GDT_ask_description( features[num], &data );
        ERROR_CHECK( status, ( "UF_GDT_ask_description", status,
                               "feature = %u", features[num] ) );

        str = concatenate_strings( str, delimiter_str, data->name );

        status = UF_GDT_free( UF_GDT_DESCRIPT_TYPE, data );
        ERROR_CHECK( status, ( "UF_GDT_free", status,
                               "data type = UF_GDT_DESCRIPT_TYPE(%d)",
                               UF_GDT_DESCRIPT_TYPE ) );
        UF_free( data );

        delimiter_str = delimiter;
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the tolerance features linked to the specified tolerance feature
 *
 * Returns:
 *     Allocated list of linked tolerance features
 *---------------------------------------------------------------------------*/
static char *ask_linked_features(
    tag_t feature               /* <I> Tolerance feature to query */
)
{
    char *str = NULL;
    int num_linked, status;
    tag_p_t linked;

    status = UF_GDT_ask_linked_features( feature, &num_linked, &linked );
    ERROR_CHECK( status, ( "UF_GDT_ask_linked_features", status,
                           "feature = %u", feature ) );

    str = ask_feature_names( ", ", num_linked, linked );

    UF_free( linked );

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of tags
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if tag1 < tag2
 *     UFD_GDT__EQUAL        if tag1 = tag2
 *     UFD_GDT__GREATER_THAN if tag1 > tag2
 *---------------------------------------------------------------------------*/
static int compare_tags(
    const void *ptr1,           /* <I> Tag 1 to compare */
    const void *ptr2            /* <I> Tag 2 to compare */
)
{
    tag_p_t tag1 = (tag_p_t) ptr1;
    tag_p_t tag2 = (tag_p_t) ptr2;

    if ( *tag1 < *tag2 )
        return ( UFD_GDT__LESS_THAN );
    else if ( *tag1 > *tag2 )
        return ( UFD_GDT__GREATER_THAN );
    else
        return ( UFD_GDT__EQUAL );
}

/*---------------------------------------------------------------------------*
 * Add the list of tags to the specified tag list which is sorted in
 * ascending order by tag value.  Only adds tags that do not already exist in
 * the tag list.
 *---------------------------------------------------------------------------*/
static void add_to_sorted_tag_list(
    int num_new_tags, /* <I>   Number of tags to add if not duplicated */
    tag_p_t new_tags, /* <I>   List of tags to add if not duplicated   */
    int *num_tags,    /* <I/O> Number of tags in list                  */
    tag_p_t *tags     /* <I/O> List of tags sorted in ascending order  */
)
{
    int alloc = *num_tags;
    int saved_num_tags = *num_tags;
    int pos;

    *tags = (tag_p_t)realloc_list( sizeof( tag_t ), num_new_tags,
                          &alloc, *num_tags, *tags );

    for ( pos = 0; pos < num_new_tags; pos++ )
    {
        if ( bsearch( &new_tags[pos], *tags, saved_num_tags,
                      sizeof( tag_t ), compare_tags ) == NULL )
        {
            (*tags)[(*num_tags)++] = new_tags[pos];
        }
    }

    qsort( *tags, *num_tags, sizeof( tag_t ), compare_tags );
}

/*---------------------------------------------------------------------------*
 * Get the list of fcfs that reference the datum specified and return the
 * list of faces contained by the fcfs' parent features.
 *
 * Returns:
 *     Allocated string representation of the list of faces whose fcfs
 *     reference the datum.
 *---------------------------------------------------------------------------*/
static char *ask_faces_referencing_datum(
    UFD_GDT__object_type_t type, /* <I> Type of object being queried */
    tag_t                 datum  /* <I> Datum being queried          */
)
{
    char *str = NULL;

    if ( type == UFD_GDT__DATUM_IDENTIFIER_TYPE )
    {
        int status, num, num_fcfs, num_faces = 0;
        tag_p_t fcfs, faces = NULL;

        status = UF_GDT_ask_datum_referencers( datum, &num_fcfs, &fcfs );
        ERROR_CHECK( status, ( "UF_GDT_ask_datum_referencers", status,
                               "datum = %u", datum ) );

        for ( num = 0; num < num_fcfs; num++ )
        {
            int num_fcf_faces;
            tag_p_t fcf_faces;
            tag_t feature;

            status = UF_GDT_ask_tol_feat_tag( fcfs[num], &feature );
            ERROR_CHECK( status, ( "UF_GDT_ask_tol_feat_tag", status,
                                   "fcf = %u", fcfs[num] ) );

            status = UF_GDT_ask_faces( feature, &num_fcf_faces, &fcf_faces );
            ERROR_CHECK( status, ( "UF_GDT_ask_faces", status,
                                   "feature = %u", feature ) );

            add_to_sorted_tag_list( num_fcf_faces, fcf_faces, &num_faces, &faces );
            UF_free( fcf_faces );
        }

        str = ask_face_list( num_faces, faces );

        UF_free( faces );
        UF_free( fcfs );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Get the next non-block character.
 *
 * NOTE: Block characters are defined as a sequence of two characters, the
 *       first of which is a '$'.
 *
 * Returns:
 *     Next non-block character
 *---------------------------------------------------------------------------*/
static char *next_char(
    char *str                   /* <I> String to query */
)
{
    char *next = NULL;

    if ( str != NULL )
    {
        next = str;
        if ( *str != '\0' )
        {
            next++;

            if ( *str == '$' )
            {
                if ( *next != '\0' )
                    next++;
            }
        }
    }

    return ( next );
}

/*---------------------------------------------------------------------------*
 * Trim the blanks off of the input string
 *
 * Returns:
 *     Allocated string copy with no leading or trailing blanks
 *---------------------------------------------------------------------------*/
static char *trim_blanks(
    char *text                  /* <I> Input string to trim */
)
{
    char *str = text;

    if ( text != NULL )
    {
        int pos;

        while ( isspace( *str ) )
            str++;

        str = copy_string( str );

        for ( pos = strlen( str ); pos >= 0; pos-- )
        {
            if ( !isspace( str[pos] ) )
                break;

            str[pos] = '\0';
        }
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * If the input text is a keyword control character then return the keyword
 * data.
 *
 * Returns:
 *     TRUE if the input text is a keyword control character; otherwise,
 *     FALSE.
 *---------------------------------------------------------------------------*/
static logical is_keyword(
    char *text,          /* <I> Input string to query                        */
    char **end_str,      /* <O> Ending '>' of keyword control character or   */
                         /*     input string if this is not a keyword        */
                         /*     control character                            */
    char **keyword_name, /* <O> Allocated keyword name or NULL if this is    */
                         /*     not a keyword control character              */
    char **keyword_arg   /* <O> Allocated keyword argument or NULL if none   */
                         /*     or if this is not a keyword control character*/
)
{
    logical found = FALSE;

    *end_str      = text;
    *keyword_name = NULL;
    *keyword_arg  = NULL;

    /* If this is a keyword control character then get the keyword name and
     * argument if any
     */
    if ( compare_strings( text, UFD_GDT__KEYWORD_CCHAR, UFD_GDT__KEYWORD_CCHAR_LEN ) == UFD_GDT__EQUAL )
    {
        char *ptr, *str;

        found = TRUE;

        str = &text[UFD_GDT__KEYWORD_CCHAR_LEN];
        while ( isspace( *str ) )
            str++;

        ptr = str;
        while ( !isspace( *ptr ) && *ptr != '>' && *ptr != '"' )
            ptr++;

        if ( str != ptr )
        {
            char saved_char = *ptr;
            char *arg_ptr;

            *ptr = '\0';
            arg_ptr = strchr( str, '(' );

            /* If no keyword arguments were found then just return the
             * keyword name */
            if ( arg_ptr == NULL )
                *keyword_name = trim_blanks( str );

            /* Keyword arguments were found so make sure to return the
             * both the keyword name and argument */
            else
            {
                int len;
                char saved_char2 = *arg_ptr;

                *arg_ptr = '\0';
                *keyword_name = trim_blanks( str );
                *arg_ptr = saved_char2;

                /* Don't to include the keyword argument's beginning '(' */
                *keyword_arg  = trim_blanks( &arg_ptr[1] );

                len = strlen( *keyword_arg );

                /* Don't to include the keyword argument's ending ')' */
                if ( (*keyword_arg)[len - 1] == ')' )
                    (*keyword_arg)[len - 1] = '\0';
            }

            *ptr = saved_char;
        }

        *end_str = ptr;

        /* Make sure to skip any user text for now so that we can return the
         * correct pointer to the end of the control character */
        if ( *ptr == '"' )
        {
            str = ptr;
            while ( isspace( *str ) )
                str++;

            for ( ptr = str; *ptr != '\0' && *ptr != '>'; ptr = next_char( ptr ) )
                *end_str = ptr;
        }
    }

    return ( found );
}

/*---------------------------------------------------------------------------*
 * Get the text representation of the keyword
 *
 * Returns:
 *     Allocated text representation of keyword
 *---------------------------------------------------------------------------*/
static char *format_keyword_text(
    tag_t part,         /* <I> Part to query for keyword names              */
    tag_t feature,      /* <I> Tolerance feature to query for keyword names */
    char *keyword_name, /* <I> Keyword name to query                        */
    char *keyword_arg   /* <I> Keyword argument or NULL if none             */
)
{
    char *prev, *text, *ptr;
    char *str = NULL;
    char arg[ MAX_LINE_BUFSIZE ] = "";
    int err = UF_GDT_ask_keyword_text( part, keyword_name, &text );

    if ( err != 0 )
        return ( NULL );

    /* Get the string representation of the keyword argument */
    if ( keyword_arg != NULL )
    {
        int status;
        int num_faces = 0;
        tag_p_t faces = NULL;

        status = UF_GDT_ask_faces( feature, &num_faces, &faces );
        ERROR_CHECK( status, ( "UF_GDT_ask_faces", status,
                               "feature = %u", feature ) );
        UF_free( faces );

        /* Display number of faces in feature for keywords requiring
         * extra data */
        sprintf( arg, "%d", num_faces );
    }

    /* Replace all argument control characters with the string representation
     * of the keyword argument
     */
    for ( prev = text, ptr = text; *ptr != '\0'; ptr = next_char( ptr ) )
    {
        if ( strncmp( ptr, UFD_GDT__ARG_CCHAR, UFD_GDT__ARG_CCHAR_LEN ) == 0 )
        {
            char saved_char = *ptr;

            *ptr = '\0';
            str  = concatenate_strings( str, arg, prev );
            *ptr = saved_char;
            prev = &ptr[UFD_GDT__ARG_CCHAR_LEN];
            ptr  = &ptr[UFD_GDT__ARG_CCHAR_LEN - 1];
        }
    }

    if ( str == text )
        str = text;
    else
    {
        str = concatenate_strings( str, prev, NULL );
        UF_free( text );
    }

    return ( str );
}


/*---------------------------------------------------------------------------*
 * Convert the keyword control characters to their text representations.
 *
 * Returns:
 *     Reallocated appended text
 *---------------------------------------------------------------------------*/
static char *convert_appended_text(
    char  *text,   /* <I> Appended text to convert                           */
                   /*     NOTE: This pointer may be invalid after the
                    *           concatenation is performed since this string
                    *           will be reallocated                          */
    tag_t  feature /* <I> Tolerance feature to query for keyword names       */
)
{
    char *ptr;
    char *prev = text;
    char *str = NULL;
    int level = 0;
    tag_t part;

    UF_OBJ_ask_owning_part( feature, &part );

    /* Convert each keyword control character to its text representation */
    for ( ptr = text; ptr != NULL && *ptr != '\0'; ptr = next_char( ptr ) )
    {
        /* Found the end of a control character */
        if ( *ptr == '>' )
            level--;

        /* Found the beginning of a control character */
        else if ( *ptr == '<' )
        {
            char *end_ptr, *name, *arg;

            if ( level == 0 && is_keyword( ptr, &end_ptr, &name, &arg ) )
            {
                char *keyword_str = format_keyword_text( part, feature, name, arg );

                *ptr = '\0';
                str = concatenate_strings( str, prev, keyword_str );
                ptr = end_ptr;
                prev = end_ptr + 1;

                UF_free( name );
                UF_free( arg );
                UF_free( keyword_str );
            }
            else
                level++;
        }
    }

    if ( str == NULL )
        str = text;
    else
    {
        str = concatenate_strings( str, prev, NULL );
        UF_free( text );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the standard or user defined keyword names listed in the
 * UF_GDT_modifier_data_s structure.
 *
 * Returns:
 *     Allocated list of keyword names
 *---------------------------------------------------------------------------*/
static char *ask_keywords_from_modifier_data(
    logical standard,           /* <I> TRUE to return standard keywords      */
                                /*     FALSE to return user defined keywords */
    tag_t   part,               /* <I> Part to query for keyword names       */
    UF_GDT_modifier_data_p_t modifier_data
                                /* <I> Modifier data containing list of      */
                                /*     keywords to query                     */
)
{
   char *str = NULL;

    if ( modifier_data != NULL )
    {
        char *delimiter = NULL;
        int num;
        int num_keywords = modifier_data->num_keywords;
        UF_GDT_keyword_p_t keywords = modifier_data->keywords;

        for ( num = 0; num < num_keywords; num++ )
        {
            int status;
            int id = keywords[num].id;
            logical is_user_defined;

            status = UF_GDT_is_user_defined_keyword( part, id,
                                                     &is_user_defined );
            ERROR_CHECK( status, ( "UF_GDT_is_user_defined_keyword", status,
                                   "part = %u, keyword id = %d",
                                   part, id ) );

            if ( (  standard && !is_user_defined ) ||
                 ( !standard &&  is_user_defined ) )
            {
                char *keyword_name = NULL;

                status = UF_GDT_ask_keyword_name( part, id,
                                                  &keyword_name );
                ERROR_CHECK( status, ( "UF_GDT_ask_keyword_name", status,
                                       "part = %u, keyword id = %d",
                                       part, id ) );
                str = concatenate_strings( str, delimiter, keyword_name );
                delimiter = ", ";
            }
        }
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the standard or user defined keyword names listed in the
 * UF_GDT_modifier_data_s structure.
 *
 * Returns:
 *     Allocated list of keyword names
 *---------------------------------------------------------------------------*/
static char *ask_keywords(
    logical standard,           /* <I> TRUE to return standard keywords      */
                                /*     FALSE to return user defined keywords */
    tag_t   part,               /* <I> Part to query for keyword names       */
    UF_GDT_modifier_data_p_t feature_modifier_data,
                                /* <I> Modifier data containing list of      */
                                /*     keywords to query                     */
    UF_GDT_modifier_data_p_t tolerance_modifier_data
                                /* <I> Modifier data containing list of      */
                                /*     keywords to query                     */
)
{
    char *str = NULL;
    char *tolerance_str = NULL;

    if ( feature_modifier_data != NULL )
        str = ask_keywords_from_modifier_data( standard, part,
                                               feature_modifier_data );

    if ( tolerance_modifier_data != NULL )
        tolerance_str = ask_keywords_from_modifier_data( standard, part,
                                                         tolerance_modifier_data );

    if ( str == NULL )
        str = tolerance_str;
    else
    {
        str = concatenate_strings( str, tolerance_str, NULL );
        UF_free( tolerance_str );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the label of the datum specified.  If we want the entire callout then
 * also return the datum's individually status if it's a datum identifier.
 *
 * Returns:
 *     Allocated datum label
 *---------------------------------------------------------------------------*/
static char *ask_datum_label(
    logical                   all_callout, /* <I> TRUE to include all callout*/
    UFD_GDT__object_type_t    datum_type,  /* <I> Type of datum being queried*/
    UFD_GDT__feature_data_p_t feature_data /* <I> Tolerance feature data     */
)
{
    char *label = NULL;
    int status;

    status = UF_GDT_ask_label_of_datum( feature_data->feature, &label );
    ERROR_CHECK( status, ( "UF_GDT_ask_label_of_datum", status,
                           "datum = %u", feature_data->feature ) );

    if ( all_callout && datum_type == UFD_GDT__DATUM_IDENTIFIER_TYPE )
    {
        UF_GDT_datum_identifier_p_t datum_data;

        status = UF_GDT_ask_datum_ident_parms( feature_data->feature,
                                               &datum_data );
        ERROR_CHECK( status, ( "UF_GDT_ask_datum_ident_parms", status,
                               "datum = %u", feature_data->feature ) );

        if ( datum_data->is_individual )
        {
            char *individually_str = "INDIVIDUALLY";

            /* <NEEDED> actual INDIVIDUALLY keyword string for datum */
            label = concatenate_strings( label, " ", individually_str );
        }

        status = UF_GDT_free( UF_GDT_DATUM_IDENT_TYPE, datum_data );
        ERROR_CHECK( status, ( "UF_GDT_free", status,
                               "data type = UF_GDT_DATUM_IDENT_TYPE(%d)",
                               UF_GDT_DATUM_IDENT_TYPE ) );
        UF_free( datum_data );
    }

    return ( label );
}

/*---------------------------------------------------------------------------*
 * Ask the tolerance features that are superfeatures of the specified
 * tolerance feature
 *
 * Returns:
 *     Allocated list of tolerance feature's superfeatures
 *---------------------------------------------------------------------------*/
static char *ask_parent_features(
    tag_t feature               /* <I> Tolerance feature to query */
)
{
    char *str = NULL;
    int alloc = 0;
    int count = 0;
    tag_p_t list = NULL;
    tag_t curr_feat, super_feat;

    for ( curr_feat = feature; curr_feat != NULL_TAG; curr_feat = super_feat )
    {
        int status;

        status = UF_GDT_ask_super_feature( curr_feat, &super_feat );
        ERROR_CHECK( status, ( "UF_GDT_ask_super_feature", status,
                               "feature = %u", curr_feat ) );

        if ( super_feat != NULL_TAG )
        {
            list = (tag_p_t) realloc_list( sizeof( tag_t ), 5, &alloc, count, list );
            list[count++] = super_feat;
        }
    }

    str = ask_feature_names( ", ", count, list );

    UF_free( list );

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the tolerance features that are subfeatures of the specified
 * tolerance feature
 *
 * Returns:
 *     Allocated list of tolerance feature's subfeatures
 *---------------------------------------------------------------------------*/
static char *ask_child_features(
    tag_t feature               /* <I> Tolerance feature to query */
)
{
    char *str = NULL;
    int count, status;
    tag_p_t list;

    status = UF_GDT_ask_sub_features( feature, &count, &list );
    ERROR_CHECK( status, ( "UF_GDT_ask_sub_features", status,
                           "feature = %u", feature ) );

    str = ask_feature_names( ", ", count, list );

    UF_free( list );

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask information specific to the tolerance feature
 *
 * Returns:
 *     Allocated tolerance feature information string
 *---------------------------------------------------------------------------*/
static char *ask_feature_info_data(
    UFD_GDT__info_type_t      info_type,      /* <I>   Type of data to return*/
    logical                   show_datum_data,/* <I>   TRUE = show datum data*/
    UFD_GDT__feature_data_p_t feature_data,   /* <I>   Tolerance feature data*/
    UFD_GDT__object_info_p_t  object_info     /* <I/O> Object data           */
)
{
    char *str = NULL;
    int status;
    logical is_retained;

    /* Tolerance feature data */
    switch ( info_type )
    {
        case UFD_GDT__PART_NAME_INFO:
            str = ask_part_name( feature_data->part );
            break;

        case UFD_GDT__TOLERANCE_FEATURE_NAME_INFO:
            str = copy_string( feature_data->feature_parms->descript->name );
            break;

        case UFD_GDT__RETAINED_STATUS_INFO:
            status = UF_GDT_is_retained( feature_data->feature, &is_retained );
            ERROR_CHECK( status, ( "UF_GDT_is_retained", status,
                                   "feature = %u", feature_data->feature ) );

            if ( is_retained )
                str = copy_string( "Retained" );
            else
                str = copy_string( "Not Retained" );
            break;

        case UFD_GDT__DESCRIPTION_INFO:
            str = copy_string( feature_data->feature_parms->descript->description );
            break;

        case UFD_GDT__FACES_INFO:
            str = ask_face_list( feature_data->feature_parms->num_faces,
                                 feature_data->feature_parms->face_list );
            break;

        case UFD_GDT__GEOMETRIC_DEFINITION_TYPE_INFO:
            str = ask_geometric_definition_type( feature_data->geom_def->type );
            break;

        case UFD_GDT__TOLERANCE_TYPE_INFO:
            str = ask_tolerance_type( object_info->tolerance_type );
            break;

        case UFD_GDT__GEOMETRY_TYPE_INFO:
            str = ask_geometry_type( feature_data->feature_parms->feature );
            break;

        case UFD_GDT__PATTERN_TYPE_INFO:
            str = ask_pattern_type( feature_data->feature_parms->pattern );
            break;

        case UFD_GDT__DISPLAY_INSTANCE_VIEWS_INFO:
            str = ask_display_instance_views( object_info->tolerance_type,
                                              feature_data->feature );
            break;

        case UFD_GDT__PULLED_FROM_INFO:
            str = ask_pulled_tolerance_component( feature_data->feature );
            break;

        case UFD_GDT__PARENT_TOLERANCE_FEATURE_INFO:
            str = ask_parent_features( feature_data->feature );
            break;

        case UFD_GDT__CHILD_TOLERANCE_FEATURES_INFO:
            str = ask_child_features( feature_data->feature );
            break;

        case UFD_GDT__LINKED_TOLERANCE_FEATURES_INFO:
            str = ask_linked_features( feature_data->feature );
            break;

        case UFD_GDT__RELATED_FACES_INFO:
            if ( show_datum_data )
                str = ask_faces_referencing_datum( object_info->tolerance_type,
                                                   feature_data->feature );
            break;

        case UFD_GDT__STANDARD_KEYWORDS_INFO:
            str = ask_keywords( TRUE, feature_data->part,
                                feature_data->feature_parms->modifier_data, NULL );
            break;

        case UFD_GDT__USER_DEFINED_KEYWORDS_INFO:
            str = ask_keywords( FALSE, feature_data->part,
                                feature_data->feature_parms->modifier_data, NULL );
            break;

        case UFD_GDT__ENTIRE_CALLOUT_STRING_INFO:
            if ( show_datum_data )
                str = ask_datum_label( TRUE, object_info->tolerance_type,
                                       feature_data );
            break;

        case UFD_GDT__CALLOUT_STRING_INFO:
            if ( show_datum_data )
                str = ask_datum_label( FALSE, object_info->tolerance_type,
                                       feature_data );
            break;

        default:
            break;
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask information from the tolerance feature
 *---------------------------------------------------------------------------*/
static void ask_feature_info(
    logical                   show_datum_data,/* <I>   TRUE = show datum data*/
    UFD_GDT__feature_data_p_t feature_data,   /* <I>   Tolerance feature data*/
    UFD_GDT__object_info_p_t  object_info     /* <I/O> Object data to report */
)
{
    int num;

    for ( num = 0; num < object_info->count; num++ )
    {
        object_info->list[num].data =
            ask_feature_info_data( object_info->list[num].type, show_datum_data,
                                   feature_data, object_info );
    }
}

/*---------------------------------------------------------------------------*
 * Add information on the empty tolerance feature specified to the part
 * report data
 *---------------------------------------------------------------------------*/
static void add_empty_feature_info(
    UFD_GDT__report_p_t       report,      /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data /* <I>   Tolerance feature data */
)
{
    UFD_GDT__object_info_t object_info;

    init_info_data( report, feature_data->part, feature_data->feature,
                    NULL_TAG, UFD_GDT__EMPTY_FEATURE_TYPE,
                    &object_info );

    ask_feature_info( FALSE, feature_data, &object_info );

    add_to_part_info_list( report, &object_info );
}

/*---------------------------------------------------------------------------*
 * Add information on the datum or datum target specified to the part report
 * data
 *---------------------------------------------------------------------------*/
static void add_datum_info(
    UFD_GDT__report_p_t       report,       /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data, /* <I>   Tolerance feature data */
    UF_GDT_tolerance_type_t   tol_type      /* <I>   UF_GDT datum type      */
)
{
    UFD_GDT__object_info_t object_info;
    UFD_GDT__object_type_t type = UFD_GDT__EMPTY_FEATURE_TYPE;

    if ( tol_type == UF_GDT_DATUM_IDENTIFIER_TYPE )
        type = UFD_GDT__DATUM_IDENTIFIER_TYPE;

    else if ( tol_type == UF_GDT_DATUM_MULTIPLE_TYPE )
        type = UFD_GDT__DATUM_MULTIPLE_TYPE;

    else if ( tol_type == UF_GDT_DATUM_TARGET_POINT_TYPE )
        type = UFD_GDT__DATUM_TARGET_POINT_TYPE;

    else if ( tol_type == UF_GDT_DATUM_TARGET_LINE_TYPE )
        type = UFD_GDT__DATUM_TARGET_LINE_TYPE;

    else if ( tol_type == UF_GDT_DATUM_TARGET_DIA_TYPE )
        type = UFD_GDT__DATUM_TARGET_DIA_TYPE;

    else if ( tol_type == UF_GDT_DATUM_TARGET_RECT_TYPE )
        type = UFD_GDT__DATUM_TARGET_RECT_TYPE;

    else if ( tol_type == UF_GDT_DATUM_TARGET_CYL_TYPE )
        type = UFD_GDT__DATUM_TARGET_CYL_TYPE;

    init_info_data( report, feature_data->part, feature_data->feature,
                    NULL_TAG, type, &object_info );

    ask_feature_info( TRUE, feature_data, &object_info );

    add_to_part_info_list( report, &object_info );
}

/*---------------------------------------------------------------------------*
 * Ask the appended text from the input tolerance at the specified appended
 * text location
 *
 * Returns:
 *     Allocated appended text string
 *---------------------------------------------------------------------------*/
static char *ask_appended_text(
    tag_t                feature, /* <I> Tolerance feature containing the
                                   *     object to query                     */
    tag_t                object,  /* <I> Object to query                     */
    UFD_GDT__info_type_t type     /* <O> Appended text info type             */
)
{
    char *str = NULL;
    int num, status;
    int num_lines = 0;
    char **lines = NULL;

    switch ( type )
    {
        case UFD_GDT__ABOVE_APPENDED_TEXT_INFO:
            status = UF_GDT_ask_appended_text( object, UF_GDT_ABOVE,
                                               &num_lines, &lines );
            ERROR_CHECK( status, ( "UF_GDT_ask_appended_text", status,
                                   "object = %u, UF_GDT_ABOVE", object ) );
            break;

        case UFD_GDT__BELOW_APPENDED_TEXT_INFO:
            status = UF_GDT_ask_appended_text( object, UF_GDT_BELOW,
                                               &num_lines, &lines );
            ERROR_CHECK( status, ( "UF_GDT_ask_appended_text", status,
                                   "object = %u, UF_GDT_BELOW", object ) );
            break;

        case UFD_GDT__BEFORE_APPENDED_TEXT_INFO:
            status = UF_GDT_ask_appended_text( object, UF_GDT_BEFORE,
                                               &num_lines, &lines );
            ERROR_CHECK( status, ( "UF_GDT_ask_appended_text", status,
                                   "object = %u, UF_GDT_BEFORE", object ) );
            break;

        case UFD_GDT__AFTER_APPENDED_TEXT_INFO:
            status = UF_GDT_ask_appended_text( object, UF_GDT_AFTER,
                                               &num_lines, &lines );
            ERROR_CHECK( status, ( "UF_GDT_ask_appended_text", status,
                                   "object = %u, UF_GDT_AFTER", object ) );
            break;

        default:
            break;
    }

    if ( num_lines > 0 )
    {
        lines[0] = convert_appended_text( lines[0], feature );
        str = copy_string( lines[0] );

        for ( num = 1; num < num_lines; num++ )
        {
            lines[num] = convert_appended_text( lines[num], feature );
            str = concatenate_strings( str, " ", lines[num] );
        }

        UF_free_string_array( num_lines, lines );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the specified characteristic's name
 *
 * Returns:
 *     Allocated characteristic name string
 *---------------------------------------------------------------------------*/
static char *ask_characteristic(
  UF_GDT_fcf_p_t fcf_data       /* <I> Feature control frame data */
)
{
    char *str = NULL;

    if      ( fcf_data->characteristic == UF_GDT_STRAIGHTNESS_TYPE )
        str = "Straightness";
    else if ( fcf_data->characteristic == UF_GDT_FLATNESS_TYPE )
        str = "Flatness";
    else if ( fcf_data->characteristic == UF_GDT_CIRCULAR_TYPE )
        str = "Circularity";
    else if ( fcf_data->characteristic == UF_GDT_CYLINDRICAL_TYPE )
        str = "Cylindricity";
    else if ( fcf_data->characteristic == UF_GDT_ANGULAR_TYPE )
        str = "Angularity";
    else if ( fcf_data->characteristic == UF_GDT_PERPENDICULAR_TYPE )
        str = "Perpendicularity";
    else if ( fcf_data->characteristic == UF_GDT_PARALLEL_TYPE )
        str = "Parallelism";
    else if ( fcf_data->characteristic == UF_GDT_LINE_PROFILE_TYPE )
        str = "Line Profile";
    else if ( fcf_data->characteristic == UF_GDT_CONCENTRIC_TYPE )
        str = "Concentricity";
    else if ( fcf_data->characteristic == UF_GDT_SYMMETRIC_TYPE )
        str = "Symmetry";
    else if ( fcf_data->characteristic == UF_GDT_CIRCULAR_RUNOUT_TYPE )
        str = "Circular Runout";
    else if ( fcf_data->characteristic == UF_GDT_TOTAL_RUNOUT_TYPE )
        str = "Total Runout";
    else if ( fcf_data->characteristic == UF_GDT_SURFACE_PROFILE_TYPE )
    {
        if ( fcf_data->num_frames == 1 )
            str = "Surface Profile";
        else
            str = "Composite Surface Profile";
    }
    else if ( fcf_data->characteristic == UF_GDT_POSITION_TYPE )
    {
        if ( fcf_data->num_frames == 1 )
            str = "Position";
        else
            str = "Composite Position";
    }

    return ( copy_string( str ) );
}

/*---------------------------------------------------------------------------*
 * Convert from UFD_GDT__object_type_t to UF_GDT_tolerance_type_t
 *
 * Returns:
 *     The UF_GDT_tolerance_type_t tolerance type
 *---------------------------------------------------------------------------*/
static UF_GDT_tolerance_type_t ask_uf_gdt_tol_type(
    UFD_GDT__object_type_t tol_type /* <I> Tolerance type */
)
{
    UF_GDT_tolerance_type_t type;

    if ( tol_type == UFD_GDT__DATUM_IDENTIFIER_TYPE )
        type = UF_GDT_DATUM_IDENTIFIER_TYPE;
    else if ( tol_type == UFD_GDT__DATUM_TARGET_POINT_TYPE )
        type = UF_GDT_DATUM_TARGET_POINT_TYPE;
    else if ( tol_type == UFD_GDT__DATUM_TARGET_LINE_TYPE )
        type = UF_GDT_DATUM_TARGET_LINE_TYPE;
    else if ( tol_type == UFD_GDT__DATUM_TARGET_DIA_TYPE )
        type = UF_GDT_DATUM_TARGET_DIA_TYPE;
    else if ( tol_type == UFD_GDT__DATUM_TARGET_RECT_TYPE )
        type = UF_GDT_DATUM_TARGET_RECT_TYPE;
    else if ( tol_type == UFD_GDT__DATUM_TARGET_CYL_TYPE )
        type = UF_GDT_DATUM_TARGET_CYL_TYPE;
    else if ( tol_type == UFD_GDT__DATUM_MULTIPLE_TYPE )
        type = UF_GDT_DATUM_MULTIPLE_TYPE;
    else if ( tol_type == UFD_GDT__FEATURE_CONTROL_FRAME_TYPE )
        type = UF_GDT_GEOMETRIC_TOLERANCE_TYPE;
    else if ( tol_type == UFD_GDT__SIZE_TOLERANCE_TYPE )
        type = UF_GDT_SIZE_TOLERANCE_TYPE;
    else if ( tol_type == UFD_GDT__WALL_THICKNESS_TYPE )
        type = UF_GDT_WALL_THICKNESS_TYPE;
    else if( tol_type == UFD_GDT__DEPTH_TOLERANCE_TYPE )
        type = UF_GDT_DEPTH_TOLERANCE_TYPE;
    else if( tol_type == UFD_GDT__LIMITS_AND_FITS_TOLERANCE_TYPE )
        type = UF_GDT_LIMITS_AND_FITS_TOLERANCE_TYPE;
    else if( tol_type == UFD_GDT__THREAD_TOLERANCE_TYPE )
        type = UF_GDT_THREAD_TOLERANCE_TYPE;
    else
    {
#ifdef NEEDED
        ASSERT_INTERNAL( tol_type == UFD_GDT__ANGULAR_DIRECTED_DIMENSION_TYPE ||
                         tol_type == UFD_GDT__LINEAR_DIRECTED_DIMENSION_TYPE );
#endif
        type = UF_GDT_DIRECTED_DIMENSION_TYPE;
    }

    return ( type );
}

/*---------------------------------------------------------------------------*
 * Convert from UF_GDT_tolerance_type_t to UFD_GDT__object_type_t
 *
 * Returns:
 *     The UFD_GDT__object_type_t tolerance type
 *---------------------------------------------------------------------------*/
static UFD_GDT__object_type_t ask_ufd_gdt_tol_type(
    UF_GDT_tolerance_type_t type /* <I> Tolerance type */
)
{
    UFD_GDT__object_type_t tol_type = UFD_GDT__EMPTY_FEATURE_TYPE;

    if( type == UF_GDT_DATUM_IDENTIFIER_TYPE )
        tol_type = UFD_GDT__DATUM_IDENTIFIER_TYPE;
    else if( type == UF_GDT_DATUM_TARGET_POINT_TYPE )
        tol_type = UFD_GDT__DATUM_TARGET_POINT_TYPE;
    else if( type == UF_GDT_DATUM_TARGET_LINE_TYPE )
        tol_type = UFD_GDT__DATUM_TARGET_LINE_TYPE;
    else if( type == UF_GDT_DATUM_TARGET_DIA_TYPE )
        tol_type = UFD_GDT__DATUM_TARGET_DIA_TYPE;
    else if( type == UF_GDT_DATUM_TARGET_RECT_TYPE )
        tol_type = UFD_GDT__DATUM_TARGET_RECT_TYPE;
    else if( type == UF_GDT_DATUM_TARGET_CYL_TYPE )
        tol_type = UFD_GDT__DATUM_TARGET_CYL_TYPE;
    else if( type == UF_GDT_DATUM_MULTIPLE_TYPE )
        tol_type = UFD_GDT__DATUM_MULTIPLE_TYPE;
    else if( type == UF_GDT_GEOMETRIC_TOLERANCE_TYPE )
        tol_type = UFD_GDT__FEATURE_CONTROL_FRAME_TYPE;
    else if( type == UF_GDT_SIZE_TOLERANCE_TYPE )
        tol_type = UFD_GDT__SIZE_TOLERANCE_TYPE;
    else if( type == UF_GDT_WALL_THICKNESS_TYPE )
        tol_type = UFD_GDT__WALL_THICKNESS_TYPE;
    else if( type == UF_GDT_DEPTH_TOLERANCE_TYPE )
        tol_type = UFD_GDT__DEPTH_TOLERANCE_TYPE;
    else if( type == UF_GDT_LIMITS_AND_FITS_TOLERANCE_TYPE )
        tol_type = UFD_GDT__LIMITS_AND_FITS_TOLERANCE_TYPE;
    else if( type == UF_GDT_THREAD_TOLERANCE_TYPE )
        tol_type = UFD_GDT__THREAD_TOLERANCE_TYPE;
    else if( type == UF_GDT_DIRECTED_DIMENSION_TYPE )
    {
#ifdef NEEDED
        tol_type = UFD_GDT__LINEAR_DIRECTED_DIMENSION_TYPE;
#endif
    }

    return ( tol_type );
}


/*---------------------------------------------------------------------------*
 * Ask the callout string that corresponds to the input tolerance along with
 * all appended text if so specified.
 *
 * Returns:
 *     Allocated callout string
 *---------------------------------------------------------------------------*/
static int ask_callout_string_index(
    UFD_GDT__feature_data_p_t feature_data,  /* <I> Tolerance feature data  */
    UFD_GDT__object_type_t    tol_type,      /* <I> Tolerance type          */
    tag_t                     tolerance,     /* <I> Tolerance tag           */
    int                       callout_num    /* <I> FCF frame number        */
)
{
    int num;
    int callout_index = -1;
    UF_GDT_tolerance_type_t type = ask_uf_gdt_tol_type( tol_type );

    for ( num = 0; num < feature_data->num_callout_strings; num++ )
    {
        if ( feature_data->callout_strings[num].type == type &&
             feature_data->callout_strings[num].tolerance == tolerance )
        {
            int pos = num + callout_num;

            if ( pos < feature_data->num_callout_strings &&
                 feature_data->callout_strings[pos].tolerance == tolerance )
            {
                callout_index = pos;
            }
            break;
        }
    }

    return ( callout_index );
}

/*---------------------------------------------------------------------------*
 * Add all appended text to the callout string that corresponds to the input
 * tolerance.
 *
 * Returns:
 *     Allocated callout string
 *---------------------------------------------------------------------------*/
static char *add_appended_text(
    tag_t  feature,     /* <I> Tolerance feature containing tolerance      */
    char  *callout_str, /* <I> Callout string                              */
                        /*     NOTE: This pointer may be invalid after the */
                        /*           concatenation is performed since this */
                        /*           string will be reallocated            */
    tag_t  tolerance    /* <I> Tolerance tag                               */
)
{
    char *str = callout_str;

    if ( str != NULL )
    {
        int num;
        char *strs[5];

        strs[0] = ask_appended_text( feature, tolerance, UFD_GDT__ABOVE_APPENDED_TEXT_INFO );
        strs[1] = ask_appended_text( feature, tolerance, UFD_GDT__BEFORE_APPENDED_TEXT_INFO );
        strs[2] = str;
        strs[3] = ask_appended_text( feature, tolerance, UFD_GDT__AFTER_APPENDED_TEXT_INFO );
        strs[4] = ask_appended_text( feature, tolerance, UFD_GDT__BELOW_APPENDED_TEXT_INFO );

        str = NULL;

        for ( num = 0; num < 5; num++ )
        {
            if ( str == NULL )
                str = strs[num];

            else if ( strs[num] != NULL )
            {
                str = concatenate_strings( str, ", ", strs[num] );
                UF_free( strs[num] );
            }
        }
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the callout string that corresponds to the input tolerance along with
 * all appended text if so specified.
 *
 * Returns:
 *     Allocated callout string
 *---------------------------------------------------------------------------*/
static char *ask_fcf_callout(
    logical                   show_all,      /* <I> TRUE to show with       */
                                             /*     appended text           */
    UFD_GDT__feature_data_p_t feature_data,  /* <I> Tolerance feature data  */
    tag_t                     tolerance,     /* <I> Tolerance tag           */
    int                       callout_num    /* <I> FCF frame number        */
)
{
    char *str = NULL;
    int num = ask_callout_string_index( feature_data,
                                        UFD_GDT__FEATURE_CONTROL_FRAME_TYPE,
                                        tolerance, callout_num );

    if ( num < 0 )
        return ( NULL );

    str = copy_string( feature_data->callout_strings[num].string );

    if ( show_all )
    {
        int pos;

        for ( pos = num + 1; pos < feature_data->num_callout_strings; pos++ )
        {
            if ( feature_data->callout_strings[pos].tolerance != tolerance )
                break;

            str = concatenate_strings( str, NULL,
                                       feature_data->callout_strings[pos].string );
        }

        str = add_appended_text( feature_data->feature, str, tolerance );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the string that corresponds to the size tolerance type of the input
 * size data.
 *
 * Returns:
 *     Allocated size tolerance type string
 *---------------------------------------------------------------------------*/
static char *ask_size_tolerance_type(
    UFD_GDT__object_type_t    type,     /* <I> Type of tolerance   */
    UF_GDT_size_tolerance_p_t size_data /* <I> Size tolerance data */
)
{
    char *str = NULL;

    if ( type != UFD_GDT__SIZE_TOLERANCE_TYPE )
        str = ask_tolerance_type( type );

    else if ( size_data->value_type == UF_GDT_LINEAR_SIZE )
        str = copy_string( "Length" );

    else if ( size_data->value_type == UF_GDT_RADIAL_SIZE )
        str = copy_string( "Radius" );

    else if ( size_data->value_type == UF_GDT_DIAMETRAL_SIZE )
        str = copy_string( "Diameter" );

    else
        str = copy_string( "No Size" );

    return ( str );
}

/*---------------------------------------------------------------------------------------
    Strings are of the form "nominal<$s>"
    
    Returns the displayed nominal value devoid of all extra characters.
  ---------------------------------------------------------------------------------------*/
static void ask_displayed_nominal(
    char    *text,              /* <I> Displayed main text string              */
    double  *displayed_nominal  /* <I/0> Displayed nominal value               */
)
{
    int j, len, k;
    char size_0[132];
    char *p = text;

    /* Extract the first size from the string */
    len = strlen( p );
    for ( j = 0, k = 0; j < len; j++, p++ )
    {
        if ( *p == '.' || ( *p >= '0' && *p <= '9' ) )
             size_0[k++] = *p;
    }
    size_0[k] = '\0';
    p++;

    sscanf( size_0, "%lf", displayed_nominal );
}


/*---------------------------------------------------------------------------------------
    Strings are of the form <Tlow!high>
                            <Thigh!low>
                            high - low
                            low - high
  ---------------------------------------------------------------------------------------*/
static void ask_displayed_limits(
    char *text,           /* <I> Displayed main text string                 */
    int prefix_len,       /* <I> Length of prefix string, e.g. 2 for "<T"   */
    char delimiter,       /* <I> Break between sizes, e.g. '!' or '-'       */
    logical upper_first,  /* <I> TRUE if high limit is first                */
    double *lower_limit,  /* <O> Displayed lower limit                      */
    double *upper_limit   /* <O> Displayed upper limit                      */
)
{
    int j, len, k;
    char size_0[132], size_1[132];
    char *p = text + prefix_len;

    /* Extract the first size from the string */
    len = strlen(p);
    for ( j = 0, k = 0; j < len; j++, p++ )
    {
        if ( *p == delimiter )
            break;

        else if ( *p == '.' || ( *p >= '0' && *p <= '9' ) )
            size_0[k++] = *p;
    }
    size_0[k] = '\0';
    p++;

    /* Extract the second size from the string */
    len = strlen(p);
    for ( j = 0, k = 0; j < len; j++, p++ )
    {
        if (*p == '>')
            break;

        else if ( *p == '.' || ( *p >= '0' && *p <= '9' ) )
            size_1[k++] = *p;
    }
    size_1[k] = '\0';

    if ( upper_first )
    {
        sscanf( size_0, "%lf", upper_limit );
        sscanf( size_1, "%lf", lower_limit );
    }
    else
    {
        sscanf( size_1, "%lf", upper_limit );
        sscanf( size_0, "%lf", lower_limit );
    }
}

/*---------------------------------------------------------------------------------------
    Determine if displayed instance shows a nominal value or limits.

    Returns the displayed nominal value if exists, leaving the limits set to 0.0.
    Returns the limits if they exits, leaving the displayed_nominal set to 0.0.
  ---------------------------------------------------------------------------------------*/
static logical ask_displayed_angular_values(
    tag_t  feature,             /* <I> feature to query */
    double *displayed_nominal,  /* <O> displayed nominal (can be 0.0 if limits are displayed     */
    double *lower_limit,        /* <O> displayed lower limit (can be 0.0 if nominal is displayed */
    double *upper_limit,        /* <O> displayed upper limit (can be 0.0 if nominal is displayed */
    logical has_limits         /* <O> TRUE if displayed instance has limits                     */
)
{
    int error_code = 0, subtype, j, k, etype;
    int num_instances = 0, num_curves = 0, num_anns = 0;
    int mpi[100];
    double mpr[100], origin[3];
    char r[32], d[32];
    UF_DRF_dim_info_p_t dim_info = NULL;
    logical is_displayed = FALSE, done = FALSE;
    tag_t dim = NULL_TAG;
    tag_p_t instances = NULL, curves = NULL, anns = NULL;
    has_limits = FALSE;

    /* Get the display instances */
    error_code = UF_GDT_ask_tol_feat_instance( feature, &num_instances, &instances );

    if ( error_code == 0 && num_instances > 0)
    {
        /* All instances have the same tolerance type - so we just need to process
           the first dimension used for display
        */
        for ( j = 0; j < num_instances && error_code == 0 && !done; j++ )
        {
            error_code = UF_GDT_ask_tags( instances[j], &curves, &num_curves, &anns, &num_anns );
            if ( error_code == 0)
            {
                for ( k = 0; k < num_anns && error_code == 0; k++ )
                {
                    error_code = UF_OBJ_ask_type_and_subtype( anns[k], &etype, &subtype );

                    if ( error_code == 0 && etype == UF_dimension_type )
                    {
                        dim = anns[k];
                        done = TRUE;
                        break;
                    }
                }
            }
            UF_free( curves );
            UF_free( anns );

        }
        UF_free( instances );
    }
    
    if ( dim != NULL_TAG )
    {
        is_displayed = TRUE;

        /* Extract the dimension preferences - we are interested in the tolerance type (mpi[6]) */
        error_code = UF_DRF_ask_object_preferences( dim, mpi, mpr, r, d );

        if ( error_code == 0 )
        {
            error_code = UF_DRF_ask_dim_info( dim, &subtype, origin, &dim_info );

            switch ( mpi[6] )
            {
                case 2:  /* Minus/Plus limit 1 line */
                {
                    ask_displayed_limits( dim_info->text_info->text->full_string, 0, '-', FALSE,
                                          lower_limit, upper_limit);
                    has_limits = TRUE;
                    break;
                }
                case 3:  /* Plus/Minus limit 2 lines */
                {
                    ask_displayed_limits( dim_info->text_info->text->full_string, 2, '!', TRUE,
                                          lower_limit, upper_limit);
                    has_limits = TRUE;
                    break;
                }
                case 10: /* Plus/Minus limit 1 line */
                {
                    ask_displayed_limits( dim_info->text_info->text->full_string, 0, '-', TRUE,
                                          lower_limit, upper_limit);
                    has_limits = TRUE;
                    break;
                }
                case 11:  /* Minus/Plus limit 2 lines */
                {
                    ask_displayed_limits( dim_info->text_info->text->full_string, 2, '!', FALSE,
                                          lower_limit, upper_limit);
                    has_limits = TRUE;
                    break;
                }
                
                case 4:     /* Plus/Minus Tolerance (just nominal string)*/
                {
                    ask_displayed_nominal( dim_info->text_info->text->full_string, displayed_nominal );
                    break;
                }
                
                case 6:     /* Plus Tolerance */
                {
                    ask_displayed_nominal( dim_info->text_info->text->full_string, displayed_nominal );
                    break;
                }
                
                case 7:     /* Minus Tolerance */
                {
                    ask_displayed_nominal( dim_info->text_info->text->full_string, displayed_nominal );
                    break;
                }
                
                case 5:     /* Plus Tolerance and Minus Tolerance */
                {
                    ask_displayed_nominal( dim_info->text_info->text->full_string, displayed_nominal );
                    break;
                }
                
                default:
                    break;
            }

            error_code = UF_DRF_free_dimension( &dim_info );
        }
    }

    return is_displayed;
}



/*---------------------------------------------------------------------------------------
    Determine if the nominal size computed for an angular directed dimension
    agrees with what is displayed.

    Returns the displayed value (converted to radians) if it differs.
    Otherwise returns the computed value.
  ---------------------------------------------------------------------------------------*/
static char *ask_angular_nominal_size(
    tag_t                     feature,                 /* <I> Tag of the feature               */
    UF_GDT_size_tolerance_p_t size_data,               /* <I> Size tolerance data              */
    char                      *computed_nominal_string /* <I> String after initial computation */
)
{
    double computed_nominal, upper_limit = 0, lower_limit = 0, displayed_nominal = 0, delta = .1e-4;
    logical has_limits = FALSE, is_displayed = FALSE;
    char *str = computed_nominal_string;

    sscanf( computed_nominal_string, "%lf", &computed_nominal );

    /* Deternime if displayed instance has a nominal value or limits. */
    is_displayed = ask_displayed_angular_values( feature, &displayed_nominal, &lower_limit, 
                                                 &upper_limit, has_limits );
    if ( is_displayed )
    {
        if ( has_limits )
        {
            lower_limit *= DEGRA;
            upper_limit *= DEGRA;
            
            /* Take complement of TWOPI if computed nominal is not within the displayed limits. */
            if ( computed_nominal < fabs( lower_limit - delta ) ||
                 computed_nominal > fabs( upper_limit + delta ))
            {
                char nominal_str[ MAX_LINE_BUFSIZE ];
                
                UF_free( computed_nominal_string );
                computed_nominal = TWOPI - computed_nominal;
                
                sprintf( nominal_str, "%.*f", size_data->decimal_format,
                         computed_nominal );
                
                str = alloc_string( sizeof( nominal_str ) + 1 );
                strcpy( str, nominal_str );
            }
        }
        else
        {
            displayed_nominal *= DEGRA;
            
            /* Take complement of TWOPI if computed nominal is not the same as the displayed nominal */
            if ( ( fabs( computed_nominal - displayed_nominal ) ) > delta )
            {
                char nominal_str[ MAX_LINE_BUFSIZE ];
                
                computed_nominal = TWOPI - computed_nominal;
                
                UF_free( computed_nominal_string );
                sprintf( nominal_str, "%.*f", size_data->decimal_format,
                         computed_nominal );
                
                str = alloc_string( sizeof( nominal_str ) + 1 );
                strcpy( str, nominal_str );
            }
        }
    }
    return str;
}

/*---------------------------------------------------------------------------*
 * Ask the callout string that corresponds to the input tolerance along with
 * all appended text if so specified.
 *
 * Returns:
 *     Allocated callout string
 *---------------------------------------------------------------------------*/
static char *ask_nominal_size(
    logical                   show_type, /* <I> Show tolerance type */
    UFD_GDT__object_type_t    type,      /* <I> Type of tolerance   */
    UF_GDT_size_tolerance_p_t size_data, /* <I> Size tolerance data */
    tag_t                     feature    /* <I> Tag of the feature  */
)
{
    char nominal_str[ MAX_LINE_BUFSIZE ];
    char *str = NULL;
    int length;

    /* If it is radial size tolerance, use its radius 
     * as the nominal value to display.
     */
    if( size_data->value_type == UF_GDT_RADIAL_SIZE )
        size_data->nominal_value /= 2.0;

    sprintf( nominal_str, "%.*f", size_data->decimal_format,
             size_data->nominal_value );

    if ( !show_type )
        str = copy_string( nominal_str );
    else
    {
        char *size_type = ask_size_tolerance_type( type, size_data );

        str = concatenate_strings( size_type, " ", nominal_str );
    }
    
    /* If it is an angular directed dimension, append 
     * "Radians" as unit to the nominal value 
     */
    if( type == UFD_GDT__ANGULAR_DIRECTED_DIMENSION_TYPE )
    {
        /*  <dps> 17-Jul-2003
            PR 471788.  Use the displayed value if the feature has display instances.
        */
        str = ask_angular_nominal_size( feature, size_data, str );
        length = strlen(str) + strlen("(Radians)") + 1;
        str = realloc_string( str,length );
        strcat( str,"(Radians)" );
    }
        
    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the callout string that corresponds to the input tolerance along with
 * all appended text if so specified.
 *
 * Returns:
 *     Allocated callout string
 *---------------------------------------------------------------------------*/
static char *ask_size_callout(
    logical                   show_all,      /* <I> TRUE to show with       */
                                             /*     nominal & appended text */
    UFD_GDT__feature_data_p_t feature_data,  /* <I> Tolerance feature data  */
    UF_GDT_size_tolerance_p_t size_data,     /* <I> Size tolerance data     */
    UFD_GDT__object_type_t    tol_type,      /* <I> Tolerance type          */
    tag_t                     tolerance      /* <I> Tolerance tag           */
)
{
    char *str = NULL;
    int num = ask_callout_string_index( feature_data, tol_type, tolerance, 0 );

    if ( num < 0 )
        return ( NULL );

    str = copy_string( feature_data->callout_strings[num].string );

    if ( show_all )
    {
        logical show_type = ( tol_type == UFD_GDT__SIZE_TOLERANCE_TYPE );
        char *nominal_str = ask_nominal_size( show_type, tol_type, 
                                              size_data, feature_data->feature);

        if ( str == NULL )
            str = nominal_str;
        else
            str = concatenate_strings( nominal_str, " ", str );

        str = add_appended_text( feature_data->feature, str, tolerance );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask ass callout strings that corresponds to the input feature along with
 * all appended text.
 *
 * Returns:
 *     Allocated callout string
 *---------------------------------------------------------------------------*/
static char *ask_entire_callout(
    UFD_GDT__feature_data_p_t feature_data, /* <I> Tolerance feature data  */
    UFD_GDT__object_type_t current_tol_type /* <I> Current tolerance type */
)
{
    int status;
    int num;
    char *str = NULL;
    char *callout_str = NULL;
    char *size_str = NULL;
    tag_t prev_tolerance = NULL_TAG;
    UF_GDT_tolerance_type_t current_type = (UF_GDT_tolerance_type_t)ask_uf_gdt_tol_type( current_tol_type );

    for ( num = 0; num < feature_data->num_callout_strings; num++ )
    {
        tag_t tolerance = feature_data->callout_strings[num].tolerance;
        UF_GDT_tolerance_type_t type = feature_data->callout_strings[num].type;

        if ( (type == UF_GDT_SIZE_TOLERANCE_TYPE ||
              type == UF_GDT_WALL_THICKNESS_TYPE ||
              type == UF_GDT_LIMITS_AND_FITS_TOLERANCE_TYPE ||
              type == UF_GDT_DEPTH_TOLERANCE_TYPE) && current_type == type )
        {
            UF_GDT_size_tolerance_p_t size_data = NULL;
            UF_GDT_depth_tolerance_p_t depth_data = NULL;
            UFD_GDT__object_type_t tol_type = ask_ufd_gdt_tol_type( type );
 
            /* If it is depth tolerance, get its data and
             * convert the data to size data structure.
             */
            if( current_type == UF_GDT_DEPTH_TOLERANCE_TYPE )
            {
                status = UF_GDT_ask_depth_tolerance_parms( feature_data->feature,
                                                           &depth_data );
                ERROR_CHECK( status, ( "UF_GDT_ask_depth_tolerance_parms", status,
                                       "feature = %u", feature_data->feature ) );
                
                size_data = convert_depth_data_to_size_data(depth_data);
                
                /* Clean up */
                status = UF_GDT_free( UF_GDT_DEPTH_TOL_TYPE, depth_data );
                ERROR_CHECK( status, ( "UF_GDT_free", status,
                                       "data type = UF_GDT_DEPTH_TOL_TYPE(%d)",
                                       UF_GDT_DEPTH_TOL_TYPE ) );
                
                UF_free( depth_data );
            }
            else
            {
                status = UF_GDT_ask_size_tolerance_parms( feature_data->feature,
                                                          &size_data );
                ERROR_CHECK( status, ( "UF_GDT_ask_size_tolerance_parms", status,
                                       "feature = %u", feature_data->feature ) );
            }
            
            size_str = ask_size_callout( TRUE, feature_data, size_data,
                                         tol_type,
                                         tolerance );

            status = UF_GDT_free( UF_GDT_SIZE_TOL_TYPE, size_data );
            ERROR_CHECK( status, ( "UF_GDT_free", status,
                                   "data type = UF_GDT_SIZE_TOL_TYPE(%d)",
                                   UF_GDT_SIZE_TOL_TYPE ) );
            UF_free( size_data );
        }
        else if ( type == UF_GDT_DIRECTED_DIMENSION_TYPE )
        {
            UFD_GDT__object_type_t tol_type;
            UF_GDT_directed_dimension_p_t dir_dim_data;

            status = UF_GDT_ask_directed_dimension( feature_data->feature,
                                                    &dir_dim_data );
            ERROR_CHECK( status, ( "UF_GDT_ask_directed_dimension", status,
                                   "feature = %u", feature_data->feature ) );

            if ( dir_dim_data->type == UF_GDT_ANGULAR_DIRECTED_DIMENSION )
                tol_type = UFD_GDT__ANGULAR_DIRECTED_DIMENSION_TYPE;
            else
                tol_type = UFD_GDT__LINEAR_DIRECTED_DIMENSION_TYPE;

            size_str = ask_size_callout( TRUE, feature_data,
                                         &dir_dim_data->size_data,
                                         tol_type, tolerance );

            status = UF_GDT_free( UF_GDT_SIZE_TOL_TYPE,
                                  &dir_dim_data->size_data );
            ERROR_CHECK( status, ( "UF_GDT_free", status,
                                   "data type = UF_GDT_SIZE_TOL_TYPE(%d)",
                                   UF_GDT_SIZE_TOL_TYPE ) );
            UF_free( dir_dim_data );
        }
        else if ( type == UF_GDT_GEOMETRIC_TOLERANCE_TYPE )
        {
            if ( tolerance != prev_tolerance )
            {
                char *fcf_str = ask_fcf_callout( TRUE, feature_data,
                                                 tolerance, 0 );

                if ( callout_str == NULL )
                    callout_str = fcf_str;
                else
                {
                    callout_str = concatenate_strings( callout_str, "||",
                                                       fcf_str );
                    UF_free( fcf_str );
                }
            }
        }

        prev_tolerance = tolerance;
    }

    if ( size_str == NULL )
        str = callout_str;

    else if ( callout_str == NULL )
        str = size_str;

    else
    {
        str = concatenate_strings( size_str, "|", callout_str );
        UF_free( callout_str );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the tolerance index string
 *
 * Returns:
 *     Allocated tolerance index string
 *---------------------------------------------------------------------------*/
static char *ask_tolerance_index_string(
    logical use_frame_num,  /* <I> TRUE to take frame_num into consideration */
    tag_t   tolerance_index,/* <I> Tolerance to query                        */
    int     frame_num       /* <I> Frame number to query if FCF              */
)
{
    char *frame_suffix;
    char tol_index_str[ MAX_LINE_BUFSIZE ];

    if ( !use_frame_num )
        frame_suffix = "";
    else if ( frame_num == 0 )
        frame_suffix = " Upper";
    else
        frame_suffix = " Lower";

    sprintf( tol_index_str, "%d%s", tolerance_index, frame_suffix );

    return ( copy_string( tol_index_str ) );
}

/*---------------------------------------------------------------------------*
 * Ask the tolerance index in the part that the input feature was pulled from
 *
 * Returns:
 *     The allocated string of the tolerance index in the part that feature
 *     was pulled from or NULL if the feature is not a pulled feature
 *---------------------------------------------------------------------------*/
static char *ask_component_tolerance_index(
    logical use_frame_num,  /* <I> TRUE to take frame_num into consideration */
    tag_t   feature,        /* <I> Feature containing tolerance              */
    tag_t   tolerance,      /* <I> Tolerance to query                        */
    int     frame_num       /* <I> Frame number to query if FCF              */
)
{
    char *str = NULL;
    int status;
    logical is_pulled;

    status = UF_GDT_is_pulled_tolerance( feature, &is_pulled );
    ERROR_CHECK( status, ( "UF_GDT_is_pulled_tolerance", status,
                           "feature = %u", feature ) );

    if ( is_pulled )
    {
        int tol_index;

        status = UF_GDT_ask_component_tolerance_index( tolerance, &tol_index );
        ERROR_CHECK( status, ( "UF_GDT_ask_component_tolerance_index", status,
                               "tolerance = %u", tolerance ) );

        str = ask_tolerance_index_string( use_frame_num, tol_index, frame_num );
    }

    return ( str );
}

/*---------------------------------------------------------------------------*
 * Ask the faces of the datums referenced by the input frame
 *
 * Returns:
 *     Allocated list of faces
 *---------------------------------------------------------------------------*/
static char *ask_datum_face_references(
    UF_GDT_data_frame_p_t frame /* <I> Feature control frame data to query */
)
{
    char *str = NULL;
    int num, num_datums = 0, num_faces = 0;
    tag_t datums[3]= {NULL_TAG, NULL_TAG, NULL_TAG};
    tag_p_t faces = NULL;

    if ( frame->primary != NULL && frame->primary->datum_feature != NULL_TAG )
        datums[num_datums++] = frame->primary->datum_feature;

    if ( frame->secondary != NULL && frame->secondary->datum_feature != NULL_TAG )
        datums[num_datums++] = frame->secondary->datum_feature;

    if ( frame->tertiary != NULL && frame->tertiary->datum_feature != NULL_TAG )
        datums[num_datums++] = frame->tertiary->datum_feature;

    for ( num = 0; num < num_datums; num++ )
    {
        int num_datum_faces, status;
        tag_p_t datum_faces;

        status = UF_GDT_ask_faces( datums[num], &num_datum_faces, &datum_faces );
        ERROR_CHECK( status, ( "UF_GDT_ask_faces", status,
                               "datum = %u", datums[num] ) );

        add_to_sorted_tag_list( num_datum_faces, datum_faces, &num_faces, &faces );
        UF_free( datum_faces );
    }

    str = ask_face_list( num_faces, faces );
    UF_free( faces );

    return ( str );
}

/*---------------------------------------------------------------------------------------
    Strings are of the form <Tlow!high>
                            <Thigh!low>
                            high - low
                            low - high
  ---------------------------------------------------------------------------------------*/
static char *ask_dim_limit(
    char *text,           /* <I> Displayed main text string                 */
    int prefix_len,       /* <I> Length of prefix string, e.g. 2 for "<T"   */
    char delimiter,       /* <I> Break between sizes, e.g. '!' or '-'       */
    logical upper_first,  /* <I> TRUE if high limit is first                */
    logical is_upper      /* <I> TRUE if upper limit requested - else lower */
)
{
    int j, len, k;
    char size_0[132], size_1[132];
    char *p = text + prefix_len;
    char *str;


    /* Extract the first size from the string */
    len = strlen(p);
    for ( j = 0, k = 0; j < len; j++, p++ )
    {
        if ( *p == delimiter )
            break;

        else if ( *p == '.' || ( *p >= '0' && *p <= '9' ) )
            size_0[k++] = *p;
    }
    size_0[k] = '\0';
    p++;

    /* Extract the second size from the string */
    len = strlen( p );
    for ( j = 0, k = 0; j < len; j++, p++ )
    {
        if ( *p == '>' )
            break;

        else if ( *p == '.' || ( *p >= '0' && *p <= '9' ) )
            size_1[k++] = *p;
    }
    size_1[k] = '\0';

    if ( is_upper )
    {
        if ( upper_first )
        {
            str = alloc_string( sizeof( size_0 ) + 1 );
            strcpy( str, size_0 );
        }
        else
        {
            str = alloc_string( sizeof( size_1 ) + 1 );
            strcpy( str, size_1 );
        }
    }
    else
    {
        if ( upper_first )
        {
            str = alloc_string( sizeof( size_1 ) + 1 );
            strcpy( str, size_1 );
        }
        else
        {
            str = alloc_string( sizeof( size_0 ) + 1 );
            strcpy( str, size_0 );
        }
    }

    return str;
}

/*---------------------------------------------------------------------------------------
    Write out the high and low limits for a dimension if is is displayed as limits.
  ---------------------------------------------------------------------------------------*/
static char *ask_limit_of_dim(
    tag_t dim,       /* <I> Dimension to process                  */
    logical is_upper /* <I> TRUE if upper limit, else lower limit */
)
{
    int error_code = 0, subtype;
    int mpi[100];
    double mpr[100], origin[3];
    char r[32], d[32];
    UF_DRF_dim_info_p_t dim_info = NULL;
    char *str = NULL;
        

    /* Extract the dimension preferences - we are interested in the tolerance type (mpi[6]) */
    error_code = UF_DRF_ask_object_preferences( dim, mpi, mpr, r, d );

    if ( error_code == 0 )
    {
        error_code = UF_DRF_ask_dim_info( dim, &subtype, origin, &dim_info );

        switch ( mpi[6] )
        {
            case 2:  /* Minus/Plus limit 1 line */
            {
                str = ask_dim_limit( dim_info->text_info->text->full_string, 0, '-', FALSE, is_upper );
                break;
            }
            case 3:  /* Plus/Minus limit 2 lines */
            {
                str = ask_dim_limit( dim_info->text_info->text->full_string, 2, '!', TRUE, is_upper );
                break;
            }
            case 10: /* Plus/Minus limit 1 line */
            {
                str = ask_dim_limit( dim_info->text_info->text->full_string, 0, '-', TRUE, is_upper );
                break;
            }
            case 11:  /* Minus/Plus limit 2 lines */
            {
                str = ask_dim_limit( dim_info->text_info->text->full_string, 2, '!', FALSE, is_upper );
                break;
            }
            default:
                break;
        }

        error_code = UF_DRF_free_dimension( &dim_info );
    }
    return str;
}

/*---------------------------------------------------------------------------------------
    Process each tolerance feature.
  ---------------------------------------------------------------------------------------*/
static char *ask_tol_feat_limit(
    tag_t tol_feat,                          /* <I> Tolerance feature to process    */
    UFD_GDT__object_type_t tolerance_type,   /* <I> Type of tolerance being queried */
    logical is_upper                         /* <I> TRUE if upper limit requested   */
)
{
    int j, k, etype, subtype;
    int error_code = 0, num_instances = 0, num_curves = 0, num_anns = 0;
    logical has_size_tol = FALSE, done = FALSE;
    tag_p_t instances = NULL, curves = NULL, anns = NULL;
    char *str = NULL;

    /* Only process features that are tolerance features */
    error_code = UF_GDT_has_size_tolerance( tol_feat, &has_size_tol );

    if ( error_code == 0 && ( has_size_tol || 
                              tolerance_type == UFD_GDT__ANGULAR_DIRECTED_DIMENSION_TYPE ||
                              tolerance_type == UFD_GDT__LINEAR_DIRECTED_DIMENSION_TYPE ) )
    {
        /* Get the display instances */
        error_code = UF_GDT_ask_tol_feat_instance( tol_feat, &num_instances, &instances );

        if ( error_code == 0 && num_instances > 0 )
        {
            /* All instances have the same tolerance type - so we just need to process
               the first dimension used for display
            */
            for ( j = 0; j < num_instances && error_code == 0 && !done; j++ )
            {
                error_code = UF_GDT_ask_tags( instances[j], &curves, &num_curves, &anns, &num_anns );

                if ( error_code == 0 )
                {
                    for ( k = 0; k < num_anns && error_code == 0; k++ )
                    {
                        error_code = UF_OBJ_ask_type_and_subtype( anns[k], &etype, &subtype );

                        if ( error_code == 0 && etype == UF_dimension_type )
                        {
                            str = ask_limit_of_dim( anns[k], is_upper );
                            done = TRUE;
                            break;
                        }
                    }
                }
                UF_free( curves );
                UF_free( anns );

            }
            UF_free( instances );
        }
    }
    return str;
}

/*---------------------------------------------------------------------------------------
    Determines the displayed lower limit if exists and returns as a string,
    otherwise returns a blank string.
  ---------------------------------------------------------------------------------------*/
static char *ask_lower_limit(
    tag_t feature,                           /* <I> Tag of the feature              */
    UFD_GDT__object_type_t tolerance_type    /* <I> Type of tolerance being queried */
)
{
    char *str = NULL;
    str = ask_tol_feat_limit( feature, tolerance_type, FALSE );
    if ( str == NULL )
    {
        str = alloc_string( 2 );
        strcpy( str, " " );
    }
    return ( str ) ;
}

/*---------------------------------------------------------------------------------------
    Determines the displayed upper limit if exists and returns as a string,
    otherwise returns a blank string.
  ---------------------------------------------------------------------------------------*/
static char *ask_upper_limit(
    tag_t feature,                           /* <I> Tag of the feature              */
    UFD_GDT__object_type_t tolerance_type    /* <I> Type of tolerance being queried */
)
{
    char *str = NULL;
    str = ask_tol_feat_limit( feature, tolerance_type, TRUE );
    if ( str == NULL )
    {
        str = alloc_string( 2 );
        strcpy( str, " " );
    }
    return ( str ) ;
}


/*---------------------------------------------------------------------------*
 * Ask information from the feature control frame
 *---------------------------------------------------------------------------*/
static void ask_fcf_info(
    UFD_GDT__feature_data_p_t feature_data,/* <I>   Tolerance feature data   */
    tag_t                     fcf,         /* <I>   Feature control frame tag*/
    int                       frame_num,   /* <I>   Frame number to query    */
    UF_GDT_fcf_p_t            fcf_data,    /* <I>   Feature control frame    */
                                           /*       data                     */
    UFD_GDT__object_info_p_t  object_info  /* <I/O> Object data to report    */
)
{
    int num;
    logical is_composite = ( fcf_data->num_frames > 1 );
    UF_GDT_data_frame_p_t frame = &fcf_data->data_frame[frame_num];

    for ( num = 0; num < object_info->count; num++ )
    {
        char str[ MAX_LINE_BUFSIZE ];
        int status, tol_index;

        /* Feature control frame data */
        switch ( object_info->list[num].type )
        {
            case UFD_GDT__TOLERANCE_NUMBER_INFO:
                status = UF_GDT_ask_tolerance_index( fcf, &tol_index );
                ERROR_CHECK( status, ( "UF_GDT_ask_tolerance_index", status,
                                       "fcf = %u", fcf ) );

                object_info->list[num].data =
                    ask_tolerance_index_string( is_composite, tol_index,
                                                frame_num );
                break;

            case UFD_GDT__TOLERANCE_TYPE_INFO:
                object_info->list[num].data = ask_characteristic( fcf_data );
                break;

            case UFD_GDT__PULLED_FROM_TOLERANCE_NUMBER_INFO:
                object_info->list[num].data =
                    ask_component_tolerance_index( is_composite,
                                                   feature_data->feature,
                                                   fcf, frame_num );
                break;

            case UFD_GDT__CALLOUT_STRING_INFO:
                object_info->list[num].data =
                    ask_fcf_callout( FALSE, feature_data, fcf, frame_num );
                break;

            case UFD_GDT__ENTIRE_CALLOUT_STRING_INFO:
                object_info->list[num].data = ask_entire_callout( feature_data,  object_info->tolerance_type);
                break;

            case UFD_GDT__TOLERANCE_BAND_INFO:
                sprintf( str, "%.*f", frame->tolerance_zone->decimal_format,
                         frame->tolerance_zone->value );
                object_info->list[num].data = copy_string( str );
                break;

            case UFD_GDT__PRIMARY_DATUM_INFO:
                if ( frame->primary != NULL )
                {
                    status = UF_GDT_ask_label_of_datum( frame->primary->datum_feature,
                                                        &object_info->list[num].data );
                    ERROR_CHECK( status, ( "UF_GDT_ask_label_of_datum", status,
                                           "datum = %u", frame->primary->datum_feature ) );
                }
                break;

            case UFD_GDT__SECONDARY_DATUM_INFO:
                if ( frame->secondary != NULL )
                {
                    status = UF_GDT_ask_label_of_datum( frame->secondary->datum_feature,
                                                        &object_info->list[num].data );
                    ERROR_CHECK( status, ( "UF_GDT_ask_label_of_datum", status,
                                           "datum = %u", frame->secondary->datum_feature ) );
                }
                break;

            case UFD_GDT__TERTIARY_DATUM_INFO:
                if ( frame->tertiary != NULL )
                {
                    status = UF_GDT_ask_label_of_datum( frame->tertiary->datum_feature,
                                                        &object_info->list[num].data );
                    ERROR_CHECK( status, ( "UF_GDT_ask_label_of_datum", status,
                                           "datum = %u", frame->tertiary->datum_feature ) );
                }
                break;

            case UFD_GDT__RELATED_FACES_INFO:
                object_info->list[num].data =
                    ask_datum_face_references( frame );
            break;

            case UFD_GDT__STANDARD_KEYWORDS_INFO:
                object_info->list[num].data =
                    ask_keywords( TRUE, feature_data->part,
                                  feature_data->feature_parms->modifier_data,
                                  frame->modifier_data );
                break;

            case UFD_GDT__USER_DEFINED_KEYWORDS_INFO:
                object_info->list[num].data =
                    ask_keywords( FALSE, feature_data->part,
                                  feature_data->feature_parms->modifier_data,
                                  frame->modifier_data );
                break;

            case UFD_GDT__ABOVE_APPENDED_TEXT_INFO:
            case UFD_GDT__BELOW_APPENDED_TEXT_INFO:
            case UFD_GDT__BEFORE_APPENDED_TEXT_INFO:
            case UFD_GDT__AFTER_APPENDED_TEXT_INFO:
                object_info->list[num].data =
                    ask_appended_text( feature_data->feature, fcf,
                                       object_info->list[num].type );
                break;

            case UFD_GDT__DISPLAYED_LOWER_LIMIT_INFO:
                object_info->list[num].data = ask_lower_limit( feature_data->feature,
                                                               object_info->tolerance_type );
                break;

            case UFD_GDT__DISPLAYED_UPPER_LIMIT_INFO:
                object_info->list[num].data = ask_upper_limit( feature_data->feature,
                                                               object_info->tolerance_type );
                break;

            default:
                object_info->list[num].data =
                    ask_feature_info_data( object_info->list[num].type, FALSE,
                                           feature_data, object_info );
                break;
        }
    }
}

/*---------------------------------------------------------------------------*
 * Add information on the feature control frame specified to the part report
 * data
 *---------------------------------------------------------------------------*/
static void add_fcf_info(
    UFD_GDT__report_p_t       report,       /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data, /* <I>   Tolerance feature data */
    tag_t                     fcf           /* <I>   Feature control frame  */
)
{
    int num, status;
    UF_GDT_fcf_p_t fcf_data;

    status = UF_GDT_ask_fcf_parms( fcf, &fcf_data );
    ERROR_CHECK( status, ( "UF_GDT_ask_fcf_parms", status, "fcf = %u", fcf ) );

    for ( num = 0; num < fcf_data->num_frames; num++ )
    {
        UFD_GDT__object_info_t object_info;

        init_info_data( report, feature_data->part, feature_data->feature,
                        fcf, UFD_GDT__FEATURE_CONTROL_FRAME_TYPE,
                        &object_info );

        ask_fcf_info( feature_data, fcf, num, fcf_data, &object_info );

        add_to_part_info_list( report, &object_info );
    }

    status = UF_GDT_free( UF_GDT_FCF_TYPE, fcf_data );
    ERROR_CHECK( status, ( "UF_GDT_free", status,
                           "data type = UF_GDT_FCF_TYPE(%d)",
                           UF_GDT_FCF_TYPE ) );
    UF_free( fcf_data );
}

/*---------------------------------------------------------------------------*
 * Add information on the all the tolerance feature's feature control frames
 * to the part report data
 *---------------------------------------------------------------------------*/
static void add_fcf_list_info(
    UFD_GDT__report_p_t       report,      /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data /* <I>   Tolerance feature data */
)
{
    int num, num_fcfs, status;
    tag_p_t fcfs;

    status = UF_GDT_ask_fcf_tags( feature_data->feature, &num_fcfs, &fcfs );
    ERROR_CHECK( status, ( "UF_GDT_ask_fcf_tags", status,
                           "feature = %u", feature_data->feature ) );

    for ( num = 0; num < num_fcfs; num++ )
        add_fcf_info( report, feature_data, fcfs[num] );

    UF_free( fcfs );
}

/*---------------------------------------------------------------------------*
 * Ask information from the size tolerance
 *---------------------------------------------------------------------------*/
static void ask_size_tolerance_info(
    UFD_GDT__feature_data_p_t feature_data, /* <I>   Tolerance feature data */
    UF_GDT_size_tolerance_p_t size_data,    /* <I>   Size tolerance data    */
    UFD_GDT__object_info_p_t  object_info   /* <I/O> Object data to report  */
)
{
    int num;

    for ( num = 0; num < object_info->count; num++ )
    {
        char str[ MAX_LINE_BUFSIZE ];
        int status, tol_index;
        double tol_band;

        /* Size tolerance/directed dimension data */
        switch ( object_info->list[num].type )
        {
            case UFD_GDT__TOLERANCE_NUMBER_INFO:
                status = UF_GDT_ask_tolerance_index( feature_data->feature, &tol_index );
                ERROR_CHECK( status, ( "UF_GDT_ask_tolerance_index", status,
                                       "feature = %u", feature_data->feature ) );

                object_info->list[num].data =
                    ask_tolerance_index_string( FALSE, tol_index, 0 );
                break;

            case UFD_GDT__TOLERANCE_TYPE_INFO:
                object_info->list[num].data =
                    ask_size_tolerance_type( object_info->tolerance_type, 
                                             size_data );
                break;

            case UFD_GDT__PULLED_FROM_TOLERANCE_NUMBER_INFO:
                object_info->list[num].data =
                    ask_component_tolerance_index( FALSE, feature_data->feature,
                                                   feature_data->feature, 0 );
                break;

            case UFD_GDT__CALLOUT_STRING_INFO:
                object_info->list[num].data =
                    ask_size_callout( FALSE, feature_data, size_data,
                                      object_info->tolerance_type,
                                      feature_data->feature );
                break;

            case UFD_GDT__ENTIRE_CALLOUT_STRING_INFO:
                object_info->list[num].data = ask_entire_callout( feature_data, object_info->tolerance_type );
                break;

            case UFD_GDT__NOMINAL_SIZE_INFO:
                /* Don't display nominal size information for thread tolerance */
                if( object_info->tolerance_type != UFD_GDT__THREAD_TOLERANCE_TYPE )
                {
                    object_info->list[num].data =
                        ask_nominal_size( FALSE, object_info->tolerance_type,
                                          size_data, feature_data->feature );
                }
                break;

            case UFD_GDT__TOLERANCE_BAND_INFO:
                /* Don't display tolerance band for thread tolerance */
                if( object_info->tolerance_type != UFD_GDT__THREAD_TOLERANCE_TYPE )
                {
                    tol_band = ( fabs( size_data->upper_tol.value ) +
                                 fabs( size_data->lower_tol.value ) );
                    sprintf( str, "%.*f", size_data->upper_tol.decimal_format,
                             tol_band );
                    object_info->list[num].data = copy_string( str );
                }
                break;

            case UFD_GDT__STANDARD_KEYWORDS_INFO:
                object_info->list[num].data =
                    ask_keywords( TRUE, feature_data->part,
                                  feature_data->feature_parms->modifier_data,
                                  size_data->modifier_data );
                break;

            case UFD_GDT__USER_DEFINED_KEYWORDS_INFO:
                object_info->list[num].data =
                    ask_keywords( FALSE, feature_data->part,
                                  feature_data->feature_parms->modifier_data,
                                  size_data->modifier_data );
                break;

            case UFD_GDT__ABOVE_APPENDED_TEXT_INFO:
            case UFD_GDT__BELOW_APPENDED_TEXT_INFO:
            case UFD_GDT__BEFORE_APPENDED_TEXT_INFO:
            case UFD_GDT__AFTER_APPENDED_TEXT_INFO:
                object_info->list[num].data =
                    ask_appended_text( feature_data->feature,
                                       feature_data->feature,
                                       object_info->list[num].type );
                break;

            case UFD_GDT__DISPLAYED_LOWER_LIMIT_INFO:
                object_info->list[num].data = ask_lower_limit( feature_data->feature,
                                                               object_info->tolerance_type );
                break;

            case UFD_GDT__DISPLAYED_UPPER_LIMIT_INFO:
                object_info->list[num].data = ask_upper_limit( feature_data->feature,
                                                               object_info->tolerance_type );
                break;

            default:
                object_info->list[num].data =
                    ask_feature_info_data( object_info->list[num].type, FALSE,
                                           feature_data, object_info );
                break;
        }
    }
}

/*---------------------------------------------------------------------------*
 * Convert the depth tolerance data to size tolerance data.
 *---------------------------------------------------------------------------*/
static UF_GDT_size_tolerance_p_t convert_depth_data_to_size_data(
    UF_GDT_depth_tolerance_p_t depth_tol_data
)
{
    int status;
    UF_GDT_size_tolerance_p_t size_tol_data = ( UF_GDT_size_tolerance_p_t )
        UF_allocate_memory( sizeof( UF_GDT_size_tolerance_t), &status );
    ERROR_CHECK( status, ( "UF_allocate_memory", status, "" ) );

    size_tol_data->value_type = UF_GDT_NO_SIZE;
    size_tol_data->dimension = NULL_TAG;
    size_tol_data->nominal_value = depth_tol_data->nominal_value;
    size_tol_data->upper_tol = depth_tol_data->upper_tol;
    size_tol_data->lower_tol = depth_tol_data->lower_tol;
    size_tol_data->tol_format = depth_tol_data->tol_format;
    size_tol_data->modifier_data = NULL;
    size_tol_data->decimal_format = depth_tol_data->decimal_format;

    return size_tol_data;
}
/*---------------------------------------------------------------------------*
 * Convert the thread tolerance data to size tolerance data.
 *---------------------------------------------------------------------------*/
static UF_GDT_size_tolerance_p_t convert_thread_data_to_size_data(
    UF_GDT_thread_tolerance_p_t thread_tol_data
)
{
    int status;
    UF_GDT_size_tolerance_p_t size_tol_data = ( UF_GDT_size_tolerance_p_t )
        UF_allocate_memory( sizeof( UF_GDT_size_tolerance_t), &status );
    ERROR_CHECK( status, ( "UF_allocate_memory", status, "" ) );

    size_tol_data->value_type = UF_GDT_NO_SIZE;
    size_tol_data->dimension = NULL_TAG;
    size_tol_data->modifier_data = thread_tol_data->modifier_data;

    return size_tol_data;
}

/*---------------------------------------------------------------------------*
 * Add information on the size tolerance specified to the part report data
 *---------------------------------------------------------------------------*/
static void add_size_tolerance_info(
    UFD_GDT__report_p_t       report,       /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data, /* <I>   Tolerance feature data */
    UF_GDT_tolerance_type_t type            /* <I> Tolerance type */
)
{
    int status;
    UFD_GDT__object_info_t object_info;
    UF_GDT_size_tolerance_p_t size_tol_data = NULL;
    UF_GDT_depth_tolerance_p_t depth_tol_data = NULL;
    UF_GDT_thread_tolerance_p_t thread_tol_data = NULL;
    UFD_GDT__object_type_t tol_type = ask_ufd_gdt_tol_type(type);

    /* If it is depth tolerance or thread tolerance, get their
     * data and then convert these data to size data structure.
     */
    if( type == UF_GDT_DEPTH_TOLERANCE_TYPE )
    {
        status = UF_GDT_ask_depth_tolerance_parms( feature_data->feature,
                                              &depth_tol_data );
        ERROR_CHECK( status, ( "UF_GDT_ask_depth_tolerance_parms", status,
                               "feature = %u", feature_data->feature ) );

        size_tol_data = convert_depth_data_to_size_data(depth_tol_data);

        /* Clean up */
        status = UF_GDT_free( UF_GDT_DEPTH_TOL_TYPE, depth_tol_data );
        ERROR_CHECK( status, ( "UF_GDT_free", status,
                           "data type = UF_GDT_DEPTH_TOL_TYPE(%d)",
                           UF_GDT_DEPTH_TOL_TYPE ) );

        UF_free( depth_tol_data );
    }
    else if( type == UF_GDT_THREAD_TOLERANCE_TYPE )
    {
        status = UF_GDT_ask_thread_tolerance_parms( feature_data->feature,
                                              &thread_tol_data );
        ERROR_CHECK( status, ( "UF_GDT_ask_thread_tolerance_parms", status,
                               "feature = %u", feature_data->feature ) );

        size_tol_data = convert_thread_data_to_size_data(thread_tol_data);
    }
    else
    {    
        status = UF_GDT_ask_size_tolerance_parms( feature_data->feature,
                                                  &size_tol_data );
        ERROR_CHECK( status, ( "UF_GDT_ask_size_tolerance_parms", status,
                               "feature = %u", feature_data->feature ) );
    }

    init_info_data( report, feature_data->part, feature_data->feature,
                    NULL_TAG, tol_type,
                    &object_info );

    ask_size_tolerance_info( feature_data, size_tol_data, &object_info );

    add_to_part_info_list( report, &object_info );

    status = UF_GDT_free( UF_GDT_SIZE_TOL_TYPE, size_tol_data );
    ERROR_CHECK( status, ( "UF_GDT_free", status,
                           "data type = UF_GDT_SIZE_TOL_TYPE(%d)",
                           UF_GDT_SIZE_TOL_TYPE ) );

    UF_free( size_tol_data );
    UF_free( thread_tol_data );
}

/*---------------------------------------------------------------------------*
 * Add information on the directed dimension specified to the part report data
 *---------------------------------------------------------------------------*/
static void add_directed_dimension_info(
    UFD_GDT__report_p_t       report,      /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data /* <I>   Tolerance feature data */
)
{
    int status;
    UFD_GDT__object_info_t object_info;
    UFD_GDT__object_type_t type;
    UF_GDT_directed_dimension_p_t dir_dim_data;

    status = UF_GDT_ask_directed_dimension( feature_data->feature,
                                            &dir_dim_data );
    ERROR_CHECK( status, ( "UF_GDT_ask_directed_dimension", status,
                           "feature = %u", feature_data->feature ) );

    if ( dir_dim_data->type == UF_GDT_ANGULAR_DIRECTED_DIMENSION )
        type = UFD_GDT__ANGULAR_DIRECTED_DIMENSION_TYPE;
    else
        type = UFD_GDT__LINEAR_DIRECTED_DIMENSION_TYPE;

    init_info_data( report, feature_data->part, feature_data->feature,
                    NULL_TAG, type, &object_info );

    ask_size_tolerance_info( feature_data, &dir_dim_data->size_data, &object_info );

    add_to_part_info_list( report, &object_info );

    UF_free( dir_dim_data );
}

/*---------------------------------------------------------------------------*
 * Initialize the UFD_GDT__object_s structure specified
 *---------------------------------------------------------------------------*/
static void init_feature_data(
    UFD_GDT__feature_data_p_t feature_data
                                /* <O> Tolerance feature data to initialize */
)
{
    feature_data->part                = NULL_TAG;
    feature_data->feature             = NULL_TAG;
    feature_data->feature_parms       = NULL;
    feature_data->geom_def            = NULL;
    feature_data->num_callout_strings = 0;
    feature_data->callout_strings     = NULL;
}

/*---------------------------------------------------------------------------*
 * Free the data contained by the UFD_GDT__object_s structure specified
 *---------------------------------------------------------------------------*/
static void free_feature_data(
    UFD_GDT__feature_data_p_t feature_data
                                /* <I/O> Tolerance feature data to free */
)
{
    int num, status;

    status = UF_GDT_free( UF_GDT_FEAT_PARMS_TYPE, feature_data->feature_parms );
    ERROR_CHECK( status, ( "UF_GDT_free", status,
                           "data type = UF_GDT_FEAT_PARMS_TYPE(%d)",
                           UF_GDT_FEAT_PARMS_TYPE ) );
    UF_free( feature_data->feature_parms );

    UF_free( feature_data->geom_def );

    for ( num = 0; num < feature_data->num_callout_strings; num++ )
    {
        status = UF_GDT_free( UF_GDT_CALLOUT_STR_TYPE,
                              &feature_data->callout_strings[num] );
        ERROR_CHECK( status, ( "UF_GDT_free", status,
                               "data type = UF_GDT_CALLOUT_STR_TYPE(%d)",
                               UF_GDT_CALLOUT_STR_TYPE ) );
    }

    UF_free( feature_data->callout_strings );

    init_feature_data( feature_data );
}

/*---------------------------------------------------------------------------*
 * Add all information on the current feature to the part report data
 *---------------------------------------------------------------------------*/
static void process_feature(
    UFD_GDT__report_p_t report, /* <I>   Part report definition & data     */
    tag_t part,                 /* <I>   Part containing tolerance feature */
    tag_t feature               /* <I>   Tolerance feature to query        */
)
{
    int num_tol_types, status;
    UF_GDT_tolerance_type_p_t tol_types;
    UFD_GDT__feature_data_t feature_data;

    init_feature_data( &feature_data );

    feature_data.part    = part;
    feature_data.feature = feature;

    status = UF_GDT_ask_feature_parms( feature, &feature_data.feature_parms );
    ERROR_CHECK( status, ( "UF_GDT_ask_feature_parms", status,
                           "feature = %u", feature ) );

    status = UF_GDT_ask_geometric_definition( feature, &feature_data.geom_def );
    ERROR_CHECK( status, ( "UF_GDT_ask_geometric_definition", status,
                           "feature = %u", feature ) );

    status = UF_GDT_ask_callout_strings( feature,
                                         &feature_data.num_callout_strings,
                                         &feature_data.callout_strings );
    ERROR_CHECK( status, ( "UF_GDT_ask_callout_strings", status,
                           "feature = %u", feature ) );

    status = UF_GDT_ask_tolerance_types( feature, &num_tol_types, &tol_types );
    ERROR_CHECK( status, ( "UF_GDT_ask_tolerance_types", status,
                           "feature = %u", feature ) );

    if ( num_tol_types == 0 )
    {
        add_empty_feature_info( report, &feature_data );
    }
    else
    {
        int num;

        for ( num = 0; num < num_tol_types; num++ )
        {
            switch ( tol_types[num] )
            {
                case UF_GDT_DATUM_IDENTIFIER_TYPE:
                case UF_GDT_DATUM_MULTIPLE_TYPE:
                case UF_GDT_DATUM_TARGET_POINT_TYPE:
                case UF_GDT_DATUM_TARGET_LINE_TYPE:
                case UF_GDT_DATUM_TARGET_DIA_TYPE:
                case UF_GDT_DATUM_TARGET_RECT_TYPE:
                case UF_GDT_DATUM_TARGET_CYL_TYPE:
                    add_datum_info( report, &feature_data, tol_types[num] );
                    break;

                case UF_GDT_GEOMETRIC_TOLERANCE_TYPE:
                    add_fcf_list_info( report, &feature_data );
                    break;

                case UF_GDT_SIZE_TOLERANCE_TYPE:
                case UF_GDT_WALL_THICKNESS_TYPE:
                case UF_GDT_DEPTH_TOLERANCE_TYPE:
                case UF_GDT_LIMITS_AND_FITS_TOLERANCE_TYPE: 
                case UF_GDT_THREAD_TOLERANCE_TYPE:    
                    add_size_tolerance_info( report, &feature_data, tol_types[num] );
                    break;

                case UF_GDT_DIRECTED_DIMENSION_TYPE:
                    add_directed_dimension_info( report, &feature_data );
                    break;                    

                default:
                    break;
            }
        }
    }

    free_feature_data( &feature_data );
    UF_free( tol_types );
}

/*---------------------------------------------------------------------------*
 * Function to display the titles for each report field
 *---------------------------------------------------------------------------*/
static void output_header(
    tag_t part,                 /* <I> Part being queried     */
    UFD_GDT__report_p_t report  /* <I> Part report definition */
)
{
    int num;
    int status;
    int units;
    UFD_GDT__object_info_t header;

    status = UF_PART_ask_units( part, &units );
    ERROR_CHECK( status, ( "UF_PART_ask_units", status,
                           "part = %u", part ) );

    init_info_data( report, part, NULL_TAG, NULL_TAG,
                    UFD_GDT__EMPTY_FEATURE_TYPE, &header );

    for ( num = 0; num < report->num_fields; num++ )
    {
        header.list[num].type = report->fields[num].type;
        header.list[num].data = copy_string( report->fields[num].title );

        if ( header.list[num].type == UFD_GDT__CALLOUT_STRING_INFO        ||
             header.list[num].type == UFD_GDT__ENTIRE_CALLOUT_STRING_INFO ||
             header.list[num].type == UFD_GDT__TOLERANCE_BAND_INFO        ||
             header.list[num].type == UFD_GDT__NOMINAL_SIZE_INFO )
        {
            char units_str[6];
            int len;

            if ( units == UF_PART_METRIC )
            {
                strcpy( units_str, " (MM)");
            }
            else
            {
                strcpy( units_str, " (IN)");
            }

            header.list[num].data = concatenate_strings( header.list[num].data,
                                                         units_str, NULL );

            len = strlen( header.list[num].data );

            if ( len > report->fields[num].max_len )
                report->fields[num].max_len = len;
        }
    }

    (*report->output_fun)( report->num_fields, report->fields, &header,
                           report->client_data );

    free_info_data( &header );
}

/*---------------------------------------------------------------------------*
 * Get the next feature in the part
 *
 * Returns:
 *     TRUE if the next tolerance feature was found; otherwise, FALSE.
 *---------------------------------------------------------------------------*/
static logical ask_next_tolerance_feature(
    tag_t   part,   /* <I> Part being cycled for tolerance features        */
    tag_p_t feature /* <I> Previous tolerance feature or NULL_TAG to begin */
                    /* <O> Next tolerance feature or NULL_TAG if no more   */
)
{
    logical found = FALSE;

    while ( !found )
    {
        int status;
        int type, subtype;

        status = UF_OBJ_cycle_objs_in_part( part, UF_tolerance_feature_type,
                                            feature );
        ERROR_CHECK( status, ( "UF_OBJ_cycle_objs_in_part", status,
                               "part = %u, feature = %u", part, *feature ) );

        if ( *feature == NULL_TAG )
            break;

        status = UF_OBJ_ask_type_and_subtype( *feature, &type, &subtype );
        ERROR_CHECK( status, ( "UF_OBJ_ask_type_and_subtype", status,
                               "feature = %u", feature ) );

        if ( subtype == UF_tolerance_feature_subtype ||
             subtype == UF_complex_tolerance_feature_subtype ||
             subtype == UF_complex_tolerance_subfeature_subtype )
            found = TRUE;
    }

    return ( found );
}

/*---------------------------------------------------------------------------*
 * Function to display requested data on all tolerances, datums and datum
 * targets in the part specified.
 *
 * Returns:
 *     UF_GDT_NO_ERROR
 *     UFD_GDT__ERR_NO_PART
 *---------------------------------------------------------------------------*/
static void show_part_report(
    tag_t part,                 /* <I> Part to query          */
    UFD_GDT__report_p_t report  /* <I> Part report definition */
)
{
    tag_t feature = NULL_TAG;

    DEBUG_ASSERT( report->output_fun != NULL );

    UFD_GDT__set_report( report );

    while ( ask_next_tolerance_feature( part, &feature ) )
        process_feature( report, part, feature );

    output_header( part, report );

    if ( report->part_info.count > 0 )
    {
        int num;

        qsort( report->part_info.lines, report->part_info.count,
               sizeof( UFD_GDT__object_info_t ), compare_rows );

        for ( num = 0; num < report->part_info.count; num++ )
        {
            (*report->output_fun)( report->num_fields, report->fields,
                                   &report->part_info.lines[num],
                                   report->client_data );
        }
    }

    UFD_GDT__set_report( NULL );
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of report
 * fields.  Compares fields based on their title.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if field1 title < field2 title
 *     UFD_GDT__EQUAL        if field1 title = field2 title
 *     UFD_GDT__GREATER_THAN if field1 title > field2 title
 *---------------------------------------------------------------------------*/
static int compare_report_fields_by_title(
    const void *ptr1,           /* <I> Report field 1 to compare */
    const void *ptr2            /* <I> Report field 2 to compare */
)
{
    UFD_GDT__report_field_p_t field1 = (UFD_GDT__report_field_p_t) ptr1;
    UFD_GDT__report_field_p_t field2 = (UFD_GDT__report_field_p_t) ptr2;

    if ( field1->title == NULL && field2->title == NULL )
        return ( UFD_GDT__EQUAL );

    else if ( field1->title == NULL )
        return ( UFD_GDT__LESS_THAN );

    else if ( field2->title == NULL )
        return ( UFD_GDT__GREATER_THAN );

    else
        return ( strcmp( field1->title, field2->title ) );
}

/*---------------------------------------------------------------------------*
 * Comparison callback function for qsort and bsearch for a list of report
 * fields.  Compares fields based on their type.
 *
 * Returns:
 *     UFD_GDT__LESS_THAN    if field1 type < field2 type
 *     UFD_GDT__EQUAL        if field1 type = field2 type
 *     UFD_GDT__GREATER_THAN if field1 type > field2 type
 *---------------------------------------------------------------------------*/
static int compare_report_fields_by_type(
    const void *ptr1,           /* <I> Report field 1 to compare */
    const void *ptr2            /* <I> Report field 2 to compare */
)
{
    UFD_GDT__report_field_p_t field1 = (UFD_GDT__report_field_p_t) ptr1;
    UFD_GDT__report_field_p_t field2 = (UFD_GDT__report_field_p_t) ptr2;

    if ( field1->type < field2->type )
        return ( UFD_GDT__LESS_THAN );

    else if ( field1->type > field2->type )
        return ( UFD_GDT__GREATER_THAN );

    else
        return ( UFD_GDT__EQUAL );
}

/*---------------------------------------------------------------------------*
 * Get the definitions (i.e. title and comparison functions) for all possible
 * report fields.
 *---------------------------------------------------------------------------*/
static void ask_report_field_defs(
    logical sorted_by_type,               /* <I> TRUE  - sorted by info type */
                                          /*     FALSE - sorted by title     */
    int *num_field_defs,                  /* <O> Number of fields in list    */
    UFD_GDT__report_field_p_t *field_defs /* <O> List of all possible fields */
)
{
    static UFD_GDT__report_field_t field_definitions[] =
    { { UFD_GDT__TOLERANCE_NUMBER_INFO,             "Tolerance Number",      compare_info_data_with_number, 0 },
      { UFD_GDT__PART_NAME_INFO,                    "Part Name",             compare_info_data_with_number, 0 },
      { UFD_GDT__TOLERANCE_FEATURE_NAME_INFO,       "Feature Name",          compare_info_data_with_number, 0 },
      { UFD_GDT__RETAINED_STATUS_INFO,              "Retained",              compare_info_data,             0 },
      { UFD_GDT__DESCRIPTION_INFO,                  "Description",           compare_info_data,             0 },
      { UFD_GDT__FACES_INFO,                        "Faces",                 compare_info_data_with_number, 0 },
      { UFD_GDT__GEOMETRIC_DEFINITION_TYPE_INFO,    "Geometric Definition",  compare_info_data,             0 },
      { UFD_GDT__TOLERANCE_TYPE_INFO,               "Tolerance Type",        compare_info_data,             0 },
      { UFD_GDT__GEOMETRY_TYPE_INFO,                "Geometry",              compare_info_data,             0 },
      { UFD_GDT__PATTERN_TYPE_INFO,                 "Pattern",               compare_info_data,             0 },
      { UFD_GDT__DISPLAY_INSTANCE_VIEWS_INFO,       "Views",                 compare_info_data_with_number, 0 },
      { UFD_GDT__PULLED_FROM_INFO,                  "Pulled From",           compare_info_data_with_number, 0 },
      { UFD_GDT__PARENT_TOLERANCE_FEATURE_INFO,     "Parent Feature",        compare_info_data_with_number, 0 },
      { UFD_GDT__CHILD_TOLERANCE_FEATURES_INFO,     "Child Features",        compare_info_data_with_number, 0 },
      { UFD_GDT__LINKED_TOLERANCE_FEATURES_INFO,    "Linked Features",       compare_info_data_with_number, 0 },
      { UFD_GDT__PULLED_FROM_TOLERANCE_NUMBER_INFO, "Pulled From Tolerance", compare_info_data_with_number, 0 },
      { UFD_GDT__CALLOUT_STRING_INFO,               "Callout",               compare_info_data,             0 },
      { UFD_GDT__ENTIRE_CALLOUT_STRING_INFO,        "Entire Callout",        compare_info_data,             0 },
      { UFD_GDT__TOLERANCE_BAND_INFO,               "Tolerance Band",        compare_info_data,             0 },
      { UFD_GDT__STANDARD_KEYWORDS_INFO,            "Standard Keywords",     compare_info_data,             0 },
      { UFD_GDT__USER_DEFINED_KEYWORDS_INFO,        "User Keywords",         compare_info_data,             0 },
      { UFD_GDT__ABOVE_APPENDED_TEXT_INFO,          "Above App Text",        compare_info_data,             0 },
      { UFD_GDT__BELOW_APPENDED_TEXT_INFO,          "Below App Text",        compare_info_data,             0 },
      { UFD_GDT__BEFORE_APPENDED_TEXT_INFO,         "Before App Text",       compare_info_data,             0 },
      { UFD_GDT__AFTER_APPENDED_TEXT_INFO,          "After App Text",        compare_info_data,             0 },
      { UFD_GDT__PRIMARY_DATUM_INFO,                "Primary Datum",         compare_info_data,             0 },
      { UFD_GDT__SECONDARY_DATUM_INFO,              "Secondary Datum",       compare_info_data,             0 },
      { UFD_GDT__TERTIARY_DATUM_INFO,               "Tertiary Datum",        compare_info_data,             0 },
      { UFD_GDT__RELATED_FACES_INFO,                "Related Faces",         compare_info_data_with_number, 0 },
      { UFD_GDT__NOMINAL_SIZE_INFO,                 "Nominal Size",          compare_info_data,             0 },
      { UFD_GDT__DISPLAYED_LOWER_LIMIT_INFO,        "Displayed Lower Limit", compare_info_data,             0 },          
      { UFD_GDT__DISPLAYED_UPPER_LIMIT_INFO,        "Displayed Upper Limit", compare_info_data,             0 }         
    };
    static UFD_GDT__report_field_t field_defs_by_title[NUM_ELEMENTS( field_definitions )];
    static int num_field_definitions = NUM_ELEMENTS( field_definitions );
    static logical initialized = FALSE;

    if ( !initialized )
    {
        int num;

        DEBUG_ASSERT( num_field_definitions == UFD_GDT__NUM_INFO_TYPES );

        for ( num = 0; num < num_field_definitions; num++ )
            field_definitions[num].max_len = strlen( field_definitions[num].title );

        qsort( field_definitions, num_field_definitions,
               sizeof( UFD_GDT__report_field_t ),
               compare_report_fields_by_type );

        memcpy( field_defs_by_title, field_definitions,
                num_field_definitions * sizeof( UFD_GDT__report_field_t ) );

        qsort( field_defs_by_title, num_field_definitions,
               sizeof( UFD_GDT__report_field_t ),
               compare_report_fields_by_title );

        initialized = TRUE;
    }

    if ( sorted_by_type )
        *field_defs = field_definitions;
    else
        *field_defs = field_defs_by_title;

    *num_field_defs = num_field_definitions;
}

/*---------------------------------------------------------------------------*
 * Search for the report field definition that corresponds to the input
 * field title.
 *
 * Returns:
 *     Report field definition corresponding to the input field title
 *---------------------------------------------------------------------------*/
static UFD_GDT__report_field_p_t ask_field_def_from_title(
    char *title                 /* <I> Title of field to search for */
)
{
    int num_field_defs;
    UFD_GDT__report_field_t search_field;
    UFD_GDT__report_field_p_t field_defs;

    search_field.type    = UFD_GDT__NUM_INFO_TYPES;
    search_field.title   = title;
    search_field.compare = NULL;
    search_field.max_len = 0;

    ask_report_field_defs( FALSE, &num_field_defs, &field_defs );

    return (struct UFD_GDT__report_field_s *)( bsearch( &search_field, field_defs, num_field_defs,
                      sizeof( UFD_GDT__report_field_t ),
                      compare_report_fields_by_title ) );
}

/*---------------------------------------------------------------------------*
 * Search for the report field definition that corresponds to the input
 * information type.
 *
 * Returns:
 *     Report field definition corresponding to the input information type
 *---------------------------------------------------------------------------*/
static UFD_GDT__report_field_p_t ask_field_def_from_type(
    UFD_GDT__info_type_t type    /* <I> Type of field to search for */
)
{
    int num_field_defs;
    UFD_GDT__report_field_t search_field;
    UFD_GDT__report_field_p_t field_defs;

    search_field.type    = type;
    search_field.title   = NULL;
    search_field.compare = NULL;
    search_field.max_len = 0;

    ask_report_field_defs( TRUE, &num_field_defs, &field_defs );

    return (struct UFD_GDT__report_field_s *)( bsearch( &search_field, field_defs, num_field_defs,
                      sizeof( UFD_GDT__report_field_t ),
                      compare_report_fields_by_type ) );
}

/*---------------------------------------------------------------------------*
 * Get the default report fields
 *---------------------------------------------------------------------------*/
static void ask_default_report_fields(
    int *num_fields,                 /* <O>  Number of default report fields  */
    UFD_GDT__report_field_p_t *fields/* <OF> Allocated list of default report */
                                     /*      fields                           */
)
{
    UFD_GDT__info_type_t default_columns[] = 
    { UFD_GDT__TOLERANCE_NUMBER_INFO,
      UFD_GDT__PART_NAME_INFO,
      UFD_GDT__PULLED_FROM_INFO,
      UFD_GDT__PULLED_FROM_TOLERANCE_NUMBER_INFO,
      UFD_GDT__RETAINED_STATUS_INFO,
      UFD_GDT__GEOMETRY_TYPE_INFO,
      UFD_GDT__TOLERANCE_TYPE_INFO,
      UFD_GDT__PATTERN_TYPE_INFO,
      UFD_GDT__NOMINAL_SIZE_INFO,
      UFD_GDT__TOLERANCE_BAND_INFO,
      UFD_GDT__PRIMARY_DATUM_INFO,
      UFD_GDT__SECONDARY_DATUM_INFO,
      UFD_GDT__TERTIARY_DATUM_INFO,
      UFD_GDT__STANDARD_KEYWORDS_INFO,
      UFD_GDT__USER_DEFINED_KEYWORDS_INFO,
      UFD_GDT__CALLOUT_STRING_INFO,
      UFD_GDT__ENTIRE_CALLOUT_STRING_INFO,
      UFD_GDT__TOLERANCE_FEATURE_NAME_INFO,
      UFD_GDT__DESCRIPTION_INFO,
      UFD_GDT__FACES_INFO,
      UFD_GDT__GEOMETRIC_DEFINITION_TYPE_INFO,
      UFD_GDT__DISPLAY_INSTANCE_VIEWS_INFO,
      UFD_GDT__PARENT_TOLERANCE_FEATURE_INFO,
      UFD_GDT__CHILD_TOLERANCE_FEATURES_INFO,
      UFD_GDT__LINKED_TOLERANCE_FEATURES_INFO,
      UFD_GDT__ABOVE_APPENDED_TEXT_INFO,
      UFD_GDT__BELOW_APPENDED_TEXT_INFO,
      UFD_GDT__BEFORE_APPENDED_TEXT_INFO,
      UFD_GDT__AFTER_APPENDED_TEXT_INFO,
      UFD_GDT__RELATED_FACES_INFO,
      UFD_GDT__DISPLAYED_LOWER_LIMIT_INFO,
      UFD_GDT__DISPLAYED_UPPER_LIMIT_INFO
    };

    int alloc = 0;
    int num;

    *fields = NULL;
    *num_fields = 0;

    for ( num = 0; num < NUM_ELEMENTS( default_columns ); num++ )
    {
        UFD_GDT__report_field_p_t field_def;

        field_def = ask_field_def_from_type( default_columns[num] );

        *fields = (UFD_GDT__report_field_p_t)realloc_list( sizeof( UFD_GDT__report_field_t ),
                                10, &alloc, *num_fields, *fields );

        (*fields)[*num_fields].type    = field_def->type;
        (*fields)[*num_fields].title   = copy_string( field_def->title );
        (*fields)[*num_fields].compare = field_def->compare;
        (*fields)[*num_fields].max_len = field_def->max_len;
        (*num_fields)++;
    }
}

/*---------------------------------------------------------------------------*
 * Read the report fields from a file
 *---------------------------------------------------------------------------*/
static void ask_report_fields_from_file(
    int  channel,                     /* <I>  I/O channel for file to read    */
    int *num_fields,                  /* <O>  Number of report fields         */
    UFD_GDT__report_field_p_t *fields /* <OF> Allocated list of report fields */
)
{
    char line[ MAX_LINE_BUFSIZE ];
    int alloc = 0;

    while ( uc4514( channel, line ) >= 0 )
    {
        char *title;
        UFD_GDT__report_field_p_t field;

        title = ask_string_no_extra_spaces( line );
        field = ask_field_def_from_title( title );

        if ( field != NULL )
        {
            *fields = (UFD_GDT__report_field_p_t)realloc_list( sizeof( UFD_GDT__report_field_t ), 10,
                                    &alloc, *num_fields, *fields );

            (*fields)[*num_fields].type    = field->type;
            (*fields)[*num_fields].title   = title;
            (*fields)[*num_fields].compare = field->compare;
            (*fields)[*num_fields].max_len = field->max_len;
            (*num_fields)++;
        }
        else
        {
            print_error( "Reading report settings", UF_GDT_NO_ERRORS,
                         "%s info type does not exist!", title );
            UF_free( title );
        }
    }
}

/*---------------------------------------------------------------------------*
 * Get the report fields from UFD_GDT__REPORT_SETTINGS_FILE or the default
 * report fields if the environment variable does not exist or there is a
 * problem opening the file.
 *---------------------------------------------------------------------------*/
static void ask_report_fields(
    int *num_fields,                  /* <O>  Number of report fields */
    UFD_GDT__report_field_p_t *fields /* <OF> List of report fields   */
)
{
    char *settings_file_envar = "UFD_GDT_REPORT_SETTINGS_FILE";
    char *settings_file;
    int exists = 1;

    UF_translate_variable( settings_file_envar, &settings_file );

    *fields = NULL;
    *num_fields = 0;

    if ( settings_file != NULL )
    {
        int status;

        status = UF_CFI_ask_file_exist( settings_file, &exists );
        ERROR_CHECK( status, ( "UF_CFI_ask_file_exist", status, "%s = %s",
                               settings_file_envar, settings_file ) );
    }

    if ( exists != 0 )
    {
        print_error( "Report setup", UF_GDT_NO_ERRORS,
                     "%s = %s does not exist!\n  Using default report columns",
                     settings_file_envar, settings_file );

        ask_default_report_fields( num_fields, fields );
    }
    else
    {
        int read_mode = 1, file_type = 3;
        int channel;

        channel = uc4504( settings_file, read_mode, file_type );

        if ( channel < 0 )
        {
            print_error( settings_file_envar, channel,
                         "Using default report columns" );
            ask_default_report_fields( num_fields, fields );
        }
        else
        {
            int disposition = 0; /* Normal close */

            ask_report_fields_from_file( channel, num_fields, fields );
            uc4540( channel, disposition );
        }
    }
}

/*---------------------------------------------------------------------------*
 * Initialize the report structure
 *---------------------------------------------------------------------------*/
static void init_report(
    UFD_GDT__report_p_t report   /* <O> Report structure to clear */
)
{
    report->num_fields      = 0;
    report->fields          = NULL;
    report->output_fun      = NULL;
    report->client_data     = NULL;
    report->part_info.alloc = 0;
    report->part_info.count = 0;
    report->part_info.lines = 0;
}

/*---------------------------------------------------------------------------*
 * Free the report fields and output data
 *---------------------------------------------------------------------------*/
static void close_report(
    UFD_GDT__report_p_t report   /* <I/O> Report structure to free & close */
)
{
    int num;

    for ( num = 0; num < report->num_fields; num++ )
        UF_free( report->fields[num].title );

    UF_free( report->fields );

    if ( report->output_fun == print_output_line )
    {
        UFD_GDT__output_list_p_t output_data;

        output_data = (UFD_GDT__output_list_p_t) report->client_data;

        if ( output_data != NULL )
        {
            for ( num = 0; num < output_data->count; num++ )
            {
                UF_free( output_data->list[num].delimiter );

                if ( output_data->list[num].type == UFD_GDT__FILE_OUTPUT )
                    fclose( output_data->list[num].file );
            }

            UF_free( output_data->list );
            UF_free( output_data );
        }
    }

    for ( num = 0; num < report->part_info.count; num++ )
        free_info_data( &report->part_info.lines[num] );

    UF_free( report->part_info.lines );

    init_report( report );
}

/*---------------------------------------------------------------------------*
 * Initialize the report fields and output data
 *
 * Returns:
 *     UF_GDT_NO_ERRORS
 *     UFD_GDT__ERR_NO_REPORT_OUTPUT_DATA
 *     Error from UF_allocate_memory
 *---------------------------------------------------------------------------*/
static int open_report(
    UFD_GDT__report_p_t report   /* <I/O> Report structure to initialize */
)
{
    char *report_file_envar = "UFD_GDT_REPORT_FILE";
    char *report_infowin_envar = "UFD_GDT_REPORT_INFOWIN";
    char *report_file;
    char *report_infowin;
    int status;
    int alloc = 0;
    UFD_GDT__output_list_p_t output_data = NULL;

    init_report( report );

    UF_translate_variable( report_file_envar, &report_file );
    UF_translate_variable( report_infowin_envar, &report_infowin );

    output_data = (UFD_GDT__output_list_p_t)UF_allocate_memory( sizeof( UFD_GDT__output_data_t ), &status );
    ERROR_CHECK( status, ( "UF_allocate_memory", status, "" ) );

    output_data->count = 0;
    output_data->list  = NULL;

    if ( report_file != NULL )
    {
        FILE *file = fopen( report_file, "w+" );

        if ( file == NULL )
        {
            print_error( "Report setup", UF_GDT_NO_ERRORS,
                         "Error opening %s = %s", report_file_envar, report_file );
        }
        else
        {
            output_data->list = (UFD_GDT__output_data_p_t)realloc_list( sizeof( UFD_GDT__output_data_t ),
                                              1, &alloc, output_data->count,
                                              output_data->list );
            output_data->list[output_data->count].type = UFD_GDT__FILE_OUTPUT;
            output_data->list[output_data->count].file = file;
            output_data->list[output_data->count].delimiter = copy_string( "\t" );
            output_data->count++;
        }
    }

    if ( report_infowin != NULL )
    {
        status = UF_UI_open_listing_window();

        if ( status != UF_GDT_NO_ERRORS )
        {
            print_error( "Report setup", status,
                         "Error opening listing window" );
        }
        else
        {
            output_data->list = (UFD_GDT__output_data_p_t)realloc_list( sizeof( UFD_GDT__output_data_t ),
                                              1, &alloc, output_data->count,
                                              output_data->list );
            output_data->list[output_data->count].type = UFD_GDT__INFO_WINDOW_OUTPUT;
            output_data->list[output_data->count].file = NULL;
            output_data->list[output_data->count].delimiter = NULL;
            output_data->count++;
        }
    }

    report->output_fun  = print_output_line;
    report->client_data = (void *) output_data;

    if ( output_data->count > 0 )
        ask_report_fields( &report->num_fields, &report->fields );
    else
    {
        print_error( "Report setup", UFD_GDT__ERR_NO_REPORT_OUTPUT_DATA,
                     "Aborting report" );
        close_report( report );

        return ( UFD_GDT__ERR_NO_REPORT_OUTPUT_DATA );
    }

    return ( UF_GDT_NO_ERRORS );
}

/*---------------------------------------------------------------------------*
 * Run the GDT report on the part file specified
 *---------------------------------------------------------------------------*/
static int show_report(
    tag_t part                  /* <I> Part to run report on */
)
{
    int error_code = UF_GDT_NO_ERRORS;
    UFD_GDT__report_t report;

    if ( part == NULL_TAG )
    {
        print_error( "Report setup", UFD_GDT__ERR_NO_PART, "" );
        return ( UFD_GDT__ERR_NO_PART );
    }

    error_code = open_report( &report );

    if ( error_code == UF_GDT_NO_ERRORS )
    {
        show_part_report( part, &report );
        close_report( &report );
    }

    return ( error_code );
}

#ifdef INTERNAL_UFUN
/*---------------------------------------------------------------------------*
 * Internal user function that runs the GDT report on the current part file.
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
extern void ufusr(
    char *param,
    int  *retcod,
    int   param_len
)
{
    int status;

    status = UF_initialize();
    if ( status != 0 )
    {
        print_error( "UF_initialize", status, "Aborting report" );
        return;
    }

    show_report( UF_PART_ask_display_part() );

    status = UF_terminate();
    if ( status != 0 )
        print_error( "UF_terminate", status, "" );
}
#else  /* !defined(INTERNAL_UFUN) */
/*---------------------------------------------------------------------------*
 * External user function that runs the GDT report on a specified part file.
 *
 * Call Syntax:
 *     external_ufun_program <part file>
 *
 * Input Arguments:
 *     <part file> - Part file to perform report on
 *---------------------------------------------------------------------------*/
extern int main(
    int    argc,                /* <I> Number of input arguments */
    char **argv                 /* <I> List of input arguments   */
)
{
    int status, term_status;
    tag_t part;
    UF_PART_load_status_t error_status;

    status = UF_initialize();
    if ( status != UF_GDT_NO_ERRORS )
    {
        print_error( "UF_initialize", status, "Aborting report" );
        return ( status );
    }

    if ( argc < 2 )
        print_error( argv[0], UFD_GDT__ERR_NO_PART, "Aborting report" );
    else
    {
        char *part_name = argv[1];

        status = UF_PART_open( part_name, &part, &error_status );

        if ( status == UF_GDT_NO_ERRORS || !error_status.failed )
        {
            if ( error_status.n_parts > 0 )
            {
                UF_free_string_array( error_status.n_parts,
                                      error_status.file_names );
                UF_free( error_status.statuses );
            }

            show_report( part );
        }
        else
        {
            int num;

            for ( num = 0; num < error_status.n_parts; num++ )
                print_error( "Open part", error_status.statuses[num],
                             "%s", error_status.file_names[num] );

            UF_free_string_array( error_status.n_parts,
                                  error_status.file_names );
            UF_free( error_status.statuses );
        }
    }

    term_status = UF_terminate();

    if ( term_status != UF_GDT_NO_ERRORS )
    {
        print_error( "UF_terminate", term_status, "" );
        if ( status == UF_GDT_NO_ERRORS )
            status = term_status;
    }

    return ( status );
}
#endif  /* INTERNAL_UFUN */
