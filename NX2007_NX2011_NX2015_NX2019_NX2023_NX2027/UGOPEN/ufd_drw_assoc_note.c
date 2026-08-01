/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_view_of_note, UF_DRAW_ask_view_notes,
 *    UF_DRAW_attach_note_to_view, and UF_DRAW_detach_note_from_view.  
 *    It is placed directly in our UFUN documentation starting with 
 *    the include statements.
 *
 
 *
 ****************************************************************************/
 
#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_so.h>
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int         ifail = 0;
    int         num_notes = 0;
    tag_t       part_tag = NULL_TAG;
    tag_t       view_tag = NULL_TAG;
    tag_t       assoc_view_tag = NULL_TAG;
    tag_t       *note_tags = NULL;
    tag_t       named_note_tag = NULL_TAG;
    tag_t       drawing_tag = NULL_TAG;
    char        error_message[133];
    char *      view_name = "TOP@1";
    char *      named_note   = "NAMEDNOTE";    
    
    ifail = UF_initialize();
    
    if ( ifail == 0 )
        part_tag = UF_PART_ask_display_part();
    
    if ( ifail == 0 && part_tag != NULL_TAG )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );
            
    if ( ifail == 0 && drawing_tag != NULL_TAG )
        ifail = UF_VIEW_ask_tag_of_view_name(view_name,
                                            &view_tag );
    
    if ( ifail == 0 && view_tag != NULL_TAG )
        ifail = UF_DRAW_ask_view_notes( view_tag, &num_notes, &note_tags );
                                                                
    if ( ifail == 0 && num_notes > 0 )
        /* Disassociate the first note from the view. */       
        ifail = UF_DRAW_detach_note_from_view( note_tags[0] );
        
    if ( ifail == 0 )
        ifail = UF_OBJ_cycle_by_name( named_note, &named_note_tag );
                                               
    if ( ifail == 0  && named_note_tag != NULL_TAG )
        /* Associate the named note to the view. */
        ifail = UF_DRAW_attach_note_to_view( named_note_tag, view_tag );
        
    if ( ifail == 0 )
        /* Verify that the note was associated to the view. */
        ifail = UF_DRAW_ask_view_of_note( named_note_tag, &assoc_view_tag );
                                                               
    printf("UF_DRAW_view_notes sample program ");                        
    if( ifail != 0 )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else if ( part_tag == NULL_TAG )
        printf( "fails.\nError is: no active part.\n" );
    else if ( view_tag == NULL_TAG )
        printf( "fails.\nError is: no TOP@1 view.\n" );
    else if ( num_notes == 0 )
        printf( "fails.\nNo notes were associated to the view.\n" );
    else if ( assoc_view_tag  != view_tag )
        printf( "fails.\nNamed note not associated to the view.\n" );
    else							
        printf( "is successful.\n" );                                                                 
    
    UF_free(note_tags);          
    
    ifail = UF_terminate();
}
