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
#include <uf_sf_types.h>
#include <uf_retiring_ugopenint.h>
#include <setjmp.h>
#include <libufun_exports.h>
#include <uf_curve.h>
#include <uf_weld_types.h>
#include <uf_sf_post_datatypes.h>
#include <uf_ugmgr_types.h>

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

/* The ifndef is used because this definition is defined in uf_sf_types.h
 * but because of massive recompile issues, it is also defined here */
#ifndef  UF_SF_LOAD_MODE_T__H_INCLUDED
#define  UF_SF_LOAD_MODE_T__H_INCLUDED
enum UF_SF_load_mode_e
{
    UF_SF_LOAD_FORCE =  1,         /* Force. */
    UF_SF_LOAD_DISTRIBUTED =  2,   /* Uniform pressure, applicable only normal
                                      to the face. */
    UF_SF_LOAD_SPACIAL =  3,
    UF_SF_LOAD_GRAVITY =  4,       /* Gravity load. */
    UF_SF_LOAD_PRESSURE =  5,      /* Pressure load, can be appied in any
                                      direction. */
    UF_SF_LOAD_MOMENT =  6,        /* Moment. */
    UF_SF_LOAD_SHEAR =  7,         /* Edge shear. */
    UF_SF_LOAD_FLUX =  8,          /* Heat flux. */
    UF_SF_LOAD_TEMPERATURE =  9,  /* Temperature load. */
    UF_SF_LOAD_CENTRIFUGAL = 10,    /* Centrifugal load. */
    UF_SF_LOAD_TORQUE = 11,         /* Torque */
    UF_SF_LOAD_BEARING = 12,         /* Bearing */

    UF_SF_LOAD_UNKNOWN_MODE = -99999   /* Unknown load mode type */
};
typedef enum UF_SF_load_mode_e  UF_SF_load_mode_t,
                               *UF_SF_load_mode_p_t;
#endif  /* UF_SF_LOAD_MODE_T__H_INCLUDED */

/* The ifndef is used because this definition is defined in uf_sf_types.h
 * but because of massive recompile issues, it is also defined here */
#ifndef  UF_SF_BC_MODE_T__H_INCLUDED
#define  UF_SF_BC_MODE_T__H_INCLUDED
enum UF_SF_bc_mode_e
{
    UF_SF_BC_CONSTRAINT = 1,            /* Both linear displacement and rotation
                                           are available. */
    UF_SF_BC_DISPLACEMENT = 2,          /* Only displacement is available,
                                           rotation is free. */
    UF_SF_BC_ROTATION = 3,              /* Only rotation is available,
                                           displacement is free. */
    UF_SF_BC_TEMPERATURE = 4,           /* Temperature BC is available. */
    UF_SF_BC_CONVECTION_COEFFICIENT = 5,/* Convection coefficient BC is
                                           available. */

    UF_SF_BC_UNKNOWN_MODE = -99999      /* Unknown BC mode type */
};
typedef enum UF_SF_bc_mode_e  UF_SF_bc_mode_t,
                             *UF_SF_bc_mode_p_t;
#endif  /* UF_SF_BC_MODE_T__H_INCLUDED */

/* The ifndef is used because this definition is defined in uf_sf_types.h
 * but because of massive recompile issues, it is also defined here */
#ifndef  UF_SF_LBC_COMPONENT_TYPE_T__H_INCLUDED
#define  UF_SF_LBC_COMPONENT_TYPE_T__H_INCLUDED
enum UF_SF_LBC_component_type_e
{
    UF_SF_NULL_COMP = -1,
    UF_SF_LBC_XYZ = 0,   /* Having XYZ components - rectangular coordinates. */
    UF_SF_LBC_RTZ,       /* Having RTZ components - Cylindrical coordinates. */
    UF_SF_LBC_RTP,       /* Having RTP components - Spherical coordinates. */
    UF_SF_LBC_NORMAL_TO, /* Applicable normal to a face only. */
    UF_SF_LBC_EDGE_CSYS  /* Applicable along an edge only. */
};
typedef enum UF_SF_LBC_component_type_e  UF_SF_LBC_component_type_t,
                                        *UF_SF_LBC_component_type_p_t;
#endif  /* UF_SF_LBC_COMPONENT_TYPE_T__H_INCLUDED */

/* The ifndef is used because this definition is defined in uf_sf_types.h
 * but because of massive recompile issues, it is also defined here */
#ifndef  UF_SFANS_SOLVER_DATA_T__H_INCLUDED
#define  UF_SFANS_SOLVER_DATA_T__H_INCLUDED
typedef struct UF_SFANS_solver_data_s
{
    int formatChoice;
    int algoChoice;
    int num_roots;
    double upper_limit;
    double lower_limit;
    double temperature;
} UF_SFANS_solver_data_t, *UF_SFANS_solver_data_p_t;
#endif  /* UF_SFANS_SOLVER_DATA_T__H_INCLUDED */

/* The ifndef is used because this definition is defined in uf_sf_types.h
 * but because of massive recompile issues, it is also defined here */
#ifndef  UF_SF_DIST_TYPE_T__H_INCLUDED
#define  UF_SF_DIST_TYPE_T__H_INCLUDED
typedef enum
{
   UF_SF_SINUSOIDAL = 0,
   UF_SF_PARABOLIC
}UF_SF_dist_type_t;
#endif  /* UF_SF_DIST_TYPE_T__H_INCLUDED */


