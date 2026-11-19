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
#include <uf_defs.h>
#include <uf_draw_types.h>
#include <uf_plist_types.h>
#include <uf_retiring_ugopenint.h>
#include <setjmp.h>
#include <uf_curve.h>
#include <uf_weld_types.h>
#include <uf_sf_post_datatypes.h>
#include <uf_ugmgr_types.h>
#include <uf_pd_types.h>

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
                  char *cr1 /* <O> Part Attribute Name */
);

/* uc5093 cycle attributes of archived part */
extern UFUNEXPORT int uc5093(
                  int *ia1, /* <I/O> Cycle State (current Attribute number)
                                     <I> 0 = Begin Cycling
                                     <O> 1 = Next Attribute returned
                                     <O> 0 = All attributes processed */
                  char *cr2, /* <O>  Part attribute title */
                  char *cr3  /* <O>  Part attribute Value */
);

/* uc5095 read name of current object during Cycling*/
extern UFUNEXPORT int uc5095(
                  char *cr1 /* <O> Name of currently cycled entity */
);

/* uc5096 cycle attributes of current archive object */
extern UFUNEXPORT int uc5096(
                  int *ia1, /* <I/O> Cycle State (current attribute number)
                                     <I> 0 = Begin Cycling
                                     <O> 1 = Next Attribute returned
                                     <O> 0 = All attributes processed */
                  char *cr2, /* <O> Attribute title */
                  char *cr3  /* <O> Attribute Value */
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
extern UFUNEXPORT int uc5102(tag_t np1, char *cp2, int ip3);

/* uc5104 Read a string attribute title.
   This functions should be replaced with UF_ATTR_cycle
   e.g.
     int uc5104(tag_t np1, int ip2, char *cr3, int *ir4)
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_string;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];
         char attribute[UF_ATTR_MAX_STRING_LEN];

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
extern UFUNEXPORT int uc5104(tag_t np1, int ip2, char *cr3, int *ir4);

/* uc5105 Read an attribute value.
   This functions should be replaced with UF_ATTR_cycle
   e.g.
     int uc5105(tag_t np1, int ip2, char *cr3, int *ir4);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_string;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];
         char attribute[UF_ATTR_MAX_STRING_LEN];

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
extern UFUNEXPORT int uc5105(tag_t np1, int ip2, char *cr3, int *ir4);

/* uc5109 find string attribute sequence number
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5109(tag_t np1, char *cp2, int ip3)
     {
         int indx = 0;
         int i=0;
         int type = UF_ATTR_string;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];
         char attribute[UF_ATTR_MAX_STRING_LEN];
         logical first_time = TRUE;

         uf_value.type = UF_ATTR_string;
         uf_value.value.string = attribute;

         while( indx !=0 || first_time )
         {
             first_time = FALSE;
             UF_ATTR_cycle(np1, &indx, UF_ATTR_string, attr_title, &uf_value);
             i++;
             if( strcmp( cp2, attr_title ) == 0 )
                 break;
         }
         if( indx == 0 )
             return 0;
         else
             return i;
     }
*/
extern UFUNEXPORT int uc5109(tag_t np1, char *cp2, int ip3);

/* uc5113 find integer attribute sequence number
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5113(tag_t np1, char *cp2);
     {
         int indx = 0;
         int i=0;
         int type = UF_ATTR_integer;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];
         logical first_time = TRUE;

         uf_value.type = UF_ATTR_integer;

         while( indx !=0 || first_time )
         {
             first_time = FALSE;
             UF_ATTR_cycle(np1, &indx, UF_ATTR_integer, attr_title, &uf_value);
             i++;
             if( strcmp( cp2, attr_title ) == 0 )
                 break;
         }
         if( indx == 0 )
             return 0;
         else
             return i;
     }
*/
extern UFUNEXPORT int uc5113(tag_t np1, char *cp2);

/* uc5114 read integer attribute title and value
   This functions should be replaced with UF_ATTR_cycle
   e.g.
     int uc5114(tag_t np1, int ip2, char *cr3, int *ir4);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_integer;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];

         uf_value.type = UF_ATTR_integer;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_integer, attr_title, &uf_value);
         }

         strcpy(cr3, attribute);
         *ir4 = uf_value.value.i;
     }
*/
extern UFUNEXPORT int uc5114(tag_t np1, int ip2, char *cr3, int *ir4);

/* uc5117 find floating point attribute sequence number
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5117(tag_t np1, char *cp2);
     {
         int indx = 0;
         int i=0;
         int type = UF_ATTR_real;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];
         logical first_time = TRUE;

         uf_value.type = UF_ATTR_real;

         while( indx !=0 || first_time )
         {
             first_time = FALSE;
             UF_ATTR_cycle(np1, &indx, UF_ATTR_real, attr_title, &uf_value);
             i++;
             if( strcmp( cp2, attr_title ) == 0 )
                 break;
         }
         if( indx == 0 )
             return 0;
         else
             return i;
     }
*/
extern UFUNEXPORT int uc5117(tag_t np1, char *cp2);

/* uc5118 read floating point attribute
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5118(tag_t np1, int ip2, char *cr3, double *rr4);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_real;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];

         uf_value.type = UF_ATTR_real;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_real, attr_title, &uf_value);
         }

         strcpy(cr3, attribute);
         *rr4 = uf_value.value.d;
     }
*/
extern UFUNEXPORT int uc5118(tag_t np1, int ip2, char *cr3, double *rr4);

/* uc5121 find null attribute sequence number
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5121(tag_t np1, char *cp2);
     {
         int indx = 0;
         int i=0;
         int type = UF_ATTR_null;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];
         logical first_time = TRUE;

         uf_value.type = UF_ATTR_null;

         while( indx !=0 || first_time )
         {
             first_time = FALSE;
             UF_ATTR_cycle(np1, &indx, UF_ATTR_null, attr_title, &uf_value);
             i++;
             if( strcmp( cp2, attr_title ) == 0 )
                 break;
         }
         if( indx == 0 )
             return 0;
         else
             return i;
     }
*/
extern UFUNEXPORT int uc5121(tag_t np1, char *cp2);

/* uc5122 read null attribute title
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5122(tag_t np1, int ip2, char *cr3);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_null;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];

         uf_value.type = UF_ATTR_null;
         for( i=0; i<ip2; i++)
         {
             UF_ATTR_cycle(np1, &indx, UF_ATTR_null, attr_title, &uf_value);
         }

         strcpy(cr3, attribute);
     }
*/
extern UFUNEXPORT int uc5122(tag_t np1, int ip2, char *cr3);

/* uc5125 find date & time attribute sequence number
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5125(tag_t np1, char *cp2);
     {
         int indx = 0;
         int i=0;
         int type = UF_ATTR_time;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];
         logical first_time = TRUE;

         uf_value.type = UF_ATTR_time;

         while( indx !=0 || first_time )
         {
             first_time = FALSE;
             UF_ATTR_cycle(np1, &indx, UF_ATTR_time, attr_title, &uf_value);
             i++;
             if( strcmp( cp2, attr_title ) == 0 )
                 break;
         }
         if( indx == 0 )
             return 0;
         else
             return i;
     }
*/
extern UFUNEXPORT int uc5125(tag_t np1, char *cp2);

/* uc5126 read date & time attribute
   This function should be replaced with UF_ATTR_cycle
   e.g.
     int uc5126(tag_t np1, int ip2, char *cr3, int *ir4);
     {
         int indx = 0;
         int i;
         int type = UF_ATTR_time;
         UF_ATTR_value_t uf_value;
         char attr_title[UF_ATTR_MAX_TITLE_LEN];

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
extern UFUNEXPORT int uc5126(tag_t np1, int ip2, char *cr3, int *ir4);

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
extern UFUNEXPORT int uc2703(char *cp1);

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
extern UFUNEXPORT int uc2720(char *cp1, int ip2, double *rp3, int ip4, int ip5);

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
extern UFUNEXPORT int uc2721(char *cp1, int ip2, double *rp3, int ip4, int ip5, int ip6);

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
extern UFUNEXPORT int uc2722(char *cp1, int ip2, double *rp3, int ip4, int ip5, int ip6);

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
extern UFUNEXPORT int uc2723(char *cp1, int ip2, char cp3[][133], int ip4, int ip5, double
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
extern UFUNEXPORT int uc5520(int *ir1, double *rr2, char *cr3, char *cr4);

/* uc5521 set drafting parameters - replaced by UF_DRF_set_preferences:
extern int uc5521(int *ip1, double *rp2, char *cp3, char *cp4)
     {
         int error=0;
         error = UF_DRF_set_preferences(ip1, rp2, cp3, cp4);
         return (error);
     }
*/
extern UFUNEXPORT int uc5521(int *ip1, double *rp2, char *cp3, char *cp4);

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

/* The next two enums and three structures aren't used anymore.  Moving from
uf_sf_types.h to here in NX7. */

/*  Element types supported by Auto Solid Mesher  */
enum UF_SF_asm_element_types_e
{
    UF_SF_ASM_SYSTEM_DEFAULT_TYPE = 0,  /* System default. */
    UF_SF_ASM_TETRA,                    /* Elements are tetrahedral. */
    UF_SF_ASM_TETRA_10                  /* Elements are tetrahedral with 10
                                           nodes. */
};
typedef enum UF_SF_asm_element_types_e UF_SF_asm_element_types_t;


/*  Auto Solid Mesher contact types  */
enum UF_SF_contact_types_e
{
    UF_SF_ASM_FIXED = 0,
    UF_SF_ASM_FREE
};
typedef enum UF_SF_contact_types_e UF_SF_contact_types_t;


/*********************** ASM attributes and parameters ************************/

/* Mesh attributes related to model geometry */
struct  UF_SF_asm_mesh_attributes_data_s
{
    double              max_elem_size;  /*  Maximum Element Size        */
    double              min_elem_size;  /*  Minimum Element Size        */
    int                 check_aspect_ratio;     /*  0 = OFF  , 1 = ON   */
    double              aspect_ratio;   /*  Aspect ratio value > 0.     */
    int                 curvature_control;      /*  0 = OFF  , 1 = ON   */
    double              curvature_factor;       /*  Curvature value > 0.*/
    int                 small_feature_control;  /*  0 = OFF  , 1 = ON   */
    double              small_feature_factor;   /*  Feature factor value > 0. */
    UF_SF_contact_types_t  contact_type;        /*  FIXED or FREE       */
};
typedef struct  UF_SF_asm_mesh_attributes_data_s
                                             UF_SF_asm_mesh_attributes_data_t,
                                            *UF_SF_asm_mesh_attributes_data_p_t;

/* Parameters unique to the Auto Solid Mesher */
struct UF_SF_asm_mesh_parameters_data_s
{
    UF_SF_asm_element_types_t  element_type;    /*  TETRA or TETRA_10   */
    double              def_elem_size;          /*  Default Element Size*/
    int                 model_augmentation;     /*  0 = OFF  , 1 = ON   */
    int                 surface_smoothing;      /*  0 = OFF  , 1 = ON   */
    int                 explicit_smoothing;     /*  0 = OFF  , 1 = ON   */
    int                 midnode_snapping;       /*  0 = OFF  , 1 = ON   */
};
typedef struct UF_SF_asm_mesh_parameters_data_s
                                             UF_SF_asm_mesh_parameters_data_t,
                                            *UF_SF_asm_mesh_parameters_data_p_t;

/* Mesh attributes and parameters structure */
struct UF_SF_asm_mesh_data_s
{
    UF_SF_asm_mesh_attributes_data_p_t  attribs;
    UF_SF_asm_mesh_parameters_data_p_t  params;

};
typedef struct UF_SF_asm_mesh_data_s  UF_SF_asm_mesh_data_t,
                                     *UF_SF_asm_mesh_data_p_t;

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
char * cp1 ,/* <I>
            File Specification of CGM
            */
char * cr2  /* <O>
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
char * line_1 ,/* <I>
               Line 1 of header (131 character max.).  This line is
               displayed in the heading of the parts list to identify
               this particular field.
               */
char * line_2 ,/* <I>
               Line 2 of header (131 character max.).  This line is
               displayed in the heading of the parts list to identify
               this particular field.  This line is directly under line_1.
               */
char * attr_title ,/* <I>
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
char * attr_title ,/* <I>
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
char * attr_title ,/* <I>
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

/****************************************************************************
Delete objects of a mechanism.

This function has been retired.  Call UF_OBJ_delete_object or
UF_OBJ_delete_array_of_objects instead. (See uf_obj.h)

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6009)(
tag_t *np1 /*<I>
             The object to be deleted.
           */
);

/****************************************************************************
Cycle by mechanism object.  This function takes the object identifier and
object type entered and returns the next object identifier of the same type.
This function is specific to mechanisms.

This routine has been retired.  Call UF_OBJ_cycle_objs_in_part instead.
In past releases UF_OBJ_cycle_objs_in_part would not work for mechanism data.
However, since we now have only a single mechanism per part, it now works.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6010)(
tag_t *na1, /* <I/O>
               On input this is the previous tag found, use a NULL tag to
               start cycling.  On output, this is the next tag.  A NULL tag
               is output when the cycle is complete.
            */
int *ip2,   /* <I>
               Object Type To Cycle
               85 = Mechanism
               86 = Joint
               87 = Link
               88 = Spring
               90 = Force
               97 = Marker
               98 = Damper
               99 = Torque
            */
int *ir3     /* <O>
                Error Flag
                0 = No errors
                1 = Object type not valid
             */
);

/****************************************************************************
Create New Mechanism and Setup Common

Initializes the mechanism name, assigns an object identifier, and sets
up parameters needed for the mechanism. Use this routine for parts
without existing mechanisms.

This function is retired.  Use UF_SF_create_scenario to create a new
scenario part and use UF_MOTION_initialize to set all the common
parameters for mechanism and motion objects.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int uc6001(
char * cp1 ,/* <I>
            Mechanism name (30 char max)
            */
tag_t * nr2  /* <O>
             Mechanism object identifier
             */
);

/****************************************************************************
Edit/Add Joint Motion Inputs

Motion inputs may only be applied to slider or revolute joints.

Return:
         Error Flag
        0 = No Errors
        1 = Joint object identifier Not Valid
        2 = Type Not Valid

This function is retired.  Please call UF_MOTION_set_joint_motion_input instead.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int uc6025(
tag_t np1 ,/* <I>
           Joint object identifier
           */
int  ip2 ,/* <I>
          Type
          1 = Function String In cp3
          2 = Parameters In rp4 And ip5
          3 = Constant In rp4
          4 = Harmonic In rp4
          */
char * cp3 ,/* <I>
            Function String  (200 char max) - If ip2 = 1
            */
double * rp4 ,/* <I>
              Real Values (10 element array)
              10 Parameter Values - If ip2 = 2
              3 Constant Values  - If ip2 = 3
              4 Harmonic Values - If ip2 = 4
              */
int ip5  /* <I>
         Integer Parameter Value - If ip2 = 2
         */
);

/****************************************************************************
Add a Link to a Mechanism

Return:
         Error Flag
        0 = No Errors
        1 = Number Of object identifier's Not Valid - <1
        2 = Geometry object identifier's Not Valid

This function is retired.  Please call UF_MOTION_create_link instead.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int uc6031(
char *   cp1 ,/* <I>
              Link Name (30 char *)
              */
int   ip2 ,/* <I>
           Number Of Geometry object identifier's
           */
tag_t *   np3 ,/* <I>
               Geometry object identifier's
               */
tag_t *  nr4  /* <O>
              Link object identifier
              */
);
/****************************************************************************
Read link weight, inertias and cog.  Inertia values represent the moments of
inertia of the mass of the link about the X, Y and Z axes and the products of
inertia of the mass with respect to the perpendicular axes XY, XZ, and YZ.

This function is retired.  Please call UF_MOTION_ask_link_mass_properties
instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6032)(
tag_t *np1, /* <I>
               Link object identifier
            */
int *ir2, /* <O>
             Weight Flag
             0 = No Weight
             1 = Weight Present In RR3
          */
double *rr3, /* <O>
                The weight.
             */
int *ir4, /* <O>
             Inertia Flag
             0 = No Inertias
             1 = Inertias Present in RR5, RR6, RR7
          */
double *rr5, /* <O>
                A six element array that will be filled with the inertias.
             */
double *rr6, /* <O>
               A three element array that will be filled with the inertia
               location.
             */
tag_t *nr7, /* <O>
               Inertia orientation matrix object identifier
             */
int *ir8, /* <O>
             COG Flag
             0 = No COG
             1 = COG Present In RR9
          */
double *rr9, /* <O>
                Three element array to receive the COG location.
             */
int *ir10 /* <O>
             Error Flag
             0 = No Errors
             1 = Link object identifier not valid
          */
);

/****************************************************************************
Return the Number of Geometry Object ID's Attached to Link

This function is retired.  Please call UF_MOTION_ask_link instead.

Environment: Internal  and  External
See Also:
History: In V10 and beyond, skeleton geometry is not valid.
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6035)(
tag_t *np1,          /* <I>
                        Link object identifier
                     */
int *ir2,            /* <O>
                        Number Of Existing Geometry object identifier's
                     */
int *ir3,            /* <O>
                        Number Of Skeleton Geometry object identifier's
                     */
int *ir4             /* <O>
                        Error Flag
                            0 = No Error
                            1 = Link object identifier Not Valid
                     */
);
/****************************************************************************
Read the Geometry Object ID Associated with a Link

This function is retired.  Please call UF_MOTION_ask_link instead.

Environment: Internal  and  External
See Also:
History: In V10 and beyond, skeleton geometry is not valid.
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6036)(
tag_t *np1,       /* <I>
                     Link object identifier
                  */
