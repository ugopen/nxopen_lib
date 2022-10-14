/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_datum_plane_parms                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example program requires an open part with a datum plane.  *
 *   The program acquires and prints out the parameters for the selected      *
 *   datum plane.                                                             *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_modl.h>
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

  char    *offset = NULL, *angle = NULL;
  tag_t   dplane, view, ftag; 
  int     i, error = 0, response = 2, zero = 0;
  double  cursor[3], origin[3], normal[3];

  UF_UI_selection_options_t opts;
  UF_UI_mask_t mask = {UF_datum_plane_type, 0, 0};
  
/* Only allow datum plane in the work part to be selectable */
  opts.num_mask_triples = 1;
  opts.mask_triples = &mask;
  opts.scope = UF_UI_SEL_SCOPE_WORK_PART;     

/* Ask to select a datum plane in displayed part to inquire on */
  error = UF_UI_select_single("Select a datum plane", &opts,
                              &response, &dplane, cursor, &view);
  
/* If there's no error & response is not CANCEL or BACK */
  if ( !error && response != 1 && response != 2 )
  {
     UF_CALL( UF_MODL_ask_object_feat(dplane, &ftag) );
     UF_CALL( UF_MODL_ask_datum_plane_parms(ftag, origin, normal,
                                         &offset, &angle));
       
     for (i=0;i<3;i++)
     { 
        printf("origin=%f, normal=%f\n",origin[i],normal[i]);
     }
     if(angle != NULL)
     {
        printf("angle = %s\n", angle);
     }
     if(offset != NULL)
     {
        printf("offset=%s\n",offset);
     }

     /* unhighlight selected plane */
     UF_CALL(UF_DISP_set_highlight(dplane,zero));
    
     UF_free(offset);
     UF_free(angle);

  }
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
