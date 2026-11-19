/*=============================================================================

        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                             Unpublished - All rights reserved
===============================================================================
File description:
This file demonstrates the use of the following UFUN APIs:
UF_DISP_ask_materials_in_part
UF_DISP_create_material

Prior to running this program user needs to:
 + Make sure they open the ufun_disp_mattex6_test.prt part first.

Internal Functions:
   ufusr

This program requires "ufun_disp_mattex6_test.prt". 

After loading the part, the program will get all the material from this part 
and then iterate each material and see if it's name is exist in the
material_swap_table's author_material_name list.If it is exist, program will 
create a new unique name irayplus material according to
the material_swap_table's system_irayplus_material_name.






==============================================================================*/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_cfi_types.h>
#include <uf_disp_ugopenint.h>

#define BUILD_UFUSR           1

#define UFT_OBJ_NO_ERROR      0

#define CLOSE_ALL_OPEN_PARTS \
    if (part_open) \
    { \
      UF_PART_close_all(); \
    } \

#define PROCESS_ERROR(error_code) \
  if (error_code != UFT_OBJ_NO_ERROR) \
  { \
    CLOSE_ALL_OPEN_PARTS \
    return (error_code); \
  }


typedef struct UFT_DISP_MATEX_material_swap_table_s
{
    char author_material_name[UF_CFI_MAX_FILE_NAME_BUFSIZE];
    char system_irayplus_material_name[UF_CFI_MAX_FILE_NAME_BUFSIZE];
} UFT_DISP_MATEX_material_swap_table_t, *UFT_DISP_MATEX_material_swap_table_p_t;


#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))


static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char    err[133], messg[300];

        UF_get_fail_message(irc, err);
        sprintf(messg, "\n%s\nerror %d at line %d in %s\n%s",
            err, irc, line, file, call);
        printf("%s\n", messg);
        if (strlen(messg) > 300)
            printf("Error is too long - memory overwrite occurred!\n");
        strcpy(&messg[129], "...");
    }
    return(irc);
}



static void do_it(void)
{
    tag_t   part_tag = UF_PART_ask_display_part(); 
    UFT_DISP_MATEX_material_swap_table_t material_swap_table[3] = {
        { "AuthorMaterial01", "Varnished Cherry" },
        { "AuthorMaterial02" ,"Blue Powder Coat"},
        { "AuthorMaterial03", "Glass Red" }
    };
    
    //Get all the irayplus materials of this part.
    int material_count = 0;
    int i = 0, j = 0, ii = 0;
    tag_t * material_tags = NULL;
    char ** material_names = NULL;
    int ask_result = UF_DISP_ask_materials_in_part(part_tag, UF_DISP_SH_IrayPlus, &material_count, &material_tags, &material_names);

    //iterate the returned material list to find out if it contain material in material_swap_table.
    if (material_count != 0 && ask_result == 0)
    {
        for (i = 0; i < material_count; i++)
        {
            for (j = 0; j < 3; j++)
            {
                if (strcmp(material_names[i], material_swap_table[j].author_material_name) == 0)
                {
                    //If found material which exist in material_swap_table in the returned material_names.
                    //Then use UF_DISP_create_material to create a new irayplus material according to system_irayplus_material_name
                    // in material_swap_table
                    tag_t new_material_tag = NULL_TAG;
                    char new_material_name[UF_SH_MAX_MAT_NAME_BUFSIZE];
                    int create_ret = UF_DISP_create_material(material_swap_table[j].system_irayplus_material_name, &new_material_tag, new_material_name);
                    if (create_ret != 0)
                        printf("Error during create material!\n");

                    //Then you could get all the linked object from this material.
                    tag_t   *objects;
                    int     object_count = 0;
                    UF_DISP_ask_geometry_of_material(material_tags[i], &object_count, &objects);

                    if (object_count > 0)
                    {
                        // reassign the new created material to object for replacing old converted material.
                        for (ii = 0; ii < object_count; ii++)
                        {
                            UF_DISP_remove_material_assignment(objects[ii]);
                            UF_DISP_assign_material(new_material_tag, objects[ii]);

                        }


                        UF_DISP_update_material_display_of_geometry(object_count, objects);


                        UF_free(objects);
                    }
                    UF_DISP_delete_material(material_tags[i]);

                    

                }
            }

                

            
        }
    }
    

    UF_free(material_tags);
    UF_free(material_names);

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