int *ip2,         /* <I>
                     Instance Of The object identifier Requested
                  */
int *ip3,         /* <I>
                     Flag
                         1 = Existing Geometry
                         2 = Skeleton Geometry
                  */
tag_t *nr4,       /* <O>
                     Geometry object identifier
                  */
int *ir5          /* <O>
                     Error Flag
                           0 = No Errors
                           1 = Link object identifier Not Valid
                           2 = Instance Number Not Valid
                           3 = Flag Not Valid
                  */
);
/****************************************************************************
Edit/Add Link Weight

This function is retired.  Please call UF_MOTION_set_link_mass_properties
instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6044)(
tag_t *np1,      /* <I>
                    Link object identifier
                 */
double *rp2,     /* <I>
                    Weight
                 */
int *ir3         /* <O>
                    Error Flag
                         0 = No Errors
                         1 = Link object identifier Not Valid
                 */
);
/****************************************************************************
Edit/Add Inertias to Link

This function is retired.  Please call UF_MOTION_set_link_mass_properties
instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6046)(
tag_t *np1,       /* <I>
                     Link object identifier
                  */
double *rp2,      /* <I>
                     Inertias
                  */
double *rp3,      /* <I>
                     Inertia Location
                  */
tag_t *np4,       /* <I>
                     Inertia Matrix object identifier
                  */
int *ir5          /* <O>
                     Error Flag
                           0 = No Errors
                           1 = Link object identifier Not Valid
                           2 = Inertia Matrix object identifier Not Valid
                  */
);

/****************************************************************************
Edit/Add Center of Gravity to Link

This function is retired.  Please call UF_MOTION_set_link_mass_properties
instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6048)(
tag_t *np1,       /* <I>
                     Link object identifier
                  */
double *rp2,      /* <I>
                     COG Location
                  */
int *ir3          /* <O>
                     Error Flag
                         0 = No Errors
                         1 = Link object identifier Not Valid
                  */
);

/****************************************************************************
Add a Marker to a Mechanism.  Markers to add to a mechanism marker represent
points of interest with respect to links. Analysis results can be obtained for
markers.

This function is retired.  Call UF_MOTION_create_marker instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void FTN(uf6071)(
tag_t *np1,       /* <I>
                     Link object identifier
                  */
int *ip2,         /* <I>
                     Marker Type
                          0 = Link Inertia CSYS Origin
                              (Not Displayable)
                          1 = Regular Marker
                          2 = Center Of Gravity Marker
                     Note - 0 And 2 Are Available For Internal User
                            Function Use, Only
                  */
double *rp3,      /* <I>
                     Marker Location
                  */
tag_t *nr4,       /* <O>
                     Marker object identifier
                  */
int *ir5          /* <O>
                     Error Flag
                           0 = No Errors
                           1 = Link object identifier Not Valid
                           2 = Type Not Valid
                  */
);

/****************************************************************************
Allows you to create gear joints between two revolutes or a revolute
and slider joint. The contact point defines the point of contact and the
gear ratio. The z-axis of the orientation matrix must be tangent to
the pitch circles.

This function is retired.  Call UF_MOTION_create_joint_coupler instead.

Return:
         Error Code:
        0 = no errors
        1 = revolute  already associated to gear joint
        2 = revolute or slider associated to gear joint
        3 = input joints do not have  a valid common
                 link. Common link must be second object
                 of input joints
        4 = invalid revolute or slider configuration
        5 = Contact Point Causes Invalid Gear Ratio
        6 = Invalid Orientation Matrix
        7 = revolute_obj is an invalid object
        8 = joint_obj is an invalid object

Environment: Internal  and  External

See Also:

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MECH_create_gear_joint(
tag_t  revolute_obj ,/* <I>
                     Revolute object identifier
                     */
tag_t  rev_or_slider ,/* <I>
                      Revolute or Slider object identifier
                      */
double contact_point[3] ,/* <I>
                         Contact Point
                         */
double contact_orientation[9] ,/* <I>
                               Contact Point Orientation
                               */
tag_t * joint_obj  /* <O>
                   Gear Joint object identifier
                   */
);


/*------------------------------------------------------------------------
Creates scenario part file from parent part (non scenario part file).

Calls to this function should be replaced with calls to
UF_SF_create_scenario_nx.

The input name should be shorter than 26 characters and should not
include path name. The reason for that is the scenario subdirectory is
associated to the master model part.

Environment: Internal  and  External

See Also:

History:
*------------------------------------------------------------------*/
extern UFUNEXPORT int UF_SF_create_scenario(
char* scenario_name ,/* <I>
                     Name of Scenario part file to create.
                     */
tag_t* new_scenario_tag /* <O>
                         Tag of created Scenario part file.
                         */
);



/* uc6570 create generic entity -- replaced by UF_UDOBJ_create_udo */
extern UFUNEXPORT int uc6570(int ip1, double *rp2, int ip3, int *ip4, int ip5, double *rp6,
                  int ip7, char cp8[][133], int ip9, tag_t *np10, tag_t *nr11);



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

/*******************************************************************************
  UF_CURVE_edit_joined_feature_with_rebuild.

  Notes:
    This function should be replaced with UF_CURVE_edit_by_curve_fit_data.
    This function will be obsolete from NX5 on
******************************************************************************/
extern int UF_CURVE_edit_joined_feature_with_rebuild
(
 tag_t                   curve_feature,   /* <I> */
 UF_CURVE_curve_fit_data curve_fit_data   /* <I> */
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
     char filename[MAX_FSPEC_SIZE + 1], /* <O>
                                         The new part name in CLI format */
     char **part_type,                  /* <OF>
                                         The part type of the part */
     char template_name[MAX_FSPEC_SIZE + 1], /* <O>
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
    char       display_name[MAX_FSPEC_SIZE + 1]   /* <O>
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
char encoded_name[MAX_FSPEC_SIZE+1] ,/* <I>
                     Encoded form of the part file name. Declare
                     this parameter with array size
                     MAX_FSPEC_SIZE+1.
                     */
char part_number[UF_UGMGR_PARTNO_SIZE+1] ,/* <O>
                    Part number. Declare this parameter with array
                    size UF_UGMGR__PARTNO_SIZE+1.
                    */
char part_revision[UF_UGMGR_PARTREV_SIZE+1] ,/* <O>
                      Part revision. Declare this parameter with array
                      size UF_UGMGR_PARTREV_SIZE+1.
                      */
char part_file_type[UF_UGMGR_FTYPE_SIZE+1] ,/* <O>
                       Part file type. Declare this parameter with array
                       size UF_UGMGR_FTYPE_SIZE+1.
                       */
char part_file_name[UF_UGMGR_FNAME_SIZE+1]  /* <O>
                       Part file name. Declare this parameter with
                       array size UF_UGMGR_FNAME_SIZE+1.
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
char cli_name[MAX_FSPEC_SIZE+1]  /* <O>
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
    const char product[MAX_FSPEC_SIZE+1] /* <I,len:MAX_FSPEC_SIZE+1>  Name of the product assembly in CLI form. */
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
    const char product[MAX_FSPEC_SIZE+1] /* <I,len:MAX_FSPEC_SIZE+1>  Name of the product assembly in CLI form. */
);


