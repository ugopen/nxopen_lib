/* 
===============================================================================

             Copyright (c) 1997-1999 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

===============================================================================

File description:
  
   This file contains the application portion of the Associate Notes demo.
   The file contains the dialog routine to create and 
   edit the note/view association. The bodies of each UDO methods and various
   support routines enable the user to link the note with the view.  The 
   code in this file should be compiled-linked into a shared image and
   placed in the "application/" directory.
   
   The public entry point is ufsta.

   Attention Windows/NT users.  To link this as a dll you will need to 
   provided the location of the ufx_udo_methods.lib which provides the 
   DllExport functions bodies.  Simply add the ufx_udo_methods.lib to the 
   link line.

 *
 *===========================================================================
*/

/* Include files */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <uf.h>
#include <uf_disp.h>
#include <uf_obj.h>
#include <uf_ui.h>
#include <uf_mb.h>
#include <uf_drf.h>
#include <uf_draw.h>
#include <uf_exit.h>
#include <uf_udobj.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_object_types.h>
#include <ufx_udo.h>

/* User actions from the main menu dialog  */
#define UFX_UDO_CREATE             1
#define UFX_UDO_ADD_NOTE           2
#define UFX_UDO_DELETE_NOTE        3
#define UFX_UDO_CANCEL             4

/* The class id for creation of the UDO around the view borders */
static unsigned int UFX_UDO_border_class = 0;

static char ERR_msg[133];

/* These are static variables which are set to values obtained at 
   startup.  They are set by UFX_UDO_ask_all_view_data_dll */
static UFX_UDO_view_info_p_t UFX_UDO_view_info_array;
static int UFX_UDO_view_num;


