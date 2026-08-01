/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_face_torus_type                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part with a torus. The code       *
 *   queries the type of the torus.                                           *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_ui.h>
#include <uf_obj.h>
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

  char *message = "Select Object";
  char errmsg[ MAX_LINE_BUFSIZE ];
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];
  UF_UI_selection_options_t opts;
  UF_UI_mask_t mask;
  int response, irc =0, off = 0, torus_type, ifail = 0;
  tag_t object, view;
  double cursor[3];
  
  opts.other_options = 0;
  opts.reserved = NULL;
  opts.num_mask_triples = 1;
  opts.mask_triples = &mask;

/* set up selectable type, subtype, solid type */
  opts.mask_triples->object_type = UF_solid_type;  
  opts.mask_triples->object_subtype = 0;
  opts.mask_triples->solid_type = UF_UI_SEL_FEATURE_TOROIDAL_FACE;

/* set selection scope to be work part */
  opts.scope = UF_UI_SEL_SCOPE_WORK_PART;
  irc = UF_UI_select_single(message,&opts,&response,
                          &object,cursor,&view);

/* if no error, get torus type and display type*/
  if (!irc)
  {
    ifail = UF_MODL_ask_face_torus_type ( object, &torus_type);
    UF_UI_open_listing_window();
    if (ifail)
    {
      UF_get_fail_message( ifail, errmsg);
      sprintf(buffer, "ERROR in ask torus type: %s\n", errmsg);
      UF_UI_write_listing_window(buffer);
    }
    else
    {
      switch(torus_type)
      {
        case UF_MODL_DOUGHNUT_TORUS:
          UF_UI_write_listing_window("The face is a doughnut torus.\n");
          break;
        case UF_MODL_APPLE_TORUS:
          UF_UI_write_listing_window("The face is an apple torus.\n");
          break;
        case UF_MODL_LEMON_TORUS:
          UF_UI_write_listing_window("The face is a lemon torus.\n");
          break;
        case UF_MODL_OSCULATING_APPLE_TORUS:
          UF_UI_write_listing_window("The face is an osculating torus.\n");
          break;
        default:
          UF_UI_write_listing_window("The face is not a torus.\n");
          break;
      }
    }
  /* unhighlight selected object */
    UF_DISP_set_highlight(object,off);
  }
  else  /* else get error message */
  {
    UF_get_fail_message(irc,errmsg);
    sprintf(buffer,"ERROR in single select: %s\n", errmsg);
    UF_UI_write_listing_window(buffer);
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