/***********************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*    creates a combined load case from the input load components and scales.
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
*************************************************************************/
extern  UFUNEXPORT int UF_SF_POST_create_combined_lcase
(
char    *clc_name,                /* <I> Name of the combined load case */
int      num_lcases,              /* <I> Number of Load Case Components */
int     *lcase_list,              /* <I> List of Load Case Component Numbers */
double  *lcase_scales,            /* <I> List of Load Case Scale factors */
int     *new_clc_num              /* <O> New Combined Load Case Number */
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* deletes a combined load case with the specified name.
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
****************************************************************************/
extern  UFUNEXPORT int UF_SF_POST_delete_combined_lcase
(
char   *clc_name                   /* <I>  Name of the combined load case */
);

/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  displays the model with the current values of result.
*
* Environment:  Internal and External
*
* History: Originally released in NX3
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_display_results(void);

/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* exit overlay mode
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_exit_overlay
(
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*   exports the current display to a file
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_export_display_to_text
(
    const char *file_name_with_extn,              /*<I> Name of file with relevant extension*/
    UF_SF_POST_file_type_t file_form              /*<I> Desired format of the file:
                                                           UF_SF_POST_FILE_ASCII
                                                           UF_SF_POST_FILE_VRML */
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  exports the current display to a vrml file
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_export_vrml
(
    const char *file_name                           /* <I> VRML file name */
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
 **************************************************************************/

extern UFUNEXPORT tag_t UF_SF_POST_get_component_unit_tag(
    UF_SF_POST_result_comp_t comp_type,/*<I> Type of results results to be set */
    const char *unit_type_selected /*<I> Units string.
                                         See uf_unit_types.h for valid units */);

/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*   gets the units_tag corresponding to the type of
*         results
*   Environment:  Internal and External
*
*  History: Originally released in NX3
**************************************************************************/
extern UFUNEXPORT tag_t UF_SF_POST_get_unit_tag
(
    UF_SF_POST_result_type_quan_t result_type, /*<I> Type of results results to be set
                                                     UF_SF_POST_DISPLACEMENT
                                                     UF_SF_POST_ROTATION
                                                     UF_SF_POST_CONTACT_DISP
                                                     UF_SF_POST_VELOCITY
                                                     UF_SF_POST_ACCELERATION
                                                     UF_SF_POST_STRESS
                                                     UF_SF_POST_STRAIN
                                                     UF_SF_POST_STRAIN_E
                                                     UF_SF_POST_STRAIN_ED
                                                     UF_SF_POST_STRAIN_EE
                                                     UF_SF_POST_THICKNESS
                                                     UF_SF_POST_TEMPERATURE
                                                     UF_SF_POST_TEMP_GRAD
                                                     UF_SF_POST_HEAT_FLUX
                                                     UF_SF_POST_THERMAL_ENERGY
                                                     UF_SF_POST_REACTION_HEAT_FLOW
                                                     UF_SF_POST_APPLIED_FORCE
                                                     UF_SF_POST_REACTION_FORCE
                                                     UF_SF_POST_ELEMENT_FORCE
                                                     UF_SF_POST_ELEMENT_PRESSURE
                                                     UF_SF_POST_FATIGUE_LIFE
                                                     UF_SF_POST_FATIGUE_DAMAGE
                                                     UF_SF_POST_FATIGUE_SAFETY
                                                     UF_SF_POST_STRENGTH_SAFETY
                                                     UF_SF_POST_ELEMENT_ERROR
                                               */
const char *unit_type_selected                 /*<I> Units string.
                                                     See uf_unit_types.h for valid units */
);


/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  initialises the sturcture for clip parameters with user given values
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
*****************************************************************************/
extern  UFUNEXPORT int UF_SF_POST_initialise_clip_params
(
UF_SF_post_clipping_data_t_p *clip_params,             /* <OF> Structure containing clip
                                                             parameters to be initialized
                                                       */
int                           clip_tgl_data,           /* <I> Clip toggle
                                                              default value = 1
                                                       */
int                           ghost_tgl_data,          /* <I> Ghost model toggle
                                                              value = 0 or 1
                                                       */
int                           outline_tgl_data,        /* <I> Outline model toggle
                                                              value = 0 or 1
                                                       */
int                           auto_update_tgl_data,    /* <I> Auto update toggle
                                                              default value = 1
                                                       */
int                           plane_type_data,         /* <I> Type of clip plane
                                                              UF_SF_CLIP_ABS_XY
                                                              UF_SF_CLIP_ABS_YZ
                                                              UF_SF_CLIP_ABS_ZX
                                                              UF_SF_CLIP_WCS_XY
                                                              UF_SF_CLIP_WCS_YZ
                                                              UF_SF_CLIP_WCS_ZX
                                                              UF_SF_CLIP_WCS_CYL_RT
                                                              UF_SF_CLIP_WCS_CYL_TZ
                                                              UF_SF_CLIP_WCS_SPH_TP
                                                       */
int                           clip_side_data,          /* <I> Clip side data
                                                              UF_SF_CLIP_POSITIVE
                                                              UF_SF_CLIP_NEGATIVE
                                                              UF_SF_CLIP_BOTH
                                                        */
double                        clip_value_data,          /* <I> Distance along the axis */
int                           clip_scale_data,          /* <I> Clip scale toggle
                                                               Default value = 1
                                                        */
double                        clip_scale_curr_min,      /* <I> Scaling minimum
                                                               default value = 0.0
                                                        */
double                        clip_scale_curr_max,      /* <I> Scaling maximum
                                                               default value = 0.0
                                                        */
double                        scale_min,                /* default value = 0 */
double                        scale_max                 /* default value = 0 */
);


/****************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*    Initialises the structure containing deformed display parameters
*    from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 ****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_def_disp_params
(
UF_SF_POST_def_disp_t_p *def_disp,              /*<OF>
                                                  Structure Containing deformed display
                                                  parameters
                                                */
UF_SF_POST_elem_edge_style_t edge_style,        /*<I>
                                                  Display type of element edges
                                                  UF_SF_POST_ELEM_EDGE_NONE,
                                                  UF_SF_POST_ELEM_EDGE_FREE,
                                                  UF_SF_POST_ELEM_EDGE_EXTERNAL,
                                                  UF_SF_POST_ELEM_EDGE_WIRE
                                                */
UF_SF_POST_hue_colors_t edge_color,             /*<I>
                                                  Color for displaying the element edges
                                                  UF_SF_POST_BLACK,
                                                  UF_SF_POST_MAGENTA_RED,
                                                  UF_SF_POST_MAGENTA,
                                                  UF_SF_POST_BLUE_MAGENTA,
                                                  UF_SF_POST_BLUE,
                                                  UF_SF_POST_CYAN_BLUE,
                                                  UF_SF_POST_CYAN,
                                                  UF_SF_POST_GREEN_CYAN,
                                                  UF_SF_POST_GREEN,
                                                  UF_SF_POST_YELLOW_GREEN,
                                                  UF_SF_POST_YELLOW,
                                                  UF_SF_POST_ORANGE,
                                                  UF_SF_POST_RED,
                                                  UF_SF_POST_DARK_GRAY,
                                                  UF_SF_POST_LIGHT_GRAY,
                                                  UF_SF_POST_WHITE
                                                */
UF_SF_POST_elem_face_style_t face_style,        /*<I>
                                                  Type of element face display
                                                  UF_SF_POST_ELEM_FACE_NONE,
                                                  UF_SF_POST_ELEM_FACE_FILLED,
                                                  UF_SF_POST_ELEM_FACE_FILLED_TRANS,
                                                  UF_SF_POST_ELEM_FACE_AUTO
                                                */
UF_SF_POST_hue_colors_t face_color,             /*<I>
                                                  Color for the displaying the element faces
                                                  UF_SF_POST_BLACK,
                                                  UF_SF_POST_MAGENTA_RED,
                                                  UF_SF_POST_MAGENTA,
                                                  UF_SF_POST_BLUE_MAGENTA,
                                                  UF_SF_POST_BLUE,
                                                  UF_SF_POST_CYAN_BLUE,
                                                  UF_SF_POST_CYAN,
                                                  UF_SF_POST_GREEN_CYAN,
                                                  UF_SF_POST_GREEN,
                                                  UF_SF_POST_YELLOW_GREEN,
                                                  UF_SF_POST_YELLOW,
                                                  UF_SF_POST_ORANGE,
                                                  UF_SF_POST_RED,
                                                  UF_SF_POST_DARK_GRAY,
                                                  UF_SF_POST_LIGHT_GRAY,
                                                  UF_SF_POST_WHITE
                                                */
UF_SF_POST_display_marker_t display_marker,     /*<I>
                                                  Marker to display the minimum and/or
                                                  maximum values
                                                  UF_SF_POST_DISPLAY_MARKER_MIN_MAX,
                                                  UF_SF_POST_DISPLAY_MARKER_MAXIMUM,
                                                  UF_SF_POST_DISPLAY_MARKER_MINIMUM,
                                                  UF_SF_POST_DISPLAY_MARKER_NONE
                                                */
logical def_sw,                                 /*<I>
                                                  Switch to decide whether to display the deformed
                                                  model or not
                                                */
logical undef_sw                                /*<I>
                                                  Switch to decide whether to display the undeformed
                                                  model or not
                                                */
);


/**************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Initialise the structure containing deformation scaling parameters
*  from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_def_scale_params
(
UF_SF_POST_def_t_p *def_scale,                  /*<OF>
                                                  Structure Containing deformation scaling
                                                  parameters
                                                */
logical true_scale,                             /*<I>
                                                  Switch that sets the deformation of model
                                                  to be displayed in true scale
                                                */
double true_multiplier,                         /*<I>
                                                  Multiplier value for true_Scale
                                                */
logical rel_scale,                              /*<I>
                                                  Switch that sets the deformation of model
                                                  to be displayed in relative scale
                                                */
int rel_percentage                              /*<I>
                                                  Value of %, the deformation should be
                                                  relative to the undeformed model
                                                */
);


/******************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*   Initialises the the structure for deformed result parameters
*  from the variables entered as input
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
******************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_deformed_result_params
(
 UF_SF_post_deform_result_t_p   def_result_params,  /*<O> Deformed Result Parameter sturcture to be filled */
 int                            loadcase,           /*<I> Loadcase selected */
 int                            iteration,          /*<I> Iteration Selected */
 UF_SF_POST_result_type_quan_t  quan,               /*<I>
                                                          Result Type Parameter
                                                            UF_SF_POST_DISPLACEMENT
                                                            UF_SF_POST_ROTATION
                                                            UF_SF_POST_CONTACT_DISP
                                                            UF_SF_POST_VELOCITY
                                                            UF_SF_POST_ACCELERATION
                                                            UF_SF_POST_STRESS
                                                            UF_SF_POST_STRAIN
                                                            UF_SF_POST_STRAIN_E
                                                            UF_SF_POST_STRAIN_ED
                                                            UF_SF_POST_STRAIN_EE
                                                            UF_SF_POST_THICKNESS
                                                            UF_SF_POST_TEMPERATURE
                                                            UF_SF_POST_TEMP_GRAD
                                                            UF_SF_POST_HEAT_FLUX
                                                            UF_SF_POST_THERMAL_ENERGY
                                                            UF_SF_POST_REACTION_HEAT_FLOW
                                                            UF_SF_POST_APPLIED_FORCE
                                                            UF_SF_POST_REACTION_FORCE
                                                            UF_SF_POST_ELEMENT_FORCE
                                                            UF_SF_POST_ELEMENT_PRESSURE
                                                            UF_SF_POST_FATIGUE_LIFE
                                                            UF_SF_POST_FATIGUE_DAMAGE
                                                            UF_SF_POST_FATIGUE_SAFETY
                                                            UF_SF_POST_STRENGTH_SAFETY
                                                            UF_SF_POST_ELEMENT_ERROR
                                                        */
 UF_SF_POST_result_type_lay_t   lay,                    /* <I> Result Type Parameter for Layer
                                                               UF_SF_POST_AT_MID
                                                               UF_SF_POST_AT_TOP
                                                               UF_SF_POST_AT_BOT
                                                               UF_SF_POST_AT_MIN
                                                               UF_SF_POST_AT_MAX
                                                               UF_SF_POST_AT_SRP_C
                                                               UF_SF_POST_AT_SRP_D
                                                               UF_SF_POST_AT_SRP_E
                                                               UF_SF_POST_AT_SRP_F
                                                         */
 double                         scale,                   /* <I> Deformation scaling value */
 int                            def_value_choice,        /* <I> Deformation value choice */
 int                            undef_choice             /* <I> Undefrmation choice */
 );

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Initializes the structure containing fringe parameters
*  from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_fringe_params
(
UF_SF_POST_fringe_t_p *fringe_params,        /* <O> Structure containing fringe parameters */
UF_SF_POST_fringe_style_t style,             /* <I> Type of fringe style
                                               UF_SF_POST_FRINGE_NONE,
                                               UF_SF_POST_FRINGE_CONTOUR_LINES,
                                               UF_SF_POST_FRINGE_ISOSURFACES,
                                               UF_SF_POST_FRINGE_CONTOUR_BANDS,
                                               UF_SF_POST_FRINGE_SMOOTH_TONE,
                                               UF_SF_POST_FRINGE_ELEM_VALUES */
UF_SF_POST_fringe_color_spec_t spec,          /* <I> Type of color spectrum
                                                UF_SF_POST_FRINGE_COLOR_STRUCT,
                                                UF_SF_POST_FRINGE_COLOR_TEMP,
                                                UF_SF_POST_FRINGE_COLOR_GRAY */
UF_SF_POST_fringe_scale_spec_t fringe_scale,  /* <I> Type of scale spectrum
                                                     UF_SF_POST_FRINGE_SCALE_AUTOMATIC,
                                                     UF_SF_POST_FRINGE_SCALE_LINEAR,
                                                     UF_SF_POST_FRINGE_SCALE_LOG */
logical whole_sw,                             /* <I> Whole model threshold switch */
double threshold_max,                         /* <I> Threshold value maximum limit */
double threshold_min,                         /* <I> Threshold value minimum limit */
int    colors_used,                           /* <I> No of colors used */
logical trans_sw,                             /* <I> Translucency switch */
UF_SF_POST_fringe_legend_opt_t legend,        /* <I> Type of legend option
                                                UF_SF_POST_FRINGE_LEGEND_NONE,
                                                UF_SF_POST_FRINGE_LEGEND_COLOR,
                                                UF_SF_POST_FRINGE_LEGEND_DETAILED
                                              */
logical thresh_sw                             /* <I> Threshold switch */
);


/**************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Initializes the structure ident_params from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_ident_params
(
UF_SF_POST_ident_parms_t_p *ident_params,    /* <OF> Structure containing Identify parameters to
                                                    be initialized*/
UF_SF_POST_ident_action_t   action,          /* <I> Entities for action to be performed
                                                    UF_SF_POST_IDENT_N_HIGH_NODES
                                                    UF_SF_POST_IDENT_N_LOW_NODES
                                                    UF_SF_POST_IDENT_NODE_IDS
                                                    UF_SF_POST_IDENT_NODE_BY_ELEM_IDS
                                                    UF_SF_POST_IDENT_N_HIGH_ELEMS
                                                    UF_SF_POST_IDENT_N_LOW_ELEMS
                                                    UF_SF_POST_IDENT_ELEM_IDS
                                              */
int                         number,           /* <I> Node or Element ID whose value needs
                                                     to be printed in the file
                                              */
char*                       data_string,      /* <I> String containing data about
                                                     elements or nodes
                                                     ex: "1-25" or "1,3,5" etc
                                              */
logical                     list_comp_sw      /* <I> Lists all components when the value is TRUE */
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  initialises the UF_SF_POST_result_parms_t_p structure with
*  user given values. To be called before a call to UF_SF_POST_select_results
*
* Environment:  Internal and External
*
* History: Originally released in NX3
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_result_parms
(
   UF_SF_POST_result_parms_t_p     *res_params,/* <OF> Parameters for selecting results */
   int                             abs_sw,    /* <I> 1 if results are requested in absolute,
                                                 0 otherwise */
   int                             avg_sw,    /*<I> 1 if results are requested in absolute, 0 otherwise */
   int                             lcase,     /*<I> Load Case number. Index starts from 0 */
   int                             iter,      /*<I> Valid for optimization,0 in othercases */
   double                          scale,     /*<I> Scale to display results*/
   UF_SF_POST_coord_sys_type_t     coords,    /*<I> Type of coordinate system
                                                    UF_SF_POST_ABS_RECTANGULAR,
                                                    UF_SF_POST_ABS_CYLINDRICAL,
                                                    UF_SF_POST_ABS_SPHERICAL,
                                                    UF_SF_POST_WRK_RECTANGULAR,
                                                    UF_SF_POST_WRK_CYLINDRICAL,
                                                    UF_SF_POST_WRK_SPHERICAL,
                                                    UF_SF_POST_LOCAL*/
   UF_SF_POST_result_type_quan_t   quan,  /*<I> Type of results to set
                                                    UF_SF_POST_DISPLACEMENT,
                                                    UF_SF_POST_ROTATION,
                                                    UF_SF_POST_CONTACT_DISP,
                                                    UF_SF_POST_VELOCITY,
                                                    UF_SF_POST_ACCELERATION,
                                                    UF_SF_POST_STRESS,
                                                    UF_SF_POST_STRAIN,
                                                    UF_SF_POST_STRAIN_E,
                                                    UF_SF_POST_STRAIN_ED,
                                                    UF_SF_POST_STRAIN_EE,
                                                    UF_SF_POST_THICKNESS,
                                                    UF_SF_POST_TEMPERATURE,
                                                    UF_SF_POST_TEMP_GRAD,
                                                    UF_SF_POST_HEAT_FLUX,
                                                    UF_SF_POST_THERMAL_ENERGY,
                                                    UF_SF_POST_REACTION_HEAT_FLOW,
                                                    UF_SF_POST_APPLIED_FORCE,
                                                    UF_SF_POST_REACTION_FORCE,
                                                    UF_SF_POST_ELEMENT_FORCE,
                                                    UF_SF_POST_ELEMENT_PRESSURE,
                                                    UF_SF_POST_FATIGUE_LIFE,
                                                    UF_SF_POST_FATIGUE_DAMAGE,
                                                    UF_SF_POST_FATIGUE_SAFETY,
                                                    UF_SF_POST_STRENGTH_SAFETY,
                                                    UF_SF_POST_ELEMENT_ERROR    */
   UF_SF_POST_result_type_lay_t    lay,      /*<I> Layer to be set for result
                                                   UF_SF_POST_AT_MID
                                                    (Result at mid section
                                                     default, applicable for all kinds of elements)
                                                   UF_SF_POST_AT_TOP
                                                    (Result at top section
                                                     applicable only for shell elements)
                                                   UF_SF_POST_AT_BOT
                                                    (Result at bottom section
                                                     applicable only for shell elements)
                                                   UF_SF_POST_AT_MIN
                                                    (Minimum value
                                                     applicable only for shell elements)
                                                   UF_SF_POST_AT_MAX
                                                    (Maximum value
                                                     applicable only for shell elements)
                                                   UF_SF_POST_AT_SRP_C
                                                    (Stress Recovery Point at section-1
                                                     applicable only for truss elements)
                                                   UF_SF_POST_AT_SRP_D
                                                    (Stress Recovery Point at section-2
                                                     applicable only for truss elements)
                                                   UF_SF_POST_AT_SRP_E
                                                    (Stress Recovery Point at section-3
                                                     applicable only for truss elements)
                                                   UF_SF_POST_AT_SRP_F
                                                    (Stress Recovery Point at section-4
                                                     applicable only for truss elements)*/
   UF_SF_POST_result_comp_t        comp,    /*<I> Component to the result type to set
                                                    UF_SF_POST_COMP_SCALAR,
                                                    UF_SF_POST_COMP_X,
                                                    UF_SF_POST_COMP_Y,
                                                    UF_SF_POST_COMP_Z,
                                                    UF_SF_POST_COMP_MAG,
                                                    UF_SF_POST_COMP_XX,
                                                    UF_SF_POST_COMP_YY,
                                                    UF_SF_POST_COMP_ZZ,
                                                    UF_SF_POST_COMP_XY,
                                                    UF_SF_POST_COMP_YZ,
                                                    UF_SF_POST_COMP_ZX,
                                                    UF_SF_POST_COMP_DETERMINANT,
                                                    UF_SF_POST_COMP_MEAN,
                                                    UF_SF_POST_COMP_MAX_SHEAR,
                                                    UF_SF_POST_COMP_MIN_PRNCPL,
                                                    UF_SF_POST_COMP_MID_PRNCPL,
                                                    UF_SF_POST_COMP_MAX_PRNCPL,
                                                    UF_SF_POST_COMP_OCTAHEDRAL
                                                    UF_SF_POST_COMP_VON_MISES    */
   tag_t                          units_tag /*<I> To be obtained using function
                                                    UF_SF_get_unit_tag*/
);

/*****************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Initialise the structure containing deformation scaling parameters
*  from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 *****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_undef_disp_params
(
UF_SF_POST_undef_disp_t_p *undef_disp,          /*<OF>
                                                  Structure Containing undeformed display
                                                  parameters
                                                */
UF_SF_POST_elem_edge_style_t edge_style,        /*<I>
                                                  Display type of element edges
                                                  UF_SF_POST_ELEM_EDGE_NONE,
                                                  UF_SF_POST_ELEM_EDGE_FREE,
                                                  UF_SF_POST_ELEM_EDGE_EXTERNAL,
                                                  UF_SF_POST_ELEM_EDGE_WIRE
                                                */
UF_SF_POST_hue_colors_t edge_color,             /*<I>
                                                  Color for displaying the element edges
                                                  UF_SF_POST_BLACK,
                                                  UF_SF_POST_MAGENTA_RED,
                                                  UF_SF_POST_MAGENTA,
                                                  UF_SF_POST_BLUE_MAGENTA,
                                                  UF_SF_POST_BLUE,
                                                  UF_SF_POST_CYAN_BLUE,
                                                  UF_SF_POST_CYAN,
                                                  UF_SF_POST_GREEN_CYAN,
                                                  UF_SF_POST_GREEN,
                                                  UF_SF_POST_YELLOW_GREEN,
                                                  UF_SF_POST_YELLOW,
                                                  UF_SF_POST_ORANGE,
                                                  UF_SF_POST_RED,
                                                  UF_SF_POST_DARK_GRAY,
                                                  UF_SF_POST_LIGHT_GRAY,
                                                  UF_SF_POST_WHITE
                                                */
UF_SF_POST_elem_face_style_t face_style,        /*<I>
                                                  Type of element face display
                                                  UF_SF_POST_ELEM_FACE_NONE,
                                                  UF_SF_POST_ELEM_FACE_FILLED,
                                                  UF_SF_POST_ELEM_FACE_FILLED_TRANS,
                                                */
UF_SF_POST_hue_colors_t face_color              /*<I>
                                                  Color for the displaying the element faces
                                                  UF_SF_POST_BLACK,
                                                  UF_SF_POST_MAGENTA_RED,
                                                  UF_SF_POST_MAGENTA,
                                                  UF_SF_POST_BLUE_MAGENTA,
                                                  UF_SF_POST_BLUE,
                                                  UF_SF_POST_CYAN_BLUE,
                                                  UF_SF_POST_CYAN,
                                                  UF_SF_POST_GREEN_CYAN,
                                                  UF_SF_POST_GREEN,
                                                  UF_SF_POST_YELLOW_GREEN,
                                                  UF_SF_POST_YELLOW,
                                                  UF_SF_POST_ORANGE,
                                                  UF_SF_POST_RED,
                                                  UF_SF_POST_DARK_GRAY,
                                                  UF_SF_POST_LIGHT_GRAY,
                                                  UF_SF_POST_WHITE
                                                */
);



/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* post mark setting
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_post_mark_setting( UF_SF_POST_mark_arrow_style_t arrowtype,/*<I>
                                                                                           UF_SF_POST_MARK_ARROW_STYLE_LINE,
                                                                                           UF_SF_POST_MARK_ARROW_STYLE_UMBRELLA,
                                                                                           UF_SF_POST_MARK_ARROW_STYLE_CYLINDER*/
                                               int markcomps,
                                               UF_SF_POST_mark_tensor_style_t tensortype,/*<I>
                                                                                        UF_SF_POST_MARK_TENSOR_STYLE_ARROWS,
                                                                                        UF_SF_POST_MARK_TENSOR_STYLE_CROWSFEET,
                                                                                        UF_SF_POST_MARK_TENSOR_STYLE_BOX*/
                                               UF_SF_POST_mark_color_type_t markcolortype,/*<I>
                                                                                            UF_SF_POST_MARK_COLOR_RESULT,
                                                                                            UF_SF_POST_MARK_COLOR_ANNOTEXT,
                                                                                            UF_SF_POST_MARK_COLOR_SELECTED*/
                                               int markcolor,
                                               UF_SF_POST_mark_size_type_t marksizetype, /*<I>
                                                                                         UF_SF_POST_MARK_SIZE_RESULT,
                                                                                        UF_SF_POST_MARK_SIZE_CONSTANT*/
                                               UF_SF_POST_mark_size_valtype_t marksizevaluetype, /*<I>
                                                                                                UF_SF_POST_MARK_SIZE_MODELPERCENT,
                                                                                                UF_SF_POST_MARK_SIZE_VALUE*/
                                               double marksizevalue,
                                               UF_SF_POST_mark_loc_type_t arrowloc,  /*<I>
                                                                                        UF_SF_POST_MARK_AT_NODES,
                                                                                        UF_SF_POST_MARK_AT_ELEMCENTROID*/
                                               int hidemark,
                                               UF_SF_POST_mark_hide_valtype_t hidetype, /*<I>
                                                                                            UF_SF_POST_MARK_HIDE_RESULTPERCENT,
                                                                                            UF_SF_POST_MARK_HIDE_VALUE*/
                                               double hidevalue,
                                               UF_SF_POST_elem_value_t elementcriterion /*<I>
                                                                                        UF_SF_POST_ELEM_VALUE_CENTD,
                                                                                        UF_SF_POST_ELEM_VALUE_AVE,
                                                                                        UF_SF_POST_ELEM_VALUE_MIN,
                                                                                        UF_SF_POST_ELEM_VALUE_MAX*/);


/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* overlays a specific post view
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_overlay
(
const char* post_view_name,    /*<I> Deformed Result Parameter sturcture */
logical set_work,/*<I>*/
logical apply_on_work /*<I>*/
);



/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* remves a specific post view from overlay
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_remove_overlay
(
const char* post_view_name    /*<I> Deformed Result Parameter sturcture */
);