/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_create_main_menu
 *
 *
 *  DESCRIPTION:  Puts up a dialog which ask the user to
 *                enter
 *                    1 Create an association of a view and note
 *                    2 Add a new note
 *                    3 Remove a note from its association with the view
 *                    4 quit via cancel or back
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_create_main_menu(
int *response    /* The response 1 thru 4 */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_initialize
 *
 *
 *  DESCRIPTION:  Must be called once per execution of a ufusr program.
 *                and must be called prior to calling any other EXAMPLE
 *                function . 
 *                One exeception is the UFX_UDO_create_main_menu which
 *                puts up the menu in a dialog and then calls this function
 *
 *
 ****************************************************************************/
static void UFX_UDO_initialize ( void);

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_create_new_udo
 *
 *
 *  DESCRIPTION:  Creates a new udo to associate with each view and
 *                series of notes. The udo is then coupled with the
 *                views tag via the UDO link mechanism
 *
 *
 *
 ****************************************************************************/

static void UFX_UDO_create_new_udo(void);

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_add_notes_to_udo
 *
 *
 *  DESCRIPTION:  This function ask the user to add notes to the
 *                selected view.  Attention points are placed on those
 *                notes which are already associated with the view.
 *                After the user selects the notes to associate with the
 *                view the notes are added to the UDO links
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_add_notes_to_udo(void);

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_delete_notes_from_udo
 *
 *
 *  DESCRIPTION:  Ask the user to select notes to remove form association
 *                with the view. The note is then removed from the UDO
 *                link mechanism.
 *
 *
 ****************************************************************************/
static void UFX_UDO_delete_notes_from_udo(void);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_terminate
 *
 *
 *  DESCRIPTION: Must be called prior to termination of the
 *               use of this package
 *
 *
 ****************************************************************************/
static void UFX_UDO_terminate ( void);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_ask_view_from_user
 *
 *
 *  DESCRIPTION:  Ask all view info by putting up a dialog to inquire
 *                the view and note information.  Return a pointer to
 *                the view structure selected. Returns true if the
 *                user selected a view and false if the user is quiting.
 *
 *
 ****************************************************************************/
static logical UFX_UDO_ask_view_from_user(
UFX_UDO_view_info_p_t *view_array    /* O  - the view array pointer */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_highlight_view
 *
 *
 *  DESCRIPTION:  Highlights the view just selected.  This routine
 *                must be called after the UFX_UDO_ask_view_from_user
 *                as it requires the view array.
 *
 *
 ****************************************************************************/
static void UFX_UDO_highlight_view(
UFX_UDO_view_info_p_t view_array    /* I  - the view array pointer */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_select_a_note
 *
 *
 *  DESCRIPTION: Selects a note by presenting a dialog.
 *               Returns 1 or 2 for back or cancel and 3 for the note was
 *               selected
 *
 *
 ****************************************************************************/
static int UFX_UDO_select_a_note(
tag_p_t note_tag              /* O The tag selected */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_deselect_note
 *
 *
 *  DESCRIPTION:  Turns off the highlighting of the note when done with
 *                the selection
 *
 *
 ****************************************************************************/
static void UFX_UDO_deselect_note(
tag_t note_tag      /* I The note to deselect */
);

static void create_udo_and_reg(
int view_num                 /* I The max number of views allowed in array */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_confirm_1
 *
 *
 *  DESCRIPTION: Pop up a error warning dialog
 *
 *
 ****************************************************************************/
static void UFX_UDO_confirm_1(
char *confirm                /* I    -- The message to show on the dialog */
);

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_atten_pt_note
 *
 *
 *  DESCRIPTION:   Puts an attention point at the note coordinates
 *
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_atten_pt_note(
tag_t note_tag  /* I The tag of the note */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_deselect_all_views
 *
 *
 *  DESCRIPTION: de highlights all  views
 *
 *
 ****************************************************************************/
static void UFX_UDO_deselect_all_views(
UFX_UDO_view_info_p_t view_array ,   /* I - the view array */
int num_entries              /* I - the number of valid entries */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_select_a_view
 *
 *
 *  DESCRIPTION: Selects a view by presenting a dialog.  Adds the view
 *               to the view array Returns a true if the user selected
 *               a view and false if nothing was selected.
 *
 *
 *
 ****************************************************************************/
static logical UFX_UDO_select_a_view(
   UFX_UDO_view_info_p_t view_array,     /* I The view array */
   int view_numb,                /* I The total number in the view array */
   int *view_entry_selected      /* O The entry in the view array selected */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_make_udo_selectable_cb
 *
 *
 *  DESCRIPTION:  A callback to be registered for the udo which makes the
 *                udo selectable. The udo consists of four lines
 *                drawn on top of the view borders.  This gives the illusion
 *                of selecting a view via class selection.
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_make_udo_selectable_cb(
tag_t udo,          /* I The udo to make selectable */
void *context       /* I The context pointer obtained from the callback */
);

static UF_MB_cb_status_t  ug_demo_assoc_notes( UF_MB_widget_t w, UF_MB_data_t client_data, 
                                  UF_MB_activated_button_p_t button);                      

static UF_MB_action_t actionTable[] =
{
    { "ug_demo_assoc_notes", (UF_MB_callback_t)ug_demo_assoc_notes, NULL },
    { NULL, NULL, NULL}
};


/*****************************************************************************
 * ufsta is a new user exit added for the User Function Custom Application 
 * project. This user exit is activated when the environment variable 
 * USER_STARTUP is defined. USER_STARTUP must point to the path of the user
 * function that you want to execute, and this user function program must 
 * have the ufsta entry.
 *
 * For example: export USER_STARTUP=/ui1/ui_v104/ufun_test/mult_ufsta.hpp
 *
*****************************************************************************/
/*ARGSUSED*/
extern void ufsta( char *param, int *ret_code, int rlen)
{  int irc ;
   irc = UF_initialize();
   if (irc != 0) fprintf(stderr,"Ufsta failed to initialize \n");
   irc = UF_MB_add_actions( actionTable);
   if (irc != 0) fprintf(stderr,"Ufsta failed in UF_MB_add_actions \n");
   irc = UF_terminate();
   if (irc != 0) fprintf(stderr,"Ufsta failed to terminate  \n");
}                                                 

/*****************************************************************************
* ug_demo_assoc_notes()
*
* This callback is executed when View->Associate Notes... is chosen
*****************************************************************************/
static UF_MB_cb_status_t  ug_demo_assoc_notes( UF_MB_widget_t w, UF_MB_data_t client_data, 
                                  UF_MB_activated_button_p_t button)                      
{
       int response;

/*  
    Loop for user to choose: 1) Create UDO, 
                             2) Add note to UDO,    
                             3) Delete note from a UDO,
                             4) Exit
*/

  /* Always initialize even if it has been done before 
     as so other uf program may have UF_terminated by mistake */
  response = UF_initialize();
  if (response != 0)
  {
       UF_get_fail_message(response,ERR_msg);
       fprintf(stderr, "UF_initialize %s \n", ERR_msg);
       return UF_MB_CB_ERROR ;
  }
    UF_UI_lock_ug_access ( UF_UI_FROM_CUSTOM );
/*  Initialize the demo functions here so that info object is available */
        UFX_UDO_initialize();
        UFX_UDO_create_main_menu(&response);
        while(UFX_UDO_CANCEL != response)
        {

            switch(response)
            {
            case UFX_UDO_CREATE:
                UFX_UDO_create_new_udo();
                break;
            case UFX_UDO_ADD_NOTE:
                UFX_UDO_add_notes_to_udo();
                break;
            case UFX_UDO_DELETE_NOTE:
                UFX_UDO_delete_notes_from_udo();
                break;
            default:
                printf( "UFX_UDO_ask_input: return wrong result.\n");
            }
        UF_DISP_refresh();
        UFX_UDO_terminate();
            UFX_UDO_initialize();
            UFX_UDO_create_main_menu(&response);
        }

    UFX_UDO_terminate();

    UF_UI_unlock_ug_access ( UF_UI_FROM_CUSTOM );

    response = UF_terminate();
    if (response != 0)
    {
       UF_get_fail_message(response,ERR_msg);
       fprintf(stderr, "UF_terminate %s \n", ERR_msg);
       return UF_MB_CB_ERROR ;
    }
    return ( UF_MB_CB_CONTINUE );
}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_create_main_menu
 *
 *
 *  DESCRIPTION:  Puts up a dialog which ask the user to 
 *                enter 
 *                    1 Create an association of a view and note
 *                    2 Add a new note 
 *                    3 Remove a note from its association with the view
 *                    4 quit via cancel or back
 *                
 *
 *
 ****************************************************************************/
static void UFX_UDO_create_main_menu(
int *response    /* The response 1 thru 4 */
)
{
   char menu_title[] = {"Action Menu"};
   char menu_items[3][38] ={ "Create view/note association",
                              "Add new notes to a view ",
                              "Remove notes from its view"};
   int menu_items_num = 3, resp;
   
   resp = uc1603(menu_title,0, menu_items,menu_items_num);
   switch (resp)
   {
       case 1:
       case 2:
          *response = 4; 

       break;
       case 5:
       case 6:
       case 7:
          *response = resp - 4;
       break;
       default:
          *response = 4;
       break;
   }
                               
}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_create_new_udo
 *
 *
 *  DESCRIPTION:  Creates a new udo to associate with each view and
 *                series of notes. The udo is then coupled with the
 *                views tag via the UDO link mechanism
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_create_new_udo(void)
{
UFX_UDO_view_info_p_t    view_info=NULL;
tag_t         part_tag = UF_ASSEM_ask_work_part();
tag_t          udo_tag;
int             error;

/*  get a view and assicated notes, then create a udo */
    while(UFX_UDO_ask_view_from_user(&view_info))
    {
    int num_links,num_notes=0,tmp_num_notes=0,i;
    UF_UDOBJ_link_p_t link_defs=NULL;
    double view_center[3];
    tag_t  *notes_array=NULL,*tmp_note_array=NULL,note_tag;
    tag_t  next_tag=NULL_TAG;

    /* highlight the selected view */
    UFX_UDO_highlight_view(view_info);

    /* check if the view already have a udo associate with it */
            UF_OBJ_cycle_objs_in_part(part_tag,UF_user_defined_object_type,
                                      &next_tag);
        while ((next_tag) != NULL_TAG)
        {
                UF_UDOBJ_all_data_t   udo_data;
                UF_UDOBJ_ask_udo_data(next_tag,&udo_data);
                if((udo_data.class_id == UFX_UDO_get_note_vw_class()) && 
                   (udo_data.link_defs[0].assoc_ug_tag==view_info->view_tag))
                {
                    /* recreate the association */
                    UF_OBJ_delete_object(next_tag);
                    UF_UDOBJ_free_udo_data(&udo_data);
                    break;
                        
                }
                UF_UDOBJ_free_udo_data(&udo_data);
                UF_OBJ_cycle_objs_in_part(part_tag,
                      UF_user_defined_object_type,
                                          &next_tag);
        }

    

      /* get notes associate with the view */
        while(UFX_UDO_select_a_note(&note_tag)==3) /* a note is selected */
        {
        num_notes++;
        if(notes_array==NULL)
        {
            notes_array = (tag_t *)malloc(sizeof(tag_t));
            notes_array[0] = note_tag;
        }
        else
        {
            notes_array = (tag_t *)malloc(sizeof(tag_t)*num_notes);
            if(notes_array!=NULL && tmp_note_array!=NULL)
            {
                memcpy(notes_array,tmp_note_array,
                    sizeof(tag_t)*(tmp_num_notes));
            }
            notes_array[tmp_num_notes]=note_tag;
            free(tmp_note_array);
        }
        tmp_note_array = notes_array;
        tmp_num_notes = num_notes;
        }

      /* deselect notes */
        for ( i = 0; i < num_notes; i++)
        UFX_UDO_deselect_note(notes_array[i]);
        UF_DISP_refresh();
            
          /* then create a udo */
        UF_UDOBJ_create_udo(UFX_UDO_get_note_vw_class(), &udo_tag);
        if(NULL_TAG == udo_tag)
        {
        printf( "The udo was not created successfully.\n");
        return;
        }

          /* associate the view and its related notes to the new udo */
        num_links = num_notes+1;
        link_defs = (UF_UDOBJ_link_p_t) 
        malloc(sizeof(UF_UDOBJ_link_t)*num_links);
        if ( NULL == link_defs)
        {
        printf( "Allocation of memory for link_defs is failed.\n");
        return;
        }
        link_defs[0].assoc_ug_tag = view_info->view_tag;
            link_defs[0].link_type = 1;
        for( i = 0; i < num_notes; i++)
        {
        link_defs[i+1].assoc_ug_tag=notes_array[i];
        link_defs[i+1].link_type = 3;
        }
        error = UF_UDOBJ_add_links(udo_tag, num_links, link_defs);
            if( error )
            {
                printf( "The links were not added to udo successfully.\n");
                return;
            }
        free(link_defs);
        free(notes_array);

    /* add original view center to the udo */
        UFX_UDO_ask_view_center_dll(view_info->view_tag,view_center);
            error = UF_UDOBJ_add_doubles(udo_tag, 3, view_center);
            if( error )
            {
                printf( "The view center not added to udo successfully.\n");
                return;
            }

    }  /* while */

}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_initialize
 *
 *
 *  DESCRIPTION:  Must be called once per execution of a ufusr program.
 *                and must be called prior to calling any other DEMO
 *                function
 *
 *
 ****************************************************************************/
static void UFX_UDO_initialize ( void)
{
  int irc;
  char drawing_name[ UF_OBJ_NAME_BUFSIZE ];
  int i,  units, units_drw,size ;
  tag_t  work_part_tag = UF_ASSEM_ask_work_part();
  double size_pos[3];


  irc = uc6492(drawing_name);
  if (irc != 0)
  {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "uc6492 %s \n", ERR_msg);
       return;
  }
  if (strcmp(drawing_name,"") == 0)
  {
      fprintf(stderr,"No drawing Active \n");
      return;
  }


  /* Get units of the part */
  UF_PART_ask_units(work_part_tag, &units);   

  /* Convert drawings which are in different units than the part */
  /* For example metric drawings in an english part */
  irc = uc6479("",&units_drw,&size,size_pos);
  if (irc != 0) 
  {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "uc6479 %s \n", ERR_msg);
  }
  /* Make the units corresponde with part definitions of units */
  if (units_drw == 1)
      units_drw = 2;
  else
      units_drw = 1;

  if (units_drw != units )
  {
      /* Part is in inches but drawing in metric */
      if (units == 1)
      {
          UFX_UDO_set_Metric(25.4);

      }
      else
          UFX_UDO_set_Metric(1.0/25.4);
      
  }
  else
  {
     UFX_UDO_set_Metric(1.0);
  }

  /* Find all the views on the drawing */
  UFX_UDO_ask_all_view_data_dll(&UFX_UDO_view_info_array,&UFX_UDO_view_num);


  /* Register the methods and create the udos */
  create_udo_and_reg(UFX_UDO_view_num);

  for (i =0; i <UFX_UDO_view_num; i++)
  {
       /* Regen the udo associated with the view */
       UF_DISP_add_item_to_display(UFX_UDO_view_info_array[i].udo_tag);
  }
 

}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_add_notes_to_udo
 *
 *
 *  DESCRIPTION:  This function ask the user to add notes to the 
 *                selected view.  Attention points are placed on those
 *                notes which are already associated with the view.
 *                After the user selects the notes to associate with the 
 *                view the notes are added to the UDO links
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_add_notes_to_udo(void)
{

UFX_UDO_view_info_p_t    view_info=NULL;
tag_t         part_tag = UF_ASSEM_ask_work_part();
int             error;
char *confirm_1 = "This view is not associated with any notes.\n";
char *confirm_2 = "This note already associate with the view.\n";

/*  get a view and assicated notes, then create a udo */
    while(UFX_UDO_ask_view_from_user(&view_info))
    {
    int num_links,tmp_num_notes=0;
    unsigned int i, num_notes = 0;
    UF_UDOBJ_link_p_t link_defs=NULL;
    tag_t  *notes_array=NULL,*tmp_note_array=NULL,note_tag;
    tag_t  next_tag=NULL_TAG,udo_tag=NULL_TAG;
    UF_UDOBJ_all_data_t   udo_data = {0};

    /* highlight the selected view */
        UFX_UDO_highlight_view(view_info);

    /* check if the view already have a udo associate with it */
            UF_OBJ_cycle_objs_in_part(part_tag,UF_user_defined_object_type,
                                      &next_tag);
        while ((next_tag) != NULL_TAG)
        {
                UF_UDOBJ_ask_udo_data(next_tag,&udo_data);
                if((udo_data.class_id == UFX_UDO_get_note_vw_class()) && 
                   (udo_data.link_defs[0].assoc_ug_tag==view_info->view_tag))
                {
                    udo_tag = next_tag;
                        break;
                }
                UF_UDOBJ_free_udo_data(&udo_data);
                UF_OBJ_cycle_objs_in_part(part_tag,
                      UF_user_defined_object_type,
                                          &next_tag);
        }

            /* if the input view is not associated with any udo, return */
            if(NULL_TAG == udo_tag)
            {
                UFX_UDO_confirm_1(confirm_1);
                return;
            }
    
    /* Puts attention points on the notes that already associated with
        the input view */
        for ( i = 1; i<udo_data.num_links; i++)
        UFX_UDO_atten_pt_note(udo_data.link_defs[i].assoc_ug_tag);

      /* get notes associate with the view */
        while(UFX_UDO_select_a_note(&note_tag)==3) /* a note is selected */
            {
        /* Check if the picked note already associated with the view */
        int bad_note = false;
        for (i=1;i<udo_data.num_links;i++)
        {
            if(udo_data.link_defs[i].assoc_ug_tag==note_tag)
            {
            UFX_UDO_confirm_1(confirm_2);
                UFX_UDO_deselect_note(note_tag);
                bad_note = true;
            }
        }

        if(bad_note) continue;
                num_notes++;
                if(notes_array==NULL)
                {
                    notes_array = (tag_t *)malloc(sizeof(tag_t));
                    notes_array[0] = note_tag;
                }
                else
                {
                    notes_array = (tag_t *)malloc(sizeof(tag_t)*num_notes);
                    if(notes_array!=NULL && tmp_note_array!=NULL)
                    {
                        memcpy(notes_array,tmp_note_array,
                                       sizeof(tag_t)*(tmp_num_notes));
                    }
                    notes_array[tmp_num_notes]=note_tag;
                    free(tmp_note_array);
                }
                tmp_note_array = notes_array;
                tmp_num_notes = num_notes;
            }

  
      /* deselect notes */
        for ( i = 0; i < num_notes; i++)
        UFX_UDO_deselect_note(notes_array[i]);
        UF_DISP_refresh();

          /* associate the view and its related notes */
        num_links = num_notes+1;
        link_defs = (UF_UDOBJ_link_p_t) 
        malloc(sizeof(UF_UDOBJ_link_t)*num_links);
        if ( NULL == link_defs)
        {
        printf( "Allocation of memory for link_defs is failed.\n");
        return;
        }
        for( i = 0; i < num_notes; i++)
        {
        link_defs[i].assoc_ug_tag=notes_array[i];
        link_defs[i].link_type = 3;
        }
        error = UF_UDOBJ_add_links(udo_tag, num_notes, link_defs);
            if( error )
            {
                printf( "The links were not added to udo successfully.\n");
                return;
            }
        free(link_defs);
        free(notes_array);


    }  /* while */

}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_delete_notes_from_udo
 *
 *
 *  DESCRIPTION:  Ask the user to select notes to remove form association
 *                with the view. The note is then removed from the UDO
 *                link mechanism.
 *               
 *
 ****************************************************************************/
static void UFX_UDO_delete_notes_from_udo(void)
{

UFX_UDO_view_info_p_t    view_info=NULL;
tag_t         part_tag = UF_ASSEM_ask_work_part();
UF_UDOBJ_link_t deleted_link;
UF_UDOBJ_all_data_t   udo_data = {0};
char *confirm_1 = "This view is not associated with any notes.\n";
char *confirm_2 = "This note is not associated with the view.\n";
char *confirm_3 = "This note has been selected to be deleted from the view.\n";

    while(UFX_UDO_ask_view_from_user(&view_info)) /* get a view */
    {
    unsigned int num_notes=0,i;
    UF_UDOBJ_link_p_t link_defs=NULL;
    tag_t  *notes_array=NULL,*tmp_note_array=NULL,note_tag;
    tag_t  next_tag=NULL_TAG,udo_tag=NULL_TAG;

    /* highlight the selected view */
    UFX_UDO_highlight_view(view_info);

    /* check if the view already have a udo associate with it */
            UF_OBJ_cycle_objs_in_part(part_tag,UF_user_defined_object_type,
                                      &next_tag);
        while ((next_tag) != NULL_TAG)
        {
                UF_UDOBJ_ask_udo_data(next_tag,&udo_data);
                if((udo_data.class_id == UFX_UDO_get_note_vw_class()) && 
                   (udo_data.link_defs[0].assoc_ug_tag==view_info->view_tag))
                {
                    udo_tag = next_tag;
                    break;
                }
                UF_UDOBJ_free_udo_data(&udo_data);
                UF_OBJ_cycle_objs_in_part(part_tag,
                      UF_user_defined_object_type,
                                          &next_tag);
            }

            /* if the input view is not associated with any udo, rechoose */
            if(NULL_TAG == udo_tag)
            {
                UFX_UDO_confirm_1(confirm_1);
                continue;
            }
    
    /* Puts attension points on the notes that already associated with
        the input view */
        for ( i = 1; i<udo_data.num_links; i++)
        UFX_UDO_atten_pt_note(udo_data.link_defs[i].assoc_ug_tag);


            /* get notes associate with the view */
        while(UFX_UDO_select_a_note(&note_tag)==3) /* a note is selected */
            {
                tag_t delete_tag = NULL_TAG;
                /* Check if the selected note associates with
                   selected view */
                for( i=1; i<udo_data.num_links; i++)
                {
                    if(note_tag == udo_data.link_defs[i].assoc_ug_tag)
                        delete_tag = note_tag;
                }
                if( NULL_TAG == delete_tag )/* the note not associate */
                {                           /* with the selected view */
                    UFX_UDO_confirm_1(confirm_2);
            UFX_UDO_deselect_note(note_tag);
                    continue;
                }

                if(notes_array==NULL)
                {

                    /* allocate memory */
                    notes_array = (tag_t *)malloc(sizeof(tag_t));
                    notes_array[0] = note_tag;
                    tmp_note_array = notes_array;
                    num_notes++;
                }
                else
                {

                   /* Check if the selected note has been seleted */
                   for ( i=0; i<num_notes; i++)
                   {
                       if ( note_tag == notes_array[i] )
                       {   /* the selected note has been selected */
                           UFX_UDO_confirm_1(confirm_3);
                           continue;
                       }
                   }

                   notes_array = (tag_t *)malloc(sizeof(tag_t)*(num_notes+1));
                   if(notes_array!=NULL && tmp_note_array!=NULL)
                   {
                        memcpy(notes_array,tmp_note_array,
                                       sizeof(tag_t)*(num_notes));
                   }
                   notes_array[num_notes]=note_tag;
                   free(tmp_note_array);
                   tmp_note_array = notes_array;
                   num_notes++;
                }  /* else */
            }      /* while select note */

  
      /* deselect notes */
        for ( i = 0; i < num_notes; i++)
        UFX_UDO_deselect_note(notes_array[i]);
        UF_DISP_refresh();

          /* delete notes */

        for( i = 0; i < num_notes; i++)
        {
        deleted_link.assoc_ug_tag=notes_array[i];
        deleted_link.link_type = 3;
            UF_UDOBJ_delete_link(udo_tag, &deleted_link);
        }
        free(link_defs);
        free(notes_array);
    }  /* while */

}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_terminate
 *
 *
 *  DESCRIPTION: Must be called to termination  use of this  
 *               of this package.
 *
 *
 ****************************************************************************/
static void UFX_UDO_terminate ( void)
{

    int  irc;

    /* Turn off highlighting then delete the udos */
    UFX_UDO_deselect_all_views(UFX_UDO_view_info_array,UFX_UDO_view_num);
    
    /* De register the classes */
    irc = UF_UDOBJ_register_attn_pt_cb(UFX_UDO_border_class,
                                             NULL);
    if (irc != 0) 
    {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "UF_UDOBJ_register_attn_pt_cb %s \n", ERR_msg);
    }
    irc = UF_UI_delete_from_class_sel(UFX_UDO_border_class);
    if (irc != 0)
    {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "UF_UI_delete_from_class_sel %s \n", ERR_msg);
    }
 

    irc = UF_UDOBJ_register_fit_cb(UFX_UDO_border_class, NULL);
    if (irc != 0) 
    {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "UF_UDOBJ_register_fit_cb %s \n", ERR_msg);
    }
    irc = UF_UDOBJ_register_display_cb(UFX_UDO_border_class,
                                           NULL);
    if (irc != 0) 
    {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "UF_UDOBJ_register_display_cb %s \n", ERR_msg);
    }
    irc = UF_UDOBJ_register_select_cb(UFX_UDO_border_class,
                                          NULL);
    if (irc != 0) 
    {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "UF_UDOBJ_register_select_cb %s \n", ERR_msg);
    }


}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_ask_view_from_user
 *
 *
 *  DESCRIPTION:  Ask all view info by putting up a dialog to inquire
 *                the view information.  Return a pointer to 
 *                the view structure selected. Returns true if the 
 *                user selected a view and false if the user is quiting.
 *
 *
 ****************************************************************************/
static logical UFX_UDO_ask_view_from_user(
UFX_UDO_view_info_p_t *view_array    /* O  - the view array pointer */
)
{
  logical keep_going;
  int entry_selected;
  
  keep_going = UFX_UDO_select_a_view(UFX_UDO_view_info_array,UFX_UDO_view_num,&entry_selected); 

  if (keep_going) *view_array = &UFX_UDO_view_info_array[entry_selected];

  return keep_going;
  
}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_highlight_view
 *
 *
 *  DESCRIPTION:  Highlights the view just selected.  This routine
 *                must be called after the UFX_UDO_ask_view_from_user
 *                as it requires the view array.
 *
 *
 ****************************************************************************/
static void UFX_UDO_highlight_view(
UFX_UDO_view_info_p_t view_array    /* I  - the view array pointer */
)
{
   int irc;
   /* Set the a special color to show it is highlighted */
   if (view_array->udo_tag == NULL_TAG)
   {
       fprintf(stderr,"bad udo tag ");
   }
   irc = UF_OBJ_set_color(view_array->udo_tag,5);
   if (irc != 0) 
   {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "UF_OBJ_set_color %s \n", ERR_msg);
   }

}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_select_a_note
 *
 *
 *  DESCRIPTION: Selects a note by presenting a dialog.  
 *               Returns 1 or 2 for back or cancel and 3 for the note was 
 *               selected
 *
 *
 ****************************************************************************/
