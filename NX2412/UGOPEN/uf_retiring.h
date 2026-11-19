/****************************************************************************

           Copyright (c) 1999-2023 Siemens
           Unpublished - All rights reserved

 File description:
          These routines are in the process of being removed from the Open API
          product.  Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release of Unigraphics.

****************************************************************************/

/*


*/

#ifndef UF_RETIRING
#define UF_RETIRING

/*  */
#define AT_MAX_TITLE_LEN 50
/*  */

#include <string.h>
#include <uf_cfi_types.h>
#include <uf_defs.h>
#include <uf_draw_types.h>
#include <uf_disp_types.h>
#include <uf_modl_expression_types.h>
#include <uf_drf_types.h>
#include <uf_modl_types.h>
#include <uf_obj_types.h>
#include <uf_object_types.h>
#include <uf_pd_types.h>
#include <uf_plist_types.h>
#include <uf_sf_enums.h>
#include <uf_sket_types.h>
#include <uf_ugmgr_types.h>
#include <uf_ugopenint.h>
#include <uf_weld_types.h>

#include <libufun_exports.h>

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif


/* uc2720 temporary display of markers  -- replaced by
   UF_DISP_display_temporary_point, e.g.

extern int uc2720( char *cp1, int ip2, double *rp3, int ip4, int ip5 )
   {
       int error_code = 0 ;
       if( cp1 == NULL || strlen(cp1) > 30 )
              return UF_err_bad_parameter_number_1;
       else
       {
           tag_t view_tag = NULL_TAG;
           UF_DISP_view_type_t which_views;
           double markerpos[3];
           UF_DISP_poly_marker_t  marker;
           UF_OBJ_disp_props_t color ;

           color.color = ip4;
           which_views =(UF_DISP_view_type_t) ip2;
           if ((strcmp(cp1,"") == 0) && (ip2 == 0))
           {
               which_views = (UF_DISP_view_type_t) 4;
           }
           else if ((ip2 == 0) && (strcmp(cp1,"") != 0))
           {
               error_code =UF_VIEW_ask_tag_of_view_name(cp1,&view_tag);
               if (error_code)
               {
                   which_views = (UF_DISP_view_type_t) 4;
                   error_code =0;
               }
           }

           if (error_code == 0)
           {
               UF_CSYS_map_point(UF_CSYS_WORK_COORDS, rp3,
                                 UF_CSYS_ROOT_COORDS, markerpos);

               marker = (UF_DISP_poly_marker_t) ip5;

               error_code=UF_DISP_display_temporary_point(view_tag,
                                            which_views,markerpos,
                                            &color,marker);
           }
       }

       return ( error_code );
   }

*/
extern UFUNEXPORT int uc2720(const char *cp1 /* <I> */, int ip2, double *rp3, int ip4, int ip5);

/* uc2721 display a temporary line    -- replaced by
   UF_DISP_display_temporary_line, e.g.

extern int uc2721( char *cp1, int ip2, double *rp3, int ip4, int ip5, int ip6)
{
    int error_code = 0;

    if( cp1 == NULL || strlen(cp1) > 30 )
          return UF_err_bad_parameter_number_1;
    else
    {
        tag_t view_tag = NULL_TAG;
        UF_DISP_view_type_t which_views;
        UF_OBJ_disp_props_t attrib;
        double linecoord[6];

        which_views =(UF_DISP_view_type_t) ip2;
        attrib.color = ip4;
        attrib.font = ip5;
        attrib.line_width = ip6;
        if ((strcmp(cp1,"") == 0) && (ip2 == 0))
        {
            which_views = UF_DISP_USE_WORK_VIEW;
        }
        else if ((ip2 == 0) && (strcmp(cp1,"") != 0))
        {
            error_code =UF_VIEW_ask_tag_of_view_name(cp1,&view_tag);
            if (error_code)
            {
                which_views = (UF_DISP_view_type_t) 4;
                error_code =0;
            }
        }
        if (error_code == 0)
        {
            UF_CSYS_map_point(UF_CSYS_WORK_COORDS, rp3,
                              UF_CSYS_ROOT_COORDS, linecoord);
            UF_CSYS_map_point(UF_CSYS_WORK_COORDS, &rp3[3],
                              UF_CSYS_ROOT_COORDS, &linecoord[3]);

            error_code = UF_DISP_display_temporary_line(view_tag,
                                                        which_views,
                                                        &linecoord[0],
                                                        &linecoord[3],
                                                      &attrib);
        }
    }

    return ( error_code );
}
*/
extern UFUNEXPORT int uc2721(const char *cp1 /* <I> */, int ip2, double *rp3, int ip4, int ip5, int ip6);

/* uc2722 display a temporary arc -- replaced by
   UF_DISP_display_temporary_arc, e.g.
extern int uc2722 ( char *cp1, int ip2, double *rp3, int ip4, int ip5, int ip6)
{
    int error_code =0;

    if( cp1 == NULL || strlen(cp1) > 30 )
          return UF_err_bad_parameter_number_1;
    else if (rp3 == NULL)
    {
        error_code = (UF_err_bad_parameter_number_3);
    }
    else
    {
        UF_DISP_view_type_t which_views;
        double arcords[6], arcenter[3], matrix[9], matrix_t[9];
        tag_t view_tag = NULL_TAG, wcs;
        UF_OBJ_disp_props_t attrib;

        attrib.color = ip4;
        attrib.font = ip5;
        attrib.line_width = ip6;

        arcords[0] = rp3[0];
        arcords[1] = rp3[1];
        arcords[2] = rp3[2];
        arcords[3] = rp3[3];
        arcords[4] = rp3[4];
        arcords[5] = rp3[5];

        which_views =(UF_DISP_view_type_t) ip2;

        if ((strcmp(cp1,"") == 0) && (ip2 == 0))
        {
            which_views = UF_DISP_USE_WORK_VIEW;
        }
        else if ((ip2 == 0) && (strcmp(cp1,"") != 0))
        {
            error_code =UF_VIEW_ask_tag_of_view_name(cp1,&view_tag);
            if (error_code)
            {
                which_views = (UF_DISP_view_type_t) 4;
                error_code =0;
            }
        }
        if (error_code == 0)
        {
            if (rp3[0] > 360.0)
            {
                 arcords[0] = ((int ) rp3[0]) % 360;
            }
            else
            {
                arcords[0] = rp3[0];
            }
            if (rp3[1] > 360.0)
            {
                arcords[1] = ( (int ) rp3[1]) % 360;
            }
            else
            {
                 arcords[1] = rp3[1];
            }
            if (arcords[0] > arcords[1])
            {
                 if( arcords[0] <= 0.0)
                     arcords[1] = arcords[1] + 360.0;
                 else
                 {
                     if( arcords[1] >= 0.0)
                     {
                         arcords[0] = arcords[0] - 360.0;
                     }
                     else
                     {
                          arcords[1] = arcords[1] +360.0;
                          if( arcords[0] > arcords[1])
                              arcords[0] = arcords[0] - 360.0;
                     }
                 }
             }

             if ( (arcords[1] - arcords[0]) > 360.0)
             {
                  arcords[1] = arcords[1] - 360.0;
             }

             arcords[0] = arcords[0]/RADEG;
             arcords[1] = arcords[1]/RADEG;

             UF_CSYS_map_point(UF_CSYS_WORK_COORDS, &rp3[2],
                              UF_CSYS_ROOT_COORDS, &arcords[2]);
             UF_CSYS_map_point(UF_CSYS_ROOT_COORDS, &arcords[2],
                              UF_CSYS_WORK_COORDS, &arcenter[0]);
             arcords[2] = arcenter[0];

             arcords[3] = arcenter[1];
             arcords[4] = arcenter[2];

             UF_CSYS_ask_wcs(&wcs);
             UF_CSYS_ask_matrix_values(wcs, matrix);

             matrix_t[0] = matrix[0];
             matrix_t[1] = matrix[3];
             matrix_t[2] = matrix[6];
             matrix_t[3] = matrix[1];
             matrix_t[4] = matrix[4];
             matrix_t[5] = matrix[7];
             matrix_t[6] = matrix[2];
             matrix_t[7] = matrix[5];
             matrix_t[8] = matrix[8];

             error_code = UF_DISP_display_temporary_arc(view_tag,which_views,
                                           matrix,arcords[0],arcords[1],
                                           &arcords[2],arcords[5],&attrib);
        }
    }
    return ( error_code );
}
*/
extern UFUNEXPORT int uc2722(const char *cp1 /* <I> */, int ip2, double *rp3, int ip4, int ip5, int ip6);

/*
   UF_DRF_get_char_font replaced by UF_UGFONT_ask_font_name, e.g.

   tag_t part_tag = UF_ASSEM_ask_work_part();
   tag_t fte_tag = NULL;
   char *name;

   UF_OBJ_cycle_objs_in_part(part_tag, UF_font_table_type, fte_tag);
   error = UF_UGFONT_ask_font_name(fte_tag, font_index, &name);
   if( strlen(name) > 15 )
      error = 1

   strcpy(cfont, name);
   UF_free(name);
*/
extern UFUNEXPORT int UF_DRF_get_char_font(
int font_index ,/* <I>
                The font index number for which to get a font
                name. Currently, there are 14 possible character
                fonts.
                */
char cfont[UF_DRF_MAX_FONT_BUFSIZE]  /* <O>
                The font name at index number "findx".
                The function outputs a C string. If there is no
                font at a particular index, the function outputs a
                blank string.
                */
);
/*
  uf5546 is replaced by UF_DRF_create_crosshatch,

extern void uf5546(
    int *num_boundaries,
    int *curve_count,
    tag_t *curves,
    tag_t *hatching,
    int *error
  )
  {
     *error = UF_DRF_create_crosshatch(*num_boundaries, curve_count, curves,
                                      NULL_TAG, hatching);
  }
*/
extern UFUNEXPORT void uf5546(
    int *num_boundaries,
    int *curve_count,
    tag_t *curves,
    tag_t *hatching,
    int *error
);

/*uc5520 read drafting parameters - replaced by UF_DRF_ask_preferences

extern int uc5520(int *ir1, double *rr2, char *cr3, char *cr4)
     {
        int error=0;
        error = UF_DRF_ask_preferences(ir1, rr2, cr3, cr4);

        return (error);
     }
*/
extern UFUNEXPORT int uc5520(int *ir1, double *rr2, char cr3[28] /* <O> */, char cr4[28] /* <O> */);

/* uc5521 set drafting parameters - replaced by UF_DRF_set_preferences:
extern int uc5521(int *ip1, double *rp2, char *cp3, char *cp4)
     {
         int error=0;
         error = UF_DRF_set_preferences(ip1, rp2, cp3, cp4);
         return (error);
     }
*/
extern UFUNEXPORT int uc5521(int *ip1, double *rp2, const char *cp3 /* <I> */, const char *cp4 /* <I> */);


/* UF_OBJ_is_type_displayable.
   Please use UF_OBJ_is_displayable instead.
   Note: Input to UF_OBJ_is_displayable is a tag of an object, not a type
*/
extern UFUNEXPORT logical UF_OBJ_is_type_displayable(
int object_type  /* <I>
                 Object type as defined in the header file uf_object_types.h.
                 */
);/* <NEC> */

/* UF_OBJ_is_type_transferable.
   Please use UF_OBJ_is_transferable instead.
   Note: Input to UF_OBJ_is_transferable is a tag of an object, not a type
*/
extern UFUNEXPORT int UF_OBJ_is_type_transferable(
int object_type,  /* <I>
                  Object type as defined in the header file uf_object_types.h.
                  */
logical *is_transferable  /* <O>
                           TRUE = This type is transferable
                           FALSE = This type is not transferable
                           */
);

/* UF_OBJ_can_type_have_matrix.
   Please use UF_CSYS_ask_matrix_of_object instead.
*/
extern UFUNEXPORT logical UF_OBJ_can_type_have_matrix(
int object_type  /* <I>
                 Object type as defined in the header file uf_object_types.h.
                 */
);

/* Data structure to generate a forming table record.  The "process_name"
 * string is the key to the records within the forming table, consequently
 * it must be unique.
 */
struct  UF_SMD_form_output_s
{
    char    *process_name;   /* Name of the process in the forming table. */
    char    *process_type;   /* Type of the process in the forming table. */
    char    *description;    /* Description of process in the forming table. */
};

typedef struct  UF_SMD_form_output_s UF_SMD_form_output_t,
                                    *UF_SMD_form_output_p_t;
/* Data structure to generate a record in the Bend Process and Bend Sequence
 * tables.  The "process_name" string will group records within the tables,
 * therefore it defines the position of the record within the table.  If the
 * process doesn't exist, the record is appended to the end of the tables.
 */
struct  UF_SMD_seq_input_s
{
    double  process_angle;   /* Process angle of the feature. */
    tag_t   feature;         /* Feature on which the process is performed. */
    char    *process_name;   /* Name of the process in the forming table. */
    char    *process_type;   /* Type of the process in the forming table. */
    char    *description;    /* Description of process in the forming table. */
} ;

typedef struct  UF_SMD_seq_input_s UF_SMD_seq_input_t,
                                  *UF_SMD_seq_input_p_t;
/* Data structure utilized to examine the contents of the Bend Sequence
 * table.
 */

struct  UF_SMD_seq_output_s
{
    double  design_angle;    /* Design angle of the feature. */
    double  process_angle;   /* Process angle of the feature. */
    double  inside_radius;   /* Inside radius of the feature. */
    double  bend_allowance;  /* Dimensional amount added to feature during
                                the elongation process. */
    tag_t   feature;         /* Feature on which the process is performed. */
    char    *feature_name;   /* Unigraphics proper name of the feature. */
    char    *process_name;   /* Name of the process in the forming table. */
    char    *bend_direction; /* The direction(up/down) of the bend. */
    char    *description;    /* Description of process in the forming table. */
    char    *baf;            /* Bend Allowance Formula. */
} ;

typedef struct  UF_SMD_seq_output_s UF_SMD_seq_output_t,
                                   *UF_SMD_seq_output_p_t;

/**************************************************************************
Creates a forming table for the current solid body in the work part.
The forming table contains the FORMED and UNFORMED entries
upon time of creation. If a table exists for the specified body, then the
tag of the existing table returns along with an error. This table should
be cleared for use in other forming table and bend sequence
operations. Otherwise, a NULL_TAG is returned if an error occurs
during the operation.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_create_form_tbl (
tag_t body ,/* <I>
            Object ID of a solid body.
            */
tag_p_t form_table  /* <O>
                    Object ID of a forming table.
                    */
);

/**************************************************************************
Find the forming table associated with a solid body (type 70, subtype 0).
If there is not a forming table associated with the body, then a NULL_TAG is
returned.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_form_tbl (
tag_t body ,/* <I>
            Object ID of a solid body.
            */
tag_p_t form_table  /* <O>
                    Object ID of a forming table.
                    */
);

/**************************************************************************
Cleans out the information with the exception of the Formed and
Unformed information, contained in the specified SMD forming
table.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_clear_form_tbl(
tag_t form_table  /* <I>
                  Object ID of a forming table.
                  */
);

/**************************************************************************
Retrieves the current sequence which represents the state of the solid
body.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_form_tbl_current_seq(
tag_t form_table ,/* <I>
                  Object ID of current form table.
                  */
int * record_index  /* <O>
                    Index of record into the forming table.
                    */
);

/**************************************************************************
Inquires the total number of sequences for a specified forming table.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_form_tbl_count(
tag_t form_table ,/* <I>
                  Object ID of current form table.
                  */
int * count  /* <O>
             Number of sequence records in the forming table.
             */
);

/**************************************************************************
Returns a pointer to an array of pointers to structures. Each structure
contains the data associated with that entry in the forming table. The
information contained within the structure is the name, the type, and
description of the forming process.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_form_tbl_data (
tag_t form_table ,/* <I>
                  Object ID of a forming table.
                  */
UF_SMD_form_output_p_t ** form_data ,/* <OF,len:count>
                                     A pointer to an array of pointers to typed
                                     data.
                                     */
int * count  /* <O>
             Number of sequences in forming table, including
             the FORMED and UNFORMED entries.
             */
);

/* Function prototypes for the Bend Process/Sequence table operations of
 * the UF_SMD module.
 */
/**************************************************************************
Creates a new bend sequence and adds it to the forming table. The
record is inserted into the forming table based on the specified index.
If a bend sequence already exists with the same process name the
routine does not add the record.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_create_bend_sequence (
tag_t form_table ,/* <I>
                  Object ID of current form table.
                  */
int record_index ,/* <I>
                  Index of record into the forming table.
                  */
UF_SMD_seq_input_p_t * seq_data ,/* <I,len:count>
                                 An array of pointers to typed data.
                                 */
int count  /* <I>
           Number of bend process records.
           */
);

/**************************************************************************
Deletes the bend sequence record specified by the index into the
forming table. This deletes the record from the forming table and all
records in the associated bend sequence table. The FORMED and
UNFORMED sequences may not be deleted.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_delete_bend_sequence(
tag_t form_table ,/* <I>
                  Object ID of current form table.
                  */
int record_index  /* <I>
                  Index of record into the forming table.
                  */
);

/**************************************************************************
Retrieves the bend sequence data for all entries in the bend sequence
table associated with the forming table.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_bend_seq_tbl_data(
tag_t form_table ,/* <I>
                  Object ID of current form table.
                  */
UF_SMD_seq_output_p_t ** seq_data ,/* <OF,len:count>
                                   A pointer to an array of pointers to typed
                                   data.
                                   */
int * count  /* <O>
             Number of records in bend sequence table
             associated with the forming table.
             */
);

/**************************************************************************
Retrieves the bend sequence data for a single sequence at the
specified index into the forming table.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_bend_seq_rec_data (
tag_t form_table ,/* <I>
                  Object ID of current form table.
                  */
int record_index ,/* <I>
                  Index of record into the forming table.
                  */
UF_SMD_seq_output_p_t ** seq_data ,/* <OF,len:count>
                                   A pointer to an array of pointers to typed
                                   data.
                                   */
int * count  /* <O>
             Number of records in bend sequence.
             */
);

/**************************************************************************
Execute the given sequence resulting in the active body being formed
through the specified sequence. This routine also adjusts the current
position in the forming table to the specified sequence.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_exec_sequence (
tag_t form_table ,/* <I>
                  Object ID of current forming table.
                  */
int record_index  /* <I>
                  Index of record into the forming table.
                  */
);


/**************************************************************************
 *
 * Function will be obsoleted in NX3, please call UF_MSAO_ask_ref()
 * instead.
 *
 *
 * Asks index-th face of MSAO.
 *
 * Environment: Internal and External
 *
 * See Also: UF_MSAO_ask_num_faces
 *           UF_MSAO_set_faces
 *
 * History:  Originally released in V19
 ***************************************************************************/
extern UFUNEXPORT int UF_MSAO_ask_face(
  tag_t msao,          /* <I>   tag of MSAO. */
  int   index,         /* <I>   face index, 0,.., num_faces-1. */
  tag_t *face          /* <O>   index-th face. */
);

/**************************************************************************

    The following plotting and CGM functions will be removed in
    Unigraphics NX5. The new plotting system in Unigraphics NX3
    added new functions to take advantage of features in the new
    system. The new functions do a better job of accessing the NX
    plotting and CGM functionality.

    .   uc6410   use UF_CGM_export_cgm_file
    .   uc6411   use UF_CGM_import_cgm_file
    .   UF_STD_set_cgm_size_mode  use UF_CGM_set_Session_export_options

 ***************************************************************************/

/****************************************************************************
Modify the size of Computer Graphics Metafile before being exported by uc6410

NOTE:
     . If size_mode=1, only first element of size_values is used.

Environment: Internal  and  External

See Also:  uc6410

History:
***************************************************************************/
extern UFUNEXPORT int UF_STD_set_cgm_size_mode (
const int size_mode,                    /* <I>
                                        CGM Size Mode
                                        1 = Scale
                                        2 = Dimensions
                                        */
const double size_values[2]             /* <I>
                                        Size Selection Array (2 element array)
                                        If size_mode=1, only size_values[0] is
                                        used for the scale of the CGM file,
                                        If size_mode=2, then size_values[0] is
                                        the X dimension of the CGM file, and
                                        size_values[1] is the Y dimension of
                                        the CGM file.
                                        */
);

/****************************************************************************
Export a Computer Graphics Metafile.  Use the CGM Defaults File cgmdef.txt
pointed to by the environment variable UGII_CGM_DEFAULTS.
The CGM font mapping and Virtual Device Coordinate type may be
specified in the cgmdef.txt file.

See the Unigraphics Online Help on FILE operations for details on how the
CGM Default File works.

NOTE:
     . If cp1 is blank, the CGM is built from the current display.
       If ip4=1, only 3 pens (ip5(3)) are used.

     . An extension of ".cgm" will be appended automatically to the output
       file name argument, cp2, if this extension is not specified in this
       argument.

Environment: Internal  and  External

See Also:  UF_STD_set_cgm_size_mode

History:
***************************************************************************/
extern UFUNEXPORT int uc6410(
char *   cp1 ,/* <I>
              Drawing Name (30 character max).  If the drawing name is
              an empty string, "", then the current display is exported.
              */
char * cp2 ,/* <I>
            Output File Name
            */
int ip3 ,/* <I>
         Text Representation Mode
        1 = Text
        2 = Polylines
         */
int ip4 ,/* <I>
         Pen Selection Mode
        1 = Plot By Density
        2 = Plot By Color
         */
int * ip5  /* <I>
           Pen Selection Array (15 element array)
           */
);

/****************************************************************************
Import a CGM to One or More Drawings.  A full list of any errors that
occurred during the drawing creation may be obtained by examining the LOG
file cp1.log, where cp1 is the CGM specification name.

Uses the CGM Default File cgmdef.txt pointed to by the Unix
environment variable UGII_CGM_DEFAULTS.

See the Unigraphics Online Help on file operations for details on how the
CGM Default File works.

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUNEXPORT int uc6411(
const char * cp1 ,/* <I>
            File Specification of CGM
            */
char cr2[ MAX_LINE_BUFSIZE ] /* <O>
            Error Text
            */
);

/*******************************************************************************
              Tabular Note Definitions and Function Prototypes
*******************************************************************************/

#define UF_DRAW_TABNOTE_FIRST_ROW      (-1)
#define UF_DRAW_TABNOTE_FIRST_COL      (-1)

#define UF_DRAW_TABNOTE_LAST_ROW       (-2)
#define UF_DRAW_TABNOTE_LAST_COL       (-2)

#define UF_DRAW_TABNOTE_ROW_NONE       (-3)
#define UF_DRAW_TABNOTE_COL_NONE       (-3)

/* Types of border */
enum UF_DRAW_tabnot_border_type_e
{
    UF_DRAW_tabnot_border_type_none=1,
    UF_DRAW_tabnot_border_type_single,
    UF_DRAW_tabnot_border_type_double
};

typedef enum UF_DRAW_tabnot_border_type_e UF_DRAW_tabnot_border_type_t;

/* Text justification */
enum UF_DRAW_tabnot_just_e
{
    UF_DRAW_tabnot_just_left=1,
    UF_DRAW_tabnot_just_center,
    UF_DRAW_tabnot_just_right,
    UF_DRAW_tabnot_just_top,
    UF_DRAW_tabnot_just_middle,
    UF_DRAW_tabnot_just_bottom
};

typedef enum UF_DRAW_tabnot_just_e UF_DRAW_tabnot_just_t;

/* Line data */
struct UF_DRAW_tabnot_line_s
{
    double start[3] ;         /* Absolute start position of line */
    double end[3] ;           /* Absolute end position of line   */
};

typedef struct UF_DRAW_tabnot_line_s UF_DRAW_tabnot_line_t,
                                    *UF_DRAW_tabnot_line_p_t;

/* Tabular note cell address */
struct UF_DRAW_tabnot_cell_s
{
    int row ;              /* Row number (starting at 1 in tabular note units)*/
    int col ;              /* Column number (starting at 1 in tab note units) */
};

typedef struct UF_DRAW_tabnot_cell_s UF_DRAW_tabnot_cell_t,
                                    *UF_DRAW_tabnot_cell_p_t;

/* Tabular note creation parameters */
struct UF_DRAW_tabnot_params_s
{
    double position[3] ;                           /* Position of upper left
                                                    corner of tabular note */

    UF_DRAW_tabnot_cell_t range_start ;            /* Cell at start of tabular
                                                    note range.  The rows in
                                                    this range can be set to
                                                    UF_DRAW_TABNOTE_FIRST_ROW,
                                                    UF_DRAW_TABNOTE_LAST_ROW or
                                                    a row number.  The columns
                                                    in this range can be set to
                                                    UF_DRAW_TABNOTE_FIRST_COL,
                                                    UF_DRAW_TABNOTE_LAST_COL or
                                                    a column number. */

    UF_DRAW_tabnot_cell_t range_end ;              /* Cell at end of tabular
                                                    tabular note range.  The
                                                    rows in this range can be
                                                    set to
                                                    UF_DRAW_TABNOTE_FIRST_ROW,
                                                    UF_DRAW_TABNOTE_LAST_ROW or
                                                    a row number.  The columns
                                                    in this range can be set to
                                                    UF_DRAW_TABNOTE_FIRST_COL,
                                                    UF_DRAW_TABNOTE_LAST_COL or
                                                    a column number. */

    UF_DRAW_tabnot_cell_t title_cell ;             /* Cell used to represent
                                                    the table's title, if
                                                    any.  If the row is set
                                                    to UF_DRAW_tabnot_row_
                                                    none, no title will be
                                                    shown                   */

    double ug_aspect_ratio ;                       /* UG text aspect ratio   */

    UF_DRAW_tabnot_border_type_t border_type ;     /* Type of table border
                                                    to use               */

    double border_width ;                          /* Width of table border
                                                    if table_border_type is
                                                    set to UF_DRAW_tabnot_
                                                    border_type_double     */

    logical use_title_cell ;                       /* If TRUE, display
                                                    title_cell as the title*/

    logical use_grid_lines ;                       /* If TRUE, display grid
                                                    lines between cells    */

    logical use_vert_grid_lines ;                  /* If TRUE, display
                                                    vertical grid lines
                                                    between columns        */

    logical use_horiz_grid_lines ;                 /* If TRUE, display
                                                    horizontal grid lines
                                                    between rows           */

    logical use_row_hdr_grid_lines ;               /* If TRUE, display a grid
                                                    line between row header
                                                    and body of table      */

    logical use_col_hdr_grid_lines ;               /* If TRUE, display a grid
                                                    line between column
                                                    header and body of tbl */

    logical auto_size_cells ;                      /* If TRUE, automatically
                                                    size row heights and
                                                    column widths to fit
                                                    tallest/widest text
                                                    strings in cells       */
};

typedef struct UF_DRAW_tabnot_params_s UF_DRAW_tabnot_params_t,
                                      *UF_DRAW_tabnot_params_p_t;

/* Tabular note evaluated data */
struct UF_DRAW_tabnot_eval_data_s
{
    UF_DRAW_tabnot_cell_t table_start ;            /* Cell at start of table */
    UF_DRAW_tabnot_cell_t table_end ;              /* Cell at end of table */
    int nm_lines ;                                 /* # of lines in "lines" */
    UF_DRAW_tabnot_line_t *lines ;                 /* <len:nm_lines>Array of lines used to
                                                    display the tabular
                                                    note.  Free using
                                                    UF_free()              */
};

typedef struct UF_DRAW_tabnot_eval_data_s UF_DRAW_tabnot_eval_data_t,
                                         *UF_DRAW_tabnot_eval_data_p_t;

/* Cell creation parameters */
struct UF_DRAW_tabnot_cell_params_s
{
    char *cell_text ;                           /* Cell text */
    char *ug_font ;                             /* UG text font */
    double ug_text_height ;                     /* UG text height */
    UF_DRAW_tabnot_just_t horiz_just ;          /* Horizontal justification */
    UF_DRAW_tabnot_just_t vert_just ;           /* Vertical justification */
    double text_angle ;                         /* Text angle */
    logical is_bold ;                           /* Is text displayed bold? */
    logical is_italic ;                         /* Is text displayed italic? */
    logical is_underlined ;                     /* Is text underlined? */
    logical is_wrapped ;                        /* Is text line wrapped? */
    logical strikethru ;                        /* Is text stricken thru? */
    logical is_hidden ;                         /* Is display of text
                                                 suppressed?        */
};

typedef struct UF_DRAW_tabnot_cell_params_s UF_DRAW_tabnot_cell_params_t,
                                           *UF_DRAW_tabnot_cell_params_p_t;

/* Cell evaluated data */
struct UF_DRAW_tabnot_cell_eval_data_s
{
    double text_position[3] ;                   /* Absolute position of text */
    char *eval_text ;                           /* Evaluated cell text */
};

typedef struct UF_DRAW_tabnot_cell_eval_data_s UF_DRAW_tabnot_cell_eval_data_t,
                                             *UF_DRAW_tabnot_cell_eval_data_p_t;

/****************************************************************************
 * Creates a new tabular note object using the specified parameters.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_tabular_note(
    UF_DRAW_tabnot_params_t *params, /* <I>
                                     Tabular note parameters
                                     */
    tag_t *new_tabular_note /* <O>
                            New tabular note object
                            */
);

/***************************************************************************
 * Returns the parameters and evaluated data from a tabular note object.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.

 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_tabular_note_params(
    tag_t tabular_note, /* <I>
                        Tabular note
                        */
    UF_DRAW_tabnot_params_t *params, /* <O>
                                     Tabular note parameters
                                     */
    UF_DRAW_tabnot_eval_data_t *eval_data /* <O>
                                          Tabular note evaluated data
                                          */
);

/***************************************************************************
 * Sets the parameters of a tabular note object.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_tabular_note_params(
    tag_t tabular_note, /* <I>
                        Tabular note
                        */
    UF_DRAW_tabnot_params_t *params /* <I>
                                    New tabular note parameters
                                    */
);

/***************************************************************************
 * Returns the customer default values used for creating tabular notes.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_tabular_note_defaults(
    UF_DRAW_tabnot_params_t *params /* <O>
                                    Tabular note parameters
                                    */
);

