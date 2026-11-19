/*===================================================================

        Copyright (c) 1996,1997 Electronic Data Systems Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_CURVE_create_silhouette                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example program creates a simple cone, then cycles through the      *
 *   canned UG views and creates silhouette curves from the solid.            *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/


#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_layout.h>
#include <uf_view.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_curve.h>
#include <uf_obj_types.h>

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


static int example1
(
   void
);

/*ARGSUSED*/
extern void ufusr(char *param, int *return_value, int paramLen)
{
    if (! UF_CALL(UF_initialize()))
    {
        *return_value = example1();
        UF_CALL(UF_terminate());
    }
}

/*--------------------------------------------------------------*/
static int example1(void)
 {
   tag_t        part_tag;
   double       origin_point[3];
   double       direction[3];
   double       scale_value;
   char       * height = "10";
   char       * diam[] = {"5", "2"};
   char         view_name[40]="\0";
   tag_t        cone_feature_tag;
   tag_t        cone_tag;
   tag_t        *curves;
   tag_t        view_tag;
   int          count;

   /* <JLM> 23-Apr-02 Fix constness */
   /*<Devansh Desai> : DES11050 :Refer to UF_OBJ_NAME_LEN instead of hard coded value */
   // +1 for null character
   static const char view_names[][ UF_OBJ_NAME_BUFSIZE ] = {"TOP", "FRONT", "TFR-TRI", "TFR-ISO"};

   /*
       First create a part in which we will initially create a
       cone.
   */
   UF_CALL(UF_PART_new( "uf_silhouette_test_part", UF_PART_ENGLISH , &part_tag ));  

   origin_point[0] = 0.0;
   origin_point[1] = 0.0;
   origin_point[2] = 0.0;

   direction[0] = 0.1;
   direction[1] = 0.2;
   direction[2] = 0.3;

   UF_CALL(UF_MODL_create_cone1( UF_NULLSIGN,
                          origin_point,
                          height,
                          diam,
                          direction,
                          &cone_feature_tag ));

   UF_CALL(UF_MODL_ask_feat_body( cone_feature_tag, &cone_tag ));

   /* 
      Create a 4 view layout
   */

   scale_value = 1.0;
   UF_CALL(uc6460("FourView",4,view_names,2, scale_value));

   /* Get the views in the current layout */
   
   for(uc6473("",view_name);strlen(view_name) != 0;uc6473("",view_name))
   {
      UF_CALL(UF_VIEW_ask_tag_of_view_name(view_name, &view_tag));
      UF_CALL(UF_CURVE_create_silhouette( cone_tag, view_tag, &count, &curves));
      UF_free(curves);
   }
 UF_CALL(UF_PART_save());
 return 0;
}