static int UFX_UDO_select_a_note(
tag_p_t note_tag              /* O The tag selected */
)
{
    char *message = "Select a Note ";
    UF_UI_selection_options_t opts;
    UF_UI_mask_t mask;
    int response, irc =0;
    tag_t  view;
    double cursor[3];
     

    opts.other_options = 0;
    opts.reserved = NULL;
    opts.num_mask_triples = 1;
    opts.mask_triples = &mask;

    /* set up selectable type, subtype */
    opts.mask_triples->object_type = UF_drafting_entity_type;  
    opts.mask_triples->object_subtype = UF_draft_note_subtype;
    opts.mask_triples->solid_type = UF_UI_SEL_NOT_A_FEATURE;

    /* set selection scope to be work part */
    opts.scope = UF_UI_SEL_SCOPE_WORK_PART;


    irc = UF_UI_select_single(message,&opts,&response,
                           note_tag,cursor,&view);

    if (irc != 0)
    {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "UF_UI_select_single %s \n", ERR_msg);
    }


    if ((response == 4) || (response == 5))
    {

        UF_UI_set_status("Note Object Selected");
        return 3;
        
    }
    else 
    {

#if 0
       UF_UI_set_status("");
#endif
       /* User wants to quit */
        return response;
    }

}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_deselect_note
 *
 *
 *  DESCRIPTION:  Turns off the highlighting of the note
 *
 *
 ****************************************************************************/