/****************************************************************************
 * Returns the parameters and evaluated data from a tabular note cell.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_read_tabnot_cell(
    tag_t tabular_note, /* <I>
                        Tabular note from which to retrieve cell parameters
                        */
    int row, /* <I>
             Row of cell
             */
    int col, /* <I>
             Column of cell
             */
    UF_DRAW_tabnot_cell_params_t *params, /* <O>
                                          Cell parameters
                                          */
    UF_DRAW_tabnot_cell_eval_data_t *eval_data /* <O>
                                               Cell evaluated data
                                               */
);

/****************************************************************************
 * Sets the parameters of a tabular note cell.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_write_tabnot_cell(
    tag_t tabular_note, /* <I>
                        Tabular note to which to set cell parameters
                        */
    int row, /* <I>
             Row of cell
             */
    int col, /* <I>
             Column of cell
             */
    UF_DRAW_tabnot_cell_params_t *params /* <I>
                                         Cell parameters
                                         */
);

/****************************************************************************
 * Deletes a tabular note cell.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_delete_tabnot_cell(
    tag_t tabular_note, /* <I>
                        Tabular note containing cell to delete
                        */
    int row, /* <I>
             Row of cell
             */
    int col /* <I>
            Column of cell
            */
);

/****************************************************************************
 * Reads the height of a tabular note row.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_read_tabnot_row_hgt(
    tag_t tabular_note, /* <I>
                        Tabular note containing row to read
                        */
    int row, /* <I>
             Row
             */
    double *height /* <O>
                   Height of row
                   */
);

/***************************************************************************
 *  Writes the height of a tabular note row.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_write_tabnot_row_hgt(
    tag_t tabular_note, /* <I>
                        Tabular note containing row to write
                        */
    int row, /* <I>
             Row
             */
    double height /* <I>
                  New row height
                  */
);

/****************************************************************************
 * Reads the width of a tabular note column.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_read_tabnot_col_wdt(
    tag_t tabular_note, /* <I>
                        Tabular note containing column to read
                        */
    int col, /* <I>
             Column
             */
    double *width /* <O>
                  Width of column
                  */
) ;

/****************************************************************************
 * Writes the width of a tabular note column.
 *
 * Environment: Internal & External
 * See Also: 
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_write_tabnot_col_wdt(
    tag_t tabular_note, /* <I>
                        Tabular note containing column to write
                        */
    int col, /* <I>
             Column
             */
    double width /* <I>
                 Column width
                 */
);

/****************************************************************************
 * Updates a tabular note.  This function should be called after edits
 * have been made to cells which might require the cell sizes in the
 * tabular note to be updated.  This does not need to be done during
 * ordinary associative updates such as when a referenced expression
 * changes.  Such updating will occur automatically.
 *
 * Environment: Internal & External
 * See Also: 
 * See Also: See example for UF_DRAW_create_tabular_note.
 * History: This function was originally released in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_update_tabnot(
    tag_t tabular_note /* <I>
                       Tabular note to update
                       */
);

/****************************************************************************
Returns the object identifier of the parts list.  This  causes  the parts
list object to be created if necessary.

Return:
         Returns the object identifier of the parts list.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT tag_t UF_PLIST_ask_tag( void );

/*****************************************************************************
Allows you to define a field in the parts list.  A parts list is made up
of up to 14 fields, which are displayed as columns in the parts list note.

Return:
         Returns one of the following error codes:
        = 0 Success
        = 1 Object identifier is not a valid report object
        = 2 Parameter range error
        = 3 Format structure invalid

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int UF_PLIST_define_field(
tag_t obj_id ,/* <I>
              The object identifier of the parts list.
              */
int pos ,/* <I>
         Position at which to add field (between 1 and 14)
         */
const char * line_1 ,/* <I>
               Line 1 of header (131 character max.).  This line is
               displayed in the heading of the parts list to identify
               this particular field.
               */
const char * line_2 ,/* <I>
               Line 2 of header (131 character max.).  This line is
               displayed in the heading of the parts list to identify
               this particular field.  This line is directly under line_1.
               */
const char * attr_title ,/* <I>
                   Attribute title for this field. Not required for Quantity
                   fields. Must be CALLOUT for automatic callouts to work on
                   this field.  For every member of the parts list, the value
                   of this attribute from the member will be displayed in this
                   field.  This field is limited to 50 bytes.
                   */
UF_PLIST_field_format_t * f_format ,/* <I>
                                    Format Structure
                                    */
int f_width ,/* <I>
             Character width of field
             */
int f_type ,/* <I>
            Field type:
                0 = Normal field
                1 = Key Field
                2 = Quantity
            */
int p_mask  /* <I>
            Bit  mask for protecting this field from the application of fit
            rules. The following values are valid for p_mask either singly
            or in any combination:
             0       = Unset all bits; no protected fields
             2       = Sets bit 1, this field may not be truncated
             4       = Sets bit 2, do not allow overwriting into this field
             8       = Sets bit 3, only allow one field to overwrite this field
             16      = Sets bit 4, do not allow changing the character size
             32      = Sets bit 5, this field may not be converted to two lines
             64      = Sets bit 6, this field may not be abbreviated
             128     = Sets bit 7, this field must keep Leading/Trailing Strings
            */
);

/*****************************************************************************
Removes a field (column) from a parts list.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_PLIST_remove_field(
tag_t obj_id ,/* <I>
              The object identifier of the parts list.
              */
int field  /* <I>
           Field to remove (between 1-14)
           */
);

/****************************************************************************
Sets the priorities for parts list fit rules and puts the array of fit rule
priorities in the database.  Fit rules are used to get the field contents
to fit within the field width when the contents are large. This does
not cause the note to be automatically updated.

The highest priority is given to priorities[0] and the lowest priority is
given to priorities[6]. For example, to specify "Shrink the character
size" and "Remove any leading internal or trailing spaces" and
nothing else, you would set up the array as follows.
int priorities[7] = {4, 7, 0, 0, 0, 0, 0};
Fit rule 4 is used first, followed by fit rule 7.

Environment: Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_fit_rules(
tag_t obj_id ,/* <I>
              The object identifier of the parts list.
              */
int priorities[7]  /* <I>
                   An array of fit rule priorities. The number in each
                   slot indicates the priority for that fit rule. A 0
                   means do not apply the rule at all.  The  slots mean:
                      1 = Truncate the field value
                      2 = Overwrite into the following field
                      3 = Overwrite into the previous field
                      4 = Shrink the character size
                      5 = Write the value in two lines
                      6 = Abbreviate the words by removing  all of
                               the vowels except the 1st
                      7 = Remove any leading, internal, or trailing
                               spaces
                   */
);

/**************************************************************************
Sets the character sizes for the parts list fit rules and then puts the
character sizes in the data base. Fit rules are used to get the field
contents to fit within the field width when the contents are large. This
does not cause the note to be automatically updated.

Environment: Internal  and  External

See Also:  UF_PLIST_set_fit_rules.

History: Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_fit_char_sizes(
tag_t obj_id ,/* <I>
              The object identifier of the Parts List
              */
int csize_option ,/* <I>
                  bit 0 set and use ccsize value entered by user
                  bit 1 set and use standard factor 0.5
                  bit 2 set and use standard factor 0.66666666
                  bit 3 set and use standard factor 0.75
                  bit 4 set and use automatic scaling factor
                  */
int dash_option ,/* <I>
                  bit 0 set and use dcsize value entered by user
                  bit 1 set and use standard factor 0.5
                  bit 2 set and use standard factor 0.66666666
                  bit 3 set and use standard factor 0.75
                  bit 4 set and use automatic scaling factor
                  bit 15 set to insert a dash between 2 lines
                 */
double ccsize ,/* <I>
               Real scaling factor for csize option
               */
double dcsize  /* <I>
               Real scaling factor for dash option
               */
);

/*****************************************************************************
This function sets a variety of output modes that take effect the next
time the parts list is listed or that a parts list note is created/recreated.
Merely setting the values does not cause the note to change.

Return:
        Return code:
        0 = Success
        1 =  Input value out of range or object
                 identifier not a parts list.

Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_display_modes(
tag_t obj_id ,/* <I>
              The object identifier of the parts list object
              */
const char * attr_title ,/* <I>
                   Attribute title to sort on
                   */
int sort_mode ,/* <I>
               Sort mode:
                 0 = No sort
                 1 = Alphabetic
                 2 =  Reverse alphabetic
                 3 = Numeric
                 4 = Reverse numeric
               Options 3 and 4 only apply if the sort field is
               specified as real or integer.
               */
int header_mode ,/* <I>
                 Header mode:
                  0 = Header will be written above the parts list
                  1 = Header will be written below the parts list
                  2 =  No header
                 */
int callout_mode ,/* <I>
                  Callout generation:
                    1 = Letter callouts
                    2 = Reverse letter callouts
                    3 = Numeric callouts
                    4 = Reverse numeric callouts
                    5 = Manual callouts
                  In order for callouts to show up, there must be a field
                  defined with an attribute title of CALLOUT
                  */
int box_mode ,/* <I>
              Box mode:
                0 = No boxes
                1 = Add boxes to parts list
              */
int report_mode ,/* <I>
                 Report mode - reserved for future use
                 */
int symbol_mode ,  /* <I>
                   ID symbol update mode:
                   Specifies whether to automatically update ID
                   symbols of a given type attached to parts list
                   members to reflect the new values generated from
                   any changed callouts.
                           0 = NO_UPDATE
                           1 = update CIRCLE ID symbols only
                           2 = update DIVIDED_CIRCLE ID symbols only
                           3 = update SQUARE ID symbols only
                           4 = update DIVIDED_SQUARE ID symbols only
                           5 = update HEXAGON ID symbols only
                           6 = update DIVIDED_HEXAGON ID symbols only
                           7 = update TRIANGLE_POINT_UP ID symbols only
                           8 = update TRIANGLE_POINT_DOWN ID symbols only
                           9 = update DATUM_TARGET ID symbols only
                          10 = update OBLONG_BOX ID symbols only
                   */
double line_space  /* <I>
                   Line space factor:
                   This factor is applied to the normal line space
                   factor for the font. It can be adjusted in conjunction
                   with the two lines fit rule and the character size for
                   that fit rule to prevent one line from overwriting
                   another.
                   */
);

/******************************************************************************
Sets the second sort field for a parts list. This takes effect the next
time the parts list is listed or that a parts list note is created or
recreated. Just setting the values does not cause the note to change.
The second sort field can only be specified if there is a first sort field
and the second may not be the same as the first.

Return:
        Return code:
        0 = Success
        1 = Input values incorrect, out of range, or
                 obj_id is not a parts list.

Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_second_sort(
tag_t obj_id ,/* <I>
              The object identifier of the parts list.
              */
const char * attr_title ,/* <I>
                   Attribute title on which to perform second sort
                   */
int smode2  /* <I>
            Second sort mode:
               0 = No sort
               1 = Alphabetic
               2 = Reverse alphabetic
               3 = Numeric
               4 = Reverse numeric
            Options 3 and 4 only apply if the sort field is
            specified as real or integer.
            */
);

/*****************************************************************************
Sets parameters for multiple column parts list. These take effect the
next time that the parts list is listed or when the parts list note is
created or recreated. Just setting the values does not cause the note to
change.  The columns mentioned here should not be confused with a
parts list field.

If rowmax = 0, it is not an error to specify the other parameters;
however, they have no effect.

Return:
         Return code:
        0 = Success
        1 = Input value out of range or obj_id not a
            parts list

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_column_modes(
tag_t obj_id ,/* <I>
              The object identifier of the parts list
              */
int rowmax ,/* <I>
            Maximum rows per column, 0 means single column
            */
int rowpos ,/* <I>
            Position or header for second and subsequent
            columns:
             -2 = Left with no header
             -1 = Left with header
              1 = Right with header
              2 = Right with no header
            */
int rowgap  /* <I>
            Gap between multiple columns, measured in
            character widths
            */
);

/****************************************************************************
Sets the Report Mode setting to one of the allowed values. This takes
effect the next time the parts list is listed or that a parts list note is
created or recreated. Just setting the values does not cause the note to
change.

Return:
         Return code:
        0 = Success
        1 = Input value out of range or obj_id not a
            parts list

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_report_mode(
tag_t obj_id ,/* <I>
              The object identifier of the parts list
              */
int value  /* <I>
           Report Mode setting:
           UF_PLIST_AS_DEFINED - parts list note is
                                 created as currently stored.
           UF_PLIST_SINGLE - parts list note is created
                             with top level children only.
           UF_PLIST_MULTIPLE - parts list is created with
                               all levels.
           */
);

/****************************************************************************
Sets the Skip One Level setting to one of the allowed values. This
takes effect the next time the parts list is listed or that a parts list note
is created or recreated. Just setting the values does not cause the note
to change.

Return:
         Return code:
        0 = Success
        1 = Input value out of range or obj_id not a
                parts list

Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_skip_level(
tag_t obj_id ,/* <I>
              The object identifier of the parts list
              */
int value  /* <I>
           Skip One Level:
              0 = Parts list note is created as currently stored.
              1 = Parts list note is created as if the single, top
                  level child of the displayed part were the
                  displayed part.
           */
);

/******************************************************************************
Sets the Frozen Level setting to one of the allowed values. This takes
effect the next time the parts list is listed or that a parts list note is
created or recreated. Just setting the values does not cause the note to
change.

Return:
         Return code:
        0 = Success
        1 = Input value out of range or obj_id not a
                parts list

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_frozen_level(
tag_t obj_id ,/* <I>
              The object identifier of the parts list
              */
int value  /* <I>
           Frozen Level (row number for current sorted list):
            0 = No rows are frozen (unfreeze all)
            < Maximum row number && > 0 = All rows
                 are frozen up to and including value.
            >= Maximum row number = All rows are
                 frozen
           */
);

/*****************************************************************************
Add a list of objects to the parts list. The quantity for each object is
set to 1. The parts list object identifier can be obtained from
UF_PLIST_ask_tag.

Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT int UF_PLIST_add_entities(
tag_t obj_id ,/* <I>
              The object identifier of the parts list.
              */
int num_to_add ,/* <I>
                Count of objects to add to parts list.
                */
tag_t objects[]  /* <I,len:num_to_add>
                 Array of objects to add
                 */
);

/****************************************************************************
Remove a list of objects from the parts list. The parts list object
identifier can be obtained from UF_PLIST_ask_tag.

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int UF_PLIST_remove_entity(
tag_t obj_id ,/* <I>
              The object identifier of the parts list.
              */
int num_to_add ,/* <I>
                Count of objects to remove from the parts list.
                */
tag_t objects[]  /* <I,len:num_to_add>
                 Array of objects to remove from the parts list.
                 */
);

/****************************************************************************
Creates a parts list note, if it does not already exist, at the input
position. If the note already exists, then the note is regenerated and
the object identifier for the note is returned.

Return:
         Return code:
        0       = Success
        1       = No parts list members
        2       = No key or quantity field defined
        > 2     = Some other parts list output error

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_PLIST_create_note(
tag_t obj_id ,/* <I>
              The object identifier of the parts list.
              */
double position[3] ,/* <I>
                    Position of note, used for create only.
                    */
tag_t * note_obj_id  /* <O>
                     Returned object identifier of parts list note
                     */
);

/****************************************************************************
Returns the identifier of the parts list note.
NOTE: If you require a drafting regeneration and you transform or
change font on the note, the parts list boxes disappear. You can regain
them by using UF_PLIST_create_note to recreate the note.

Return:
         Object identifier of parts list note

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT tag_t UF_PLIST_ask_tag_of_note(
tag_t obj_id  /* <I>
              The object identifier of the parts list
              */
);

/*****************************************************************************
The following load option will be obsoleted in NX 3.

Please use UF_ASSEM_ask_last_filter to get the last used
filter or cset in the part file followed by UF_FLTR_evaluate_filter or
UF_PART_open_cset to open the assembly with the filter or cset.

 *****************************************************************************/
#define UF_ASSEM_use_last_filter        3

/* uc6573 add/append character data to a generic entity
   -- replaced by UF_UDOBJ_add_strings */
/* This function only works on ASCII data and will be made obsolete in NX12. */
extern UFUNEXPORT int uc6573(tag_t np1, int jp2, char cp3[][133]/* <I,len:jp2>*/);

/* uc6578 read character data from a generic entity
   -- replaced by UF_UDOBJ_ask_udo_data */
/* This function only works on ASCII data and will be made obsolete in NX12. */
extern UFUNEXPORT int uc6578(tag_t np1, int jp2, int jp3, char cr4[][133]/* <I/O,len:jp2>*/);

/* uc6582 modify character data in a generic entity
   -- replaced by UF_UDOBJ_ask_udo_data
      and UF_UDOBJ_edit_strings */
/* This function only works on ASCII data and will be made obsolete in NX12. */
extern UFUNEXPORT int uc6582(tag_t np1, int jp2, int jp3, char cp4[][133]/* <I,len:jp3>*/);

/* uf6586 set/reset a generic entity modified
   -- replaced by UF_UDOBJ_clear_udo_status */
/* This function only works on ASCII data and will be made obsolete in NX12. */
extern UFUNEXPORT void uf6586(const tag_t *np1, const int *ip2, int *ir3);


/*****************************************************************************
Converts the given internal part name into a display name in the same
format as would be used by NX for menus, banners and etc. This
function accepts a CLI format name as well as an internal format
name, for NX Manager names.
e.g.,   From:   "@DB/peters-part/A/spec/sheet1" (cli format)
                                or
        From:   "%UGMGR=3.2 PN=Peters..." (internal format)
        To:     "peters-part/A (spec: sheet1)" (display format)

Environment: Internal  and  External

See Also:  UF_PART_ask_tag_of_disp_name.
          
History:
This function should be replaced with UF_PART_file_name_for_display from NX 5.0
and is mandatory if Longer IDs functionality is enabled NX/Manager
 ******************************************************************************/
extern UFUNEXPORT int UF_PART_name_for_display
(
    const char *name_format,                     /* <I>
                                                 Command Line Input format,
                                                 e.g.,
                                                 "@DB/peters-part/A/spec/sheet1"
                                                  or Internal format
                                                 "%UGMGR=3.2 PN=Peters..."
                                                 */
    char       display_name[ MAX_FSPEC_BUFSIZE ]   /* <O>
                                                  Display format
                                                  "peters-part/A (spec: sheet1)"
                                                  */
);
/*****************************************************************************
Attempts to find a part whose displayed name matches the input and
returns its tag if found and NULL_TAG if no matching part is found.
A typical application for this routine could be for times when the
Open API application needs to display lists of parts in a menu for
the user to select.

Environment: Internal  and  External

See Also: UF_PART_file_name_for_display
          
History:
Deprecated in NX10.0

This API will not work anymore as NX now honors the display name format specified
by Teamcenter. This means the display names for parts may not be unique any more.
Use UF_PART_ask_part_tag with CLI name instead.
 ******************************************************************************/
extern UFUNEXPORT int UF_PART_ask_tag_of_disp_name(
const char *display_name,/* <I>
                         Display format "peters-part/A (spec: sheet1)"
                         */
tag_t *part_tag  /* <O>
                 Tag to display_name.
                 */
);

/******************************************************************************
Decodes the specified NX Manager part file name into its constituent
elements - the part number, part revision, part file type, and part file
name. If a particular element is not present in the encoded input
string, the corresponding output argument is the empty string "".
The encoded_name input argument can be any one of the following:

An internal form string such as that returned from the function
UF_UGMGR_encode_part_filename or other functions that
return part filenames (e.g. UF_PART_ask_part_name).

A command line input form string such as that returned from
UF_UGMGR_convert_name_to_cli.

A string input by a user of a Open API program.

Environment: Internal  and  External

See Also:
 UF_UGMGR_encode_part_filename
 UF_UGMGR_convert_name_to_cli


History:
This function should be replaced with UF_UGMGR_decode_part_file_name from NX 5.0
and is mandatory if Longer IDs functionality is enabled NX/Manager.

This function only works on ASCII data and will be made obsolete in a later release.
******************************************************************************/
extern UFUNEXPORT int UF_UGMGR_decode_part_filename(
char encoded_name[ MAX_FSPEC_BUFSIZE ] ,/* <I>
                     Encoded form of the part file name. Declare
                     this parameter with array size
                     MAX_FSPEC_BUFSIZE.
                     */
char part_number[UF_UGMGR_PARTNO_BUFSIZE] ,/* <O>
                    Part number. Declare this parameter with array
                    size UF_UGMGR__PARTNO_BUFSIZE.
                    */
char part_revision[UF_UGMGR_PARTREV_BUFSIZE] ,/* <O>
                      Part revision. Declare this parameter with array
                      size UF_UGMGR_PARTREV_BUFSIZE.
                      */
char part_file_type[UF_UGMGR_FTYPE_BUFSIZE] ,/* <O>
                       Part file type. Declare this parameter with array
                       size UF_UGMGR_FTYPE_BUFSIZE.
                       */
char part_file_name[UF_UGMGR_FNAME_BUFSIZE]  /* <O>
                       Part file name. Declare this parameter with
                       array size UF_UGMGR_FNAME_BUFSIZE.
                       */
);

/*******************************************************************************
Converts a part name from the internal format to the command line
input format. This routine is a null operation if not running
NX Manager.
e.g.,   From: "%UGMGR=3.2 PN=Peters-part -PRN=A..."
        To:     "@DB/peters-part/A/spec/sheet1"

Environment: Internal  and  External

See Also:


History:
This function should be replaced with UF_UGMGR_convert_name_to_cli from NX 5.0
and is mandatory if Longer IDs functionality is enabled NX/Manager
 *****************************************************************************/
extern UFUNEXPORT int UF_UGMGR_convert_name_to_cli(
const char * internal_name ,/* <I>
                            Internal format "%UGMGR=3.2
                            PN=Peters-part -PRN=A..."
                            */
char cli_name[ MAX_FSPEC_BUFSIZE ]  /* <O>
                          Command Line Input format, e.g.,
                          "@DB/peters-part/A/spec/sheet1"
                          */
);


/******************************************************************************
Sets the distance tolerance found in the Modeling Preferences dialog box.
This function is retired. This function has been replaced with UF_MODL_set_distance_tolerance_of_part.
Return:
      Void.
Environment: Internal  and  External
See Also:
History:
    Deprecated in NX1953
 ******************************************************************************/
extern UFUNEXPORT void UF_MODL_set_distance_tolerance(
double * tolerance ,/* <I>
                    Distance tolerance. Value must be greater than
                    metric 1e-5 or English 3e-7.
                    */
int * err_flag  /* <EC>
                Error code:
                0 = No error
                1 = Invalid value, tolerance not changed
                */
);

/******************************************************************************
Sets the angle tolerance found in the Modeling Preferences dialog box.
This function is retired. This function has been replaced with UF_MODL_set_angle_tolerance_of_part.
Return:
       Void.
Environment: Internal  and  External
See Also:
History:
    Deprecated in NX1953
 *****************************************************************************/
extern UFUNEXPORT void UF_MODL_set_angle_tolerance(
double * tolerance ,/* <I>
                    Angle tolerance. Value must be greater than e-10
                    (greater than zero).
                    */
int * err_flag  /* <EC>
                Error code:
                0 = No error
                1 = Invalid value, tolerance not changed
                */
);

/******************************************************************************
Gets the distance tolerance found in the Modeling Preferences dialog
box. This value is in the units of the part.
This function is retired. This function has been replaced with UF_MODL_ask_distance_tolerance_of_part.

Return:
       Void.

Environment: Internal  and  External
See Also:
History:
    Deprecated in NX1953
 ******************************************************************************/
extern UFUNEXPORT void UF_MODL_ask_distance_tolerance(
double * tolerance  /* <O>
                    Distance tolerance
                    */
);

/******************************************************************************
Gets the angle tolerance found in the Modeling Preferences dialog
box. The angle tolerance is returned in degrees.
This function is retired. This function has been replaced with UF_MODL_ask_angle_tolerance_of_part.
Return:
      Void.
Environment: Internal  and  External
See Also:
History:
    Deprecated in NX1953
 ******************************************************************************/
extern UFUNEXPORT void UF_MODL_ask_angle_tolerance(
double * tolerance  /* <O>
                    Angle tolerance (in degrees)
                    */
);


/******************************************************************************
Thickens the input sheet body based on the offsets specified. The
routine creates expressions for each of the offsets created.

This function is retired. This function has been replaced with Journamation support.


Environment: Internal  and  External
See Also: 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_thicken_sheet(
tag_t sheet_body_tag ,/* <I>
                      Object identifier of the sheet body to be thickened.
                      */
char * first_offset ,/* <I>
                     The offset from the face(s) of the input sheet body
                     that one side of the resultant solid body should be.
                     If positive the offset is applied in the direction of
                     the sheet face normal, if negative the offset is
                     applied in the direction opposite to the sheet face
                     normal.
                     */
char * second_offset ,/* <I>
                      The offset from the face(s) of the input sheet body
                      that the other side of the resultant body should be.
                      If positive the offset is applied in the direction of
                      the sheet face normal, if negative the offset is
                      applied in the direction opposite to the sheet face
                      normal.
                      */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new solid body
                      UF_POSITIVE   = add to active solid body
                      UF_NEGATIVE = subtract from active solid body
                      UF_UNSIGNED = intersect with active solid body
                      */
tag_t * thicken_sheet_tag  /* <O>
                           Object identifier for the thicken sheet feature.
                           */
);

/******************************************************************************
This routine retrieves the parameters used to thicken a sheet body.

This function is retired. This function has been replaced with Journamation support.

Environment: Internal  and  External
See Also: 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_thicken_sheet_parms(
tag_t thicken_sheet_tag ,/* <I>
                         Object identifier for the thicken sheet feature.
                         */
tag_t * sheet_tag ,/* <O>
                   Object identifier of the sheet body that was
                   thickened.
                   */
char ** first_offset ,/* <OF>
                      The value of the offset from the face(s) of the input
                      sheet body that one side of the resultant solid body
                      was. If positive the offset was applied in the
                      direction of the sheet face normal, if negative the
                      offset was applied in the direction opposite to the
                      sheet face normal. Free the memory allocated for
                      this output by calling UF_free(first_offset).
                      */
char ** second_offset  /* <OF>
                       The value of the offset from the face(s) of the input
                       sheet body that the other side of the resultant body
                       was. If positive the offset was applied in the
                       direction of the sheet face normal, if negative the
                       offset was applied in the direction opposite to the
                       sheet face normal. Free the memory allocated for
                       this output by calling UF_free(second_offset).
                       */
);

/******************************************************************************
This routine changes the parameters used to thicken a sheet body.

This function is retired. This function has been replaced with Journamation support.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_redefine_thicken_sheet(
       tag_t thicken_sheet_tag,  /* <I>
                                 Object identifier for the thicken sheet feature
                                 */
       char *first_offset,       /* <I>
                                 String containing first offset value
                                 */
       char *second_offset,      /* <I>
                                 String containing second offset value
                                 */
       tag_t sheet_body_tag,     /* <I>
                                 New sheet body to be thickened.  If NULL then
                                 the present sheet body will be used.
                                 */
       tag_t target_body_tag     /* <I>
                                 New target body.  If  NULL then the present
                                 target body will be used.
                                 */
);

/**************************************************************************
Read Drafting Object Text Data:
This routine deciphers the ann_data returned from UF_DRF_ask_ann_data and
returns just one text string. This routine can be called once for each
text string (or segment) in the data block.  The number of segments
is returned by UF_DRF_ask_ann_data.

Please use new user function UF_DRF_ask_text_data which avoids buffer overflow
by dynamically allocating output string.

Environment: Internal  and  External

See Also:  UF_DRF_ask_ann_data

History:
 *************************************************************************/
extern UFUNEXPORT int uc5574(
int ip1 ,/* <I>
         Segment Number
         1 < ip1 < = num_segments returned by UF_DRF_ask_ann_data
         */
int * ann_data ,/* <I/O>
                Array of ann_data returned by UF_DRF_ask_ann_data
                */
char cr3[ MAX_LINE_BUFSIZE ] ,/* <O>
            Text String
            */
int * ir4 ,/* <O>
           Length of Line in 1/64th's Character Size, Expressed in Integers
           */
int * ir5  /* <O>
           Number of Characters in String
           */
);

/******************************************************************************
     Queries the data from a Product Definition.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_attribues(
    tag_t product_definition,                         /* <I>
                                                        Tag of the product
                                                        definition object to
                                                        query. Must be of type
                                                        UF_smsp_product_definition_type
                                                        and subtype
                                                        UF_smsp_product_attribute_subtype
                                                      */
    tag_p_t *product_attributess,    /* <OF,len:num_product_attributes> Product attributes */
    int *num_product_attributes      /* <O>  Number of product attributes */

);

/******************************************************************************
     Queries the data from a Product Definition Attribute.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_attribue_data(
    tag_t attribute,                            /* <I>
                                                   Tag of the product
                                                   definition object to
                                                   query. Must be of type
                                                   UF_smsp_product_definition_type
                                                   and subtype
                                                   UF_smsp_product_attribute_subtype
                                                */
    UF_PD_product_attribute_p_t attribute_data /* <O> Data of Product attributes */
);

/******************************************************************************
     Queries the attribute value data from a Product Definition Attribute Value.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_attribue_value_data(
    tag_t attribute_value,                     /* <I>
                                                  Tag of the product
                                                  definition object to
                                                  query.
                                               */
    UF_PD_attribute_value_p_t value_data     /* <O> Data of Product attributes */
);

/******************************************************************************
     Queries the data from a Product Definition Attribute.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History:
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_attribue_data_2(
    tag_t attribute,                            /* <I>
                                                   Tag of the product
                                                   definition object to
                                                   query. Must be of type
                                                   UF_smsp_product_definition_type
                                                   and subtype
                                                   UF_smsp_product_attribute_subtype
                                                */
    UF_PD_product_attribute_2_p_t attribute_data /* <O> Data of Product attributes */
);