/*-----------------------------------------------------------------------------
Formats or submits a problem for Nastran analysis.

This function should be replaced with UF_SF_solve_active_solution_nx.

To set the default temperature, number of roots, and frequency limits:

Get the tag of the active solution by calling
UF_SF_ask_active_solution_and_step_nx.
Get the tags of the steps in the active solution by calling
UF_SF_solution_ask_num_steps_nx and UF_SF_solution_ask_nth_step_nx.

Get the property tags by calling UF_SF_solution_ask_property_nx
and UF_SF_step_ask_property_nx. The names corresponding
to the argument list in this function are:
"Default Temperature"
"Frequency Range - Lower Limit",
"Frequency Range - Upper Limit"
"Number of Desired Modes"

Use UF_SF_property_set_value_nx to set the values.

note: Environment variable must be set for NASTRAN.
possible return error values are:

UF_SF_NAS_ANA_S_SUBMIT_ERR  Submission error,

UF_SF_NAS_ANA_S_ENV_VAR_ERR if environment for
NASTRAN is not set,

UF_SF_NAS_ANA_S_AUTHFILE_VAR_NOT_FOUND if licence
is not found,

UF_SF_NAS_ANA_S_BOUNDARY_CONFLICTS for conflicted BC's

UF_SF_NAS_ANA_S_FORMAT_COMPLETE for successful format.

UF_SF_NO_ACTIVE_SOLUTION if no solution is active.

UF_SF_INCOMPATIBLE_SOLUTION is solver for active solution is not NASTRAN.

Environment: Internal  and  External

See Also:

History:
-----------------------------------------------------------------------------*/
extern UFUNEXPORT int UF_SF_analysis_nastran (
char* job_title ,/* <I>
                 Name of job for Nastran run.
                 */
int format_choice ,/* <I>
                   Format/Solve option:
                    0 (for format and solve)
                    1 (for format only)
                   */
double temperature ,/* <I>
                    temperature
                    */
double upper_limit ,/* <I>
                    Upper frequency limit, only for Modal analysis.
                    */
double lower_limit ,/* <I>
                    Lower frequency limit, only for Modal analysis.
                    */
int num_roots /* <I>
               Number of modes, only for Modal analysis.
               */
);

extern UFUNEXPORT int UF_SF_analysis_thermal_flow (
int format_choice /* <I> Format/Solve option:
                    0 (for format and solve)
                    1 (for format only)
                   */
);


/*-----------------------------------------------------------------------------
This routine format and solve a problem using StructureP.E solver

This function should be replaced with UF_SF_solve_active_solution_nx.

To set the default temperature, number of roots, frequency limits, and
scratch directory:

Get the tag of the active solution by calling
UF_SF_ask_active_solution_and_step_nx.
Get the tags of the steps in the active solution by calling
UF_SF_solution_ask_num_steps_nx and UF_SF_solution_ask_nth_step_nx.

Get the property tags by calling UF_SF_solution_ask_property_nx
and UF_SF_step_ask_property_nx. The names corresponding to the
argument list in this function are:
"Default Temperature"
"Frequency Range - Lower Limit",
"Frequency Range - Upper Limit"
"Number of Desired Modes"

Get the solver property tags by calling UF_SF_solution_ask_solver_property_nx.
The names corresponding to the argument list in this function are:
"Scratch Directory"

Use UF_SF_property_set_value_nx to set the values.

Environment: Internal and External

See Also:

History:

 ----------------------------------------------------------------------------*/
extern UFUNEXPORT int UF_SF_format_solve_ugfea_analysis
(
  char  *scratch_dir,    /* <I> if NULL use UGII_TMP_DIR */
  int    num_of_modes,   /* <I> number of eigen values to extract */
  double lower_limit,    /* <I> eigen value lower limit */
  double upper_limit,    /* <I> eigen value upper limit */
  double temperature     /* <I> reference temperature */
);

/*-----------------------------------------------------------------------------
Formats or submit a problem for Abaqus analysis.

This function should be replaced with UF_SF_solve_active_solution_nx.

To set the default temperature, number of roots, frequency limits, and
scratch directory:

Get the tag of the active solution by calling
UF_SF_ask_active_solution_and_step_nx.
Get the tags of the steps in the active solution by calling
UF_SF_solution_ask_num_steps_nx and UF_SF_solution_ask_nth_step_nx.

Get the property tags by calling UF_SF_solution_ask_property_nx
and UF_SF_step_ask_property_nx. The names corresponding to the argument
list in this function are:
"Default Temperature"
"Frequency Range - Lower Limit",
"Frequency Range - Upper Limit"
"Number of Desired Modes"

Get the solver property tags by calling UF_SF_solution_ask_solver_property_nx.
The names corresponding to the argument list in this function are:
"Scratch Directory"

Use UF_SF_property_set_value_nx to set the values.

note: UGII_ABAQUS Environment variable must be set run Abaqus analysis.

possible return error values are:

    UF_SF_INVALID_SCRATCH_DIR           Invalid scratch directory
    UF_SF_ABAQUS_INVALID_SOLVE_OPTION   Invalid solve option
    UF_SF_ABAQUS_NO_STEPS_DEFINED       No steps defined
    UF_SF_ABAQUS_ENV_VAR_ERROR          UGII_ABAQUS env variable not set
    UF_SF_ABAQUS_BC_CONFLICTS           Conflicting BCs with in a step
    UF_SF_ABAQUS_ALL_STEPS_SUPPRESSEd   All steps are suppressed
    UF_SF_ABAQUS_SUBMIT_ERROR           Analysis job submission error
    UF_SF_NO_ACTIVE_SOLUTION            No solution is active.
    UF_SF_INCOMPATIBLE_SOLUTION         Active solution's solver is not ABAQUS.

Environment: Internal  and  External

See Also: UF_SF_abaqus_create_step

History:
-----------------------------------------------------------------------------*/
extern UFUNEXPORT int  UF_SF_analysis_abaqus
(
  char  *scratch_dir,    /* <I> if NULL use UGII_TMP_DIR */
  int   solve_option,    /* <I> 0 = format and solve
                                1 = format only
                         */
  int    num_of_modes,   /* <I> number of eigen values to extract */
  double lower_limit,    /* <I> eigen value lower limit */
  double upper_limit,    /* <I> eigen value upper limit */
  double temperature     /* <I> reference temperature */
);