/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* updates the corresponding data related to deformed  and undeformed options
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_select_deformed_results
(
UF_SF_post_deform_result_t_p  def_result_params    /*<I> Deformed Result Parameter sturcture */
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* sets the result structure with the obtained data from the user
*
* Environment:  Internal and External
*
* History: Originally released in NX3
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_select_results(
      UF_SF_POST_result_parms_t_p result_params/* <I> Parameters for selecting results
                                              Use function UF_SF_initialise_result_parms
                                              to set this structure */
                                               );

/**************************************************************************
*   This function is retired. This function has been replaced with Journamation support
*
*  sets the "clip" structure with the obtained data from the user
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_set_clipping
(
UF_SF_post_clipping_data_t_p clip_params             /* <I> Structure containing clip
                                                            parameters
                                                     */
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*   feeds the data relating to deformed display parameters into NX specific structures
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_set_def_disp_params
(
 UF_SF_POST_def_disp_t_p def_disp       /*<I> Structure containing deformed display parameters
                                              obtained from UF_SF_POST_initialise_def_disp_params()
                                        */
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*   feeds the data relating to fringe parameters into NX specific structures
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_set_fringe_params
(
                   UF_SF_POST_fringe_t_p fringe_params  /* <I> Structure containing
                                                               fringe parameter variables
                                                        */
);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*   feeds the data relating to undeformed parameters into NX specific structures
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_set_undef_disp_params
(
 UF_SF_POST_undef_disp_t_p undef_disp   /*<I> Structure containing undeformed display parameters
                                              obtained from UF_SF_POST_initialise_undef_disp_params()
                                        */
 );

/***********************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*   Set up the ident parameters in the Ident structure
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
************************************************************************/
extern UFUNEXPORT int UF_SF_POST_write_ident_data
(
UF_SF_POST_ident_parms_t_p ident_params,    /*<I> Structure containing Identify parameters */
char*                      data_file        /*<I> File name to write Identify data */
);

/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* post mark setting
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_marker_display(UF_SF_POST_display_marker_t marker /*<I>
                                                                              Marker to display the minimum and/or
                                                                              maximum values
                                                                              UF_SF_POST_DISPLAY_MARKER_MIN_MAX,
                                                                              UF_SF_POST_DISPLAY_MARKER_MAXIMUM,
                                                                              UF_SF_POST_DISPLAY_MARKER_MINIMUM,
                                                                              UF_SF_POST_DISPLAY_MARKER_NONE
                                                                            */);

/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Get the currently set result param
*  Fill result_params structure with
*  current result settings. This function can be called anytime after post is initialized
*
* Environment:  Internal and External
*
* History: Originally released in NX4
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_result_params
(
    UF_SF_POST_result_parms_t_p result_params  /* <OF> Parameters for selecting results */
);


/******************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
 * This function returns the number of iterations for the input
 * result case and the iteration numbers themselves.
 * The calling function is responsible for freeing the memory associated with
 * the "iters" array.
 * Return :
 *  Return  code:
 *        = 0 No error
 *        = not 0 Error code
 * Environment:  External & internal.
 * See Also:
 * History:
 *  INPUT --
 *   lcase         - the case in which to get the result iters.
 *
 *  OUTPUT --
 *    num          - number of iterations .
 *    iters        - Pointer to an array of iteration numbers - Allocates Memory
 *********************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_result_iters(
    const int lcase ,  /* <I>
                        the case in which to get the result iters
                        */
    int *num ,  /* <O>
                 number of iterations
                */
    int **iters /* <OF,len:num>
                 Pointer to an array of iteration numbers -
                 Allocates Memory
                 This should be freed by UF_free.
                */
);
/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Get the currently set result for a given node/element id
* Environment:  Internal and External
*
* History: Originally released in NX4
 * Return :
 *  Return  code:
 *        = 0 No error
 *        = not 0 Error code
 * Environment:  External & internal.
 * See Also:
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_id_result
(
    const UF_SF_POST_object_type_t objtype,  /* <I>
                                            Which object type to look for
                                            (i.e. UF_SF_POST_NODE or UF_SF_POST_ELEM)
                                         */
    const int id, /* <I>
                    ID number of the object
                */
    float *value  /* <O>
                    result value for the object
                */
);
/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Get the currently set fringe param
*  Fill fringe_params structure with
*  current fringe settings. This function can be called anytime after post is initialized
*
* Environment:  Internal and External
*
* History: Originally released in NX4
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_fringe_params
(
    UF_SF_POST_fringe_t_p fringe_params  /* <OF> Parameters for selecting results */
);


/***************************************************************************
*   This function is retired. This function has been replaced with Journamation support
*
* Gets the data relating to deformed display parameters into NX specific structures
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_def_disp_params
(
 UF_SF_POST_def_disp_t_p def_disp       /*<I> Structure containing deformed display parameters */
);




/***************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
* Gets the data relating to undeformed parameters into NX specific structures
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_undef_disp_params
(
 UF_SF_POST_undef_disp_t_p undef_disp   /*<I/O> Structure containing undeformed display parameters */
 );



/**************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Gets the "clip" structure from the system data
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_clipping
(
UF_SF_post_clipping_data_t_p clip_params             /* <I/O> Structure containing clip
                                                            parameters
                                                     */
);


/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*  Gets the corresponding data related to deformed  and undeformed options
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_deformed_results
(
    UF_SF_post_deform_result_t_p  def_result_params    /*<I/O> Deformed Result Parameter sturcture */
);

/*************************************************************************
*   This function is retired.  This function has been replaced with Journamation support
*
*   set import result file name for import autotests
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX4
*****************************************************************************/
extern UFUNEXPORT int UF_SF_set_import_result_filename(char *result_filename /*<I>
                                                                             This function sets result filename
                                                                             into the solution
                                                                             */ );

/******************************************************************************
    Mating condition structures. A mating condition consists of one or
    more constraints. Each constraint consists of a pair of mated geometric
    entities, and information on the type of mating of those entities.

    The mating condition user function interface will be completely retired
    when the mating conditions functionality is replaced by assembly
    positioning constraints.  Assembly constraints can be automated using
    their Journamation interface.
******************************************************************************/

enum UF_ASSEM_load_status_e
{
    UF_ASSEM_ok,
    UF_ASSEM_suppressed,         /* The object referenced by the mating
                                    condition is suppressed. */
    UF_ASSEM_not_loaded,         /* The object referenced by the mating
                                    condition is not loaded. */
    UF_ASSEM_instance_suppressed /* One of the instances along the path
                                    to the referenced object has been marked
                                    as suppressed. */
};

typedef enum UF_ASSEM_load_status_e UF_ASSEM_load_status_t;

/* Possible values for the 'from_type' field

    <SP> 9-Sep-2002
    ASM2004: Add UF_ASSEM_parametric_face. NOTE: The order here must match
    that in occ.sch
*/

#define UF_ASSEM_planar_face        0
#define UF_ASSEM_cylindrical_face   1
#define UF_ASSEM_conical_face       2
#define UF_ASSEM_toroidal_face      3
#define UF_ASSEM_spherical_face     4
#define UF_ASSEM_axi_sym_face       5
#define UF_ASSEM_straight_edge      6
#define UF_ASSEM_datum_plane        7
#define UF_ASSEM_datum_axis         8
#define UF_ASSEM_csys               9
#define UF_ASSEM_component         10
#define UF_ASSEM_point             11
#define UF_ASSEM_line              12
#define UF_ASSEM_circle_edge       13
#define UF_ASSEM_circle            14
#define UF_ASSEM_spline            15
#define UF_ASSEM_port              16
#define UF_ASSEM_parametric_face   17

/* Possible values for the 'mate_type' field */

#define UF_ASSEM_mate       0
#define UF_ASSEM_align      1
#define UF_ASSEM_orient     2
#define UF_ASSEM_v16_mate   3
#define UF_ASSEM_v16_align  4
#define UF_ASSEM_angle      5
#define UF_ASSEM_distance   6
#define UF_ASSEM_parallel   7
#define UF_ASSEM_perpendicular    8
#define UF_ASSEM_center           9
#define UF_ASSEM_tangent          10

#define UF_ASSEM_planar_angle    0
#define UF_ASSEM_3d_angle        1

#define UF_ASSEM_center_1_to_1   0
#define UF_ASSEM_center_1_to_2   1
#define UF_ASSEM_center_2_to_1   2
#define UF_ASSEM_center_2_to_2   3

#define UF_ASSEM_has_no_help_point      0
#define UF_ASSEM_has_help_point_on_from 1
#define UF_ASSEM_has_help_point_on_to   2
#define UF_ASSEM_has_help_point_on_both 3

/* Structure to define the Degree of Freedom (DOF) */
struct UF_ASSEM_dof_s
{
    double  base_point[3];       /* where the DOF's should be originated */
    int     num_trans_dof;       /* number of translational dof's        */
    double  trans_dof[3][3];     /* An array of vectors that define the
                                    translational degrees of freedom.  These are
                                    unitized, with their origin at the
                                    base_point.  Note that the vectors beyond
                                    "num_trans_dof" in this array are undefined.
                                 */
    int     num_rot_dof;         /* number of rotational dof's           */
    double  rot_dof[3][3];       /* An array of vectors that define the
                                    rotational degrees of freedom.  These are
                                    unitized, with their origin at the
                                    base_point.  Note that the vectors beyond
                                    "num_rot_dof" in this array are undefined.
                                 */
};

typedef struct UF_ASSEM_dof_s UF_ASSEM_dof_t, *UF_ASSEM_dof_p_t;

/*
    Constraint:
*/

struct UF_ASSEM_constraint_s
{
    UF_ASSEM_load_status_t from_status;  /* Load status of the object mated
                                            from.  This can be UF_ASSEM_ok,
                                            UF_ASSEM_suppressed or
                                            UF_ASSEM_not_loaded.  */
    UF_ASSEM_load_status_t to_status;    /* Load status of the object mated
                                            to */
    byte    mate_type;       /* Type of this constraint, one of the values:
                                UF_ASSEM_mate - Planar faces are mated
                                                together - i.e. surface normals
                                                point in opposite directions.
                                                Cylindrical faces touch.
                                UF_ASSEM_align - Planar faces are aligned, i.e.
                                                 surface normals point in the
                                                 same direction.  Cylindrical
                                                 faces are aligned along their
                                                 central axes.
                                UF_ASSEM_orient - Objects are at an angle.  In
                                                  this case, the "offset" field
                                                  is used to specify an angle.
                                Since V16, should use the following mating type :
                                    UF_ASSEM_v16_mate
                                    UF_ASSEM_v16_align
                                    UF_ASSEM_angle
                                    UF_ASSEM_distance
                                    UF_ASSEM_parallel
                                    UF_ASSEM_perpendicular
                                    UF_ASSEM_center
                                    UF_ASSEM_tangent */
    byte    from_type;       /* Type of the object mated from, value can be
                                UF_ASSEM_planar_face, UF_ASSEM_cylindrical_face,
                                UF_ASSEM_conical_face, UF_ASSEM_toroidal_face,
                                UF_ASSEM_spherical_face, UF_ASSEM_axi_sym_face,
                                UF_ASSEM_straight_edge, UF_ASSEM_datum_plane,
                                UF_ASSEM_datum_axis, UF_ASSEM_csys or
                                UF_ASSEM_component

                                Since V16, the following object types added :
                                    UF_ASSEM_point
                                    UF_ASSEM_line
                                    UF_ASSEM_circle_edge
                                    UF_ASSEM_circle
                                    UF_ASSEM_spline
                             */
    byte    to_type;         /* Type of the object mated from this can have
                                the same values as from_type. */

    tag_t   from;            /* prototype tag of object mated from */
    tag_t   from_part_occ;   /* part occurrence of object mated from */
    tag_t   to;              /* prototype tag of object mated to */
    tag_t   to_part_occ;     /* part occurrence of object mated to */

    tag_t   offset;          /* expression tag to be used as the offset
                                between the two objects (or the angle if
                                they are oriented.)  This is expresion can
                                be evaluated using UF_MODL_ask_exp_tag_value.
                                A NULL_TAG value can be used to represent an
                                offset of 0. */

    const char *name;        /* The name of this constraint */

    logical user_name;       /* TRUE if the name was defined by the user.  If
                                FALSE, then the name was derived from the names
                                of the mated objects. */
    logical suppressed;      /* TRUE if the constraint is suppressed */
    logical inherited;       /* TRUE if the constraint is an original constraint
                                of an override mating condition */
    byte    sub_type;        /* subtype for angle or center constraints :

                                UF_ASSEM_planar_angle : angle is measured
                                anti-clockwise from TO to FROM about an angle
                                AXIS;

                                UF_ASSEM_3d_angle : angle is measured between
                                TO and FROM.

                                UF_ASSEM_center_1_to_1 : align one object into
                                the center of the other;

                                UF_ASSEM_center_1_to_2 : align one FROM object
                                with the center of two TO objects;

                                UF_ASSEM_center_2_to_1 : align the center of
                                two FROM objects with one TO object;

                                UF_ASSEM_center_2_to_2 : align the center of
                                two FROM objects with the center of two TO
                                objects */

    byte    second_from_type; /* Type of the second FROM object for center
                                 constraint : 2-1 and 2-2 */
    tag_t   second_from;      /* prototype tag of the second FROM object */
    tag_t   second_from_part_occ; /* part occurrence of the second FROM object */

    byte    second_to_type; /* Type of the second TO object for center
                               constraint : 1-2 and 2-2 OR type of the angle
                               axis object for the planar constraint */
    tag_t   second_to;      /* prototype tag of the second TO object or angle
                               axis */
    tag_t   second_to_part_occ; /* part occurrence of the second TO object or
                                   angle axis */

    byte    has_help_point; /* indicate on which geom a help point is defined :
                               UF_ASSEM_has_no_help_point : no help point is
                               defined

                               UF_ASSEM_has_help_point_on_from : help point is
                               defined for FROM object, and is stored in
                               help_points[0,1,2]

                               UF_ASSEM_has_help_point_on_to : help point is
                               defined for TO object, and is stored in
                               help_points[3,4,5]

                               UF_ASSEM_has_help_point_on_both : help points
                               are defined for both FROM object and TO object,
                               and are stored in help_points[0,1,2] and
                               help_points[3,4,5] */
    double  help_points[6]; /* help points defined in part occ space. used for
                               specifying where the tangent position should be
                               located. Currently, help points are needed for
                               tangent constraint and any spline-related
                               constraints. If no help points are defined, the
                               constraint solver will find the closest solution
                            */
} ;

typedef struct UF_ASSEM_constraint_s UF_ASSEM_constraint_t,
*UF_ASSEM_constraint_p_t;

#define UF_ASSEM_MAX_CONSTRAINTS 300

/*
    Mating condition
*/
struct UF_ASSEM_mating_condition_s
{

    tag_t                   mated_object;     /* The instance tag of the
                                                 component that is positioned
                                                 with this mating condition. */
    tag_t                   part_occurrence;  /* The tag of the part occurrence
                                                 in which the mating condition
                                                 exists. This field can vary if
                                                 override is TRUE */
    const char              *name;            /* The name of this mating
                                                 condition. */
    logical                 user_name;        /* TRUE if the name was
                                                 defined by the user. FALSE, if
                                                 the user did not specify a
                                                 name, and the name has instead
                                                 been derived from the names of
                                                 the components involved. */
    short                  init_check;        /* This is set by UF_ASSEM_init_mc
                                                 which should be used when
                                                 allocating mating conditions
                                              */
    UF_ASSEM_constraint_t  constraints[UF_ASSEM_MAX_CONSTRAINTS]; /*
                                                 The array of constraints
                                                 that define this mating
                                                 condition. */
    int                     num_constraints;  /* The number of constraints
                                                 in this mating condition. */
    logical                 suppressed;       /* TRUE if the mating condition
                                                 is suppressed.  A suppressed
                                                 mating conditions is not
                                                 updated in response to any
                                                 changes in the mated geometry.
                                              */
    logical                 override;         /* TRUE if this is an override
                                                 mating condition */
    logical                 implicit;         /* TRUE if the override mating
                                                 condition is implicit. This
                                                 field is meaningless unless
                                                 override is TRUE */
};

typedef struct UF_ASSEM_mating_condition_s UF_ASSEM_mating_condition_t,
*UF_ASSEM_mating_condition_p_t;


/* Values used in UF_ASSEM_solve_mc  */
enum UF_ASSEM_mc_status_e
{
    UF_ASSEM_mc_solved,
    UF_ASSEM_mc_not_solved,
    UF_ASSEM_mc_no_mating_specified,
    UF_ASSEM_mc_suppressed,           /* This could apply either to the mating
                                         condition or to all its constraints */
    UF_ASSEM_mc_data_unloaded,        /* This means that a to or from geometry
                                         used in the mating condition is not
                                         available, either because the part is
                                         not loaded or because a feature is
                                         suppressed */
    UF_ASSEM_mc_ignored               /* This means that the arrangement the
                                         condition was solved in is set to
                                         ignore constraints */
};


typedef enum UF_ASSEM_mc_status_e UF_ASSEM_mc_status_t;

/* Values used in UF_ASSEM_check_mc_structure */
enum UF_ASSEM_mc_structure_state_e
{
    UF_ASSEM_structure_ok,        /* The mating condition structure is valid.*/
    UF_ASSEM_no_component,        /* No component was specified */
    UF_ASSEM_invalid_entity_type, /* An invalid type of object was given in a
                                     constraint or an occurrence was given */
    UF_ASSEM_invalid_occ,         /* There was no occurrence of the given object
                                     in the given part occurrence. */
    UF_ASSEM_invalid_from_part,   /* The from_part_occ does not exist in the
                                     component to be mated. */
    UF_ASSEM_invalid_to_part,     /* The to_part_occ does exist in the
                                     component to be mated (i.e. trying to
                                     mate a component to itself. */
    UF_ASSEM_circular_mating,     /* The mating condition would cause a
                                     circular chain of dependencies within
                                     the mating conditions in this part.*/
    UF_ASSEM_promoted_object,     /* An attempt was made to mate a component
                                     using promoted geometry. This is not
                                     allowed. */
    UF_ASSEM_invalid_offset,      /* Implies that the expression stored in a
                                     mating conditions constraint is invalid.
                                     For example, if the expression is in a
                                     different part than the mating condition
                                     itself. */
    UF_ASSEM_invalid_from_ipath,  /* Indicates a problem in the instance path
                                     generated from the from_part_occ field
                                     specified in the mating condition data
                                     structure. */
    UF_ASSEM_invalid_to_ipath,    /* Indicates a problem in the instance path
                                     generated from the to_part_occ field
                                     specified in the mating condition data
                                     structure. */
    UF_ASSEM_invalid_override,    /* Indicates one or more override instances
                                     in a constraint that does not belong to an
                                     override mating condition. */
    UF_ASSEM_not_initialized      /* Indicates the structure was not initialized
                                     using UF_ASSEM_init_mc. */
};

