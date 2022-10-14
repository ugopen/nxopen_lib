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

#include <uf_attr.h>
#include <uf_cfi_types.h>
#include <uf_defs.h>
#include <uf_draw_types.h>
#include <uf_plist_types.h>
#include <uf_obj_types.h>
#include <uf_retiring_ugopenint.h>
#include <setjmp.h>
#include <uf_curve.h>
#include <uf_weld_types.h>
#include <uf_sf_post_datatypes.h>
#include <uf_sf_types.h>
#include <uf_ugmgr_types.h>
#include <uf_pd_types.h>
#include <uf_sf_model_checker.h>

#include <libufun_exports.h>

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************
   Old naming convention prototypes - attribute functions
  ***************************************************************************/
/* uc5090, uc5092, uc5093, uc5095 and uc5096 were brought forward
   from V9.x, and do not have one for one replacements from V15 onwards.
*/

/* uc5090 open archive part attribute access */
extern UFUNEXPORT int uc5090(
                  char *cp1 /* <I> Pathname of Part */
);

/* uc5092 read archived part part attribute name */
extern UFUNEXPORT int uc5092(
                  char cr1[ UF_ATTR_MAX_TITLE_BUFSIZE ] /* <O> Part Attribute Name */
);

/* uc5093 cycle attributes of archived part */
extern UFUNEXPORT int uc5093(
                  int *ia1, /* <I/O> Cycle State (current Attribute number)
                                     <I> 0 = Begin Cycling
                                     <O> 1 = Next Attribute returned
                                     <O> 0 = All attributes processed */
                  char cr2[ UF_ATTR_MAX_TITLE_BUFSIZE ], /* <O>  Part attribute title */
                  char cr3[ UF_ATTR_MAX_STRING_BUFSIZE  ]  /* <O>  Part attribute Value */
);

/* uc5095 read name of current object during Cycling*/
extern UFUNEXPORT int uc5095(
                  char cr1[ UF_OBJ_NAME_BUFSIZE ] /* <O> Name of currently cycled entity */
);

/* uc5096 cycle attributes of current archive object */
extern UFUNEXPORT int uc5096(
                  int *ia1, /* <I/O> Cycle State (current attribute number)
                                     <I> 0 = Begin Cycling
                                     <O> 1 = Next Attribute returned
                                     <O> 0 = All attributes processed */
                  char cr2[ UF_ATTR_MAX_TITLE_BUFSIZE ], /* <O> Attribute title */
                  char cr3[ UF_ATTR_MAX_STRING_BUFSIZE  ]  /* <O> Attribute Value */
);

/* uf5091 close archive part after attribute access */
extern UFUNEXPORT void FTN(uf5091)(
                  int *errorcode /* <O> Error code */
);

/* uf5094 cycle archived objects */
extern UFUNEXPORT void FTN(uf5094)(
                  int *indx, /* <I/O> Cycle State
                                      <I> 0 = Begin Cycling
                                      <O> 1 = Next Entity
                                      <O> 0 = All Entities Processed */
                  int *type, /* <I>   Entity type */
                  int *errorcode /* <O> Error Code */
);

/* uc5102 remove attribute
   This function should be replaced with UF_ATTR_delete,
   e.g.
     int uc5102(tag_t np1, char *cp2, int ip3);
     {
        UF_ATTR_delete(np1, UF_ATTR_any, cp2);
     }
*/
extern UFUNEXPORT int uc5102(tag_t np1, const char *cp2/* <I> */, int ip3);

/* uc5104 Read a string attribute title.
   This functions should be replaced with UF_ATTR_cycle
   e.g.
     int uc5104(tag_t np1, int ip2, char *cr3, int *ir4)
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_string;
         UF_ATTR_value_t uf_value;
         char attr_title[ UF_ATTR_MAX_TITLE_BUFSIZE ];
         char attribute[ UF_ATTR_MAX_STRING_BUFSIZE  ];

         uf_value.type = UF_ATTR_string;
         uf_value.value.string = attribute;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_string, attr_title, &uf_value);
         }
         strcpy(cr3, attr_title);
         *ir4 = strlen(attr_title);
     }
*/
extern UFUNEXPORT int uc5104(tag_t np1, int ip2, char cr3[UF_ATTR_MAX_TITLE_BUFSIZE ] /* <O> */, int *ir4);