/*-----------------------------------------------------------------------------
Formats or submits a problem for Ansys analysis.

This function should be replaced with UF_SF_solve_active_solution_nx.

To set the default temperature, number of roots, and frequency limits:

Get the tag of the active solution by calling
UF_SF_ask_active_solution_and_step_nx.
Get the tags of the steps in the active solution by calling
UF_SF_solution_ask_num_steps_nx and UF_SF_solution_ask_nth_step_nx.

Get the property tags by calling UF_SF_solution_ask_property_nx
and UF_SF_step_ask_property_nx. The names corresponding to the argument
list in this function are:
"Default Temperature"
"Frequency Range - Lower Limit",
"Frequency Range - Upper Limit"
"Number of Modes"

Use UF_SF_property_set_value_nx to set the values.

note: Environment variable must be set for ANSYS.

possible return error values are:
UF_SF_NAS_ANA_S_SUBMIT_ERR  Submission error,

UF_SF_NAS_ANA_S_ENV_VAR_ERR if environment for Ansys is not set,

UF_SF_NAS_ANA_S_AUTHFILE_VAR_NOT_FOUND if licence is not found,

UF_SF_NAS_ANA_S_BOUNDARY_CONFLICTS for  conflicted BC's

UF_SF_NO_ACTIVE_SOLUTION if no solution is active.

UF_SF_INCOMPATIBLE_SOLUTION if active solution's solver is not ANSYS.

Environment: Internal  and  External

See Also:

History:
-----------------------------------------------------------------------------*/
extern UFUNEXPORT int    UF_SF_analysis_ansys (
char* job_title ,/* <I>
                 Name of job for Ansys run.
                 */
int format_choice ,/* <I>
                   Format/Solve option:
                    0 (for format and solve)
                    1 (for format only)
                   */
double temperature ,/* <I>
                    temperature
                    */
double upper_limit ,/* <I>
                    Upper frequency limit, only for Modal analysis.
                    */
double lower_limit ,/* <I>
                    Lower frequency limit, only for Modal analysis.
                    */
int num_roots /* <I>
               Number of modes, only for Modal analysis.
              */
);

/*-----------------------------------------------------------------------------
Formats or submits a problem for Ansys analysis. This function is a replacement
for UF_SF_analysis_ansys, and has been upgraded to allow more control over the
job parameters and options.

This function should be replaced with UF_SF_solve_active_solutio_nx.

To set the default temperature, number of roots, frequency limits, and
algorith:

Get the tag of the active solution by calling
UF_SF_ask_active_solution_and_step_nx.
Get the tags of the steps in the active solution by calling
UF_SF_solution_ask_num_steps and UF_SF_solution_ask_nth_step.

Get the property tags by calling UF_SF_solution_ask_property_nx
and UF_SF_step_ask_property_nx. The names corresponding to the argument
list in this function are:

"Default Temperature"
"Frequency Range - Lower Limit",
"Frequency Range - Upper Limit"
"Number of Modes"
"Algorithm"

Use UF_SF_property_set_value_nx to set the values.

For "Algorith", the property enum values are as follows:

  Solution type = Linear Statics, Linear Statics - Adaptive, Nonlinear Statics,
                  Buckling, and Thermal:
   Frontal = 0
   PCG = 1
   JCG = 2
   Sparse = 3

  Solution type = Modal:
   Subspace = 0
   Lanczos = 1
   Power Dynamics = 2

note: Environment variable must be set for ANSYS.
    UGII_ANSYS
    UGII_ANSYS_VERSION

UF_SF_format_solve_ansys_analysis:

possible return error values are:
    UF_SF_NAS_ANA_S_SUBMIT_ERR  Submission error,
    UF_SF_NAS_ANA_S_ENV_VAR_ERR if environment for Ansys is not set,
    UF_SF_NAS_ANA_S_AUTHFILE_VAR_NOT_FOUND if licence is not found,
    UF_SF_NAS_ANA_S_BOUNDARY_CONFLICTS for  conflicted BC's
    UF_SF_NO_ACTIVE_SOLUTION if no solution is active.
    UF_SF_INCOMPATIBLE_SOLUTION if active solution's solver is not ANSYS.

Environment: Internal  and  External

See Also:

History:
-----------------------------------------------------------------------------*/
extern UFUNEXPORT int    UF_SF_format_solve_ansys_analysis (
char* job_title ,/* <I>
                              Name of job for Ansys run.
                 */
UF_SFANS_solver_data_t  *user_solver_data  /* <I> solutions parameters
                              formatChoice     Format/Solve option
                                               0 (for format and solve)
                                               1 (for format only)
                              temperature      Reference temperature
                              num_roots        number of modal eigen values to extract
                              upper_limit      modal eigen values upper limit
                              Lower_limit      modal eigen value lower limit

                              algoChoice       Solver algorithm options
                                  CHOOSE ONE FOR ME  -1
                                  FRONTAL_SOLVER     0
                                  PCG_SOLVER         1
                                  JCG_SOLVER         2
                                  SPARSE_SOLVER      3
                                  JCG_PCG_SOLVER     4
                                  JCG_FRONTAL_SOLVER 5
                                  SUBSPACE_MODOPT    6
                                  LANCZOS_MODOPT     7
                                  POWERDYN_MODOPT    8
                                            */
);