static void UFX_UDO_deselect_note(
tag_t note_tag       /* I The note to deselect */
)              
{
    UF_DISP_set_highlight( note_tag,0);
}

/****************************************************************************
 *
 *  FUNCTION: create_udo_and_reg
 *
 *
 *  DESCRIPTION: create the udo and register the method for the UFX_UDO_border_class
 *               The methods create the illusion of using selection to 
 *               select a view border via user function
 *
 *
 ****************************************************************************/
static void create_udo_and_reg(
int view_num                 /* I The max number of views allowed in array */
)
{
    char class_name[] = "BORDER_CLASS" ;
    char *class_strings = &class_name[0];
    static logical first_time = TRUE;
    int irc, i;
    UF_DISP_system_params_t system_parameters;


    /* The class was not found and it is the first time*/
    if ((UFX_UDO_border_class == 0) && (first_time))
    {
        irc =UF_UDOBJ_create_class("BORDER_CLASS","Border Class",
                                    &UFX_UDO_border_class);
        if (irc != 0) 
        {
            UF_get_fail_message(irc,ERR_msg);
            fprintf(stderr, "UF_UDOBJ_create_class %s \n", ERR_msg);
        }

    }
    irc = UF_UDOBJ_register_attn_pt_cb(UFX_UDO_border_class,
                                             UFX_UDO_make_udo_selectable_cb);
    if (irc != 0) 
    {
         UF_get_fail_message(irc,ERR_msg);
         fprintf(stderr, "UF_UDOBJ_register_attn_pt_cb %s \n", ERR_msg);
    }
    irc = UF_UI_add_to_class_sel(UFX_UDO_border_class);
    if (irc != 0) 
    {
         UF_get_fail_message(irc,ERR_msg);
         fprintf(stderr, "UF_UI_add_to_class_sel %s \n", ERR_msg);
    }

    irc = UF_UDOBJ_register_fit_cb(UFX_UDO_border_class, 
                                   UFX_UDO_make_udo_selectable_cb);
    if (irc != 0) 
    {
         UF_get_fail_message(irc,ERR_msg);
         fprintf(stderr, " UF_UDOBJ_register_fit_cb %s \n", ERR_msg);
    }
    irc = UF_UDOBJ_register_display_cb(UFX_UDO_border_class, 
                                           UFX_UDO_make_udo_selectable_cb);
    if (irc != 0) 
    {
         UF_get_fail_message(irc,ERR_msg);
         fprintf(stderr, " UF_UDOBJ_register_display_cb %s \n", ERR_msg);
    }
    irc = UF_UDOBJ_register_select_cb(UFX_UDO_border_class, 
                                          UFX_UDO_make_udo_selectable_cb);
    if (irc != 0) 
    {
         UF_get_fail_message(irc,ERR_msg);
         fprintf(stderr, "UF_UDOBJ_register_select_cb %s \n", ERR_msg);
    }

    /* Get the system color */
    UF_DISP_ask_system_parameters(&system_parameters);

    for (i = 0; i <view_num; i++)
    {
       irc = UF_UDOBJ_create_udo(UFX_UDO_border_class, 
                                 &(UFX_UDO_view_info_array[i].udo_tag));
       if (irc != 0) 
       {
            UF_get_fail_message(irc,ERR_msg);
            fprintf(stderr, "UF_UDOBJ_create_udo %s \n", ERR_msg);
       }

       /* Add a string identifier just to make sure we know this is our
          UDO
       */
       irc =UF_UDOBJ_add_strings(UFX_UDO_view_info_array[i].udo_tag,1,
                                 &class_strings);
       if (irc != 0) 
       {
            UF_get_fail_message(irc,ERR_msg);
            fprintf(stderr, "UF_UDOBJ_add_strings %s \n", ERR_msg);
       }

       /* Set the udo to the system color */
       irc = UF_OBJ_set_color(UFX_UDO_view_info_array[i].udo_tag, system_parameters.color);
       if (irc != 0) 
       {
            UF_get_fail_message(irc,ERR_msg);
            fprintf(stderr, "UF_OBJ_set_color %s \n", ERR_msg);
       }
    }

    first_time = false;
}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_confirm_1
 *
 *
 *  DESCRIPTION: Pop up a error warning dialog
 *
 *
 ****************************************************************************/