/* uc5105 Read an attribute value.
   This functions should be replaced with UF_ATTR_cycle
   e.g.
     int uc5105(tag_t np1, int ip2, char *cr3, int *ir4);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_string;
         UF_ATTR_value_t uf_value;
         char attr_title[ UF_ATTR_MAX_TITLE_BUFSIZE ];
         char attribute[ UF_ATTR_MAX_STRING_BUFSIZE  ];

         uf_value.type = UF_ATTR_string;
         uf_value.value.string = attribute;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_string, attr_title, &uf_value);
         }
         strcpy(cr3, attribute);
         *ir4 = strlen(attribute);
     }
*/
extern UFUNEXPORT int uc5105(tag_t np1, int ip2, char cr3[UF_ATTR_MAX_TITLE_BUFSIZE ] /* <O> */, int *ir4);

/* uc5114 read integer attribute title and value
   This functions should be replaced with UF_ATTR_cycle
   e.g.
     int uc5114(tag_t np1, int ip2, char *cr3, int *ir4);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_integer;
         UF_ATTR_value_t uf_value;
         char attr_title[ UF_ATTR_MAX_TITLE_BUFSIZE ];

         uf_value.type = UF_ATTR_integer;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_integer, attr_title, &uf_value);
         }

         strcpy(cr3, attribute);
         *ir4 = uf_value.value.i;
     }
*/
extern UFUNEXPORT int uc5114(tag_t np1, int ip2, char cr3[UF_ATTR_MAX_TITLE_BUFSIZE ] /* <O> */, int *ir4);

/* uc5118 read floating point attribute
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5118(tag_t np1, int ip2, char *cr3, double *rr4);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_real;
         UF_ATTR_value_t uf_value;
         char attr_title[ UF_ATTR_MAX_TITLE_BUFSIZE ];

         uf_value.type = UF_ATTR_real;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_real, attr_title, &uf_value);
         }

         strcpy(cr3, attribute);
         *rr4 = uf_value.value.d;
     }
*/
extern UFUNEXPORT int uc5118(tag_t np1, int ip2, char cr3[UF_ATTR_MAX_TITLE_BUFSIZE ] /* <O> */, double *rr4);

/* uc5122 read null attribute title
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5122(tag_t np1, int ip2, char *cr3);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_null;
         UF_ATTR_value_t uf_value;
         char attr_title[ UF_ATTR_MAX_TITLE_BUFSIZE ];

         uf_value.type = UF_ATTR_null;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_null, attr_title, &uf_value);
         }

         strcpy(cr3, attribute);
     }
*/
extern UFUNEXPORT int uc5122(tag_t np1, int ip2, char cr3[UF_ATTR_MAX_TITLE_BUFSIZE ] /* <O> */);

/* uc5126 read date & time attribute
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5126(tag_t np1, int ip2, char *cr3, int *ir4);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_time;
         UF_ATTR_value_t uf_value;
         char attr_title[ UF_ATTR_MAX_TITLE_BUFSIZE ];

         uf_value.type = UF_ATTR_time;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_time, attr_title, &uf_value);
         }

         strcpy(cr3, attribute);
         ir4[0] = uf_value.value.time[0];
         ir4[1] = uf_value.value.time[1];
     }
*/
extern UFUNEXPORT int uc5126(tag_t np1, int ip2, char cr3[UF_ATTR_MAX_TITLE_BUFSIZE ] /* <O> */, int *ir4);

/* uc2703 regenerate the display of a single view  -- replaced by
   UF_DISP_regenerate_view, e.g.

extern int uc2703( char *cp1 )
   {
        char view_name[31];
        tag_t view_tag;

        if( cp1 == NULL || strlen(cp1) > 30 )
           return UF_err_bad_parameter_number_1;

        if (strcmp(cp1,"") == 0)
        {
             uc6448(view_name);
        }
        else
        {
            strcpy(view_name,cp1);
        }

        error =UF_VIEW_ask_tag_of_view_name(view_name,&view_tag);
        if( error == 0)
        {
             if (view_tag != NULL_TAG)
             {
                 error = UF_DISP_regenerate_view(view_tag);
             }
         }
        return error;
    }
*/
extern UFUNEXPORT int uc2703(const char *cp1 /* <I> */);

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