/***************************************************************************
Finds all the load cases and boundary condition sets in the given
scenario part. If you pass NULL_TAG to the first argument, then the
current work part is traversed.

Calls to this function should be replaced with appropriate calls to the
following functions:  UF_SF_ask_num_solutions_nx, UF_SF_ask_nth_solution_nx,
UF_SF_solution_ask_num_steps_nx, UF_SF_solution_ask_nth_step_nx.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_SF_locate_all_lbc_cases(
tag_t  part_tag ,/* <I>
                 Tag of the part to traverse for load case.
                 If NULL_TAG is passed then
                 current work part is traversed.
                 */
int* num_lbc_cases ,/* <O>
                    Number of load cases and
                    boundary condition sets found in
                    the current scenario part.
                    */
tag_p_t*  lbc_case_pp  /* <OF,len:num_lbc_cases>
                       pointer to the pointer to the array
                       of the tag for the load cases and
                       the boundary condition sets.  if
                       num_lbc_cases != 0, must be freed
                       in the calling routine by calling UF_free.
                       */
);


/***************************************************************************
Removes the specified number of loads and boundary conditions from
a load case or boundary condition set.

Calls to this function should be replaced with appropriate calls to the
following functions:  UF_SF_remove_from_solution_nx, UF_SF_remove_from_step_nx.

Environment: Internal  and  External

See Also:

History:

****************************************************************************/
extern UFUNEXPORT int UF_SF_remove_from_lbc_case(
int num_of_lbc ,/* <I>
                Number of loads and boundary conditions.
                */
tag_t*  lbc ,/* <I,len:num_of_lbc>
             pointer to the array of tags for  loads or
             boundary conditions
             */
tag_t lbc_case  /* <I>
                The tag for a load case or boundary
                condition set
                */
);

/***************************************************************************
Locates the loads and boundary conditions in
a load case or boundary condition set.  The membs_pp pointer is
undefined if num_members is zero.

Calls to this function should be replaced with appropriate calls to the
following functions:  UF_SF_locate_solution_members_nx, UF_SF_locate_step_members_nx.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_SF_locate_lbc_members(
tag_t lbc_case ,/* <I>
                the tag for a load case or bc set
                */
int *num_members ,/* <O>
                 number of loads and bc's in the load case or
                 bc set
                 */
tag_t** membs_pp  /* <OF,len:num_members>
                  the pointer to the pointer to the array of the
                  tags of the loads and bc's.  If num_members is zero,
                  this pointer should not be used.  If num_members
                  is > 0, then this array must be freed by calling UF_free.
                  */
);

/***************************************************************************
Given the tag of a load case, this function finds the name of the load
case associated to the given tag.

Calls to this function should be replaced with appropriate calls to the
following functions:  UF_SF_solution_ask_name_nx, UF_SF_step_ask_name_nx.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_SF_ask_lbc_name(
tag_t  lbc_case ,/* <I>
                 Tag of the load case attached to name.
                 */
char* lbc_name  /* <O>
                Name of the load case.
                The maximum number of allowable
                characters is 24.
                */
);

/***************************************************************************
Given a load or boundary condition entity, this function finds the load
case or step load or bc belongs to.

Calls to this function should be replaced with appropriate calls to the
following functions:  UF_SF_ask_solution_nx, UF_SF_ask_step_nx.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_SF_ask_lbc_case(
tag_t  lbc_tag ,/* <I>
                Tag of the load or boundary condition.
                */
tag_t* lbc_case_tag  /* <O>
                     The tag of a load case or boundary condition
                     set.
                     */
);

/***************************************************************************
Given a name of a load case, this function finds the tag of the load
case associated to the given name.

Calls to this function should be replaced with appropriate calls to the
following functions:  UF_SF_locate_named_solution_nx, UF_SF_locate_named_step_nx.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_SF_locate_named_lbc_case(
char* lbc_name ,/* <I>
                Name of the load case
                The maximum name size is 24 characters.
                */
tag_t*  lbc_case  /* <O>
                  Tag of the load case attached to name.
                  */
);

/*************************************************************************
Creates a load case with a given name.

Calls to this function should be replaced with appropriate calls to the
following functions:  UF_SF_create_step_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/

extern UFUNEXPORT int UF_SF_create_load_case(
char* lbc_name ,/* <I>
                Name for the load case
                */
tag_t* lbc_case /* <O>
                 Tag for the load case
                 */
);

/*-----------------------------------------------------------------------------
Create a step definition in Abaqus env part file.

Calls to this function should be replaced with appropriate calls to the
following functions:  UF_SF_create_step_nx.

possible return error values are:

UF_SF_NON_ABAQUS_ENV - Non Abaqus environment
UF_SF_STEP_INVALID_NAME - Invalid Step Name
UF_SF_STEP_NAME_EXIST - Step Name already exist in the part

Environment: Internal  and  External

See Also:

History:
-----------------------------------------------------------------------------*/
extern UFUNEXPORT int  UF_SF_abaqus_create_step (
    char*   step_name,            /* <I> step name */
    int     number_of_increments, /* <I> number of increments */
    int     nlgeom,               /* <I> nonlinear gemetry = 0 FALSE
                                     = 1 TRUE */
    tag_p_t step_tag              /* <O> step tag */
);