static void UFX_UDO_confirm_1(
char *confirm                /* I    -- The message to show on the dialog */
)
{
int wait=1;

    /* pop up a error message dialog */
    uc1601(confirm,wait);
}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_atten_pt_note
 *
 *
 *  DESCRIPTION:   Puts an attention point at the note coordinates
 *                 
 *                
 *
 *
 ****************************************************************************/
static void UFX_UDO_atten_pt_note(
tag_t note_tag  /* I The tag of the note */
)
{
    int error;
    double note_position[3];

     uf5552(&note_tag,
                 note_position, &error );
     if (error != 1)
     {
          fprintf(stderr,"Could not find position for note \n ");
     }
     error= uc2720("",1,note_position,0,5);
     if (error != 0) fprintf(stderr,"Could not attention point note \n ");
}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_deselect_all_views
 *
 *
 *  DESCRIPTION: de highlights all  views
 *
 *
 ****************************************************************************/
static void UFX_UDO_deselect_all_views(
UFX_UDO_view_info_p_t view_array ,   /* I - the view array */
int num_entries              /* I - the number of valid entries */
)              
{
    int i, irc;
    for (i=0; i<num_entries; i++)
    {
         if (view_array[i].udo_tag != NULL_TAG)
         {
             UF_DISP_set_highlight( view_array[i].udo_tag,0);

             /* And delete the old one */
             irc =  UF_OBJ_delete_object(view_array[i].udo_tag);
             if (irc != 0) 
             {
                UF_get_fail_message(irc,ERR_msg);
                fprintf(stderr, "UF_OBJ_delete_object %s \n", ERR_msg);
             }

             /* Get rid of udo until next time to select */
             view_array[i].udo_tag = NULL_TAG;
         }

    } 
}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_select_a_view
 *
 *
 *  DESCRIPTION: Selects a view by presenting a dialog.  Adds the view 
 *               to the view array Returns a true if the user selected
 *               a view and false if nothing was selected.
 *
 *
 *
 ****************************************************************************/
