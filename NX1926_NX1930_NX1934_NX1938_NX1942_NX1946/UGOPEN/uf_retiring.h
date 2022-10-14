/****************************************************************************

           Copyright (c) 1999-2006,2008 UGS Corp.
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
#include <uf_defs.h>
#include <uf_cfi_types.h>
#include <uf_drf_types.h>
#include <uf_draw_types.h>
#include <uf_eplib_types.h>
#include <uf_modl_types.h>
#include <uf_plist_types.h>
#include <uf_obj_types.h>
#include <uf_retiring_ugopenint.h>
#include <setjmp.h>
#include <uf_eplib_types.h>
#include <uf_weld_types.h>
#include <uf_sf_post_datatypes.h>
#include <uf_sf_types.h>
#include <uf_sf_legend.h>
#include <uf_sf_disp_mesh.h>
#include <uf_ugmgr_types.h>
#include <uf_pd_types.h>
#include <uf_sf_model_checker.h>
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

#define UF_RLIST_err_ports_not_found           (1945047)
#define UF_RLIST_err_comps_not_found           (1945054)

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

typedef struct UF_EPLIB_charx_s  UF_ROUTE_charx_t, *UF_ROUTE_charx_p_t;

/**/
#ifndef UF_EPLIB_part_lib_part_t_defined
#define UF_EPLIB_part_lib_part_t_defined
typedef struct UF_EPLIB_part_lib_part_s UF_ROUTE_part_lib_part_t,
    *UF_ROUTE_part_lib_part_p_t;
#endif

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
    const char*                     node_id;
    /*  Input:  Specifies the name/ID of the node in the
     *          Product Library View under which to look
     *          for matching characteristics.
     */

    int                             num_criteria;
    UF_ROUTE_charx_p_t              criteria;
    /*  Input:  Characteristics structure used to for item selection.
     */

    int                             num_matches;
    UF_ROUTE_part_lib_part_p_t      matches;
    /*  Output: Characteristics of the parts that match the criteria.
     */

    int                             error;
    /*  Output:  Zero indicates success
     */
};
/* Structure passed to the SPLIT_DESCRIPTORS plugin.
 *
 * The SPLIT_DESCRIPTORS plugin splits the given characteristics into
 * descriptor characteristics, hidden characteristics, and applied
 * characteristics.
 */
struct UF_ROUTE_split_descriptors_plugin_s
{
    int                             num_charx;
    UF_ROUTE_charx_p_t              charx;
    /*  Input:  Characteristics to split up.
     */

    int                             num_descriptor_charx;
    UF_ROUTE_charx_p_t              descriptor_charx;
    /*  Output: Non-hidden descriptor characteristics.
     */

    int                             num_hidden_charx;
    UF_ROUTE_charx_p_t              hidden_charx;
    /*  Output: Hidden descriptor characteristics.
     */

    int                             num_applied_charx;
    UF_ROUTE_charx_p_t              applied_charx;
    /*  Output: Applied descriptor characteristics.
     */

    int                             error;
    /*  Output: Zero indicates success
     */
};

struct UF_ROUTE_cb_fab_data_s
{
    char   file_name[ UF_ATTR_MAX_STRING_BUFSIZE ];       /* file name, eg "C:\Temp\my_new_fab.prt"  */
    int    num_charx;                               /* number of charx */
    UF_ROUTE_charx_p_t   charx;                     /* charx list  */
};
typedef struct UF_ROUTE_cb_fab_data_s UF_ROUTE_cb_fab_data_t, *UF_ROUTE_cb_fab_data_p_t;

typedef struct UF_ROUTE_split_descriptors_plugin_s
    UF_ROUTE_split_descriptors_plugin_t, *UF_ROUTE_split_descriptors_plugin_p_t;


/**********************************************************************
Sets the characteristics to the given routing object.

Environment: Internal  and  External

See Also:


History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_characteristics
(
tag_t obj_id ,/* <I>
              Object identifier of the routing object.
              */
int  charx_count ,/* <I>
                  Count of the characteristics.
                  */
UF_ROUTE_charx_p_t list  /* <I,len:charx_count>
                         List of all characteristics.
                         */
);

