/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_PS_create_ps_trim                                               *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This program creates a cone and then creates trimmed curves for          *
 *   the edges of the cone.                                                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_ps.h>
#include <uf_view.h>

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
   char       * height = "10";
   char       * diam[] = {"5", "2"};
   tag_t        cone_feature_tag;
   tag_t        cone_tag;
   int          edge_count, i;
   uf_list_p_t  edges;
   tag_t        edge_id;
   tag_t        ps_curves[50];

   /*
       First create a part in which we will initially create a
       block.
   */
   UF_CALL(UF_PART_new( "trim_curve_test_part", UF_PART_ENGLISH , &part_tag ));  

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

   UF_CALL(UF_MODL_ask_body_edges( cone_tag, &edges ));

   UF_CALL(UF_MODL_ask_list_count(edges, &edge_count));

   for (i=0;i< edge_count;i++)
   {
        UF_CALL(UF_MODL_ask_list_item(edges,i,&edge_id));
        UF_CALL(UF_PS_create_ps_trimmed_curve(edge_id, &ps_curves[i]));
   }
   UF_CALL(UF_MODL_delete_list(&edges));

 return 0;
}