/*------------------------------------------------------------------------
 *
 *   FUNCTION
 *      UF_SF_locate_all_load_groups
 *
 *   DESCRIPTION
 *       function to get all load groups.
 *
 *       Calls to this function should be replaced with appropriate calls to the
 *       following functions:  UF_SF_ask_num_solutions_nx, UF_SF_ask_nth_solution_nx,
 *       UF_SF_solution_ask_num_steps_nx, UF_SF_solution_ask_nth_step_nx.
 *
 *   INPUT
 *      int       *load_group_count
 *      tag_p_t   *load_group_tags
 *
 *   OUTPUT
 *      int       *load_group_count
 *      tag_p_t   *load_group_tags
 *
 *   RETURN
 *      int -   error 0 for success
 *                    1 for failure
 *
 *
 *------------------------------------------------------------------------*/
extern UFUNEXPORT int  UF_SF_locate_all_load_groups ( int     *load_group_count,  /*<O>*/
                                                      tag_p_t *load_group_tags    /*<OF,len:load_group_count>*/);


/*------------------------------------------------------------------------
 *
 *   FUNCTION
 *      UF_SF_locate_all_bc_groups
 *
 *   DESCRIPTION
 *       function find all the bc groups in the current scenario part
 *
 *       Calls to this function should be replaced with appropriate calls to the
 *       following functions:  UF_SF_ask_num_solutions_nx, UF_SF_ask_nth_solution_nx,
 *       UF_SF_solution_ask_num_steps_nx, UF_SF_solution_ask_nth_step_nx.
 *
 *   INPUT
 *       None
 *
 *   OUTPUT
 *       bc_group_count: number of load groups found in the current scenario part
 *       bc_group_tags:  pointer to the pointer to the array of the tag
 *                      for the load groups
 *                      MUST BE FREED IN THE CALLING ROUTING
 *   RETURN
 *                      Returns:              0(success) OR > 1(failure).
 *
 *   NOTE
 *       1) if bc_group_tags == 0; DON'T USE bc_group_tags pointer
 *       2) if bc_group_tags != 0; bc_group_tags MUST BE FREED IN CALLING
 *                                 ROUTINE
 *
 *------------------------------------------------------------------------*/
extern UFUNEXPORT int  UF_SF_locate_all_bc_groups (
                                                int     *bc_group_count, /*<O>*/
                                                tag_p_t *bc_group_tags   /*<OF,len:bc_group_count>*/
                                                  );
/*-----------------------------------------------------------------------------
Sets the current analysis language and analysis type.

Calls to this function should be replaced with calls to
UF_SFL_set_active_solution_and_step.

Environment: Internal  and  External

See Also:

History:
-----------------------------------------------------------------------------*/
extern UFUNEXPORT int UF_SF_set_cur_anl_lang (
char* language_name /* <I>
                     The name of the current language.  Must be a
                     char [UF_SF_LANG_MAX_NAME_LENGTH].
                     */
);

/*-----------------------------------------------------------------------------
Given a language name, returns the language tag. If not found,
returns NULL_TAG.  To find the current language, input
UF_SF_LANG_CURRENT.  If there is no current language, returns
NULL_TAG.

Calls to this function should be replaced with calls to
UF_SFL_ask_solution.

Environment: Internal  and  External

See Also:

History:
-----------------------------------------------------------------------------*/
extern UFUNEXPORT int UF_SF_locate_anl_lang(
const char* language_name ,/* <I>
                     The name the language.  Must be a char
                     [UF_SF_LANG_MAX_NAME_LENGTH].
                     */
tag_t* language_tag /* <O>
                     Tag to the found language.
                     */
);

/*-----------------------------------------------------------------------------
Returns the current analysis languages and analysis types. Note that
the num_languages output is not optional, there must always by the
pointer to the num_languages int passed in. This value will always be
passed back out.

Calls to this function should be replaced with calls to
UF_SFL_ask_num_languages and UF_SFL_ask_nth_language.

Environment: Internal  and  External

See Also:

History:
-----------------------------------------------------------------------------*/
extern UFUNEXPORT int UF_SF_ask_anl_langs (
int* num_languages ,/* <O>
                    The number of languages already defined.
                    NOTE: The current language is always the first in
                          the language_names_ptr array.
                    */
char*** language_names_ptr /* <OF,len:num_languages>
                           pointer to an array of character pointers
                           containing the language names. These must
                           be freed by calling UF_free_string_array.
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

/***************************************************************************
Given a loadcase or step this function sets the suppress state for the group.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_SF_suppress_lbc_group(
tag_t   lbc_case_tag, /* <I> Tag of the loadcase or step. */
logical suppressed    /* <I> = TRUE  - Suppress
                             = FALSE - Unsuppress
                     */
);

/*************************************************************************
Creates a load variation case with a given name.

Calls to this function should be replaced with calls to
UF_SF_create_dursol_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_create_lv_case(
char* lvc_name,  /* <I>
                        Name for the load variation case
                        */
tag_p_t lv_case        /* <O>
                        Tag for the load variation case
                        */
);

/*************************************************************************
Deletes a load variation case.

Environment: Internal  and  External

Calls to this function should be replaced with calls to
UF_SF_delete_dursol_nx.

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_delete_lv_case(
tag_t lv_case    /* <I>
                  Tag for the load variation case
                  */
);