#define UF_ROUTE_CHARX_TYPE_UNKNOWN     UF_EPLIB_CHARX_TYPE_UNKNOWN
#define UF_ROUTE_CHARX_TYPE_INT         UF_EPLIB_CHARX_TYPE_INT
#define UF_ROUTE_CHARX_TYPE_REAL        UF_EPLIB_CHARX_TYPE_REAL
#define UF_ROUTE_CHARX_TYPE_STR         UF_EPLIB_CHARX_TYPE_STR
#define UF_ROUTE_CHARX_TYPE_ANY         UF_EPLIB_CHARX_TYPE_ANY
#define UF_ROUTE_CHARX_TYPE_REF         UF_EPLIB_CHARX_TYPE_REF
#define UF_ROUTE_CHARX_TYPE_ANY_REF     UF_EPLIB_CHARX_TYPE_ANY_REF
#define UF_ROUTE_CHARX_TYPE_INT_EXPR    UF_EPLIB_CHARX_TYPE_INT_EXPR
#define UF_ROUTE_CHARX_TYPE_REAL_EXPR   UF_EPLIB_CHARX_TYPE_REAL_EXPR
#define UF_ROUTE_CHARX_TYPE_STR_EXPR    UF_EPLIB_CHARX_TYPE_STR_EXPR

/*
 * - the charx expression parser error messages
 */
#define UF_ROUTE_CHARX_EXPR_unknown             ERROR_ROUTE_base + 165
#define UF_ROUTE_CHARX_EXPR_err_num_eq_eq       ERROR_ROUTE_base + 166
#define UF_ROUTE_CHARX_EXPR_err_num_eq_rel      ERROR_ROUTE_base + 167
#define UF_ROUTE_CHARX_EXPR_err_num_eq_none     ERROR_ROUTE_base + 168
#define UF_ROUTE_CHARX_EXPR_err_num_eq_str      ERROR_ROUTE_base + 169
#define UF_ROUTE_CHARX_EXPR_err_num_num_eq      ERROR_ROUTE_base + 170
#define UF_ROUTE_CHARX_EXPR_err_num_num_rel     ERROR_ROUTE_base + 171
#define UF_ROUTE_CHARX_EXPR_err_num_num_num     ERROR_ROUTE_base + 172
#define UF_ROUTE_CHARX_EXPR_err_num_num_str     ERROR_ROUTE_base + 173
#define UF_ROUTE_CHARX_EXPR_err_num_range_eq    ERROR_ROUTE_base + 174
#define UF_ROUTE_CHARX_EXPR_err_num_range_rel   ERROR_ROUTE_base + 175
#define UF_ROUTE_CHARX_EXPR_err_num_range_range ERROR_ROUTE_base + 176
#define UF_ROUTE_CHARX_EXPR_err_num_range_str   ERROR_ROUTE_base + 177
#define UF_ROUTE_CHARX_EXPR_err_num_rel_eq      ERROR_ROUTE_base + 178
#define UF_ROUTE_CHARX_EXPR_err_num_rel_rel     ERROR_ROUTE_base + 179
#define UF_ROUTE_CHARX_EXPR_err_num_rel_none    ERROR_ROUTE_base + 180
#define UF_ROUTE_CHARX_EXPR_err_num_rel_range   ERROR_ROUTE_base + 181
#define UF_ROUTE_CHARX_EXPR_err_num_rel_str     ERROR_ROUTE_base + 182
#define UF_ROUTE_CHARX_EXPR_err_num_none        ERROR_ROUTE_base + 183
#define UF_ROUTE_CHARX_EXPR_err_num_str         ERROR_ROUTE_base + 184
#define UF_ROUTE_CHARX_EXPR_err_str_eq_eq       ERROR_ROUTE_base + 185
#define UF_ROUTE_CHARX_EXPR_err_str_eq_rel      ERROR_ROUTE_base + 186
#define UF_ROUTE_CHARX_EXPR_err_str_eq_none     ERROR_ROUTE_base + 187
#define UF_ROUTE_CHARX_EXPR_err_str_quote_eq    ERROR_ROUTE_base + 188
#define UF_ROUTE_CHARX_EXPR_err_str_quote_rel   ERROR_ROUTE_base + 189
#define UF_ROUTE_CHARX_EXPR_err_str_quote_quote ERROR_ROUTE_base + 190
#define UF_ROUTE_CHARX_EXPR_err_str_quote_str   ERROR_ROUTE_base + 191
#define UF_ROUTE_CHARX_EXPR_err_str_str_eq      ERROR_ROUTE_base + 192
#define UF_ROUTE_CHARX_EXPR_err_str_str_rel     ERROR_ROUTE_base + 193
#define UF_ROUTE_CHARX_EXPR_err_str_str_quote   ERROR_ROUTE_base + 194
#define UF_ROUTE_CHARX_EXPR_err_str_str_str     ERROR_ROUTE_base + 195
#define UF_ROUTE_CHARX_EXPR_err_str_none        ERROR_ROUTE_base + 196
#define UF_ROUTE_CHARX_EXPR_err_str_rel_rel     ERROR_ROUTE_base + 197

