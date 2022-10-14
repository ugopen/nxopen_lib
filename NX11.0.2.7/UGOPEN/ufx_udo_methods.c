/*==============================================================================
 *
 *       Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
 *                  Unpublished - All rights reserved
 *
 *==============================================================================
 *  File description:
 *
 *  This file registers the UDO methods once during startup of Unigraphics.
 *  The public entry point is ufsta.  The methods persist during the entire
 *  Unigraphics session.
 *  The bodies of the registered methods are contained in ufx_udo_application.c
 *  The code in this file should be compiled-linked and placed in the
 *  "udo/" directory. 
 *

 *
 *===========================================================================
*/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_udobj.h>
#include <uf_drf.h>
#include <uf_view.h>
#include <uf_draw.h>
#include <uf_exit.h>
#include <ufx_udo.h>

/* Metric scale factor for converting metric drawings on english parts */
static double METRIC_scale;

/* The class id for associating UDO's with views and notes   */
static unsigned int     UFX_UDO_note_vw_class;

/* The pointer to the view array */
static UFX_UDO_view_info_p_t UFX_UDO_view_info_array;

/* Total number of elements in the view array */
static int UFX_UDO_view_num;

static UFX_UDO_view_info_t space_for_info_array[MAX_DRAW_VIEWS];
static UFX_UDO_view_info_t space_for_info_array2[MAX_DRAW_VIEWS];
static UFX_UDO_view_info_p_t updated_info_array;

static char ERR_msg[133];

/* Forward declarations */
static void UFX_UDO_add_all_view_to_array(
UFX_UDO_view_info_p_t view_array,      /* I  - The pointer to the array */
int *view_numb                 /* I/O - The number in the array and is updated
                                  to the new number of elements in the array */
);
static void UFX_UDO_read_view_data(
UFX_UDO_view_info_p_t view_array,     /* I The view array */ 
int view_index                /* I The index into the view array */
);
static void UFX_UDO_ask_view_center(
tag_t view_tag,               /* I - The view tag */
double view_center[3]         /* O - The views center */
);
static  void UFX_UDO_ask_all_view_data(
    UFX_UDO_view_info_p_t *view_array,  /* I/O  - The pointer to the array */
    int *view_numb              /* O - The number of elements in the array */
);

/* These functions are declared external and exported. They will be 
   called from the ufx_udo_application.c file.  They provided access to 
   static data set at startup time 
*/

DllExport extern void UFX_UDO_ask_all_view_data_dll(
    UFX_UDO_view_info_p_t *view_array,  /* I/O  - The pointer to the array */
    int *view_numb              /* O - The number of elements in the array */
)
{
    UFX_UDO_ask_all_view_data(view_array,view_numb);
}

DllExport extern void UFX_UDO_ask_view_center_dll(tag_t view_tag,
                                                  double view_center[3])
{
    UFX_UDO_ask_view_center(view_tag,view_center);
}
/* Set the metric value */
DllExport extern void UFX_UDO_set_Metric(double  metric /*I Metric values */)
{
     METRIC_scale = metric;
     return;
}
/* Get the note view class created at startup time */
DllExport extern UF_UDOBJ_class_t UFX_UDO_get_note_vw_class(void)
{
    return UFX_UDO_note_vw_class;
}
/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_update_cb
 *
 *
 *  DESCRIPTION: This is the update callback which is executed by
 *               Unigraphics each time a view is moved. The callback
 *               calculates the views new position and then moves each
 *               note associated with the view by the indicated value.
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_update_cb( tag_t udo_tag,     /* I The udo tag */
                                               /* I The reason for the update */
                            UF_UDOBJ_link_p_t update_cause  
);

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_create_and_reg_update
 *
 *
 *  DESCRIPTION: This routine creates the note/view class and 
 *               registers the update method.
 *
 *
 *
 ****************************************************************************/

static void UFX_UDO_create_and_reg_update( void );

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_ask_note_position
 *
 *
 *  DESCRIPTION:  Returns the note position at time of update
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_ask_note_position(
tag_t note_tag,                /* I - The note tag */
double note_position[3]       /* O - The notes position at update */
);

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_move_note_position
 *
 *
 *  DESCRIPTION:  Changes the note position to the new position specfied
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_move_note_position(
    tag_t note_id,          /* I the note to move */
    double position[3]      /* I the new position of the note */
);

/****************************************************************************
 *
 *  FUNCTION:  ufsta
 *
 *
 *  DESCRIPTION: This is the entry point to be executed at startup time
 *               to initialize and register the method for updating the 
 *               notes associated with the view.
 *
 *
 *
 ****************************************************************************/
extern void ufsta( char *param, int *retcod, int param_len )
{

    int error;

    UFX_UDO_note_vw_class = 0;
    METRIC_scale = 1.0;
    UFX_UDO_view_num = 0;
    UFX_UDO_view_info_array = NULL;
   
    error = UF_initialize();
    if (error)
    {
       UF_get_fail_message(error,ERR_msg);
       fprintf(stderr, "UF_initialize %s \n", ERR_msg);
       error = UF_terminate();
       return;
    }

    UFX_UDO_create_and_reg_update();

    error = UF_terminate();
    if (error)
    {
       UF_get_fail_message(error,ERR_msg);
       fprintf(stderr, " UF_terminate %s \n", ERR_msg);
    }
    return;
}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_create_and_reg_update
 *
 *
 *  DESCRIPTION: This routine creates the note/view class and 
 *               registers the update method.
 *
 *
 *
 ****************************************************************************/

static void UFX_UDO_create_and_reg_update( void )
{
    int error;

    /*  create a UDO class */
    error = UF_UDOBJ_create_class("associate view and note",
                NULL, &UFX_UDO_note_vw_class);
    if ( error )
    {
         UF_get_fail_message(error,ERR_msg);
         fprintf(stderr, "UF_UDOBJ_create_class %s \n", ERR_msg);
         return;
    }

    /*  register udpate call back */
    error = UF_UDOBJ_register_update_cb(UFX_UDO_note_vw_class, UFX_UDO_update_cb);
    if ( error )
    {
        UF_get_fail_message(error,ERR_msg);
        fprintf(stderr, "UF_UDOBJ_register_update_cb %s \n", ERR_msg);
        return;
    }

}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_update_cb
 *
 *
 *  DESCRIPTION: This is the update callback which is executed by
 *               Unigraphics each time a view is moved. The callback
 *               calculates the views new position and then moves each
 *               note associated with the view by the indicated value.
 *
 *
 *
 ****************************************************************************/
static void UFX_UDO_update_cb( tag_t udo_tag,   /* I The udo tag */
                                             /* I The reason for the update */
                            UF_UDOBJ_link_p_t update_cause)
{
int             num_notes,error,i,j;
UF_UDOBJ_all_data_t    udo_data;


/* Get out if update_cause in NULL. This can happen when notes which 
   are associated with a view get deleted */

        if (update_cause == NULL) return;

/* Always initialize as some other UF program may have terminated by
   mistake 
*/
        error = UF_initialize();
        if (error)
        {
            printf("UF_initialize failed \n");
            error = UF_terminate();
            return;
        }
/* get all udo data */
    error = UF_UDOBJ_ask_udo_data(udo_tag, &udo_data);
    if(error || (udo_data.num_links == 0))
    {
                printf( "UFX_UDO_update_cb: did not get udo data successfully.\n");
                error = UF_terminate();
         return;
    }


/*  If function is called because a note is deleted and 
    its tag is not associate with the UDO return directlly */
        if(NULL_TAG == update_cause->assoc_ug_tag)
    {
                error = UF_terminate();
        return;
    }

/*  If the function is called because the view is updated */
    else if ( update_cause->assoc_ug_tag == 
            udo_data.link_defs[0].assoc_ug_tag)
    {
    tag_t view_tag,note_tag;
    double view_center[3],note_position[3],new_position[3];
/* get view tag and view center */
        view_tag = udo_data.link_defs[0].assoc_ug_tag;
        UFX_UDO_ask_view_center(view_tag,view_center);

/* get note tag, the new note position and move the note */
        num_notes = udo_data.num_links-1;
        for( i = 0; i < num_notes; i++)
            {
                note_tag = udo_data.link_defs[i+1].assoc_ug_tag;
            UFX_UDO_ask_note_position(note_tag,  note_position);
                for ( j = 0; j < 3; j++)
                {
                 new_position[j] = (view_center[j] - udo_data.doubles[j])
                     + note_position[j];
            }
                UFX_UDO_move_note_position(note_tag, new_position);
            }
/* update new view position */
        UF_UDOBJ_edit_doubles(udo_tag,view_center);
    }


/*  If the function is called because a note is updated */
    else
    {
                error = UF_terminate();
        return;
    }

    UF_UDOBJ_free_udo_data(&udo_data);

        error = UF_terminate();
        if (error)
        {
            printf("UF_terminate failed \n");
            return;
        }
}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_move_note_position
 *
 *
 *  DESCRIPTION:  Changes the note position to the new position specfied 
 *                
 *
 *
 ****************************************************************************/
static void UFX_UDO_move_note_position(
    tag_t note_id,          /* I the note to move */
    double position[3]      /* I the new position of the note */
)
{
    int error;
    position[2] = 0.0;
    FTN(uf5553)(&note_id, position, &error);
    if (error != 1) fprintf (stderr, "Error moving note \n ");

}
/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_ask_note_position
 *
 *
 *  DESCRIPTION:  Returns the note position at time of update 
 *                
 *
 *
 ****************************************************************************/
static void UFX_UDO_ask_note_position(
tag_t note_tag,                /* I - The note tag */
double note_position[3]       /* O - The notes position at update */
)
{
    int error;
   

     FTN(uf5552)(&note_tag,
                 note_position, &error );
     if (error != 1)
     {
          fprintf(stderr,"Could not find position for note \n ");
     }
}

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_ask_view_center
 *
 *
 *  DESCRIPTION:  Returns the view center at time of update 
 *                
 *
 *
 ****************************************************************************/
static void UFX_UDO_ask_view_center(
tag_t view_tag,               /* I - The view tag */
double view_center[3]         /* O - The views center */
)
{
    int i;
    /* find all the view data */
    UFX_UDO_ask_all_view_data(&UFX_UDO_view_info_array,&UFX_UDO_view_num);

    for (i = 0; i<UFX_UDO_view_num; i++)
    {
        if (view_tag ==  UFX_UDO_view_info_array[i].view_tag)
        {
            view_center[0] = (UFX_UDO_view_info_array[i].view_borders[0] +
                             UFX_UDO_view_info_array[i].view_borders[2])/2;

            view_center[1] = (UFX_UDO_view_info_array[i].view_borders[1] +
                             UFX_UDO_view_info_array[i].view_borders[3])/2;
            view_center[2] =0.0;
            return;
        }
    } 

   fprintf(stderr,"Unable to read view center \n" );

}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_ask_all_view_data
 *
 *
 *  DESCRIPTION: Finds all the view data at the time of inquiry and updates
 *               the view array.  Also returns memory for the view array.
 *               The view_array must be NULL on the first call and 
 *               the pointer returned must be input on subsequent calls.
 *
 *
 ****************************************************************************/
static  void UFX_UDO_ask_all_view_data(
    UFX_UDO_view_info_p_t *view_array,  /* I/O  - The pointer to the array */
    int *view_numb              /* O - The number of elements in the array */
)
{
   int local_view_num = 0, i, j;

   /* Handle getting the correct address */
   if ((*view_array) == space_for_info_array)
   {
       updated_info_array = space_for_info_array2;
   }
   else if ((*view_array) == space_for_info_array2)
   {
       updated_info_array = space_for_info_array ;

   }
   else if ((*view_array)  == NULL)
   {
       (*view_array) = space_for_info_array;
       updated_info_array = space_for_info_array2;
   }
   else
   {
       fprintf(stderr, "Bad address for info array \n");
   }

   /* refind all the views */
   UFX_UDO_add_all_view_to_array(updated_info_array,&local_view_num);

  /* Now get the latest list uptodate in the local_info_array */

  for (i=0; i< MAX_DRAW_VIEWS; i++)
  {
      for (j = 0; j < MAX_DRAW_VIEWS; j++)
      {
          if ( (*view_array)[j].view_tag == updated_info_array[i].view_tag)
          {

              /* Update the UDO tag as it persists across the session */
              updated_info_array[i].udo_tag = (*view_array)[j].udo_tag;
              
          }
      }
  }


  *view_array = updated_info_array;
  *view_numb = local_view_num;
}

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_add_all_view_to_array
 *
 *
 *  DESCRIPTION: Finds all the views and places them in the view array
 *
 *
 ****************************************************************************/
static void UFX_UDO_add_all_view_to_array(
UFX_UDO_view_info_p_t view_array,      /* I  - The pointer to the array */
int *view_numb                 /* I/O - The number in the array and is updated
                                  to the new number of elements in the array */
)
{
  char drawing_name[ UF_OBJ_NAME_BUFSIZE ];
  char view_name[ UF_OBJ_NAME_BUFSIZE ] ="";
  int  irc =0;
  logical  done_cycling_views = false;
  
  (*view_numb) = 0;
  irc = uc6492(drawing_name);
  if (irc != 0)
  {
       UF_get_fail_message(irc,ERR_msg);
       fprintf(stderr, "uc6492 %s \n", ERR_msg);
       fprintf(stderr, "Error reading drawing name \n");
       return;
  }
  if (strcmp(drawing_name,"") == 0)
  {
      fprintf(stderr,"No drawing Active \n");
      return;
  }


  while (!done_cycling_views)
  {
      irc = uc6499(drawing_name, view_name); 
      if (irc != 0) 
      {
          UF_get_fail_message(irc,ERR_msg);
          fprintf(stderr, "uc6499 %s \n", ERR_msg);
          fprintf(stderr, "Can't find view name \n ");
          return;
      }
      if (strcmp(view_name, "")  == 0)
      {
          /* No Views */
          done_cycling_views = TRUE;
      }
      else
      {
 
          /* Save the view name */ 
          strcpy(view_array[*view_numb].view_name,view_name); 

          UFX_UDO_read_view_data(view_array, *view_numb);

          (*view_numb)++;
      }
  }
     
}
/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_read_view_data
 *
 *
 *  DESCRIPTION: Reads the view data from the database and update the 
 *               view array
 *
 *
 ****************************************************************************/
static void UFX_UDO_read_view_data(
UFX_UDO_view_info_p_t view_array,     /* I The view array */ 
int view_index                /* I The index into the view array */
)
{
    int irc, units,size, i; 
    double max[2];
    /* Find the tag of the view */

     irc = UF_VIEW_ask_tag_of_view_name(view_array[view_index].view_name, 
                                    &(view_array[view_index].view_tag));
     if (irc != 0)
     {
          UF_get_fail_message(irc,ERR_msg);
          fprintf(stderr, "UF_VIEW_ask_tag_of_view_name %s \n", ERR_msg);
          fprintf(stderr, "Could not find the view tag \n ");
          return;
     }


     /* Read View Center and Scale */
     irc = uc6430(view_array[view_index].view_name,
                  view_array[view_index].view_cntr ,
                  &(view_array[view_index].view_scale));
     if (irc != 0)
     {
          UF_get_fail_message(irc,ERR_msg);
          fprintf(stderr, " uc6430 %s \n", ERR_msg);
          fprintf(stderr, "Could not read view center and scale \n ");
          return;
     }

     irc = uc6485(view_array[view_index].view_name,
                  view_array[view_index].view_borders);
                       
     if (irc != 0)
     {
          UF_get_fail_message(irc,ERR_msg);
          fprintf(stderr, " uc6485 %s \n", ERR_msg);
          fprintf(stderr, "Could not read borders \n ");
          return;
     }
  
     irc = uc6479("",&units,&size,max);
     if (irc != 0)
     {
          UF_get_fail_message(irc,ERR_msg);
          fprintf(stderr, "uc6479 %s \n", ERR_msg);
          fprintf(stderr, "Could not read drawing size \n ");
          return;
     }
     /* Convert to correct scale */
     for (i =0; i < 4 ; i++)
     {
         view_array[view_index].view_borders[i] =
                    view_array[view_index].view_borders[i] * METRIC_scale;
     }
}
