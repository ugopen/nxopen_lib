/*==============================================================================

             Copyright (c) 1999,2002,2003,2004 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved
================================================================================
File description:

    This file contains both an internal and external User Function program
    that outputs a part's Product Definition data to a tab delimited
    file and/or the information window.  Each row of data output contains
    information on one of the following:
        Business Modifier
        Product Definition
        Product Definition Geometry
        Product Definition Attributes
        Product Definition Instance
        Product Definition Status

Customization:

    Use the UFD_SMSP_REPORT_SETTINGS_FILE environment variable to point to a
    file that defines the list of data to output in the order that it will be
    shown.  This file will contain the title of a column of data to output
    per line.  Only the column titles appearing in the file will be shown.
    Thus, to omit a column simply omit its title from the file.  Note that
    the columns will appear in the order that they are specified in the file.

    The following are valid data column titles:

        Part Name
        Definition Title
        Status
        Scope
        Geometry
        Applications
        Displayed In Views
        Attribute Title     
        Attribute Group     
        Attribute Type      
        Attribute DFA File  
        Business Modifier
        Attribute Item

    Note: 1. If Business Modifier is defined, Modifier Title and Modifier Value
             will be lised in the report;
          2. If Attribute Item is defined, Item Title and Item Value will be 
             listed in the report.
          3. Modifier Title is the title defined in the part for each Business
             Modifier. 

    See the ufd_smsp_report_settings.dat file for an example.

    Use the UFD_SMSP_REPORT_FILE environment variable to point to the tab
    delimited file to output the data to.  Note that this file will be
    overwritten if it already exists.

    Define the UFD_SMSP_REPORT_INFOWIN environment variable to indicate that
    data should be output to the information window.

Build comments:

    To compile the internal User Function program the INTERNAL_UFUN #define
    must be defined.  To compile the external User Function program the
    INTERNAL_UFUN #define must not be defined.


==============================================================================*/

#include <uf_defs.h>
#include <ctype.h>
#include <math.h>
#include <stdarg.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <uf.h>
#include <uf_assem.h>
#include <uf_cfi.h>
#include <uf_gdt.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_pd_types.h>
#include <uf_pd.h>
#include <uf_ui.h>
#include <uf_view.h>

#define INTERNAL_UFUN
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
    { if ( status != UF_SMSP_NO_ERROR ) DUMP_ERROR( args ); }

/*---------------------------------------------------------------------------*
 * Macro used to obtain the number of elements in a static array
 *---------------------------------------------------------------------------*/
#define NUM_ELEMENTS( array ) ( sizeof( array ) / sizeof( array[0] ) )

/*---------------------------------------------------------------------------*
 * Possible UFD_SMSP error codes
 *---------------------------------------------------------------------------*/
#define UFD_SMSP__ERR_NO_PART                (101)
#define UFD_SMSP__ERR_NO_REPORT_OUTPUT_DATA  (102)
#define UFD_SMSP__ERR_NO_OUTPUT_FILE         (103)
#define UFD_SMSP__ERR_NO_OUTPUT_WINDOW       (104)
#define UFD_SMSP__TEMP_BUSMOD_TITLE          ("Temp Business Modifier")

/*---------------------------------------------------------------------------*
 * Possible information types to show in report
 *---------------------------------------------------------------------------*/
typedef enum
{
    UFD_SMSP__NULL_TYPE,
    UFD_SMSP__PART_NAME,
    UFD_SMSP__DEFINITION_TITLE,
    UFD_SMSP__DEFINITION_STATUS,
    UFD_SMSP__DEFINITION_SCOPE,
    UFD_SMSP__DEFINITION_GEOMETRY,
    UFD_SMSP__DEFINITION_APPLICATION,
    UFD_SMSP__DEFINITION_DISPLAY,
    UFD_SMSP__ATTRIBUTE_TITLE,
    UFD_SMSP__ATTRIBUTE_GROUP,
    UFD_SMSP__ATTRIBUTE_TYPE,
    UFD_SMSP__ATTRIBUTE_DFA_FILE,
    UFD_SMSP__BUSINESS_MODIFIER,
    UFD_SMSP__BUSMOD_TITLE,
    UFD_SMSP__BUSMOD_VALUE,
    UFD_SMSP__ATTRIBUTE_ITEM,
    UFD_SMSP__ITEM_TITLE,
    UFD_SMSP__ITEM_VALUE,

    /* GD&T information */
    UFD_SMSP__GDT_GROUP_INFO,                           /* GD&T does not have the type */

    UFD_SMSP__TOL_FEAT_APPLICATION,
    UFD_SMSP__TOLERANCE_NUMBER_INFO,
    UFD_SMSP__PART_NAME_INFO,                      
    UFD_SMSP__TOLERANCE_FEATURE_NAME_INFO,         
    UFD_SMSP__RETAINED_STATUS_INFO,                
    UFD_SMSP__DESCRIPTION_INFO,                    
    UFD_SMSP__FACES_INFO,                          
    UFD_SMSP__GEOMETRIC_DEFINITION_TYPE_INFO,      
    UFD_SMSP__TOLERANCE_TYPE_INFO,                 
    UFD_SMSP__GEOMETRY_TYPE_INFO,                  
    UFD_SMSP__PATTERN_TYPE_INFO,
    UFD_SMSP__DISPLAY_INSTANCE_VIEWS_INFO,         
    UFD_SMSP__PULLED_FROM_INFO,
    UFD_SMSP__PARENT_TOLERANCE_FEATURE_INFO,
    UFD_SMSP__CHILD_TOLERANCE_FEATURES_INFO,
    UFD_SMSP__LINKED_TOLERANCE_FEATURES_INFO,      
    UFD_SMSP__PULLED_FROM_TOLERANCE_NUMBER_INFO,   
    UFD_SMSP__CALLOUT_STRING_INFO,
    UFD_SMSP__ENTIRE_CALLOUT_STRING_INFO,
    UFD_SMSP__TOLERANCE_BAND_INFO,
    UFD_SMSP__STANDARD_KEYWORDS_INFO,
    UFD_SMSP__USER_DEFINED_KEYWORDS_INFO,
    UFD_SMSP__ABOVE_APPENDED_TEXT_INFO,
    UFD_SMSP__BELOW_APPENDED_TEXT_INFO,
    UFD_SMSP__BEFORE_APPENDED_TEXT_INFO,
    UFD_SMSP__AFTER_APPENDED_TEXT_INFO,
    UFD_SMSP__PRIMARY_DATUM_INFO,
    UFD_SMSP__SECONDARY_DATUM_INFO,
    UFD_SMSP__TERTIARY_DATUM_INFO,
    UFD_SMSP__RELATED_FACES_INFO,
    UFD_SMSP__NOMINAL_SIZE_INFO,
    UFD_SMSP__NUM_INFO_TYPES
} UFD_SMSP__info_type_t, *UFD_SMSP__info_type_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to define types of report output available
 *---------------------------------------------------------------------------*/
#define UFD_SMSP__NO_OUTPUT                         (0)
#define UFD_SMSP__FILE_OUTPUT                       (1<<0)
#define UFD_SMSP__INFO_WINDOW_OUTPUT                (1<<1)
#define UFD_SMSP__output_type_t                     unsigned int

/*---------------------------------------------------------------------------*
 * Structure used to contain data on where to output the report
 *---------------------------------------------------------------------------*/
typedef struct UFD_SMSP__output_format_s
{
    UFD_SMSP__output_type_t type; /* Type of output                        */
    FILE *file;                   /* File name to be output                */
} UFD_SMSP__output_format_t, *UFD_SMSP__output_format_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to contain a single column of data contained in a report row
 *---------------------------------------------------------------------------*/
typedef struct UFD_SMSP__info_data_s
{
    UFD_SMSP__info_type_t type; /* Type of information in data string        */
    char *str;                  /* Information data string of the given type */
} UFD_SMSP__info_data_t, *UFD_SMSP__info_data_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to determine output data type defined 
 * in UFD_SMSP_REPORT_SETTINGS_FILE
 *---------------------------------------------------------------------------*/
typedef struct UFD_SMSP__info_list_s
{
    int num_types;                          /* Number of info types to be output  */
    UFD_SMSP__info_type_t *types;           /* Type of information in data string */
} UFD_SMSP__info_list_t, *UFD_SMSP__info_list_p_t;

/*---------------------------------------------------------------------------*
 * Callback function used to add type to report 
 *
 * Returns:
 *     error code
 *---------------------------------------------------------------------------*/
typedef int (*UFD_SMSP__add_type_f_t)
(
    UFD_SMSP__info_type_t type,
    void * report
);

/*---------------------------------------------------------------------------*
 * Callback function used to ask data to report 
 *
 * Returns:
 *     error code
 *---------------------------------------------------------------------------*/
typedef int (*UFD_SMSP__fill_data_f_t)
(
    UFD_SMSP__info_type_t type,
    void * data,
    logical is_gdt,
    int smrt, 
    int attr
);

/*---------------------------------------------------------------------------*
 * Structure defining a single data field in the report
 *---------------------------------------------------------------------------*/
typedef struct UFD_SMSP__report_form_s
{
    UFD_SMSP__info_type_t type;
    char                 *title;      /* Title of the field             */
    UFD_SMSP__add_type_f_t add_type;  /* callback function to add this  */ 
                                      /* type to report form            */
    UFD_SMSP__fill_data_f_t fill_data;
} UFD_SMSP__report_form_t, *UFD_SMSP__report_form_p_t;

/*---------------------------------------------------------------------------*
 * Structure defining a single data field in the report
 *---------------------------------------------------------------------------*/
typedef struct UFD_SMSP__report_field_s
{
    char                 *title;      /* Title of the field             */
    UFD_SMSP__info_data_t data;       /* Data/String of the field       */
    int column;                       /* Position of field              */
} UFD_SMSP__report_field_t, *UFD_SMSP__report_field_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to contain a single column of data contained in a report row
 *---------------------------------------------------------------------------*/
typedef struct UFD_SMSP__output_field_s
{
    int num_fields;                         /* total field in the report    */
    int current_col;                        /* current field column filled  */
    UFD_SMSP__report_field_p_t fields;      /* report field data            */
} UFD_SMSP__output_field_t, *UFD_SMSP__output_field_p_t;

typedef struct UFD_SMSP__GDT_mapped_type_s
{
    UFD_SMSP__info_type_t GDT_type;
    UFD_SMSP__info_type_t type;
} UFD_SMSP__GDT_mapped_type_t;

typedef struct UFD_SMSP__GDT_fields_only_s
{
    UFD_SMSP__info_type_t GDT_type;
} UFD_SMSP__GDT_fields_only_t;

/*---------------------------------------------------------------------------*
 * Structure defining a single data field in the report
 *---------------------------------------------------------------------------*/
typedef struct UFD_SMSP__GDT_report_field_s
{
    UFD_SMSP__info_type_t type;   /* Type of info contained in the field      */
} UFD_SMSP__GDT_report_field_t, *UFD_SMSP__GDT_report_field_p_t;


/*-------------------------------------------------------------------------*
 * Structure defining a tolerance feature attribute data.
 *-------------------------------------------------------------------------*/
typedef struct UFD_SMSP__GDT_tol_feat_attr_data_s
{
    /* Product attribute data */  
    UF_PD_product_attribute_t product_att_data;

    /* Business Modifier data used by tolerance attribute. */
    int num_busmods;
    UF_PD_business_modifier_p_t busmods;

}  UFD_SMSP__GDT_tol_feat_attr_data_t, * UFD_SMSP__GDT_tol_feat_attr_data_p_t;


/*-------------------------------------------------------------------------*
 * Structure defining a tolerance feature data
 *-------------------------------------------------------------------------*/
typedef struct UFD_SMSP__GDT_tol_feat_data_s
{

    /* GDT tol feature attributes -
     * 1. Product Attributes
     * 2. Tolerances
     */
    int num_attributes;
    tag_p_t attributes;
    UFD_SMSP__GDT_tol_feat_attr_data_p_t tol_feat_attr_data;

}  UFD_SMSP__GDT_tol_feat_data_t, * UFD_SMSP__GDT_tol_feat_data_p_t;


/*-------------------------------------------------------------------------*
 * Structure defining a part that contains product definition data
 *-------------------------------------------------------------------------*/
typedef struct UFD_SMSP__part_s
{
    tag_t tag;
    char *name;
    int num_definitions;
    int max_values;    /* max number of values in attributes                   */

    int max_busmod;       /* max number of business modifier in attributes        */    
    char **busmod_titles; /* array to hold business modifier title in the part */

    UF_PD_product_definition_p_t *definitions; /* array of definition data pointers */
    tag_t * definition_tags;                   /* array of definition tag pointers */

    /* GD&T info */
    int num_GDT_fields;
    UFD_SMSP__GDT_report_field_p_t GDT_fields;
    int num_GDT_fields_only;

    UFD_SMSP__GDT_tol_feat_data_p_t tol_feat_data; 
    tag_p_t tol_feat_tags;
    int num_tol_feats;

}  UFD_SMSP__part_t, * UFD_SMSP__part_p_t;

/*---------------------------------------------------------------------------*
 * Structure used to define a part report
 *---------------------------------------------------------------------------*/
typedef struct UFD_SMSP__report_s
{
    UFD_SMSP__output_format_t format;     /* Type to output                   */
    UFD_SMSP__info_list_t     list;       /* Info list need to be output      */
    UFD_SMSP__output_field_t  output;     /* Real data to be output           */
    UFD_SMSP__part_t          part;       /* Part info                        */
} UFD_SMSP__report_t, *UFD_SMSP__report_p_t;

/*---------------------------------------------------------------------------*
 * Prototypes of local callback functions
 * 
 * All function will return error code 
 *---------------------------------------------------------------------------*/
static int add_null(UFD_SMSP__info_type_t type, void *data);
static int add_type(UFD_SMSP__info_type_t type, void *data);
static int add_values   (UFD_SMSP__info_type_t type, void *data);
static int add_modifiers(UFD_SMSP__info_type_t type, void *data);

