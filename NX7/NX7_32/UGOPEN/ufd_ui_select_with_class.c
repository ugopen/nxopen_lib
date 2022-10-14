/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_UI_select_with_class_dialog                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *                                                                            *
 *   This example requires and open part and shows using the class selection  *
 *   dialog with all standard object types selectable. To set different       *
 *   object types selectable, see the example for                             *
 *   UF_UI_select_with_single_dialog.                                         *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_ui.h>
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
    char cue[] = "Select Objects";
    char title[] = "User Title";
    int response, count, i;
    tag_p_t objects;

    /* Use multiple class selection with scope set to any object
       in the work part and without using an initialization procedure.
    */
    if((UF_CALL(UF_UI_select_with_class_dialog(
          cue, title, UF_UI_SEL_SCOPE_WORK_PART,
          NULL, NULL, &response, &count, &objects))) == 0)
    {
         printf("object count = %d\n",count);
         if (response == UF_UI_OK && count > 0)
         {
             for (i=0; i<count; i++)
             {
                 printf("object tag = %d\n", objects[i]);
                 UF_DISP_set_highlight(objects[i], 0);
             }
             UF_free(objects);
         }
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