typedef enum UF_ASSEM_mc_structure_state_e UF_ASSEM_mc_structure_state_t;


/******************************************************************************
    Mating conditions prototypes

    Note that the format of the transform returned by UF_ASSEM_solve_mc is the
    same as that returned by UF_ASSEM_ask_component_data.

    Mating conditions have been replaced by a new Assembly Constraint mechanism.
    for details please investigate ja_xxx_xxx

 ******************************************************************************/

/*************************************************************************
Returns the mating condition defined for a given component.


Environment: Internal  and  External

See Also:
History:
 ************************************************************************/
extern UFUNEXPORT int UF_ASSEM_ask_mc_data_of_compnt(
tag_t component ,/* <I>
                 Instance tag of component
                 */
logical * mated ,/* <O>
                 Set to true if the component is mated, and false
                 otherwise.
                 */
UF_ASSEM_mating_condition_p_t mc_data  /* <O>
                                       If mated is true, this structure is
                                       filled in with the data that defines the
                                       mating condition.
                                       */
);

/*************************************************************************
Solves a mating condition and returns information about it.

Environment: Internal  and  External

See Also:

History:
 ************************************************************************/
extern UFUNEXPORT int UF_ASSEM_solve_mc(
UF_ASSEM_mating_condition_p_t mc_data ,/* <I>
                                       The definition of the mating condition.
                                       */
UF_ASSEM_mc_status_t * status ,/* <O>
                               The result of solving. The possible values are:
                                 UF_ASSEM_mc_solved  - a solution was found.
                                 UF_ASSEM_mc_not_solved - no solution could be
                                                          found.
                                 UF_ASSEM_mc_no_mating_specified - no
                                                    constraints were specified.
                                 UF_ASSEM_mc_suppressed - the condition or all
                                               its constraints were suppressed.
                                 UF_ASSEM_mc_data_unloaded - a part referenced
                                                  in the condition is unloaded.
                               */
UF_ASSEM_dof_p_t dof ,/* <O>
                      If a solution was found, this structure is filled
                      in with the degrees of freedom still remaining.
                      */
double transform[4][4]  /* <O>
                        If a solution was found, this array is filled in
                        with the transform that would be applied to
                        the mated component in order to satisfy the
                        mating conditions. This is the same format as
                        the transform used in UF_ASSEM_ask_component_data.
                        */
);

/*************************************************************************
Initializes a mating condition data structure if one is being created
from scratch.

Environment: Internal  and  External

See Also:

History:
 ************************************************************************/
extern UFUNEXPORT int UF_ASSEM_init_mc(
UF_ASSEM_mating_condition_p_t mc_data   /* <O>
                                        A mating condition structure
                                        */
);

/*************************************************************************
Checks that the data structures of a mating condition are valid.


Environment: Internal  and  External

See Also:

History:
 ************************************************************************/
extern UFUNEXPORT int UF_ASSEM_check_mc_structure (
UF_ASSEM_mating_condition_p_t mc_data ,/* <I>
                                       The definition of the mating condition.
                                       */
UF_ASSEM_mc_structure_state_t * struct_status ,/* <O>
                             The status of the mating condition structure.  See
                             the definition of UF_ASSEM_mc_structure_stat_t.
                                               */
tag_t * invalid_tag  /* <O>
                     If status is not UF_ASSEM_structure_ok, this is
                     set to the tag that caused the error.
                     */
);

/*************************************************************************
Applies a mating condition to a component.

Environment: Internal  and  External

See Also:

History:
 ************************************************************************/
extern UFUNEXPORT int UF_ASSEM_apply_mc_data (
UF_ASSEM_mating_condition_p_t mc_data ,/* <I>
                                       The definition of the mating condition.
                                       */
UF_ASSEM_mc_structure_state_t * struct_status ,/* <O>
                             The status of the mating condition structure.  See
                             the definition of UF_ASSEM_mc_structure_stat_t.
                                               */
UF_ASSEM_mc_status_t * status  /* <O>
                               The result of solving the mating condition. (See
                               above.) NOTE: If struct_status ==
                               UF_ASSEM_structure_ok and status ==
                               UF_ASSEM_mc_solved, then the mating
                               condition is applied to the component, and the
                               component is repositioned. Otherwise, the
                               component is not moved, and its mating
                               condition data is not altered.
                               */
);

/*****************************************************************************
This routine takes the tag of an instance or a part occurrence and
deletes its mating condition (including any associated constraint
data). If there is no mating condition on the component, removed is
returned as false, but no error is given.  If a condition is deleted,  then
removed is returned as true.

Note: A call to UF_MODL_update is necessary to update the mating conditions status.

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUNEXPORT int UF_ASSEM_delete_mc(
tag_t component ,/* <I>
                 Object identifier of component whose mating
                 condition is to be removed.
                 */
logical * removed  /* <O>
                   Removal flag:
                    TRUE = Mating condition removed
                    FALSE = No mating condition to remove
                   */
);

/*****************************************************************************
Returns the unique set of part occurrences which are mated to a
component. The mating conditions can be removed from the part
occurrences so that when the component is removed from the
assembly, the interactive user does not receive message boxes for each
of the mating conditions (update conflict notification).  Hence this
routine considers two components mated even if the mating condition is
suppressed.

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUNEXPORT int UF_ASSEM_ask_comps_mated_to_me(
tag_t component ,/* <I>
                 Tag of part occurrence or instance which has
                 another component mated to it.
                 */
tag_t ** mated_component ,/* <OF,len:n_mated_components>
                          Address of an array which is filled with part
                          occurrences which are mated to the component.
                          Duplicates are removed. Use UF_free to deallocate
                          memory
                          */
int * n_mated_components  /* <O>
                          Number of part occurrences returned in
                          mated_components.
                          */
);

/*****************************************************************************
This routine will create a mating condition as suppressed.  The motion
of the component will be deferred until the mating condition is unsuppressed.

Environment : Internal  and  External

See Also:

History :
***************************************************************************/
extern UFUNEXPORT int UF_ASSEM_create_suppressed_mc (
UF_ASSEM_mating_condition_p_t  mc_data, /* <I>
                                        The definition of the mating condition.
                                        */
UF_ASSEM_mc_structure_state_t * struct_status /* <O>
                             The status of the mating condition structure.  See
                             the definition of UF_ASSEM_mc_structure_stat_t.
                                               */
);