/* uc2723 display temporary text -- replaced by
   UF_DISP_display_temporary_text, e.g.

extern int uc2723 ( char *cp1, int ip2, char cp3[][133], int ip4, int ip5,
    double *rp6, int ip7,  int ip8, double rp9, int ip10 )
{
    int error_code =0;

    if( cp1 == NULL || strlen(cp1) > 30 )
          return UF_err_bad_parameter_number_1;
    else if (cp3 == NULL)
    {
         error_code = (UF_err_bad_parameter_number_3);
    }
    else
    {
        char *string, text[132*80];
        int line , len, total_offset;
        UF_DISP_view_type_t which_views;
        int MAXLEN= 80;
        UF_OBJ_disp_props_t color;
        UF_DISP_text_ref_t ref_point;
        tag_t view_tag;
        double text_abs[3];

        if (ip4 > MAXLEN)
           ip4 = MAXLEN;

        ip5 = 0;

        which_views = (UF_DISP_view_type_t)ip2;
        color.color =  ip8;
        ref_point = (UF_DISP_text_ref_t)ip7;

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
            string = &text[0];
            total_offset =0;

            for (line =0; line< ip4; line++)
            {
                len = strlen(cp3[line]);
                strncpy(string, &(cp3[line][0]),len);
                string[len] = '\n';
                total_offset = total_offset + len + 1;
                string = &text[total_offset];
            }

            text[total_offset] = '\0';

            FTN(map12)(rp6,text_abs);
            UF_CSYS_map_point(UF_CSYS_WORK_COORDS, rp6,
                              UF_CSYS_ROOT_COORDS, text_abs);
            error_code = UF_DISP_display_temporary_text(
                                   view_tag, which_views,text,text_abs,
                                   ref_point,&color,rp9,ip10);
        }
    }

    return ( error_code );
}

*/
extern UFUNEXPORT int uc2723(char *cp1, int ip2, char cp3[][133]/* <I,len:ip4>*/, int ip4, int ip5, double
 *rp6, int ip7, int ip8, double rp9, int ip10);

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
char cfont[16]  /* <O>
                The font name at index number "findx".  The
                current value of UF_DRF_MAX_FONT_LEN is
                16. The function outputs a C string. If there is no
                font at a particular index, the function outputs a
                blank string.
                */
);
/*
  uf5546 is replaced by UF_DRF_create_crosshatch,

extern void FTN(uf5546)(
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
extern UFUNEXPORT void FTN(uf5546)(
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

extern UFUNEXPORT int UF_KF_ask_edit_method
(
    int *edit_method  /* <O> edit method
                             0 = edit existing rule
                             1 = delete, then re-create rule */
);
extern UFUNEXPORT int UF_KF_set_edit_method
(
    int new_method  /* <I> edit method
                             0 = edit existing rule
                             1 = delete, then re-create rule */
);

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
 * Function will be obsoleted in NX3, please call UF_MSAO_set_refs()
 * instead.
 *
 *
 * Sets faces to be analysed by MSAO.
 *
 * Environment: Internal and External
 *
 * See Also: UF_MSAO_ask_num_faces
 *           UF_MSAO_ask_face
 *
 * History:  Originally released in V19,
 ***************************************************************************/
extern UFUNEXPORT int UF_MSAO_set_faces(
  tag_t msao,          /* <I>   tag of MSAO. */
  tag_t *faces,        /* <I,len:num_faces>
                       array of faces. */
  int num_faces        /* <I>   number of faces in the array. */
);


/**************************************************************************
 *
 * Function will be obsoleted in NX3, please call UF_MSAO_ask_num_refs()
 * instead.
 *
 *
 * Asks number of faces of the MSAO.
 *
 * Environment: Internal and External
 *
 * See Also: UF_MSAO_set_faces
 *           UF_MSAO_ask_face
 *
 * History:  Originally released in V19
 ***************************************************************************/