/******************************************************************************
Returns the direction vector which is opposite of offset direction vector
and direction vector which is in the draft direction vector for a string of curves.

This function is retired. This function has been replaced with UF_CURVE_ask_offset_direction_2
which gives offset direction vector and the draft direction vector for a string of curves.

Environment: Internal  and  External
See Also:
History:This function was modified in V13.0 to add the base_point parameter.
 ******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_offset_direction(
UF_STRING_p_t input_curves ,/* <I>
                            Pointer to curves list structure
                               int num         Total number of primary strings
                                               (min=1,max=1)
                               int string[]    Total number of segment curves/
                                               sketch id of each primary string
                                               (min=1,max=402)
                               int dir[]       Direction of each primary string
                                                  1 = Start to End
                                                 -1 = End to Start
                               tag_t id[]      Identifier of primary curves
                            Use UF_MODL_init_string_list and
                            UF_MODL_create_string_list
                            to create input strings. Use
                            UF_MODL_free_string_list to free
                            memory after the string is created.
                            */
double offset_direction_vector[3] ,/* <O>
                                   direction vector which is opposite of offset direction vector
                                   */
double draft_direction_vector[3] ,/* <O>
                                  positive draft height direction
                                  */
double base_point[3]  /* <O>
                      base point of vectors
                      */
);

/*******************************************************************************
 * Queries the work plane emphasis dim color attribute, which is obsolete
 * in NX 6.0. This function is retired and there is no replacement.
 * Environment: Internal  and  External
 * See Also:
 * History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_work_plane_dim_clr(
                       int * color        /* <O> Emphasis dim color. */
);

/*******************************************************************************
 * Sets the work plane emphasis dim color attribute, which is obsolete
 * in NX 6.0. This function is retired and there is no replacement.
 * Environment: Internal  and  External
 * See Also:
 * History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DISP_set_work_plane_dim_clr(
                        int dim_color     /* <I> Emphasis dim color.  */
);

/*In NX 8.5.this struct is retired and there is no replacement.*/
struct UF_CURVE_analysis_display_s
{
    double  curvature_comb_scale_factor;  /* Scale factor to apply to
                                             curvature combs -
                                             1.0 is normal.  This may be
                                             negative */
    logical show_control_polygon;         /* Visible only for splines */
    logical show_curvature_comb;          /* Visible for arcs, conics and
                                             splines */
    logical show_inflections;             /* Visible only for splines */
    logical show_peaks;                   /* Visible only for conics and
                                             splines */
    logical show_knots;                   /* Visible only for splines*/
    double  comb_density;                 /* The input teeth of curvature combs */
    int     comb_interneedle_density;     /* Visibile for arcs, conics and splines*/
    double  ustart;                       /* The specified start  parameter, range from 0 - 100*/
    double  uend;                         /* The specified end  parameter, range from 0 - 100 */
    logical use_max_length;               /* Control if limit the max length to combs, true: use max length, otherwise false */
    double  max_length;                   /* The length to limit  combs */
    int     proj_choice;                  /*  none=0, plane of curve=1, specified direction=2, work  view=3 */
    double  specified_dir[3];             /*  Vector to show which direction the combs will apply to */
};

typedef struct UF_CURVE_analysis_display_s UF_CURVE_analysis_display_t,
*UF_CURVE_analysis_display_p_t;

/****************************************************************************
 * Returns the values of the Curve Analysis Display Options of
 * a line, circle, conic or spline
 * Retired in NX8.5. Use GeometricAnalysis.CurveCurvatureAnalysis object.
 * Environment: Internal and External
 * UF_CURVE_ask_analysis_display
 * See Also: UF_CURVE_ask_spline_sap
    UF_CURVE_set_analysis_display
 *
 * History:  Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_analysis_display(
tag_t curve_tag ,/* <I>
                    The tag of the curve.  The curve may be of type
                    UF_line_type, UF_circle_type, UF_conic_type or
                    UF_spline_type.
                 */
UF_CURVE_analysis_display_p_t analysis_display_options /* <O>
                                                          The current options
                                                          for curve analysis
                                                          display
                                                        */
);

/****************************************************************************
 * Sets the values of the Curve Analysis Display Options of
 * a line, circle, conic or spline
 * Retired in NX8.5. Use GeometricAnalysis.CurveCurvatureAnalysis object.
 * Environment: Internal and External
 *
 * See Also: UF_CURVE_set_spline_sap
   UF_CURVE_ask_analysis_display
 *
 * History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_CURVE_set_analysis_display(
tag_t curve_tag ,/* <I>
                    The tag of the curve.  The curve may be of type
                    UF_line_type, UF_circle_type, UF_conic_type or
                    UF_spline_type.
                 */
UF_CURVE_analysis_display_p_t analysis_display_options  /* <I>
                                                           The new options for
                                                           curve analysis
                                                           display
                                                        */
);

/****************************************************************************
Returns the values of the Shape Analysis Parameters (SAP) of a
B-curve. Shape Analysis Parameters are a set of parameters used to
display B-curves characteristics. The current SAP includes four
integer flags used to indicate the display status of the control polygon,
curvature comb, inflection points and peak points of a B-curve, and a
real value used to scale the teeth length of the curvature comb.

Please use UF_CURVE_ask_analysis_display instead of UF_CURVE_ask_spline_sap,
as UF_CURVE_ask_spline_sap will eventually become obsolete.
Retired in NX8.5. Use GeometricAnalysis.CurveCurvatureAnalysis object.
Environment: Internal  and  External

See Also: UF_CURVE_set_spline_sap
          UF_CURVE_ask_analysis_display

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_spline_sap(
tag_t curve_tag ,/* <I>
                 B-curves tag
                 */
int display_flag[4] ,/* <O>
                     B-curves SAP values
                     [0]= control polygon display flag
                     [1]= curvature comb display flag
                     [2]= inflection points display flag
                     [3]= peak points display flag
                     */
double * scale_factor  /* <O>
                       B-curves SAP value
                       */
);

/****************************************************************************
Sets the values of the Shape Analysis Parameters (SAP) of a B-curve
(Please refer to UF_CURVE_ask_spline_sap for explanation of Shape
Analysis Parameters).

Please use UF_CURVE_set_analysis_display instead of UF_CURVE_set_spline_sap,
as UF_CURVE_set_spline_sap will eventually become obsolete.

NOTE: This routine only sets B-curves SAP values. Users have to
call display routines afterwards to see the appearance change.
Retired in NX8.5. Use GeometricAnalysis.CurveCurvatureAnalysis object.
Environment: Internal  and  External

See Also: UF_CURVE_ask_spline_sap

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CURVE_set_spline_sap(
tag_t curve_tag ,/* <I>
                 B-curves tag
                 */
int display_flag[4] ,/* <I>
                     B-curves SAP values
                     [0]= control polygon display flag
                     [1]= curvature comb display flag
                     [2]= inflection points display flag
                     [3]= peak points display flag
                     */
double scale_factor  /* <I>
                     B-curves SAP value
                     */
);

/****************************************************************************
All UF_CLEAR functions (for Clearance Analysis) now become deprecated starting in NX9.0.
Users should start using Clearance Analysis builder and JA functions for NXOpen
programming.
****************************************************************************/

/*******************************************************************************
                                  ** Macros **
 ******************************************************************************/

#define UF_CLEAR_BIT(n)                 ( 1 << ((n) - 1) )

/*******************************************************************************
                                ** Constants **
 ******************************************************************************/

/*******************************************************************************
                                  Error codes

The following module specific failure codes can be returned by the
UF_CLEAR routines.

*******************************************************************************/
#define UF_CLEAR_ERROR_BASE             ERROR_CLEAR_base

/* An attempt has been made to create a data set
      with the name of an existing data set. */
#define UF_CLEAR_err_name_exists        ( UF_CLEAR_ERROR_BASE + 1 )
/* The named data set cannot be found. */
#define UF_CLEAR_err_cant_find_dataset  ( UF_CLEAR_ERROR_BASE + 2 )
#define UF_CLEAR_err_not_clranl_obj     ( UF_CLEAR_ERROR_BASE + 3 )
/* An invalid object list number has been supplied.
   The list number must be 1 or 2. */
#define UF_CLEAR_err_bad_list_num       ( UF_CLEAR_ERROR_BASE + 4 )
#define UF_CLEAR_err_no_work_part       ( UF_CLEAR_ERROR_BASE + 5 )
#define UF_CLEAR_err_cant_find_point    ( UF_CLEAR_ERROR_BASE + 6 )
/* The tag (or tags) specified does not define a valid interference. */
#define UF_CLEAR_err_bad_interf         ( UF_CLEAR_ERROR_BASE + 7 )
/* The two object tags do not define a valid pair. */
#define UF_CLEAR_err_bad_pair           ( UF_CLEAR_ERROR_BASE + 8 )
#define UF_CLEAR_err_bad_num_zones      ( UF_CLEAR_ERROR_BASE + 9 )
/* The tag specified was not a valid part. */
#define UF_CLEAR_err_bad_part           ( UF_CLEAR_ERROR_BASE + 10 )
#define UF_CLEAR_err_sheet_intersect    ( UF_CLEAR_ERROR_BASE + 11 )
/* An error occurred during analysis. */
#define UF_CLEAR_err_analysis_error     ( UF_CLEAR_ERROR_BASE + 12 )
/* A faceting error occurred during analysis. */
#define UF_CLEAR_err_facet_err          ( UF_CLEAR_ERROR_BASE + 13 )
#define UF_CLEAR_err_obj_not_avail      ( UF_CLEAR_ERROR_BASE + 14 )
/* The tag specified was not a valid clearance analysis data set. */
#define UF_CLEAR_err_bad_dataset        ( UF_CLEAR_ERROR_BASE + 15 )
/* An invalid copy mode parameter was supplied to a routine. */
#define UF_CLEAR_err_bad_copy_mode      ( UF_CLEAR_ERROR_BASE + 16 )
/* The text supplied is invalid (either too long or zero length). */
#define UF_CLEAR_err_bad_string         ( UF_CLEAR_ERROR_BASE + 17 )
/* A null pointer has been passed to a routine. */
#define UF_CLEAR_err_null_pointer       ( UF_CLEAR_ERROR_BASE + 18 )
/* The object list type parameter is nvalid. */
#define UF_CLEAR_err_bad_list_type      ( UF_CLEAR_ERROR_BASE + 19 )
/* The analysis mode supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_analysis_mode  ( UF_CLEAR_ERROR_BASE + 20 )
/* The tag specified does not refer to a valid expression. */
#define UF_CLEAR_err_bad_expression     ( UF_CLEAR_ERROR_BASE + 21 )
/* The data in an object list is invalid. */
#define UF_CLEAR_err_bad_list_data      ( UF_CLEAR_ERROR_BASE + 22 )
/* The exclusion rule supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_exclude_rules  ( UF_CLEAR_ERROR_BASE + 23 )
/* The message filter supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_msg_filter     ( UF_CLEAR_ERROR_BASE + 24 )
/* The layer number supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_layer          ( UF_CLEAR_ERROR_BASE + 25 )
/* The color index supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_color          ( UF_CLEAR_ERROR_BASE + 26 )
/* The data set in question does not contain any analysis results. */
#define UF_CLEAR_err_no_results         ( UF_CLEAR_ERROR_BASE + 27 )

/*
  These constants are used as masks for the interactive_msg_filter field.
  They are also used in the UF_CLEAR_interfere structure for the type field.
*/
#define UF_CLEAR_NO_INTERFERENCE                0
#define UF_CLEAR_SOFT_INTERFERENCE              UF_CLEAR_BIT(1)
#define UF_CLEAR_TOUCH_INTERFERENCE             UF_CLEAR_BIT(2)
#define UF_CLEAR_HARD_INTERFERENCE              UF_CLEAR_BIT(4)
#define UF_CLEAR_CONT_1_IN_2_INTERFERENCE       UF_CLEAR_BIT(5)
#define UF_CLEAR_CONT_2_IN_1_INTERFERENCE       UF_CLEAR_BIT(6)
#define UF_CLEAR_NEW_INTERFERENCE               UF_CLEAR_BIT(8)

/*
  These constants are used to define the analysis mode.  Note do not
  use the first four (UF_CLEAR_SOLID_BASED, UF_CLEAR_FACET_BASED,
  UF_CLEAR_EXHAUSTIVE_FACET_MODE, or UF_CLEAR_BEST_AVAILABLE_BASED).
  They are used to define the next five (described below)
  which are to be used by users.
*/
#define UF_CLEAR_SOLID_BASED            UF_CLEAR_BIT(1)
#define UF_CLEAR_FACET_BASED            UF_CLEAR_BIT(2)
#define UF_CLEAR_EXHAUSTIVE_FACET_MODE  UF_CLEAR_BIT(3)
#define UF_CLEAR_BEST_AVAILABLE_BASED   UF_CLEAR_BIT(4)

/*
  UF_CLEAR_QUICK_FACET is the fastest clearance analysis mode.  It uses
      existing facetted representations where possible, and generates
      temporary facetted representations of solid bodies that don?t have
      a facetted representation loaded.  It maps into the interactive mode
      Facet Based.
*/
#define UF_CLEAR_QUICK_FACET            UF_CLEAR_FACET_BASED
/*
  UF_CLEAR_FULL_FACET use of this mode is generally discouraged.  It is a
      legacy analysis mode that had a special meaning in the pre-V18
      clearance analysis application which has been largely lost in the
      re-implemented functionality.  In the current system, it will perform
      a slightly more exhaustive analysis than the quick facet mode (and
      therefore will be a little more resource intensive), but in most if
      not all cases will yield the same results as UF_CLEAR_QUICK_FACET.
      It also maps into the interactive mode Facet Based.
*/
#define UF_CLEAR_FULL_FACET             ( UF_CLEAR_FACET_BASED | UF_CLEAR_EXHAUSTIVE_FACET_MODE )
/*
  UF_CLEAR_FACET_SOLID will perform analysis based on loaded solids where
      possible, but will fall back on analyzing facetted representations
      where they are loaded instead of solids.  Solid analysis is slower,
      so depending on the mix of facets and solids that are loaded in the
      session, the performance of UF_CLEAR_FACET_SOLID will fall somewhere
      between the performance of UF_CLEAR_QUICK_FACET and UF_CLEAR_SOLID.
      This mode maps into the interactive mode Use Solids Where Available.
*/
#define UF_CLEAR_FACET_SOLID            ( UF_CLEAR_FACET_BASED | UF_CLEAR_SOLID_BASED )
/*
  UF_CLEAR_SOLID is the most accurate and slowest analysis mode.  It does
      analysis based on solid bodies exclusively.  In cases where solid
      data is not loaded, demand loading will occur so that the analysis
      can be performed.  This maps to the interactive mode Use Solids.
*/
#define UF_CLEAR_SOLID                  UF_CLEAR_SOLID_BASED
#define UF_CLEAR_BEST_AVAILABLE         ( UF_CLEAR_FACET_SOLID | UF_CLEAR_BEST_AVAILABLE_BASED )

/*
  These constants are used to define the types of object lists.
  A negative value is used for list2 if it is not used.
*/
#define UF_CLEAR_ALL_OBJECTS            1
#define UF_CLEAR_ALL_BUT                2
#define UF_CLEAR_FIXED_LIST             4
#define UF_CLEAR_ALL_VISIBLE_OBJECTS    5
#define UF_CLEAR_LIST2_NOT_USED         ( -1 )

/*
  These constants are used to define the source of a clearance zone.
*/
#define UF_CLEAR_USING_DEFAULT_CZ       0
#define UF_CLEAR_USING_DEFINED_CZ       1
#define UF_CLEAR_USING_OBJ1_CZ          2
#define UF_CLEAR_USING_OBJ2_CZ          3
#define UF_CLEAR_USING_PAIR_CZ          4

/*
  These constants are used to define the exclusion rules.
*/
#define UF_CLEAR_EXCLUDE_WITHIN_COMP    UF_CLEAR_BIT(2)
#define UF_CLEAR_EXCLUDE_WITHIN_GROUP   UF_CLEAR_BIT(3)
#define UF_CLEAR_EXCLUDE_WITHIN_PART    UF_CLEAR_BIT(4)

/*
  This exclusion rule is no longer supported and should not be used.
  At runtime an error will occur if it is used.
*/
#define UF_CLEAR_EXCLUDE_MATING_PAIRS   UF_CLEAR_BIT(1)

/*
  These constants specify why a job was aborted.
*/
#define UF_CLEAR_NOT_ABORTED            0
#define UF_CLEAR_ABORTED_BY_USER        1
#define UF_CLEAR_ABORTED_ON_ERROR       2

/*
  These constants specify the reason for inclusion/exclusion.
*/
#define UF_CLEAR_EXCL_NO_REASON         0
#define UF_CLEAR_EXCL_USER_DEF          UF_CLEAR_BIT(1)
#define UF_CLEAR_EXCL_SAME_COMP         UF_CLEAR_BIT(2)
#define UF_CLEAR_EXCL_SAME_GROUP        UF_CLEAR_BIT(3)
#define UF_CLEAR_EXCL_MATED_COMP        UF_CLEAR_BIT(4)
#define UF_CLEAR_EXCL_SAME_PART         UF_CLEAR_BIT(5)
#define UF_CLEAR_EXCL_COMP_SUPPRESSED   UF_CLEAR_BIT(6)
#define UF_CLEAR_EXCL_NON_GEOM          UF_CLEAR_BIT(7)
#define UF_CLEAR_EXCL_UNIT_SUBASSY      UF_CLEAR_BIT(8)

/*
  These constants specify how results should be handled when copying a dataset.
*/
#define UF_CLEAR_COPY_NO_RESULTS        0
#define UF_CLEAR_COPY_RESULTS           1
#define UF_CLEAR_COPY_INTERF_BODIES     2

/**************************
 ** Structures and Types **
 **************************/
/************************************************************************
Contains the summary of the most recent analysis results.
************************************************************************/
struct UF_CLEAR_summary_s {
        int     start_time;             /* The starting time of the last
                                           analysis run (in seconds since
                                           00:00:00 1/1/1970.
                                        */
        int     end_time;               /* The ending time of the last
                                           analysis run (in seconds since
                                           00:00:00 1/1/1970.
                                        */
        int     run_time;               /* the total analysis time (in secs.) */
        int     version;                /* The version of this analysis run.
                                           This is a positive number.
                                        */
        int     analysis_mode;          /* The analysis mode.  One of
                                           UF_CLEAR_QUICK_FACET,
                                           UF_CLEAR_FULL_FACET,
                                           UF_CLEAR_BEST_AVAILABLE,
                                           UF_CLEAR_FACET_SOLID and
                                           UF_CLEAR_SOLID.
                                        */
        int     num_lists;              /* Number of object lists analyzed.
                                           Can be either 1 or 2.
                                        */
        int     n_list1;                /* The number of objects in list 1.   */
        int     n_list2;                /* The number of objects in list 2.   */
        int     n_pairs;                /* The number of pairs built from
                                           the object lists.
                                        */
        int     excluded_pairs;         /* The number of pairs that were
                                           excluded from analysis, either
                                           due to exclusion rules or
                                           explicit pair exclusion.
                                        */
        int     changed_pairs;          /* The number of pairs that had
                                           changed since the previous
                                           clearance analysis.
                                        */
        int     changed_objs;           /* The number of objects that had
                                           changed since the previous
                                           clearance analysis.
                                        */
        int     checked_pairs;          /* The total number of pairs that
                                           underwent analysis.
                                        */
        int     new_n_hard;             /* The total number of new hard
                                           interferences.
                                        */
        int     new_n_soft;             /* The total number of new soft
                                           interferences.
                                        */
        int     new_n_touching;         /* The total number of new touching
                                           interferences.
                                        */
        int     new_n_containment;      /* The total number of new containment
                                           interferences.
                                        */
        int     new_n_all_interf;       /* The total number of new
                                           interferences.
                                        */
        int     n_hard;                 /* The total number of hard
                                           interferences.
                                        */
        int     n_soft;                 /* The total number of soft
                                           interferences.
                                        */
        int     n_touching;             /* The total number of touching
                                           interferences.
                                        */
        int     n_containment;          /* The total number of containment
                                           interferences.
                                        */
        int     n_all_interf;           /* The total number of interferences. */
        int     job_aborted;            /* Indicates if the analysis was
                                           aborted.  Valid values are
                                           UF_CLEAR_NOT_ABORTED,
                                           UF_CLEAR_ABORTED_BY_USER and
                                           UF_CLEAR_ABORTED_ON_ERROR.
                                        */
        int     num_zones;              /* The number of assembly zones used
                                           by the analysis (batch only).
                                        */
};

typedef struct UF_CLEAR_summary_s UF_CLEAR_summary_t, *UF_CLEAR_summary_p_t;

/*************************************************************************
Contains data associated with an interference.
*************************************************************************/
struct UF_CLEAR_interf_data_s {
        int     type;                   /* The type of interference.  One of
                                           UF_CLEAR_SOFT_INTERFERENCE,
                                           UF_CLEAR_TOUCH_INTERFERENCE,
                                           UF_CLEAR_HARD_INTERFERENCE,
                                           UF_CLEAR_CONT_1_IN_2_INTERFERENCE
                                           or UF_CLEAR_CONT_2_IN_1_INTERFERENCE.
                                        */
        logical new_interference;       /* Is this a new interference?        */
        int     n_bodies;               /* The number of interference bodies. */
        tag_t   *interf_bodies;         /* <len:n_bodies> The array of interference body
                                           tags.  This array must be freed
                                           when no longer needed by the user,
                                           provided n_bodies > 0.
                                        */
        double  point1[3];              /* A point on object 1.               */
        double  point2[3];              /* A point on object 2.               */
        char    text[ MAX_LINE_BUFSIZE ];/* The text associated with this
                                           interference.
                                        */
        int     interf_num;             /* A unique number for the
                                           interference.
                                        */
};

typedef struct UF_CLEAR_interf_data_s UF_CLEAR_interf_data_t,
                                     *UF_CLEAR_interf_data_p_t;

/*************************************************************************
Contains the clearance analysis module preference settings.
*************************************************************************/
struct UF_CLEAR_pref_s {
        int     interactive_msg_filter; /* The mode of the interactive message
                                           filter, composed of one or more of
                                           the following bits:
                                           UF_CLEAR_NO_INTERFERENCE,
                                           UF_CLEAR_SOFT_INTERFERENCE,
                                           UF_CLEAR_TOUCH_INTERFERENCE,
                                           UF_CLEAR_HARD_INTERFERENCE,
                                           UF_CLEAR_CONT_1_IN_2_INTERFERENCE,
                                           UF_CLEAR_CONT_2_IN_1_INTERFERENCE,
                                           and UF_CLEAR_NEW_INTERFERENCE.
                                        */
        logical save_interference;      /* Should interference bodies be
                                           saved?
                                        */
        int     interference_layer;     /* The layer on which to put
                                           interference bodies.
                                        */
        int     interference_color;     /* The color to assign to all
                                           interference bodies.
                                        */
        int     interf_attn_color;      /* This member is no longer used.
                                        */
        int     parent_attn_color;      /* This member is no longer used.
                                        */
};

typedef struct UF_CLEAR_pref_s UF_CLEAR_pref_t, *UF_CLEAR_pref_p_t;

/*******************************************************************************
                         ** Function Prototypes **

 ******************************************************************************/

/*******************************************************************************
                        ** Begin dataset routines.
*******************************************************************************/

/*******************************************************************************
*  Gets the name of a clearance analysis dataset.
*  The name must be allocated to at least MAX_LINE_SIZE+1 characters.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_next_dataset
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::ClearanceSetName property instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_dataset_name (
tag_t dataset ,/* <I>
               The dataset tag.
               */
char name[ MAX_LINE_BUFSIZE ]  /* <O>
             The name of the dataset. Must be allocated to
             MAX_LINE_SIZE+1 characters.
             */
);

/*******************************************************************************
*
*  Gets the version of a clearance analysis dataset. The version indicates
*  how many times clearance analysis has been run on a data set. If the
*  version is zero, then the analysis has never been run.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_next_dataset
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::GetVersion instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_dataset_version (
        tag_t   dataset,        /* <I> The dataset tag.                       */
        int     *version        /* <O> The version of dataset.                */
);

/*******************************************************************************
*  Cycles all clearance analysis datasets in a part, beginning with NULL_TAG
*  as the the input set.  NULL_TAG will be passed back to signify the end of
*  cycling.
*  Note: The dataset tag may only be used as a parameter to other UF_CLEAR
*        functions.
*  Note: Do not delete a dataset while it is being cycled.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSetCollection::iterator instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_next_dataset (
tag_t part_tag ,/* <I>
                The part in which to find the dataset.
                */
tag_t * dataset  /* <I/O>
                 On input, the current dataset.
                 On output, the next dataset.
                */
 );

/*******************************************************************************
*
*  Makes a copy of a dataset.  You must supply a unique name.  There are three
*  modes in which to copy the dataset: UF_CLEAR_COPY_NO_RESULTS only copies
*  the setup data.  The version of the new dataset is set to zero (meaning
*  clearance analysis has not been run);  UF_CLEAR_COPY_RESULTS makes a copy of
*  the current analysis results, but not the interference bodies;
*  UF_CLEAR_COPY_INTERF_BODIES makes a complete copy of the results. The name
*  must  be less than MAX_LINE_SIZE characters long.
*  NOTE: The new data set tag may only be used as a parameter to
*  other UF_CLEAR functions.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_name_exists
*                               UF_CLEAR_err_bad_string
*                               UF_CLEAR_err_bad_copy_mode.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::Copy() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_copy_dataset (
        tag_t   dataset,        /* <I>
                                The dataset to copy.
                                */
        const char    *name,          /* <I>
                                The name of the new dataset.
                                */
        int     mode,           /* <I>
                                Copy mode, see above.
                                */
        tag_t   *new_dataset    /* <O>
                                The dataset that is copied.
                                */
);

/*******************************************************************************
*
*  Determines the number of clearance analysis datasets in the specified part.
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_part.
*
*  Environment :Internal & External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSetCollection::CountClearanceSets() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_count_datasets (
        tag_t   part_tag,       /* <I>
                                   The part in which to count.
                                */
        int     *num            /* <O>
                                   The number of datasets.
                                */
);

/*******************************************************************************
*  Creates a new clearance analysis data set, initialized to default values.
*  If successful, this routine returns the tag of the new dataset. If a
*  dataset of the given name already exists, an error is returned. The
*  name must be less than MAX_LINE_SIZE characters long.
*  NOTE: The new data set tag may only be used as a parameter to
*  other UF_CLEAR functions.

* Return:
*       Return code:
*              0 = No error
*          not 0 = Error code, which includes
*                              UF_CLEAR_bad_part
*                              UF_CLEAR_err_name_exists
*                              UF_CLEAR_err_bad_string.
*
* Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder object instead.
********************************************************************************/
extern UFUNEXPORT int UF_CLEAR_create_dataset(
tag_t part_tag ,/* <I>
                The part in which the new dataset belongs.
                */
const char * name ,/* <I>
             The name of the new dataset.
             */
tag_t * dataset  /* <O>
                 The new dataset tag.
                 */
);

/*******************************************************************************
*
*  Delete the given clearance analysis data set.
*  NOTE: Do not delete data sets while they are being cycled.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::Delete() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_delete_dataset(
tag_t dataset  /* <I>
               The dataset to delete.
               */
);

/*******************************************************************************
*
*  Finds the tag of a named clearance analysis data set. If the name
*  doesn't exist, UF_CLEAR_err_cant_find_dataset is returned. The
*  name must be equal to or less than MAX_LINE_SIZE characters long.
*  NOTE: The data set tag may only be used as a parameter to other
*  UF_CLEAR functions.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_part
*                               UF_CLEAR_err_bad_string
*                               UF_CLEAR_err_cant_find_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_rename_dataset
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSetCollection::FindObject() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_find_dataset(
tag_t part_tag ,/* <I>
                The part in which to search.
                */
const char * name ,/* <I>
             The name of the dataset to search for.
             */
tag_t * dataset  /* <O>
                 The tag of the found dataset.
                 */
);

/*******************************************************************************
Routine to find the user's method for generating a saveas dataset name.
This method is called in response to including non-master parts in a saveas
of their master part.

Note: This routine, if registered, will be called in preference to the
existing Team Center Engineering user exit routine, which may be called from user's UFUN anyway.

Environment: Internal and External
See Also:
History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_UGMGR_ask_saveas_dataset_name
(
    UF_UGMGR_saveas_dataset_name_fn_t *func
                                      /* <I>
                                      Pointer to the user supplied
                                      registered Open API program
                                      */
);
/******************************************************************************
Routine to register the user's method for generating a saveas dataset name.
May be NULL to unregister a program.

Note: This routine, if registered, will be called in preference to the
existing Team Center Engineering user exit routine, which may be called from user's UFUN anyway.

Environment: Internal and External

See Also: UF_UGMGR_ask_saveas_dataset_name
 UF_UGMGR_saveas_dataset_name_t


History:This function was originally released in V15.0.
******************************************************************************/
extern UFUNEXPORT int UF_UGMGR_reg_saveas_dataset_name
(
    UF_UGMGR_saveas_dataset_name_fn_t saveas_dataset_name_fn
                                      /* <I>
                                      Pointer to the user supplied
                                      registered Open API program
                                      */
);

/*******************************************************************************
This routine finds the user's method for generating a new id for a part. The id
may be item_id for the default domain. For non-default domain, the id may be the
mfk id. The callback will be executed when the "Assign" button in the new part
dialog in NX Manager is selected. This callback can not contain a call to UF_initialize.
If it is called an error 1105002 "UF_initialize may not be called once UF_terminate is
called". It is necessary to call UF_UI_lock_ug_access prior to calling any
interactive API functions.


Environment: Internal and External

See Also: UF_UGMGR_reg_new_id
 UF_UGMGR_new_id_t

History: Deprecated in NX11.0

Please use Teamcenter customization for registering user exit routine for multifield key generation.
*****************************************************************************/
extern UFUNEXPORT int UF_UGMGR_ask_new_id(
    UF_UGMGR_new_id_fn_t *func /* <I>
                               Pointer to registered function to invoke
                               */
                               );