/*****************************************************************************
This routine will suppress or unsuppress a mating condition

Environment : Internal  and  External

See Also:

History :
***************************************************************************/
extern UFUNEXPORT int UF_ASSEM_suppress_mc(
       tag_t component,  /* <I>
                         Tag of part occurrence or instance which has
                         a mating condition
                         */
       logical suppress  /* <I>
                         True  - suppress the mating condition
                         False - unsuppress the mating condition
                         */
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
char * cr3 ,/* <O>
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
/*******************************************************************************-
 *
 * This routine try to load VKI meshing library.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Released in v18.0
 *******************************************************************************/
extern UFUNEXPORT int  UF_SF_load_vki_mesh_lib(void);

/*******************************************************************************-
 *
 * This routine try to load VDM library.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Released in v18.0
 *******************************************************************************/
extern UFUNEXPORT int  UF_SF_load_vdm_lib(void);

/*******************************************************************************-
 *
 * This routine try to load Hyper Opt library.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Released in v18.0
 *******************************************************************************/
extern UFUNEXPORT int  UF_SF_load_hypopt_lib(void);

/*******************************************************************************-
 *
 * This routine try to load ADAMS library.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Released in v18.0
 *******************************************************************************/
extern UFUNEXPORT int  UF_SF_load_adams_lib(void);


#define UF_RLIST_err_ports_not_found           (1945047)
#define UF_RLIST_err_comps_not_found           (1945054)



/* [HELPSTRING][HELPCONTEXT] */

/*
 *This is a common enum that comprises of values to be used for various features.
 *Each feature data structure will enumerate valid values that can be used for that feature parameter.
 */
enum UF_NXSM_FEATURE_PROPERTY_CONSTANTS
{
        IG_NULL_CONSTANT  = 0,
        IG_LEFT  = 1,
        IG_RIGHT = 2,
        IG_SYMMETRIC     = 3,
        IG_INSIDE        = 4,
        IG_OUTSIDE       = 5,
        IG_BOTH  = 6,
        IG_NORMAL_SIDEDUMMY       = 7,
        IG_REVERSE_NORMAL_SIDEDUMMY        = 8,
        IG_EXTEND        = 9,
        IG_NOEXTEND      = 10,
        IG_THKINPROFILEPLANE     = 11,
        IG_THK_NORMAL_TO_PROFILE_PLANE       = 12,
        IG_FINITE        = 13,
        IG_TONEXT        = 14,
        IG_TO_END_OF_EDGE   = 14,
        IG_FROM_TO        = 15,
        IG_THROUGH_ALL    = 16,
        IG_THREE_HUNDRED_AND_SIXTY  = 17,
        IG_PARALLEL_DUMMY = 18,
        IG_ANGULAR_DUMMY  = 19,
        IG_NORMAL        = 20,
        IG_THROUGH_AXIS   = 21,
        IG_SINGLE_EDGE    = 22,
        IG_MULTIPLE_EDGES = 23,
        IG_EDGES_BY_LOOP   = 24,
        IG_EDGES_BY_VERTEX = 25,
        IG_ALL   = 26,
        IG_CONCAVE       = 27,
        IG_CONVEX        = 28,
        IG_START = 29,
        IG_END   = 30,
        IG_LINEAR        = 31,
        IG_RADIAL        = 32,
        IG_REGULAR_HOLE   = 33,
        IG_COUNTER_BORE_HOLE       = 34,
        IG_COUNTER_SINK_HOLE       = 35,
        IG_COUNTER_DRILL_HOLE      = 36,
        IG_TAPPED_HOLE    = 37,
        IG_TAPERED_HOLE   = 38,
        IG_CONST_RADIUS_ROUND      = 39,
        IG_VAR_RADIUS_ROUND        = 40,
        IG_CHAMFER_45DEG_SETBACK   = 41,
        IG_CHAMFER_ANGLE_SETBACK   = 42,
        IG_CHAMFER2_SETBACKS      = 43,
        IG_NONE  = 44,
        IG_TAPER_BY_ANGLE  = 45,
        IG_TAPER_BY_RATIO  = 46,
        IG_CLOSED        = 47,
        IG_PROFILE_BASED_CROSSSECTION      = 48,
        IG_EDGE_BASED_CROSSSECTION = 49,
        IG_TANGENT       = 50,
        IG_RECTANGULAR_BEND_RELIEF = 51,
        IG_FILLET_BEND_RELIEF      = 52,
        IG_RIP_BEND_RELIEF = 53,
        IG_BEND_ONLY_CORNER_RELIEF  = 54,
        IG_BEND_AND_FACE_CORNER_RELIEF       = 55,
        IG_RIP_CORNER_RELIEF       = 56,
        IG_NFTYPE        = 57,
        IG_EQUATION_TYPE  = 58,
        IG_PATTERN_MIRROR = 59,
        IG_PATTERN_RECTANGULAR    = 60,
        IG_PATTERN_CIRCULAR       = 61,
        IG_PATTERN_USER_DEFINED    = 62,
        IG_FROM_REFERENCE_END      = 64,
        IG_FROM_NONREFERENCE_END   = 65,
        IG_RND_ROLL_ACROSS_TANGENT_EDGES_ON   = 66,
        IG_RND_ROLL_ACROSS_TANGENT_EDGES_OFF  = 67,
        IG_RND_CAP_ACROSS_SHARP_EDGES        = 68,
        IG_RND_ROLL_ACROSS_SHARP_EDGES       = 69,
        IG_RND_ROLL_ALONG_BLEND_EDGES_ON      = 70,
        IG_RND_ROLL_ALONG_BLEND_EDGES_OFF     = 71,
        IG_TO_KEY_POINT    = 72,
        IG_FLATTEN       = 73,
        IG_AS_CONSTRUCTION        = 74,
        IG_OFFSET        = 75,
        IG_MITRE_PARALLEL_TO_THICKNESS      = 76,
        IG_MITRE_NORMAL_TO_THICKNESS        = 77,
        IG_MITRE_BY_DIST   = 78,
        IG_MITRE_BY_ANGLE  = 79,
        IG_MITRE_REGULAR_CUT       = 80,
        IG_MITRE_MANUFACTURING_CUT = 81,
        IG_PROJECT_OPTION_PROJECT  = 82,
        IG_PROJECT_OPTION_WRAP     = 83,
        IG_LIP   = 84,
        IG_GROOVE        = 85,
        IG_PARTING_FROM_PLANE      = 86,
        IG_PARTING_FROM_SURFACE    = 87,
        IG_PARTING_FROM_EDGE       = 88,
        IG_PARTING_FROM_CURVE      = 89,
        IG_SPLIT_DRAFT    = 90,
        IG_SPLIT_ANGLE1_RIGHT      = 91,
        IG_SPLIT_ANGLE1_LEFT       = 92,
        IG_LOUVERFORMEDENDTYPE   = 93,
        IG_LOUVERLANCEDENDTYPE   = 94,
        IG_LOUVERROUND   = 95,
        IG_LOUVERROUNDNONE       = 96,
        IG_INSIDE_DIMENSION       = 97,
        IG_OUTSIDE_DIMENSION      = 98,
        IG_FULL  = 99,
        IG_BEND  = 100,
        IG_ADD_ROUND      = 101,
        IG_NO_ROUND       = 102,
        IG_CLOSE_FACES    = 103,
        IG_OVERLAP_FACES  = 104,
        IG_TREATMENT_OFF  = 105,
        IG_TREATMENT_INTERSECT    = 106,
        IG_TREATMENT_CIRCLE_CUTOUT = 107,
        IG_STEP_DRAFT     = 108,
        IG_SHOW_BOUNDARIES        = 109,
        IG_REMOVE_BOUNDARIES      = 110,
        IG_CORNER_ROUND   = 111,
        IG_NO_CORNER_ROUND = 112,
        IG_NATURAL       = 113,
        IG_PERIODIC      = 114,
        IG_ROUND_ALL_VERTEX_SETBACK = 115,
        IG_ROUND_SINGLE_VERTEX_SETBACK      = 116,
        IG_ROUND_VERTEX_EDGE_SETBACK        = 117,
        IG_ROUND_SETBACK_IS_ABSOLUTE        = 118,
        IG_ROUND_SETBACK_IS_RELATIVE        = 119,
        IG_CIRCULAR      = 120,
        IG_USHAPED       = 121,
        IG_VSHAPED       = 122,
        IG_PUNCHED_END    = 123,
        IG_LANCED_END     = 124,
        IG_FORMED_END     = 125,
        IG_SWEEP_ALIGN_PARALLEL    = 126,
        IG_SWEEP_ALIGN_NORMAL      = 127,
        IG_ROUND_START_VERTEX_EDGE_SETBACK   = 128,
        IG_ROUND_END_VERTEX_EDGE_SETBACK     = 129,
        IG_SUBTRACT      = 130,
        IG_UNITE = 131,
        IG_INTERSECT     = 132,
        IG_CONTINUOUS    = 133,
        IG_FLANGE_FULLEDGE        = 134,
        IG_FLANGE_CENTER_OF_EDGE    = 135,
        IG_FLANGE_START_ON_END_EDGE  = 136,
        IG_FLANGE_END_ON_END_EDGE    = 137,
        IG_FLANGE_START_FROM_END_EDGE        = 138,
        IG_FLANGE_END_FROM_END_EDGE  = 139,
        IG_FLANGE_FROM_BOTH_ENDS_OF_EDGE      = 140,
        IG_FLANGE_OFFSET  = 141,
        IG_CHAINED_CORNER_RELIEF   = 142,
        IG_TANGENT_INTERIOR       = 143,
        IG_PARALLEL_TO_PLANE       = 144,
        IG_VBOTTOM_DIM_TO_FLAT      = 145,
        IG_VBOTTOM_DIM_TO_V = 146,
        IG_TAPER_DIM_AT_TOP = 147,
        IG_TAPER_DIM_AT_BOTTOM      = 148,
        IG_COUNTER_BORE_PROFILE_IS_AT_TOP     = 149,
        IG_COUNTER_BORE_PROFILE_IS_AT_BOTTOM  = 150,
        IG_TAPER_BY_RL_RATIO        = 151,
        IG_RNDMITERAT_CORNER      = 152,
        IG_RND_ROLL_AROUND_CORNER   = 153,
        IG_RND_PRESERVE_TOPOLOGYON = 154,
        IG_RND_PRESERVE_TOPOLOGY_OFF        = 155,
        IG_STEP_DRAFT_PERPENDICULAR        = 156,
        IG_EXTEND_BEND_RELIEF      = 157,
        IG_EQUAL_OFFSET   = 158,
        IG_UNEQUAL_OFFSET = 159,
        IG_THICKNESS     = 160,
        IG_FACES_TOUCHING_CURVES_ONLY       = 161,
        IG_CURVESET_SEPERATOR     = 162,
        IG_SIDE_INFOSET_SEPERATOR  = 163,
        IG_REGULAR_THREAD = 164,
        IG_STRAIGHT_PIPETHREAD    = 165,
        IG_TAPERED_PIPETHREAD     = 166,
        IG_REMOVE_INTERNAL_BOUNDARIES      = 167,
        IG_REMOVE_EXTERNAL_BOUNDARIES      = 168,
        IG_DELETE_FACEHEAL        = 169,
        IG_ENDCAPS       = 170,
        IG_CURVATURE_CONTINUOUS   = 171,
        IG_NONSYMMETRIC  = 172,
        IG_TREATMENT_DRAFT        = 173,
        IG_TREATMENT_CROWN        = 174,
        IG_CLOSE_CORNER_NONE       = 175,
        IG_CLOSE_CORNER_OPEN       = 176,
        IG_CLOSE_CORNER_CLOSED     = 177,
        IG_CLOSE_CORNER_CIRCLE_CUTOUT       = 178,
        IG_PATTERN_ALONG_CURVE     = 179,
        IG_PATTERN_MOUNTING_BOSS   = 180,
        IG_SM_CLEARANCE_CUTOUT     = 181,
        IG_SM_MIDPLANE_CUTOUT      = 182,
        IG_TREATMENT_U_CUTOUT      = 220,
        IG_TREATMENT_V_CUTOUT      = 221,
        IG_TREATMENT_RECTANGULAR_CUTOUT = 222
    
};
typedef enum UF_NXSM_FEATURE_PROPERTY_CONSTANTS
             UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t;

/*
 *NXSM - TAB FEATURE
 */

/* Data structure for Base Tab */
struct UF_NXSM_tab_data_s
{

    tag_t sketch_obj;                   /* sketch tag or section tag of sketch.
                                           You can either pass sketch tag or create a 
                                           section for sketch, pass the tag of section.
                                         * NULL_TAG (default) */

    char sweep_dist[UF_MAX_EXP_LENGTH]; /* Sweep distance */
    
    logical sweep_direction;            /* Sweep direction flag - 
                                           If set to true - the tab is swept in the direction of normal 
                                           to datum plane on which sketch has drawn.
                                           If set to false - sweeping in opposite direction to the normal direction of datum plane */

    logical is_global_thickness;        /* Flag for global thickness 
                                           0 - Thickness value applies to only a feature
                                           1 - Thickness applies to whole part(default) */ 

};
typedef struct UF_NXSM_tab_data_s UF_NXSM_tab_data_t, *UF_NXSM_tab_data_p_t;

/*
 *NXSM - SECONDARY TAB FEATURE
 */

/* Data structure for Secondary Tab */
struct UF_NXSM_sec_tab_data_s
{

    tag_t sketch_profile;                         /* sketch tag or section tag of sketch.
                                                    You can either pass sketch tag or create a 
                                                    section for sketch, pass the tag of section.
                                                  * NULL_TAG (default) */

    tag_t placement_face;                         /* Placement face of the base tab for creating secondary tab */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t material_side;
                                                  /* Sketch side on which material will be added
                                                   * IG_LEFT - default
                                                   * IG_RIGHT  */                                                           

};
typedef struct UF_NXSM_sec_tab_data_s UF_NXSM_sec_tab_data_t, *UF_NXSM_sec_tab_data_p_t;


/* Data structure for bend option */
struct UF_NXSM_bend_option_s
{
    char bend_radius[UF_MAX_EXP_LENGTH];   /* Bend radius */

    logical is_bend_radius_global;         /* flag to use default value. 
                                              TRUE  - 0.1 in /3.0 mm (default)
                                              FALSE - To use user defined bend radius make it FALSE  */

    logical bend_relief;                   /* Bend relief require or not 
                                              TRUE - bend relief require
                                              FALSE - bend relief not require (default) */

    logical extend_bend_relief;            /* flag to to extend bend relief 
                                              TRUE - Extend bend relief to source body
                                              FALSE - default */ 

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t bend_relief_type; 
                                            /* It provides clearance between the bend and the Source Face 
                                             * IG_RECTANGULAR_BEND_RELIEF - for square shape relief(default), 
                                             * IG_FILLET_BEND_RELIEF - for round shape relief 
                                             * IG_RIP_BEND_RELIEF - bend relief not require*/

    char bend_relief_depth[UF_MAX_EXP_LENGTH]; /* Depth of bend relief */

    logical bend_relief_depth_global;         /* flag to use global value. 
                                               * TRUE - 0.1 in /3.0 mm (default) 
                                               * FALSE - To use user defined bend relief width make it FALSE */

    char bend_relief_width[UF_MAX_EXP_LENGTH];  /* Width of bend relief */

    logical bend_relief_width_global;         /* flag to use global value. 
                                               * TRUE - 0.1 in /3.0 mm (default) 
                                               * FALSE - To use user defined bend relief width make it FALSE */
    
    logical corner_relief;                    /* Corner relief require or not 
                                               * TRUE - bend relief require
                                               * FALSE - bend relief not require (default) */
    
   UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t corner_relief_type; 
                                              /* Corner relief is used to avoid deformation and tear of 
                                                 material during bending process.
                                               * IG_RIP_CORNER_RELIEF  - default,                                                  
                                               * IG_BEND_ONLY_CORNER_RELIEF - relief apply to bend only ,
                                               * IG_BEND_AND_FACE_CORNER_RELIEF - relief apply to bend and face,
                                               * IG_CHAINED_CORNER_RELIEF  - relief apply to bend and chain of faces */  

   char neutral_factor[UF_MAX_EXP_LENGTH];    /* default value - 0.33333 */

   logical neutral_factor_global;             /* flag to use global value. 
                                               * TRUE - Use default value(default) 
                                               * FALSE - To use user defined neutral factor make it FALSE */

};
typedef struct UF_NXSM_bend_option_s UF_NXSM_bend_option_t, *UF_NXSM_bend_option_p_t;


/*
 *NXSM - BEND FEATURE
 */

/* Data structure for bend feature */
struct UF_NXSM_bend_data_s
{

    tag_t sketch_profile;                         /* sketch tag or section tag of sketch.
                                                     You can either pass sketch tag or create a 
                                                     section for sketch, pass the tag of section.
                                                   * NULL_TAG (default) */

    char bend_angle[UF_MAX_EXP_LENGTH];           /* Bend angle in degrees*/

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t bend_dir;
                                                  /* Bend direction
                                                   * IG_NORMAL_SIDEDUMMY - in the direction of normal to selected 
                                                                            face (default)
                                                   * IG_REVERSE_NORMAL_SIDEDUMMY - opposite to normal direction of
                                                                                  selected face 
                                                   */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t fixed_side;
                                                  /* part of the selected face to be fixed to create bend 
                                                   * IG_LEFT - (defualt),
                                                   * IG_RIGHT 
                                                   */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t material_side;
                                                  /* Indicates the bend position
                                                   * IG_RIGHT - bend start position is at sketch profile (default),
                                                   * IG_SYMMETRIC - bend start and end positions are at equal 
                                                                   distance from the sketch_profile
                                                   * IG_LEFT - bend end position is at sketch_profile
                                                   * IG_INSIDE - Moved part of face lie just inside the sketch_profile 
                                                   * IG_OUTSIDE -Moved part of face lie just outside the sketch_profile
                                                   */ 

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t extend_option;
                                                  /* Extend the bend upto the opposite edges along sketch profile
                                                   * IG_EXTEND - extend upto opposite edges ( default ) 
                                                   */

    UF_NXSM_bend_option_t  bend_options;          /* Bend option */
    
};
typedef struct UF_NXSM_bend_data_s UF_NXSM_bend_data_t, *UF_NXSM_bend_data_p_t;



/*
 *NXSM - CLOSED CORNER FEATURE
 */

/* Main Data structure for closed corner */
struct UF_NXSM_closed_corner_data_s
{
    tag_t bend_faces[2];    /*for creating closed corner first time send in two valid bend faces from here.
                              subsequently, send additional valid bend faces while editing so as to add more 
                              corners to be closed.  */

    int n_edges;            /* Actual number of edges in the array "parent_edges".*/

    tag_t* parent_edges;   /* <OF,len:n_edges> array of parent edges
                           NULL - at the time of creating closed corner
                           During "edit", the "ask_feature" method will return the current array of parent edges
                           User can remove any edges from that array if he so desires.
                           Update the "n_edges" variable accordingly to reflect actual number of edges in this array. */
    
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t treatment_type;
                                        /* Type of closed corner treatment - 
                                           IG_TREATMENT_OFF - default
                                           IG_TREATMENT_INTERSECT - intersection at the corner
                                           IG_TREATMENT_CIRCLE_CUTOUT - circular cutout at the corner
                                         */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t closure_type; 
                                        /* Type of closure -
                                           IG_TREATMENT_OFF - default
                                           IG_CLOSE_FACES - close the corner faces
                                           IG_OVERLAP_FACES - overlap the corner faces */
                                        
    const char* treatment_dia;          /* diameter value for the "IG_TREATMENT_CIRCLE_CUTOUT" 
                                           treatment for closed corner */

    const char* overlap_ratio;          /* ratio of overlap for the overlapping faces - 
                                           valid values range from 0.0 to 1.0    */
                                   
    const char* corner_gap;             /* gap in between the closing faces -
                                           valid values range from 0.0 upto the material 
                                           thickness of the body. */
                                   
};
typedef struct UF_NXSM_closed_corner_data_s UF_NXSM_closed_corner_data_t, *UF_NXSM_closed_corner_data_p_t;

/*
 *NXSM - FLANGE FEATURE
 */

/*Enum for flange width option*/
typedef enum
{
    OPTION_NOT_SET = -101,
    CUSTOM_WIDTH_TYPE = -1, /* ==> user has edited the flange sketch manually so it is no longer a pre-configured type */
    FULL_WIDTH_TYPE = 0,
    CENTERED_TYPE,
    AT_END_TYPE,
    FROM_BOTH_ENDS_TYPE,
    FROM_END_TYPE
} UF_NXSM_FLANGE_WIDTH_OPTION_e_t;

/*Data structure for flange sketch*/
struct UF_NXSM_flange_sketch_data_s
{
    UF_NXSM_FLANGE_WIDTH_OPTION_e_t width_option;   /* choose appropriate width_option from UF_NXSM_FLANGE_WIDTH_OPTION_e_t*/
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t dim_option;   /* Indicates whether to measure the dimension from the inside edge or outside edge of the flange.
                                                            valid values -
                                                            IG_OUTSIDE_DIMENSION - default
                                                            IG_INSIDE_DIMENSION
                                                          */
    const char* length;   /* length of the flange*/
    const char* width;    /* width of the flange*/
    double snap_point[3];   /* for AT_END_TYPE / FROM_END_TYPE width option.
                               User can use "UF_MODL_ask_edge_verts" routine
                               to get the end points of the parent edge of flange & send the desired point co-ords to the snap_point*/
    const char* dist_from_end;    /* distance from the end at which the flange would start - FROM_END_TYPE width option.*/
    const char* dist_from_left_end;   /* distance from left end of the edge - FROM_BOTH_ENDS_TYPE width option.*/
    const char* dist_from_right_end;  /* distance from the right end of the edge - FROM_BOTH_ENDS_TYPE width option.*/
    UF_NXSM_FLANGE_WIDTH_OPTION_e_t prev_width_option;      /*width_option value with which the feature was created earlier.
                                                             *"ask_feature" method populates this parameter.
                                                             */
};
typedef struct UF_NXSM_flange_sketch_data_s UF_NXSM_flange_sketch_data_t, *UF_NXSM_flange_sketch_data_p_t;

/* Main Data structure for flange */
struct UF_NXSM_flange_data_s
{
    tag_t parent_edge;    /* tag of the edge on which flange is to be placed*/
    tag_t sketch_tag;     /* sketch of the flange - send a NULL_TAG for create.
                             flange will create its sketch internally based on various calculations & input sketch data.
                             User can query the feature & get the sketch tag for further modifications to the sketch if so desired.
                          */
    const char* angle;    /* flange angle
                             should have value between 0 to 180 degrees.
                           */
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t material_side;    /* Side on which material will be added with respect to the mould line
                                                                valid values - 
                                                                IG_LEFT - default
                                                                IG_RIGHT
                                                                IG_EXTEND
                                                              */
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t br_type;    /* bend relief type
                                                          valid values -
                                                          IG_RECTANGULAR_BEND_RELIEF - default
                                                          IG_FILLET_BEND_RELIEF     
                                                          IG_BEND_ONLY_CORNER_RELIEF  
                                                          IG_BEND_AND_FACE_CORNER_RELIEF      
                                                          IG_RIP_CORNER_RELIEF     
                                                        */
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t cr_type;    /* corner relief type 
                                                          valid values - 
                                                          IG_RIP_CORNER_RELIEF - default
                                                          IG_BEND_ONLY_CORNER_RELIEF  
                                                          IG_BEND_AND_FACE_CORNER_RELIEF      
                                                        */
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t off_type;       /* offset type.
                                                              valid values -
                                                              IG_NONE - default
                                                              IG_LEFT
                                                              IG_RIGHT
                                                            */
    const char* bend_rad;    /* bend radius for the flange */
    logical use_global_radius_value;   /* false - default
                                          true - if user wants to link his flange to global bend radius value
                                        */
    const char* br_width;   /* bend relief width*/
    logical use_global_br_width_value;   /* false - default
                                            true - if user wants to link his flange to global bend radius value
                                          */
    const char* br_length;  /* bend relief length*/
    logical use_global_br_length_value;   /* false - default
                                             true - if user wants to link his flange to global bend radius value
                                           */
    const char* off_val;    /*offset value*/
    const char* n_factor;       /* neutral factor value */
    logical use_global_nfactor_value;   /* false - default
                                           true - if user wants to link his flange to global bend radius value
                                         */
    logical extend_bend_relief;     /* false - default
                                       true - If user wants bend relief to be extended
                                     */
};
typedef struct UF_NXSM_flange_data_s UF_NXSM_flange_data_t, *UF_NXSM_flange_data_p_t;

/*
 *NXSM - UNBEND FEATURE
 */

/* Main Data structure for Unbend */
struct UF_NXSM_unbend_data_s
{
    tag_t ref_entity;       /* A non-thickness face/edge that will be the reference for unbend operation.*/

    tag_t face_collector;   /* SC_collector object used to add/remove bend faces to be unbent*/
    
    int   nbend;            /* Number of bend faces unbent*/
    
    tag_t *bend_list;       /* <OF,len:nbend> array of bend faces unbent*/
};
typedef struct UF_NXSM_unbend_data_s UF_NXSM_unbend_data_t, *UF_NXSM_unbend_data_p_t;


/*
 *NXSM - REBEND FEATURE
 */

/* Main Data structure for Rebend */
struct UF_NXSM_rebend_data_s
{
    tag_t face_collector;   /* SC_collector object used to add/remove bend faces to be unbent*/

    int   nbend;            /* Number of bend faces unbent*/

    tag_t *unbend_list;     /* <OF,len:nbend> array of bend faces unbent*/
};
typedef struct UF_NXSM_rebend_data_s UF_NXSM_rebend_data_t, *UF_NXSM_rebend_data_p_t;


/******************************************************************************
Data structure for Mitre cut

Mitre cut is essentially an end treatment to the contour flange feature, which shall 
prevent merging/interference with the existing or newly placed features in sheet metal.  
Sometimes without mitreing we would end up with merging the faces of the adjoining 
contour flange features.
The mitre cut is optional, and can be done in two ways.  Either ?Normal to thickness face?
or ?Normal to source face' which is same as 'Parallel to thickness face?.  
Mitreing is provided at the start or end of contour flange or at both start and end of 
contour flange.
******************************************************************************/
struct UF_NXSM_mitre_cflange_data_s
{
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t   mitre_position; 
                                                /* It indicates the cut location if require, 
                                                  IG_NONE -  no mitre(default)  , 
                                                  IG_START - mitre at start,
                                                  IG_RIGHT - mitre at end,   
                                                 */
                                                                                      
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t  mitre_type_at_start;
                                                 /* Type of cut at the start of contour flange
                                                    IG_MITRE_NORMAL_TO_THICKNESS- normal to thickness face(default) , 
                                                    IG_MITRE_PARALLEL_TO_THICKNESS- normal to source face 
                                                  */ 
                                                          

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_type_at_end;  
                                                 /* Type of cut at the end of contour flange
                                                    IG_MITRE_PARALLEL_TO_THICKNESS- normal to thickness face(default),  
                                                    IG_MITRE_NORMAL_TO_THICKNESS- normal to source face 
                                                  */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_side_at_start;
                                                  /* mitre plane orientation at start of contour flange 
                                                     IG_INSIDE - for cut(default),
                                                     IG_OUTSIDE - for grow       
                                                   */       

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_side_at_end; 
                                                  /* mitre plane orientation at end of contour flange 
                                                     IG_INSIDE - for cut(default), 
                                                     IG_OUTSIDE - for grow      
                                                   */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_by_dist_or_angle_at_start; 
                                                  /* Specify mitre cut by distance or angle 
                                                     IG_MITRE_BY_ANGLE -mitre location by angle(default) 
                                                   */
                                                                           
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t mitre_by_dist_or_angle_at_end; 
                                                   /* Specify mitre cut by distance or angle 
                                                      IG_MITRE_BY_ANGLE -mitre location by angle(default) 
                                                    */

    char mitre_angle_at_start[UF_MAX_EXP_LENGTH];  /* Angle in degrees at the start of contour flange */
  
    char mitre_angle_at_end[UF_MAX_EXP_LENGTH];    /* Angle in degrees at the end of contour flange */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t  mitre_cut_type;  
                                                   /* Type of cut  
                                                      IG_MITRE_REGULAR_CUT - Regular or Clean cut (default),
                                                      IG_MITRE_MANUFACTURING_CUT - manufacturing cut 
                                                    */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t close_corner_type;   
                                                    /* Type of corner
                                                       IG_CLOSE_CORNER_NONE - default,
                                                       IG_CLOSE_CORNER_OPEN - corner open,
                                                       IG_CLOSE_CORNER_CLOSED - corner closed,
                                                       IG_CLOSE_CORNER_CIRCLE_CUTOUT - circular cutout at the corner 
                                                     */

    char close_corner_dia[UF_MAX_EXP_LENGTH];       /* Diameter of close corner*/ 

};
typedef struct UF_NXSM_mitre_cflange_data_s UF_NXSM_mitre_cflange_data_t, *UF_NXSM_mitre_cflange_data_p_t;

/*
 *NXSM - BASE CONTOUR FLANGE FEATURE
 */

/* Data structure for Base contour flange  */
struct UF_NXSM_base_cflange_data_s
{
    tag_t sketch_section;                         /* Tag of section object created from sketch.
                                                     NULL_TAG (default) */
    
    char thickness[UF_MAX_EXP_LENGTH];            /* Thickness of contour flange */
    
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t thickness_side;
                                                  /* Thickness direction,  
                                                     IG_LEFT - default,
                                                     IG_RIGHT */
                                                     
    char projection_dist[UF_MAX_EXP_LENGTH];      /* Distance through which sketch is projected */
    
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t projection_side; 
                                                  /* Whether projection is in the normal direction or 
                                                     opposite to the normal direction of datum plane on 
                                                     which profile is generated 
                                                     IG_LEFT - to normal direction (default)
                                                     IG_RIGHT - opposite to normal direction    */
   
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t extent_type;  
                                                 /* Extent to which profile is to be swept, 
                                                    IG_FINITE - sweep the skecth through specified distance along 
                                                                projection direction(default),
                                                    IG_SYMMETRIC - sweep the sketch through specfied distance along
                                                                   normal and opposite to normal to plane
                                                  */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t bend_parm_type;
                                                 /* IG_NFTYPE(default) */

    UF_NXSM_mitre_cflange_data_t mitre_data;     /* Data for mitre cut */

    UF_NXSM_bend_option_t bend_options;          /* Bend data */

    logical is_global_thickness;                     /* Flag for global thickness 
                                                   0 - Thickness value applies to only a feature
                                                   1 - Thickness applies to whole part(default) */ 
};
typedef struct UF_NXSM_base_cflange_data_s UF_NXSM_base_cflange_data_t, *UF_NXSM_base_cflange_data_p_t;

/*
 *NXSM - SECONDARY CONTOUR FLANGE FEATURE
 */

/* Data structure for Secondary contour flange  */
struct UF_NXSM_sec_cflange_data_s
{
    tag_t sketch_section;                          /* Tag of section object created from sketch.
                                                      NULL_TAG (default) */
    
    tag_t ref_edge;                                /* Tag of edge to which flange will be connected */

    tag_t section_edges;                           /* Section tag of edges 
                                                      If NULL_TAG, it is secondary contour flange otherwise chain
                                                      contour flange */  

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t  profile_ref_end; 
                                                   /* It represents the end of the edge where sketch 
                                                        profile is created
                                                      IG_INSIDE - Within the edge (default) */  

    char projection_dist[UF_MAX_EXP_LENGTH];       /* Distance through which sketch is projected */
    
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t  projection_side;
                                                   /* Whether projection is in the normal direction or opposite to 
                                                      the normal direction of datum plane on which profile is generated 
                                                      IG_LEFT - to normal direction (default)
                                                      IG_RIGHT - opposite to normal direction */
   UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t extent_type;
                                              /* To create secondary contour flange use following options 
                                                 Extent to which profile is to be swept, 
                                                 IG_FINITE - sweep the skecth through specified distance along 
                                                             projection direction(default),
                                                 IG_TO_END_OF_EDGE - sweep along the whole edge   
                                                 IG_SYMMETRIC - sweep the sketch through specfied distance along
                                                                     normal and opposite to normal to plane
                                              
                                                To create chain contour flange use following option
                                                IG_TO_END_OF_EDGE - sweep along the whole edge  */
                                                    

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t bend_parm_type;
                                                   /* IG_NFTYPE(default) */
        
    UF_NXSM_mitre_cflange_data_t mitre_data;       /* Data for mitre cut */

    UF_NXSM_bend_option_t bend_options;            /* Bend data */
};
typedef struct UF_NXSM_sec_cflange_data_s UF_NXSM_sec_cflange_data_t, *UF_NXSM_sec_cflange_data_p_t;



 /*
 *NXSM - FLATTEN
 */

/* Data structure for flatten feature  */

struct UF_NXSM_flat_solid_data_s
{
    tag_t     face_tag;                   /* Face to be oriented upward in the flat pattern  
                                             face_tag = NULL_TAG (default) */
   
    tag_t     edge_tag;                   /* Edge for X axis and origin.
                                             edge_tag = NULL_TAG (default) */

    int   is_start_vertex;                /* 0 - Start vertex of edge(default)
                                             1 - End vertex of edge */

};
typedef struct UF_NXSM_flat_solid_data_s UF_NXSM_flat_solid_data_t, *UF_NXSM_flat_solid_data_p_t;


/*
 * NXSM - JOG
 */


/* Data structure for jog feature */
struct UF_NXSM_jog_data_s
{
    tag_t     sketch_tag;                    /* sketch tag or section tag of sketch.
                                                You can either pass sketch tag or create a 
                                                section for sketch, pass the tag of section.
                                                NULL_TAG (default) */

    char  offset_dist[UF_MAX_EXP_LENGTH];    /* Distance through which the two faces will be separated */
    
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t offset_type; 
                                             /* The way offset_dist is measured
                                                IG_OFFSET - Length of web excluding thickness of base body (default)
                                                IG_FULL - Length of web including thickness of base body */
     
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t jog_dir;
                                             /* Direction to which part of the face to be moved to create jog
                                                IG_NORMAL_SIDEDUMMY - In the direction of normal to 
                                                                      selected face (default)
                                                IG_REVERSE_NORMAL_SIDEDUMMY - In opposite direction of
                                                                              normal to selected face */

                                                
    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t fixed_side; 
                                            /* Part of the face which is to be fixed 
                                               IG_LEFT - default,  
                                               IG_RIGHT */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t material_side;
                                            /* IG_INSIDE - default
                                               IG_OUTSIDE 
                                               IG_EXTEND */

    UF_NXSM_FEATURE_PROPERTY_CONSTANTS_e_t extend_option; 
                                            /* Extend the jog along the sketch if the sketch 
                                               is not intersecting boundaries.
                                               IG_EXTEND - Extend the jog along the sketch(default)
                                               IG_NOEXTEND - Don't extend (Don't try this option) */

    UF_NXSM_bend_option_t bend_options; /* Bend data */

};
typedef struct UF_NXSM_jog_data_s UF_NXSM_jog_data_t, *UF_NXSM_jog_data_p_t;



/*
 *NXSM - FLANGE FEATURE
 REFER FLANGE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for flange feature with the
following default values and options. 

    parent_edge = NULL_TAG;
    sketch_tag = NULL_TAG;    
    br_type = IG_RECTANGULAR_BEND_RELIEF;
    cr_type = IG_RIP_CORNER_RELIEF;
    off_type = IG_NONE;
    material_side = IG_LEFT;

    bend_rad = "0.1";
    br_width = "0.1";
    br_length = "0.1";
    off_val = "0.01";       
    n_factor = "0.33";
    angle = "0.0";
    extend_bend_relief = false;

    use_global_radius_value = false;
    use_global_br_width_value = false;
    use_global_br_length_value = false;
    use_global_nfactor_value = false;    

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_flange_data(
UF_NXSM_flange_data_p_t flange_data /* <OF> 
                                     *   The flange data structure to be initialized.
                                     */
);