static int fill_part_name    (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_pd_title     (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_pd_status    (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_pd_scope     (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_pd_geometry  (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_pd_app       (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_pd_display   (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_att_title    (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_att_group    (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_att_type     (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_att_dfa      (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_bmod_data    (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_item_data    (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);
static int fill_null_data    (UFD_SMSP__info_type_t type, void * data, logical is_gdt, int smrt, int attr);

static int insert_to_field           (UFD_SMSP__report_p_t report, UFD_SMSP__info_type_t type, char * data);
static int insert_item_to_field      (UFD_SMSP__report_p_t report, UF_PD_attribute_value_p_t item, int index);
static int insert_item_data_to_field (UFD_SMSP__report_p_t report, UF_PD_attribute_value_data_p_t data, int index);
static int insert_busmod_to_field    (UFD_SMSP__report_p_t report, UF_PD_business_modifier_p_t busmod, int index);

/************  GD&T Function prototype ********************/
static int add_gdt_type(UFD_SMSP__info_type_t type, void *data);
static void fill_GDT_report(UFD_SMSP__report_p_t report);
static void close_GDT_report(UFD_SMSP__report_p_t report); 
static logical ask_next_tolerance_feature(tag_t part, tag_p_t feature);
static void process_feature(UFD_SMSP__report_p_t report, tag_t part, int tol_feat);
static void print_error(char *msg, int error_code, const char *format, ...);
static UF_GDT_size_tolerance_p_t convert_depth_data_to_size_data(
    UF_GDT_depth_tolerance_p_t depth_tol_data
);
static UF_GDT_size_tolerance_p_t convert_thread_data_to_size_data(
    UF_GDT_thread_tolerance_p_t thread_tol_data
);
/*---------------------------------------------------------------------------*
 * Structure to map a GDT type
 *---------------------------------------------------------------------------*/
static UFD_SMSP__GDT_mapped_type_t mapping_GDT_type_table [] =
{
    { UFD_SMSP__PART_NAME_INFO,                 UFD_SMSP__PART_NAME },
    { UFD_SMSP__TOLERANCE_FEATURE_NAME_INFO,    UFD_SMSP__DEFINITION_TITLE },
    { UFD_SMSP__RETAINED_STATUS_INFO,           UFD_SMSP__DEFINITION_STATUS },
    { UFD_SMSP__GEOMETRY_TYPE_INFO,             UFD_SMSP__DEFINITION_SCOPE },
    { UFD_SMSP__DISPLAY_INSTANCE_VIEWS_INFO,    UFD_SMSP__DEFINITION_DISPLAY },
    { UFD_SMSP__TOL_FEAT_APPLICATION,           UFD_SMSP__DEFINITION_APPLICATION },
    { UFD_SMSP__FACES_INFO,                     UFD_SMSP__DEFINITION_GEOMETRY },
    { UFD_SMSP__DESCRIPTION_INFO,               UFD_SMSP__ATTRIBUTE_TITLE },
    { UFD_SMSP__TOLERANCE_TYPE_INFO,            UFD_SMSP__ATTRIBUTE_TYPE },
    { UFD_SMSP__GDT_GROUP_INFO,                 UFD_SMSP__ATTRIBUTE_GROUP },
    { UFD_SMSP__ATTRIBUTE_DFA_FILE,             UFD_SMSP__ATTRIBUTE_DFA_FILE },
    { UFD_SMSP__BUSINESS_MODIFIER,              UFD_SMSP__BUSINESS_MODIFIER},
};
 
/*---------------------------------------------------------------------------*
 * Structure of report form
 *---------------------------------------------------------------------------*/
static UFD_SMSP__report_form_t report_field_defs[] =
{ 
  { UFD_SMSP__PART_NAME,              "Part Name",         add_type, fill_part_name   },

  /* definition field */
  { UFD_SMSP__DEFINITION_TITLE,       "Definition Title",  add_type, fill_pd_title    },
  { UFD_SMSP__DEFINITION_STATUS,      "Status",            add_type, fill_pd_status   }, 
  { UFD_SMSP__DEFINITION_SCOPE,       "Scope",             add_type, fill_pd_scope    },
  { UFD_SMSP__DEFINITION_GEOMETRY,    "Geometry",          add_type, fill_pd_geometry },
  { UFD_SMSP__DEFINITION_APPLICATION, "Applications",      add_type, fill_pd_app      },
  { UFD_SMSP__DEFINITION_DISPLAY,     "Displayed In Views",add_type, fill_pd_display  },

  /* attribute fields */
  { UFD_SMSP__ATTRIBUTE_TITLE,        "Attribute Title",   add_type, fill_att_title   },
  { UFD_SMSP__ATTRIBUTE_GROUP,        "Attribute Group",   add_type, fill_att_group   },
  { UFD_SMSP__ATTRIBUTE_TYPE,         "Attribute Type",    add_type, fill_att_type    },
  { UFD_SMSP__ATTRIBUTE_DFA_FILE,     "Attribute DFA File",add_type, fill_att_dfa     },

  /* attribute item field */
  { UFD_SMSP__ATTRIBUTE_ITEM,         "Attribute Item",    add_values,    fill_item_data },
  { UFD_SMSP__ITEM_TITLE,             "Item Title",        add_null, fill_null_data },
  { UFD_SMSP__ITEM_VALUE,             "Item Value",        add_null, fill_null_data },

  /* business modifier */
  { UFD_SMSP__BUSINESS_MODIFIER,      "Business Modifier", add_modifiers, fill_bmod_data },
  { UFD_SMSP__BUSMOD_VALUE,           "Modifier Value",    add_null, fill_null_data },
  { UFD_SMSP__BUSMOD_TITLE,           UFD_SMSP__TEMP_BUSMOD_TITLE,    add_null, fill_null_data },

  /* GD&T information */
  { UFD_SMSP__TOLERANCE_NUMBER_INFO,             "Tolerance Number",      add_gdt_type, fill_null_data },
  { UFD_SMSP__PATTERN_TYPE_INFO,                 "Pattern",               add_gdt_type, fill_null_data },
  { UFD_SMSP__PULLED_FROM_INFO,                  "Pulled From",           add_gdt_type, fill_null_data },
  { UFD_SMSP__PARENT_TOLERANCE_FEATURE_INFO,     "Parent Feature",        add_gdt_type, fill_null_data },
  { UFD_SMSP__CHILD_TOLERANCE_FEATURES_INFO,     "Child Features",        add_gdt_type, fill_null_data },
  { UFD_SMSP__LINKED_TOLERANCE_FEATURES_INFO,    "Linked Features",       add_gdt_type, fill_null_data },
  { UFD_SMSP__PULLED_FROM_TOLERANCE_NUMBER_INFO, "Pulled From Tolerance", add_gdt_type, fill_null_data },
  { UFD_SMSP__CALLOUT_STRING_INFO,               "Callout",               add_gdt_type, fill_null_data },
  { UFD_SMSP__ENTIRE_CALLOUT_STRING_INFO,        "Entire Callout",        add_gdt_type, fill_null_data },
  { UFD_SMSP__TOLERANCE_BAND_INFO,               "Tolerance Band",        add_gdt_type, fill_null_data },
  { UFD_SMSP__STANDARD_KEYWORDS_INFO,            "Standard Keywords",     add_gdt_type, fill_null_data },
  { UFD_SMSP__USER_DEFINED_KEYWORDS_INFO,        "User Keywords",         add_gdt_type, fill_null_data },
  { UFD_SMSP__ABOVE_APPENDED_TEXT_INFO,          "Above App Text",        add_gdt_type, fill_null_data },
  { UFD_SMSP__BELOW_APPENDED_TEXT_INFO,          "Below App Text",        add_gdt_type, fill_null_data },
  { UFD_SMSP__BEFORE_APPENDED_TEXT_INFO,         "Before App Text",       add_gdt_type, fill_null_data },
  { UFD_SMSP__AFTER_APPENDED_TEXT_INFO,          "After App Text",        add_gdt_type, fill_null_data },
  { UFD_SMSP__PRIMARY_DATUM_INFO,                "Primary Datum",         add_gdt_type, fill_null_data },
  { UFD_SMSP__SECONDARY_DATUM_INFO,              "Secondary Datum",       add_gdt_type, fill_null_data },
  { UFD_SMSP__TERTIARY_DATUM_INFO,               "Tertiary Datum",        add_gdt_type, fill_null_data },
  { UFD_SMSP__RELATED_FACES_INFO,                "Related Faces",         add_gdt_type, fill_null_data },
  { UFD_SMSP__NOMINAL_SIZE_INFO,                 "Nominal Size",          add_gdt_type, fill_null_data },
};

static  UFD_SMSP__GDT_fields_only_t UFD_SMSP__GDT_fields_only_table [] =  
{
    UFD_SMSP__TOLERANCE_NUMBER_INFO, 
    UFD_SMSP__PATTERN_TYPE_INFO,
    UFD_SMSP__PULLED_FROM_INFO,
    UFD_SMSP__PARENT_TOLERANCE_FEATURE_INFO, 
    UFD_SMSP__CHILD_TOLERANCE_FEATURES_INFO, 
    UFD_SMSP__LINKED_TOLERANCE_FEATURES_INFO,
    UFD_SMSP__PULLED_FROM_TOLERANCE_NUMBER_INFO,
    UFD_SMSP__CALLOUT_STRING_INFO, 
    UFD_SMSP__ENTIRE_CALLOUT_STRING_INFO, 
    UFD_SMSP__TOLERANCE_BAND_INFO,
    UFD_SMSP__STANDARD_KEYWORDS_INFO,  
    UFD_SMSP__USER_DEFINED_KEYWORDS_INFO, 
    UFD_SMSP__ABOVE_APPENDED_TEXT_INFO,
    UFD_SMSP__BELOW_APPENDED_TEXT_INFO,
    UFD_SMSP__BEFORE_APPENDED_TEXT_INFO, 
    UFD_SMSP__AFTER_APPENDED_TEXT_INFO, 
    UFD_SMSP__PRIMARY_DATUM_INFO, 
    UFD_SMSP__SECONDARY_DATUM_INFO,
    UFD_SMSP__TERTIARY_DATUM_INFO,
    UFD_SMSP__RELATED_FACES_INFO, 
    UFD_SMSP__NOMINAL_SIZE_INFO
};

/*------------------------------------------------------------------------*
 * Local function propotypes
 * 
 * All function will return error code 
 *------------------------------------------------------------------------*/

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

        if ( length2 > 0  && str2 != NULL )
            strcat( copy, str2 );

        if ( length3 > 0  && str3 != NULL )
            strcat( copy, str3 );
    }

    return ( copy );
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
    int length = strlen( str );
    char *copy = NULL;

    if ( length > 0 )
    {
        copy = alloc_string( length + 1 );
        strcpy( copy, str );
    }

    return ( copy );
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

    switch ( error_code )
    {
        case UFD_SMSP__ERR_NO_PART:
            str = "No part sprecified";
            break;

        case UFD_SMSP__ERR_NO_REPORT_OUTPUT_DATA:
            str = "No output data specified";
            break;

        case UFD_SMSP__ERR_NO_OUTPUT_FILE:
            str = "No output file defined";
            break;

        case UFD_SMSP__ERR_NO_OUTPUT_WINDOW:
            str = "No output window defined";
            break;
            
        default:
            str = "User Function error";
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

    if ( error_code == UF_SMSP_NO_ERROR )
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
 * Initialize the report structure
 *---------------------------------------------------------------------------*/
static int init_report( UFD_SMSP__report_p_t report)
{
    /* output format */
    report->format.type    = UFD_SMSP__NO_OUTPUT;
    report->format.file    = NULL;

    /* information list to be output */
    report->list.num_types          = 0;
    report->list.types              = NULL;

    /* information output list field */
    report->output.num_fields  = 0;
    report->output.current_col = 0;
    report->output.fields      = NULL;
    
    /* part information */
    report->part.tag             = NULL_TAG;
    report->part.name            = NULL;
    report->part.num_definitions = 0;
    report->part.max_values      = 0;
    report->part.max_busmod      = 0;
    report->part.busmod_titles   = NULL;
    report->part.definitions     = NULL;

    /* GDT information */
    report->part.num_GDT_fields = 0;
    report->part.GDT_fields = NULL;
    report->part.num_GDT_fields_only = 0;
    report->part.num_tol_feats = 0;
    report->part.tol_feat_tags = NULL;
    report->part.tol_feat_data = NULL;

    return UF_SMSP_NO_ERROR;
}

/*---------------------------------------------------------------------------*
 * Initialize the report fields and output data
 *
 * Returns:
 *     UF_SMSP_NO_ERRORS
 *     UFD_SMSP__ERR_NO_REPORT_OUTPUT_DATA
 *     Error from UF_allocate_memory
 *---------------------------------------------------------------------------*/
static int open_report(
    UFD_SMSP__report_p_t report   /* <I/O> Report structure to initialize */
)
{
    char *report_file_envar = "UFD_SMSP_REPORT_FILE";
    char *report_infowin_envar = "UFD_SMSP_REPORT_INFOWIN";
    char *report_file;
    char *report_infowin;
    int status = UF_SMSP_NO_ERROR;

    /* load environment variable */
    UF_translate_variable( report_file_envar, &report_file );
    UF_translate_variable( report_infowin_envar, &report_infowin );

    if (report_file != NULL)
    {
        /* open the file */
        FILE *file = fopen( report_file, "w+" );

        if ( file == NULL )
        {
            /* can't open the file, report an error */
            print_error( "Report setup", UF_SMSP_NO_ERROR,
                         "Error opening %s = %s", report_file_envar, report_file );

            status = UFD_SMSP__ERR_NO_OUTPUT_FILE;
        }
        else
        {
            report->format.type |= UFD_SMSP__FILE_OUTPUT;
            report->format.file  = file;
        }
    }
    else
        status = UFD_SMSP__ERR_NO_OUTPUT_FILE;
        
    if ( report_infowin != NULL )
    {
        int open_status = UF_UI_open_listing_window();
        if (open_status != UF_SMSP_NO_ERROR )
        {
            /* can't open listing window, report an error */
            print_error( "Report setup", open_status,
                         "Error opening listing window" );

            if (status == UFD_SMSP__ERR_NO_OUTPUT_FILE)
                status = UFD_SMSP__ERR_NO_REPORT_OUTPUT_DATA;
        }
        else
        {
            report->format.type |= UFD_SMSP__INFO_WINDOW_OUTPUT;
            status = UF_SMSP_NO_ERROR;
        }
    }
    else
    {
        if (status == UFD_SMSP__ERR_NO_OUTPUT_FILE)
            status = UFD_SMSP__ERR_NO_REPORT_OUTPUT_DATA;
    }        

    return status;
}

static int initialization(UFD_SMSP__report_p_t report)
{
    int status;

    status = UF_initialize();

    if ( status != UF_SMSP_NO_ERROR )
    {
        print_error( "UF_initialize", status, "Aborting report" );
        return ( status );
    }

    /* initialize the report data set */
    status = init_report(report);

    return status;
}

/*---------------------------------------------------------------------------*
 * Get the default report fields
 *---------------------------------------------------------------------------*/
static void ask_default_report_fields(
    UFD_SMSP__report_p_t report
)
{
    UFD_SMSP__info_type_t default_columns[] = 
    {     
        UFD_SMSP__PART_NAME,
        UFD_SMSP__DEFINITION_TITLE,
        UFD_SMSP__DEFINITION_STATUS,
        UFD_SMSP__DEFINITION_SCOPE,
        UFD_SMSP__DEFINITION_GEOMETRY,
        UFD_SMSP__DEFINITION_APPLICATION,
        UFD_SMSP__DEFINITION_DISPLAY,
        UFD_SMSP__ATTRIBUTE_TITLE,
        UFD_SMSP__ATTRIBUTE_GROUP,
        UFD_SMSP__ATTRIBUTE_TYPE,
        UFD_SMSP__ATTRIBUTE_DFA_FILE,
        UFD_SMSP__BUSINESS_MODIFIER,
        UFD_SMSP__ATTRIBUTE_ITEM
    };

    int status, num, num_column =  NUM_ELEMENTS( default_columns );
    UFD_SMSP__info_type_t *types;

    types =  (UFD_SMSP__info_type_t *)UF_allocate_memory(sizeof(UFD_SMSP__info_type_t) * num_column, &status );
    ERROR_CHECK( status, ( "UF_allocate_memory", status, "" ) );

    report->list.num_types = num_column;
    report->list.types = types;

    for ( num = 0; num < num_column; num++ )
        types[num] =  default_columns[num];

}

/*---------------------------------------------------------------------------*
 * Get the informatio type from the field title of 
 *---------------------------------------------------------------------------*/
static  char * ask_field_title_of_info_type(
    UFD_SMSP__info_type_t type
)
{
    int i, num_items = NUM_ELEMENTS( report_field_defs );

    for ( i= 0; i < num_items; i ++)
    {
        if (type == report_field_defs[i].type)
            return copy_string(report_field_defs[i].title);
    }

    /* try GDT data type */
    num_items = NUM_ELEMENTS( mapping_GDT_type_table );
    for (i=0; i<num_items; i++)
    {
        if (type == mapping_GDT_type_table[i].GDT_type)
        {
            return ask_field_title_of_info_type(mapping_GDT_type_table[i].type);
        }
    }

    return NULL;
}

/*---------------------------------------------------------------------------*
 * Get the field title of the informatio type
 *---------------------------------------------------------------------------*/
static  UFD_SMSP__info_type_t ask_info_type_of_field_title(
    const char *title
)
{
    int i, num_items = NUM_ELEMENTS( report_field_defs );

    for ( i= 0; i < num_items; i ++)
    {
        if (strcmp(title, report_field_defs[i].title) == 0)
            return report_field_defs[i].type;
    }

    return UFD_SMSP__NULL_TYPE;
}

/*---------------------------------------------------------------------------*
 * Read the report fields from a file
 *---------------------------------------------------------------------------*/
static void ask_report_fields_from_file(
    int  channel,                     /* <I>  I/O channel for file to read    */
    UFD_SMSP__report_p_t report       /* <IO> Output report data              */
)
{
    char line[ MAX_LINE_BUFSIZE ];
    int status, num_item = 0;
    UFD_SMSP__info_type_t type;
    int size = sizeof(UFD_SMSP__info_type_t);

    while ( uc4514( channel, line ) >= 0 )
    {
        char *title;

        title = ask_string_no_extra_spaces(line);
        type = ask_info_type_of_field_title(title);

        if (type != UFD_SMSP__NULL_TYPE)
        {
            report->list.types = (UFD_SMSP__info_type_t *)UF_reallocate_memory(report->list.types, size * (num_item+1), &status );
            ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );

            report->list.types[num_item] = type;
            num_item++;
        }

        else
            print_error( "Reading report settings", UF_SMSP_NO_ERROR,
                         "%s Title type does not support!", title );

        UF_free( title );
    }

    report->list.num_types = num_item;
}

static int ask_report_fields(UFD_SMSP__report_p_t report)
{
    char *settings_file_envar = "UFD_SMSP_REPORT_SETTINGS_FILE";
    char *settings_file;
    int exists = 1;
    int error = UF_SMSP_NO_ERROR;

    UF_translate_variable( settings_file_envar, &settings_file );

    if ( settings_file != NULL )
    {
        int status;

        status = UF_CFI_ask_file_exist( settings_file, &exists );
        ERROR_CHECK( status, ( "UF_CFI_ask_file_exist", status, "%s = %s",
                               settings_file_envar, settings_file ) );
    }

    if ( exists != 0 )
    {
        print_error( "Report setup", UF_SMSP_NO_ERROR,
                     "%s = %s does not exist!\n  Using default report columns",
                     settings_file_envar, settings_file );

        ask_default_report_fields( report );
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
            ask_default_report_fields( report );
        }
        else
        {
            int disposition = 0; /* Normal close */

            ask_report_fields_from_file( channel, report);
            uc4540( channel, disposition );
        }
    }

    return error;
}

static void fill_column(UFD_SMSP__report_p_t report, int column, 
                        UFD_SMSP__info_type_t type, char *title)
{
    report->output.fields[column].title = title;
    report->output.fields[column].column = column;
    report->output.fields[column].data.type = type;
    report->output.fields[column].data.str = NULL;
    report->output.current_col++;

    report->output.num_fields = report->output.current_col;
}

static void insert_busmod_title_in_field(UFD_SMSP__report_p_t report, char *title)
{
    int i, status;
    for (i=0; i<report->part.max_busmod; i++)
    {
        /* check if the title is already in the field */
        if (strcmp(title, report->part.busmod_titles[i]) == 0)
            return;
    }

    /* insert the business modiifer title into the field */
    if (report->part.max_busmod == 0)
    {
        report->part.busmod_titles = (char **)UF_allocate_memory(sizeof( char *), &status );
        ERROR_CHECK( status, ( "UF_allocate_memory", status, "" ) );
    }
    else
    {
        report->part.busmod_titles = (char **)UF_reallocate_memory(report->part.busmod_titles, 
                                                          (report->part.max_busmod+1) * sizeof( char *),
                                                          &status );
        ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );
    }

    report->part.busmod_titles[report->part.max_busmod] = copy_string(title);
    report->part.max_busmod++;
}

static void ask_busmod_title_in_part(UFD_SMSP__report_p_t report)
{
    int pd, attr, busmod, i,j,k;
    UF_PD_product_definition_p_t pd_data;
    UF_PD_product_attribute_p_t attr_data;
    UF_PD_business_modifier_p_t busmod_data;
    UFD_SMSP__GDT_tol_feat_data_p_t tol_feat_data;
    UFD_SMSP__GDT_tol_feat_attr_data_p_t tol_feat_attr_data;

    for (pd = 0; pd < report->part.num_definitions; pd++)
    {
        pd_data = report->part.definitions[pd];
        for (attr = 0; attr < pd_data->num_product_attributes; attr++)
        {
            attr_data = &pd_data->product_attributes[attr];
            for (busmod=0; busmod < attr_data->number_busmods; busmod++)
            {
                busmod_data = &attr_data->busmods[busmod];
                insert_busmod_title_in_field(report, busmod_data->title);
            }
        }
    } 
    
    /* Count on GD&T object to see if we need add more busmod */
    for( i = 0; i < report->part.num_tol_feats; i ++ )
    {
        tol_feat_data = &report->part.tol_feat_data[i];
        for( j =0 ; j < tol_feat_data->num_attributes; j++ )
        {
            tol_feat_attr_data = &(tol_feat_data->tol_feat_attr_data[j]);
            attr_data = &tol_feat_attr_data->product_att_data;

            /* Business modifiers for tolerance attributes. */
            for( k =0 ; k < tol_feat_attr_data->num_busmods; k++ )
            {
                busmod_data = &tol_feat_attr_data->busmods[k];
                insert_busmod_title_in_field(report, busmod_data->title);
            }
            
            /* Business modifiers for product attributes. */
            for (k = 0; k < attr_data->number_busmods; k++)
            {
                busmod_data = &attr_data->busmods[k];
                insert_busmod_title_in_field(report, busmod_data->title);
            }
        }
    }
}

/*---------------------------------------------------------------------------*
 * Callback function to add type to report field
 *---------------------------------------------------------------------------*/
static int add_null(
    UFD_SMSP__info_type_t type,
    void *data
)
{
    return (UF_SMSP_NO_ERROR);
}

/*----------------------------------------------------------------------------*
 * Ask to mapped GDT type 
 *----------------------------------------------------------------------------*/
static UFD_SMSP__info_type_t ask_GDT_mapped_type(UFD_SMSP__info_type_t type)
{
    int i; 

    for (i=0; i< NUM_ELEMENTS(mapping_GDT_type_table); i++)
    {
        if (type == mapping_GDT_type_table[i].type)
            return mapping_GDT_type_table[i].GDT_type;
    }
    
    return UFD_SMSP__NULL_TYPE;
}

/*---------------------------------------------------------------------------*
 * Callback function to add type to report field
 *---------------------------------------------------------------------------*/
static int add_type(
    UFD_SMSP__info_type_t type,
    void *data
)
{
    int column, size, status, error = UF_SMSP_NO_ERROR;
    UFD_SMSP__info_type_t GDT_type;
    UFD_SMSP__report_p_t report = (UFD_SMSP__report_p_t)data;
    
    column = report->output.current_col;
    size = sizeof(UFD_SMSP__report_field_t)*(column+1);

    report->output.fields = (UFD_SMSP__report_field_p_t)UF_reallocate_memory(report->output.fields, size, &status );
    ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );

    fill_column(report, column, type, ask_field_title_of_info_type(type));

    /* mapping to GDT type if defined */
    GDT_type = ask_GDT_mapped_type(type);
    if (GDT_type != UFD_SMSP__NULL_TYPE)
        error = add_gdt_type(GDT_type, data); 

    return error;
}

/*---------------------------------------------------------------------------*
 * Callback function to add type to report field
 *---------------------------------------------------------------------------*/
static int add_gdt_type(
    UFD_SMSP__info_type_t type,
    void *data
)
{
    int status, num_fields, size, error = UF_SMSP_NO_ERROR;
    UFD_SMSP__report_p_t report = (UFD_SMSP__report_p_t)data;
    UFD_SMSP__info_type_t GDT_type;
    
    num_fields = report->part.num_GDT_fields;
    size = sizeof(UFD_SMSP__GDT_report_field_t) * (num_fields+1);
    report->part.GDT_fields = (UFD_SMSP__GDT_report_field_p_t)UF_reallocate_memory(report->part.GDT_fields , size, &status );
    ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );

    report->part.GDT_fields[num_fields].type = type;
    report->part.num_GDT_fields++;

    /* add output fields for GD&T for sure */
    GDT_type = ask_GDT_mapped_type(type);
#if 0
    if (GDT_type != UFD_SMSP__NULL_TYPE)
        error = add_values(UFD_SMSP__ATTRIBUTE_ITEM, report);
#endif

    return error;
}

static int add_values(
    UFD_SMSP__info_type_t type,
    void *data
)
{
    static logical first = TRUE;
    int status, error = UF_SMSP_NO_ERROR;
    UFD_SMSP__report_p_t report = (UFD_SMSP__report_p_t)data;
    int i, column, size;
    UFD_SMSP__info_type_t this_type;
    char *title, msg[ MAX_LINE_BUFSIZE ];

    DEBUG_ASSERT(type == UFD_SMSP__ATTRIBUTE_ITEM);

    /* only create value form once, even user defines the parameter
     * several times */
#if 0
    if (!first)
        return error;
#endif

    first = FALSE;
    column = (report->output.current_col+report->part.max_values*2);
    size = sizeof(UFD_SMSP__report_field_t)*column;
    report->output.fields = (UFD_SMSP__report_field_p_t)UF_reallocate_memory(report->output.fields, size, &status );
    ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );
    
    for (i=0; i<report->part.max_values; i++)
    {
        /* Item Title */
        this_type = UFD_SMSP__ITEM_TITLE;
        column = report->output.current_col;
        title = ask_field_title_of_info_type(this_type);
        sprintf(msg, "%s %d", title, i); 
        fill_column(report, column, this_type, copy_string(msg));
        UF_free(title);

        /* Item Value */
        this_type = UFD_SMSP__ITEM_VALUE;
        column = report->output.current_col;
        title = ask_field_title_of_info_type(this_type);
        sprintf(msg, "%s %d", title, i);
        fill_column(report, column, this_type, copy_string(msg));
        UF_free(title);
    }
    return error;
}

static int add_modifiers(
    UFD_SMSP__info_type_t type,
    void *data
)
{
    static logical first = TRUE;
    int status, error = UF_SMSP_NO_ERROR;
    UFD_SMSP__info_type_t GDT_type;
    UFD_SMSP__report_p_t report = (UFD_SMSP__report_p_t)data;
    int i, column, size;

    DEBUG_ASSERT(type == UFD_SMSP__BUSINESS_MODIFIER);

    /* only create value form once, even user defines the parameter
     * several times */
#if 0
    if (!first)
      return error; 
#endif

    first = FALSE;
    column = (report->output.current_col+report->part.max_busmod);

    size = sizeof(UFD_SMSP__report_field_t)*column;
    report->output.fields = (UFD_SMSP__report_field_p_t)UF_reallocate_memory(report->output.fields, size, &status );
    ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );
    
    for (i=0; i<report->part.max_busmod; i++)
    {
        /* Modifier Title */
        column = report->output.current_col;
        fill_column(report, column, UFD_SMSP__BUSMOD_TITLE, report->part.busmod_titles[i]);
    }

    /* mapping to GDT type if defined */
    GDT_type = ask_GDT_mapped_type(type);
    if (GDT_type != UFD_SMSP__NULL_TYPE)
        error = add_gdt_type(GDT_type, data);

    return error;
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

static int ask_definition_data_in_part(
    tag_t part, 
    UFD_SMSP__report_p_t report
)
{
    int num, error = UF_SMSP_NO_ERROR;
    tag_p_t pd_tags;

    /* query all definitions in the part */
    error = UF_PD_ask_product_definitions(part, &pd_tags, &num);

    if (error)
        print_error( "Loading definitions from part", error,
                         "Can't read definition from part %d ", part );
    else if (num > 0)
    {
        UF_PD_product_definition_p_t pd_ptr;
        int status, i;

        report->part.tag = part;
        report->part.name = ask_part_name(part);

        report->part.definitions = (UF_PD_product_definition_p_t *)UF_allocate_memory(sizeof(UF_PD_product_definition_p_t) * num, &status );
        ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );

        report->part.definition_tags = (tag_t *)UF_allocate_memory(sizeof(tag_t) * num, &status );
        ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );

        for (i=0; !error && i<num; i++)
        {
            error = UF_PD_ask_product_definition_data(pd_tags[i], &pd_ptr);
            report->part.definitions[i] = pd_ptr;
            report->part.definition_tags[i] = pd_tags[i];
        }
        
        report->part.num_definitions = num;

        UF_free(pd_tags);
    }

    return error;
}


static int ask_tolerance_features(
    tag_t part,
    tag_p_t *feat_tags,
    int *num_feats
)
{
    tag_t feature = NULL_TAG;
    int error = UF_SMSP_NO_ERROR;
    
    *num_feats = 0;
    *feat_tags = (tag_t *)UF_allocate_memory( sizeof(tag_t) * (*num_feats), &error );
    ERROR_CHECK( error, ( "UF_allocate_memory", error, "" ) );

    while( !error && ask_next_tolerance_feature(part, &feature ) )
    {
        *feat_tags = (tag_t *)UF_reallocate_memory( *feat_tags, sizeof(tag_t) * (*num_feats + 1), &error );
        (*feat_tags)[*num_feats] = feature;
        (*num_feats)++;
        ERROR_CHECK( error, ( "UF_reallocate_memory", error, "" ) );
    }
    
    return error;
}


static int ask_gdt_tol_feat_data_in_part(
    tag_t part, 
    UFD_SMSP__report_p_t report
)
{
    int num, error = UF_SMSP_NO_ERROR;
    tag_p_t tol_feat_tags = NULL;

    /* Add GD&T fields only info */
    report->part.num_GDT_fields_only = NUM_ELEMENTS( UFD_SMSP__GDT_fields_only_table );

    /* query all tolerance features in the part */
    error = ask_tolerance_features(part, &tol_feat_tags, &num);

    if (error)
        print_error( "Loading gdt tolerance features from part", error,
                         "Can't read gdt tolerance features from part %d ", part );
    
    else if (num > 0)
    {
        int status, i;

        report->part.num_tol_feats = num;
        report->part.tag = part;

        report->part.tol_feat_data = (UFD_SMSP__GDT_tol_feat_data_p_t)UF_allocate_memory(sizeof(UFD_SMSP__GDT_tol_feat_data_t) * num, &status );
        ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );

        report->part.tol_feat_tags = (tag_t *)UF_allocate_memory(sizeof(tag_t) * num, &status );
        ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );

        for (i=0; !error && i<num; i++)
        {
            int num_tols = 0, num_product_atts = 0, loop, att_loop, num_total = 0;
            tag_p_t tol_tags = NULL, product_atts = NULL; 
            tag_t tol_feat_tag = tol_feat_tags[i];
            UF_GDT_tolerance_type_p_t tolerance_types = NULL;

            report->part.tol_feat_tags[i] = tol_feat_tags[i];

            error = UF_GDT_ask_tolerances( tol_feat_tag, &tol_tags, &num_tols, &tolerance_types );

            if (error)
                print_error( "Loading gdt tolerances from part", error,
                             "Can't read gdt tolerances from part %d ", part );
                
            if (error == UF_SMSP_NO_ERROR)
            {
                error = UF_GDT_ask_product_attributes(tol_feat_tag, &num_product_atts, &product_atts);
                
                if (error)
                    print_error( "Loading product attributes for gdt from part", error,
                                 "Can't read product attributes for gdt from part %d ", part );
            }
            
            if (error == UF_SMSP_NO_ERROR)
            {
                /* Now, we have both the tolerances and product attributes under the attribute umbrella. */
                num_total = num_tols + num_product_atts;
                
                (report->part.tol_feat_data[i]).num_attributes = num_total;
                
                (report->part.tol_feat_data[i]).tol_feat_attr_data = 
                    (UFD_SMSP__GDT_tol_feat_attr_data_p_t)UF_allocate_memory(
                        sizeof(UFD_SMSP__GDT_tol_feat_attr_data_t)* num_total, &status );
                ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );
                
                (report->part.tol_feat_data[i]).attributes = 
                    (tag_t *)UF_allocate_memory(sizeof(tag_t) * num_total, &status );
                ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );
                
                for( loop = 0; !error && loop < num_tols; loop ++ )
                {
                    tag_t tol_tag = tol_tags[loop];
                    tag_p_t modifiers = NULL;
                    int num_mods, inner_loop;
                    
                    (report->part.tol_feat_data[i]).attributes[loop] = tol_tag;
                    
                    UF_PD_init_attribute(&(report->part.tol_feat_data[i]).tol_feat_attr_data[loop].product_att_data);
                    
                    error = UF_PD_ask_business_process_modifiers(tol_tag, &modifiers, &num_mods );
                    
                    (report->part.tol_feat_data[i]).tol_feat_attr_data[loop].num_busmods = num_mods;
                    
                    (report->part.tol_feat_data[i]).tol_feat_attr_data[loop].busmods = (UF_PD_business_modifier_p_t)UF_allocate_memory(sizeof(UF_PD_business_modifier_t)*num_mods, &status );
                    ERROR_CHECK( status, ( "UF_reallocate_memory", status, "" ) );
                    
                    for( inner_loop = 0; !error && inner_loop < num_mods; inner_loop ++ )
                    {
                        tag_t mod_tag = modifiers[inner_loop];
                        UF_PD_business_modifier_t modifier_data;
                        
                        error = UF_PD_ask_business_process_modifier_data( mod_tag, &modifier_data );
                        
                        ((report->part.tol_feat_data[i]).tol_feat_attr_data[loop]).busmods[inner_loop].title = copy_string(modifier_data.title);
                        ((report->part.tol_feat_data[i]).tol_feat_attr_data[loop]).busmods[inner_loop].value = copy_string(modifier_data.value);
                        
                        /* Clean up */
                        UF_PD_free_business_modifier_data( &modifier_data );
                    }
                    
                    /* Clean up */
                    UF_free(modifiers);
                    
                }
                
                att_loop = 0;
                for( loop = num_tols; !error && loop < num_total; loop++ )
                {
                    tag_t att = product_atts[att_loop];
                    UF_PD_product_attribute_t attr_data;
                    
                    (report->part.tol_feat_data[i]).attributes[loop] = att;
                    
                    error = UF_PD_ask_product_attribue_data(att, &attr_data);
                    
                    (report->part.tol_feat_data[i]).tol_feat_attr_data[loop].num_busmods = 0;
                    (report->part.tol_feat_data[i]).tol_feat_attr_data[loop].busmods = NULL;
                    (report->part.tol_feat_data[i]).tol_feat_attr_data[loop].product_att_data = attr_data;
                    
                    att_loop++;        
                }
            }
            
            /* Clean up */
            UF_free(tol_tags);
            UF_free(tolerance_types);
            UF_free(product_atts);
        }

        UF_free(tol_feat_tags);
    }

    return error;
}