/*******************************************************************************
Registers the user's method for generating a new id for a part. The supplied
callback is executed in response to the "Assign" button in the new part dialog
in NX Manager. If a NULL is used then the program will be un-registered.
In the registered callback, a call to UF_UI_lock_ug_access is necessary prior
to calling any interactive API functions. Also - it is not necessary to call
UF_initialize in the callback. It will raise an error if called.

Note:  This routine, if registered, will be called in preference to the
existing Teamcenter user exit routine.

Environment: Internal and External

See Also:  UF_UGMGR_ask_new_id
 UF_UGMGR_new_id_t


History: Deprecated in NX11.0

Please use Teamcenter customization for registering user exit routine for multifield key generation.
*******************************************************************************/
extern UFUNEXPORT int UF_UGMGR_reg_new_id
(
UF_UGMGR_new_id_fn_t new_id_fn /* <I>
                               Pointer to the user supplied
                               registered Open callback
                               */
                               );

/*******************************************************************************
*
*  Changes the name of the given data set. If a dataset of the given name
*  already exists, an error is returned. The name must be equal to or less
*  than MAX_LINE_SIZE characters long.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_name_exists
*                               UF_CLEAR_err_bad_string.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_create_dataset
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::ClearanceSetName property instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_rename_dataset(
tag_t dataset ,/* <I>
               The dataset to rename.
               */
const char * name  /* <I>
             The new name.
             */
);

/*****************************************************************************
                       Begin the object list routines.
******************************************************************************/

/*****************************************************************************
*
*  Inquire the number of object lists used by the given clearance analysis
*  data set. The number of lists can either be 1 or 2.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_obj_list
*   UF_CLEAR_set_obj_list
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::TotalCollectionCount property instead.
******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_num_lists(
tag_t dataset ,/* <I>
               The dataset tag.
               */
int * num_lists  /* <O>
                 The number of lists used (1 or 2).
                 */
);

/*******************************************************************************
*
*  Inquires data associated with one of the clearance analysis object lists,
*  specified by which_list. The list_type corresponds to the ways the
*  object lists can be defined in the interactive application by using one
*  of these values: UF_CLEAR_ALL_OBJECTS, UF_CLEAR_ALL_VISIBLE_OBJECTS,
*  UF_CLEAR_ALL_BUT, or UF_CLEAR_FIXED_LIST.
*  If the data set only uses one list and which_list is 2, then list_type is
*  set to UF_CLEAR_LIST2_NOT_USED. The list is evaluated when
*  necessary and the number of objects in the list is returned in list_size.
*  A pointer to a tag_array is returned.
*  If list_size is greater than zero, you must call UF_free when you no
*  longer need this array. The tag_array stores either solid body or facet
*  model tags depending on which objects are currently loaded. If both
*  are loaded, the solid body tags are returned. If neither object is
*  loaded, then NULL_TAG is placed in the array.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_list_num.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_num_lists
*   UF_CLEAR_set_obj_list
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use following Assemblies::ClearanceAnalysisBuilder's properties instead:
*  ClearanceBetween
*  TotalCollectionCount
*  CollectionOne(Two)Range
*  CollectionOne(Two)Objects
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_obj_list(
tag_t dataset ,/* <I>
                 The dataset tag.
                 */
int which_list ,/* <I>
                Is this for list 1 or list 2?
                Acceptable values are 1 and 2.
                */
int * list_type ,/* <O>
                 The type of list (UF_CLEAR_ALL_OBJECTS,
                 UF_CLEAR_ALL_VISIBLE_OBJECTS,
                 UF_CLEAR_ALL_BUT,
                 UF_CLEAR_FIXED_LIST, or
                 UF_CLEAR_LIST2_NOT_USED).
                 */
int * list_size ,/* <O>
                 The number of objects in list.
                 */
tag_t ** tag_array  /* <OF,len:list_size>
                    The pointer to an array of objects (solids or facets)
                    on the list.  This should be freed by calling UF_free.
                    */
);

/*******************************************************************************
*  Returns a list of objects that was last selected to be excluded from
*  which_list, regardless of the current list type. If an object on the list  is
*  currently not loaded, a NULL_TAG is put in its place in the
*  tag_array. You need to free the tag_array when no longer needed.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset and
*                               UF_CLEAR_err_bad_list_num.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_obj_list
*   UF_CLEAR_set_obj_list
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use following Assemblies::ClearanceAnalysisBuilder's properties instead:
*  ClearanceBetween
*  TotalCollectionCount
*  CollectionOne(Two)Range
*  CollectionOne(Two)Objects
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_obj_all_but_list (
tag_t dataset ,/* <I>
               The dataset tag
               */
int which_list ,/* <I>
                Determines which list to use:
                1 = List 1
                2 = List 2
                */
int * list_size ,/* <O>
                 The number of objects in the list
                 */
tag_t ** tag_array  /* <OF,len:list_size>
                    The array of objects (solid or facet) on the list.
                    This should be freed by calling UF_free.
                    */
);

/*******************************************************************************
*  Fully defines a clearance analysis object list, specified by which_list.
*  The list type corresponds to the ways an object list can be defined in
*  the interactive application by using one of these values:
*  UF_CLEAR_ALL_OBJECTS, UF_CLEAR_ALL_VISIBLE_OBJECTS, UF_CLEAR_ALL_BUT, or
*  UF_CLEAR_FIXED_LIST.
*  To specify a one list data set, set which_list to 2 and list_type to
*  UF_CLEAR_LIST2_NOT_USED. No tag_array is necessary.
*  For a UF_CLEAR_ALL_OBJECTS or UF_CLEAR_ALL_VISIBLE_OBJECTS list, you do
*  not need to supply a tag_array -- the list is automatically evaluated
*  when necessary.
*  For a UF_CLEAR_ALL_BUT list, you must specify the tags of those
*  solid bodies and/or facet models you want to explicitly exclude from
*  the list. The list of included objects is reevaluated when necessary.
*  For a UF_CLEAR_FIXED_LIST, you must specify an array of objects
*  to be members of the list. These objects must be solid bodies or facet
*  models. This list is not further evaluated. Note that you may need to
*  call this routine twice, once for each list.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_list_num
*                               UF_CLEAR_err_bad_list_type
*                               UF_CLEAR_err_bad_list_data.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_num_lists
*   UF_CLEAR_ask_obj_list
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use following Assemblies::ClearanceAnalysisBuilder's properties instead:
*  ClearanceBetween()
*  TotalCollectionCount
*  CollectionOne(Two)Range
*  CollectionOne(Two)Objects
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_obj_list(
tag_t dataset ,/* <I>
               The dataset tag.
               */
int which_list ,/* <I>
                Is this for list 1 or list 2? Acceptable values are 1
                and 2.
                */
int list_type ,/* <I>
               The new type of list
                (UF_CLEAR_ALL_OBJECTS,
                UF_CLEAR_ALL_VISIBLE_OBJECTS,
                UF_CLEAR_ALL_BUT,
                UF_CLEAR_FIXED_LIST, or
                UF_CLEAR_LIST2_NOT_USED).
               */
int list_size ,/* <I>
               The size of tag_array.
               */
tag_t * tag_array  /* <I,len:list_size> list_size
                   The object tags (solids or facets) to be applied to
                   the list.
                   */
);

/****************************************************************************
                         Begin clearance zone routines.
*****************************************************************************/

/****************************************************************************
*
*  Inquire the default clearance zone for the given data set. This routine
*  returns the clearance zone expression tag. If no expression has ever
*  been set, NULL_TAG is returned. Interpret its value as 0.0. For a
*  non-null expression, call UF_MODL_ask_exp_tag_value to get the
*  value of the expression.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_object_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_object_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::GetDefaultClearanceZone() instead.
*****************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_default_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t * def_clr_zone  /* <O>
                      The default clearance zone expression tag.
                      */
);

/*******************************************************************************
*
*  Inquire the clearance zone assigned to a given object.  The object must be
*  a member of the dataset.  The tag of the expression is returned.  If no
*  expression has ever been set, the part of the given object is checked for
*  a clearance zone expression, if none is found, NULL_TAG will be returned
*  for clr_zone. Interpret its value as 0.0 (this is the default value).  For a
*  non-null expression, call UF_MODL_ask_exp_tag_value to get its value.  The
*  source parameter tells where the clearance zone comes from.
*  UF_CLEAR_USING_DEFINED_CZ specifies that the object has its own clearance
*  zone.  UF_CLEAR_USING_DEFAULT_CZ means the default clearance zone is used.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_object_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::GetObjectClearanceZone() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_object_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object ,/* <I>
              The object (solid or facet) whose clearance zone is
              requested.
              */
tag_t * clr_zone ,/* <O>
                    The clearance zone expression.
                  */
int * source  /* <O>
              The source of the clearance zone (one of
              UF_CLEAR_USING_DEFINED_CZ, or
              UF_CLEAR_USING_DEFAULT_CZ).
              */
);

/*******************************************************************************
*  Inquire the clearance zone for a specific pair of objects.  Both objects
*  must be members of the given dataset.  The tag of the expression is
*  returned.  If no expression has ever been set, NULL_TAG will be returned
*  for clr_zone.  Interpret its value as 0.0 (this is the default value).  For
*  a non-null expression, call UF_MODL_ask_exp_tag_value to get its value.
*  The source parameter tells where the clearance zone comes from.  The
*  clearance zone could be the greater of the zones from object 1 or 2
*  (UF_CLEAR_USING_OBJ1_CZ or UF_CLEAR_USING_OBJ2_CZ).
*  UF_CLEAR_USING_PAIR_CZ means this pair has its own explicit clearance zone.
*  UF_CLEAR_USING_DEFAULT_CZ means the default clearance zone is used.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_object_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::GetPairClearanceZone() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_pair_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
tag_t * clr_zone ,/* <O>
                  The clearance zone expression.
                  */
int * source  /* <O>
              The source of the clearance zone (one of
              UF_CLEAR_USING_OBJ1_CZ,
              UF_CLEAR_USING_OBJ2_CZ,
              UF_CLEAR_USING_PAIR_CZ, or
              UF_CLEAR_USING_DEFAULT_CZ).
              */
);

/*******************************************************************************
*  Sets the default clearance zone for the given data set. During analysis,
*  any object pair that doesn't have either a zone for one of its objects or
*  for the pair, explicitly uses this default clearance zone. You must
*  supply the tag of a valid expression.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_expression.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_ask_object_clear_zone
*   UF_CLEAR_set_object_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::SetDefaultClearanceZone() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_default_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t def_clr_zone  /* <I>
                    The tag of the new default clearance zone
expression.
                    */
);

/*******************************************************************************
*
* Assigns the clearance zone for the given object. The object must be a
* member of the data set. During analysis, any object pair that doesn't
* have a clearance zone explicitly assigned to that pair uses the greater
* of the clearance zones assigned to each object. You must supply the
* tag of a valid expression.
*
* Return:
*       Return code:
*              0 = No error
*          not 0 = Error code, which includes
*                              UF_CLEAR_err_bad_dataset
*                              UF_CLEAR_err_bad_expression.
*
* Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_ask_object_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalaysisBuilder's AddObjectClearanceZone() and DeleteObjectClearanceZone() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_object_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object ,/* <I>
              The object (solid or facet) whose clearance zone is
              being set.
              */
tag_t clr_zone  /* <I>
                The new clearance zone expression.
                */
);

/*******************************************************************************
*  Assign the clearance zone for the given object pair. Each object must
*  be a member of the data set. During analysis, the pair clearance zones
*  overrides any clearance zones assigned to the individual objects. You
*  must supply the tag of a valid expression.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_expression.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_ask_object_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_object_clear_zone
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder's AddPairClearanceZone() and DeletePairClearanceZone() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_pair_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
tag_t clr_zone  /* <I>
                The new clearance zone expression.
                */

);

/*******************************************************************************
                      ** Begin pair exclusion routines.
*******************************************************************************/

/*******************************************************************************
*  Enquires the global exclusion rules. These settings cause classes of
*  object pairs to be excluded from analysis: pairs belonging to the same
*  sub-assembly/component, pairs belonging to the same part and pairs
*  belonging to the same group.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*
*
*  History:  NX9: UF_CLEAR_EXCLUDE_MATING_PAIRS no longer supported
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder's GetIsIgnorePairsWithinSameGroup(), GetIsIgnorePairsWithinSamePart(), and GetIsIgnorePairsWithinSameSubassembly() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_exclude_rules(
tag_t dataset ,/* <I>
               The dataset tag.
               */
int * exclude_rules  /* <O>
                     The exclusion rules that were applied. Any of the
                     following constants can be ORed together:
                     UF_CLEAR_EXCLUDE_WITHIN_COMP
                     UF_CLEAR_EXCLUDE_WITHIN_PART
                     UF_CLEAR_EXCLUDE_WITHIN_GROUP
                     */
);

/*******************************************************************************
*  Inquires if an object pair has changed since the last analysis run. Both
*  objects must be solid bodies or facet models that are members of the
*  clearance analysis data set. If either object has changed since the last
*  analysis run, then is_changed is returned as TRUE. If no analysis has
*  been run on either of the objects, TRUE is returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_set_exclude_rules
*   UF_CLEAR_set_pair_exclusion
*   UF_CLEAR_set_pair_inclusion
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::GetIsPairChanged() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_is_pair_changed(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
logical * is_changed  /* <O>
                      Has this pair changed since the last analysis run?
                      */
);

/*******************************************************************************
*  Inquires if an object pair is to be included in the analysis. Both objects
*  must be solid bodies or facet models that are members of the
*  clearance analysis data set. If the pair is to be analyzed, the include_it
*  is returned as TRUE. The reason parameter signifies why the pair is
*  included or excluded. UF_CLEAR_EXCL_NO_REASON is returned
*  when the default behavior is applied.
*  UF_CLEAR_EXCL_USER_DEF means the user has explicitly
*  included or excluded this pair. UF_CLEAR_EXCL_SAME_COMP,
*  UF_CLEAR_EXCL_SAME_PART, UF_CLEAR_EXCL_SAME_GROUP, and
*  UF_CLEAR_EXCL_MATED_COMP are returned if one of the
*  global exclusion rules applied to this pair. Only one such rule is
*  returned, even if several such rules apply to the given pair.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_is_pair_changed
*   UF_CLEAR_set_exclude_rules
*   UF_CLEAR_set_pair_exclusion
*   UF_CLEAR_set_pair_inclusion
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::GetIsPairIncluded() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_is_pair_included(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
logical * include_it ,/* <O>
                      Should this pair be included in the analysis?
                      */
int * reason ,/* <O>
                The reason the pair is included or excluded (one of
                UF_CLEAR_EXCL_NO_REASON,
                UF_CLEAR_EXCL_USER_DEF,
                UF_CLEAR_EXCL_SAME_COMP,
                UF_CLEAR_EXCL_SAME_PART,
                UF_CLEAR_EXCL_SAME_GROUP, or
                UF_CLEAR_EXCL_MATED_COMP).
              */
char ** text  /* <OF>
                The text associated with
                UF_CLEAR_set_pair_inclusion and
                UF_CLEAR_set_pair_exclusion when reason is
                UF_CLEAR_EXCL_USER_DEF, or an empty
                string is returned. Use UF_free((void *) *text) to
                deallocate memory when done.
              */
);

/*******************************************************************************
*  Sets the global exclusion rules. These settings causes classes of object
*  pairs to be excluded from analysis: pairs belonging to the same sub-assembly/
*  component; pairs belonging to the same part; and pairs belonging to the
*  same group. The exclude_rules value can be comprised of zero or more of
*  the following constants ORed together: UF_CLEAR_EXCLUDE_WITHIN_COMP,
*  UF_CLEAR_EXCLUDE_WITHIN_PART and UF_CLEAR_EXCLUDE_WITHIN_GROUP.
*  The default value is to exclude nothing, i.e., exclude_rules = 0.
*  The customer default file can also be used to change this
*  default value.  See the default values for,
*  Assemblies_ClrAnlExclMatingPairs, Assemblies_ClrAnlExclWithinComp,
*  Assemblies_ClrAnlExclWithinPart and Assemblies_ClrAnlExclWithinGroup.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_exclude_rule.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_is_pair_changed
*   UF_CLEAR_is_pair_included
*   UF_CLEAR_set_pair_exclusion
*   UF_CLEAR_set_pair_inclusion
*
*
*  History:  NX9: UF_CLEAR_EXCLUDE_MATING_PAIRS no longer supported
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder's SetIsIgnorePairsWithinSameGroup(), SetIsIgnorePairsWithinSamePart(), SetIsIgnorePairsWithinSameSubassembly() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_exclude_rules(
tag_t dataset ,/* <I>
               The data set tag.
               */
int exclude_rules  /* <I>
                        Which rules should be applied? The following
                        constants can be ORed together:
                        UF_CLEAR_EXCLUDE_WITHIN_COMP,
                        UF_CLEAR_EXCLUDE_WITHIN_PART,
                        and UF_CLEAR_EXCLUDE_WITHIN_GROUP.
                  */
);

/*******************************************************************************
*  Explicitly excludes an object pair from analysis. Each object must be a
*  member of the data set. You may associate a text string with the pair.
*  The string must be equal to or less than MAX_LINE_SIZE characters
*  long.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_string.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_is_pair_changed
*   UF_CLEAR_is_pair_included
*   UF_CLEAR_set_exclude_rules
*   UF_CLEAR_set_pair_inclusion
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assenblies::ClearanceAnalysisBuilder::AddException() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_pair_exclusion(
tag_t dataset ,/* <I>
               The data set tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
const char * text  /* <I>
             The text to associate with each pair.
             */
);

/*******************************************************************************
*
*  Explicitly includes an object pair in analysis. Each object must be a
*  member of the data set. You may associate a text string with the pair.
*  The string must be equal to or less than MAX_LINE_SIZE characters
*  long.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_string.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_is_pair_changed
*   UF_CLEAR_is_pair_included
*   UF_CLEAR_set_exclude_rules
*   UF_CLEAR_set_pair_exclusion
*
*
*  History:
* *  Deprecated in NX9.0
* *
*  Equivalent JA function/property:
*  Please use Assenblies::ClearanceAnalysisBuilder::AddException() instead.
*/
extern UFUNEXPORT int UF_CLEAR_set_pair_inclusion(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
const char * text  /* <I>
             The text to associate with each pair.
             */
);

/*******************************************************************************
                         ** Begin analysis routines.
*******************************************************************************/

/*******************************************************************************
*  Inquires the current clearance analysis mode. It may have one of the
*  following values: UF_CLEAR_QUICK_FACET, UF_CLEAR_FULL_FACET,
*  UF_CLEAR_BEST_AVAILABLE, UF_CLEAR_FACET_SOLID, or UF_CLEAR_SOLID.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::GetCalculationMethod() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_analysis_mode(
tag_t dataset ,/* <I>
               The data set tag.
               */
int * analysis_mode  /* <O>
                     One of the following analysis modes:
                     UF_CLEAR_QUICK_FACET,
                     UF_CLEAR_FULL_FACET,
                     UF_CLEAR_BEST_AVAILABLE,
                     UF_CLEAR_FACET_SOLID, or
                     UF_CLEAR_SOLID.
                     */
);

/*******************************************************************************
*  Inquires the data associated with a given pair of interfering objects.
*  The structure that is returned contains the type of interference. The
*  interference type is one of:
*  UF_CLEAR_SOFT_INTERFERENCE,
*  UF_CLEAR_TOUCH_INTERFERENCE,
*  UF_CLEAR_HARD_INTERFERENCE,
*  UF_CLEAR_CONT_1_IN_2_INTERFERENCE,
*  UF_CLEAR_CONT_2_IN_1_INTERFERENCE, or
*  UF_CLEAR_NO_INTERFERENCE.
*  If the interference was computed during the most recent analysis run,
*  the new_interference will be TRUE. The array of interference bodies
*  that are associated with the interference are passed back in the
*  interf_bodies field. n_bodies indicates the size of this array. This array
*  of tags could refer to points, lines, curves, and/or solid bodies,
*  depending on the analysis mode and the type of interference. If
*  n_bodies is greater than 0, this array must be freed using UF_free by
*  the caller when no longer needed. point1 and point2 indicate points
*  (in assembly coordinates) on both of the interfering objects. The text
*  field contains any text the user has associated with this interference.
*  interf_num is a unique number associated with each interference. You
*  may choose to sort interference based on this value. If the two objects
*  do not have a stored interference, then zero is returned for the
*  interference number, UF_CLEAR_NO_INTERFERENCE is returned as
*  the type, and the size of the interf_bodies array is zero.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_interf.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::GetInterferenceData() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_interf_data(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t  object1 ,/* <I>
                The first object (solid or facet) in the pair.
                */
tag_t  object2 ,/* <I>
                The second object (solid or facet) in the
                pair.
                */
UF_CLEAR_interf_data_t * interf_data  /* <O>
                                      The structure containing data on this
                                      interfering pair.
                                      */
);

/*******************************************************************************
*  Cycles the interference in a clearance analysis data set. Interferences
*  are stored as object pairs. Start the cycling using NULL_TAG as the
*  input values for both object1 and object2. This routine passes back the
*  tags of the objects that define the next interference. NULL_TAG
*  returned for either object indicates the end of the cycling.
*  NOTE: The object tags that are passed back may refer to unloaded
*  objects. One or both of these objects could be object occurrences that
*  refer to unloaded prototypes. Before using these tags for any purpose
*  (other than cycling interferences) you must verify that the objects
*  refer to loaded objects.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_interf.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::GetNextInterference() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_next_interf(
tag_t dataset ,/* <I>
               The data set tag.
               */
tag_t * object1 ,/* <I/O>
               The first object (solid or facet) in the pair.
                 */
tag_t * object2  /* <I/O>
                 The second object (solid or facet) in the pair.
                 */
);

/*******************************************************************************
*  Inquires a summary of the results of the most recent clearance
*  analysis run. The UF_CLEAR_summary_t structure is filled with
*  analysis statistics, including numbers of objects, number of pairs,
*  number of checked pairs, and number of interferences of each type. If
*  clearance analysis has never been run on the data set, an error is
*  returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_no_results.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_count_interferences
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::GetResults() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_results(
tag_t dataset ,/* <I>
               The data set tag.
               */
UF_CLEAR_summary_t * summary  /* <O>
                              The summary structure.
                              */
);

/*******************************************************************************
*  Inquires the number of interferences stored in a clearance analysis
*  data set. If clearance analysis has never been run on the data set, an
*  error is returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::GetNumberOfInterferences() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_count_interferences(
tag_t dataset ,/* <I>
               The data set tag.
               */
int * num_interf  /* <O>
                  The number of interferences associated with the
                  dataset.
                  */
);

/*******************************************************************************
*  Deletes the interference for a given object pair. Both objects must be
*  members of the given data set. If the object pair does not refer to an
*  existing interference, an error is returned. All data associated with the
*  interference is deleted.
*  NOTE: It is acceptable to delete the interference bodies without
*  deleting the interference itself. Use the normal deletion functions to
*  delete the interference points, lines, curve, and/or solid bodies. By
*  doing so, all interference data is retained except for the bodies
*  themselves. This might be desirable in cases where the interference
*  bodies make the part file unnecessarily large.
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_interf.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::DeleteInterference() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_delete_interf(
tag_t dataset ,/* <I>
               The data set tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2  /* <I>
               The second object (solid or facet) in the pair.
               */
);

/*******************************************************************************
*  Performs clearance analysis on the given dataset using the previously
*  set options. This function looks at all object pairs from the objects
*  lists. All object pairs that are not excluded and have changed since the
*  last analysis run are analyzed. Facet models are created when
*  necessary if using one of the facet analysis modes. Interference results
*  are created using previously set options. This function can not be
*  gracefully interrupted and interferences are not reported as they are
*  found.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes:
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_analysis_error
*                               UF_CLEAR_err_facet_error
*                               UF_CLEAR_err_obj_not_avail.
*
*  Environment: Internal  and  External
*
*  See Also:
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::PerformAnalysis() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_do_clearance_analysis(
tag_t dataset  /* <I>
               The dataset tag.
               */
);

/*******************************************************************************
*  Sets the clearance analysis mode. It may have one of the following
*  values: UF_CLEAR_QUICK_FACET, UF_CLEAR_FULL_FACET,
*  UF_CLEAR_BEST_AVAILABLE, UF_CLEAR_FACET_SOLID, or UF_CLEAR_SOLID.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_analysis_mode,
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_delete_interf
*   UF_CLEAR_set_interf_text
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::SetCalculationMethod() instead.
******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_analysis_mode(
tag_t dataset ,/* <I>
               The data set tag.
               */
int analysis_mode  /* <I>
                   One of the following analysis modes:
                   UF_CLEAR_QUICK_FACET,
                   UF_CLEAR_FULL_FACET,
                   UF_CLEAR_BEST_AVAILABLE,
                   UF_CLEAR_FACET_SOLID, or
                   UF_CLEAR_SOLID.
                   */
);

/*******************************************************************************
*  Associates a text string to an interfering object pair. Both objects must
*  be members of the given dataset. If the object pair does not refer to
*  an existing interference, an error is returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset,
*                               UF_CLEAR_err_bad_interf.
*
*  Environment: Internal  and  External
*
*  See Also:
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSet::SetInterferenceText() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_interf_text (
tag_t dataset ,/* <I>
               The dataset tag
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair
               */
const char * text  /* <I>
             The text to associate with the interference. The
             length of the text cannot be greater than the value
             assigned to the string constant MAX_LINE_SIZE.
             */
);

/*******************************************************************************
                       ** Begin miscellaneous routines.
*******************************************************************************/

/*******************************************************************************
*  Inquire clearance module preferences. The structure contains the
*  current interactive message filter, which indicates the types of
*  interferences that are displayed by the interactive analysis and review
*  functions. Each bit of this integer refers to a specific type of
*  interference (UF_CLEAR_SOFT_INTERFERENCE, etc.). Use the
*  appropriate C bitwise logical operators (&, |, and ^) to interpret this
*  value. The save_interference parameter indicates if the interference
*  bodies are saved during analysis. The current layer and color
*  assignments are returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_delete_all
*   UF_CLEAR_set_preferences
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder::GetInteferenceColor(), GetLayer(), and GetSaveInterferenceGeometry(). interactive_msg_filter is no longer supported
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_preferences(
tag_t dataset ,/* <I>
               The dataset tag.
               */
UF_CLEAR_pref_t * preferences  /* <O>
                               The preferences structure.
                               */
);

/*******************************************************************************
*  Deletes all clearance analysis data from the given part, including all
*  clearance analysis data sets, analysis results, and interference bodies.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes:
*                               UF_CLEAR_bad_part.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_preferences
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_set_preferences
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceSetCollection::DeleteAllAnalysisData() instead.
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_delete_all(
tag_t part_tag  /* <I>
                The part from which all clearance analysis data is to
be deleted.
                */
);

/*******************************************************************************
*  Sets clearance module preferences. The structure contains the current
*  interactive message filter, which indicates the types of interferences
*  that are displayed by the interactive analysis and review functions.
*  Each bit of this integer refers to a specific type of interference
*  (UF_CLEAR_SOFT_INTERFERENCE, etc.). Use the appropriate C
*  bitwise logical operators (&, |, and ^) to set this value. The
*  save_interference parameter indicates if the interference bodies are
*  to be saved during analysis. The layer and color assignments will be
*  given to all new interference bodies. If you want to set just one of the
*  values, you must call UF_CLEAR_ask_preferences to fill the structure. Next,
*  edit those fields you want to change; then call UF_CLEAR_set_preferences.
*  The default values are:
*
*      interactive_msg_filter:   ALL (i.e., display all).
*      save_interference:        TRUE
*      interference_layer:       0 (current)
*      interference_color:       YELLOW
*
*  These defaults are controlled by the customer defaults file.  The default
*  behavior can be changed by editting that file.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_msg_filter
*                               UF_CLEAR_err_bad_layer
*                               UF_CLEAR_err_bad_color.
*
*  Environment: Internal  and  External
*
*  See Also:
*
*
*  History:
*  Deprecated in NX9.0
*
*  Equivalent JA function/property:
*  Please use Assemblies::ClearanceAnalysisBuilder's SetInteferenceColor(), SetLayer(), and SetSaveInterferenceGeometry(). interactive_msg_filter is no longer supported
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_preferences(
tag_t dataset ,/* <I>
               The data set tag.
               */
UF_CLEAR_pref_t preferences  /* <I>
                             The preferences structure.
                             */
);

/*******************************************************************************
Read a line of text from a file opened with uc4504. The user is responsible
for making sure that the cbuf has enough space allocated to hold the longest
line in the file.

IMPORTANT: This function will be removed in NX10. All current callers of this function
need to be modified to call uc4514a instead.

Return:
         Return code
        <  0 = Error
        >= 0 = Length Of Line Read

Environment: Internal  and  External

See Also:
 uc4504

History:
*******************************************************************************/
extern UFUNEXPORT int uc4514(
int chan ,/* <I>
          I/O channel number returned by uc4504
          */
char cbuf[] /* <O>
             Line read
             */
);


/***************************************************************************
 * Return the persistent HANDLE for an object tag.
 * WARNING this routine has been replaced by UF_TAG_ask_handle_from_tag
 *
 * Multiple parts can be loaded into NX during a single session, and
 * the Tag (i.e. Object Identifier) cannot be guaranteed between sessions.
 * Consequently, "handles" were created to identify objects between sessions.
 * This handle is persistent between sessions.
 *
 * This function will normally honor the UF_TEXT_set_text_mode() and return
 * locale or utf8 data depending on what the mode has been set to.  However,
 * if the handle has characters from outside your locale, then this function
 * will output a warning to the syslog, and will return a null pointer for the
 * handle.  It is suggested that UF_TEXT_set_text_mode(UF_TEXT_ALL_UTF8) be
 * set when you are working with handles that may come from parts that have
 * characters that are outside of your locale (e.g. parts with Japanese
 * characters on an english system).
 *
 * Return:
 * Returns name of handle for object tag. This return string must be freed
 * by calling UF_free.
 *
 * Environment: Internal  and  External
 * See Also:  UF_TAG_ask_tag_of_handle
 *            UF_TAG_ask_handle_from_tag
 * History:
 * Deprecated in NX 10.0
 ***************************************************************************/
extern UFUNEXPORT char *UF_TAG_ask_handle_of_tag (
    tag_t   object_tag     /* <I>
               tag of object to query for persistent handle
               */
);/* <NEC> */