/*************************************************************************
Edit a load variation case (name only).

Calls to this function should be replaced with calls to
UF_SF_edit_dursol_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_edit_lv_case(
tag_t lv_case,         /* <I>
                        Tag for the load variation case
                        */
const char* lvc_name   /* <I>
                        Name for the load variation case
                        */
);

/*************************************************************************
Returns the current load variation case tag and name.

Calls to this function should be replaced with calls to
UF_SF_ask_num_dursols_nx and UF_SF_ask_nth_dursol_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_ask_current_lv_case(
tag_p_t lv_case,        /* <O>
                        Tag for the load variation case
                        */
char** lvc_name        /* <OF>
                        Name for the load variation case
                        If *lvc_name != 0, must be freed
                        in the calling routine by calling UF_free.
                        */
);

/*************************************************************************
Returns the count and tags of all load variations associated with the
load variation case.

Calls to this function should be replaced with calls to
UF_SF_dursol_ask_load_count_nx and UF_SF_dursol_ask_load_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_locate_all_members_lv_case(
tag_t lv_case,        /* <I>
                        Tag for the load variation case
                        */
int* num_lv,           /* <O>
                        Number of load variations
                        */
tag_p_t*  lv_pp       /* <OF,len:num_lv>
                       pointer to the pointer to the array
                       of the tag for the load variations.
                       If num_lv != 0, must be freed
                       in the calling routine by calling UF_free.
                       */
);

/*************************************************************************
Deletes all load variations from the load variation case.

Calls to this function should be replaced with calls to
UF_SF_dursol_locate_all_members_nx and UF_SF_dursol_remove_load_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_delete_all_members_lv_case(
tag_t lv_case    /* <I>
                  Tag for the load variation case
                  */
);

/*************************************************************************
Creates a load variations and adds it to the load variation case.

Calls to this function should be replaced with calls to
UF_SF_create_lv_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_create_lv(
char* lv_name,         /* <I>
                        Load variation name
                        If lv_name = NULL, a default name will be assigned.
                        */
int num_cycles,  /* <I>
                  Number of load variation cycles
                  */
double scaling_factor, /* <I>
                        Scaling factor
                        */
int function_type,  /* <I>
                     Type of function to be assigned.
                       UF_SF_HALF_UNIT_CYCLE
                       UF_SF_FULL_UNIT_CYCLE
                     */
tag_t lbc_group,       /* <I>
                        Lbc group tag
                        */
tag_p_t lv_tag         /* <O>
                        Load variation tag
                        */
);

/*************************************************************************
Deletes load variation and removes from the load variation case.

Calls to this function should be replaced with calls to
UF_SF_delete_lv_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_delete_lv(
tag_t lv          /* <I>
                  Tag for the load variation
                  */
);

/*************************************************************************
Returns the information on a load variation.

Calls to this function should be replaced with calls to
UF_SF_ask_lv_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_ask_lv(
tag_t lv,               /* <I>
                         Tag for the load variation
                        */
char** lv_name,          /* <OF>
                         Load variation name
                         If NULL, name is NOT returned.
                         If lv_name != 0, name must be freed with UF_free
                        */
int* num_cycles,        /* <O>
                         Number of load variation cycles
                         If NULL, value is NOT returned
                         */
double* scaling_factor, /* <O>
                         Scaling factor
                         If NULL, value not returned
                        */
int* function_type,  /* <O>
                      Type of function to be assigned.
                        UF_SF_HALF_UNIT_CYCLE
                        UF_SF_FULL_UNIT_CYCLE
                      If NULL, value not returned.
                      */
tag_p_t lbc_group      /* <O>
                        Lbc group tag
                        If NULL, value not returned.
                        */
);

/*************************************************************************
Modifies the information on a load variation.

Calls to this function should be replaced with calls to
UF_SF_edit_lv_nx.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_SF_edit_lv(
tag_t lv,               /* <I>
                         Tag for the load variation
                         */
const char* lv_name,    /* <I>
                         Load variation name
                         If NULL, name is NOT modified.
                         */
int* num_cycles,        /* <I>
                         Number of load variation cycles
                         If NULL, value is NOT modified
                        */
double* scaling_factor, /* <I>
                         Scaling factor
                         If NULL, value not modified
                         */
int* function_type,  /* <I>
                      Type of function to be assigned.
                        UF_SF_HALF_UNIT_CYCLE
                        UF_SF_FULL_UNIT_CYCLE
                      If NULL, value not modified.
                      */
tag_t* lbc_group_tag  /* <I/O>
                       Tag of the LBC group
                       If NULL, value not modified
                       */
);

/* uc6570 create generic entity -- replaced by UF_UDOBJ_create_udo */
extern UFUNEXPORT int uc6570(int ip1, double *rp2, int ip3, int *ip4, int ip5, double *rp6,
                  int ip7, char cp8[][133], int ip9, tag_t *np10, tag_t *nr11);


/**************************************************************************
Create a load object on a single geometry object (point, edge/curve, face).

UF_SF_FAILED_TO_CREATE_LOAD for failed load creation

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
 ************************************************************************/