static int create_output_form_of_type(UFD_SMSP__report_p_t report)
{
    int i, k, error = UF_SMSP_NO_ERROR;
    UFD_SMSP__info_type_t type;

    for (i=0; !error && i<report->list.num_types; i++)
    {
        type = report->list.types[i];
        for (k=0; k<NUM_ELEMENTS( report_field_defs ); k++)
        {
            if (type == report_field_defs[k].type)
            {
                error = (*report_field_defs[k].add_type)(type, (void*)report);
                break;
            }
        }
    }

    /* total fields need to output */
    report->output.num_fields = report->output.current_col;

    return error;
}

static int ask_max_attribute_value_items(UF_PD_product_definition_p_t pd)
{
    int i, max = 0;

    for (i=0; i<pd->num_product_attributes; i++)
    {
        if (max < pd->product_attributes[i].num_attribute_value_dats)
            max = pd->product_attributes[i].num_attribute_value_dats;
    }

    return max;
}

static int ask_max_attribute_value_number(UF_PD_product_definition_p_t pd)
{
    int i, max = 0;

    for (i=0; i<pd->num_product_attributes; i++)
    {
        if (max < pd->product_attributes[i].num_attribute_values)
            max = pd->product_attributes[i].num_attribute_values;
    }

    return max;
}