/*****************************************************************************
 * Assigns an attribute to the object specified. If the attribute does not
 * exist for the specified attribute type then create the attribute;
 * otherwise, modify its existing value.
 *
 * The calling routine must call UF_MODL_update() to propagate the attribute
 * change.
 *
 * Passing an object tag will result in modifying or creating an attribute
 * on that object. Passing in a part tag will result in modifying or
 * creating a part attribute for that part.
 *
 * The part in which the object resides must be fully loaded.
 *
 * If the attribute is of type UF_ATTR_string or UF_ATTR_reference, the
 * maximum length of its value is limited by UF_ATTR_MAX_STRING_BUFSIZE.
 *
 * If the attribute is of type UF_ATTR_time, then the value is assumed to be
 * in the current timezone of the machine running the program.
 * The value, when stored in NX, is converted from that timezone to UTC.
 * The valid range for attributes of type UF_ATTR_time is from 01-Jan-1970 to 31-Dec-2105.
 *
 * Environment: Internal  and  External
 * See Also : 
 *
 * Equivalent Functionality: UF_ATTR_set_user_attribute or NXObject::SetUserAttribute
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_assign(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
char * title ,/* <I>
              Attribute  Title (maximum character length is UF_ATTR_MAX_TITLE_BUFSIZE)
              */
UF_ATTR_value_t value  /* <I>
                       Typed Attribute Value
                       */
);

/*****************************************************************************
 * Sets the lock status of an attribute on the object specified. If the attribute does not
 * exist for the specified attribute type then an error is returned.
 *
 * Passing an object tag will result in modifying an attribute
 * on that object. Passing in a part tag will result in modifying
 * a part attribute for that part.
 *
 * The part in which the object resides must be fully loaded.
 *
 * Unlocking a locked attribute requires access via a Customer Default setting
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_set_user_attribute_lock_with_title_and_type or NXObject::SetUserAttributeLock
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_locked(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
char * title ,/* <I>
              Attribute  Title (maximum character length is UF_ATTR_MAX_TITLE_BUFSIZE)
              */
logical locked  /* <I>
             The new locked status
             */
);

/*****************************************************************************
 * Gets the lock status of an attribute on the object specified. If the attribute does not
 * exist for the specified attribute type then an error is returned.
 *
 * Passing an object tag will result in querying an attribute
 * on that object. Passing in a part tag will result in querying
 * a part attribute for that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_get_user_attribute_lock or NXObject::GetUserAttributeLock
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_ask_locked(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
char * title ,/* <I>
              Attribute  Title (maximum character length is UF_ATTR_MAX_TITLE_BUFSIZE)
              */
logical *locked  /* <O>
             The attribute's locked status
             */
);

/*****************************************************************************
 * Deletes the attribute of the specified type from the object. If the type
 * is UF_ATTR_any (or 6), then this function will delete all attributes with
 * the given title.
 *
 * The calling routine must call UF_MODL_update() to propagate the attribute
 * change.
 *
 * The part in which the object resides must be fully loaded.
 *
 * Passing in an object tag will result in deleting the attribute from that
 * object.  Passing in a part tag will result in deleting a part attribute from
 * that part.  Attributes that are inherited will not be deleted (and no error
 * message will be returned).  To delete an inherited attribute, the object that
 * owns that attribute must be passed into the function.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_delete_user_attribute or NXObject::DeleteUserAttribute
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_delete(
tag_t object ,/* <I>
            Part tag or part attribute tag.
            */
int type ,/* <I>
          Attribute  Type:
            UF_ATTR_bool
            UF_ATTR_integer
            UF_ATTR_real,
            UF_ATTR_time
            UF_ATTR_null,
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
char * title  /* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_BUFSIZE)
              */
);


/*****************************************************************************
 * Deletes all attributes of the specified type from the object. If the type
 * is UF_ATTR_any (or 6) then this function removes all attributes from the
 * object.
 *
 * The calling routine must call UF_MODL_update() to propagate the attribute
 * change.
 *
 * The part in which the object resides must be fully loaded.
 *
 * Passing in an object tag will result in deleting attributes from that
 * object.  Passing in a part tag will result in deleting part attributes from
 * that part.  Attributes that are inherited will not be deleted (and no error
 * message will be returned).  To delete an inherited attribute, the object that
 * owns that attribute must be passed into the function.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_delete_user_attributes or NXObject::DeleteUserAttributes
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_delete_all(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
int type  /* <I>
          Attribute  Type:
            UF_ATTR_bool
            UF_ATTR_integer
            UF_ATTR_real,
            UF_ATTR_time
            UF_ATTR_null,
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
);

/*****************************************************************************
 * Cycle through all the object's attributes of the specified type,
 * returning the title and value of the next attribute.
 *
 * If the type specified is UF_ATTR_any (or 6) then cycle through all the
 * attributes of the object.
 *
 * NOTE: Callers should not rely on attributes being returned in any
 *       particular order.
 *
 * If there are no more attributes to cycle then
 * a zero will be returned as the cycle status(indx).
 *
 * Passing an object tag will result in cycling the attributes of that object.
 * Passing in a part tag will result in cycling the part attributes of that
 * part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_get_next_user_attribute
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_cycle(
tag_t object ,/* <I>
              Part tag or object tag.
              */
int * indx ,/* <I/O>
            Cycle Status:(input)
               0 = Begin Cycling
            Cycle Status:(output)
               0 = Done Cycling or No Attribute Returned
               1 = Next Attribute Returned
            */
int type ,/* <I>
          Attribute Type to Cycle:
             UF_ATTR_bool
             UF_ATTR_integer
             UF_ATTR_real,
             UF_ATTR_time
             UF_ATTR_null,
             UF_ATTR_string
             UF_ATTR_any
             UF_ATTR_reference
          */
char  title[ UF_ATTR_MAX_TITLE_BUFSIZE ] ,/* <O>
                 Attribute Title (maximum character length is
                 UF_ATTR_MAX_TITLE_BUFSIZE)
              */
UF_ATTR_value_p_t value /* <I/O>
                     Typed Attribute Value:(Input)
                         If type is UF_ATTR_string then
                         value->value.string must point to the character
                         array where the string value will be returned.
                         If type is UF_ATTR_reference then
                         value->value.reference must point to the
                         character array where the string value will be
                         returned.
                     Typed Attribute Value:(Output)
                         If type is UF_ATTR_any and the returned
                         value->type is UF_ATTR_string or
                         UF_ATTR_reference then the string returned
                         was dynamically allocated and you must use
                         UF_free to deallocate the memory.
                         If the returned value->type is UF_ATTR_time, then
                         the value will be in the current time zone of the
                         machine on which the program is being executed.
                    */
);

/*****************************************************************************
 * Read the value of the attribute of the given type with the specified
 * title. If the attribute's type is UF_ATTR_any (or 6) then return the
 * value of the first attribute found with the given title.
 *
 * NOTE: Callers should not rely on attributes being returned in any
 *       particular order.
 * UF_ATTR_bool (8)
 *
 * If no attribute was found then a zero will be returned as the attribute's
 * type.  Passing an object tag will result in reading a value from the
 * attributes of that object. Passing in a part tag will result in reading a
 * value from the part attribute of that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_get_user_attribute or NXObject::GetUserAttribute
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_read_value(
tag_t object ,/* <I>
              Part tag or object tag.
              */
char * title ,/* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_BUFSIZE)
              */
int type ,/* <I>
          Attribute Type to Search:
            UF_ATTR_bool
            UF_ATTR_integer
            UF_ATTR_real
            UF_ATTR_time
            UF_ATTR_null
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
UF_ATTR_value_p_t value /* <IOF>
                         Typed Attribute Value:
                            If "type" is UF_ATTR_string then
                            "value->value.string" must either be NULL or
                            point to a character buffer of size
                            UF_ATTR_MAX_STRING_BUFSIZE.  If the value is
                            NULL, then the returned buffer will be allocated,
                            and the user is responsible for freeing it
                            by calling UF_free().

                            If "type" is UF_ATTR_reference then
                            "value->value.string" must either be NULL or
                            point to a character buffer of size
                            UF_ATTR_MAX_STRING_BUFSIZE.  If the value is
                            NULL, then the returned buffer will be allocated,
                            and the user is responsible for freeing it
                            by calling UF_free().

                            If "value->type" = 0, then the attribute does not
                            exist for the type searched.

                            If "type" is UF_ATTR_any and the returned
                            "value->type" is UF_ATTR_string or
                            UF_ATTR_reference, then the string returned
                            was dynamically allocated and you must use
                            UF_free to deallocate the memory.

                            If "value->type" is UF_ATTR_time, then
                            the value will be in the current time zone of the
                            machine on which the program is being executed.
                         */
);

/*****************************************************************************
 * Read the reference string of the given attribute, which must be of reference type.
 *
 * If no attribute was found then a zero will be returned as the attribute's
 * type.  Passing an object tag will result in reading a value from the
 * attributes of that object. Passing in a part tag will result in reading a
 * value from the part attribute of that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_get_user_attribute or NXObject::GetUserAttribute
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_read_reference_string(
tag_t object ,/* <I>
              Part tag or object tag.
              */
char * title ,/* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_BUFSIZE)
              */
UF_ATTR_value_p_t reference_string /* <IOF>
                         Typed Attribute Value:
                            "value->value.reference" must either be NULL or
                            point to a character buffer of size
                            UF_ATTR_MAX_STRING_BUFSIZE.  If the value is
                            NULL, then the returned buffer will be allocated,
                            and the user is responsible for freeing it
                            by calling UF_free().
                         */
);

/*****************************************************************************
 * Count the number of attributes of the specified type that belong to the
 * object. If the attribute type specified is UF_ATTR_any then return
 * the count for all types.
 *
 * Passing an object tag will result in counting the attributes of
 * that object. Passing in a part tag will result in counting the
 * part attributes of that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_count_user_attributes or NXObject::GetUserAttributeCount
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_count_attributes(
tag_t object ,/* <I>
              Part tag or object tag.
              */
int type ,/* <I>
          Attribute Type:
            UF_ATTR_bool
            UF_ATTR_integer
            UF_ATTR_real
            UF_ATTR_time
            UF_ATTR_null
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
int * count  /* <O>
             Attribute Count
             */
);

/*****************************************************************************
 * Searches the specified attribute type for the attribute title. If the type
 * specified is UF_ATTR_any (or 6) then return the first attribute found with
 * the given title.
 *
 * NOTE: Callers should not rely on attributes being returned in any
 *       particular order.
 *
 * UF_ATTR_bool(8)
 * If the attribute was found then the title_type parameter returns its
 * attribute type; otherwise, a zero is returned.
 *
 * Passing an object tag will result in finding the attributes of
 * that object. Passing in a part tag will result in finding the
 * part attributes of that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: UF_ATTR_get_next_user_attribute
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_find_attribute(
tag_t object ,/* <I>
              Part tag or object tag.
              */
int type ,/* <I>
          Attribute Type:
            UF_ATTR_integer
            UF_ATTR_real,
            UF_ATTR_time
            UF_ATTR_null,
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
            UF_ATTR_bool
          */
char * title ,/* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_BUFSIZE)
              */
int * title_type  /* <O>
                  Type of Attribute Found:
                      0 = Attribute Not Found.
                      UF_ATTR_integer
                      UF_ATTR_real
                      UF_ATTR_time
                      UF_ATTR_null
                      UF_ATTR_reference
                      UF_ATTR_string
                      UF_ATTR_bool
                  */
);

/*****************************************************************************
 * Find the part attribute object for the work part.  Once the part attribute
 * object identifier is obtained, it may be used as
 * input to other routines that handle user defined attributes.
 * Each part has one and only one part attribute object.
 *
 * NOTE: This function is no longer needed for any of the UF_ATTR functions, new and old.
 *       Instead, the part tag may be used when reading and writing part attributes.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 *
 * Equivalent Functionality: None. See NOTE.
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History: Deprecated in NX 8.0
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_ask_part_attribute(
tag_t * attribute  /* <O>
                   Object Identifier of part attribute of the work part
                   */
);

/*****************************************************************************
 * Reads all the part attributes from a part file without requiring that the
 * part be opened. The values returned are always those stored on disk
 * even if the part is currently loaded in memory (use
 * UF_ATTR_ask_part_attrs for such a part). This routine is normally
 * considerably more efficient than opening the part and finding the part
 * attribute.
 *
 * Environment: Internal and External
 *
 * Equivalent Functionality: UF_ATTR_get_user_attributes_in_file
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_ask_part_attrs_in_file(
const char * part_name ,/* <I>
                        Part file name to read part attributes from or
                        part name when using NX Manager (internal name).
                        */
int * n_attributes ,/* <O>
                    Count of attributes returned.
                    */
UF_ATTR_part_attr_p_t * attributes  /* <OF,len:n_attributes>
                                    Allocated array of structures holding
                                    attribute titles and values. This must
                                    be freed by the caller using UF_free.

                                    If a returned attribute type is UF_ATTR_string or
                                    UF_ATTR_reference then the string returned
                                    was dynamically allocated and you must use
                                    UF_free to deallocate the memory.

                                    If a returned attribute type is UF_ATTR_time, then
                                    the value will be in the current time zone of the
                                    machine on which the program is being executed.
                                    */
);

/*****************************************************************************
 * Reads all of the part attributes from the specified part. The part must
 * be loaded to use this function.
 *
 * Discouraged in new applications
 * Environment: Internal and External
 *
 * Equivalent Functionality: UF_ATTR_get_user_attributes or NXObject::GetUserAttributes
 *
 * NOTE: Due to the many existing calls to this function in legacy applications,
 *       we do not intent to obsolete it, just discourage its use in new code.
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_ask_part_attrs(
const tag_t part_tag ,/* <I>
                      part tag of the part from which to read attributes.
                      */
int * n_attributes ,/* <O>
                    Count of attributes returned.
                    */
UF_ATTR_part_attr_p_t * attributes  /* <OF,len:n_attributes>
                                    Allocated array of structures holding
                                    attribute titles and values.  This must
                                    be freed by the caller using UF_free.

                                    If a returned attribute type is UF_ATTR_string or
                                    UF_ATTR_reference then the string returned
                                    was dynamically allocated and you must use
                                    UF_free to deallocate the memory.

                                    If a returned attribute type is UF_ATTR_time, then
                                    the value will be in the current time zone of the
                                    machine on which the program is being executed.
                                    */
);

/*****************************************************************************
Set the work part to a different part quietly.  Setting the work part quietly
sets the work part without updating the display in an interactive NX session.
By doing this, objects can be created in other than the current work part
(which most Open API routines currently rely on).  This routine will
return an error if the given part is not already fully loaded.

This routine should be used with great care and the previous
environment should be restored immediately.

Please avoid using this function as much as possible with the Advanced
Simulation application.

NOTE: Actions that cannot be performed interactively are not supported
with this function.



Environment: Internal  and  External

Warning:
This routine can be used when necessary to perform operations in parts which are
not the work part.  The function should always be called in pairs, once
before and once immediately after the desired operation is performed
in the other part.  Always specify the previous_work_part
returned by the first call as the part argument for the second call.
Doing many operations within the context of a work part that has been
set via this function can be a source of instabilities in the system.

Equivalent functionality:  UF_ASSEM_set_work_part_context_quietly
and  UF_ASSEM_restore_work_part_context_quietly

History: 
Deprecated in NX 11.0
*****************************************************************************/
/*  */
extern UFUNEXPORT int UF_ASSEM_set_work_part_quietly (
    tag_t   part ,              /* <I>
                                the part to become the new work part
                                */
    tag_t  *previous_work_part  /* <O>
                                the work part when this routine
                                was called (NX should be reset to
                                this immediately after completing
                                the context sensitive operations.)
                                */
);

/******************************************************************************
Resets the name and description of a specified part in the database,
given the database tag of the part.  Both the part_name and the part_desc
arguments may be specified as NULL or the empty string "". If you specify
either argument as NULL or the empty string, the appropriate field is not
set in the database.

For example, if you specify part_name to be "engine" and part_desc
to be NULL, then only the part name field is set in the database.
The UF_UGMGR_set_part_name_desc function is used to reset the name and
description of the specified part in the database.  When a part is created
using the UF_PART_new function, the name and description of the part default
to the part number. It is only when the part has been saved that you may
alter its default name and description using the UF_UGMGR_set_part_name_desc
function.

Environment: Internal  and  External

See Also:


History: Deprecated in NX11
******************************************************************************/
extern UFUNEXPORT int UF_UGMGR_set_part_name_desc(
    UF_UGMGR_tag_t database_part_tag,/* <I>
                                     Database tag of the part whose name and
                                     description we wish to reset.
                                     */
char * part_name,/* <I>
                 Name of the part.
                 */
char * part_desc /* <I>
                 Part description.
                 */
);


/****************************************************************************
*This function will initialize the UF_DRF_custom_symbol_t structure.  This
*routine should be called prior to filling this structure with valid data.
*Calling this routine will guarantee that the data structure does not
*contain garbage values.  Calling this routine WILL NOT guarantee that the
*structure will contain valid values which can be processed by
*UF_DRF_create_custom_symbol_instance.  Do not call this routine on a
*structure with valid pointers to allocated memory.  Doing that will cause
*the pointers to be reset, causing the allocated memory to become inaccessible.
*Please free any dynamically allocated memory in this structure before
*overwriting the pointers with new data.
*
*Return:      Return values include the following:
*             UF_DRF_NO_ERRORS
*             Other UF error codes
*
* NOTE: This function is no longer needed.
*       
*
*Discouraged in new applications

*Environment: Internal and External

*Equivalent Functionality: NXOpen.Annotations.MasterCustomSymbolData class should be used

* History: Deprecated in NX 1872
******************************************************************************/
extern UFUNEXPORT int UF_DRF_initialize_custom_symbol_data(
    UF_DRF_custom_symbol_p_t symbol_definition /*<I/O> Structure to initialize*/
);

/***************************************************************************
*This function will create and display a new custom symbol.  This function
*uses existing objects of the following types to form the symbol: lines,
*arcs, splines, parabolas, hyperbolas, B-curves, crosshatch, area fill, and
*notes.  All objects which are passed into this routine via the data structure
*are consumed by the function call (they are not available for use as
*individual objects after this function returns).
*
*The symbol scale and angle may be edited, as well as its color, font, and
*width.  However, all other edits (such as text-specific edits, or display
*edits of symbol pieces) must be performed interactively at this time.
*
*Return:    Return values include the following:
*UF_DRF_invalid_custom_symbol_piece
*UF_DRF_default_text_out_of_bounds
*UF_DRF_objects_not_in_same_view
*UF_DRF_NO_ERRORS
*
*Environment: Internal and External
*
*See Also: UF_DRF_is_sbf_symbol, UF_DRF_initialize_custom_symbol_data,
*UF_DRF_ask_custom_symbol_scale, UF_DRF_set_custom_symbol_scale,
*UF_DRF_ask_custom_symbol_angle, UF_DRF_set_custom_symbol_angle
*
*
* NOTE: This function is no longer needed.
*
*
*Discouraged in new applications

*Environment: Internal and External

*Equivalent Functionality: NXOpen.Annotations.MasterSymbolBuilder and NXOpen.Annotations.CustomSymbolBuilder class should be used

* History: Deprecated in NX 1872
*****************************************************************************/
extern UFUNEXPORT int UF_DRF_create_custom_symbol_instance(
    const UF_DRF_custom_symbol_t *  symbol_definition,  /*<I> Structure containing
                                                        data necessary for
                                                        custom symbol definition*/
    tag_t *                         new_symbol_tag      /*<O> The tag of the new
                                                        custom symbol instance*/
);

/*******************************************************************************
Query the number of features which are out of date.

Environment: Internal  and  External
See Also:
History: This function was originally released in V16.0.
Deprecated in NX2306.
The definition of "out of date" has changed in the time since this function was first introduced. This function is finding features that have update failures instead of out of date features. Please use NXOpen.Part.GetUpdateStatusReport to find feature failures and NXOpen.Features.Feature.IsOutOfDate to determine if a feature is out of date.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_out_of_date_features(
    int       *num_feature, /* <O>
                            Number of out of date features.
                            */
    tag_t     **features   /* <OF,len:num_feature>
                           Array of features which are out of date.  This array
                           must be freed by calling UF_free.
                           */
);

/******************************************************************************
Sews sheet bodies or faces of solid bodies together.  When sewing solids, the
arrays targets and tools contain the faces from the target and tool bodies.  The
faces from one body must match in geometry with the faces from the other body.
It is important to understand the interactive functionality in NX before trying
to use this function.

 NOTE: This function is no longer needed.
     
Discouraged in new applications

Equivalent Functionality: NXOpen::Features::Sew builder class should be used

Environment: Internal  and  External
See Also:  UF_MODL_create_multiple_sews
           UF_MODL_ask_sew_sheet_body
           UF_MODL_edit_sew_sheet_body
           UF_MODL_ask_sew_solid_body
           UF_MODL_edit_sew_solid_body
History:
Deprecated in NX2306.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_sew(
    int option,/* <I>
                Option flag:
                0 = Sew general
                1 = Sew all instances
                */
    int num_targets,/* <I>
                     Size of the targets array
                     */
    tag_t targets[],/* <I,len:num_targets>
                     Array of target tags ( sheet body when type_body = 0
                          or face(s) from a solid body when type_body = 1 ).
                     */
    int num_tools,/* <I>
                     Size of the tool array
                     */
    tag_t tools[],/* <I,len:num_tools>
                     Array of tool tags ( sheet body when type_body = 0
                        or face(s) from a solid body when type_body = 1 ).
                   */
    double tolerance,/* <I>
                      Tolerance value
                      */
    int type_body,/* <I>
                   Type of body:
                   0 = Sheet (default)
                   1 = Solid
                   */
    uf_list_p_t *disjoint_list,/* <OF,free:UF_MODL_delete_list>
                                 List contains disjoint sheets from the target.
                                 This list must be freed by calling
                                 UF_MODL_delete_list.
                                 */
    tag_t *sew_id  /* <O>
                    The sew feature that was created.
                    */
);
/*******************************************************************************
Create multiple sewn sheets from a set of sheets.  This routine returns a list
of sheet bodies.  If you want the sew features, they can be obtained by calling

 NOTE: This function is no longer needed.
     
Discouraged in new applications

Equivalent Functionality: NXOpen::Features::Sew builder class should be used

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_ask_sew_sheet_body
           UF_MODL_edit_sew_sheet_body
           UF_MODL_ask_sew_solid_body
           UF_MODL_edit_sew_solid_body
History: Modified in V15 to return a list of sheet bodies, not a list of SEW
features
Deprecated in NX2306.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_multiple_sews(
    tag_t target_sheet,/* <I>
                        Target sheet
                        */
    int num_tools,/* <I>
                   Number of tools sheet array.
                   */
    tag_t tools_sheet[],/* <I,len:num_tools>
                         Tools sheet array.
                         */
    double tolerance,/* <I>
                      tolerance value.
                      */
    uf_list_p_t *disjoint_list,/* <OF,free:UF_MODL_delete_list>
                                List of disjoint sheets.  This list must be freed
                                by calling UF_MODL_delete_list.
                                */
    uf_list_p_t *sew_list  /* <OF>
                           List of sewn sheets.  These are sheet bodies.
                           If you want the sheet feature, then you must call
                           UF_MODL_ask_body_features and then search the list
                           for the latest SEW feature.  This list must be freed
                           by calling UF_MODL_delete_list.
                           */
);
/******************************************************************************
Returns the information stored in the record of the input sew sheet body feature.

 NOTE: This function is no longer needed.
     
Discouraged in new applications

Equivalent Functionality: NXOpen::Features::Sew builder class should be used

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_create_multiple_sews
           UF_MODL_edit_sew_sheet_body
History: Original release was in V16.0.1.
Deprecated in NX2306.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sew_sheet_body
(
    tag_t   feature_obj_eid,       /* <I> Feature object id of trimmed sheet.  */
    tag_t *target_sheet_body,     /* <O> Tag of the target sheet body */
    int *tool_sheet_bodies_count,/* <O> Number of tool sheet bodies */
    tag_t **tool_sheet_bodies,      /* <OF,len:tool_sheet_bodies_count> Array of NX eids of sheet bodies.
                                            This array must be freed by calling UF_free.  */
    double *tolerance               /* <O> Distance tolerance for approximations.  */
);

/******************************************************************************
Returns the information stored in the record of the input sew solid body feature.

 NOTE: This function is no longer needed.
     
Discouraged in new applications

Equivalent Functionality: NXOpen::Features::Sew builder class should be used

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_edit_sew_solid_body
History: Original release was in V16.0.1.
Deprecated in NX2306.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sew_solid_body
(
    tag_t   feature_obj_eid,   /* <I> Feature object id of trimmed sheet.  */
    int *target_faces_count,/* <O> Number of faces on the target body to be sewn */
    tag_t **target_faces,      /* <OF,len:target_faces_count> Array of NX eids of faces on the target body
                                       to be sewn. This array must be freed by
                                       calling UF_free.  */
    int *tool_faces_count,  /* <O> Number of faces on the tool body to be sewn */
    tag_t **tool_faces,        /* <OF,len:tool_faces_count> Array of NX eids of faces on the tool body
                                       to be sewn. This array must be freed by
                                       calling UF_free.  */
    double *tolerance          /* <O> Distance tolerance for approximations.  */
);

/******************************************************************************
Modifies data of the input sew sheet bodies feature to the specified
tool bodies and tolerance conditions specified in the inputs.

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_create_multiple_sews
           UF_MODL_ask_sew_sheet_body
History: Original release was in V16.0.1.
Deprecated in NX2306.

 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_sew_sheet_body
(
    tag_t  feature_obj_eid,/* <I> Feature object id of sew feature.  */
    tag_t  new_target_eid,  /* <I> The NX eid of the the new target sheet body.
                                   This option will be available in V17. */
    int    tool_body_count, /* <I> Number of tool sheet bodies */
    tag_t *tool_body_eids,  /* <I,len:tool_body_count>
                                   Array of NX eids of sheet bodies */
    double tolerance        /* <I> Distance tolerance for approximations */
);

/******************************************************************************
Modifies data of the input sew solid bodies feature to the specified
tool and target faces and tolerance conditions specified in the inputs.

 NOTE: This function is no longer needed.
     
Discouraged in new applications

Equivalent Functionality: NXOpen::Features::Sew builder class should be used

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_ask_sew_solid_body
History: Original release was in V16.0.1.
Deprecated in NX2306.

 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_sew_solid_body
(
    tag_t     feature_obj_eid,  /* <I> Feature object id of trimmed sheet.  */
    int       target_faces_count,/* <I> Number of faces on the target body to be sewn */
    tag_t *target_faces,      /* <I,len:target_faces_count>
                                       Array of NX eids of faces on the target body
                                       to be sewn. This array must be freed by
                                       calling UF_free.  */
    int       tool_faces_count,  /* <I> Number of faces on the tool body to be sewn */
    tag_t *tool_faces,        /* <I,len:tool_faces_count>
                                       Array of NX eids of faces on the tool body
                                       to be sewn. This array must be freed by
                                       calling UF_free.  */
    double    tolerance          /* <I> Distance tolerance for approximations.  */
);

/****************************************************************************
Creates a solid of revolution.

 NOTE: This function is no longer needed.
     
Discouraged in new applications

Equivalent Functionality: NXOpen.Features.RevolveBuilder class should be used

Environment: Internal  and  External
See Also:
History:Deprecated in NX2306.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_revolved(
    uf_list_p_t obj_id_list,/* <I>
                               List of objects or one section builder object tag
                               but not both, to be revolved
                             */
    char *limit[2],/* <I>
                   Limits of revolution. The declaration should be
                   *limit[2], where limit[0] = start angle and limit[1] =
                   end angle. Angles are in degrees.
                   */
    double point[3],/* <I>
                     Point
                     */
    double direction[3],/* <I>
                         Revolution axis.
                         */
    UF_FEATURE_SIGN sign,/* <I>
                          The sign of the operation to be performed.
                          UF_NULLSIGN = create new target solid
                          UF_POSITIVE = add to target solid
                          UF_NEGATIVE = subtract from target solid
                          UF_UNSIGNED = intersect with target solid
                          */
    uf_list_p_t *feature_list  /* <OF,free:UF_MODL_delete_list>
                                List of feature identifiers created.  This
                                list must be freed by calling UF_MODL_delete_list.
                                */
);

/*************************************************************************
Creates a solid of revolution, and performs Boolean operation with given
target body.

 NOTE: This function is no longer needed.
     
Discouraged in new applications

Equivalent Functionality: NXOpen.Features.RevolveBuilder class should be used

Environment: Internal  and  External
See Also:  UF_MODL_create_revolved
History: Originally released in V16.0.
Deprecated in NX2306.
*********************************************************************/
extern UFUNEXPORT int UF_MODL_create_revolved1(
    uf_list_p_t obj_id_list,/* <I>
                                List of objects or one section builder object tag
                                but not both, to be revolved
                             */
    char *limit[2],/* <I>
                   Limits of revolution. The declaration should be
                   *limit[2], where limit[0] = start angle and limit[1] =
                   end angle. Angles are in degrees.
                   */
    double point[3],/* <I>
                     Point
                     */
    double direction[3],/* <I>
                         Revolution axis.
                         */
    UF_FEATURE_SIGN sign,/* <I>
                          The sign of the operation to be performed.
                          UF_NULLSIGN = create new target solid
                          UF_POSITIVE = add to target solid
                          UF_NEGATIVE = subtract from target solid
                          UF_UNSIGNED = intersect with target solid
                          */
    tag_t         target_body,   /* <I> Boolean target */
    uf_list_p_t *feature_list  /* <OF,free:UF_MODL_delete_list>
                                List of feature identifiers created.  This
                                list must be freed by calling UF_MODL_delete_list.
                                */
);

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

/* Routing structures not used in UGOpen interface any more */

// 
typedef void* (*UF_RULE_check_function_f_t)(tag_t   rule,/* <I> Rule to check */
    void* data /* <I> Client data   */);

typedef struct ROUTE_plugin_s UF_ROUTE_plugin_t, *UF_ROUTE_plugin_p_t;