extern UFUNEXPORT int UF_SF_create_load_nx(
UF_SF_load_mode_t load_type ,/* <I>
                             Type of load to be created.
                              UF_SF_LOAD_FORCE
                              UF_SF_LOAD_DISTRIBUTED
                              UF_SF_LOAD_SPACIAL
                              UF_SF_LOAD_GRAVITY
                              UF_SF_LOAD_PRESSURE
                              UF_SF_LOAD_MOMENT
                              UF_SF_LOAD_SHEAR
                              UF_SF_LOAD_FLUX
                              UF_SF_LOAD_TEMPERATURE
                              UF_SF_LOAD_CENTRIFUGAL
                             */
tag_t geometry_tag ,/* <I>
                    Tag of the geometry object to be loaded
                    */
tag_t normal_face ,/* <I>
                   Tag of face object to be used with the
                   component_type option (otherwise use NULL_TAG)
                   */
tag_t along_edge ,/* <I>
                  Tag of edge object to be used with the
                  component_type option (otherwise use NULL_TAG)
                  */
UF_SF_LBC_component_type_t component_type ,/* <I>
                                           The option for orientation.
                                           Available options:
                                            UF_SF_LBC_XYZ,
                                            UF_SF_LBC_RTZ,
                                            UF_SF_LBC_RTp,
                                            UF_SF_LBC_NORMAL_TO,
                                            UF_SF_LBC_EDGE_CSYS
                                           */
double load_value[3] ,/* <I>
                      The load value
                      For Force, pressure, Moment, Gravity, and
                      Heat Flux use the edge component type:[0]
                      [1] [2] load vector.
                      For Unf. pressure,Edge Shear, Temperature,
                      Heat Flux use the edge component_type
                      [0] load scalar. [1] [2] is unused

                      Allowable combinations:

                       f = face
                       e = curve or edge
                       p = point
                       pa= part
                       b = body

                              \ Orientation component type
                  Neutral type \ | XYZ | RTZ | RTP | Norm to | Along Edge |
                                \|
                           Force | fep   fep   fep      f           e
                      Unf. Press |  -     -     -       f           -
                    Gravity Load |  pa    -     -       -           -
                        Pressure |  fe   fe    fe       -           -
                          Moment |  e    e      -       -           e
                      Edge Shear |  -    -      -       -           e
                     Temperature |  fep  -      -       -           -
                       Heat Flux |  fe   -      -       f           -

                      */
tag_t* load_tag /* <O>
                 Tag of the created load.
                 */
);


/**************************************************************************---
Create a bearing load object on a cylindrical face or a circular edge.

UF_SF_FAILED_TO_CREATE_LOAD for failed load creation

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
 ************************************************************************/
extern UFUNEXPORT int UF_SF_create_bearing_load_nx
(
tag_t geometry_tag,    /* <I> Tag of geometry object to be loaded */
double tot_load,       /* <I> Total bearing load value */
UF_SF_dist_type_t
           dist_type,  /* <I> Type of distribution
                                UF_SF_SINUSOIDAL (sinusoidal distribution)
                                UF_SF_PARABOLIC  (parabolic distribution)
                       */
double region_angle,   /* <I> Total region angle symmetric about the max load
                              line
                       */
tag_t vector,          /* <I> vector tag defining the direction and max load
                              line.  (Maximum load line will be the intersection
                              of vector from center point to the geometry.)
                       */
tag_p_t load_tag       /* <O> created load_tag */
);


/****************************************************************************
Queries bearing load entity attributes: geometry, load vector, load value,
region angle, and distribution type.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUNEXPORT int UF_SF_ask_bearing_load_nx(tag_t load_tag,  /* <I> Load tag */
                                  tag_t *geom_tag, /* <O> geometry */
                                  tag_t *vector,   /* <O> load vector */
                                  double *value,   /* <O> load value */
                                  double *region_angle,
                                                   /* <O> load angle */
                                  UF_SF_dist_type_t *dist_type
                                                   /* <O> distribution type */
                                 );

/*****************************************************************************
Queries the load entity attributes, load type, load class, load dimension,
load value components, and the update pending status.  If any of the
attributes are unneeded, simply pass a NULL for that structure pointer.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_SF_ask_load(
tag_t load_tag ,/* <I>
                Load tag to query.
                */
UF_SF_load_mode_t* load_mode_ptr ,/* <O>
                                  Type of load.
                                  */
UF_SF_load_class_t* load_class ,/* <O>
                                Class of load ( face, edge, part,
                                body or curve ).
                                */
UF_SF_LBC_component_type_t* component_type ,/* <O>
                                            The option for orientation
                                            */
UF_SF_load_dimension_t* dimension ,/* <O>
                                   Dimension of load ( Scalar, vector
                                                      or axis load.)
                                   */
logical*  upd_pend ,/* <O>
                    TRUE or FALSE for update pending.
                    */
int* num_values ,/* <O>
                 Number of  load value components.
                 */
double* value_array /* <O,len:num_values>
                     The load value
                     For Force, pressure, Moment, Gravity, and
                     Heat Flux using the edge component
                     type:[0] [1] [2] load vector.
                     For Unf. pressure,Edge Shear,
                     Temperature, Heat Flux using the edge
                     component_type
                      [1] [2]  un used
                     [0] load scalar
                     pass in array of size 3.  Read this array
                     depending on num_values.
                     */
);

/**************************************************************************
Edits a load object.

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUNEXPORT int UF_SF_edit_load(
tag_t load_tag ,/* <I>
                Tag of load to edit.
                */
double load_value[3] /* <I>
                      The load value
                      For Force, pressure, Moment, Gravity, and
                      Heat Flux using the edge component
                      type:[0] [1] [2] load vector.
                      For Unf. pressure,Edge Shear,
                      Temperature, Heat Flux using the edge
                      component_type
                       [1] [2]  un used
                      [0] load scalar
                      */
);




/******************************************************************************
Locates loads from either a mesh_geometry or the model
geometry.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_SF_locate_loads (
tag_t object_tag ,/* <I>
                  Tag of Object having load.
                  */
UF_SF_load_mode_t load_type ,/* <I>
                             The type of load.
                             */
int    *num_load, /* <O> number of loads */
tag_t** load_tag  /* <O,len:num_load>
                  Tag of the loads or NULL_TAG if not
                  found.
                  */
);

/******************************************************************************
Locates geometry affected by a Load.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_SF_locate_load_geom (
tag_t load_tag ,/* <I>
                Tag of load entity.
                */
int* geom_cnt ,/* <O>
              Number of geometry entities.
              */
tag_t** geometry_tag /* <OF,len:geom_cnt>
                      pointer to the array of geometric tags.
                      If geom_cnt > 0 then the caller must call UF_free
                      to free this array.
                     */
);


 /**************************************************************************
Creates a boundary condition object on a single geometry object
(point, edge/curve, face).

UF_SF_FAILED_TO_CREATE_CONSTRAINT for failed constraint creation

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
************************************************************************/
extern UFUNEXPORT int UF_SF_create_bc_nx(
UF_SF_bc_mode_t bc_type ,/* <I>
                         Type of boundary condition to be created:
                          UF_SF_BC_CONSTRAINT - Displacement/ Rotation
                          UF_SF_BC_DISPLACEMENT - Displacement
                          UF_SF_BC_ROTATION - Rotation
                          UF_SF_BC_TEMPERATURE-Temperature
                          UF_SF_BC_CONVECTION_COEFFICIENT
                          - Convection Coefficient
                         */
tag_t geometry_tag ,/* <I>
                    Tag of the geometry object to be constrained
                    */
tag_t normal_face ,/* <I>
                   Tag of face object to be used with the UF_SF_LBC_NORMAL_TO
                   and UF_SF_LBC_EDGE_CSYS component_type options
                   (otherwise use NULL_TAG)
                   */
tag_t along_edge ,/* <I>
                  Tag of edge object to be used with the UF_SF_LBC_EDGE_CSYS
                  component_type options (otherwise use NULL_TAG)
                  */
UF_SF_LBC_component_type_t compo ,/* <I>
                                  The orientation option.
                                    UF_SF_LBC_XYZ
                                    UF_SF_LBC_RTZ
                                    UF_SF_LBC_RTP
                                    UF_SF_LBC_NORMAL_TO
                                    UF_SF_LBC_EDGE_CSYS
                                  */
double bc_value[6] ,/* <I>
                    The boundary condition component  values.
                    Ambient temperature is defined for convection
                    coefficient.
                    Allowable combinations:

                      f = face
                      e = curve or edge
                      p = point


                                \ Orientation component type
                    Neutral type \ | XYZ | RTZ | RTP | Norm to | Along Edge |
                                  \|
                   Displace/Rotate | fep   fep   fep      f           e
                          Displace | fep   fep   fep      f           e
                            Rotate | fep   fep   fep      f           e
                       Temperature | fep    -     -       -           -
                      Conv. Coeff. | fep    -     -       -           -
                    */

tag_t* bc_tag /* <O>
               Tag of the created boundary condition  object
               */
);

/******************************************************************************
Queries the boundary condition entity attributes.  The bc_name and type,
bc_class, update pending status, component values, coordinate system and
component values.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_SF_ask_bc (
tag_t bc_tag ,/* <I>
              Tag of the boundary condition to get.
              */
UF_SF_bc_mode_t* bc_mode_ptr ,/* <O>
                              Load name and type, UF_SF_bc_mode_t
                              */
UF_SF_bc_class_t* bc_class_ptr ,/* <O>
                                class of boundary condition , UF_SF_bc_class_t
                                */
UF_SF_LBC_component_type_t* component_type ,/* <O>
                                            The option for orientation
                                            */
logical* update_pending ,/* <O>
                         TRUE or FALSE for bc update pending
                         */
int* num_of_values ,/* <O>
                    Number of components values
                    */
double* value_array /* <O,len:num_of_values>
                     The boundary condition component values. If value is
                     equal to UF_SF_FREE_VALUE then the corresponding dof
                     is left free.  pass in array of size six.
                     */
);

 /**************************************************************************
Edits a boundary condition object.

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUNEXPORT int UF_SF_edit_bc(
tag_t bc_tag ,/* <I>
              Tag of BC to edit.
              */
double bc_value[6] /* <I>
                    The boundary condition component values.
                    Ambient temperature is defined for
                    convection coefficient.
                    Assign value as UF_SF_FREE_VAL
                    UE for free degrees of freedom.
                    */
);

/*****************************************************************************
Locates geometry affected by a boundary condition.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_SF_locate_bc_geom (
tag_t bc_tag ,/* <I>
              Tag of BC entity.
              */
int* gem_cnt ,/* <O>
              Number of geometry entities.
              */
tag_p_t* geometry_tag /* <OF,len:gem_cnt>
                       pointer to the array of geometry tags.
                       If the number of geometry entities is > 0, then
                       UF_free must be called to free this array.
                       */
);


/******************************************************************************
Locates BCs from either a mesh_geometry or the model
geometry or the mesh_geometry would be linked to.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_SF_locate_bcs (
tag_t object_tag ,/* <I>
                Tag of the mesh geometry or model geometry entity.
                */
UF_SF_bc_mode_t bc_type ,/* <I>
                         The type of BC.
                         */
int   *num_bc,  /* <O>
                number of BC found */
tag_t** bc_tag /* <O,len:num_bc>
                Tag of the boundary condition .  Or
                NULL_TAG if not found.
                */
);


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


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING */
