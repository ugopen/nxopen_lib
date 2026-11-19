/*==============================================================================
          Copyright (c) 1998-2002  Electronic Data Systems Corporation
                       Unpublished - All rights reserved

================================================================================
 File Name: ufx_cycle_internal.c

 File Description:
   This is the internal User Function version of cycling the data model. This
   code opens a dialog box and gets the part file name to cycle. The major work 
   is done by UFX_CYCLE_data. For details, see the ufx_cycle_common.c source 
   file.
================================================================================


*******************************************************************************/


/* Include Files */
#include <stdio.h>
#include <ufx_cycle.h>
#include <uf_ui.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_assem.h>

/* Function Prototypes */
static int initialize(void);
static void menu(int *response, char *part_name);
static int put_file_selection(char *part_name);



/* -----------------------------------------------------------------------------
 Function name: ufusr

 Function Description: Internal User Function entry point.

 Inputs:
   param - Parameters (unused).
   param_len - Length of param argument. Unigraphics handles this input for you.

 Output:
   retcod - Return code. Only used by Internal User Exits.
   -----------------------------------------------------------------------------
*/
   
extern void ufusr(char *param, int *retcod, int param_len)
{

  int err;
  int response = UF_UI_OK;
  tag_t part_tag;

/* Part name to cycle on. Assign a null for the default part name. */
  char part_name[ MAX_FSPEC_BUFSIZE ] = {'\0'};

  err = initialize();
  if(!err)
  {
    do
    {
      part_tag = UF_ASSEM_ask_work_part();
      if(part_tag == NULL_TAG)
      {
      
      
        response = put_file_selection(part_name);
        if(response == UF_UI_OK)
        {
          err = UFX_CYCLE_open_part(part_name, &part_tag);
          if(!err)
          {
            UFX_CYCLE_data(part_tag);
          }
        }
        
      }
    } while(err && (response != UF_UI_CANCEL));
/* End of do-while err */
    if(part_tag)
    {
      do
      {
        if(response == UF_UI_OK)
        {
          menu(&response, part_name);
        }
      } while(!err && (response == UF_UI_OK));
    } /* end of if there is a work part */
        
    UF_terminate();
  } /* End of if !err */
  
} /* End of ufusr */



/* Allow unloading of shared image from a dialog. This allows you to
   modify the program, recompile, and relink without having to bring
   Unigraphics down to clear the image from memory.
*/
int ufusr_ask_unload(void)
{
  return (UF_UNLOAD_IMMEDIATELY);
}

/* -----------------------------------------------------------------------------
 Function Name: report_err

 Function Description:
   Prints the error message from UF_get_fail_message to a UGII
   dialog or prints an alternate message if UF_get_fail_message fails. 

 Inputs:
   status - return value from a User Function.
   alt_msg - Alternate message to use if UF_get_fail_message fails. Note that
             alt_msg cannot be NULL.

 Outputs: None.

 Returns: None
   -----------------------------------------------------------------------------
*/

extern void report_err(int status, char *alt_msg)
{
  char message[ MAX_LINE_BUFSIZE ], buffer[ UF_UI_MAX_STRING_BUFSIZE ];

  int err = UF_get_fail_message(status, message);

  if(err)
  {
     sprintf(buffer, "%s \n", alt_msg);
     uc1601(buffer, 1);
  }
  else
  {
     sprintf(buffer, "%s \n", message);
     uc1601(buffer, 1);
  }
}

/* -----------------------------------------------------------------------------
 Function Name: menu

 Function Description:
   Displays a multiple menu dialog which offers the choice of cycling the work
   part or a part specified from the file list dialog.

 Inputs:
   None.

 Outputs:
   response - Back, OK, or Cancel
   part_name - Name of part to cycle.

 Returns:
   None.
   -----------------------------------------------------------------------------
*/

static void menu(int *response, char *part_name)
{
  char *menu_title = "Select Only One Option To Cycle";
  char menu_list[2][38] = {"Cycle Work Part", "Specify Part to Cycle"};
  int array_dim = 2, obs=1, select_array[2];
  int err;
  tag_t part_tag;
  logical menu_choice;

  do
  {
    int temp_return;
    temp_return = uc1605(menu_title,obs,menu_list,array_dim,select_array);
    menu_choice = FALSE;
    if(temp_return == 1)
    {
      *response = UF_UI_BACK;
    }
    else if(temp_return == 2)
    {
      *response = UF_UI_CANCEL;
    }
    else 
    {
      *response = UF_UI_OK;
    
      if(select_array[0] == select_array[1])
      {
        uc1601("Please select one option.",1);
        menu_choice = TRUE;
      }
      else if(select_array[0] == 1)
      {
        part_tag = UF_ASSEM_ask_work_part();
        UFX_CYCLE_data(part_tag);
      }

      else
      {
        do
        {
          err =0;
          *response = put_file_selection(part_name);
          if(*response == UF_UI_OK)
          {
            part_tag = UF_PART_ask_part_tag(part_name);
            if(part_tag == NULL_TAG)
            {
              err = UFX_CYCLE_open_part(part_name, &part_tag);
              if(!err)
              {
                UFX_CYCLE_data(part_tag);
              }
            }
            /* The specified part is loaded */
            else if(part_tag == UF_ASSEM_ask_work_part())
            {
              uc1601("This part is already loaded. Will cycle.",1);
              UFX_CYCLE_data(part_tag);
            }
            else
            {
              uc1601("This part is loaded, make it the work part.",1);
            }
          }
        } while(err);
        menu_choice = (*response != UF_UI_CANCEL);   
      }
    }

  } while(menu_choice);
  
}

/* -----------------------------------------------------------------------------
 Function Name: initialize

 Function Description:
   Initializes User Function and opens Information window.

 Inputs:
   None.

 Outputs:
   None.

 Returns:
   err - function error codes.
   -----------------------------------------------------------------------------
*/


static int initialize(void)
{
  char err_msg[ MAX_LINE_BUFSIZE ];
  int err;

  err = UF_initialize();
  if(err)
  {
    fprintf(stderr,"\nError: Could not init UFUN.\n");
    UF_get_fail_message(err,err_msg);
    fprintf(stderr, "Error %d: %s \n",err,err_msg);
  }
  else
  {
    err = UF_UI_open_listing_window();
    if(err)
    {
      fprintf(stderr, "\nUnable to open listing window.\n");
      UF_terminate();
    }
  }
  return(err);
}

/* -----------------------------------------------------------------------------
 Function Name: put_file_selection

 Function Description:
   Displays the file selection dialog and gets a part name.

 Inputs:
   None.

 Outputs:
   part_name - part name from file selection dialog.

 Returns:
   response - Back or cancel from file selection dialog.
   -----------------------------------------------------------------------------
*/

static int put_file_selection(char *part_name)
{
  
  logical unused;
  int err, response, file_select;
   
  do
  {
    err = UF_UI_ask_open_part_filename(part_name, &unused, &response);
 
    file_select = (response == UF_UI_OK) && (err);

    if(err && (response != UF_UI_CANCEL))
    {   
      report_err(err, "Invalid Part Name or Part Not In This Directory.\n"); 
    }
         
  } while(file_select);
  
  return(response);
  
}