/****************************************************************************
This is to initialize the data structure for the sketch to be used for flange feature with the
following default values and options. 

    at_start_point = false;
    dim_option = IG_OUTSIDE_DIMENSION;
    width_option = FULL_WIDTH_TYPE;
    prev_width_option = OPTION_NOT_SET;

    length = "0.0";
    width = "0.0";
    dist_from_end = "0.0";
    dist_from_left_end = "0.0";       
    dist_from_right_end = "0.0";       

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_flange_sketch_data(
UF_NXSM_flange_sketch_data_p_t sketch_data /* <OF>
                                            *   The data structure for flange sketchto be initialized.
                                            */
);

/****************************************************************************
This is to create a NXSM flange feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_flange(
UF_NXSM_flange_data_p_t   flange_data,  /* <I>
                                         *   Input data to be used to create a flange feature.
                                         */
UF_NXSM_flange_sketch_data_p_t   sketch_data,  /* <I>
                                                *   Input data for a sketch to be used to create a flange feature.
                                                */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a flange feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_flange(
tag_t feature,          /* <I> 
                         * flange feature to be asked 
                         */
UF_NXSM_flange_data_p_t flange_data, 
                        /* <O>
                         * Data for the flange feature.
                         */
UF_NXSM_flange_sketch_data_p_t sketch_data
                        /* <O>
                         * Data for sketch of the flange feature.
                         */
);

/****************************************************************************
This is to edit a flange feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_flange 
           UF_NXSM_create_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_flange(
tag_t feature,          /* <I> 
                         * flange feature to be edited
                         */
UF_NXSM_flange_data_p_t flange_data,
                        /* <I>
                         * Data for the flange feature.
                         */
UF_NXSM_flange_sketch_data_p_t sketch_data 
                        /* <I>
                         * Data for sketch of the flange feature.
                         */
);

/****************************************************************************
This is to initialize the data structure for flange feature returned by the query method. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_flange_data(
UF_NXSM_flange_data_p_t flange_data /* <I>
                                     *   The flange data structure to be freed.
                                     */
);

/****************************************************************************
This is to free the data structure for the sketch returned by the query method. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_flange_sketch_data(
UF_NXSM_flange_sketch_data_p_t sketch_data /* <I>
                                            *   The data structure for flange sketch to be freed.
                                            */
);


/*
 *NXSM - TAB FEATURE
 REFER TAB BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for base tab feature with the
following default values and options. 

    sketch_obj                 NULL_TAG
    sweep_dist                 0.1/3.0 [in/mm]
    sweep_direction[3]         {0.0,0.0,0.0} 
    is_global_thickness        1
    
    
Environment: Internal  and  External
See Also:  UF_NXSM_create_tab
           UF_NXSM_edit_tab
           UF_NXSM_ask_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_tab_data(
UF_NXSM_tab_data_p_t tab_data /* <OF>
                               * The tab data structure to be initialized.
                               */
);

/****************************************************************************
This is to create a NXSM Tab feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_tab
          UF_NXSM_ask_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_tab(
UF_NXSM_tab_data_p_t   tab_data, /* <I>
                                  * Input data to be used to create a tab feature.
                                  */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a tab feature.
If a sketch_tag was used to create or edit the base tab, a sketch_tag will be returned from this method.
If a section_tag was used to create or edit the base tab, a section_tag will be returned from this method.

Environment: Internal  and  External
See Also:  UF_NXSM_create_tab
          UF_NXSM_edit_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_tab(
tag_t feature,          /* <I> 
                         * Tab feature to be asked
                         */
UF_NXSM_tab_data_p_t tab_data /* <OF>
                               * Data for the Tab feature.
                               */
);
/****************************************************************************
This is to edit a tab feature with given data.

Environment: Internal  and  External
See Also: UF_NXSM_ask_tab
          UF_NXSM_create_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_tab(
tag_t feature,          /* <I> 
                         * Tab feature to be edited
                         */
UF_NXSM_tab_data_p_t tab_data /* <I>
                               * Data for the Tab feature.
                               */
);


/*
 *NXSM - BASE CONTOUR FLANGE FEATURE
 REFER BASE CONTOUR FLANGE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for base contour flange feature with the
following default values and options. 

    sketch_section                              NULL_TAG
    thickness                                   0.00
    thickness_side                              IG_LEFT
    projection_dist                             0.1/3.0 [in/mm]
    projection_side                             IG_LEFT
    extent_type                                 IG_FINITE
    bend_parm_type                              IG_NFTYPE
    mitre_data.mitre_position                   IG_NONE
    mitre_data.mitre_type_at_start              IG_MITRE_NORMAL_TO_THICKNESS
    mitre_data.mitre_type_at_end                IG_MITRE_NORMAL_TO_THICKNESS
    mitre_data.mitre_side_at_start              IG_INSIDE
    mitre_data.mitre_side_at_end                IG_INSIDE
    mitre_data.mitre_by_dist_or_angle_at_start  IG_MITRE_BY_ANGLE
    mitre_data.mitre_by_dist_or_angle_at_start  IG_MITRE_BY_ANGLE
    mitre_data.mitre_angle_at_start             -45.0
    mitre_data.mitre_angle_at_end               -45.0
    mitre_data.mitre_cut_type                   IG_MITRE_REGULAR_CUT
    mitre_data.close_corner_type                IG_CLOSE_CORNER_NONE 
    mitre_data.close_corner_dia                 0.00   
    bend_options.bend_radius                    3.0 / 0.1  [mm/in]
    bend_options.is_bend_radius_global          TRUE
    bend_options.bend_relief                    FALSE
    bend_options.extend_bend_relief             FALSE
    bend_options.bend_relief_type               IG_RECTANGULAR_BEND_RELIEF
    bend_options.bend_relief_depth              3.0 / 0.1 [mm/in]
    bend_options.bend_relief_depth_global       TRUE
    bend_options.bend_relief_width              3.0 / 0.1 [mm/in]
    bend_options.bend_relief_width_global       TRUE
    bend_options.corner_relief                  FALSE
    bend_options.corner_relief_type             IG_RIP_CORNER_RELIEF
    bend_options.neutral_factor                 0.33333    
    bend_options.neutral_factor_global          TRUE
    is_global_thickness                         1    

Environment: Internal  and  External
See Also:  UF_NXSM_create_base_cflange
           UF_NXSM_edit_base_cflange
           UF_NXSM_ask_base_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_base_cflange_data(
UF_NXSM_base_cflange_data_p_t base_cflange_data
                        /* <OF>
                        The base_cflange data structure to be initialized.
                        */
);


/****************************************************************************
This is to create a NXSM base contour flange feature based on the input data. 

Environment: Internal  and  External
See Also:
           UF_NXSM_edit_base_cflange
           UF_NXSM_ask_base_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_base_cflange(
UF_NXSM_base_cflange_data_p_t  base_cflange_data, 
                        /* <I>
                        Input data to be used to create a base contour flange feature.
                        */
tag_t  **features      /* <OF>
                        List of feature identifiers created.  This 
                        must be freed by caller.
                        */
);

/****************************************************************************
This is to edit a base contour flange feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_base_cflange
           UF_NXSM_create_base_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_base_cflange(
tag_t feature,          /* <I> 
                         * Base contour flange feature to be edited
                         */
UF_NXSM_base_cflange_data_p_t base_cflange_data /* <I>
                               * Data for the base contour flange feature.
                               */
);

/****************************************************************************
This is to inquire the data for a feature.


Environment: Internal  and  External
See Also:  UF_NXSM_create_base_cflange
           UF_NXSM_edit_base_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_base_cflange(
tag_t feature,          /* <I> 
                         * Base contour flange feature to be asked
                         */
UF_NXSM_base_cflange_data_p_t base_cflange_data /* <OF>
                               * Data for the base contour flange feature.
*/
);


/*
 *NXSM - BEND FEATURE
 REFER BEND BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for bend feature with the following 
default values and options. 

    sketch_section                         NULL_TAG  
    bend_angle                             90 degrees.
    bend_dir                               IG_NORMAL_SIDEDUMMY
    fixed_side                             IG_LEFT
    material_side                          IG_RIGHT
    extend_option                          IG_EXTEND

    bend_options.bend_radius                3.0 / 0.1 [mm/in]
    bend_options.is_bend_radius_global      TRUE
    bend_options.bend_relief                FALSE
    bend_options.extend_bend_relief         FALSE
    bend_options.bend_relief_type           IG_RECTANGULAR_BEND_RELIEF
    bend_options.bend_relief_depth          3.0 / 0.1 [mm/in]
    bend_options.bend_relief_depth_global   TRUE
    bend_options.bend_relief_width          3.0 / 0.1 [mm/in]
    bend_options.bend_relief_width_global   TRUE
    bend_options.corner_relief              FALSE
    bend_options.corner_relief_type         IG_RIP_CORNER_RELIEF
    bend_options.neutral_factor             TRUE
    bend_options.neutral_factor_global      0.3333333
         
  
Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_cflange,
           UF_NXSM_edit_sec_cflange
           UF_NXSM_ask_sec_cflange
        
History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_bend_data(
UF_NXSM_bend_data_p_t bend_data
                        /* <OF>
                        bend data structure to be initialized.
                        */
);

/****************************************************************************
This is to create a NXSM bend feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_bend
           UF_NXSM_ask_bend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_bend(
    UF_NXSM_bend_data_p_t  bend_data, 
                        /* <I>
                        Input data to be used to create a bend feature.
                        */
   
    tag_t  **features   /* <OF>
                           List of feature identifiers created.  This 
                           must be freed by caller.
                        */
   
);