static int ask_max_gdt_attribute_value_number(
    UFD_SMSP__GDT_tol_feat_data_p_t tol_feat_data
)
{
    int loop, max = 0;

    for (loop = 0; loop < tol_feat_data->num_attributes; loop++)
    {
        if (max < tol_feat_data->tol_feat_attr_data[loop].product_att_data.num_attribute_values)
            max = tol_feat_data->tol_feat_attr_data[loop].product_att_data.num_attribute_values;
    }
    
    return max;
}

static int ask_max_gdt_attribute_value_items(
    UFD_SMSP__GDT_tol_feat_data_p_t tol_feat_data
)
{
    int loop, max = 0;
    
    for (loop = 0; loop < tol_feat_data->num_attributes; loop++)
    {
        if (max < tol_feat_data->tol_feat_attr_data[loop].product_att_data.num_attribute_value_dats)
            max = tol_feat_data->tol_feat_attr_data[loop].product_att_data.num_attribute_value_dats;        
    }
    
    return max;
}

static int fill_attribute_data(UFD_SMSP__report_p_t report, logical is_gdt, int smrt, int attr)
{
    int i, k, error = UF_SMSP_NO_ERROR;
    UFD_SMSP__info_type_t type;
    
    for (i=0; !error && i<report->list.num_types; i++)
    {
        type = report->list.types[i];
        for (k=0; k<NUM_ELEMENTS( report_field_defs ); k++)
        {
            if (type == report_field_defs[k].type)
            {
                error = (*report_field_defs[k].fill_data)(type, (void*)report, is_gdt, smrt, attr);
                break;
            }
        }
    }

    return error;
}

static char * creat_single_line_title(UFD_SMSP__report_p_t report)
{
    int i;
    char *line = NULL;

    for (i=0; i<report->output.num_fields; i++)
        line = concatenate_strings(line, report->output.fields[i].title, "\t");

    /* end of the line */
    line = concatenate_strings(line, "\n", NULL);

    return line;
}

static char * creat_single_line_data(UFD_SMSP__report_p_t report)
{
    int i;
    char *line = NULL;

    for (i=0; i<report->output.num_fields; i++)
        line = concatenate_strings(line, report->output.fields[i].data.str, "\t");

    /* end of the line */
    line = concatenate_strings(line, "\n", NULL);

    return line;
}

static int output_data_to_file(UFD_SMSP__report_p_t report, char *line)
{
    int error = UF_SMSP_NO_ERROR;

    fprintf(report->format.file, "%s", line );

    return error;
}

/*ARGSUSED */
static int output_data_to_window(UFD_SMSP__report_p_t report, char *line)
{
    int status;
        
    status = UF_UI_write_listing_window( line );
    ERROR_CHECK( status, ( "UF_UI_write_listing_window", status,
                           "line = %s", line ) );
    return status;
}

static int output_field_title(UFD_SMSP__report_p_t report)
{
    int error = UF_SMSP_NO_ERROR;
    char *line = NULL;
    
    line = creat_single_line_title(report);

    if (report->format.type & UFD_SMSP__FILE_OUTPUT)
        output_data_to_file(report, line);

    if (report->format.type & UFD_SMSP__INFO_WINDOW_OUTPUT)
        output_data_to_window(report, line);
    
    UF_free( line );

    return error;
}

static int output_data_to_device(UFD_SMSP__report_p_t report)
{
    int error = UF_SMSP_NO_ERROR;
    char *line;

    line = creat_single_line_data(report);

    /* send to the output file if defined */
    if (report->format.type & UFD_SMSP__FILE_OUTPUT)
        error = output_data_to_file(report, line);

    /* send to the output window if defined */
    if (!error && report->format.type & UFD_SMSP__INFO_WINDOW_OUTPUT)
        error = output_data_to_window(report, line);

    UF_free(line);

    return error;
}

static int cleanup_filled_data(UFD_SMSP__report_p_t report)
{
    int i, error = UF_SMSP_NO_ERROR;

    for (i=0; i<report->output.num_fields; i++)
    {
        if (report->output.fields[i].data.str != NULL)
        {
            UF_free(report->output.fields[i].data.str);
            report->output.fields[i].data.str = NULL;
        }
    }

    return error;
}

static int cleanup_filled_field(UFD_SMSP__report_p_t report)
{
    int i, error = UF_SMSP_NO_ERROR;

    /* free filled data */
    error = cleanup_filled_data(report);

    /* free the filled title */
    for (i=0; !error && i<report->output.num_fields; i++)
    {
        if (report->output.fields[i].title != NULL)
        {
            UF_free(report->output.fields[i].title);
            report->output.fields[i].title = NULL;
        }

        report->output.fields[i].column = 0;
        report->output.fields[i].data.type =  UFD_SMSP__NULL_TYPE;
    }

    report->output.num_fields = 0;
    UF_free(report->output.fields);

    return error;
}

static int  fill_report_data_field(UFD_SMSP__report_p_t report)
{
    int loop_attr, loop_pd, num_attrs, error = UF_SMSP_NO_ERROR;

    if (report->part.num_definitions > 0 || report->part.num_tol_feats > 0)
        output_field_title(report);
    
    for (loop_pd=0; !error && loop_pd<report->part.num_definitions; loop_pd++)
    {
        num_attrs = report->part.definitions[loop_pd]->num_product_attributes;
        for (loop_attr=0; !error && loop_attr<num_attrs; loop_attr++)
        {
            
            error = fill_attribute_data(report, FALSE, loop_pd, loop_attr);
            
            /* output the attribute data in a single line */
            error = output_data_to_device(report);
            
            /* cleanup the filled field */
            error = cleanup_filled_data(report);
        }
    }
    
    /* fill GD&T feature data to report fields */
    fill_GDT_report(report);

    return error;
}

static int determine_report_form(UFD_SMSP__report_p_t report)
{
    int i, error = UF_SMSP_NO_ERROR;
    
    /* fix the field format, need to find the max number
     * attribue number and business mdifier number */ 
    int num_values, num_value_items, max_value_items =0, max_values = 0;
    for (i=0; i<report->part.num_definitions; i++)
    {
        num_values = ask_max_attribute_value_number(report->part.definitions[i]);
        num_value_items = ask_max_attribute_value_items(report->part.definitions[i]);

        if (num_values > max_values) max_values = num_values;
        if (num_value_items > max_value_items) max_value_items = num_value_items;
    }
    
    /* Find the max number, attribute number for gdt */
    for (i=0; i<report->part.num_tol_feats; i++)
    {        
        num_values = ask_max_gdt_attribute_value_number(&report->part.tol_feat_data[i]);
        num_value_items = ask_max_gdt_attribute_value_items(&report->part.tol_feat_data[i]);
        
        if (num_values > max_values) 
            max_values = num_values;
        if (num_value_items > max_value_items) 
            max_value_items = num_value_items;
    }

    /* determine how many business modifier in the part */
    ask_busmod_title_in_part(report);

    /* combine attribute values and attribute items */
    report->part.max_values = max_values + max_value_items;

    /* add gdt feature data */
    if (report->part.num_tol_feats > 0 && report->part.num_GDT_fields_only > report->part.max_values)
        report->part.max_values = report->part.num_GDT_fields_only;


    /* it is time to create the report by info data type */
    error = create_output_form_of_type(report);
    return error;
}

/*----------------------------------------------------------------------
 * Function will determine the report fields based on the 
 * user requirement and part information, it will determine 
 * all titles in a single column of data contained in a report row
 *----------------------------------------------------------------------*/
static int create_report_fields_from_part(UFD_SMSP__report_p_t report)
{
    int error = UF_SMSP_NO_ERROR;

   /* No output? do nothing and return here */
    if (report->format.type == UFD_SMSP__NO_OUTPUT)
        return error;

    /* determine the output spreadsheet format */
    error = determine_report_form(report);

    /* fill the report field */
    if (error == UF_SMSP_NO_ERROR)
        error = fill_report_data_field(report);

    return error;
}

static int create_report_format(UFD_SMSP__report_p_t report)
{
    int error = UF_SMSP_NO_ERROR;

    /* ask user requireed report fields */
    error = ask_report_fields(report);

    /* create report fields based on product definition info */
    if (error == UF_SMSP_NO_ERROR)
        error = create_report_fields_from_part(report);

    /* done, cleanup */
    error = cleanup_filled_field(report);

    return error;
}

static int close_report_files(UFD_SMSP__report_p_t report)
{
    int error_code = UF_SMSP_NO_ERROR;
    
    if (report->format.type & UFD_SMSP__FILE_OUTPUT)
        fclose(report->format.file);

    return ( error_code );

}

static int UFD_SMSP__GDT_free_data( UFD_SMSP__report_p_t report )
{
    int loop, error = UF_SMSP_NO_ERROR;

    for( loop = 0; loop < report->part.num_tol_feats; loop ++ )
    {
        UFD_SMSP__GDT_tol_feat_data_p_t tol_feat_data = &report->part.tol_feat_data[loop];
        int inner_loop;
        
        for( inner_loop = 0; inner_loop < tol_feat_data->num_attributes; inner_loop++ )
        {
            UFD_SMSP__GDT_tol_feat_attr_data_p_t tol_feat_attr_data = &tol_feat_data->tol_feat_attr_data[inner_loop];
            int inner_inner_loop;
            
            for( inner_inner_loop = 0; inner_inner_loop < tol_feat_attr_data->num_busmods; inner_inner_loop++ )
            {
                UF_PD_business_modifier_p_t busmod = &tol_feat_attr_data->busmods[inner_inner_loop];
                
                /* Clean up */
                error = UF_PD_free_business_modifier_data( busmod );
            }
            
            /* Clean up */
            UF_free( tol_feat_attr_data->busmods );                    
            error = UF_PD_free_product_attribute_data( &tol_feat_attr_data->product_att_data );            
        }
        
        /* Clean up */        
        UF_free( tol_feat_data->tol_feat_attr_data );
        UF_free( tol_feat_data->attributes );
    }
    
    /* Clean up */
    UF_free( report->part.tol_feat_tags );
    UF_free( report->part.tol_feat_data );
    
    return error;
}

static int close_report(UFD_SMSP__report_p_t report)
{
    int i, error = UF_SMSP_NO_ERROR;

    /* close all opened files */
    close_report_files(report);

    /* free memory */
    for (i=0; !error && i<report->part.num_definitions; i++)
        error = UF_PD_free_product_definition_data(&report->part.definitions[i]);
    
    /* free GD&T data memory */
    UFD_SMSP__GDT_free_data( report );

    UF_free(report->part.definitions);
    UF_free(report->list.types);

    error = init_report(report);
    
    return ( error );
}

static int show_report(UFD_SMSP__report_p_t report)
{
    int error_code = UF_SMSP_NO_ERROR;

    /* create report format based on user's requirement */
    error_code = create_report_format( report );
    
    /* done, close report */
    close_report( report );

    return ( error_code );
}

/*ARGSUSED */
static int end_report(UFD_SMSP__report_p_t report)
{
    int term_status, error = UF_SMSP_NO_ERROR;

    term_status = UF_terminate();
    if ( error != 0 )
    {
        print_error( "UF_terminate", term_status, "" );
        if ( error == UF_SMSP_NO_ERROR )
            error = term_status;
    }

    return error;
}

static int start_show_report(UFD_SMSP__report_p_t report, tag_t part_tag)
{
    int error = UF_SMSP_NO_ERROR;

    /* query all definition data in the part */
    error = ask_definition_data_in_part(part_tag, report);
    error = ask_gdt_tol_feat_data_in_part(part_tag, report);
    
    if (error != UF_SMSP_NO_ERROR)
    {
        print_error( "Loading definitions from part", error,
                     "Can't read definition from part %d ", part_tag );
        return error;
    }
    
    /* prepare to output the report */
    error = open_report(report);
    
    /* output report now */
    if (error == UF_SMSP_NO_ERROR)
        error = show_report(report);

    /* terminate and cleanup */
    error = end_report(report);

    return error;
}