static logical UFX_UDO_select_a_view(
   UFX_UDO_view_info_p_t view_array,     /* I The view array */
   int view_numb,                /* I The total number in the view array */ 
   int *view_entry_selected      /* O The entry in the view array selected */
)
{
    char *message_selected ="View Selected ";
    char *message = "Select a View ";
    UF_UI_selection_options_t opts;
    UF_UI_mask_t mask;
    int response, irc =0;
    tag_t udo_object, view;
    double cursor[3];

    opts.other_options = 0;
    opts.reserved = NULL;
    opts.num_mask_triples = 1;
    opts.mask_triples = &mask;

    /* set up selectable type, subtype */

    /* Notice that all UDO will be selectable regardless of 
       class. Single selection requires this .  Notice that the
       only subtype allowed is subtype = 0. 
    */
    opts.mask_triples->object_type = UF_user_defined_object_type,
    opts.mask_triples->object_subtype = 0;
    opts.mask_triples->solid_type = UF_UI_SEL_NOT_A_FEATURE;

    /* set selection scope to be work part */
    opts.scope = UF_UI_SEL_SCOPE_WORK_PART;

    /* Clear the message status */
    UF_UI_set_status("");

    irc = UF_UI_select_single(message,&opts,&response,
                           &udo_object,cursor,&view);

    if (irc != 0) 
    {
        UF_get_fail_message(irc,ERR_msg);
        fprintf(stderr, "UF_UI_select_single %s \n", ERR_msg);
    }

    if ((response == 4) || (response == 5))
    {
        int i;

        for (i =0; i<view_numb; i++)
        {
            if (view_array[i].udo_tag == udo_object)
            {
                *view_entry_selected = i; 
                (void)UF_DISP_set_highlight(udo_object,1);
                UF_UI_set_status(message_selected);
                return true ;
            }
        }
         
        fprintf(stderr,"View not found corrupt data structure \n ");
        return false;
        
    }
    else if ((response == 2 ) || (response == 1))
    {

       /* User wants to quit */
        return false;
    }
    else
    {
        /* Should never get here */
        fprintf(stderr, "Should never get here select_a_view \n ");
        return false;

    }

}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_make_udo_selectable_cb
 *
 *
 *  DESCRIPTION:  A callback to be registered for the udo which makes the 
 *                udo selectable.  The udo consists of four lines 
 *                drawn on top of the view borders.  This gives the illusion
 *                of selecting a view via class selection.
 *
 *
 ****************************************************************************/