/****************************************************************************
This is to inquire the data for NXSM Bend feature.
If a sketch_tag was used to create or edit the bend, a sketch_tag will be returned from this method.
If a section_tag was used to create or edit the bend, a section_tag will be returned from this method.


Environment: Internal  and  External
See Also:  UF_NXSM_create_bend
           UF_NXSM_edit_bend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_bend(
tag_t feature,          /* <I> 
                         * bend feature to be asked
                         */
UF_NXSM_bend_data_p_t bend_data /* <OF>
                               * Data for the bend feature.
                               */
);

/****************************************************************************
This is to edit a NXSM bend feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_bend
           UF_NXSM_create_bend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_bend(
tag_t feature,          /* <I> 
                         * Bend feature to be asked
                         */
UF_NXSM_bend_data_p_t bend_data /* <I>
                               * Data for the bend feature.
                               */
);



/*
 *NX - CLOSED CORNER FEATURE
 REFER CLOSED CORNER FEATURE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for closed corner feature with the
following default values and options. 

    n_edges = 0;            
    parent_edges = NULL;    
    treatment_type = IG_TREATMENT_OFF;
    closure_type = IG_CLOSE_CORNER_NONE;
    treatment_dia = 0.0;
    overlap_ratio = 0.0;
    corner_gap = 0.0;       

Environment: Internal  and  External
See Also:  UF_NXSM_create_closed_corner
           UF_NXSM_edit_closed_corner
           UF_NXSM_ask_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_closed_corner_data(
UF_NXSM_closed_corner_data_p_t clcorner_data /* <OF>
                                     *   The clcorner data structure to be initialized.
                                     */
);

/****************************************************************************
This is to create a NXSM closed corner feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_closed_corner
           UF_NXSM_ask_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_closed_corner(
UF_NXSM_closed_corner_data_p_t   clcorner_data,  /* <I>
                                         *   Input data to be used to create a clcorner feature.
                                         */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a closed corner feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_closed_corner
           UF_NXSM_edit_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_closed_corner(
tag_t feature,          /* <I> 
                         * clcorner feature to be asked 
                         */
UF_NXSM_closed_corner_data_p_t clcorner_data 
                        /* <OF>
                         * Data for the clcorner feature.
                         */
);

/****************************************************************************
This is to edit a closed corner feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_closed_corner 
           UF_NXSM_create_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_closed_corner(
tag_t feature,          /* <I> 
                         * clcorner feature to be edited
                         */
UF_NXSM_closed_corner_data_p_t clcorner_data 
                        /* <I>
                         * Data for the clcorner feature.
                         */
);

/****************************************************************************
This is to free the data structure for closed corner feature. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_closed_corner
           UF_NXSM_edit_closed_corner
           UF_NXSM_ask_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_closed_corner_data(
UF_NXSM_closed_corner_data_p_t clcorner_data /* <I>
                                     *   The clcorner data structure to be freed.
                                     */
);


/****************************************************************************
This is used to get a corner edge given its associated bend faces.

History:New in NX5.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_get_qualified_corner_edge
(tag_t bend_face1,/*<I> 
                    * Bend face adjacent to a corner edge
                    */ 
 tag_t bend_face2, /*<I> 
                   * Another bend face adjacent to a corner edge
                   */
 logical is_3flange_feature,/* <I>
                            * True if the corner is of 3 bend   
                            */
 tag_t* corner_edge/*<O>
                   * Corner edge of the associated bend faces
                   */ );




/*
 *NXSM - FLATTEN FEATURE
 REFER FLATTEN FEATURE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for flatten feature with the
following default values and options.

    face_tag          NULL_TAG
    edge_tag          NULL_TAG
    is_start_vertex   0

Environment: Internal  and  External
See Also: UF_NXSM_create_flat_solid
          
History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_init_flat_solid(
UF_NXSM_flat_solid_data_p_t flat_solid_data
                        /* <I/O>
                        The flatten data structure to be initialized.
                        */
);



/****************************************************************************
This is to create a SBSM flatten feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_init_flat_solid
       
History:New in NX3.0

 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_create_flat_solid(
    UF_NXSM_flat_solid_data_p_t  flat_solid_data, 
                        /* <I>
                        Input data to be used to create a flatten feature.
                        */
   
    tag_t  **features   /* <OF> 
                           List of feature identifiers created.  This 
                           must be freed by caller.
                           Use SM_free( ) to free the features
                        */
);


/****************************************************************************
This is to inquire the data for a flatten feature.

Environment: Internal  and  External
See Also: UF_NXSM_create_flat_solid
          UF_NXSM_edit_flat_solid
History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_flat_solid(
            tag_t feature, /* <I> 
                            * Flatten feature to be asked
                            */       
            UF_NXSM_flat_solid_data_p_t flat_solid_data     /* <OF>
                                                             * Data for the Flatten feature.
                                                             */
            );


/****************************************************************************
This is to edit a Flatten feature with given data.
On Success returns 0.

Environment: Internal  and  External
See Also: UF_NXSM_ask_flat_solid
          UF_NXSM_create_flat_solid
History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_edit_flat_solid(
        tag_t features, /* <I> 
                         * Flatten feature to be edited */

        UF_NXSM_flat_solid_data_p_t get_flat_solid_data  /* <I>
                               * Data for the Flatten feature. */
        );




/*
 *NXSM - JOG FEATURE
 REFER JOG FEATURE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for jog feature with the following 
default values and options. 

    sketch_tag                                 NULL_TAG
    offset_dist                                25.4/1.00 [mm/in]
    offset_type                                IG_OFFSET
    fixed_side                                 IG_LEFT
    material_side                              IG_INSIDE
    extend_option                              IG_EXTEND 
    
    bend_options.bend_radius                   3.0 / 0.1 [mm/in]
    bend_options.is_bend_radius_global         TRUE
    bend_options.bend_relief                   FALSE
    bend_options.extend_bend_relief            FALSE
    bend_options.bend_relief_type              IG_RIP_BEND_RELIEF
    bend_options.bend_relief_depth             3.0 / 0.1 [mm/in]
    bend_options.bend_relief_depth_global      TRUE
    bend_options.bend_relief_width             3.0 / 0.1 [mm/in]
    bend_options.bend_relief_width_global      TRUE
    bend_options.corner_relief                 FALSE
    bend_options.corner_relief_type            IG_RIP_CORNER_RELIEF
    bend_options.neutral_factor                TRUE
    bend_options.neutral_factor_global         0.3333333
         
  
Environment: Internal  and  External
See Also: UF_NXSM_create_jog
          UF_NXSM_edit_jog
          UF_NXSM_ask_jog

History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_init_jog(
UF_NXSM_jog_data_p_t jog_data
                        /* <I/O>
                        The jog data structure to be initialized.
                        */
);


/****************************************************************************
This is to create a SBSM jog feature based on the input data. 


Environment: Internal  and  External
See Also: UF_NXSM_edit_jog
          UF_NXSM_ask_jog

History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_create_jog(
    UF_NXSM_jog_data_p_t  jog_data, 
                        /* <I>
                        Input data to be used to create a jog feature.
                        */
   
    tag_t  **features   /* <OF> 
                           List of feature identifiers created.  This 
                           must be freed by caller.
                           Use SM_free( ) to free the features
                        */
);


/****************************************************************************
This is to inquire the data for a jog feature.
If a sketch_tag was used to create or edit the jog, a sketch_tag will be returned from this method.
If a section_tag was used to create or edit the jog, a section_tag will be returned from this method.

Environment: Internal  and  External
See Also: UF_NXSM_create_jog
          UF_NXSM_edit_jog

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_jog(
tag_t feature,          /* <I> 
                         * Jog feature to be asked
                         */
UF_NXSM_jog_data_p_t jog_data /* <OF>
                               * Data for the Jog feature.
                               */
);
/****************************************************************************
This is to edit a jog feature with given data.

Environment: Internal  and  External
See Also: UF_NXSM_ask_jog
          UF_NXSM_create_jog

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_jog(
tag_t feature,          /* <I> 
                         * Jog feature to be edited */
                         
UF_NXSM_jog_data_p_t jog_data /* <I>
                               * Data for the jog feature. */
                               
);


/*
 *NX - REBEND FEATURE
 REFER REBEND FEATURE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for base rebend feature with the
following default values and options. 

    tag_t face_collector    = NUL_TAG;
    int   nbend         = 0;
    tag_t *unbend_list    = NULL;

Environment: Internal  and  External
See Also:  UF_NXSM_create_rebend
           UF_NXSM_edit_rebend
           UF_NXSM_ask_rebend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_rebend_data(
UF_NXSM_rebend_data_p_t rebend_data /* <OF>
                                     *   The rebend data structure to be initialized.
                                     */
);

/****************************************************************************
This is to create a NXSM rebend feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_rebend  
           UF_NXSM_ask_rebend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_rebend(
UF_NXSM_rebend_data_p_t   rebend_data,  /* <I>
                                         *   Input data to be used to create a rebend feature.
                                         */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a rebend feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_rebend
          UF_NXSM_edit_rebend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_rebend(
tag_t feature,          /* <I> 
                         * rebend feature to be asked 
                         */
UF_NXSM_rebend_data_p_t rebend_data 
                        /* <OF>
                         * Data for the rebend feature.
                         */
);
/****************************************************************************
This is to edit a rebend feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_rebend
           UF_NXSM_create_rebend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_rebend(
tag_t feature,          /* <I> 
                         * rebend feature to be edited
                         */
UF_NXSM_rebend_data_p_t rebend_data 
                        /* <I>
                         * Data for the rebend feature.
                         */
);

/****************************************************************************
This is to free the data structure for rebend feature. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_unbend
           UF_NXSM_edit_unbend
           UF_NXSM_ask_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_rebend_data(
UF_NXSM_rebend_data_p_t rebend_data /* <I>
                                     *   The rebend data structure to be freed.
                                     */
);


/*
 *NXSM - SECONDARY CONTOUR FLANGE FEATURE
 REFER SECONDARY CONTOUR FLANGE FEATURE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for secondary contour flange feature with the
following default values and options. 

    sketch_section                              NULL_TAG
    ref_edge                                    NULL_TAG     
    section_edges                               NULL
    profile_ref_end                             IG_INSIDE
    projection_dist                             25.4 / 1.0 [mm/in]
    projection_side                             IG_LEFT
    extent_type                                 IG_FINITE
    bend_parm_type                              IG_NFTYPE
    mitre_data.mitre_position                   IG_NONE
    mitre_data.mitre_type_at_start              IG_MITRE_NORMAL_TO_THICKNESS
    mitre_data.mitre_type_at_end                IG_MITRE_NORMAL_TO_THICKNESS
    mitre_data.mitre_side_at_start              IG_INSIDE
    mitre_data.mitre_side_at_end                IG_INSIDE
    mitre_data.mitre_by_dist_or_angle_at_start  IG_MITRE_BY_ANGLE
    mitre_data.mitre_by_dist_or_angle_at_start  IG_MITRE_BY_ANGLE
    mitre_data.mitre_angle_at_start             -45.0 degrees
    mitre_data.mitre_angle_at_end               -45.0 degrees 
    mitre_data.mitre_cut_type                   IG_MITRE_REGULAR_CUT
    mitre_data.close_corner_type                IG_CLOSE_CORNER_NONE 
    mitre_data.close_corner_dia                 0.00   [mm/in]
    bend_options.bend_radius                    3.0 / 0.1  [mm/in]
    bend_options.is_bend_radius_global          TRUE
    bend_options.bend_relief                    FALSE
    bend_options.extend_bend_relief             FALSE
    bend_options.bend_relief_type               IG_RECTANGULAR_BEND_RELIEF
    bend_options.bend_relief_depth              3.0 / 0.1 [mm/in]
    bend_options.bend_relief_depth_global       TRUE
    bend_options.bend_relief_width              3.0 / 0.1 [mm/in]
    bend_options.bend_relief_width_global       TRUE
    bend_options.corner_relief                  FALSE
    bend_options.corner_relief_type             IG_RIP_CORNER_RELIEF
    bend_options.neutral_factor                 0.33333    
    bend_options.neutral_factor_global          TRUE
    
        
    
Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_cflange
           UF_NXSM_edit_sec_cflange
           UF_NXSM_ask_sec_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_sec_cflange_data(
UF_NXSM_sec_cflange_data_p_t sec_cflange_data
                        /* <OF>
                        The secondary cflange data structure to be initialized.
                        */
);

/****************************************************************************
This is to create a NXSM secondary contour flange feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_sec_cflange
           UF_NXSM_ask_sec_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_sec_cflange(
    UF_NXSM_sec_cflange_data_p_t  sec_cflange_data, 
                        /* <I>
                        Input data to be used to create a secondary contour flange feature.
                        */
    tag_t  **features   /* <OF>
                           List of feature identifiers created.  This 
                           must be freed by caller.
                        */
);

/****************************************************************************
This is to edit a secondary contour flange feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_sec_cflange
           UF_NXSM_create_sec_cflange

History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_edit_sec_cflange(
tag_t feature,          /* <I> 
                         * Secondary contour flange feature to be asked
                         */
UF_NXSM_sec_cflange_data_p_t sec_cflange_data /* <I>
                               * Data for the Secondary contour flange feature.
                               */

);

/****************************************************************************
This is to inquire the data for a Secondary Contour Flange feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_cflange
           UF_NXSM_edit_sec_cflange

History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_ask_sec_cflange(
tag_t feature,          /* <I> 
                         * secondary contour flange feature to be asked
                         */
UF_NXSM_sec_cflange_data_p_t sec_cflange_data /* <OF>
                               * Data for the secondary contour flange feature.
                               */
);


/*
 *NXSM - SECONDARY TAB FEATURE
 REFER SECONDARY TAB FEATURE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for secondary tab feature with the
following default values and options. 

    sketch_profile             NULL_TAG
    placement_face             NULL_TAG
    material_side              IG_LEFT
    
   
Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_tab
           UF_NXSM_edit_sec_tab
           UF_NXSM_ask_sec_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_sec_tab_data(
UF_NXSM_sec_tab_data_p_t tab_data
                        /* <OF>
                        The secondary tab data structure to be initialized.
                        */
);

/****************************************************************************
This is to create a NXSM Secondary Tab feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_sec_tab,
           UF_NXSM_ask_sec_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_sec_tab(
UF_NXSM_sec_tab_data_p_t   sec_tab_data, 
                        /* <I>
                        Input data to be used to create a secondary tab feature.
                        */
tag_t  **features       /* <OF>
                        List of feature identifiers created.  This 
                        must be freed by caller.
                        */
);

/****************************************************************************
This is to inquire the data for a secondary tab feature.
If a sketch_tag to create or edit the secondary tab, a sketch_tag will be returned from this method.
If a section_tag to create or edit the secondary tab, a section_tag will be returned from this method.

Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_tab
           UF_NXSM_edit_sec_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_sec_tab(
tag_t feature,          /* <I> 
                        Tab feature to be asked */
UF_NXSM_sec_tab_data_p_t sec_tab_data 
                        /* <OF>
                        Data for the secondary tab feature.
                        */
);
/****************************************************************************
This is to edit a secondary tab feature with given data.  

Environment: Internal  and  External
See Also:  UF_NXSM_ask_sec_tab
           UF_NXSM_create_sec_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_sec_tab(
tag_t feature,          /* <I> 
                        Tab feature to be edited*/
UF_NXSM_sec_tab_data_p_t sec_tab_data 
                        /* <I>
                        Data for the Tab feature.
                        */
);


/*
 *NX - UNBEND FEATURE
 REFER UNBEND FEATURE BUILDER FOR EQUIVALENT APIS
 */

/****************************************************************************
This is to initialize the data structure for base unbend feature with the
following default values and options. 

    tag_t face_collector    = NULL_TAG;
    tag_t ref_entity    = NULL_TAG;
    int   nbend         = 0;
    tag_t *bend_list    = NULL;
    tag_t body = NULL_TAG;


Environment: Internal  and  External
See Also:  UF_NXSM_create_unbend
           UF_NXSM_edit_unbend
           UF_NXSM_ask_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_unbend_data(
UF_NXSM_unbend_data_p_t unbend_data /* <OF>
                                     *   The unbend data structure to be initialized.
                                     */
);

/****************************************************************************
This is to create a NXSM unbend feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_unbend
           UF_NXSM_ask_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_unbend(
UF_NXSM_unbend_data_p_t   unbend_data,  /* <I>
                                         *   Input data to be used to create a unbend feature.
                                         */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a unbend feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_unbend
           UF_NXSM_edit_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_unbend(
tag_t feature,          /* <I> 
                         * unbend feature to be asked 
                         */
UF_NXSM_unbend_data_p_t unbend_data 
                        /* <OF>
                         * Data for the unbend feature.
                         */
);

/****************************************************************************
This is to edit a unbend feature with given data.

Environment: Internal  and  External
See Also: UF_NXSM_ask_unbend
          UF_NXSM_create_unbend


History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_unbend(
tag_t feature,          /* <I> 
                         * unbend feature to be edited
                         */
UF_NXSM_unbend_data_p_t unbend_data 
                        /* <I>
                         * Data for the unbend feature.
                         */
);

/****************************************************************************
This is to free the data structure for unbend feature. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_unbend
           UF_NXSM_edit_unbend
           UF_NXSM_ask_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_unbend_data(
UF_NXSM_unbend_data_p_t unbend_data /* <I>
                                     *   The unbend data structure to be freed.
                                     */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING */
