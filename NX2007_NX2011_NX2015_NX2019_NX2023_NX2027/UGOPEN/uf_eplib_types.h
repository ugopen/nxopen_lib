/**********************************************************************
        Copyright (c) 1998 Unigraphics Solutions Corporation
                  Unpublished - All rights reserved



File description:

     User function support for the  Library
**********************************************************************/
#ifndef UF_EPLIB_TYPES_INCLUDED
#define UF_EPLIB_TYPES_INCLUDED

/**************
 ** Includes **
 **************/
#include <uf_defs.h>
#include <uf_attr.h>

#ifdef __cplusplus
extern "C" {
#endif

/************
 ** Macros **
 ************/

/***************
** Constants **
***************/

#define UF_EPLIB_TABLE_LOADED_NONE    0
#define UF_EPLIB_TABLE_LOADED_HEADER  1
#define UF_EPLIB_TABLE_LOADED_ALL     2

#define UF_EPLIB_TYPE_FILE_SELECT     0
#define UF_EPLIB_TYPE_VIEW            1
#define UF_EPLIB_TYPE_EXTERNAL        2

/**************************
 ** Structures and Types **
 **************************/

/* 
 */
typedef enum
{
   UF_EPLIB_CHARX_TYPE_UNKNOWN   = -1 ,
   UF_EPLIB_CHARX_TYPE_INT       =  0 , /*  */
   UF_EPLIB_CHARX_TYPE_REAL      =  1 , /*  */
   UF_EPLIB_CHARX_TYPE_STR       =  4 , /*  */
   UF_EPLIB_CHARX_TYPE_ANY       =  6 , /*  */
   UF_EPLIB_CHARX_TYPE_REF       = 10 ,
   UF_EPLIB_CHARX_TYPE_ANY_REF   = 11 ,
   UF_EPLIB_CHARX_TYPE_INT_EXPR  = 12 , /* integer expresions for characteristic */
   UF_EPLIB_CHARX_TYPE_REAL_EXPR = 13 , /* real    expresions for characteristic */
   UF_EPLIB_CHARX_TYPE_STR_EXPR  = 14 , /* string  expresions for characteristic */
   UF_EPLIB_CHARX_TYPE_LAST      = 15   /* The last in the list. It is not a real type */
} UF_ELIB_type_e;

/* Characteristic Value Structure*/
struct UF_EPLIB_charx_value_u
{
    int            i_value;   /* UF_EPLIB_CHARX_TYPE_INT  - Integer charx value */
    double         r_value;   /* UF_EPLIB_CHARX_TYPE_REAL - Real charx value    */
    char           *s_value;  /* UF_EPLIB_CHARX_TYPE_STR  - String charx value
                                 UF_EPLIB_CHARX_TYPE_INT_EXPR  - Expression integer charx value
                                 UF_EPLIB_CHARX_TYPE_REAL_EXPR - Expression real   charx value
                                 UF_EPLIB_CHARX_TYPE_STR_EXPR  - Expression string charx value  */
};
typedef struct UF_EPLIB_charx_value_u UF_EPLIB_charx_value_u_t,
                    *UF_EPLIB_charx_value_u_p_t;

/* Characteristic description */
struct UF_EPLIB_charx_s
{
    int                         type;    /* see UF_ELIB_type_e */
    char                        title[ UF_ATTR_MAX_TITLE_BUFSIZE ];    /* Charx title */
    UF_EPLIB_charx_value_u_t    value;
};
typedef struct UF_EPLIB_charx_s UF_EPLIB_charx_t, *UF_EPLIB_charx_p_t;

/* Multi valued characteristic definition.  Typically used for Specification
 * characteristics in an application view.
 */
struct UF_EPLIB_multi_val_charx_s
{
    UF_ELIB_type_e              type;
    char                        title[ UF_ATTR_MAX_TITLE_BUFSIZE ];    /* Charx title */
    int                         num_values; /* Number of possible characteristic values */
    UF_EPLIB_charx_value_u_t    *values;    /* len:num_values */
};
typedef struct UF_EPLIB_multi_val_charx_s UF_EPLIB_multi_val_charx_t, *UF_EPLIB_multi_val_charx_p_t;

struct UF_EPLIB_part_lib_part_s
{
    int                 num_charx;
    UF_EPLIB_charx_p_t  charx; /* <len:num_charx> */
};
typedef struct UF_EPLIB_part_lib_part_s UF_EPLIB_part_lib_part_t,
        *UF_EPLIB_part_lib_part_p_t;

struct UF_EPLIB_part_table_column_s
{
    int      type;
    char    *name;
    logical  hidden;
    logical  variable;
};
typedef struct UF_EPLIB_part_table_column_s UF_EPLIB_part_table_column_t,
        *UF_EPLIB_part_table_column_p_t;

struct UF_EPLIB_part_table_applcx_s
{
    char  *name;
    char  *format;
    char **appl_columns; /* <len:num_appl_col> */
    int    num_appl_col;
};
typedef struct UF_EPLIB_part_table_applcx_s UF_EPLIB_part_table_applcx_t,
        *UF_EPLIB_part_table_applcx_p_t;

union UF_EPLIB_part_table_datum_u
{
    char  *string_data;
    int    integer_data;
    double real_data;
};
typedef union UF_EPLIB_part_table_datum_u UF_EPLIB_part_table_datum_t,
        *UF_EPLIB_part_table_datum_p_t;

struct UF_EPLIB_part_table_index_s
{
    int   row;
    char *part_number;
};
typedef struct UF_EPLIB_part_table_index_s UF_EPLIB_part_table_index_t,
               *UF_EPLIB_part_table_index_p_t;

struct UF_EPLIB_part_table_s
{
    char                          *name;
    char                          *description;
    char                          *image;
    UF_EPLIB_part_table_column_t **columns;/* <len:num_columns> */
    int                            num_columns;
    int                            num_rows;
    UF_EPLIB_part_table_datum_t   *data;
    UF_EPLIB_part_table_applcx_t **applied;/* <len:num_applied> */
    int                            num_applied;
    int                            load_status;
    UF_EPLIB_part_table_index_t   *pn_index;
};
typedef struct UF_EPLIB_part_table_s UF_EPLIB_part_table_t,
               *UF_EPLIB_part_table_p_t;

struct UF_EPLIB_part_library_view_node_s
{
    char               *identifier;
    char               *name;
    char               *bitmap;
    char               *filter;
    UF_EPLIB_part_table_t *table;
    int                 num_subnodes;
    struct UF_EPLIB_part_library_view_node_s **subnodes; /* <len:num_subnodes> */
};
typedef struct UF_EPLIB_part_library_view_node_s UF_EPLIB_part_lib_view_node_t,
               *UF_EPLIB_part_lib_view_node_p_t;

struct UF_EPLIB_part_library_view_s
{
    char                           *name;
    UF_EPLIB_part_lib_view_node_t *top;
};
typedef struct UF_EPLIB_part_library_view_s UF_EPLIB_part_library_view_t,
               *UF_EPLIB_part_library_view_p_t;

struct UF_EPLIB_part_lib_s
{
    char                      *part_number;
    char                      *part_file_name;
    char                      *family_member_name;
    UF_EPLIB_part_library_view_t  *part_library_view;
    char                      *external_library;
    int                       part_library_type;
    char                         *entry_point;
};
typedef struct UF_EPLIB_part_lib_s UF_EPLIB_part_lib_t,
               *UF_EPLIB_part_lib_p_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_EPLIB_TYPES_INCLUDED */
