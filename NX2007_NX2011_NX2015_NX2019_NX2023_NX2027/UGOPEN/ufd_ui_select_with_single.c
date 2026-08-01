/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_UI_select_with_single_dialog                                    *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example requires an open part. The exampe demonstrates presenting   *
 *   the single select dialog and using the initialization procedure to set   *
 *   the object type mask to only lines and edges.                            *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_object_types.h>
#include <uf_disp.h>

static int init_proc(UF_UI_selection_p_t select, 
                     void *user_data);

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
    char cue[] = "cue message";
    char title[] = "dialog title";
    int response;
    tag_t object, view;
    double cursor[3];


    if(!UF_CALL(UF_UI_select_with_single_dialog(cue,title,
                   UF_UI_SEL_SCOPE_NO_CHANGE, init_proc, NULL,
                   &response, &object, cursor, &view)))
    {
        if (response == UF_UI_OBJECT_SELECTED || 
            response == UF_UI_OBJECT_SELECTED_BY_NAME)
        {
            printf("object tag = %d\n", object);
            if (response == UF_UI_OBJECT_SELECTED)
            {
                printf("view = %d\n", view);
                printf("cursor position = %f %f %f\n", 
                        cursor[0], cursor[1], cursor[2]);
            }
        }
        /* unhighlight selected object */
        UF_DISP_set_highlight(object,0);
    }
}

/* selection initialization procedure */
static int init_proc(
    UF_UI_selection_p_t select,
    void* user_data)
{
    int num_triples = 2;
    UF_UI_mask_t mask_triples[] = {
         UF_line_type, 0, 0,
         UF_solid_type, 0, UF_UI_SEL_FEATURE_ANY_EDGE};

    /* enable only lines and edges */
    if((UF_CALL(UF_UI_set_sel_mask(select,
            UF_UI_SEL_MASK_CLEAR_AND_ENABLE_SPECIFIC,
            num_triples, mask_triples))) == 0)
    {
        return (UF_UI_SEL_SUCCESS);
    }
    else
    {
        return (UF_UI_SEL_FAILURE);
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