/*
    The UF_ROUTE_bundle_data_s structure is the structure that is used
    to pass information to and receive information from a user written
    bundle diameter calculation routine. In Wiring, you may define
    a "Plug-in" for the routine that calculates the set of curves that
    should be used to model the cross section of the wire bundle based
    on the number of wires in the bundle (and their diameters). This
    is the structure that is supplied to your bundle diameter routine.
*/
struct UF_ROUTE_bundle_data_s
{
    int     num_wires;
    tag_t* wires; /* <len:num_wires> */
    int     num_stock_data;
    tag_t* stock_data; /* <len:num_stock_data> */
    int     num_cross_sections;
    tag_t* cross_sections;/* <len:num_cross_sections> */
    int     num_anchors;
    tag_t* anchors;/* <len:num_anchors> */
};
typedef struct UF_ROUTE_bundle_data_s 
            UF_ROUTE_bundle_data_t, *UF_ROUTE_bundle_data_p_t;

/* The UF_ROUTE_cda_data_s is the structure that holds the data required to
   run the cable drawing automation program as a user-function utility from
   the wiring interface. This structure indicates the number of records
   selected and the selected connection list tags in the Rlist navigator
*/
struct UF_ROUTE_cda_data_s
{
    int num_recs;
    tag_t* recs; /* <len:num_recs> */
};
typedef struct UF_ROUTE_cda_data_s UF_ROUTE_cda_data_t, *UF_ROUTE_cda_data_p_t;

/* The UF_ROUTE_iman_bom_data_s is the structure used to implement the
   Routing Team Center Engineering BOM post piping parts list callback.
   It is currently empty but may be implemented in the future. */
struct UF_ROUTE_iman_bom_data_s
{
    logical place_holder;
};
typedef struct UF_ROUTE_iman_bom_data_s 
            UF_ROUTE_iman_bom_data_t, *UF_ROUTE_iman_bom_data_p_t;

/*
   Bit mask of options used in the UF_ROUTE_pcf_gen_data_s structure's options.
*/
enum UF_ROUTE_pcf_options_e
{
    UF_ROUTE_PCF_ASK_TO_OVERWRITE_FILE = (1 << 1),
    UF_ROUTE_PCF_NEVER_OVERWRITE_FILE = (1 << 2),
    UF_ROUTE_PCF_ALWAYS_OVERWRITE_FILE = (1 << 3)
};

typedef enum UF_ROUTE_pcf_options_e UF_ROUTE_pcf_options_t, *UF_ROUTE_pcf_options_p_t;

/* Structure passed to the STOCK_COMPONENT_LOOKUP plugin. */
struct UF_ROUTE_component_reuse_plugin_s
{
    tag_t   stock;
    /* Input:   Tag of the stock object */

    tag_t   new_stock_component;
    /* Output:  Tag of the part to replace the
                stock component with. */
};
typedef struct UF_ROUTE_component_reuse_plugin_s
UF_ROUTE_component_reuse_plugin_t, * UF_ROUTE_component_reuse_plugin_p_t;

/* Structure passed to the STOCK_COMPONENT_LOCKED plugin. */
struct UF_ROUTE_component_lock_plugin_s
{
    tag_t   stock;
    /* Input:   Tag of the stock object */

    logical is_modifiable;
    /* Output:  TRUE if stock component can be modified,
                FALSE otherwise. */
};
typedef struct UF_ROUTE_component_lock_plugin_s
UF_ROUTE_component_lock_plugin_t, * UF_ROUTE_component_lock_plugin_p_t;

/* Structure passed to the ALLOW_DEFAULT_ELBOW_PLACEMENT plugin. */
struct UF_ROUTE_allow_default_fitting_plugin_s
{
    tag_t                           rcp;
    /*  Input:  The rcp to place the fitting at.  */

    int                             num_spec_charx;
    /* Input:   Specification characteristics.  Each specification characteristic
                can have one or more possible values.  Default part selection ensures
                that every matching part has at least one of the values from a
                multi valued specification characteristic.
                Eg: If FITTING_MATERIAL is a specification characteristic and
                    has values COPPER, STEEL - all matching parts have a
                    FITTING_MATERIAL value of either COPPER or STEEL.
     */
    UF_EPLIB_multi_val_charx_p_t    spec_charx; /*<len:num_spec_charx>*/

    UF_EPLIB_part_lib_part_t        match_criteria;
    /* Input:   Part descriptor characteristics that are not in the specification
                 characteristic list.  Part descriptor characteristics can
                only be single valued. These characteristics help uniquely
                determine the default fitting to place.
     */

    const char* default_fitting_table;
    /* Input:   Part library table identifier to use for determining the default fitting.
                The identifier is defined in the Part Library View file for the application.
     */

    logical                         allow_placement;
    /* Output:  if TRUE, default elbow placement at the input RCP is valid */

    logical                         force_override;
    /* Output:  if TRUE, forces placement of the part specified in the
     *          the override_fitting definition. */

    UF_EPLIB_part_lib_part_t        override_fitting;
    /* Output:  Only used if force_override is TRUE.  Fully specifies the default fitting
                to place [include values of all selection characteristics].
     */
};
typedef struct UF_ROUTE_allow_default_fitting_plugin_s
            UF_ROUTE_allow_default_fitting_plugin_t, *UF_ROUTE_allow_default_fitting_plugin_p_t;

/* Structure passed to the SPECIFY_ITEM plugin.
 *
 * The SPECIFY_ITEM plugin selects a part, stock, elbow,
 * wire, cable, or shield conforming to the given
 * characteristics.
 *
 * The SPECIFY_ITEM plugin must filter the selected part
 * based on the current discipline and specification by
 * calling the FilterOnCurrentSpecifications routine.
 */
struct UF_ROUTE_specify_item_plugin_s
{
    int                             mode;
    /*  Input:  Specifies the type of item (e.g. part, stock, elbow, etc.)
     *          Valid values: (See uf_ui_route.h)
     *          UF_UI_ROUTE_PLV_INDEX_PARTS
     *          UF_UI_ROUTE_PLV_INDEX_STOCK,
     *          UF_UI_ROUTE_PLV_INDEX_ELBOWS
     *          UF_UI_ROUTE_PLV_INDEX_CUT_ELBOWS,
     *          UF_UI_ROUTE_PLV_INDEX_REPLACE_PART
     *          UF_UI_ROUTE_PLV_INDEX_WIRES,
     *          UF_UI_ROUTE_PLV_INDEX_CABLES
     *          UF_UI_ROUTE_PLV_INDEX_SHIELDS
     */

    const char* node_id;
    /*  Input:  Specifies the name/ID of the node in the
     *          Product Library View under which to look
     *          for matching characteristics.
     */

    int                             num_specifications;
    const char** specifications;
    /*  Input:  Specifies all of the disciplines and specifications
     *          that are currently valid.  Reserved for future use.
     */

    UF_EPLIB_part_lib_part_t        chosen_part;
    /*  Input:  Characteristics structure used to for item selection.
     *          Represents the characteristics from a part chosen by
     *          the user before calling the plug-in.
     *
     *  Output: Characteristics of the part the user selected while
     *          running the plug-in.
     */

    tag_t                           placer_object;
    /*  Output: Selected placement object.  A condemned point to stand in
    *           for screen position pick.  Will be a NULL_TAG in Assign
    *           Stock (UF_UI_ROUTE_PLV_INDEX_STOCK) mode.
    */

    double                          placer_object_pos[3];
    /*  Output: Placement position in Work Occurrence coordinates.
    */

    int                             error;
    /*  Output:  Zero indicates success
     */
};

typedef struct UF_ROUTE_specify_item_plugin_s
            UF_ROUTE_specify_item_plugin_t, *UF_ROUTE_specify_item_plugin_p_t;

/* Structure passed to the CHARACTERISTIC_MATCH plugin.
 *
 * The CHARACTERISTIC_MATCH plugin selects a set of parts
 * or a set of stocks conforming to the given
 * criteria.
 *
 * The CHARACTERISTIC_MATCH plugin must filter the selected part
 * based on the current discipline and specification by
 * calling the FilterOnCurrentSpecifications routine.
 */
struct UF_ROUTE_characteristic_match_plugin_s
{
    const char* node_id;
    /*  Input:  Specifies the name/ID of the node in the
     *          Product Library View under which to look
     *          for matching characteristics.
     */

    int                             num_criteria;
    UF_EPLIB_charx_p_t              criteria;
    /*  Input:  Characteristics structure used to for item selection.
     */

    int                             num_matches;
    UF_EPLIB_part_lib_part_p_t      matches;
    /*  Output: Characteristics of the parts that match the criteria.
     */

    int                             error;
    /*  Output:  Zero indicates success
     */
};

typedef struct UF_ROUTE_characteristic_match_plugin_s
            UF_ROUTE_characteristic_match_plugin_t, *UF_ROUTE_characteristic_match_plugin_p_t;

/* The plugin for Duct Reinforcement uses this enumeration to tell the dialog
 the type of reinforcement to create*/
enum UF_ROUTE_duct_reinforcement_types_e
{
    UF_ROUTE_DUCT_REINFORCEMENT_TYPE_NONE,      /* No reinforcement needs to be created on the selected duct */
    UF_ROUTE_DUCT_REINFORCEMENT_TYPE_INSIDE,    /* Inside reinforcement needs to be created on the selected duct */
    UF_ROUTE_DUCT_REINFORCEMENT_TYPE_OUTSIDE    /* Outside reinforcement needs to be created on the selected duct */
};

typedef enum UF_ROUTE_duct_reinforcement_types_e UF_ROUTE_duct_reinforcement_types_t,
                *UF_ROUTE_duct_reinforcement_types_p_t;

/* The duct reinforcement plugin evaluates the parent duct selected and determines
 the various parameters for duct reinforcement creation. These parameters are
 stored using the following struct.*/
struct UF_ROUTE_duct_reinforcement_parameters_s
{
    UF_ROUTE_duct_reinforcement_types_t     reinforcementType;                 /* Type of reinforcement to be applied options are None, Inside or Outside */
    logical                                 parallelStockBlockVisibility;      /* Parallel Stock Block Visibility */
    UF_EPLIB_part_lib_part_t                parallelStock;                     /* Stock to be applied parallel to axis of the duct */
    int                                     numberOfPairs;                     /* Number of pairs of parallel reinforcements to be applied */
    double                                  spacing;                           /* Space between each pair of reinforcement applied parallel to axis of the duct */
    logical                                 perpendicularStockBlockVisibility; /* Perpendicular Stock Block Visibility */
    logical                                 reinforcementTypeBlockVisibility;  /* Reinforcement Type Visibility */
    UF_EPLIB_part_lib_part_t                perpendicularStock;                /* Stock to be applied perpendicular to axis of the duct */
    double                                  interval;                          /* Interval at which perpendicular stock is to be applied */
    double                                  clearnce;                          /* Minimum clearance value from the start and end of the parent duct */
    logical                                 editMode;                          /* Is the plugin invoked during edit of duct reinforcement*/
};

typedef struct UF_ROUTE_duct_reinforcement_parameters_s UF_ROUTE_duct_reinforcement_params_t,
            *UF_ROUTE_duct_reinforcement_params_p_t;

/* Output data structure */
struct UF_ROUTE_cb_data_out_s
{
    char   part_name[UF_ATTR_MAX_STRING_BUFSIZE];       /* part name, E.g. "pipe_flg_blind"  */
    char   member_name[UF_ATTR_MAX_STRING_BUFSIZE];     /* member name , E.g., "p3036" */
    char   part_number[UF_ATTR_MAX_STRING_BUFSIZE];     /* part number, E.g., "EDS-3002" */
    int    num_charx;                               /* number of charx */
    UF_EPLIB_part_lib_part_t* part;
    UF_EPLIB_charx_p_t   charx_list;                /* charx list  */
};
typedef struct UF_ROUTE_cb_data_out_s UF_ROUTE_cb_data_out_t, * UF_ROUTE_cb_data_out_p_t;


/******************************************************************************
Adds conics to the current sketch.

The following restrictions applies:
1) UF_SKET_initialize_sketch must have been previously called.
2) The construction coordinate system of the conic you wish to add must be
parallel to the sketch plane for legacy sketches.
3) Object has to be either a hyperbola, parabola, or a partial ellipse
   with angular span smaller than 180 degree.

Environment: Internal and External

See Also: UF_SKET_initialize_sketch

For new sketches, use <ja_method>NXOpen.Sketch.AddGeometry</ja_method>

History: This function was originally released in V17.0
******************************************************************************/
extern UFUNEXPORT int UF_SKET_add_conics
(
 tag_t sketch_tag,    /* <I>  Sketch tag.                      */
 int count,           /* <I>  Number of conics to be added.   */
 tag_t *object        /* <I,len:count>
                              Array of conics to be added to the sketch */
);

/******************************************************************************
This routine adds extracted objects to a legacy sketch. New objects, extracted
from the input objects and become associative with the input objects, will
be added to the sketch.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal and external.

See Also: UF_SKET_initialize_sketch

For new sketches, use <ja_method>NXOpen.SketchCollection.CreateProjectBuilder</ja_method>

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_add_extracted_objects
(
 tag_t  sketch_tag, /* <I> Sketch tag                            */
 int    count,      /* <I> Number of objects to be extracted     */
 tag_t  *objects,   /* <I,len:count>
                           Array of objects to be extracted      */
 int    output_mode,/* <I> Output mode
                           UF_SKET_EXTR_ORIG_TYPE
                           UF_SKET_EXTR_MULTI_SPLINES
                           UF_SKET_EXTR_SINGLE_SPLINE
                    */
 int    *num_extracted_objs, /* <O>  Number of extracted objects */
 tag_t  **extracted_objs     /* <OF,len:num_extracted_objs>
                             Array of extracted objects.
                                Use UF_free to deallocate memory when done.
                             */
);

/******************************************************************************
This function returns the constaint class of the given constraint tag.

Environment: Internal  and  External

See Also:
For new sketches, use <ja_class>NXOpen.SketchDimensionalConstraint</ja_class>

History: This function was originally released in V17.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_constraint_class
(
 tag_t                con_tag,    /* <I> Constraint tag */
 UF_SKET_con_class_t *con_class   /* <O>
                                     Constraint class:
                                     - UF_SKET_geo_cons
                                     - UF_SKET_dim_cons
                                  */
);

/******************************************************************************
This function finds the constaint type

Environment: Internal  and  External

See Also:
For new sketches, use <ja_method>NXOpen.SketchConstraint.ConstraintType</ja_method>

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_constraint_type
(
   tag_t con_tag,                /* <I>  Constraint tag          */
   UF_SKET_con_type_t  *con_type /* <O>  The type of constraint  */
);

/******************************************************************************
This function finds all the geometric constraints associated with a geometry.

Environment: Internal  and  External

See Also: UF_SKET_ask_constraints_of_geometry

For new sketches, use <ja_method>NXOpen.SketchGeometricConstraint.GetGeometry</ja_method>

History: V17 change: This function was renamed from UF_SKET_ask_constraints_of_geometry,
         which was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_geo_cons_of_geometry
(
   tag_t sketch_tag, /* <I>  Sketch tag.             */
   tag_t geom_tag,   /* <I>  Tag of the geometry.    */
   int   *con_num,   /* <O>  Number of constraints.  */
   tag_t **con_tags  /* <OF,len:con_num>
                             Array of constraints.
                        Use UF_free to deallocate memory when done.
                     */
);

/******************************************************************************
This function finds all the constraints, with the specified class, associated
 with a geometry.

Environment: Internal  and  External

See Also: UF_SKET_ask_geo_cons_of_geometry

For new sketches, use <ja_method>NXOpen.Sketch.GetConstraintsForGeometry</ja_method>

History: V17 change: This function is new for V17.0. Although the
         function's name is not new, the parameter list has changed.

        Past callers of the UF_SKET_ask_constraints_of_geometry function
        should replace their calls by UF_SKET_ask_geo_cons_of_geometry or
        may use this function with additional parameter 'con_class' set to
        SKET_geo_cons to get the same result as before.

******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_constraints_of_geometry
(
tag_t               sketch_tag, /* <I> Sketch tag */
tag_t               geom_tag,   /* <I>  Tag of the geometry.    */
UF_SKET_con_class_t con_class,  /* <I>
                                   Constraint class:
                                   - UF_SKET_all_cons
                                   - UF_SKET_geo_cons
                                   - UF_SKET_dim_cons
                                */
int                 *con_num,   /* <O> Number of output constraints */
tag_t              **con_tags   /* <OF,len:con_num>
                                   Array of constraints of the sketch.
                                    Use UF_free to deallocate memory when done.
                                */
);

/*******************************************************************************
Output geometric constraints of a given sketch.

Environment: Internal  and  External


See Also: UF_SKET_ask_constraints_of_sketch

For new sketches, use <ja_method>NXOpen.Sketch.GetAllConstraintsOfType</ja_method>

History: V17 change: This function was renamed from UF_SKET_ask_constraints_of_sketch,
         which was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_geo_cons_of_sketch
(
 tag_t     sketch_tag,   /* <I> Sketch tag */
 int       *num_cons,    /* <O> Number of output constraints */
 tag_t     **con_tags    /* <OF,len:num_cons>
                                Array of constraints of the sketch.
                            Use UF_free to deallocate memory when done.
                         */
);

/*******************************************************************************
Output constraints, with the specified class, of a given sketch.


Environment: Internal  and  External

See Also: UF_SKET_ask_geo_cons_of_sketch

For new sketches, use <ja_method>NXOpen.Sketch.GetAllConstraintsOfType</ja_method>

History: V17 change: This function is new for V17.0. Although the
         function's name is not new, the parameter list has changed.

        Past callers of the UF_SKET_ask_constraints_of_sketch function
        should replace their calls by UF_SKET_ask_geo_cons_of_sketch or
        may use this function with additional parameter 'con_class' set
        to SKET_geo_cons to get the same result as before.

*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_constraints_of_sketch
(
tag_t               sketch_tag, /* <I> Sketch tag */
UF_SKET_con_class_t con_class,  /* <I>
                                   Constraint class:
                                   - UF_SKET_all_cons
                                   - UF_SKET_geo_cons
                                   - UF_SKET_dim_cons
                                */
int                 *num_cons,  /* <O> Number of output constraints */
tag_t              **con_tags   /* <OF,len:num_cons>
                                    Array of constraints of the sketch.
                                    Use UF_free to deallocate memory when done.
                                */
);

/******************************************************************************
Returns the current values for each of the sketch preference
variables applicable for legacy sketches created in V13.0 and beyond.
To determine if this function should be called instead of
UF_SKET_ask_legacy_preferences, use UF_OBJ_ask_type_and_subtype and check for
UF_v13_sketch_subtype.

Environment: Internal and External

See Also: UF_SKET_ask_legacy_preferences
          UF_SKET_set_preferences
          UF_SKET_set_legacy_preferences

History: V15.0 change: This function is new for V15.0. Although the
         function's name is not new, the parameter list has changed.

         NX6   change: Sketches no longer have a  'character size' and 'decimal places'
         preference. Each individual dimension will have these preferences.
         The parameter list for this function will not change, but the values returned
         for 'character size' and 'decimal places' will always be the global annotation 
         preferences.

For new sketches, use <ja_class>NXOpen.Preferences.PartSketch</ja_class> or 
                      <ja_class>NXOpen.Preferences.SessionSketch</ja_class>

*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_preferences
(
 tag_t    sketch_tag,  /* <I> Tag of input sketch; May be set to
                          NULL_TAG if there is not a particular
                          sketch which the user wants to query.
                       */
 double   *snap_angle,                    /* <O> Snap angle preference */
 char     name_prefix[ UF_OBJ_NAME_BUFSIZE ],   /* <O> Prefix for new sketch names */
 char     vertex_prefix[ UF_OBJ_NAME_BUFSIZE ], /* <O> Prefix for vertex names */
 char     line_prefix[ UF_OBJ_NAME_BUFSIZE ],   /* <O> Prefix for line names */
 char     arc_prefix[ UF_OBJ_NAME_BUFSIZE ],    /* <O> Prefix for arc names */
 char     conic_prefix[ UF_OBJ_NAME_BUFSIZE ],  /* <O> Prefix for conic names */
 char     spline_prefix[ UF_OBJ_NAME_BUFSIZE ], /* <O> Prefix for spline names */
 double   *char_size,                     /* <O> Character size is no longer a sketch preference. This parameter
                                             will always return the global annotation preferences- dimension
                                             character size */
 int      *dec_places,                    /* <O> Decimal places are no longer a sketch preference. This parameter
                                             will always return the global annotation preferences- dimension
                                             decimal places */
 int      *dim_label                      /* <O> Dimension Label:
                                                 1 = value
                                                 2 = expression
                                                 3 =  name
                                          */
);

/*******************************************************************************
This routine returns the given legacy sketch's status and the degrees of freedom
needed to make the sketch full-constrained if it is currently
under-constrained.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch

For new sketches, use <ja_method>NXOpen.Sketch.GetStatus</ja_method>

History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_sketch_status
(
 tag_t            sketch_tag,    /* <I> Sketch tag */
 UF_SKET_status_t *sket_status,  /* <O> Sketch's current status.
                                        (See type UF_SKET_status_t in
                                        uf_sket_types.h for valid values).
                                 */
 int              *dof_needed    /* <O> Degrees of freedom needed to make the
                                        sketch fully-constrained. This value
                                        is meaningful only when sketch's status
                                        is UF_SKET_under_constrained.
                                 */

);

/*******************************************************************************
This routine returns the active sketch, or NULL_TAG if none active
This function is valid only for modeling sketches created in V13.0 and later
versions of NX.

Environment: Internal  and  External

For new sketches, use <ja_method>NXOpen.Session.ActiveSketch</ja_method>

History: This function was originally released in NX5.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_active_sketch
(
 tag_t          * sketch_tag    /* <O> Active sketch tag, NULL_TAG if none  */

);

/****************************************************************************
This routine creates sketch geometry constraints of the specified type.
Not all parameters are required based on the type of constraint being
created. Refer to the descriptions below to determine which parameters
are used for each type of sketch constraints.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_delete_constraints
          UF_SKET_initialize_sketch
          UF_SKET_read_geometric_constraint
          UF_SKET_update_sketch

For new sketches, use <ja_method>NXOpen.SketchCollection.CreateConstraintBuilder</ja_method>

History: V17 change: This function was renamed from UF_SKET_create_constraint, which
         was originally released in V16.0.
****************************************************************************/
extern UFUNEXPORT int UF_SKET_create_geometric_constraint
(
 tag_t                sketch_tag,     /* <I>  Sketch tag.               */
 UF_SKET_con_type_t   con_type,       /* <I>  Constraint type.
                                         Valid types are:
                                          UF_SKET_fixed
                                          UF_SKET_horizontal
                                          UF_SKET_vertical
                                          UF_SKET_constant_length
                                          UF_SKET_constant_angle
                                          UF_SKET_uniform_scaled
                                          UF_SKET_non_uniform_scaled
                                          UF_SKET_parallel
                                          UF_SKET_perpendicular
                                          UF_SKET_collinear
                                          UF_SKET_equal_length
                                          UF_SKET_equal_radius
                                          UF_SKET_coincident
                                          UF_SKET_concentric
                                          UF_SKET_midpoint
                                          UF_SKET_slope
                                          UF_SKET_tangent
                                          UF_SKET_point_on_curve
                                          UF_SKET_point_on_string
                                      */
 int                   num_con_geoms, /* <I> Number of constraint geometries */
 UF_SKET_con_geom_t   *con_geoms,     /* <I,len:num_con_geoms>
                                         Array of constraint geometries
                                         (See type UF_SKET_con_geom_t in
                                         file uf_sket_types.h for the
                                         structure members).
                                      */
 tag_t                 *con_tag       /* <O> The tag of the created
                                         geometric constraint.
                                      */
);

/***************************************************************************


Some background and terminology
********************************

   All geometris used in a sketch can be broadly categorized into
   "External Reference Geometry" and "Internal Geometry":

   * Internal Geometry
     These are the regular point and curves (lines/arcs/ellipse/splines)
     that were created when a sketch is activated or were created outside
     the sketch but added to the sketch later. Currently, parabola and
     hyperbola are not supported as internal geometris.

   * External Reference Geometry
     These geometries are mainly used as reference for internal geometries.
     They are considered as 'fixed' objects for the sketch in question.
     Currently, external reference geometries could be non-sketch point/curves,
     point/curves belonging to sketches other than the one in question,
     datum planes, datum axis, and solid edges. Parabola and hyperbola
     cannot be used as external reference geometry either.

     NOTES:
       To be able to use curves in other sketches, datum planes, datum axis
       and solid edges as external reference for a sketch, they must be
       created before the sketch in question is created.
       For using non-sketch point/curves as external reference, there is no
       such a restriction.


  The UF_SKET_con_geom_t structure could represent an object itself or
  a vertex of the object.

  * Vertex Geometry

    When UF_SKET_con_geom_t is used to represent a vertex of an object,
    you need to set the 'geom_tag' to the tag of the object and the
    'vertex_type' to an appropriate value (ref.: the enum type
    UF_SKET_geom_vertex_t in uf_sket_types.h). You will also need to provide
    the 'vertex_index' (starting from 1) for spline's defining points. We will
    refer UF_SKET_con_geom_t of this kind by "Vertex Geometry".

  * Line/Circle/Ellipse/Spline/DatumAxis/DatumPlane Geometry

    When using UF_SKET_con_geom_t to represent an object, simply set the
    'geom_tag' to the tag of the object and the 'vertex_type' to
    UF_SKET_no_vertex. Depending on the types of the objects, they are
    referred as "Line Geometry", "Circle Geometry", ...etc.
    Notes that solid edges with line/circle/ellipse/spline as its underlying
    geometry are also referred as "Line/Circle/Ellipse/Spline Geometry".

  * Help data

    Help data are used to indicate the whereabouts on the geometry a
    constraint should apply to. They are only needed when the constraints
    are of type UF_SKET_tangent, UF_SKET_point_on_curve, and
    UF_SKET_point_on_string unless the geometry involved is a line or a
    straight edge. Help data is specified by either specifing a help point
    or a help parameter in the UF_SKET_con_geom_t structure.



The valid constraint geometry input for each constraint type
****************************************************************

       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Following constraint types require exactly one constraint geometry,
        which must be an internal geometry to the sketch specified.
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 con_type                      con_geoms[0]
---------------------------------------------------------------------------
 UF_SKET_fixed               Vertex_Geometry or a Line/Circle/Ellipse_Geometry
 UF_SKET_horizontal          Line_Geometry
 UF_SKET_vertical            Line_Geometry
 UF_SKET_constant_length     Line_Geometry
 UF_SKET_constant_angle      Line_Geometry
 UF_SKET_uniform_scaled      Spline_Geometry
 UF_SKET_non_uniform_scaled  Spline_Geometry


       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       Following constraint types require exactly two constraint geometries
       and at least one of them must be an internal geometry to the sketch
       specified. The order of input constraint geometries can be exchanged.
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 con_type                     con_geoms[0]  |  con_geoms[1]
---------------------------------------------------------------------------
 UF_SKET_parallel            Line_Geometry    | Line_Geometry
                             Line_Geometry    | Ellipse_Geometry
                             Ellipse_Geometry | Ellipse_Geometry
                             Line_Geometry    | DatumAxis_Geometry
                             Line_Geometry    | DatumPlane_Geometry

 UF_SKET_perpendicular       Line_Geometry    | Line_Geometry
                             Line_Geometry    | Ellipse_Geometry
                             Ellipse_Geometry | Ellipse_Geometry
                             Line_Geometry    | DatumAxis_Geometry
                             Line_Geometry    | DatumPlane_Geometry

 UF_SKET_collinear           Line_Geometry    | Line_Geometry
                             Line_Geometry    | DatumAxis_Geometry
                             Line_Geometry    | DatumPlane_Geometry

 UF_SKET_equal_length        Line_Geometry    | Line_Geometry

 UF_SKET_equal_radius        Circle_Geometry  | Circle_Geometry

 UF_SKET_concentric          Circle_Geometry  | Circle_Geometry
                             Circle_Geometry  | Ellipse_Geometry
                             Ellipse_Geometry | Ellipse_Geometry

 UF_SKET_coincident          Vertex_Geometry  | Vertex_Geometry

 UF_SKET_midpoint            Vertex_Geometry  | Line_Geometry
                             Vertex_Geometry  | Circle_Geometry

 UF_SKET_slope               Vertex_Geometry  | Line_Geometry
                             Vertex_Geometry  | Circle_Geometry
                             Vertex_Geometry  | Ellipse_Geometry
                             Vertex_Geometry  | Spline_Geometry
                             Vertex_Geometry  | DatumAxis_Geometry
                             Vertex_Geometry  | DatumPlane_Geometry
                            ( The Vertex Geometry must represent a spline's
                              defining point)

 UF_SKET_point_on_curve      Vertex_Geometry  | Line_Geometry
                             Vertex_Geometry  | Circle_Geometry
                             Vertex_Geometry  | Ellipse_Geometry
                             Vertex_Geometry  | Spline_Geometry
                             Vertex_Geometry  | DatumAxis_Geometry
                             Vertex_Geometry  | DatumPlane_Geometry

 UF_SKET_tangent            Only the following combinations are invalid:
                             Line_Geometry    | Line_Geometry
                             Line_Geometry    | DatumAxis_Geometry
                             Line_Geometry    | DatumPlane_Geometry
                             Spline_Geometry  | DatumAxis_Geometry
                             Spline_Geometry  | DatumPlane_Geometry

       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       This constraint type requires at least two constraint geometries.
       The first one must be a Vertex Geometry.
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 con_type                      con_geoms[0]     con_geoms[1,...]
---------------------------------------------------------------------------

 UF_SKET_point_on_string    Vertex_Geometry    extracted curves

    *The geometries specified in con_geoms[1] to con_geoms[num_con_geoms-1]
    must be extracted curves (see UF_SKET_add_extracted_objects) and one of
    them must have help data specified. If there are multiple help data
    specified, the first one will be used.


*****************************************************************************/


/******************************************************************************
This routine creates sketch dimensions of the specified type.
Not all parameters are required based on the type of dimension
being created.  Refer to the descriptions below to determine
which parameters are used for each type of sketch dimension.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_update_sketch
          UF_SKET_read_dimension

For new sketches, use <ja_method>NXOpen.SketchCollection.CreateAngularDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateLinearDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateRapidDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateRadialDimensionBuilder</ja_method>

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_create_dimension
(
tag_t sketch_tag,                       /* <I>
                                           Sketch tag
                                        */
