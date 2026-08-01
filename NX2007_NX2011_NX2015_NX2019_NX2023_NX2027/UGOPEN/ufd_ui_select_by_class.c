/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_UI_select_by_class                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The example code program    *
 *   demonstrates how to use multiple selection by class. The selection class *
 *   is masked for lines, circles, conics, splines, and points.               *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_object_types.h>
#include <uf_disp.h>

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
int irc = 0;
char *message = "Select Objects";
UF_UI_selection_options_t opts;
UF_UI_mask_t mask[5] = {{UF_line_type, 0, 0},
                         {UF_circle_type, 0, 0},
                         {UF_conic_type, UF_all_subtype, 0},
                         {UF_spline_type, 0, 0},
                         {UF_point_type, 0, 0}};
int response, count;
tag_p_t objects;
int i;
int off = 0;
    
opts.other_options = 0;
opts.reserved = NULL;
opts.num_mask_triples = 5;
opts.scope = UF_UI_SEL_SCOPE_WORK_PART_AND_OCC;
opts.mask_triples = &mask[0];

/* set selection scope to be work part & occurrence */
irc = UF_UI_select_by_class( message,&opts,&response,&count,&objects );

 /* if no error, print information about selected objects */
if(!irc)
{
  printf("response= %d, object count= %d\n",response,count);
  /* fall through only if objects selected */
  if (objects != NULL)
  {
    for (i=0; i < count; i++)
    {
      printf("object tag= %d\n", objects[i]);
      /* unhighlight selected objects */
      UF_DISP_set_highlight(objects[i],off); 
    }
  }
}

UF_free(objects);

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