static void UFX_UDO_make_udo_selectable_cb(
tag_t udo,          /* I The udo to make selectable */
void *context       /* I The context pointer obtained from the callback */
)
{
    int i, irc;
    logical filled = false;
    double borders[12];
    char drawing_name[ UF_OBJ_NAME_BUFSIZE ];
    UF_DISP_inquire_t display_info;

  /* Always initialize even if it has been done before 
     as so other uf program may have UF_terminated by mistake */
    irc = UF_initialize();
    if (irc != 0) 
    {
        UF_get_fail_message(irc,ERR_msg);
        fprintf(stderr, "UF_initialize %s \n", ERR_msg);
        return;
    }
    /* Find out what type of display,selection, fit or attention
       point operation is being performed 
    */
    irc = UF_DISP_ask_display_context(context, &display_info); 
    if (irc != 0) 
    {
        UF_get_fail_message(irc,ERR_msg);
        fprintf(stderr, "UF_DISP_ask_display_context %s \n", ERR_msg);
    }

    
    /* This check is done for demonstration purposes */
    /* When we are selecting fitting or calculating attention points 
       we don't care if the drawing view is open for display as these
       operations don't require an open view  
    */
    if ((display_info.context_running == UF_DISP_SELECT_SING) ||
         (display_info.context_running == UF_DISP_SELECT_BOX) ||
         (display_info.context_running == UF_DISP_ATTEN) ||
         (display_info.context_running == UF_DISP_FIT))
    {
    }

    /* However, when we want to display the UDO the drawing view must 
       be open.  If I had not checked to see if the drawing view where 
       open then our UDO would have been displayed in the drawing member
       views plus the drawing view
    */
    else
    {

        /* No drawing current get out */
        irc = uc6492(drawing_name);
        if (irc != 0)  
        {
            UF_terminate();
            return;
        }
        if (strcmp(drawing_name,"") == 0) return;

        /* Drawing view not open get out */
        if (display_info.is_draw_open_disp != true)
        {
            UF_terminate();
            return;
        }
    }


    /* When we get here we can be displaying, selecting, fitting, or
       calculating attention points */
    
    for (i =0; i< UFX_UDO_view_num; i++)
    {
        /* Find  the udo in the view array and see if the view is valid */
        /* It should be valid as where checking only the active views */
        
        if ((udo == UFX_UDO_view_info_array[i].udo_tag) &&
            (UFX_UDO_view_info_array[i].view_tag != 0))
        {

           /* Map from Drawing to absolute coordinates */

           /* Xmin, Ymin */
           borders[0] = UFX_UDO_view_info_array[i].view_borders[0]   ;
           borders[1] = UFX_UDO_view_info_array[i].view_borders[1]  ;
           borders[2] = 0.0;

           /* LEFT Top corner */
     
           borders[3] = UFX_UDO_view_info_array[i].view_borders[0]   ;
           borders[4] = UFX_UDO_view_info_array[i].view_borders[3]  ;
           borders[5] = 0.0;
        
           /* Xmax , Ymax */
           borders[6] = UFX_UDO_view_info_array[i].view_borders[2]  ;
           borders[7] = UFX_UDO_view_info_array[i].view_borders[3]  ;
           borders[8] = 0.0;

            /* RIGHT Bottom corner Xmax Ymin */

           borders[9] = UFX_UDO_view_info_array[i].view_borders[2] ;
           borders[10] = UFX_UDO_view_info_array[i].view_borders[1];
           borders[11] = 0.0;

           /* Draw the polygon for display, selection, fit, or attention
              point calculations 
           */
           irc =  UF_DISP_display_polygon(borders,4 ,filled,context);
           if (irc != 0)
           {
               UF_get_fail_message(irc,ERR_msg);
               fprintf(stderr, "  UF_DISP_display_polygon %s \n", ERR_msg);
           }
           break;
        }
    }         

    irc = UF_terminate();
    if (irc != 0)
    {
         UF_get_fail_message(irc,ERR_msg);
         fprintf(stderr, " UF_terminate %s \n", ERR_msg);
    }

    return;

}
