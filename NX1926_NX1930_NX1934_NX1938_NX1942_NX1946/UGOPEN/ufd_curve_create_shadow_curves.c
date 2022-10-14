/*==================================================================================================

                        Copyright (c) 2007 UGS Corp.
                      Unpublished - All rights reserved

====================================================================================================
File description:

A code example to use the new function UF_create_shadow_curves. The program extracts 
shadow curves from a given part and puts them into an array
    

====================================================================================================
   Date      Name                    Description of Change
12-May-2008  Hua Du                  Written
$HISTORY$
==================================================================================================*/
#include <stdlib.h>
#include <uf_defs.h>
#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_object_types.h>
#include <uf_modl.h>
#include <uf_view.h> 
#include <uf_layer.h>
#include <uf_part.h>
#include <uf_obj.h>
#include <stdio.h>
#include <string.h>
#include <uf_curve.h>

struct Solid_Array 
{ 
    tag_t *solid_array; /* Solids to shadow */
    int    num_of_solids; /*Number of solids */
}; /* passed to UF_create_shadow curves */

struct Shadow_Array   
{
    tag_t *shadow_curves; /* Array of shadow curves obtained */ 
    int   curve_count;  /* Number of curves */
};
  
#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133], messg[300] = "\0 ";

        UF_get_fail_message(irc, err);
        printf (messg, "\n%s\nerror %d at line %d in %s\n%s",
            err, irc, line, file, call);
        printf("%s\n", messg);
        if (strlen(messg) > 300)
            printf("Error is too long - memory overwrite occurred!\n");
        strcpy(&messg[129], "...");
        uc1601(messg, TRUE);  /* Internal only - remove for external */
    }
    return(irc);
}

static void do_it(void)
{
    char view[30] = "\0 "; 
    tag_t  part_tag = UF_PART_ask_display_part() ; 
    struct Solid_Array solids;
    struct Shadow_Array shadow_result;   
    tag_t  view_tag, solid_tag = NULL_TAG;          
    int type,ii;
    type= UF_solid_type; 
    solids.solid_array = (tag_t * ) malloc(10*sizeof(tag_t)) ;
    solids.num_of_solids = 0 ; 
    printf ("part_tag is %d\n" , part_tag); 

    for ( UF_OBJ_cycle_objs_in_part(part_tag, type, &solid_tag);
          solid_tag != NULL_TAG;  
          UF_OBJ_cycle_objs_in_part(part_tag, type, &solid_tag))     /*Extract the solids from part */ 
    { 
        int type1, subtype1, layer_status; 
        UF_OBJ_disp_props_t disp_props; 
        UF_OBJ_ask_type_and_subtype( solid_tag, &type1, &subtype1); 
        UF_OBJ_ask_display_properties(solid_tag, & disp_props); /* find the layer status of the solid */
        UF_LAYER_ask_status(disp_props.layer, &layer_status);
        
        if (subtype1 != UF_solid_body_subtype ||
            disp_props.blank_status == UF_OBJ_BLANKED   /* make sure the solid is on selectable layer */
            || layer_status ==  UF_LAYER_INACTIVE_LAYER 
            || layer_status == UF_LAYER_REFERENCE_LAYER ) 
            continue;
          
        if ( solids.num_of_solids % 10 == 0 && solids.num_of_solids != 0 ) 
        {  
            int temp = solids.num_of_solids/10;
            solids.solid_array = (tag_t * ) realloc(solids.solid_array, (temp+1)*10 *sizeof(tag_t)) ;
            printf ("reallocating \n" ); /*If more than 10 solids make room for more */
        }
        solids.solid_array[solids.num_of_solids ++ ] = solid_tag ;        
        printf( "Inside the loop\n" ); 
        printf( "number of solids is : %d ", solids.num_of_solids ); 
        printf ("Solid tag is: %d \n ", solid_tag); 
    }
    
    UF_VIEW_ask_tag_of_view_name(view, &view_tag);  /*Ask view tag of work view (pass blank as first parameter */
    printf("view tag is : %d \n ", view_tag); 
    printf ("Number of solids : %d\n ", solids.num_of_solids); 
    for(ii = 0; ii < solids.num_of_solids; ii ++ ) 
        printf( "%d solid tag is : %d \n ", ii, solids.solid_array[ii]); 

    /*extract the shadow curves */
    UF_CALL( UF_CURVE_create_shadow_curves(solids.num_of_solids, solids.solid_array,view_tag,
                                            &shadow_result.curve_count, 
                                            &shadow_result.shadow_curves)) ;

    printf( " Number of curves in our case %d\n " , shadow_result.curve_count); 
    printf ("beginning to write the curves...\n" ); 
    for (ii = 0 ; ii < shadow_result.curve_count; ii++ ) 
    {
        printf ( "The curves are %d\n ", shadow_result.shadow_curves[ii]); 
    } /*print the curves to verify result - debugging purposes */
    
    UF_free(shadow_result.shadow_curves);
    free( solids.solid_array);
    
} 

void ufusr(char *param, int *retcode, int paramLen)
{
    if (UF_CALL(UF_initialize())) return;
    printf ("Inside ufusr before excecuting do_it \n" ); 
    do_it();
    UF_terminate();

}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}

