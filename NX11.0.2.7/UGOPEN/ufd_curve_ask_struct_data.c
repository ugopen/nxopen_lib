/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CURVE_ask_curve_struct_data                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates temp.prt. The code creates a line and      *
 *   checks the data against the input values.                                *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf.h>
#include <uf_curve.h>
#include <uf_ui.h>
#include <uf_object_types.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char    messg[133];
        printf("%s, line %d:  %s\n", file, line, call);
        (UF_get_fail_message(irc, messg)) ?
            printf("    returned a %d\n", irc) :
            printf("    returned error %d:  %s\n", irc, messg);
    }
    return(irc);
}

static void do_ugopen_api(void)
{

  char prtnam[]={"temp"};
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];
  int english = 2;
  int curve_type;
  double  *curve_data;
  tag_t id;
  tag_t part_tag;
  UF_CURVE_struct_p_t curve;        
  
  UF_CURVE_line_t line;
  line.start_point[0] = 1.0;
  line.start_point[1] = 1.0;
  line.start_point[2] = 1.0;
  line.end_point[0] = 2.0;
  line.end_point[1] = 0.0;
  line.end_point[2] = 1.0;

  
  UF_CALL(UF_PART_new(prtnam,english,&part_tag));
  UF_CALL(UF_CURVE_create_line(&line, &id));
  UF_CALL(UF_CURVE_ask_curve_struct(id,&curve));
  UF_CALL(UF_CURVE_ask_curve_struct_data(curve,
                                         &curve_type,
                                         &curve_data));
  if(curve_type == UF_line_type)
  {
    UF_CALL(UF_UI_open_listing_window());
    sprintf(buffer,"\nStart Parameter, t0 = %f\n", curve_data[0]);
    UF_CALL(UF_UI_write_listing_window(buffer));
    sprintf(buffer,"The scale value, tscale = %f\n", curve_data[1]);
    UF_CALL(UF_UI_write_listing_window(buffer));
    sprintf(buffer,"The periodicity is: %f\n", curve_data[2]);
    UF_CALL(UF_UI_write_listing_window(buffer));
    sprintf(buffer, "The first point (x,y,z) is: %f, %f, %f\n",
            curve_data[3], curve_data[4], curve_data[5]);
    UF_CALL(UF_UI_write_listing_window(buffer));
    sprintf(buffer,"The second point (x,y,z) is: %f, %f, %f\n",
            curve_data[6],curve_data[7],curve_data[8]);
    UF_CALL(UF_UI_write_listing_window(buffer));
    
  }
  UF_CALL(UF_CURVE_free_curve_struct(curve)); 
  UF_free(curve_data);
}
/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
{
    if (!UF_CALL(UF_initialize()))
    {
        do_ugopen_api();
        UF_CALL(UF_terminate());
    }
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