extern UFUNEXPORT int UF_MSAO_ask_num_faces(
  tag_t msao,          /* <I>   tag of MSAO. */
  int   *num_faces     /* <O>   number of faces. */
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

/* uc6570 create generic entity -- replaced by UF_UDOBJ_create_udo */
extern UFUNEXPORT int uc6570(int ip1, double *rp2, int ip3, int *ip4, int ip5, double *rp6,
                  int ip7, char cp8[][133]/* <I,len:ip7>*/, int ip9, tag_t *np10, tag_t *nr11);



/******************************************************************************
Edits projection curves using an advanced rebuild option

Environment: Internal and External

See Also:  UF_CURVE_edit_proj_curves

History: Release in NX3

Notes:
   This function should be replaced with UF_CURVE_edit_by_curve_fit_data.
   This function will be obsolete from NX5 on
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_proj_curves_with_rebuild
(
 tag_t                   int_curve_object,  /* <I> Feature tag of intersection curve to edit */
 UF_CURVE_curve_fit_data curve_fit_data     /* <I> curve fit data */
);

/******************************************************************************
Edits Intersection curves using an advanced rebuild option

Environment: Internal and External

See Also:  UF_CURVE_edit_int_object

History: Release in NX3

Notes:
   This function should be replaced with UF_CURVE_edit_by_curve_fit_data.
   This function will be obsolete from NX5 on
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_int_object_with_rebuild
(
 tag_t                   int_curve_object,  /* <I> Feature tag of intersection curve to edit */
 UF_CURVE_curve_fit_data curve_fit_data     /* <I> curve fit data */
);

/* System Interface Description */
struct UF_ROUTE_system_interface_s
{
    char *name;
    char *description;
    char *parameters;
    char *bitmap;
    int   type;
    int   process_id;
};
typedef struct UF_ROUTE_system_interface_s UF_ROUTE_system_interface_t,
               *UF_ROUTE_system_interface_p_t;


/**********************************************************************
Returns the number of system interfaces and an array of these
interfaces.

Environment: Internal  and  External

See Also:

History:

Notes:
   This function has not been valid since pre-V18.  There is no
   replacement as the functionality has been obsoleted.
   This function will be obsolete from NX6 on
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_sys_ints(
void*                       app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
int  * num_system_interfaces ,/* <O>
                              Number of system interfaces.
                              */
UF_ROUTE_system_interface_p_t * system_interfaces  /* <OF,len:num_system_interfaces>
                                                   Array of system interfaces.
                                                   */
);

/**********************************************************************
Update all out-of-date stock objects.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_fix_stale_stock( void );

/*****************************************************************************
 To fetch an array of all weld objects in the specified assembly.
Optionally, filter the weld objects by weld type.
The weld_array must be freed using UF_free.

Environment : Internal and External
See Also :

History : Originally released in v16.0.1
This function should be replaced by UF_WELD_locate_welds2
*****************************************************************************/
extern UFUNEXPORT int UF_WELD_locate_welds(
tag_t           work_part,   /* <I>
                                The specified assembly to query
                             */
UF_WELD_types_t weld_type,   /* <I>
                                The weld type filter to apply to this query.
                                If no filtering is desired, then input
                                UF_WELD_ALL_TYPES . This filter can have
                                combinations like UF_WELD_GROOVE_TYPE+
                                UF_WELD_SPOT_TYPE+...
                             */
int             *count,      /* <O>
                                Pointer to the number of weld object which
                                answer the query. This may be 0.

                                This storage is not allocated by the
                                function. Pass in a valid integer location

                                If the count is not desired, pass in a NULL
                                instead of a pointer
                             */
tag_p_t         *weld_array  /* <OF,len:count>
                                The pointer in which to return the array
                                containing the tags of the found
                                weld_objects. If UF_WELD_ALL_TYPES,
                                then all of the weld objects in the
                                assembly will be returned. If any other
                                filter option, then only the objects of
                                the specified type are returned.

                                If NULL is passed in instead of a pointer,
                                then the array is not returned.
                                Such an option might be used to simply
                                obtain a count of the objects.

                                If the pointer is returned as non_NULL,
                                then the array must be freed by UF_free
                              */
                                           );