UF_SKET_con_type_t dim_type,            /* <I>
                                           Type of dimensions:
                                                UF_SKET_horizontal_dim
                                                UF_SKET_vertical_dim
                                                UF_SKET_parallel_dim
                                                UF_SKET_perpendicular_dim
                                                UF_SKET_angular_dim
                                                UF_SKET_radius_dim
                                                UF_SKET_diameter_dim
                                        */
UF_SKET_dim_object_p_t dim_object1,     /* <I>
                                           Data of first object geometry tag.
                                        */
UF_SKET_dim_object_p_t dim_object2,     /* <I>
                                           Data of second object geometry tag.
                                           Not used for UF_SKET_radius_dim or
                                           UF_SKET_diameter_dim.
                                        */
double dim_origin[3],                   /* <I>
                                           Dimension origin (X, Y, Z)
                                           in model space
                                        */
tag_t *dim_tag                          /* <O>
                                           Tag of created dimension
                                        */
);


/******************************************************************************
This routine creates dimension constraint.  This function differs from
that of UF_SKET_create_dimension for it will output the constraint tag
as opposed to the dimension tag and also the perimeter dimension creation is
supported by this routine.


The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_update_sketch
          UF_SKET_create_dimension
          UF_SKET_create_dimensional_constraint

For new sketches, use <ja_method>NXOpen.SketchCollection.CreateAngularDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateLinearDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateRapidDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateRadialDimensionBuilder</ja_method>

History: This function was originally released in V17.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_create_dimensional_constraint
(
tag_t sketch_tag,                  /* <I>
                                      Sketch tag
                                   */
UF_SKET_con_type_t dim_type,       /* <I>
                                      Type of dimensions:
                                          UF_SKET_horizontal_dim
                                          UF_SKET_vertical_dim
                                          UF_SKET_parallel_dim
                                          UF_SKET_perpendicular_dim
                                          UF_SKET_angular_dim
                                          UF_SKET_radius_dim
                                          UF_SKET_diameter_dim
                                          UF_SKET_perimeter_dim
                                   */
int num_dim_obj,                   /* <I>
                                      Number of geometry tags in the
                                      geoms array
                                   */
UF_SKET_dim_object_p_t dim_objs,   /* <I,len:num_dim_obj>
                                      Array of num_geom geometry tags
                                   */
double dim_origin[3],              /* <I>
                                      Dimension origin (X, Y, Z)
                                      in model space
                                   */
tag_t *con_tag                     /* <O>
                                      Tag of created dimensional constraint
                                   */
);

/******************************************************************************
This routine deletes constaints given their tags. The constraint tags could
belong to different sketches.

Environment: Internal  and  External

See Also: UF_SKET_create_geometric_constraint
          UF_SKET_read_geometric_constraint

For new sketches, use <ja_method>NXOpen.Update.AddObjectsToDeleteList</ja_method>

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_delete_constraints
(
  int   num_cons,     /* <I> number of constraints to be deleted */
  tag_t *con_tags     /* <I,len:num_cons>
                             Array of constraint tag.            */
);

/******************************************************************************
This function mirrors the objects on a center line. New objects and "mirror"
 constraints between the original objects and the new objects will be created.
 Note that points on the center line and lines collinear to the center line
 will not be mirrored. Therefore, the output number of mirrored objects will
 not necessaily be the same as the input number of objects.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch

For new sketches, use <ja_method>NXOpen.SketchCollection.CreateSketchMirrorPatternBuilder</ja_method>

History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_mirror_objects
(
   tag_t sketch_tag,      /* <I>  Sketch tag.                          */
   tag_t center_line_tag, /* <I>  Tag of the center line for mirror    */
   int   num_objs,        /* <I>  Number of objects.                   */
   tag_t *obj_tags,       /* <I,len:num_objs>
                                  Array of objects to be mirrored      */
   int   *num_new_objs,   /* <O>  Number of mirrored objects or
                                  constraints created.
                          */
   tag_t **new_obj_tags,  /* <OF,len:num_new_objs>
                                  Array of mirrored objects.
                                  Use UF_free to deallocate memory when done.
                          */
   tag_t **con_tags       /* <OF,len:num_new_objs>
                                  Array of constraints.
                                  Use UF_free to deallocate memory when done.
                          */
);

/******************************************************************************
This function queries the constraint information

Environment: Internal  and  External

See also : UF_SKET_create_geometric_constraint

For new sketches, use <ja_class>NXOpen.SketchGeometricConstraint</ja_class>

History: V17 change: This function was renamed from UF_SKET_read_constraint,
         which was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_read_geometric_constraint
(
 tag_t sketch_tag,                /* <I>  Sketch tag.              */
 tag_t con_tag,                   /* <I>  Constraint tag.          */
 UF_SKET_con_type_t *con_type,    /* <O>  Constraint type.         */
 int *geom_count,                 /* <O>  Number of geometries.   */
 UF_SKET_con_geom_p_t *con_geoms  /* <OF,len:geom_count>
                                     Array of constraint geometries.
                                     Use UF_free to deallocate memory when done.
                                  */
);

/******************************************************************************
This function queries the dimension information.

Environment: Internal  and  External

See also :  UF_SKET_create_dimension

For new sketches, use <ja_method>NXOpen.SketchCollection.CreateAngularDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateLinearDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateRapidDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateRadialDimensionBuilder</ja_method>

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_read_dimension
(
tag_t sketch_tag,                       /* <I>
                                           Sketch tag
                                        */
tag_t dim_tag,                          /* <I>
                                           Dimension tag
                                        */
UF_SKET_con_type_t *dim_type,           /* <O>
                                           Type of dimensions:
                                               UF_SKET_horizontal_dim
                                               UF_SKET_vertical_dim
                                               UF_SKET_parallel_dim
                                               UF_SKET_perpendicular_dim
                                               UF_SKET_angular_dim
                                               UF_SKET_radius_dim
                                               UF_SKET_diameter_dim
                                        */
UF_SKET_dim_object_p_t dim_object1,     /* <O>
                                           Data of first object geometry tag
                                        */
UF_SKET_dim_object_p_t dim_object2,     /* <O>
                                           Data of second object geometry tag.
                                           Not used for UF_SKET_radius_dim or
                                           UF_SKET_diameter_dim
                                        */
double dim_origin[3],                   /* <O>
                                           Dimension origin in model space
                                        */
tag_t *dim_exp                          /* <O>
                                           Dimension expression tag
                                           (NULL_TAG for Reference dimensions)
                                        */
);

/******************************************************************************
This routine reads dimension constraint given a constraint tag.  This routine
differs from that of UF_SKET_read_dimension as it takes in the constraint tag
as opposed to the dimension tag.


The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_update_sketch
          UF_SKET_read_dimension
          UF_SKET_read_dimensional_constraint

For new sketches, use <ja_method>NXOpen.SketchCollection.CreateAngularDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateLinearDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateRapidDimensionBuilder</ja_method>,
                      <ja_method>NXOpen.SketchCollection.CreateRadialDimensionBuilder</ja_method>

History: This function was originally released in V17.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_read_dimensional_constraint
(
tag_t sketch_tag,                       /* <I>
                                           Sketch tag
                                        */
tag_t con_tag,                          /* <I>
                                           Tag of dimensional constraint to read.
                                        */
UF_SKET_con_type_t *dim_type,           /* <O>
                                           Dimension type
                                        */
int *num_dim_obj,                       /* <O>
                                           Number of geometry tags in the
                                           geoms array
                                        */
UF_SKET_dim_object_p_t *dim_objs,       /* <OF,len:num_dim_obj>
                                           Array of num_geom geometry tags
                                           Use UF_free to deallocate memory when done.
                                        */
double dim_origin[3],                   /* <O>
                                           Dimension origin (X, Y, Z)
                                           in model space
                                        */
tag_t *dim_tag,                         /* <O>
                                           Tag of associated dimension object.
                                           Could be a NULL_TAG for cases such as
                                           perimeter dimensions.
                                        */
tag_t *exp_tag                          /* <O>
                                           Tag of associated expression object
                                        */
);

/******************************************************************************
Sets the sketch preferences for legacy sketches created in V13 and beyond.
To determine if this function should be used instead of
UF_SKET_set_legacy_preferences, use UF_OBJ_ask_type_and_subtype
and check for subtype UF_v13_sketch_subtype.

Environment: Internal and External.

See Also:  UF_SKET_ask_preferences
to set preferences for sketches created in V13.0 and beyond.
          UF_SKET_ask_legacy_preferences
          UF_SKET_set_legacy_preferences

For new sketches, use <ja_class>NXOpen.Preferences.PartSketch</ja_class> or <ja_class>NXOpen.Preferences.SessionSketch</ja_class>

History: This function is new for V15.0. Although the function
         name is not new, the parameter list has changed.

         NX6   change: Sketches no longer have a  'character size' and 'decimal places'
         preference. Each individual dimension will have these preferences.
         The parameter list for this function has not changed. Calling this function
         will result in the 'character size' and 'decimal places' being set on each
         individual dimension in the sketch. 
         
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_set_preferences
(
 tag_t     sketch_tag,       /* <I> Sketch tag.
                                May be NULL_TAG if there is no existing
                                sketch to which the preferences are to be
                                associated. The preferences will then
                                be applied to the sketches created
                                thereafter, with the exception of character size
                                and decimal places. These two will always come from
                                annotation preferences.
                             */

 int       values[10],          /* <I>
                                Array flag to indicate what action to
                                perform for which sketch preference
                                variable.
                                0: Do nothing
                                1: Action

                                [0]: Snap angle
                                [1]: Sketch name prefix
                                [2]: Vertex name prefix
                                [3]: Line name prefix
                                [4]: Arc name prefix
                                [5]: Conic name prefix
                                [6]: Spline name prefix
                                [7]: Character size
                                [8]: Decimal places
                                [9]: Dimension label
                             */

 double     snap_angle,                       /* <I> Snap angle            */
 char       name_prefix[ UF_OBJ_NAME_BUFSIZE ],     /* <I,len:UF_OBJ_NAME_LEN>
                                                  Sketch name prefix   */

 char       vertex_prefix[ UF_OBJ_NAME_BUFSIZE ],   /* <I,len:UF_OBJ_NAME_LEN>
                                                  Vertex name prefix   */

 char       line_prefix[ UF_OBJ_NAME_BUFSIZE ],     /* <I,len:UF_OBJ_NAME_LEN>
                                                  Line Iname prefix    */

 char       arc_prefix[ UF_OBJ_NAME_BUFSIZE ],      /* <I,len:UF_OBJ_NAME_LEN>
                                                  Arc name prefix      */

 char       conic_prefix[ UF_OBJ_NAME_BUFSIZE ],    /* <I,len:UF_OBJ_NAME_LEN>
                                                  Conic name prefix    */

 char       spline_prefix[ UF_OBJ_NAME_BUFSIZE ],   /* <I,len:UF_OBJ_NAME_LEN>
                                                  Spline name prefix   */

 double     char_size,                        /* <I>  Character size is no longer a sketch preference. The 
                                                 character size will be set for each individual dimension in 
                                                 the sketch. If sketch_tag==NULL_TAG nothing will be done. */

 int        dec_places,                       /* <I>   Decimal places are no longer a sketch preference. The 
                                                 decimal places will be set for each individual dimension in 
                                                 the sketch. If sketch_tag==NULL_TAG nothing will be done. */

 int        dim_label                         /* <I>  Dimension label
                                                 1 : Value
                                                 2 : Expression
                                                 3 : Name
                                              */
);

/******************************************************************************
This function updates the current legacy sketch. If you had call to
UF_SKET_create_geometric_constraint, UF_SKET_create_dimension or
UF_SKET_mirror_objects to create constraints or dimensions in a sketch,
it is highly recommended that this routine should be called before calling
UF_SKET_terminate_sketch.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_create_dimension
          UF_SKET_create_geometric_constraint
          UF_SKET_mirror_objects
          UF_SKET_terminate_sketch

For new sketches, use <ja_method>NXOpen.Sketch.Update</ja_method>

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_update_sketch
(
    tag_t sketch_tag       /* <I>    Sketch object tag.    */
);

/******************************************************************************
This function determines whether a given constraint is inferred or not.
This function is valid only for modeling sketches created in V13.0 and later
versions of NX.  The concept of inferred constraint is not strongly supported
and this function should no longer be used.

Environment: Internal  and  External

See Also:

For new sketches, use <ja_method>NXOpen.SketchDimensionalConstraint.DimensionState</ja_method>

History: This function was originally released in V18.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_con_is_inferred
(
 tag_t    con_tag,          /* <I>  Constraint object tag. */
 logical *inferred_con_fl   /* <O>  A flag that determines
                                    whether a given con is
                                    inferred or not.       */
);

/******************************************************************************
This function returns all inferred constraints of the given sketch.
This function is valid only for modeling sketches created in V13.0 and later
versions of NX.  The concept of inferred constraint is not strongly supported
and this function should no longer be used.

Environment: Internal  and  External

See Also:

History: This function was originally released in V18.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_inferred_cons_of_sketch
(
 tag_t sketch_tag,       /* <I>  Sketch object tag.      */
 int   *num_cons,        /* <O>  Number of inferred cons.*/
 tag_t **con_tags        /* <OF,len:num_cons>
                                 Array of inferred cons.
                                 Use UF_free to deallocate
                                 the memory when done.   */
);

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


struct UF_ROUTE_retrieve_eplib_data_s
{
    UF_EPLIB_part_lib_p_t   library;
    int                     error_code;
};

typedef struct UF_ROUTE_retrieve_eplib_data_s
UF_ROUTE_retrieve_eplib_data_t, * UF_ROUTE_retrieve_eplib_data_p_t;

/* uf4401 opens the listing device set by uc4400 for output
   if you only need to open the listing window for output
   (and not a particular listing device set by uc4400)
   this function may be replaced with NXOpen.ListingWindow.Open()

   Comments refered to this being obsoleted, but was not moved to uf_retiring.h until
   NX 2406.

   Original comment refers to using UF_UI_open_listing_window which is also deprecated in NX2312.
   Instead use NXOpen.ListingWindow.Open()

   */
extern UFUNEXPORT void uf4401(int* ir1);

/* uf4402 closes listing device set by uc4400
   if you only need to close the listing window
   (and not a particular device set by uc4400)
   this function may be replaced by NXOpen.ListingWindow.Close()

   Comments refered to this being obsoleted, but was not moved to uf_retiring.h until
   NX 2406.

   Original comment refers to using UF_UI_close_listing_window which is also deprecated in NX2312.
   Instead use NXOpen.ListingWindow.Close()
   */
extern UFUNEXPORT void uf4402(void);

/* uc4403 write character string to listing device set by call to uc4400
   if you only need to write to the listing window
   (as opposed to a listing device set by uc4400)
   this function may be replaced with NXOpen.ListingWindow.WriteFullline()

   Comments refered to this being obsoleted, but was not moved to uf_retiring.h until
   NX 2406.

   Original comment refers to using UF_UI_write_listing_window which is also deprecated in NX2312.
   Instead use NXOpen.ListingWindow.WriteFullline()*/
extern UFUNEXPORT int uc4403(const char* cp1/* <I> */);

/* uc4404 write character string and integer to listing device set by uc4400
   if you only need to write the data to the listing window
   (and not a particular device set by uc4400)
   this function may be replaced by NXOpen.ListingWindow.WriteFullline()

   Comments refered to this being obsoleted, but was not moved to uf_retiring.h until
   NX 2406.

   Original comment refers to using UF_UI_write_listing_window which is also deprecated in NX2312.
   Instead use NXOpen.ListingWindow.WriteFullline()*/
extern UFUNEXPORT int uc4404(const char* cp1/* <I> */, int ip2);

/* uc4406 write character string and real to listing device set by uc4400
   if you only need to write the data to the listing window
   (and not a particular listing device set by uc4400)
   this function may be replaced by NXOpen.ListingWindow.WriteFullline()

   Comments refered to this being obsoleted, but was not moved to uf_retiring.h until
   NX 2406.

   Original comment refers to using UF_UI_write_listing_window which is also deprecated in NX2312.
   Instead use NXOpen.ListingWindow.WriteFullline()*/
extern UFUNEXPORT int uc4406(const char* cp1/* <I> */, double rp2);

/****************************************************************************
Opens and manages (displays) a motif style Information
window if in internal Open API mode.  The first time
this window is opened it will be empty.  Further calls will
display the information previously displayed in the window.
If in external Open API mode, sets the listing window
flag to open.

Equivalent Functionality: NXOpen.ListingWindow.Open() should be used

Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406.

 ****************************************************************************/
extern UFUNEXPORT int UF_UI_open_listing_window(void); 

/****************************************************************************
Closes the listing window. If in internal Open API, the window is
closed. If in external Open API, then the device is set to closed.

Equivalent Functionality: NXOpen.ListingWindow.Close() should be used

Environment: Internal  and  External

See Also:  UF_UI_exit_listing_window

History: For V15.0, this function was modified so that it closes the window but
         does not clear the windows contents. Prior to V15.0, this function
         closed and cleared the window in Internal Open API.
History:
Deprecated in NX2306.

 ****************************************************************************/
extern UFUNEXPORT int UF_UI_close_listing_window(void); 

/****************************************************************************
Closes and clears the listing window. If in internal Open API,
the window is closed and cleared. If in external Open API, the
device is set to closed.

Equivalent Functionality: NXOpen.ListingWindow.CloseWindow() should be used

Environment: Internal and External

See Also : UF_UI_close_listing_window

History: This function was originally released in V15.0.
Deprecated in NX2306.
****************************************************************************/
extern UFUNEXPORT int UF_UI_exit_listing_window(void); 

/****************************************************************************
Writes a character string to the Information window. You should add
your own new line after the string is placed. If in internal Open
API, text is displayed in the Information window. If in external
Open API, text is printed to standard out. The Information
window must be opened before you can write to it.

Once UF_terminate has completed in an external program, you can no
longer write to the console window.  It must be reinitialized with system
calls.

Note: When running an internal Open API program (such as a dll with
predefined entry point, not a main executable), the code has no
knowledge of the application or process that launched the user
function program.  Therefore all internal API's are treated as an
internal NX program and set the standard output to the listing window.
Any call to UF_UI_write_listing_window will attempt to write to the
listing window.

Consequently, if a GRIP batch program calls an internal Open application
that uses UF_UI_write_listing_window, it will not be able to find the
listing window and will raise an error.  In cases where GRIP batch will
be calling an internal program, please use UF_print_syslog to write the
output to the syslog.

Equivalent Functionality: NXOpen.ListingWindow.WriteFullline() should be used

Environment: Internal  and  External

See Also:

History:
Deprecated in NX2306.
 ****************************************************************************/
extern UFUNEXPORT int UF_UI_write_listing_window(
    const char* string  /* <I>
                         pointer to character string
                         */
); 

/****************************************************************************
Queries whether the Information window is open or closed. This
function returns a value of FALSE if the Information window:
has never been opened, has been closed with File-->Exit, File-->Close,
has been closed by a call to UF_UI_close_listing_window or by selecting
the Information button.

Equivalent Functionality: NXOpen.ListingWindow.IsOpen() should be used

Environment: Internal  and  External

See Also:

History:
Deprecated in NX2306.
 ****************************************************************************/
extern UFUNEXPORT int UF_UI_is_listing_window_open(
    logical* response  /* <O>
                        Response flag:
                        TRUE = Window is open
                        FALSE = Window is closed
                        */
); 

/****************************************************************************
Saves the contents of the Information window to the file specified by
the argument.

Note: The saved listing window information is limited to 256 characters
per line.  If a line is longer than 256 characters, it will be wrapped to
multiple lines in the saved file.

Equivalent Functionality: NXOpen.ListingWindow.SelectDevice() should be used

Environment: Internal and External

See Also:

History:
Deprecated in NX2306.
 ****************************************************************************/
extern UFUNEXPORT int UF_UI_save_listing_window(
    char* filename  /* <I>
                     filename to which Information  Window contents is
                     written.
                     */
); 

/****************************************************************************
*   Get name of the current syslog
*
*   Environment: Internal and External
*
*   Equivalent Functionality: NXOpen.LogFile.FileName() should be used
*   See Also:
*
*   History: Released in NX2.0.5
*   Deprecated in NX 2406
****************************************************************************/

extern UFUNEXPORT int UF_ask_syslog_filename(
    char** filename /* <OF>
                      pointer to dynamically allocated path
                      filename must be freed with UF_free()
                   */
);

/****************************************************************************
*   Output a message to the syslog.
*
*   This message can be used to print run time information about the NX Open
*   program to the syslog and is useful for state checking, validation and
*   debugging.
*
*   Printing the trace is especially useful while debugging and reporting a
*   problem.
*
*   Equivalent Functionality: NXOpen.LogFile should be used
*   Environment: Internal and External
*
*   See Also:
*
*   History: Released in V18.0
*   Deprecated in NX 2406
****************************************************************************/
extern UFUNEXPORT int UF_print_syslog(
    char* message, /* <I>
                      Message to be output to the syslog
                   */
    logical trace  /* <I>
                      TRUE = Print the stack trace along with the message
                      FALSE = Print only the message
                   */
);


/****************************************************************************
*   Query the current NX Open program environment for the current image.
*
*   Note: This value is updated during initialization so it is set for
*   each image and won't remember the information from previous images.
*
*   Equivalent Functionality: NXOpen.Session.IsBatch should be used
*   Environment: Internal and External
*
*   Returns:
*     Void
*
*   History:
*  Deprecated in NX 2406
****************************************************************************/
extern UFUNEXPORT void uf3192(
    int* ir1 /* <O>
                The environment that the NX Open program is running in.
                0 is External Open, 1 is Internal Open.
             */
);

/**************************************************************************
 * Returns the compatible base release version number. For example, if
 * you call this function from 1847, it returns NX V1847.
 * For monthly release this function returns its compatible base release version. For example,
 * if you call this function from 1851, it returns NX V1847
 * You must use UF_free to deallocate space used by release.
 *  Equivalent Functionality: See 
 *                               -NXOpen.Session.ReleaseNumber 
 *                               -NXOpen.Session.IsFunctionalRelease 
 *                               -NXOpen.Session.CompatibleBaseRelease 
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 * Deprecated in NX 2406
****************************************************************************/
extern UFUNEXPORT int   UF_get_release(
    char** release  /* <OF>
                     Major release version number
                     */
);


/*****************************************************************************
 * Calls and executes a GRIP program. Your GRIP program must be written,
 * compiled, linked, and ready to run.
 *
 * While a GRIP program executes, it can have access to an Open C API function
 * arguments and their contents. Argument passing to the GRIP program occurs
 * through UFARGS. After GRIP program termination, the Open C API program has
 * access to any assignments made by the GRIP program. The GRIP program
 * completes its execution and then UF_call_grip outputs a return value.
 *
 * Note:  If the path is omitted in the grip_executable string passed to
 * UF_call_grip, NX will look in the current directory for the grip program.
 * It will not look in the directory of the ufunc program or use any
 * environment variables, including UGII_INITIAL_GRIP_DIR, to search for the
 * GRIP program.
 *
 * UF_translate_variable can be used to extract an environment variable and
 * concatenate it with the program name.
 *
 * The following GRIP commands are not
 * supported in External mode when calling GRIP:
 *         ALL OF GRIP NC
 *         PLNOTE  EDTXHT  CHAIN
 *         BLANK   UNBLNK  RVBLNK
 * If any of these commands are encountered, an error is written to the
 * batch log file.
 *
 * Equivalent Functionality: See NXOpen.Session.ExecuteGrip
 * Environment: Internal  and  External
 *
 * See Also: 
 *
 * History:
 * Deprecated in NX 2406
 ****************************************************************************/
extern UFUNEXPORT int UF_call_grip(
    char* grip_executable,  /* <I>
                                Name of GRIP program to execute (file name
                                or full path name).
                                */
    int count,          /* <I>
                                Count of arguments to pass to GRIP executable
                                */
    UF_args_p_t UFARGS      /* <I,len:count>
                                An array of structures where each element in
                                 the array is a structure that contains an
                                arguments type, size, and address.  Note that
                                if an argument is type UF_TYPE_CHAR, the array
                                must be initialized prior to the UF_call_grip
                                call.
                                */
);


/*****************************************************************************
    Unique identifiers for standard NX applications
*****************************************************************************/

#define UF_APP_NONE          (0)      /* No App Module (may be in External UF)*/
#define UF_APP_DRAFTING      (1)      /* Drafting */
#define UF_APP_MECHANISMS    (14)     /* CAE - Mechanisms */
#define UF_APP_CAM           (16)     /* Manufacturing */
/* obsoleted in NX 3         (38)        ICAD - Generative Modeling */
#define UF_APP_MODELING      (40)     /* Modeling */
#define UF_APP_VALISYS       (47)     /* Valisys - Quality Control */
#define UF_APP_GATEWAY       (48)     /* Gateway */

/* UGMX retired in V18.0.0.12 */
#define UF_APP_UGMX          (50)     /* UGMX Interface */

#define UF_APP_HARNESS       (51)
#define UF_APP_FLAT          (60)     /* Sheet Metal Design - Flat Patterns */
#define UF_APP_SHTNEST       (61)     /* Sheet Metal Design - Nesting */
#define UF_APP_PUNCH         (62)     /* Sheet Metal Design - Punch Press */
#define UF_APP_MPG           (63)  /* Sheet Metal Design - Multipart Gridding */
#define UF_APP_SSL           (64)     /* Sheet Metal Design - Surface Layout */
#define UF_APP_SHTFAB        (65)     /* Sheet Metal Design - Fabrication */
#define UF_APP_SMD           (66)     /* Sheet Metal Design Application */
#define UF_APP_BUILDER       (67)     /* UI Builder */
#define UF_APP_SFEM          (68)     /* CAE Advanced Simulation */
#define UF_APP_ROUTE         (69)     /* PSA - Routing Applications */
               /* obsoleted  (70)        PSA - Virtual Mockup (Division) */
#define UF_APP_PIPE          (71)     /* PSA - Routing - Piping */
#define UF_APP_TUBE          (72)     /* PSA - Routing - Tubing */
#define UF_APP_STEEL         (73)     /* PSA - Routing - Steel */
#define UF_APP_CONDUIT       (74)     /* PSA - Routing - Conduit */
#define UF_APP_RACEWAY       (75)     /* PSA - Routing - Raceway */
#define UF_APP_SHOPS         (76)     /* Manufacturing - Shop floor app */
#define UF_APP_WIRE          (77)     /* PSA - Routing - Wiring */
#define UF_APP_MTB           (78)     /* Manufacturing - Machine Tool Builder */
#define UF_APP_SKETCHER      (79)     /* Legacy Sketcher Task Environment */
#define UF_APP_NOPART        (80)     /* No Part loaded menubar */
               /* obsoleted  (81)        CAE - Advanced FEM */
#define UF_APP_ROUTE_MECH    (82)     /* PSA - Routing - Mechanical */
#define UF_APP_ROUTE_ELEC    (83)     /* PSA - Routing - Electrical */
#define UF_APP_ROUTE_LGCL    (84)     /* PSA - Routing - Logical */
#define UF_APP_SBSM          (85)     /* SBSM - Straight Break Sheet Metal */
#define UF_APP_SEQUENCING    (86)     /* Sequencing Task Environment */
#define UF_APP_UFUN          (87)     /* UFUN app */
#define UF_APP_STUDIO        (88)     /* Shape Studio */
#define UF_APP_DESFEM        (89)     /* CAE - Design Simulation */
#define UF_APP_SHIP          (90)     /* PSA - Ship Building */
#define UF_APP_AEROSM        (91)     /* PSA - Aerospace Sheet Metal Application */
#define UF_APP_FLEX_PCB      (92)     /* Flexible Printed Circuit Design */
#define UF_APP_INSPECTION    (93)     /* CMM Inspection Programming */
#define UF_APP_MECHATRONICS  (94)     /* Mechatronics Designer */
#define UF_APP_STYLER        (95)     /* Block Styler */
#define UF_APP_SUBSET_DEFINITION (96) /* Subset Definition task environment */
#define UF_APP_TRUE_STUDIO   (97)     /* True Studio Task Environment */
#define UF_APP_SHIP_BASICDESIGN (98)  /* Ship Building */
#define UF_APP_SHIP_DETAILSDESIGN (99)/* Ship Building */
#define UF_APP_SHIP_MANUFACTURE (100) /* Ship Building */
#define UF_APP_SINUCAST      (101)    /* SinuCAST */
#define UF_APP_SUBDIVISION_MODELING   (102)  /* Subdivision Modeling Task Environment */

/*****************************************************************************
 * Returns the current application module. The value that is returned
 * maps to a string defined constant. You can find the string in the
 * header file uf.h. The strings are of the form UF_APP_<module>.
 * For example, UF_APP_DRAFTING represents the drafting module.
 *
 * Note - if this function is called from an external program it will
 *        always return a FALSE and an app id of APP_NONE.
 * 
 * Equivalent Functionality: See NXOpen.Session.ApplicationName
 * Environment: Internal
 * See Also:
 * History:
 * Deprecated in NX 2406
 *****************************************************************************/
extern UFUNEXPORT int UF_ask_application_module(
    int* module_id  /* <O>
                    The module identification value of the
                    current application.
                    */
);


/****************************************************************************
 * Reserve a license against the specified license context.
 * If the specified user-defined context does not already exist it will be created.
 * Equivalent Functionality: See NXOpen.LicenseManager
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 * Deprecated in NX 2406
 ****************************************************************************/
extern UFUNEXPORT int UF_reserve
(
    const char* license, /* <I>
                              License feature name to be reserved
                              */
    const char* context_name  /* <I>
                              Name of context to reserve license against.  Will use the default context if NULL is specified.
                              */
);

/****************************************************************************
 * Release a license against the specified license context.
 * Equivalent Functionality: See NXOpen.LicenseManager
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 * Deprecated in NX 2406
 ****************************************************************************/
extern UFUNEXPORT int UF_release
(
    const char* license, /* <I>
                              License feature name to be released
                              */
    const char* context_name /* <I>
                              Name of context to release license against.  Will use the default context if NULL is specified.
                              */
);

