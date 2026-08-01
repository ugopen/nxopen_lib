/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_UI_remove_from_sel_list                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example shows class selection with a selection callback. In the     *
 *   callback, if a face is deselected, all adjacent faces are also           *
 *   deselected. In addition, the selection callback terminates the dialog    *
 *   when a certain number of objects have been selected. This example        *
 *   requires an open part.                                                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_disp.h>
#include <uf_modl.h>
#include <uf_obj.h>
#include <uf_object_types.h>

typedef struct user_data_s{
    int max_count;
} user_data_t, *user_data_p_t;

static int init_proc(
    UF_UI_selection_p_t select,
    void *user_data);

static int sel_cb(
    int num_selected,
    tag_p_t objects,
    int num_deselected,
    tag_p_t deselected_objects,
    void *user_data,
    UF_UI_selection_p_t select);

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
    user_data_t data;

    /* initialize maximum number of entities to be selected */
    data.max_count = 25;

    /* call class selection dialog */
    if((UF_CALL(UF_UI_select_with_class_dialog(cue, title,
          UF_UI_SEL_SCOPE_WORK_PART, init_proc, &data,
          &response, &count, &objects))) == 0)
    {
        printf("object count = %d\n", count);
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

/*  initialization procedure */
static int init_proc(
    UF_UI_selection_p_t select,
    void *user_data)
{

    /* enable faces to be selectable */
    UF_UI_mask_t mask_triples[] = {
        UF_solid_type, 0, UF_UI_SEL_FEATURE_ANY_FACE};
    if(UF_CALL(UF_UI_set_sel_mask(select,
                             UF_UI_SEL_MASK_ENABLE_SPECIFIC,
                             1, mask_triples)))
    {   
        return (UF_UI_SEL_FAILURE);
    }

    /* specify selection callback */
    if((UF_CALL(UF_UI_set_sel_procs(select, 
                                    NULL,
                                    sel_cb,
                                    user_data))) == 0)
    {
        return (UF_UI_SEL_SUCCESS);
    }
    else
    {
        return (UF_UI_SEL_FAILURE);
    }
}

/* user selection callback 
   if a face was deselected, deselect all adjacent faces.
   when more than max_count objects have been selected,
   terminate the dialog */
static int sel_cb(
    int num_selected,
    tag_p_t objects,
    int num_deselected,
    tag_p_t deselected_objects,
    void *user_data,
    UF_UI_selection_p_t select)
{
    int type,subtype,i,j, count;
    tag_t face;
    logical in_list, unhilite = true;
    uf_list_p_t adj_faces;
    user_data_p_t data = (user_data_p_t)user_data;

    /* if objects were deselected */
    if (num_deselected > 0)
    {
        /* loop over deselected objects */
        for (i=0; i<num_deselected; i++)
        {
            /* if object is a face */
            UF_OBJ_ask_type_and_subtype  
                  (deselected_objects[i],&type,&subtype);
            if (type == UF_solid_type && 
                subtype == UF_solid_face_subtype)
            {
                /* get all adjacent faces */
                UF_MODL_ask_adjac_faces(deselected_objects[i],
                                        &adj_faces);
                UF_MODL_ask_list_count(adj_faces,&count);

                /* remove the adjacent faces from the selection 
                   list and turn off their highlighting */
                for (j=0; j<count; j++)
                {
                     UF_MODL_ask_list_item(adj_faces,j,&face);
                     if (face != NULL_TAG)
                     {
                         UF_UI_is_object_in_sel_list
                              (select,face,&in_list);
                         if (in_list)
                         {
                             UF_UI_remove_from_sel_list
                                (select,1,&face,unhilite);
                         }
                      }
                 }
                 UF_MODL_delete_list(&adj_faces);
             }
         }
    }
    /* else if objects selected, check max count */
    else if (num_selected > 0)
    {
        /* ask the number of objects currently selected */
        if((UF_CALL(UF_UI_ask_sel_list_count(select, &count))) == 0)
        {
            /*exit dialog if maximum number of objects have been 
              selected */
            if (count > data->max_count)
            {
                return (UF_UI_CB_EXIT_DIALOG);
            }
        }
    }

    return (UF_UI_CB_CONTINUE_DIALOG);
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
