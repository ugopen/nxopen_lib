/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_UI_set_sel_procs                                                *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example requires an open part. The example shows using a filter     *
 *   procedure with the single selection dialog to only select arcs of a      *
 *   certain radius and only select sheet bodies. Also, see the example for   *
 *   UF_UI_remove_from_sel_list which shows the use of a selection callback.  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_modl.h>
#include <uf_curve.h>
#include <uf_object_types.h>

static int init_proc(UF_UI_selection_p_t select,
                     void *user_data);
static int filter_proc(tag_t object, int type[3],
                       void *user_data,
                       UF_UI_selection_p_t select);

typedef struct user_data_s{
    double radius;
}user_data_t,*user_data_p_t;

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

    char cue[] = "Cue Message";
    char title[] = "Dialog Title";
    int response;
    tag_t object, view;
    double cursor[3];
    user_data_t data;

    data.radius = 1.5;
    /* Use single selection dialog with the scope set to the
       work part and use a filter procedure.
    */
    UF_CALL(UF_UI_select_with_single_dialog(
          cue, title, UF_UI_SEL_SCOPE_WORK_PART,
          init_proc, &data,
          &response, &object, cursor, &view));
}

/* initialization procedure */
static int init_proc(
    UF_UI_selection_p_t select,
    void *user_data)
{

    /* specify filter procedure for this dialog */
    if((UF_CALL(UF_UI_set_sel_procs(select,
                                    filter_proc,
                                    NULL,
                                    user_data))) == 0)
    {
        return (UF_UI_SEL_SUCCESS);
    }
    else
    {
        return (UF_UI_SEL_FAILURE);
    }
}


/* filter procedure */
static int filter_proc(
    tag_t object,
    int type[3],
    void *user_data,
    UF_UI_selection_p_t select)

{
    user_data_p_t data = (user_data_p_t)user_data;
    UF_CURVE_arc_t arc_data;
    int body_type;

    /* for arcs, filter on radius */
    if (type[0] == UF_circle_type)
    {
        UF_CALL(UF_CURVE_ask_arc_data(object,&arc_data));
        if (arc_data.radius > data->radius)
        {
            return (UF_UI_SEL_ACCEPT);
        }
        else
        {
            return (UF_UI_SEL_REJECT);
        }
    }
    /* for bodies, only accept sheet bodies */
    else if ((type[0] == UF_solid_type)  &&
              (type[1] == UF_solid_body_subtype))
    {
         UF_CALL(UF_MODL_ask_body_type(object,&body_type));
         if (body_type == UF_MODL_SHEET_BODY)
         {
             return (UF_UI_SEL_ACCEPT);
         }
         else
         {
             return (UF_UI_SEL_REJECT);
         }
    }
    else
    {
         return (UF_UI_SEL_ACCEPT);
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