/****************************************************************************
 * Release all licenses against the specified license context.  If
 * the context specified is a user-defined context it will be deleted.
 * Equivalent Functionality: See NXOpen.LicenseManager
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 * Deprecated in NX 2406
 ****************************************************************************/
extern UFUNEXPORT int UF_release_all
(
    const char* context_name /* <I>
                              Name of context release to release.  Will use the default context if NULL is specified.
                              */
);

/****************************************************************************
 * Returns the licenses that are currently reserved against a context.
 * This method will also output the licenses reserved against the default context in the syslog.
 * Equivalent Functionality: See NXOpen.LicenseManager
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 * Deprecated in NX 2406
 ****************************************************************************/
extern UFUNEXPORT int UF_get_reserved_licenses
(
    const char* context_name, /* <I>
                              Name of context to release against.  Will use the default context if NULL is specified.
                              */
    int* n_licenses,             /* <O>
                               The number of licenses.
                        */
    char*** licenses       /* <OF,len:n_licenses>
                        The list of license reserved against the specified context.  This must be
                        freed by calling UF_free_string_array.
                        */
);

/****************************************************************************
 * Translates environment variables to their equivalence strings. You
 * must supply the complete name of the variable argument.  The pointer passed
 * back points to an operating system string.  This string must not be changed.
 * Equivalent Functionality: See NXOpen.Session.GetEnvironmentVariableValue
 * Environment: Internal  and  External
 *
 * See Also: 
 *
 * History:
 * Deprecated in NX 2406
 ****************************************************************************/
extern UFUNEXPORT int UF_translate_variable(
    const char* variable, /* <I>
                     Environment Variable to Translate
                 */
    char** translation     /* <O>
                 Translated variable name or NULL if nonexistent.
                 */
);

/****************************************************************************
 * Sets an environment variable to the string specified in value. You must
 * supply the complete name of variable.
 * Equivalent Functionality: No NXOpen method is provided
 * Environment: Internal  and  External
 *
 * See Also: 
 *
 * History:
 * Deprecated in NX 2406
 ****************************************************************************/
extern UFUNEXPORT int UF_set_variable(
    const char* variable, /* <I>
                             Environment Variable to set in Operating System
                             */
    const char* value      /* <I>
                             Value or equivalence string for the variable.
                             */
);


/*******************************************************************************
Open a file for binary buffered I/O.  The open mode
is used to indicate how the file is to be accessed.
The file format is used both to specify a default extension to use and
for the write modes, the type to be stored in the file's header.  For the
read mode, a format of zero may be specified indicating no default
extension.

A native operating system file may be opened by using the
appropriate file type. For example, a format of 4 opens a text file in
the native file system.

A successful open returns a simple integer channel number.  This
channel number is to be passed to the routines for reading, writing,
skipping, and closing the file.

uc4510 (read characters), uc4511 (read integers), uc4512 (read reals),
and uc4513 (read bytes) are used to read primitive data types from a
file open with uc4500. Combinations of these types may be used to
create more complex data types. The I/O channel number returned by uc4500
is passed to these other routines.

uc4520 (write characters), uc4521 (write integers), uc4522 (write
reals), and uc4523 (write bytes) are used to write primitive data types
to a file opened with uc4500. Combinations of these calls are used to
create more complex types. The I/O channel number returned by uc4500
is passed to these other routines.

uc4530 (skip characters), uc4531 (skip integers), uc4532 (skip reals),
and uc4533 (skip bytes) are used to bypass primitive data types in a
file opened with uc4500. A combination of these may be used to skip
over more complex types. Skips may be backward by using negative
skip counts.

For characters, the count will be rounded up to the next integer
boundary (e.g. a write/read/skip of 5 will actually write/read/skip 8
characters).

Return:
         Return code:
         <0 = error
         >= 0 = i/o channel number

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4510
 uc4511
 uc4512
 uc4513
 uc4520
 uc4521
 uc4522
 uc4523


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4500(
    const char* fspec,/* <I>
                        File To Open
                        */
    int omode,/* <I>
               Open Mode
               1 = Read
               2 = Write
               3 = Write, Replace
               5 = Update
               7 = Scratch
               */
    int ftype  /* <I>
               File Format
               */
);

/*******************************************************************************
Read characters from a file opened with uc4500.

For characters, the count will be rounded up to the next integer
boundary (e.g. a read of 5 will actually read 8 characters).
Integer variables are used for storing the characters in byte format.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4510(
    int chan,/* <I>
              I/O Channel Number returned from uc4500.
              */
    int len,/* <I>
             Number Of Characters To Read
             */
    char cbuf[UF_MAXWORD] /* <O>
                 Array To Read Characters Into
                 */
);
/*******************************************************************************
Read integers from a file opened with uc4500.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4511(
    int chan,/* <I>
              I/O Channel Number returned from uc4500.
              */
    int len,/* <I>
             Number Of Integers To Read
             */
    int* sibuff  /* <O>
                  Array To Read Integers Into
                  */
);

/*******************************************************************************
Read reals from a file opened with uc4500.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4512(
    int chan,/* <I>
              I/O Channel Number returned from uc4500
              */
    int len,/* <I>
             Number Of Reals To Read
             */
    double rbuff[]  /* <O>
                    Array To Read Reals Into
                    */
);

/*******************************************************************************
Read bytes from a file opened with uc4500.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4513(
    int chan,/* <I>
              I/O Channel Number returned by uc4500
              */
    int len,/* <I>
             Number Of Bytes To Read
             */
    char bbuf[UF_MAXWORD] /* <O>
                 Array To Read Bytes Into
                 */
);

/*******************************************************************************
Write characters to a file opened with uc4500.
The count will be rounded up to the next integer
boundary (e.g. a write of 5 will actually write 8 characters).

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int  uc4520(
    int chan,/* <I>
              I/O channel number returned by uc4500.
              */
    long len,/* <I>
              Number of characters to write
              */
    const char* cbuff  /* <I>
                        Character data to write
                        */
);

/*******************************************************************************
Write integers to a file opened with uc4500.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4521(
    int chan,/* <I>
              I/O channel number returned by uc4500
              */
    long len,/* <I>
              Number of integers to write
              */
    int* sibuff  /* <I>
                  Integer data to write
                  */
);
/*******************************************************************************
Write reals to a file opened with uc4500.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4522(
    int chan,/* <I>
              I/O channel number returned by uc4500
              */
    long len,/* <I>
              Number of reals to write
              */
    double rbuff[]  /* <I>
                    Real data to write
                    */
);
/*******************************************************************************
Write bytes to a file opened with uc4500.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4523(
    int chan,/* <I>
              I/O channel number returned by uc4500
              */
    long len,/* <I>
              Number of bytes to write
              */
    const void* bbuff  /* <I>
                        Byte data to write
                        */
);


/*******************************************************************************
Open a text file for I/O.  Only the routines uc4514,
uc4524, and uc4525 for reading and writing lines may be used on text
file. See the description of uc4500 for a description of the parameters.
For omode = 4, the file must exist and will be opened for write. The
file pointer will be initially positioned at the end of file.
For omode = 6, a printer is opened. If the filespec is blank, the
default printer will be opened.

Return:
         Return code:
        < 0 = error
        >= 0 = I/O Channel Number

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4514a
 uc4524
 uc4525


History:
Deprecated in NX 2406
******************************************************************************/
extern UFUNEXPORT int uc4504(
    const char* fspec,/* <I>
                        File To Open
                        */
    int omode,/* <I>
               Open Mode
               1 = Read
               2 = Write
               3 = Write, Replace
               4 = Append
               6 = Printer
               */
    int ftype  /* <I>
               File Type
               */
);

/*******************************************************************************
Read a line of text from a file opened with uc4504.

Return:
         Return code
        <  0 = Error
        >= 0 = Length Of Line Read

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4504

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4514a(
    int chan,/* <I>
              I/O channel number returned by uc4504
              */
    char** cbuf /* <OF>
                Line read. The buffer must be freed with UF_free()
                */
);

/*******************************************************************************
Write a line to a text file.  Only complete lines may
be written to a text file. The addition of any delimiters (e.g. newline)
is done automatically.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4504

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4524(
    int chan,/* <I>
              I/O channel number returned by uc4504
              */
    const char* cbuf  /* <I>
                       Line to write
                       */
);
/*******************************************************************************
uc4525 is used to write a page break to a text file.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4504

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4525(
    int chan  /* <I>
              I/O channel number returned by uc4504
              */
);

/*******************************************************************************
Open a binary file for block I/O.  Only the routines
uc4516 and uc4526 for reading and writing blocks may be used on a
file opened with uc4506. See the description of uc4500 for a
description of the parameters.

Return:
         Return code:
        > 0 = error
        <= 0 = I/O Channel Number

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External
See Also:
 uc4516
 uc4526

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4506(
    const char* fspec,/* <I>
                        File To Open
                        */
    int omode,/* <I>
               Open Mode
               1 = Read
               2 = Write
               3 = Write, Replace
               5 = Update
               7 = Scratch
               */
    int ftype  /* <I>
               File Type
               */
);

/*******************************************************************************
Randomly read blocks from a file opened with
uc4506. Data is always read on a block boundary.

Return:
         Return code
        < 0 = Error
        > 0 = Number of bytes actually read

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4506

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4516(
    int chan,/* <I>
              I/O channel number returned by uc4506
              */
    int block,/* <I>
               Starting block number to read (from 0)
               */
    int bytes,/* <I>
               Number of bytes to read
               */
    char* cbuf  /* <O>
                 Data read
                 */
);

/*******************************************************************************
Randomly write to a file opened with uc4506. The
data is always written on a block boundary.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4506

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4526(
    int chan,/* <I>
              I/O channel number returned by uc4506
              */
    int block,/* <I>
               Starting block number to write (from 0)
               */
    int bytes,/* <I>
               Number of bytes to write
               */
    const char* buf  /* <I>
                      Data to write
                      */
);

/*******************************************************************************
Open a file for record oriented I/O. Only the
routines uc4517 and uc4527 may be used to read and write records.
Record I/O is generally only supported for native files.

Return:
         Return code:
        < 0 = error
        >= 0 = I/O Channel Number

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External
See Also:
 uc4517
 uc4527

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4507(
    const char* fspec,/* <I>
                        File Specification
                        */
    int omode,/* <I>
               Open Mode
               1 = Read
               2 = Write
               3 = Replace
               5 = Update
               7 = Scratch
               */
    int ftype,/* <I>
               File Type
               */
    int rectype  /* <I>
                 Record Format
                 = 0 = Variable Length Records
                 > 0 = Fixed Record Length
                 */
);

/*******************************************************************************
Read the next record from a file opened using uc4507.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4507

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4517(
    int chan,/* <I>
              I/O channel number returned by uc4507
              */
    int* bytes,/* <O>
                 Length of record read in bytes
                 */
    char* cbuf /* <O>
                 Array to read record into
                 */
);

/*******************************************************************************
Write a record to a file opened with uc4507.  For fixed
length record files, the parameter bytes is ignored.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4507

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4527(
    int chan,/* <I>
              I/O channel number returned by uc4507
              */
    int bytes,/* <I>
               Length of record to write in bytes
               */
    const char* cbuf  /* <I>
                       Buffer containing data to write
                       */
);


/*******************************************************************************
Open a directory for reading.  Directory entries are read
using uc4518 with the fields picked out using uc4600 to uc4609.
Sub-directories may be opened using uc4509.

The dmode bit-mask is used to indicate the intention of the
application in using the directory.  Bits zero through seven indicate
which fields from the file header to read and bits ten through thirteen
specify special directory options.

You can specify which bits to set by using the left shift operator in
conjuction with the bit wise or. For example, to set bits 11 and 13, you
would use the following declaration:
int dmode = (1 << 11) | (1 << 13);

A wildcard template may be used and is specified when the directory
is opened.  It may be passed separate from the directory filespec or as
part of the directory filespec.  For example:

dmode(bit 11) = 1, fspec = "disk/manager", wcard = "*.prt" will
return out all parts in the manager's directory.

If neither dmode(bit 11) or dmode(bit 12) is set then all files will be
returned.   dmode(bit 11) and dmode(bit 12) should not be
set at the same time.

If dmode(bit 13) is set then the caller is only interested in the names
of the files and none of the header attributes.  If this is set then none
of the parameter dmode(bit 0) through dmode(bit 7) should be set.

If dmode(bit 10) is set then the caller is intending to open
sub-directories.  If it is not set then uc4509 should not be called.

Return:
         Return code:
        < 0 = error
        >= 0 = I/O Channel Number

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External
See Also:
 uc4518
 uc4600
 uc4609
 uc4509


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4508(
    const char* fspec,/* <I>
                        Directory Specification
                        */
    int dmode,/* <I>
               Bit-mask Of Open Options
               bit 0 =   Read Owner Field
                       0 = No
                       1 = Yes
               bit 1 = Read Protection Classfield
                       0 = No
                       1 = Yes
               bit 2 = Read Status Field
                       0 = No
                       1 = Yes
               bit 3 = Read Length Field
                       0 = No
                       1 = Yes
               bit 4 = Read Dates
                       0 = No
                       1 = Yes
               bit 5 = Read Description Field
                       0 = No
                       1 = Yes
               bit 6 = Read Customer Area Field
                       0 = No
                       1 = Yes
               bit 7 = Read Machine Field
                       0 = No
                       1 = Yes
               bit 8-9 = *Reserved*
               bit 10 = Enable Sub-trees
                       0 = No
                       1 = Yes
               bit 11 = Template Given
                       0 = No
                       1 = Yes, Template In wcard
               bit 12 = Directory Contains Wildcards
                       0 = No
                       1 = Yes
               bit 13 =  Read Filenames Only
                       0 = No
                       1 = Yes
               bit 14-15 = *Reserved*
               */
    int ftype,/* <I>
               This argument is no longer used.
               */
    const char* wcard  /* <I>
                        Wildcard Template
                        */
);

/*******************************************************************************
Open a subdirectory of the currently open directory.
The previous directory entry read by uc4518 must have been of type
directory (format 100-112) otherwise the error 'not a directory'
is returned. Subdirectories are closed using uc4549.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External
See Also:
 uc4518
 uc4549
History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4509(void);


/*******************************************************************************
Read the next directory entry and save the entry's
information in memory. This information may then be accessed by the
routines uc4600 through uc4609.

Return:
         Return code
        < 0 = Error
          0 = Entry Read
          1 = End Of Subdirectory
          2 = End Of Directory

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External
See Also:
 uc4508
History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4518(void);

/*******************************************************************************
Returns the full filespec of the last directory entry
read. This is provided so the Open C API program need not be
concerned with the syntax of filespecs in forming them.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4508

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4519(
    char fspec[MAX_FSPEC_BUFSIZE]  /* <O>
                  Full file specification of the last directory
                  entry read.
                  */
);

/*******************************************************************************
Skip characters in a file opened with uc4500.
Skips may be backward by using negative skip counts.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4530(
    int chan,/* <I>
              I/O channel number returned by uc4500
              */
    long len  /* <I>
              Number of characters to skip over
              */
);
/*******************************************************************************
Skip integers in a file opened with uc4500.
Skips may be backward by using negative skip counts.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4531(
    int chan,/* <I>
              I/O channel number returned by uc4500
              */
    long len  /* <I>
              Number of integers to skip over
              */
);
/******************************************************************************
Skip reals in a file opened with uc4500.
Skips may be backward by using negative skip counts.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4532(
    int chan,/* <I>
              I/O channel number returned by uc4500
              */
    long len  /* <I>
             Number of reals to skip over
             */
);
/*******************************************************************************
Skip bytes in a file opened with uc4500.
Skips may be backward by using negative skip counts.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4533(
    int chan,/* <I>
              I/O channel number returned by uc4500
              */
    long len  /* <I>
              Number of bytes to skip over
              */
);
/******************************************************************************
Find the current position within a file opened with
uc4500. That position may then be restored using uc4535.

Return:
         Return code:
        < 0 = Error
        >= 0 = File position

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500
 uc4535
History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT long uc4534(
    int chan  /* <I>
              I/O channel number returned by uc4500
              */
);
/*******************************************************************************
Restore the read/write position within a file
previously saved using uc4534. The file must have been opened with
uc4500.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4500
 uc4534

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4535(
    int chan,/* <I>
              I/O channel number returned by uc4500
              */
    long pos  /* <I>
              File position returned by uc4534
              */
);
/*******************************************************************************
Reposition a file back to the beginning. This may be
used for binary, text, and record I/O files.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4536(
    int chan  /* <I>
              I/O channel number
              */
);
/******************************************************************************
Close a file opened with either uc4500, uc4504,
uc4506, or uc4507. The close disposition is used to indicate whether a
file opened for write is to be saved or not. A normal close will make
the file permanent and delete any previous file with the same name.
An abort close will delete the file and retain any previous file with the
same name.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4540(
    int chan,/* <I>
              I/O channel number
              */
    int disp  /* <I>
              Disposition
              0 = Normal close
              1 = Abort close
              */
);
/*******************************************************************************
Determine characteristics of an open file given its I/O channel number.
The integer date/times in qreslt (if qreslt = 6) can be converted to
character strings using uc4582.

Starting in NX 11 a query type of 5 is no longer supported.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4544(
    int chan,/* <I>
              I/O channel number
              */
    int qitem,/* <I>
               Item to inquire:
               1 = File System
               2 = File Type
               3 = Last Error
               4 = Record Format
               6 = Creation, Modify, Access
                    Dates
               */
    int* qreslt  /* <O>
                  Query result:
                  For qreslt = 1,
                          2 = NATIVE
                  For qreslt = 2,
                  See File Types
                  For qreslt = 3, Last read or write error
                  For qreslt = 4,
                          = 0 = Variable length records
                          > 0 = Fixed record length
                  For qreslt = 6, qreslt is an array of 6  integers
                          (0)-(1) = Creation Date,Time
                          (2)-(3) = Modification Date,Time
                          (4)-(5) = Last Access Date,Time
                  */
);

/*******************************************************************************
Determines the file length (in bytes) of
an open file given its I/O channel number.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4547(
    int chan,/* <I>
              I/O channel number
              */
    int qitem,/* <I>
               Item to query
               1 = File length in bytes
               */
    int* qreslt  /* <O>
                  Query result
                  */
);

/*******************************************************************************
Close any directories opened with uc4508. If any
subdirectories are open, they will be closed as well.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4508

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4548(void);

/*******************************************************************************
Close a subdirectory opened with uc4509.  Directory
reads will then continue with the previous directory.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:
 uc4509

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4549(void);
/*******************************************************************************
Checks whether the specified file of the given type exists.

NOTE: Mixed or upper case file names may not be found if the
environment variable UGII_OPTION = LOWER is set.

Passing an ftype of 0 will look for a file but does not work for a directory.
To check for a directory the ftype must be set to 100.

Return:
         Return code:
        < 0 = Error
        = 0 = File Exists
        = 1 = File Does Not Exist

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4560(
    const char* fspec,/* <I>
                        File to check
                        */
    int ftype  /* <I>
               File type
               0 will check for files
               100 will check for directories
               */
);
/*******************************************************************************
Remove a given file from the file system.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4561(
    const char* fspec,/* <I>
                        File to delete
                        */
    int ftype  /* <I>
               File type
               */
);
/*******************************************************************************
Change the name of a given file.  The new file name
should be a simple name (e.g. no directory specification).

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4562(
    const char* fspec,/* <I>
                        Old file name
                        */
    int ftype,/* <I>
               File type
               */
    const char* fspec2  /* <I>
                         New file name
                         */
);
/*******************************************************************************
Create an empty directory.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4563(
    const char* fspec,/* <I>
                        Directory to create
                        */
    int ftype  /* <I>
               File type
               */
);

/******************************************************************************
Retrieve the header information of a single file and
store it in memory. The information may then be retrieved using
uc4600 through uc4609.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External
See Also:
 uc4600
 uc4601
 uc4602
 uc4603
 uc4605
 uc4606
 uc4607
 uc4608
 uc4609


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4564(
    const char* fspec,/* <I>
                        File specification from which to read header
                        */
    int ftype,/* <I>
               File type
               */
    int fmode  /* <I>
               Bit-mask Specifying Header Fileds Desired
               bit     0 = Read Owner Field
                       0 = No
                       1 = Yes
               bit 1 = Read Protection Class Field
                       0 = No
                       1 = Yes
               bit 2 = Read Status Field
                       0 = No
                       1 = Yes
               bit 3 = Read Length Field
                       0 = No
                       1 = Yes
               bit 4 = Read Dates
                       0 = No
                       1 = Yes
               bit 5 = Read Description Field
                       0 = No
                       1 = Yes
               bit 6 = Read Customer Area Field
                       0 = No
                       1 = Yes
               bit 7 = Read Machine Field
                       0 = No
                       1 =yes
               bit 8-15 = *Reserved*
               */
);


/*******************************************************************************
Read the current default value for a directory.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4565(
    int def,/* <I>
             Default to read:
             1 = Current directory
             2 = '$' directory
             3 = '!' directory
             */
    char fspec[MAX_FSPEC_BUFSIZE] /* <O>
                  Current Setting
                  */
);
/******************************************************************************
Change the current user's directory.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:

History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int  uc4566(
    int def,/* <I>
             Default to change:
             1 = Current directory
             2 = '$' directory
             3 = '!' directory
             */
    const char* fspec  /* <I>
                        New default value
                        */
);

/*******************************************************************************
Copies or moves a file from a source file specification to a destination file
specification.  When any move option is used, the source file will only be
deleted after it has been successfully copied to the destination file.

Using a file type of -1 indicates "any file type" so changing extensions
during the copy or move operation will work correctly.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int  uc4567(
    const char* srcspc,/* <I>
                         Source file specification
                         */
    const char* dstspc,/* <I>
                         Destination file specification
                         */
    int cmode,/* <I>
               Specifies Copy/Move Options:
                    = UF_CFI_COPY_NEVER_REPLACE
                    = UF_CFI_COPY_ALWAYS_REPLACE
                    = UF_CFI_COPY_REPLACE_IF_NEWER
                    = UF_CFI_COPY_LEGACY  (same as UF_CFI_COPY_NEVER_REPLACE)
                    = UF_CFI_MOVE_NEVER_REPLACE
                    = UF_CFI_MOVE_ALWAYS_REPLACE
                    = UF_CFI_MOVE_REPLACE_IF_NEWER
                    = UF_CFI_MOVE_LEGACY  (same as UF_CFI_MOVE_NEVER_REPLACE)
               */
    int stype,/* <I>
               Source file type
               */
    int dtype  /* <I>
               Destination file type
               */
);



/*******************************************************************************
Examine a filespec and make sure it conforms to the syntax of the file
system.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4570(
    const char* fspec,/* <I>
                        File specification to validate
                        */
    int ftype  /* <I>
               File type
               */
);
/*******************************************************************************
Examine a filespec and make sure it is a valid directory specification for
the file system.  A "directory file spec" is a path to a file which is a
directory.

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4571(
    const char* fspec,/* <I>
                        Directory File Specification To Validate
                        */
    int ftype  /* <I>
               File Type
               */
);
/*******************************************************************************
Examine a filespec and make sure it is a valid wildcard directory specification
for the file system.   This will also indicate whether there were any
wildcard characters in the filespec.  To find all files that match the wildcard
filespec, open the directory with uc4508 and supply the wildcard filespec,
then read (uc4518) each matching entry and the corresponding filespec (uc4519).

Return:
         Return code:
        = 0 = Valid file specification
        = 1 = Valid with wildcards
        Anything else is an error

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4572(
    const char* fspec,/* <I>
                        File specification to validate
                        */
    int ftype  /* <I>
               File type
               */
);

/*******************************************************************************
Given a filespec return its fully qualified equivalent.  If
a non-zero file type is given, the extension will also be set. For
example, the native system with a default directory DISK2/JOE
fspec = "foo", type = 2 will produce expfspec = "DISK2/JOE/FOO.PRT"

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4573(
    const char* fspec,/* <I>
                        File specification to expand
                        */
    int ftype,/* <I>
               File type
               */
    char expfspec[MAX_FSPEC_BUFSIZE]  /* <O>
                     Expanded file specification
                     */
);

/*******************************************************************************
Accept a filespec and removes any directory path, extension,
and any system specific information and returns the resultant simple
filename. For example:
fspec = "/DISK1/JOE/FOO.PRT", ftype = 2 will produce fname = "FOO".

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4574(
    const char* fspec,/* <I>
                        File specification from which to extract name
                        */
    int ftype,/* <I>
               File type
               */
    char fname[UF_CFI_MAX_FILE_NAME_BUFSIZE]  /* <O>
                  Simple file name
                  */
);
/*******************************************************************************
Combine a directory with a filename producing a file specification (filespec).
For example:

dspec = "/manager", ftype = 2, fname = "bar"

will produce fspec = "/MANAGER/BAR.PRT".

If the file name is a directory, using a filetype of 100 will merge the
directories. For example:

dspec = "/manager", ftype = 100, fname = "bar"

will produce fspec = "/MANAGER/BAR".

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4575(
    const char* dspec,/* <I>
                        Directory
                        */
    int ftype,/* <I>
               File type
               */
    const char* fname,/* <I>
                        File name
                        */
    char fspec[MAX_FSPEC_BUFSIZE]  /* <O>
                  Resultant file specification
                  */
);
/*******************************************************************************
Take a filespec and returns its directory and filename components. For example:

fspec = "/Manager/Work/BENCH", ftype = 2


Note that this routine is impacted by the UGII_OPTION environment variable,
so if UGII_OPTION=lower is set, then the above example will produce:
dspec = "/manager/work" and fname = "bench.prt".

Equivalent Functionality: See language specification for alternatives.  For example
C++ could use std::filesystem, std::ifstream, and\or std::ofstream which are all available in C++ 17.
Environment: Internal  and  External

See Also:


History:
Deprecated in NX 2406
*******************************************************************************/
extern UFUNEXPORT int uc4576(
    const char* fspec,/* <I>
                        File specification to split up
                        */
    int ftype,/* <I>
               File type
               */
    char dspec[MAX_FSPEC_BUFSIZE],/* <O>
                  Directory component
                  */
    char fname[UF_CFI_MAX_FILE_NAME_BUFSIZE] /* <O>
                  File name component
                  */
);

/*****************************************************************
 * Creates a shaded image using the capabilities of NX Photo and saves
 * that image as a TIFF, GIF, or JPEG file. You specify the image type
 * by including the appropriate file extension in the save_filename
 * parameter. Use any one of the following file extensions:
 * .tif - TIFF
 * .gif - GIF
 * .jpg - JPEG
 * For example, specifying "test.jpg" for the filename parameter
 * creates a JPEG file.
 * The batch shade function shades the active view using the light
 * sources, backgrounds, foregrounds, materials and textures that were
 * setup using interactive NX. If the current layout is a drawing then
 * this function will return without creating an output file.
 *
 * If using a shade method of UF_DISP_high_quality, UF_DISP_preview,
 * UF_DISP_photo_real or UF_DISP_raytrace then a Studio Render license
 * is required.  If this license is not available then the method will
 * default back to UF_DISP_phong.
 *
 * Please note this API generates output shaded image file using Lightworks Author renderer and
 * supports Lightworks Author materials and textures.  IrayPlus materials won't be processed.
 * Please set IRAY+ environment variable to 0 before executing NX Open utilities using this API.
 * Environment: Internal  and  External
 * See Also: 
 * History: Deprecated in NX2406
 * Equivalent Functionality: <ja_class>NXOpen.Gateway.ImageCaptureBuilder</ja_class> Class should be used
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_batch_shade(
    char* filename,            /* <I>
                                Name of output TIFF, GIF, or JPEG file
                                */
    int x_size,                /* <I>
                                X size of output in pixels
                                */
    int y_size,                /* <I>
                                Y size of output in pixels
                                */
    UF_DISP_shade_method_t method  /* <I>
                                   Type of shade to produce.  Either:
                                    UF_DISP_flat, UF_DISP_gouraud,
                                    UF_DISP_phong, UF_DISP_high_quality,
                                    UF_DISP_preview,
                                    UF_DISP_photo_real, or
                                    UF_DISP_raytrace
                                    */
);

/*****************************************************************
 * Creates a shaded image using the capabilities of NX Photo and saves
 * that image as a TIFF, GIF, or JPEG file. You specify the image type
 * by including the appropriate file extension in the save_filename
 * parameter. Use any one of the following file extensions:
 * .tif - TIFF
 * .gif - GIF
 * .jpg - JPEG
 * For example, specifying "test.jpg" for the filename parameter
 * creates a JPEG file.
 * The batch shade function shades the active view using the light
 * sources, backgrounds, foregrounds, materials and textures that were
 * setup using interactive NX. If the current layout is a drawing then
 * this function will return without creating an output file.
 * This function allows setting of some options for the shading process.
 *
 * If using a shade method of UF_DISP_high_quality, UF_DISP_preview,
 * UF_DISP_photo_real or UF_DISP_raytrace then a Studio Render license
 * is required.  If this license is not available then the method will
 * default back to UF_DISP_phong.
 *
 * Please note this API generates output shaded image file using Lightworks Author renderer and
 * supports Lightworks Author materials and textures.  IrayPlus materials won't be processed.
 * Please set IRAY+ environment variable to 0 before executing NX Open utilities using this API.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Deprecated in NX2406
 * Equivalent Functionality: <ja_class>NXOpen.Gateway.ImageCaptureBuilder</ja_class> Class should be used
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_batch_shade_options(
    char* filename,            /* <I>
                                Name of output TIFF, GIF, or JPEG file
                                */
    int x_size,                /* <I>
                                X size of output in pixels
                                */
    int y_size,                /* <I>
                                Y size of output in pixels
                                */
    UF_DISP_shade_method_t method, /* <I>
                                   Type of shade to produce.  Either:
                                    UF_DISP_flat, UF_DISP_gouraud,
                                    UF_DISP_phong, UF_DISP_high_quality,
                                    UF_DISP_preview,
                                    UF_DISP_photo_real, or
                                    UF_DISP_raytrace
                                    */
    UF_DISP_shade_options_p_t options /* <I>
                                      Options to control the shading
                                      process.
                                      */
);

#ifdef __cplusplus
}
#endif
#undef EXPORTLIBRARY

#endif /* UF_RETIRING */
