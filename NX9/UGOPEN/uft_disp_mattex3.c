/*=============================================================================

           Copyright 2009  Siemens Product Lifecycle Management Software Inc.
              All rights reserved.

===============================================================================
File description:
This file demonstrates the use of the following UFUN APIs:
UF_DISP_ask_material
   This routine is used to query material/texture assigned to the geometry(body, face or facetted bodies) 

UF_DISP_ask_currently_selected_material
   This routine is used to query currently selected material/texture in the Materials in Part palette

UF_DISP_ask_work_part_material_lwa_user_data_area
   This routine is used to get the work part material LWA user area data based on the material tag and the
   attribute string key.

UF_DISP_ask_library_material_lwa_user_data_area
   This routine is used to get the library material LWA user area data based on the material_full_archive_file 
   and the attribute string key.

The program shows how thedr new APIs allow user to find the currently selected material 
in both the Materials in Part palette and/or the Materials library.  
From there user can access the LWA user area data for the selected material.  

This programs requires a lwa files containing material specifiation in the LWA user area.
Work Flow:
1.Create a new part.  
2.Activate Material Texture context.
3.Open an lwa file with specification attributes in the LWA user area from the Material Library Navigator.
4.Select any of the materials in this library and run test_iuf on the selected material. 
5. Copy any of the materials to Part(MB3). 
6. Select the copied materials in the "Materials in Part" palette and run test_iuf on the material.. 
This test will get the LWA user area data info attributes for the selected material.
NOTE: the program assumes the specification attributes to contain these string key name:
"Surface Code", "Base Color Code", "BaseProcessing". 


Internal Functions:
   ufusr





==============================================================================*/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_ui.h>
#include <uf_cfi_types.h>
#include <uf_disp_ugopenint.h>

#define BUILD_UFUSR           1

#define UFT_OBJ_NO_ERROR      0

static logical part_open = FALSE;

#define CLOSE_ALL_OPEN_PARTS \
    if (part_open) \
    { \
      UF_PART_close_all(); \
      part_open = FALSE; \
    } \

#define PROCESS_ERROR(error_code) \
  if (error_code != UFT_OBJ_NO_ERROR) \
  { \
    CLOSE_ALL_OPEN_PARTS \
    return (error_code); \
  }

#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char
            err[133],
            messg[300];

        UF_get_fail_message(irc, err);
        sprintf(messg, "\n%s\nerror %d at line %d in %s\n%s",
            err, irc, line, file, call);
        printf("%s\n", messg);
        if (strlen(messg) > 300)
            printf("Error is too long - memory overwrite occurred!\n");
        strcpy(&messg[129], "...");
        /*uc1601(messg, TRUE);*/  /* Internal only - remove for external */
    }
    return(irc);
}


static char* check_string_key [3] = {
    "Base Color Code", //293048
    "Base Processing",  //brushed
    "Surface Code"     //383762
};

static void do_it(void)
{
    int selected_mat_error = ERROR_OK;
 
    tag_t currently_selected_material_tag = NULL_TAG;
    char selected_material_full_archive_name[ MAX_FSPEC_BUFSIZE ];
    const char *attribute_data = NULL;
    int result;
    int j,m;

    UF_DISP_material_source_t material_source;

    selected_mat_error = UF_DISP_ask_currently_selected_material(&material_source, &currently_selected_material_tag, 
        selected_material_full_archive_name);

    if(selected_mat_error == ERROR_OK)
    {
        if(material_source == UF_DISP_lw_material_in_Materials_in_Part_Palette && currently_selected_material_tag != NULL_TAG)
        {
             for(j=0;j<3;j++)
             {
                 // attribute_data is only valid if result is ERROR_OK
                 result = UF_DISP_ask_work_part_material_lwa_user_area_data(currently_selected_material_tag, 
                     check_string_key[j], &attribute_data);
             }
        }
        else if(material_source == UF_DISP_lw_material_in_Materials_Library && strlen(selected_material_full_archive_name) > 1)
        {
             for(m=0;m<3;m++)
             {
                 // attribute_data is only valid if result is ERROR_OK
                 result = UF_DISP_ask_library_material_lwa_user_area_data( selected_material_full_archive_name,
                     check_string_key[m], &attribute_data);
             }
        }
    }
}
              
        
  
#if BUILD_UFUSR
/****************************************************************************
 *
 *  FUNCTION:    ufusr(param, retcod, param_len)
 *
 *  DESCRIPTION: This is the entry point for Internal User Function
 *               programs.  The parameters are unused.
 *
 ****************************************************************************/
/*ARGSUSED*/
extern void ufusr(char *param, int *retcode, int paramLen)
{
    if (UF_CALL(UF_initialize())) return;

    do_it();

    UF_terminate();
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
#endif /*BUILD_UFUSR */