/**********************************************************************
Returns the characteristics data of a routing object.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_characteristics
(
tag_t obj_id ,/* <I>
              Object identifier of the routing object.
              */
int c_type ,/* <I>
            Type of characteristic desired. Valid values
            are:
            UF_ROUTE_CHARX_TYPE_INT
            UF_ROUTE_CHARX_TYPE_REAL
            UF_ROUTE_CHARX_TYPE_STR
            UF_ROUTE_CHARX_TYPE_ANY
            */
int * charx_count ,/* <O>
                   Count of the characteristics.
                   */
UF_ROUTE_charx_p_t * list  /* <OF,len:charx_count,free:UF_ROUTE_free_charx_array>
                           List of all characteristics. The allocated list
                           must be freed by calling UF_ROUTE_free_charx_array.
                           */
);/*<NON_NXOPEN>*/

/**********************************************************************
Deletes a list of  characteristics from a given routing object.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_delete_characteristics
(
tag_t  obj_id ,/* <I>
               Object identifier of the routing object whose
               characteristics needs to be deleted.
               */
int charx_count ,/* <I>
                 Number of characteristics to be deleted.
                 */
UF_ROUTE_charx_p_t list  /* <I,len:charx_count>
                         List of  characteristics to be deleted.
                         */
);

/**********************************************************************
Loads the given part, or part family member if member name is
among the list of characteristics, into the current session. The part is
loaded but NOT made the current work part. The returned part tag
may subsequently be used by the Assembly functions to add this part
as a component to the assembly for later "placement" within the
routing.

If the part is already loaded the routine finds the part. If member
name is among the list of characteristics, the routine will establish it if
it is an instance of the part.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_load_part_by_charx
(
int  num_charx ,/* <I>
                Number of characteristics.
                */
UF_ROUTE_charx_t  charx[] ,/* <I,len:num_charx>
                           Array of characteristics associated with a part
                           */
tag_t *  part  /* <O>
               Part tag of the loaded part or NULL_TAG if it
               was not loaded.
               */
);
/* Characteristics Environment */

/**********************************************************************
Replaces the current characteristic environment with the supplied set
of characteristics.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_charx_env
(
int  num_charx ,/* <I>
                Number of characteristics supplied
                */
UF_ROUTE_charx_t charx[]  /* <I,len:num_charx>
                          Array of characteristics supplied.
                          */
);

/**********************************************************************
Updates the current characteristic environment with the given
characteristics by updating existing values in the environment and
adding new values.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_update_charx_env
(
int num_charx ,/* <I>
               Number of characteristics
               supplied.
               */
UF_ROUTE_charx_t  charx[]  /* <I,len:num_charx>
                           Array of characteristics
                           */
);

/**********************************************************************
Returns the number of characteristics and the array containing
characteristic titles, values and types.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_charx_env
(
int * num_charx ,/* <O>
                 Number of the characteristics.
                 */
UF_ROUTE_charx_p_t * charx  /* <OF,len:num_charx>
                            List of all characteristics.
                            */
);

/**********************************************************************
Matches part entries in the part library based on the given set of
characteristics. If start is not NULL, it should be the name of the
node in the part library hierarchy at which to start the search.

Environment: Internal  and  External

See Also:  UF_ROUTE_free_match_results

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_match_charx_in_plib
(
char * start ,/* <I>
              Name of the start node in the part
              library view tree.
              */