/************************************************************************
 *     This routine just brings up the part selection dialog to prompt
 *     for the new part name. This routine does not actually create the part.
 *     This routine was written to provide the routine that does the
 *     same work which UF_UI_ask_create_part_filename does in native NX. In
 *     NX Manager, UF_UI_ask_create_part_filename creates the specified
 *     part, this routine can be used when you want to get the filename
 *     but not yet create the part.
 *
 * See Also:  UF_UI_ask_create_part_filename
 * Environment : Internal
 * History : Originally released in V16.0
 * This function should be replaced with UF_UI_ugmgr_ask_create_part_file_name from NX 5.0
 *  and is mandatory if Longer IDs functionality is enabled NX/Manager
 ************************************************************************/
extern UGOPENINTEXPORT int UF_UI_ugmgr_ask_create_part_name
(
     char filename[ MAX_FSPEC_BUFSIZE ], /* <O>
                                         The new part name in CLI format */
     char **part_type,                  /* <OF>
                                         The part type of the part */
     char template_name[ MAX_FSPEC_BUFSIZE ], /* <O>
                                               The seed part name */
     int  *response                      /* <O>
                                          The response from the user */
);

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
and is mandatory if Longer IDs functionality is enabled NX/Manager
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

/***********************************************************************
Adds a Product Assembly to the list of those recognised by the current
NX Manager session.

Specify the Product Assembly in CLI format.

Environment : Internal  and  External

History : Originally released in V19.0
This function should be replaced with UF_UGMGR_add_product_assembly_part from NX 5.0
and is mandatory if Longer IDs functionality is enabled NX/Manager
***********************************************************************/
extern UFUNEXPORT int UF_UGMGR_add_product_assembly
(
    const char product[ MAX_FSPEC_BUFSIZE ] /* <I,len:MAX_FSPEC_SIZE+1>  Name of the product assembly in CLI form. */
);

/***********************************************************************
Removes a Product Assembly from the list of those recognised by the
current NX Manager session.

Specify the Product Assembly in CLI format.

Environment : Internal  and  External

History : Originally released in V19.0
This function should be replaced with UF_UGMGR_remove_product_assembly_part from NX 5.0
and is mandatory if Longer IDs functionality is enabled NX/Manager
***********************************************************************/
extern UFUNEXPORT int UF_UGMGR_remove_product_assembly
(
    const char product[ MAX_FSPEC_BUFSIZE ] /* <I,len:MAX_FSPEC_SIZE+1>  Name of the product assembly in CLI form. */
);


/************************************************************************
This routine returns an array of attribute titles, and an array
of corresponding attribute values for the specified part from
the current clone operation.

   This function assumes that part attributes must be string type. This restrictriction is being removed.
   Replace with UF_CLONE_ask_part_attrs, which can handle all supported types.

Environment : Internal  and  External
See Also :
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_attribute_values
(
    const char *part_name, /* <I>
                              The name of a part in the current clone operation;
                              for native, or import, an O/S filename; in
                              NX Manager or for export, a CLI name
                           */
    int        *n_attributes,    /* <O>
                                    the number of attributes returned
                                 */
    char     ***attribute_titles, /* <OF,len:n_attributes> with UF_free_string_array
                                   the attribute titles
                                */
    char     ***attribute_values /* <OF,len:n_attributes> with UF_free_string_array
                                   the attribute values
                                */
);

