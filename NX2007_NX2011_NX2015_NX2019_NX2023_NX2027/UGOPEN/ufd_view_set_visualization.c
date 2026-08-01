/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_VIEW_set_visualization                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example assumes that you have a part loaded and that your current   *
 *   view is the TFR-TRI view. Hidden edges are changed to dashed.            *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_view.h>
#include <uf_ui.h>

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
  char *view_name = "TFR-TRI";
  UF_VIEW_visualization_t view_data;
  tag_t view_tag = NULL_TAG;

  /* Always retrieve the current display parameters before
     setting them. */
  UF_CALL(UF_VIEW_ask_visualization(view_tag, &view_data));

  /*  Set the new modes. */
  view_data.hidden_edge_mode = UF_VIEW_HIDDEN_EDGES_DASHED;
 
  /* Get the tag of the TFR-TRI view. */
  UF_CALL(UF_VIEW_ask_tag_of_view_name(view_name, &view_tag));

  /*  Write the new data to the database. */
  UF_CALL(UF_VIEW_set_visualization(view_tag, &view_data));
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