int num_criteria ,/* <I>
                  Number of characteristics being
                  matched
                  */
UF_ROUTE_charx_p_t criteria ,/* <I,len:num_criteria>
                             Array of match characteristics.
                             */
int * num_matches ,/* <O>
                   Number of matches found.
                   */
UF_ROUTE_part_lib_part_p_t * matches  /* <OF,len:num_matches,free:UF_ROUTE_free_match_results>
                                      Array of matches. To be freed using
                                      UF_ROUTE_free_match_results.
                                      */
);

/**********************************************************************
Frees the memory associated with the result of a part library match.
These values should not have been changed since being returned from
the match function (UF_ROUTE_match_charx_in_plib).

Environment: Internal  and  External

See Also:  UF_ROUTE_match_charx_in_plib

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_free_match_results
(
int num_matches ,/* <I>
                 Number of matches to be freed
                 */
UF_ROUTE_part_lib_part_p_t matches  /* <I,len:num_matches>
                                    Array of matches to be freed
                                    */
);/* <NON_NXOPEN> */

/**********************************************************************
This function frees the allocated charx array. Must use after every
call to UF_ROUTE_ask_characteristics

Environment: Internal  and  External

See Also:

History:
***********************************************************************/
extern UFUNEXPORT  int UF_ROUTE_free_charx_array
(
int    num_charx,               /* <I>
                                Number of Charx values
                                */
UF_ROUTE_charx_p_t charx_list   /* <I,len:num_charx>
                                Array of the characteristics
                                */
);/* <NON_NXOPEN> */

/*****************************************************************************

  Finds the index of the charx whose title matches the title passed in.  If
  the index is -1 the title was not found in the charx.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_find_title_in_charx
(
    int                 num_charx,  /* <I>    number of charx */
    UF_ROUTE_charx_p_t  charx,      /* <I,len:num_charx>
                                        array of charx to search */
    char*               title,      /* <I>    title to search for */
    int*                index       /* <O>    Index into charx that matches title */
);

/**********************************************************************

Find the characteristic of specified type and name
for the given terminal port.  The characteristic is
looked for in the following order:
1) input terminal tag
2) the terminal's prototype if the input terminal is an occurrence.
3) the terminal's multiport
4) the terminal's part occurrence

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_find_terminal_charx
(
    char  *charx_name,      /* <I> , the name of the charx to search for*/
    int   charx_type,       /* <I> , the type of the charx */
    tag_t terminal,         /* <I> , the tag of the terminal port being asked*/
    UF_ROUTE_charx_p_t charx/* <O> , the desired charx*/);


/*
    Bend corner creation methods.
*/
enum UF_ROUTE_bend_radius_method_e
{
    UF_ROUTE_bend_radius_method_radius,
    UF_ROUTE_bend_radius_method_ratio_to_diameter,
    UF_ROUTE_bend_radius_method_bend_radius_table,
    UF_ROUTE_bend_radius_method_inner_radius
} ;
typedef enum UF_ROUTE_bend_radius_method_e UF_ROUTE_bend_radius_method_t,
             *UF_ROUTE_bend_radius_method_p_t;

/* Corner Preference Structure */
struct UF_ROUTE_corner_pref_s
{
    int                             type;
    UF_ROUTE_bend_radius_method_t   bend_radius_method;
    double                          bend_ratio;
    double                          bend_radius;
    int                             radius_units;
    tag_t                           dir;        /* Only used for miter with one segment */
    char*                           bend_table_entry;
};
typedef struct UF_ROUTE_corner_pref_s UF_ROUTE_corner_pref_t,
               *UF_ROUTE_corner_pref_p_t;

/**********************************************************************
Returns the "corner" information such as type, RCP id and the Corner
object id when supplied with any one of the following:
   The RCP at which the corner was created.
   The Corner object id obtained after calling one of the
      UF_ROUTE_create_bend or UF_ROUTE_create_miter routines.
   The Segment created as a result of the Bend corner. Miter corner
      does not create a segment. The input may be an existing RCP, a
      Bend segment or a Corner object.

Return:
     TRUE object is some kind of corner
     FALSE otherwise.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_ask_obj_corner_info
(
tag_t obj_id ,/* <I>
              Object identifier to interrogate. Can be an RCP,
              a Bend Segment, or a Corner (Bend or Miter)
              object .
              */