/*****************************************************************************

This routine copies the attributes of the source object to all its immediate linked objects
provided the linked objects are loaded.

   The functionality provided by this function will soon no longer be required (planned for NX7).
   At that time, the calls to this function should be removed.
   Any subsequent call to UF_MODL_update or a function that includes a model update will then
   cause the copying of the attributes from the source object to linked objects.

   NOTE: Until the function is actually retired, you need to continue to call this function.
         This is just a warning that it will go away.

Environment: Internal  and  External

See Also:

******************************************************************************/
extern UFUNEXPORT int UF_WAVE_copy_attributes
(
 tag_t source_object /* <I>
                        The object that has changed attributes
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

/*********************************************************************
Detach the segments from their follow curves by removing the associativity
between the segments and their follow curves, removing the associativity
between the guide curve and the follow curve, and either making their rcps
absolute or redefining them in terms of the follow curve of another segment
that we are not detaching

As of NX1, this function is incompatible with the Routing data model.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_detach_segments (
int segment_count,  /* <I>
                    The number of segments to be detached
                    */

tag_p_t segments    /* <I,len:segment_count>
                    An array of tags of the segments to be detached
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
#define UF_CLEAR_FULL_FACET             ( UF_CLEAR_FACET_BASED | \
                                          UF_CLEAR_EXHAUSTIVE_FACET_MODE )
/*
  UF_CLEAR_FACET_SOLID will perform analysis based on loaded solids where
      possible, but will fall back on analyzing facetted representations
      where they are loaded instead of solids.  Solid analysis is slower,
      so depending on the mix of facets and solids that are loaded in the
      session, the performance of UF_CLEAR_FACET_SOLID will fall somewhere
      between the performance of UF_CLEAR_QUICK_FACET and UF_CLEAR_SOLID.
      This mode maps into the interactive mode Use Solids Where Available.
*/
#define UF_CLEAR_FACET_SOLID            ( UF_CLEAR_FACET_BASED | \
                                          UF_CLEAR_SOLID_BASED )
/*
  UF_CLEAR_SOLID is the most accurate and slowest analysis mode.  It does
      analysis based on solid bodies exclusively.  In cases where solid
      data is not loaded, demand loading will occur so that the analysis
      can be performed.  This maps to the interactive mode Use Solids.
*/
#define UF_CLEAR_SOLID                  UF_CLEAR_SOLID_BASED
#define UF_CLEAR_BEST_AVAILABLE         ( UF_CLEAR_FACET_SOLID | \
                                          UF_CLEAR_BEST_AVAILABLE_BASED )

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

/******************************************************************************

Creates a thread feature.  Specify the creation parameters in the
thread parameter structure. For internal thread, argument "internal_thread"
can be set as "TRUE".

IMPORTANT: This function will be removed in NX10. All current callers of this function
need to be modified to call UF_MODL_create_symb_thread and set the value of "internal_thread"
in parameters structure.

Environment: Internal  and  External
See Also: 
  UF_MODL_symb_thread_data_p_t
History: This function is new to NX8.5.1.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_symb_thread_2(
UF_MODL_symb_thread_data_p_t parameters ,/* <I>
                                         Pointer to thread parameter structure
                                         UF_MODL_symb_thread_data_s
                                         */
logical internal_thread , /* <I> "TRUE" for internal thread, else "FALSE" */
tag_t * thread_obj_id  /* <O>
                       Thread object id
                       */
);

/******************************************************************************
Edits a thread feature. This function will need a data structure as input.
If you do not intend to change a component of type char* of the structure,
 please initialize it as NULL. Before calling this function, you can call
UF_MODL_ask_symb_thread_parms to check the existing thread parameters.

Note that you are not allowed to edit the first three fields of the data
structure: cyl_face, start_face, and axis_direction. Only if a thread is
created by the option "manual input" instead of "choose from table",
can you edit pitch, angle, minor and major diameters. Manual defined thread
has an empty callout, so you can know whether a thread is created by "manual input"
by checking if the callout is NULL, but you can not simply set callout = NULL.

For internal thread, argument "internal_thread" can be set as "TRUE".

As any other editing function, you may need to call UF_MODL_update to view
your feature changes for internal Open API applications.

IMPORTANT: This function will be removed in NX10. All current callers of this function
need to be modified to call UF_MODL_edit_symb_thread and set the value of "internal_thread"
in parameters structure.

Environment: Internal  and  External
See Also:
 UF_MODL_symb_thread_data_p_t
History: This function is new to NX8.5.1.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_symb_thread_2(
tag_t thread_obj_id ,/* <I>
                     Thread object id
                     */
logical internal_thread , /* <I> "TRUE" for internal thread, else "FALSE" */  
UF_MODL_symb_thread_data_p_t parameters  /* <I>
                                         Pointer to thread parameter
                                         structure UF_MODL_symb_thread_data_s
                                         */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY


#endif /* UF_RETIRING */