static char* ask_attached_geom_type(
    tag_t geom_tag,
    int *geom_type
)
{
    int err, etype, stype;
    char *type = NULL;
    int geometry_type = NULL_TAG;

    err = UF_OBJ_ask_type_and_subtype(geom_tag, &etype, &stype);

    if (err != 0)
        return type;

    geometry_type = etype;
    switch (etype)
    {
        case UF_line_type:
            type = copy_string("Line");
            break;

        case UF_circle_type:
            type = copy_string("Circle");
            break;

        case UF_conic_type:
            type = copy_string("Conic");
            break;

        case UF_point_type:
            type = copy_string("Point");
            break;

        case UF_spline_type:
            type = copy_string("Spline");
            break;

        case UF_cylinder_type:
            type = copy_string("Cylinder");
            break;

        case UF_cone_type:
            type = copy_string("Cone");
            break;

        case UF_sphere_type:
            type = copy_string("Sphere");
            break;

        case UF_component_type:
            type = copy_string("Component");
            break;

        case UF_solid_type:
        {
            geometry_type = stype;
            switch (stype)
            {
                case UF_solid_face_subtype:
                    type = copy_string("Face");
                    break;

                case UF_solid_body_subtype:
                    type = copy_string("Solid");
                    break;

                case UF_solid_edge_subtype:
                    type = copy_string("Edge");
                    break;

                default:
                    break;
            }
            break;
        }

        case UF_face_type:
            type = copy_string("Face");
            break;

        case UF_edge_type:
            type = copy_string("Edge");
            break;

        case UF_solid_composite_type:
            type = copy_string("Composite");
            break;

        case UF_pattern_type:
            type = copy_string("Pattern");
            break;

        default:
            break;            
    }

    *geom_type = geometry_type;
    return type;
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, 
 * pd, attr, bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_part_name  (UFD_SMSP__info_type_t type, void * data, logical is_gdt, 
                            int smrt, int attr)
{
    UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;

    return insert_to_field(report, type, report->part.name);
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd 
 * attr, bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_pd_title   (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                            int smrt, int attr)
{
    if (!is_gdt)
    {
        UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
        
        return insert_to_field(report, type, report->part.definitions[smrt]->name);
    }    
    return UF_SMSP_NO_ERROR;
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd
 * attr, bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_pd_status  (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                            int smrt, int attr)
{
    int error = UF_SMSP_NO_ERROR;

    if (!is_gdt)
    {
        UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
        
        if (report->part.definitions[smrt]->retained)
            error = insert_to_field(report, type, "Retained");
        else
            error = insert_to_field(report, type, "Active");
    }
    return error; 
}

static char * ask_display_in_views(tag_t pd)
{
    int error = UF_SMSP_NO_ERROR;
    tag_t *instances = NULL;
    int i, num_instances = 0;
    char view_name[ UF_OBJ_NAME_BUFSIZE ];
    int view_dep;
    char *delimiter = NULL;
    char *str = NULL;

    error = UF_PD_ask_product_definitions_instances(pd, &instances, &num_instances);

    for (i=0; !error && i <num_instances; i++)
    {
        error = uc6409( instances[i], &view_dep, view_name );
        ERROR_CHECK( error, ( "uc6409", error,
                               "instance = %u", instances[i]));
        
        if ( view_dep == 0 )
            str = concatenate_strings( str, delimiter, "Model Views" );
        else
            str = concatenate_strings( str, delimiter, view_name );
        
        delimiter = ", ";            
    } 

    UF_free( instances );

    return str;
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data,  pd
 * attr, bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_pd_scope   (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                            int smrt, int attr)
{
    int i, error = UF_SMSP_NO_ERROR;

    if (!is_gdt)
    {
        UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
        tag_t geometry_tag;
        char **geom_set = NULL, *scope = NULL;
        char *geometry_type, *delimiter = NULL;
        int k, num_types = 0, applied_geom_type[100] = { 0 }, geom_type;
        logical applied = FALSE;
        
        for (i=0; i<report->part.definitions[smrt]->num_geometry_references; i++)
        {
            geometry_tag = report->part.definitions[smrt]->geometry_references[i];        
            geometry_type = ask_attached_geom_type(geometry_tag, &geom_type);
            
            applied = FALSE;
            
            for (k=0; !applied && k<num_types; k++)
                applied = (geom_type == applied_geom_type[k]);
            
            if (!applied)
            {
                scope = concatenate_strings(scope, delimiter, geometry_type);
                delimiter = ",";
                applied_geom_type[k] = geom_type;
                num_types ++;
            }
            
            UF_free(geometry_type);
        }
        
        if (scope == NULL)
            scope = copy_string ("None");
        
        error = insert_to_field(report, type, scope);
        UF_free(scope);
    }
    
    return error;
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd 
 * attr, bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_pd_geometry(UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                            int smrt, int attr)
{
    int i, error = UF_SMSP_NO_ERROR;

    if (!is_gdt)
    {
        UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
        char *geom = NULL, str[10];
        tag_t geometry_tag;
        char *delimiter = NULL;
        
        for (i=0; i<report->part.definitions[smrt]->num_geometry_references; i++)
        {
            geometry_tag = report->part.definitions[smrt]->geometry_references[i];
            sprintf(str, "%d", geometry_tag);
            geom = concatenate_strings(geom, delimiter, str);
            delimiter = ",";
        }
        
        error = insert_to_field(report, type, geom);
        UF_free(geom);
    }    
    return error; 
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd
 * attr, bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_pd_app (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                        int smrt, int attr)
{
    int error = UF_SMSP_NO_ERROR, num_instances = 0;

    if (!is_gdt)            
    {
        UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
        char str[ MAX_LINE_BUFSIZE ];
        tag_t *instances = NULL, pd_tag = report->part.definition_tags[smrt];
        
        error = UF_PD_ask_product_definitions_instances(pd_tag, &instances, &num_instances);
        
        sprintf(str, "%d", num_instances);
        error = insert_to_field(report, type, str);
    }
    
    
    return error; 
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd
 * attr, bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_pd_display (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                            int smrt, int attr)
{
    int error = UF_SMSP_NO_ERROR;
    
    if (!is_gdt)
    {
        UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
        tag_t pd_tag = report->part.definition_tags[smrt];
        char *view_names;
        
        view_names = ask_display_in_views(pd_tag);
        
        error = insert_to_field(report, type, view_names);
        UF_free(view_names);
    }
    return error; 
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, 
 * bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_att_title  (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                            int smrt, int attr)
{
    int error = UF_SMSP_NO_ERROR;
    UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
    char *string;
    
    if (is_gdt)
        string = report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.attribute_name;
    else
        string = report->part.definitions[smrt]->product_attributes[attr].attribute_name;
    error = insert_to_field(report, type, string);

    return error;
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd, attr
 * bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_att_group  (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                            int smrt, int attr)
{
    int error = UF_SMSP_NO_ERROR;        
    UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
    char *string;

    if (is_gdt)
        string = report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.attribute_group;
    else
        string = report->part.definitions[smrt]->product_attributes[attr].attribute_group;
    error = insert_to_field(report, type, string);
    
    return error; 
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd, attr 
 * bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_att_type   (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                            int smrt, int attr)
{
    int error = UF_SMSP_NO_ERROR;
    UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
    char *string;

    if (is_gdt)
        string = report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.attribute_type_name;
    else
        string = report->part.definitions[smrt]->product_attributes[attr].attribute_type_name;
    error = insert_to_field(report, type, string);
    
    return error; 
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd, attr
 * bmod, value are not used 
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_att_dfa    (UFD_SMSP__info_type_t type, void * data, logical is_gdt, 
                            int smrt, int attr)
{
    int error = UF_SMSP_NO_ERROR;
    UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
    char *string;
    
    if (is_gdt)
        string = report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.kf_name;
    else
        string = report->part.definitions[smrt]->product_attributes[attr].kf_name;
    error = insert_to_field(report, type, string);
    
    return error; 
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd, attr, bmod, value
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_bmod_data (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                           int smrt, int attr)
{
    int i, num_items, error = UF_SMSP_NO_ERROR;
    UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
    UF_PD_business_modifier_p_t value;
    
    if (is_gdt)
        num_items = report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.number_busmods;
    else
        num_items = report->part.definitions[smrt]->product_attributes[attr].number_busmods;
    
    for (i=0; !error && i<num_items; i++)
    {
        if (is_gdt)
            value = &report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.busmods[i];
        else
            value = &report->part.definitions[smrt]->product_attributes[attr].busmods[i];
        error = insert_busmod_to_field(report, value, i);
    }

    return error; 
}

static char *ask_attribute_value_item(UF_PD_attribute_value_string_p_t value)
{
    int i;
    char *str = NULL, *delimiter = NULL;
    
    for (i=0; i<value->num_strings; i++)
    {
        str = concatenate_strings(str, delimiter, value->strings[i]);
        delimiter = ",";
    }

    return str;
}

static char *ask_attribute_value(UF_PD_attribute_value_p_t value)
{
    char msg[ MAX_LINE_BUFSIZE ];

    switch (value->value_type)
    {
        case UF_PD_INTEGER_VALUE:
            sprintf(msg, "%d", value->integer_value);
            break;

        case UF_PD_NUMBER_VALUE:
            sprintf(msg, "%f", value->number_value);
            break;

        case UF_PD_LIST_VALUE:
        case UF_PD_STRING_VALUE:
        case UF_PD_URL_VALUE:
            sprintf(msg, "%s", value->string_value);
            break;
        default:
            break;
    }

    return (copy_string(msg));
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd, attr, bmod, value
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_null_data (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                           int smrt, int attr)
{
    return (UF_SMSP_NO_ERROR);
}

/*----------------------------------------------------------------------------------
 * Callback function to ask part title
 *
 * Input type, data, pd, attr, bmod, value
 *
 * return: error code will be return
 *--------------------------------------------------------------------------------*/  
/*ARGSUSED */
static int fill_item_data (UFD_SMSP__info_type_t type, void * data, logical is_gdt,
                           int smrt, int attr)
{
    int i, num_items, num_values, error = UF_SMSP_NO_ERROR;
    UFD_SMSP__report_p_t report = ( UFD_SMSP__report_p_t ) data;
    UF_PD_attribute_value_p_t value;
    UF_PD_attribute_value_data_p_t item_data;
    
    if (is_gdt)
        num_values = report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.num_attribute_values;
    else
        num_values = report->part.definitions[smrt]->product_attributes[attr].num_attribute_values;

    for (i=0; !error && i<num_values; i++)
    {
        if (is_gdt)
            value = &report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.values[i];
        else
            value = &report->part.definitions[smrt]->product_attributes[attr].values[i];
        error = insert_item_to_field(report, value, i);
    }

    if (is_gdt)
        num_items = report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.num_attribute_value_dats;
    else
        num_items = report->part.definitions[smrt]->product_attributes[attr].num_attribute_value_dats;
    
    for (i=0; !error && i<num_items; i++)
    {
        if (is_gdt)
            item_data = &report->part.tol_feat_data[smrt].tol_feat_attr_data[attr].product_att_data.value_dats[i];
        else
            item_data = &report->part.definitions[smrt]->product_attributes[attr].value_dats[i];
        error = insert_item_data_to_field(report, item_data, i+num_values);
    }
    return error; 
}

static int insert_string_of_title(UFD_SMSP__report_p_t report, char *title, char *str)
{
    int i, error = UF_SMSP_NO_ERROR;
    logical find = FALSE;

    if (title == NULL || str == NULL)
        return error;

    for (i=0; !find && i<report->output.num_fields; i++)
    {
        if (strcmp(title, report->output.fields[i].title) == 0)
        {
            report->output.fields[i].data.str = copy_string(str);
            find = TRUE;
        }
    }

    /* must find */
    DEBUG_ASSERT(find);

    return error;
}

static int insert_to_field(UFD_SMSP__report_p_t report, UFD_SMSP__info_type_t type, char * data)
{
    int error = UF_SMSP_NO_ERROR;
    char * title;

    /* find the proper title to hold the data */
    title = ask_field_title_of_info_type(type);

    error = insert_string_of_title(report, title, data);

    return error;
}

static int insert_item_data_to_field (UFD_SMSP__report_p_t report, 
                                      UF_PD_attribute_value_data_p_t data, int index)
{
    int error = UF_SMSP_NO_ERROR;
    char *tmp_title = ask_field_title_of_info_type(UFD_SMSP__ITEM_TITLE);
    char title[ MAX_LINE_BUFSIZE ];
    
    /* add title to the field */
    sprintf(title, "%s %d", tmp_title, index);
    error = insert_string_of_title(report, title, data->title);
    UF_free(tmp_title);

    /* add item value to the field */
    if (!error)
    {
        char *str = ask_attribute_value_item(&data->dat);

        tmp_title = ask_field_title_of_info_type(UFD_SMSP__ITEM_VALUE);
        sprintf(title, "%s %d", tmp_title, index);
        error = insert_string_of_title(report, title, str);

        UF_free(str);
        UF_free(tmp_title);
    }
    
    return error;
}

static int insert_item_to_field(UFD_SMSP__report_p_t report, 
                                UF_PD_attribute_value_p_t item, int index)
{
    int error = UF_SMSP_NO_ERROR;
    char *tmp_title = ask_field_title_of_info_type(UFD_SMSP__ITEM_TITLE);
    char title[ MAX_LINE_BUFSIZE ];
    
    /* add title to the field */
    sprintf(title, "%s %d", tmp_title, index);
    error = insert_string_of_title(report, title, item->value_title);
    UF_free(tmp_title);

    /* add item value to the field */
    if (!error)
    {
        char *str = ask_attribute_value(item);

        tmp_title = ask_field_title_of_info_type(UFD_SMSP__ITEM_VALUE);
        sprintf(title, "%s %d", tmp_title, index);
        error = insert_string_of_title(report, title, str);

        UF_free(str);
        UF_free(tmp_title);
    }
    
    return error;
}

static int ask_bmod_field_index(UFD_SMSP__report_p_t report, char *title)
{
    int i, error = UF_SMSP_NO_ERROR ; 

    for (i=0; i<report->output.num_fields; i++)
    {
        if (report->output.fields[i].data.type == UFD_SMSP__BUSMOD_TITLE)
        {
            if (strcmp(report->output.fields[i].title, title) == 0)
            {
                if (report->output.fields[i].data.str != NULL)
                    print_error("Duplicated Business Modifier Title", 
                                error, "%s", title);
                return i;
            }
        }
    }

    /* shall not reach here */
    DEBUG_ASSERT(FALSE);

    return error;
}

/*ARGSUSED */
static int insert_busmod_to_field(UFD_SMSP__report_p_t report, 
                                  UF_PD_business_modifier_p_t item, int i)
{
    int index, error = UF_SMSP_NO_ERROR;

    index = ask_bmod_field_index(report, item->title);

    if (item->value != NULL)
        report->output.fields[index].data.str = copy_string(item->value);
    else
        report->output.fields[index].data.str = copy_string("-");
    return error;
}


#ifdef INTERNAL_UFUN
/*---------------------------------------------------------------------------*
 * Internal user function that runs the SMSP report on the current part file.
 *---------------------------------------------------------------------------*/
/*ARGSUSED */
extern void ufusr(char *param, int *retcod, int param_len)
{
    int error = UF_SMSP_NO_ERROR;
    UFD_SMSP__report_t report;

    error = initialization(&report);

    if (error == UF_SMSP_NO_ERROR)
    {
        tag_t part_tag = UF_PART_ask_display_part();

        error = start_show_report(&report, part_tag);
    }   
}

#else  /* !defined(INTERNAL_UFUN) */
/*---------------------------------------------------------------------------*
 * External user function that runs the SMSP report on a specified part file.
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
    UFD_SMSP__report_t report;
    
    status = initialization(&report);

    if ( status != UF_SMSP_NO_ERROR )
    {
        print_error( "UF_initialize", status, "Aborting report" );
        return ( status );
    }

    if ( argc < 2 )
        print_error( argv[0], UFD_SMSP__ERR_NO_PART, "Aborting report" );
    else
    {
        char *part_name = argv[1];

        status = UF_PART_open( part_name, &part, &error_status );

        if ( status == UF_SMSP_NO_ERROR || !error_status.failed )
        {
            if ( error_status.n_parts > 0 )
            {
                UF_free_string_array( error_status.n_parts,
                                      error_status.file_names );
                UF_free( error_status.statuses );
            }

            status = start_show_report(&report, part);
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

    if ( term_status != UF_SMSP_NO_ERROR )
    {
        print_error( "UF_terminate", term_status, "" );
        if ( status == UF_SMSP_NO_ERROR )
            status = term_status;
    }

    return ( status );
}
#endif  /* INTERNAL_UFUN */

/***********************************  GD&T Data process function **********************/

/*---------------------------------------------------------------------------*
 * Keyword control character definitions
 *---------------------------------------------------------------------------*/
#define UFD_GDT__KEYWORD_CCHAR      "<*KEYWORD "
#define UFD_GDT__KEYWORD_CCHAR_LEN  strlen( UFD_GDT__KEYWORD_CCHAR )
#define UFD_GDT__ARG_CCHAR          "<*>"
#define UFD_GDT__ARG_CCHAR_LEN      strlen( UFD_GDT__ARG_CCHAR )

/*---------------------------------------------------------------------------*
 * Constants used to define the type of tolerance being queried
 *---------------------------------------------------------------------------*/
typedef enum
{
    UFD_GDT__NO_TYPE = -1,
    UFD_GDT__EMPTY_FEATURE_TYPE,
    UFD_GDT__PRODUCT_ATTRIBUTE_TYPE,
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
 * Structure used to contain a single column of data contained in a report row
 *---------------------------------------------------------------------------*/
typedef struct UFD_GDT__info_data_s
{
    UFD_SMSP__info_type_t type; /* Type of information in data string        */
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

/* function prototype */
static char *ask_feature_info_data(UFD_SMSP__info_type_t info_type, logical show_datum_data,
    UFD_GDT__feature_data_p_t feature_data, UFD_GDT__object_info_p_t  object_info);

static void ask_size_tolerance_info(
    UFD_GDT__feature_data_p_t feature_data, /* <I>   Tolerance feature data */
    UF_GDT_size_tolerance_p_t size_data,    /* <I>   Size tolerance data    */
    UFD_GDT__object_info_p_t  object_info   /* <I/O> Object data to report  */
);

/*---------------------------------------------------------------------------*
 * Function to display requested data on all tolerances, datums and datum
 * targets in the part specified.
 *
 * Returns:
 *     UF_GDT_NO_ERROR
 *     UFD_GDT__ERR_NO_PART
 *---------------------------------------------------------------------------*/
static void fill_GDT_report(
        UFD_SMSP__report_p_t report /* <I> Part report definition */
)
{
    int loop;    
    tag_t part = report->part.tag;
    int error = UF_SMSP_NO_ERROR;
 
    for (loop = 0; loop < report->part.num_tol_feats; loop++)
    {
        /* process feature information */
        process_feature( report, part, loop );
        
        /* cleanup the single line memory and reset the statu */
        error = cleanup_filled_data(report);
    }

    close_GDT_report(report );
}

/*---------------------------------------------------------------------------*
 * Free the report fields and output data
 *---------------------------------------------------------------------------*/
static void close_GDT_report(UFD_SMSP__report_p_t report)
{
}

/*---------------------------------------------------------------------------*
 * Initialize the UFD_GDT__object_info structure with the specified data
 *---------------------------------------------------------------------------*/
static void init_info_data(
    UFD_SMSP__report_p_t report,  /* <I> Report containing fields to query */
    tag_t part,                   /* <I> Part tag of tolerance feature     */
    tag_t feature,                /* <I> Tolerance feature tag             */
    tag_t tolerance,              /* <I> FCF tag or NULL_TAG               */
    UFD_GDT__object_type_t type,  /* <I> Tolerance object type             */
    UFD_GDT__object_info_p_t object_info
                                  /* <O> Initialized internal object data  */
)
{
    int status, num;

    object_info->part           = part;
    object_info->feature        = feature;
    object_info->tolerance      = tolerance;
    object_info->tolerance_type = type;

    object_info->count = report->part.num_GDT_fields;
    object_info->list  = (UFD_GDT__info_data_p_t)
        UF_allocate_memory( object_info->count * sizeof( UFD_GDT__info_data_t ), &status );
    ERROR_CHECK( status, ( "UF_allocate_memory", status, "" ) );

    for ( num = 0; num < report->part.num_GDT_fields; num++ )
    {
        object_info->list[num].type = report->part.GDT_fields[num].type;
        object_info->list[num].data = NULL;
    }
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
    tag_t *tag1 = (tag_t *) ptr1;
    tag_t *tag2 = (tag_t *) ptr2;

    if ( *tag1 < *tag2 )
        return ( UFD_GDT__LESS_THAN );
    else if ( *tag1 > *tag2 )
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

static int insert_feature_data_to_title_field(
    UFD_SMSP__report_p_t report,
    char *title,
    char *str,
    logical shared,
    int index
)
{
    int error = UF_SMSP_NO_ERROR;
    char *tmp, tmp_title[ MAX_LINE_BUFSIZE ];

    if (shared)
    {
        error = insert_string_of_title(report, title, str);
        return error;
    }

    /* insert real GDT feature data into the report field */    
    if (!error)
    {
        tmp = ask_field_title_of_info_type(UFD_SMSP__ITEM_TITLE);
        sprintf(tmp_title, "%s %d", tmp, index);
        error = insert_string_of_title(report, tmp_title, title);
        UF_free(tmp);
    }

    if (!error)
    {
        tmp = ask_field_title_of_info_type(UFD_SMSP__ITEM_VALUE);
        sprintf(tmp_title, "%s %d", tmp, index);
        error = insert_string_of_title(report, tmp_title, str);
        UF_free(tmp);
    }

    return error;
}

/*----------------------------------------------------------------------------
 * Find tolerance busmod data for the given tolerance
 *
 * Return error code
 *----------------------------------------------------------------------------*/
static UFD_SMSP__GDT_tol_feat_attr_data_p_t find_gdt_tolerance_busmod_data( 
     UFD_SMSP__report_p_t report,
    UFD_GDT__object_info_p_t  object_info     /* <I> Object data           */
)
{
    UFD_SMSP__GDT_tol_feat_attr_data_p_t tol_feat_attr_data = NULL;
    int loop;

    if( object_info->tolerance == NULL_TAG )
        return NULL;

    for( loop = 0; loop < report->part.num_tol_feats; loop ++ )
    {
        int inner_loop;
        UFD_SMSP__GDT_tol_feat_data_p_t tol_feat_data = &report->part.tol_feat_data[loop];

        for( inner_loop = 0; inner_loop < tol_feat_data->num_attributes; inner_loop++ )
        {
            if( tol_feat_data->attributes[inner_loop] == object_info->tolerance )
            {
                tol_feat_attr_data = tol_feat_data->tol_feat_attr_data;
                break;
            }
        }
    }
    return tol_feat_attr_data;
}
    

/*----------------------------------------------------------------------------
 * Fill information specific to the tolerance feature to report field 
 *
 * Return error code
 *----------------------------------------------------------------------------*/
static int fill_feature_info_data(
    UFD_SMSP__report_p_t report,
    UFD_GDT__object_info_p_t  object_info     /* <I> Object data           */
)
{
    int i, index, GDT_index, error = UF_SMSP_NO_ERROR;
    char *title = NULL;
    logical found = FALSE, found_busmod = FALSE;
    
    GDT_index = -1;

    for (i=0; i<object_info->count; i++)
    {
        found = FALSE;
        found_busmod = FALSE;

        for (index=0; !found && !found_busmod && index<NUM_ELEMENTS(mapping_GDT_type_table); index++)
        {
            if (object_info->list[i].type == mapping_GDT_type_table[index].GDT_type)
            {
                if( object_info->list[i].type == UFD_SMSP__BUSINESS_MODIFIER )
                    found_busmod = TRUE;
                else
                {
                    title = ask_field_title_of_info_type(mapping_GDT_type_table[index].type);
                    found = TRUE;
                }
            }
        }

        /* GDT_index is used to define the GDT feature data index 
         * that will match the number of Item in the report field
         */
        if (!found && !found_busmod)
        {
            title = ask_field_title_of_info_type(object_info->list[i].type);
            GDT_index ++;
        }

        /* if found busmod title, try to fill the busmod data from GD&T object */
        if( found_busmod )
        {
            UFD_SMSP__GDT_tol_feat_attr_data_p_t attr_data = NULL;
            int loop;

            attr_data = find_gdt_tolerance_busmod_data( report, object_info ); 
            
            if( attr_data != NULL )
            {
                for( loop = 0; loop < attr_data->num_busmods; loop++ )
                {
                    UF_PD_business_modifier_p_t value;
                    value = &attr_data->busmods[loop];
                    error = insert_busmod_to_field(report, value, loop); 
                }
            }
        }
        else
            error = insert_feature_data_to_title_field (report, title, object_info->list[i].data, found, GDT_index); 

        /* Clean up */
        if( title != NULL )
        {
            UF_free(title); 
            title = NULL;
        }
    }
                
    return error;
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
    tag_t *face1 = (tag_t *) ptr1;
    tag_t *face2 = (tag_t *) ptr2;
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
 * are listed by face tag.
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
        char face_index_str[ MAX_LINE_BUFSIZE ];

        sprintf( face_index_str, "%d", faces[num] );
        str = concatenate_strings( str, delimiter, face_index_str );
        delimiter = ",";
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

    if (type_str == NULL)
        return type_str;
    else
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
        type_str = "Tolerance Feature";
    else if ( type == UFD_GDT__PRODUCT_ATTRIBUTE_TYPE )
        type_str = "Product Attribute";
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

    if (type_str == NULL)
        return type_str;
    else
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
    else if (type == UF_GDT_SPLINE_FEATURE)
        type_str = "Spline";
    else if (type == UF_GDT_GEAR_FEATURE)
        type_str = "Gear";
    else if (type == UF_GDT_CIRCULAR_TOOTH_THICKNESS_FEATURE)
        type_str = "Circular Tooth Thickness";
    else if (type == UF_GDT_CIRCULAR_SPACE_WIDTH_FEATURE)
        type_str = "Circular Space Width";
    else if (type == UF_GDT_PIN_MEASUREMENT_FEATURE)
        type_str = "Pin Measurement";

    if (type_str == NULL)
        return type_str;
    else
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

static char * ask_tol_feat_application(
    UFD_GDT__object_type_t obj_type, /* <I> Type of object being queried    */
    tag_t                 feature    /* <I> Feature of object being queried */
)
{
    char *delimiter = NULL;
    char str_instance[ MAX_LINE_BUFSIZE ];
    int num_instances, status;
    tag_p_t instances;

    status = UF_GDT_ask_tol_feat_instance( feature, &num_instances, &instances );
    ERROR_CHECK( status, ( "UF_GDT_ask_tol_feat_instance", status,
                           "feature = %u", feature ) );

    sprintf(str_instance, "%d", num_instances);

    UF_free( instances );
    return copy_string (str_instance);
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
    UFD_SMSP__report_p_t       report,      /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data /* <I>   Tolerance feature data */
)
{
    UFD_GDT__object_info_t object_info;
    int status;

    init_info_data( report, feature_data->part, feature_data->feature,
                    NULL_TAG, UFD_GDT__EMPTY_FEATURE_TYPE,
                    &object_info );

    ask_feature_info( FALSE, feature_data, &object_info );
    fill_feature_info_data(report, &object_info );

    /* need output data here, otherwise the previous 
     * feature data will be lost
     */
    status = output_data_to_device(report);
}

/*---------------------------------------------------------------------------*
 * Add information on the datum or datum target specified to the part report
 * data
 *---------------------------------------------------------------------------*/
static void add_datum_info(
    UFD_SMSP__report_p_t      report,       /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data, /* <I>   Tolerance feature data */
    UF_GDT_tolerance_type_t   tol_type      /* <I>   UF_GDT datum type      */
)
{
    UFD_GDT__object_info_t object_info;
    UFD_GDT__object_type_t type = UFD_GDT__NO_TYPE;
    int status;

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
    fill_feature_info_data(report, &object_info );

    /* need output data here, otherwise the previous 
     * feature data will be lost
     */
    status = output_data_to_device(report);
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
 * Ask the callout string that corresponds to the input tolerance along with
 * all appended text if so specified.
 *
 * Returns:
 *     Allocated callout string
 *---------------------------------------------------------------------------*/
static char *ask_nominal_size(
    logical                   show_type, /* <I> Show tolerance type */
    UFD_GDT__object_type_t    type,      /* <I> Type of tolerance   */
    UF_GDT_size_tolerance_p_t size_data  /* <I> Size tolerance data */
)
{
    char nominal_str[ MAX_LINE_BUFSIZE ];
    char *str = NULL;

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
        int length = strlen(str) + strlen("(Radians)") + 1;
        str = realloc_string( str,length );
        strcat( str,"(Radians)" );
    }

    return ( str );
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
    UFD_GDT__object_type_t tol_type = UFD_GDT__NO_TYPE;

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
        if ( compare_strings( keyword_name, "UG_INDIVIDUAL_COUNT", -1 ) ||
             compare_strings( keyword_name, "UG_PATTERN_COUNT", -1 ) )
            sprintf( arg, "%d Faces", num_faces );
        else
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
    UFD_SMSP__info_type_t type     /* <O> Appended text info type             */
)
{
    char *str = NULL;
    int num, status;
    int num_lines = 0;
    char **lines = NULL;

    switch ( type )
    {
        case UFD_SMSP__ABOVE_APPENDED_TEXT_INFO:
            status = UF_GDT_ask_appended_text( object, UF_GDT_ABOVE,
                                               &num_lines, &lines );
            ERROR_CHECK( status, ( "UF_GDT_ask_appended_text", status,
                                   "object = %u, UF_GDT_ABOVE", object ) );
            break;

        case UFD_SMSP__BELOW_APPENDED_TEXT_INFO:
            status = UF_GDT_ask_appended_text( object, UF_GDT_BELOW,
                                               &num_lines, &lines );
            ERROR_CHECK( status, ( "UF_GDT_ask_appended_text", status,
                                   "object = %u, UF_GDT_BELOW", object ) );
            break;

        case UFD_SMSP__BEFORE_APPENDED_TEXT_INFO:
            status = UF_GDT_ask_appended_text( object, UF_GDT_BEFORE,
                                               &num_lines, &lines );
            ERROR_CHECK( status, ( "UF_GDT_ask_appended_text", status,
                                   "object = %u, UF_GDT_BEFORE", object ) );
            break;

        case UFD_SMSP__AFTER_APPENDED_TEXT_INFO:
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

        strs[0] = ask_appended_text( feature, tolerance, UFD_SMSP__ABOVE_APPENDED_TEXT_INFO );
        strs[1] = ask_appended_text( feature, tolerance, UFD_SMSP__BEFORE_APPENDED_TEXT_INFO );
        strs[2] = str;
        strs[3] = ask_appended_text( feature, tolerance, UFD_SMSP__AFTER_APPENDED_TEXT_INFO );
        strs[4] = ask_appended_text( feature, tolerance, UFD_SMSP__BELOW_APPENDED_TEXT_INFO );

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
        char *nominal_str = ask_nominal_size( show_type, tol_type, size_data );

        if ( str == NULL )
            str = nominal_str;
        else
            str = concatenate_strings( nominal_str, " ", str );

        str = add_appended_text( feature_data->feature, str, tolerance );
    }

    return ( str );
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
    UFD_SMSP__report_p_t      report,      /* <I/O> Current report         */
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
    tag_t tolerance = NULL_TAG;

    status = UF_GDT_ask_tolerance( feature_data->feature, type, &tolerance );
    ERROR_CHECK( status, ( "UF_GDT_ask_size_tolerance", status,
                           "feature = %u", feature_data->feature ) );

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
                    tolerance, tol_type,
                    &object_info );

    ask_size_tolerance_info( feature_data, size_tol_data, &object_info );

    fill_feature_info_data(report, &object_info );

    /* need output data here, otherwise the previous 
     * feature data will be lost
     */
    status = output_data_to_device(report);

    status = UF_GDT_free( UF_GDT_SIZE_TOL_TYPE, size_tol_data );
    ERROR_CHECK( status, ( "UF_GDT_free", status,
                           "data type = UF_GDT_SIZE_TOL_TYPE(%d)",
                           UF_GDT_SIZE_TOL_TYPE ) );

    UF_free( size_tol_data );
    UF_free( thread_tol_data );
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

    if (str == NULL)
        return str;

    else
        return ( copy_string( str ) );
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
    tag_t datums[3] = { NULL_TAG };
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
        tag_p_t datum_faces = NULL;

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

static char * ask_gdt_dfa_file( tag_t gdt_obj )
{
    char *dfa_file = NULL;

    UF_GDT_ask_gdt_object_dfa_file( gdt_obj, &dfa_file );

    return dfa_file;

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
            case UFD_SMSP__TOLERANCE_NUMBER_INFO:
                status = UF_GDT_ask_tolerance_index( feature_data->feature, &tol_index );
                ERROR_CHECK( status, ( "UF_GDT_ask_tolerance_index", status,
                                       "feature = %u", feature_data->feature ) );

                object_info->list[num].data =
                    ask_tolerance_index_string( FALSE, tol_index, 0 );
                break;

            case UFD_SMSP__TOLERANCE_TYPE_INFO:
                object_info->list[num].data =
                    ask_tolerance_type( object_info->tolerance_type );
                break;

            case UFD_SMSP__PULLED_FROM_TOLERANCE_NUMBER_INFO:
                object_info->list[num].data =
                    ask_component_tolerance_index( FALSE, feature_data->feature,
                                                   object_info->tolerance, 0 );
                break;

            case UFD_SMSP__CALLOUT_STRING_INFO:
                object_info->list[num].data =
                    ask_size_callout( FALSE, feature_data, size_data,
                                      object_info->tolerance_type,
                                      feature_data->feature );
                break;

            case UFD_SMSP__ENTIRE_CALLOUT_STRING_INFO:
                object_info->list[num].data = ask_entire_callout( feature_data, object_info->tolerance_type );
                break;

            case UFD_SMSP__NOMINAL_SIZE_INFO:
                /* Don't display nominal size information for thread tolerance */
                if( object_info->tolerance_type != UFD_GDT__THREAD_TOLERANCE_TYPE )
                {
                    object_info->list[num].data =
                        ask_nominal_size( FALSE, object_info->tolerance_type,
                                          size_data );
                }
                break;

            case UFD_SMSP__TOLERANCE_BAND_INFO:
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

            case UFD_SMSP__STANDARD_KEYWORDS_INFO:
                object_info->list[num].data =
                    ask_keywords( TRUE, feature_data->part,
                                  feature_data->feature_parms->modifier_data,
                                  size_data->modifier_data );
                break;

            case UFD_SMSP__USER_DEFINED_KEYWORDS_INFO:
                object_info->list[num].data =
                    ask_keywords( FALSE, feature_data->part,
                                  feature_data->feature_parms->modifier_data,
                                  size_data->modifier_data );
                break;

            case UFD_SMSP__ABOVE_APPENDED_TEXT_INFO:
            case UFD_SMSP__BELOW_APPENDED_TEXT_INFO:
            case UFD_SMSP__BEFORE_APPENDED_TEXT_INFO:
            case UFD_SMSP__AFTER_APPENDED_TEXT_INFO:
                object_info->list[num].data =
                    ask_appended_text( feature_data->feature,
                                       feature_data->feature,
                                       object_info->list[num].type );
                break;
            case UFD_SMSP__ATTRIBUTE_DFA_FILE:
                object_info->list[num].data = ask_gdt_dfa_file( object_info->tolerance );
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
            case UFD_SMSP__TOLERANCE_NUMBER_INFO:
                status = UF_GDT_ask_tolerance_index( fcf, &tol_index );
                ERROR_CHECK( status, ( "UF_GDT_ask_tolerance_index", status,
                                       "fcf = %u", fcf ) );

                object_info->list[num].data =
                    ask_tolerance_index_string( is_composite, tol_index,
                                                frame_num );
                break;

            case UFD_SMSP__TOLERANCE_TYPE_INFO:
                object_info->list[num].data = ask_characteristic( fcf_data );
                break;

            case UFD_SMSP__PULLED_FROM_TOLERANCE_NUMBER_INFO:
                object_info->list[num].data =
                    ask_component_tolerance_index( is_composite,
                                                   feature_data->feature,
                                                   fcf, frame_num );
                break;

            case UFD_SMSP__CALLOUT_STRING_INFO:
                object_info->list[num].data =
                    ask_fcf_callout( FALSE, feature_data, fcf, frame_num );
                break;

            case UFD_SMSP__ENTIRE_CALLOUT_STRING_INFO:
                object_info->list[num].data = ask_entire_callout( feature_data, object_info->tolerance_type );
                break;

            case UFD_SMSP__TOLERANCE_BAND_INFO:
                sprintf( str, "%.*f", frame->tolerance_zone->decimal_format,
                         frame->tolerance_zone->value );
                object_info->list[num].data = copy_string( str );
                break;

            case UFD_SMSP__PRIMARY_DATUM_INFO:
                if ( frame->primary != NULL )
                {
                    status = UF_GDT_ask_label_of_datum( frame->primary->datum_feature,
                                                        &object_info->list[num].data );
                    ERROR_CHECK( status, ( "UF_GDT_ask_label_of_datum", status,
                                           "datum = %u", frame->primary->datum_feature ) );
                }
                break;

            case UFD_SMSP__SECONDARY_DATUM_INFO:
                if ( frame->secondary != NULL )
                {
                    status = UF_GDT_ask_label_of_datum( frame->secondary->datum_feature,
                                                        &object_info->list[num].data );
                    ERROR_CHECK( status, ( "UF_GDT_ask_label_of_datum", status,
                                           "datum = %u", frame->secondary->datum_feature ) );
                }
                break;

            case UFD_SMSP__TERTIARY_DATUM_INFO:
                if ( frame->tertiary != NULL )
                {
                    status = UF_GDT_ask_label_of_datum( frame->tertiary->datum_feature,
                                                        &object_info->list[num].data );
                    ERROR_CHECK( status, ( "UF_GDT_ask_label_of_datum", status,
                                           "datum = %u", frame->tertiary->datum_feature ) );
                }
                break;

            case UFD_SMSP__RELATED_FACES_INFO:
                object_info->list[num].data =
                    ask_datum_face_references( frame );
            break;

            case UFD_SMSP__STANDARD_KEYWORDS_INFO:
                object_info->list[num].data =
                    ask_keywords( TRUE, feature_data->part,
                                  feature_data->feature_parms->modifier_data,
                                  frame->modifier_data );
                break;

            case UFD_SMSP__USER_DEFINED_KEYWORDS_INFO:
                object_info->list[num].data =
                    ask_keywords( FALSE, feature_data->part,
                                  feature_data->feature_parms->modifier_data,
                                  frame->modifier_data );
                break;

            case UFD_SMSP__ABOVE_APPENDED_TEXT_INFO:
            case UFD_SMSP__BELOW_APPENDED_TEXT_INFO:
            case UFD_SMSP__BEFORE_APPENDED_TEXT_INFO:
            case UFD_SMSP__AFTER_APPENDED_TEXT_INFO:
                object_info->list[num].data =
                    ask_appended_text( feature_data->feature, fcf,
                                       object_info->list[num].type );
                break;
            case UFD_SMSP__ATTRIBUTE_DFA_FILE:
                object_info->list[num].data = ask_gdt_dfa_file( fcf );
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
    UFD_SMSP__report_p_t       report,       /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data, /* <I>   Tolerance feature data */
    tag_t                     fcf           /* <I>   Feature control frame  */
)
{
    int error = UF_SMSP_NO_ERROR;
    int num, status;
    UF_GDT_fcf_p_t fcf_data;

    status = UF_GDT_ask_fcf_parms( fcf, &fcf_data );
    ERROR_CHECK( status, ( "UF_GDT_ask_fcf_parms", status, "fcf = %u", fcf ) );

    for ( num = 0; !error && num < fcf_data->num_frames; num++ )
    {
        UFD_GDT__object_info_t object_info;

        init_info_data( report, feature_data->part, feature_data->feature,
                        fcf, UFD_GDT__FEATURE_CONTROL_FRAME_TYPE,
                        &object_info );

        ask_fcf_info( feature_data, fcf, num, fcf_data, &object_info );

        fill_feature_info_data(report, &object_info );

        /* need output data here, otherwise the previous 
         * feature data will be lost
         */
        error = output_data_to_device(report);
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
    UFD_SMSP__report_p_t       report,      /* <I/O> Current report         */
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
 * Add information on the directed dimension specified to the part report data
 *---------------------------------------------------------------------------*/
static void add_directed_dimension_info(
    UFD_SMSP__report_p_t      report,      /* <I/O> Current report         */
    UFD_GDT__feature_data_p_t feature_data /* <I>   Tolerance feature data */
)
{
    int status;
    UFD_GDT__object_info_t object_info;
    UFD_GDT__object_type_t type;
    UF_GDT_directed_dimension_p_t dir_dim_data;
    tag_t tolerance;

    status = UF_GDT_ask_tolerance( feature_data->feature, UF_GDT_SIZE_TOLERANCE_TYPE, &tolerance );

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

    object_info.tolerance = tolerance;

    ask_size_tolerance_info( feature_data, &dir_dim_data->size_data, &object_info );

    fill_feature_info_data(report, &object_info );

    /* need output data here, otherwise the previous 
     * feature data will be lost
     */
    status = output_data_to_device(report);

    UF_free( dir_dim_data );
}

/*---------------------------------------------------------------------------*
 * Add all information on the current feature to the part report data
 *---------------------------------------------------------------------------*/
static void add_product_atts_info( 
    UFD_SMSP__report_p_t report,           /* <I> Part report definition & data     */
    int tol_feat,                          /* <I> Feature position */
    UFD_GDT__feature_data_p_t feature_data /* <I>   Tolerance feature data */
)
{
    UFD_GDT__object_info_t object_info;
    int status, loop;
    
    init_info_data( report, feature_data->part, feature_data->feature,
                    NULL_TAG, UFD_GDT__PRODUCT_ATTRIBUTE_TYPE,
                    &object_info );

    ask_feature_info( FALSE, feature_data, &object_info );
    fill_feature_info_data( report, &object_info );

    for (loop = 0; loop < (report->part.tol_feat_data[tol_feat]).num_attributes; loop++)
        fill_attribute_data(report, TRUE, tol_feat, loop);

    /* need output data here, otherwise the previous 
     * feature data will be lost
     */
    status = output_data_to_device(report);    
}

/*---------------------------------------------------------------------------*
 * Add all information on the current feature to the part report data
 *---------------------------------------------------------------------------*/
static void process_feature(
    UFD_SMSP__report_p_t report, /* <I>   Part report definition & data     */
    tag_t part,                  /* <I>   Part containing tolerance feature */
    int tol_feat                 /* <I>   Tolerance feature to query        */
)
{
    int num_tol_types, num_product_atts, status;    
    tag_t feature = report->part.tol_feat_tags[tol_feat];
    tag_p_t product_atts;
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

    status = UF_GDT_ask_product_attributes(feature, &num_product_atts, &product_atts);
    ERROR_CHECK( status, ( "UF_GDT_ask_product_attributes", status,
                           "feature = %u", feature ) );
    
    if ( num_tol_types == 0 && num_product_atts == 0)
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
        
        /* Process product attributes of tolerance feature. */
        if (num_product_atts > 0)
            add_product_atts_info( report, tol_feat, &feature_data );
    }

    free_feature_data( &feature_data );
    UF_free( tol_types );
    UF_free( product_atts );
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
 * Ask information specific to the tolerance feature
 *
 * Returns:
 *     Allocated tolerance feature information string
 *---------------------------------------------------------------------------*/
static char *ask_feature_info_data(
    UFD_SMSP__info_type_t     info_type,      /* <I>   Type of data to return*/
    logical                   show_datum_data,/* <I>   TRUE = show datum data*/
    UFD_GDT__feature_data_p_t feature_data,   /* <I>   Tolerance feature data*/
    UFD_GDT__object_info_p_t  object_info     /* <I/O> Object data           */
)
{
    char *str = NULL;
    int status, num_datums;
    logical is_retained, is_datum;
    tag_t dfa_obj = feature_data->feature;
    tag_p_t datums = NULL;

    status = UF_GDT_is_datum( feature_data->feature, &is_datum );
    ERROR_CHECK( status, ( "UF_GDT_is_datum", status,
                                   "feature = %u", feature_data->feature ) );

    /* If the feature is a datum/target/multiple datum, then
     * query the dfa for the first datum objects associated
     * with the feature.
     */
    if( is_datum )
    {
        status = UF_GDT_ask_datums_of_feature( feature_data->feature, &datums, &num_datums );
        ERROR_CHECK( status, ( "UF_GDT_ask_datums_of_feature", status,
                                   "feature = %u", feature_data->feature ) );
        DEBUG_ASSERT( num_datums > 0 );
        
        dfa_obj = datums[0];

        /* Clean up */
        UF_free(datums);
    }        

    /* Tolerance feature data */
    switch ( info_type )
    {
        case UFD_SMSP__PART_NAME_INFO:
            str = ask_part_name( feature_data->part );
            break;

        case UFD_SMSP__TOLERANCE_FEATURE_NAME_INFO:
            str = copy_string( feature_data->feature_parms->descript->name );
            break;

        case UFD_SMSP__RETAINED_STATUS_INFO:
            status = UF_GDT_is_retained( feature_data->feature, &is_retained );
            ERROR_CHECK( status, ( "UF_GDT_is_retained", status,
                                   "feature = %u", feature_data->feature ) );

            if ( is_retained )
                str = copy_string( "Retained" );
            else
                str = copy_string( "Active" );
            break;

        case UFD_SMSP__DESCRIPTION_INFO:
            str = copy_string("Tolerance Type");
            break;

        case UFD_SMSP__TOL_FEAT_APPLICATION:
            str = ask_tol_feat_application(object_info->tolerance_type,
                                              feature_data->feature );
            break;

        case UFD_SMSP__GDT_GROUP_INFO:
            str = copy_string("GD&T");
            break;

        case UFD_SMSP__FACES_INFO:
            str = ask_face_list( feature_data->feature_parms->num_faces,
                                 feature_data->feature_parms->face_list );
            break;

        case UFD_SMSP__GEOMETRIC_DEFINITION_TYPE_INFO:
            str = ask_geometric_definition_type( feature_data->geom_def->type );
            break;

        case UFD_SMSP__TOLERANCE_TYPE_INFO:
            str = ask_tolerance_type( object_info->tolerance_type );
            break;

        case UFD_SMSP__GEOMETRY_TYPE_INFO:
            str = ask_geometry_type( feature_data->feature_parms->feature );
            break;

        case UFD_SMSP__PATTERN_TYPE_INFO:
            str = ask_pattern_type( feature_data->feature_parms->pattern );
            break;

        case UFD_SMSP__DISPLAY_INSTANCE_VIEWS_INFO:
            str = ask_display_instance_views( object_info->tolerance_type,
                                              feature_data->feature );
            break;

        case UFD_SMSP__PULLED_FROM_INFO:
            str = ask_pulled_tolerance_component( feature_data->feature );
            break;

        case UFD_SMSP__PARENT_TOLERANCE_FEATURE_INFO:
            str = ask_parent_features( feature_data->feature );
            break;

        case UFD_SMSP__CHILD_TOLERANCE_FEATURES_INFO:
            str = ask_child_features( feature_data->feature );
            break;

        case UFD_SMSP__LINKED_TOLERANCE_FEATURES_INFO:
            str = ask_linked_features( feature_data->feature );
            break;

        case UFD_SMSP__RELATED_FACES_INFO:
            if ( show_datum_data )
                str = ask_faces_referencing_datum( object_info->tolerance_type,
                                                   feature_data->feature );
            break;

        case UFD_SMSP__STANDARD_KEYWORDS_INFO:
            str = ask_keywords( TRUE, feature_data->part,
                                feature_data->feature_parms->modifier_data, NULL );
            break;

        case UFD_SMSP__USER_DEFINED_KEYWORDS_INFO:
            str = ask_keywords( FALSE, feature_data->part,
                                feature_data->feature_parms->modifier_data, NULL );
            break;

        case UFD_SMSP__ENTIRE_CALLOUT_STRING_INFO:
            if ( show_datum_data )
                str = ask_datum_label( TRUE, object_info->tolerance_type,
                                       feature_data );
            break;

        case UFD_SMSP__CALLOUT_STRING_INFO:
            if ( show_datum_data )
                str = ask_datum_label( FALSE, object_info->tolerance_type,
                                       feature_data );
            break;
        case UFD_SMSP__ATTRIBUTE_DFA_FILE:
                str = ask_gdt_dfa_file( dfa_obj );
                break;
        default:
            break;
    }

    return ( str );
}