int * crn_typ ,/* <O>
               Corner type such as
               UF_ROUTE_CORNER_NONE
               UF_ROUTE_CORNER_BEND
               UF_ROUTE_CORNER_MITER
               */
tag_t * crn_rcp ,/* <O>
                 Object Identifier of the RCP at this Corner
                 only, else NULL_TAG
                 */
tag_t * crn_obj  /* <O>
                 Object Identifier of the Corner object. This is
                 equal to obj_id if the input is a Corner. If the
                 input is an RCP or Bend Segment this is the
                 Corner object to that RCP or segment
                 */
);/* <NEC> */

/**********************************************************************
Returns the "bend corner"  radius when supplied with any one of the
following:
    . The RCP at which the Bend was created.
    . The Bend Corner object id obtained after calling one of the
      UF_ROUTE_create_bend routines.
    . The segment created as a result of the Bend Corner.

Return:
         Returns :
        True = If the obj_id is a valid bend object.
        False = invalid object.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_ask_obj_bend_radius
(
tag_t obj_id ,/* <I>
              Object identifier to interrogate. Can be a RCP,
              a Bend segment, or a Corner (only bend
              corner) object.
              */
double * radius  /* <O>
                 Radius at the Bend Corner.
                 */
);/* <NEC> */

/**********************************************************************
Returns the radius of a bend.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_bend_radius
(
tag_t bend_tag ,/* <I>
                Tag of bend object to query
                */
double * radius  /* <O>
                 Bend radius of bend
                 */
);

/**********************************************************************
Inquire of a bend, which RCP it is associated with.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_bend_rcp
(
tag_t bend_tag ,/* <I>
                Tag of bend
                */
tag_t * rcp  /* <O>
             Tag of rcp which has bend corner assigned
             */
);


/**********************************************************************
Returns the Bend segment object identifier for a given Bend corner.
When a Bend Corner is created at the intersection of two Segments,
via the UF_ROUTE_create_bend_by_radius or
UF_ROUTE_create_bend_by_ratio routine, two new objects are
created. One is the Bend Corner object, which holds the information
about the corner, e.g., the radius, and the other is a Routing Segment
which models the bend or fillet between the two original Segments.
Returns the tag of this bend segment.

Environment: Internal  and  External

See Also:  UF_ROUTE_create_bend_by_radius
           UF_ROUTE_create_bend_by_ratio

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_bend_segment
(
tag_t bend_obj ,/* <I>
                Object identifier of the Bend corner object
                */
tag_t * seg_id  /* <O>
                Object identifier of the segment that corresponds to
                the Bend.
                */
);

/**********************************************************************
Assigns a Bend corner with the given radius to the input object. If the
input object is the RCP, corner, or Segment associated with an existing
bend corner, the corner and associated Segment is updated with the
new radius. If the assignment is to an RCP or Corner of a Miter
corner, the old corner is removed and a new Bend corner is created.

Environment: Internal  and  External

See Also:


History:Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_bend_by_radius
(
tag_t obj_id ,/* <I>
              Object identifier of an existing RCP, or a
              Bend segment or a Corner.
              */
double radius ,/* <I>
               Radius of the Bend Corner.
               */
tag_t *corner ,/* <O>
              Object identifier of the newly created
              Corner.
              */
tag_t * seg  /* <O>
             Object identifier of the Bend corner
             segment.
             */
);

/**********************************************************************
Assigns a Bend corner. The radius for the bend is determined by
multiplying the given ratio times the diameter of the stock. The
stock's diameter is determined from a characteristic assigned to the
Stock Data object associated with the stock. The characteristic title
should be that returned by routine UF_ROUTE_ask_app_view_diameter.

If the input object is the RCP, corner, or Segment associated with an
existing bend corner, the corner and associated Segment is updated
with the new radius. If the assignment is to an RCP or Corner of a
Miter corner, the old corner is removed and a new Bend corner is
created.

Environment: Internal  and  External

See Also:


History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_bend_by_ratio
(
tag_t obj_id ,/* <I>
              Object identifier of an existing RCP, or a
              Bend segment or a Corner.
              */
