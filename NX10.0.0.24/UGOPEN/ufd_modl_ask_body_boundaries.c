/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_body_boudaries                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a part that contains a sheet body. This   *
 *   program uses UF_UI_select_single to get the body tag of the sheet body.  *
 *   Then, the program writes a report to the information window.             *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_disp.h>
#include <uf_modl.h>
#include <uf_ui.h>
#include <uf_object_types.h>

static void get_body_type(tag_t body);

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
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];

  double cursor[3];

  int err = 0, response =2;
  int num_bnd=0, *num_edges, i, count=0;

  UF_UI_selection_options_t opts;
  UF_UI_mask_t mask = {UF_solid_type,0,UF_UI_SEL_FEATURE_BODY};

  tag_t body, view, *edge_tags;

  opts.num_mask_triples = 1;
  opts.mask_triples = &mask;
  opts.scope = UF_UI_SEL_SCOPE_WORK_PART;
  

  UF_UI_open_listing_window();
  response = 4;
  do
  {
  err = UF_UI_select_single("Select a solid body", &opts,
                            &response, &body,
                            cursor, &view);

  if((response == 4) || (response == 5))
  {
    get_body_type(body);
  }

  if(!err && response !=1 && response !=2)
  {/* If there's no error and response is not CANCEL or BACK */

    UF_CALL(UF_MODL_ask_body_boundaries(body,&num_bnd,&num_edges,&edge_tags));

    if(num_bnd != 0)
    {
    
      for(i = 0; i < num_bnd; i++)
      {
        sprintf(buffer, "num_edges[%d] = %d\n", i, num_edges[i]);
        UF_UI_write_listing_window(buffer);
        count += num_edges[i];
      }
      sprintf(buffer,"\nThe total number of edges is: %d\n\n",count);
      UF_UI_write_listing_window(buffer);
      for(i = 0; i < count; i++)
      {
        sprintf(buffer, "edge_tags[%d] = %d\n", i, edge_tags[i]);
        UF_UI_write_listing_window(buffer);
      }
      UF_free(edge_tags);
      UF_free(num_edges);
      count = 0;
    }
    else
    {
      sprintf(buffer,"The number of boundaries was: %d\n",num_bnd);
      UF_UI_write_listing_window(buffer);

    }
  }
  UF_CALL(UF_DISP_set_highlight(body,0));
  }while((response == 4) || (response == 5));

}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
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

static void get_body_type(tag_t body)
{
  int err, type;
  char err_msg[ MAX_LINE_BUFSIZE ];
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];

  err = UF_MODL_ask_body_type(body,&type);
  if(err)
  {
    UF_get_fail_message(err,err_msg);
    sprintf(buffer, "ERROR in ask body type: %s\n", err_msg);
    UF_UI_write_listing_window(buffer);
  }
  else
  {
    switch(type)
    {
      case UF_MODL_SOLID_BODY:
        UF_UI_write_listing_window("\nThis is a solid body.\n");
        break;
      case UF_MODL_SHEET_BODY:
        UF_UI_write_listing_window("\nThis is a sheet body.\n");
        break;
      case 0:
        UF_UI_write_listing_window("\nThis was not a solid or sheet body.\n");
        break;
      default:
        UF_UI_write_listing_window("\nUnacceptable input, terminating...\n");
        break;
    }
  }
}
