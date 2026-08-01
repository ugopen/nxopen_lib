/*===================================================================

          Copyright (c) 1998-2002 Electronic Data Systems Corporation
                       Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_UI_open_part
 *    It is placed directly in our UG/Open documentation starting with
 *    the include statements.
 *
 *  
 *
 ********************************************************************/

/* ***** Include Files ***** */

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_ui.h>

/* ***** Local Prototype ***** */

static logical my_error_handler
(
    UF_UI_err_data_p_t     error_fn_data,
    char                  *file_name,
    int                    error,
    UF_PART_load_status_t *error_status,
    logical               *skip_error_disp
);

/* ***** Entry Point ***** */

/*ARGSUSED*/
extern void ufusr ( char *param , int *ret_code , int len )
{
    /*
       *********************
       variable declarations
       *********************
    */
    int response;
    tag_t part_tag = NULL_TAG;
    char file_name [  MAX_FSPEC_BUFSIZE ] = "flange.prt";
    const char *message = "part open error";
    logical unused;
    UF_PART_load_status_t part_status;
    UF_UI_err_t error_handler;
    
    /*
       ************************************************
       initialize the 'struct' as an open part 'struct'
       and assign the local function prototyped above
       as the callback
       ************************************************
    */
    error_handler.type = UF_UI_open_part_fun;
    error_handler.fun.open = my_error_handler;

    /*
       ************************************************
       assign the client data and its size

       Note:  this is an arbitrary usage of the client
       data.  A better use might be to pass the name of
       a UIStyler dialog which would then be invoked in
       the callback
       ************************************************
    */
    error_handler.fun_data.size = strlen ( message ) + 1;
    error_handler.fun_data.data = message;

    /*
      *************************************************
      call the function, free any allocated memory
      *************************************************
    */
    UF_initialize ( );
    UF_UI_open_part ( &error_handler , file_name , &unused , &part_tag ,
		      &response ,  &part_status );
    if ( part_status.statuses != NULL )
	{
	UF_free ( part_status.statuses );
	}
    if ( part_status.file_names != NULL )
	{
	UF_free_string_array ( part_status.n_parts , part_status.file_names );
	}
    UF_terminate ( );
}

/* ***** local function to be invoked as a callback ***** */
static logical my_error_handler
(
    UF_UI_err_data_p_t     error_fn_data,
    char                  *file_name,
    int                    error,
    UF_PART_load_status_t *error_status,
    logical               *skip_error_disp
)
{
    /*
      ***************************************************
      this function trivially just prints the client data
      that it receives as well as the file name and the
      error

      As mentioned above, a better usage of the client
      data would be to pass through the name of a
      UIStyler dialog to display.  Such a use might
      resemble the following:

      UF_STYLER_create_dialog (
	( char * ) error_fn_data->data ,
        callbacks ,
	n_callbacks ,
	NULL ,
	&response );

      ***************************************************
    */
    fprintf ( stderr , "my_error_handler called with:\n"
		       "    error_fn_data->size = %d\n"
		       "    error_fn_data->data = %s\n"
		       "    file_name           = %s\n"
		       "    error               = %d\n" ,
		       error_fn_data->size ,
		       ( const char * ) error_fn_data->data ,
		       file_name ,
		       error
            );

    /* **************************************************
       instruct UG to display its error dialog and to
       continue looping within the dialog until a part
       is opened
       **************************************************
    */
    *skip_error_disp = TRUE;
    return TRUE;
}
