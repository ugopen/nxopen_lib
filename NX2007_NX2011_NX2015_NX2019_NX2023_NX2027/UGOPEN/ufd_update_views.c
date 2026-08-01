/*===================================================================

        Copyright (c) 1999  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/


/*==============================================================================

Description:
     This program shows how to use:

     UF_DRAW_ask_drawings
     UF_DRAW_open_drawing
     UF_DRAW_ask_views
     UF_DRAW_ask_view_display
     UF_DRAW_set_view_display
     UF_DRAW_upd_out_of_date_views 

Program Description:
     Runs as an external UG/Open program that takes as command line arguments
     top-level assembly drawing parts for each assembly or piece part
     that needs to be updated. All drawings in the input part files will have
     all their out-of-date views updated. This program also turns on extracted
     edges for member views.
 
    ==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_assem.h>
#include <uf_draw.h>
#include <uf_part.h>
#include <uf_defs.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static void update_drawings( void );
static void save_all_parts( void );
static void extract_edges( tag_t drawing_tag );

static int report( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char    messg[MAX_LINE_BUFSIZE];
        printf("%s, line %d:  %s\n", file, line, call);
        (UF_get_fail_message(irc, messg)) ?
            printf("    returned a %d\n", irc) :
            printf("    returned error %d:  %s\n", irc, messg);
    }
    return(irc);
}

/* -----------------------------------------------------------------------------
 Function Name: main

 Function Description:
   The main for external UG/Open.

 Input:
   argc - Argument count
   argv - Pointers to character strings of arguments.

 Output: None.

 Returns:
   0 - Indicates success.
   -----------------------------------------------------------------------------
*/


extern int main( int argc, char *argv[] )
{
    int indx;

    if (!UF_CALL(UF_initialize()))
    {
        if ( argc == 0 )
        {
            printf( "No arguments supplied, nothing to do!\n" );
            return 0;
        }

        for ( indx = 1; indx < argc; indx++ )
        {
            tag_t this_part = NULL_TAG;
            UF_PART_load_status_t error_status;
            UF_ASSEM_options_t    options;

            printf( "Updating drawings in part %s\n",argv[indx] );

            /* Reset all the options for each assembly just in case. */
            UF_CALL( UF_ASSEM_ask_assem_options( &options ));
            options.load_options    = UF_ASSEM_load_as_saved;
            options.failure_action  = UF_ASSEM_dont_abort_on_failure;
            options.load_latest     = UF_ASSEM_load_latest_version;
            options.load_components = UF_ASSEM_do_load_components;
            options.load_fully      = UF_ASSEM_load_components_fully;
            UF_CALL( UF_ASSEM_set_assem_options( &options ));
        
            UF_CALL(UF_PART_open( argv[indx], &this_part, &error_status ));
            if ( error_status.failed )
            {
                int indx2;

                for ( indx2 = 0; indx2 <  error_status.n_parts; indx2++ )
                {
                    printf("Error number %d. Opening child part %s failed\n",
                           error_status.statuses[indx2],
                           error_status.file_names[indx2]);
                }
                UF_free_string_array( error_status.n_parts,
                                      error_status.file_names );
                UF_free( error_status.statuses );
                /* Just in case, close any open child parts. */
                UF_CALL( UF_PART_close_all() );
                /* Don't quit completely but continue to attempt to retrieve
                   parts because they might not all be broken.
                */
                continue;
            }
            update_drawings( );
            save_all_parts( );
            UF_CALL( UF_PART_close_all());
        }
        UF_CALL(UF_terminate());
    }
    return 0;
}
    
/* ----------------------------------------------------------------------------
 Function Name: update_drawings

 Function Description:
   Gets a list of all the drawings in the part file, opens the drawing, and
   updates any view that is out of date.
   ----------------------------------------------------------------------------
*/

static void update_drawings( void )
{
    int indx, error_code = 0;
    int num_drawings = 0;
    tag_p_t drawing_list = NULL;

    /* Get a list of all the drawings in the part file. */
    error_code = UF_DRAW_ask_drawings( &num_drawings, &drawing_list );

    if ( error_code > 0 || num_drawings == 0 )
        return;

    for ( indx = 0; indx < num_drawings; indx++ )
    {
        /* Open each drawing and update any out-of-date views. */
        UF_CALL( UF_DRAW_open_drawing( drawing_list[indx] ));
        extract_edges( drawing_list[indx] );
        UF_CALL( UF_DRAW_upd_out_of_date_views( drawing_list[indx] ));
    }
    UF_free( drawing_list );
}

/*-----------------------------------------------------------------------------
 Function Name: extract_edges

 Function Description:
   Sets extracted edges for drawing member views.
  -----------------------------------------------------------------------------
*/
static void extract_edges(tag_t drawing_tag)
{
    int num_views = 0;
    int indx2;
    tag_p_t view_list = NULL;
    UF_DRAW_view_prfs_t view_display_parms;

    /* Get the list of view tags from the drawing. */
    if(!UF_CALL(UF_DRAW_ask_views(drawing_tag, &num_views, &view_list)))
    {
         /* Cycle through the views. */
         for(indx2 = 0; indx2 < num_views; indx2++)
         {
             /* Get the view's current display parameter settings
                before changing them.
             */
             UF_CALL(UF_DRAW_ask_view_display(view_list[indx2],
                                              &view_display_parms));
             /* Turn on extracted edges. */
             view_display_parms.extracted_edges = (UF_DRAW_extracted_edges_t)1;
             /* Set the view's display parameters. */
             UF_CALL(UF_DRAW_set_view_display(view_list[indx2],
                                              &view_display_parms));
         }
         UF_free( view_list );
    }
}
    


    

/* ----------------------------------------------------------------------------
 Function Name: save_all_parts

 Function Description:
   Saves all parts in the session to disk with their original names. Error
   checks for failure and sends a message to stderr.
   ----------------------------------------------------------------------------
*/

static void save_all_parts ( void )
{
    int err_count = 0;
    tag_t *parts = NULL;
    int   *error_list = NULL;

    if((UF_PART_save_all(&err_count, &parts, &error_list)) !=0)
    {
       int i;
       char errmsg[MAX_LINE_BUFSIZE];

       /* Process each file error. */
       for(i=0; i < err_count; i++)
       {
          sprintf(errmsg, "Part %u failed to save with error %d\n",
                           parts[i], error_list[i]);
          fprintf(stderr, "%s", errmsg);
       }
       UF_free(parts);
       UF_free(error_list);
    }
}