double ratio ,/* <I>
              Ratio of stock diameter to bend radius
              assigned to the Bend corner.
              */
tag_t * corner ,/* <O>
                Object identifier of the newly created
                Corner.
                */
tag_t * seg  /* <O>
             Object identifier of the Bend corner
             segment.
             */
);

/**********************************************************************
Assigns a Miter corner to the input object. The assignment can
involve the removal of an existing Corner and the creation of a new
Corner.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_miter_corner
(
tag_t obj_id ,/* <I>
              Object identifier of an existing RCP, or Bend
              segment or a Miter Corner.
              */
tag_t * corner  /* <O>
                Object identifier of the newly created Corner.
                */
);

/**********************************************************************
Removes the Corner, be it a Bend or a Miter.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_remove_corner
(
tag_t corner  /* <I>
              Object identifier of the Corner, Bend or
              Miter.
              */
);

/**********************************************************************
Inquires whether the given RCP is an RCP on the end of a bend
segment. This is not the same as the bend RCP.

Return:
         Return code:
        TRUE = RCP is on a bend segment
        FALSE = RCP is not on a bend segment

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_rcp_bend_seg_rcp
(
tag_t candidate ,/* <I>
                 Candidate RCP
                 */
tag_p_t corner  /* <O>
                Corner object or NULL_TAG
                */
);/* <NEC> */

/**********************************************************************
Inquires whether the given RCP has a miter corner assigned to it.

Return:
         Return code:
        TRUE = RCP has miter assigned
        FALSE = RCP has no miter assigned

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_rcp_miter_corner
(
tag_t rcp  /* <I>
           Tag of RCP
           */
);/* <NEC> */

/**********************************************************************
Returns the corner assigned to the RCP.  If no corner is assigned, then
NULL_TAG is returned.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_corner
(
tag_t rcp_tag ,/* <I>
               Tag of Route Control Point.
               */
tag_p_t corner  /* <O>
                Tag of corner assigned to the RCP (or
                NULL_TAG).
               */
);

/* */
#ifndef UF_ROUTE_application_view_t_defined
#define UF_ROUTE_application_view_t_defined
typedef struct ROUTE_application_view_s UF_ROUTE_application_view_t,
* UF_ROUTE_application_view_p_t;
#endif


/**********************************************************************
Returns an integer value which is a bit mask indicating the allowable
corner types for the given Application View. The bits set in this value
can be tested using symbols defined in uf_route.h. These are:
        UF_ROUTE_AV_CORNERS_BEND, UF_ROUTE_AV_CORNERS_COPE,
        UF_ROUTE_AV_CORNERS_MITER and UF_ROUTE_AV_CORNERS_SBEND.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_corners
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of the Application View
                                        structure
                                        */
int  * curves  /* <O>
               Flags indicating allowed corner
               types
               */
);

/**********************************************************************
Returns the bend corner that this segment represents. The corner is
NULL_TAG if segment is not a bend segment.

Environment: Internal  and  External

See Also:

History:Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_bend_crnr
(
tag_t segment ,/* <I>
               Tag of segment to query.
               */
tag_p_t corner  /* <O>
                Tag of bend corner (or NULL_TAG).
                */
);



/******************************************************************************
Creates a thread feature.  Specify the creation parameters in the
thread parameter structure.

For internal thread, argument "internal_thread" should be set as "TRUE" in parameters
which is pointer to thread parameter structure UF_MODL_symb_thread_data_s.

IMPORTANT:
"NXOpen.Features.Thread" classes have been introduced in NX1926 to create, edit and query threads.
Thread feature use thread standard file from environment variable UGII_THREADED_HOLE_STANDARD_DIR for features
created interactively or using thread NXOpen classes in NX1926 and later.
UF_MODL_create_symb_thread() will continue to use thread standards from .dat files to preserve existing
automation programs.

Environment: Internal  and  External
See Also: 
  UF_MODL_symb_thread_data_p_t
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_symb_thread(
    UF_MODL_symb_thread_data_p_t parameters,/* <I>
                                             Pointer to thread parameter structure
                                             UF_MODL_symb_thread_data_s
                                             */
    tag_t* thread_obj_id  /* <O>
                           Thread object id
                           */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING */
