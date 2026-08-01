/*=============================================================================

        Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
                             Unpublished - All rights reserved
===============================================================================
File description:
This file demonstrates the use of the following UFUN APIs:
UF_DISP_open_LWA_archive_materials_library
UF_DISP_copy_LWA_archive_material_to_work_part
UF_DISP_remove_material_assignment
UF_DISP_update_material_display_of_geometry

Prior to running this problem user needs to:
 + make sure lwa_file_name is correctly set. 
 + make sure the materials to copy to work_part are from the lwa_file_name 
   otherwise the copy and assignment will fail.

Internal Functions:
   ufusr

This program requires "ufun_update_mattex_test.prt". 

After loading the part, the program will copy the following materials from lwa_file_name to the work part using UF_DISP_copy_LWA_archive_material_to_work_part:
+ Grid black 1/8
+ Webbing
+ Pink shoe leather
NOTE: these materials are from the NX shipped lwpda.lwa (in ugphoto kits).

This user function comes with a test case of four different scenarios.  User will be prompted
to enter the scenario number to test.  Additional scenarios can be setup by the user by adding 
to the "switch" statement below depending on the individual testing preferences.

Scenario 1: apply pink shoe leather material to all faces with magenta materials 
After this scenario, the magenta block will have pink show leather material applied to it.

Scenario 2: apply webbing material to all facet_bodies list 
After this test, the sheet bodies in the middle row of the part will all have webbing material applied to them.

Scenario 3: apply grid_black  material to all faces with cyan materials 
After this test, the two cyan blocks on the top row will have grid black material applied to them.

Scenario 4: assign none to all body with original cyan_material
After this test, the two original cyan blocks will became pink (the body color), since the material has been removed from them.



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


typedef struct UFT_DISP_MATTEX_materials_list_s
{
   tag_t material_tag;
   char material_name[ UF_CFI_MAX_FILE_NAME_BUFSIZE];
}  UFT_DISP_MATTEX_materials_list_t, * UFT_DISP_MATTEX_materials_list_p_t;

static tag_t facet_body_list[6]={NULL_TAG, NULL_TAG, NULL_TAG, NULL_TAG, NULL_TAG, NULL_TAG};
static tag_t body_list[6];
static tag_t face_list[6];
static int face_list_count =0;
static int body_list_count = 0;

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

static logical not_added_material(
    UFT_DISP_MATTEX_materials_list_t * material_list,
    char* material_name)
{
    int i;
    for(i=0;i<5;i++)
    {
       if(strcmp(material_name, material_list[i].material_name) == 0)
         return false;
    }
    return true;
}

static void do_it(void)
{
    tag_t   part_tag = UF_PART_ask_display_part(); 
    tag_t   feature_tag = NULL_TAG;
    int     type = UF_solid_type;
    int subtype;
    int     material_found = 0;
    UFT_DISP_MATTEX_materials_list_t materials_list[5] = {0, 0};
    char    material_name[512];
    tag_t   material_tag;
    char lwa_file_name[ UF_CFI_MAX_FILE_NAME_BUFSIZE];
  
    /* get all the materials textures assigned to UF_solid_type objects and 
       store them in the materials_list */ 

    UF_OBJ_cycle_objs_in_part(part_tag, type, &feature_tag);
    while(feature_tag != NULL_TAG)
    { 
        material_name[0] = '\0';
        UF_DISP_ask_material(feature_tag, &material_tag, material_name);

        /* only interested in testing with these materials */
        if( material_tag != 0 &&  material_found <5 &&
            not_added_material(materials_list, material_name) &&
            ((!strcmp(material_name, "clover")) ||
             (!strcmp(material_name, "blue marble")) ||
             (!strcmp(material_name, "gold")) ||
             (!strcmp(material_name, "magenta")) ||
             (!strcmp(material_name, "cyan"))))
        {
           materials_list[material_found].material_tag = material_tag;
           strcpy(materials_list[material_found].material_name, material_name);
           material_found++;
        }
        
        UF_OBJ_cycle_objs_in_part(part_tag, type, &feature_tag);
    } 

    /* Go through some facetted_bodies & some faces of soild bodies (if existed). 
       Apply these materials textures to them one by one */
    if(material_found)
    {
        /* For faceted bodies */
        tag_t object_tag = NULL_TAG;
        int ii;
        int findex;
        int otype;
        int sindex;
        char    input[10] = {""};
        int     input_len, scenario_counter = 0;
        tag_t   list3[3];
        tag_t grid_black_material_tag = NULL_TAG;
        tag_t webbing_material_tag = NULL_TAG;
        tag_t pink_shoe_leather_material_tag = NULL_TAG;

        type = UF_faceted_model_type; /* same as RM_facet_topology_type*/
        UF_OBJ_cycle_objs_in_part(part_tag, type, &object_tag);

        for ( ii = 0; (object_tag!= NULL_TAG)  ; ii++)
        {
            if(ii<6)
                facet_body_list[ii] = object_tag;
            
            UF_OBJ_cycle_objs_in_part(part_tag, type, &object_tag);
        }


        // gather all faces with magenta materials
        type = UF_solid_type;
        UF_OBJ_cycle_objs_in_part(part_tag, type, &object_tag);
        findex = 0;
        while (object_tag != NULL_TAG)
        {
            UF_OBJ_ask_type_and_subtype(object_tag,&otype,&subtype);
            if(subtype == UF_solid_face_subtype) 
            {
                material_name[0] = '\0';
                UF_DISP_ask_material(object_tag, &material_tag, material_name);
                if(!strcmp(material_name, "magenta") && findex <6)
                {
                    face_list[findex++] = object_tag;
                }
            }
            UF_OBJ_cycle_objs_in_part(part_tag, type, &object_tag);
        }
        face_list_count = findex;


        // gather all bodies with cyan material
        type = UF_solid_type;
        UF_OBJ_cycle_objs_in_part(part_tag, type, &object_tag);
        sindex = 0;
        while(object_tag != NULL_TAG)
        {
            UF_OBJ_ask_type_and_subtype(object_tag,&otype,&subtype);
            if(subtype == UF_solid_body_subtype)
            {
                material_name[0] = '\0';
                UF_DISP_ask_material(object_tag, &material_tag, material_name);
                if(!strcmp(material_name, "cyan") && sindex <6)
                    body_list[sindex++] = object_tag;
            }
            UF_OBJ_cycle_objs_in_part(part_tag, type, &object_tag);
        }
        body_list_count = sindex;

        // Please make sure the lwa_file_name is set up correctly.

        strcpy(lwa_file_name, "E:\\workdir\\nx9_13_reference\\wntx64\\kits\\ugphoto\\lwpda.lwa");

        if(UF_DISP_open_LWA_archive_materials_library(lwa_file_name) == 0)
        {
            // Please make sure the materials to copy to work part are the ones found in the materials archive library specified by lwa_file_name.
            UF_DISP_copy_LWA_archive_material_to_work_part("Grid black 1/8\"", &grid_black_material_tag);
            UF_DISP_copy_LWA_archive_material_to_work_part("Webbing", &webbing_material_tag);
            UF_DISP_copy_LWA_archive_material_to_work_part("Pink shoe leather", &pink_shoe_leather_material_tag);
        }
        
        /* If "Ok" is selected, keep looping */
        while (uc1600("Please enter scenario number: 1 (apply pink shoe leather), 2 (apply webbing to facet_bodies), 3 (apply grid_black), or 4(assign none)", input, &input_len) == 5) 
        {
            sscanf(input, "%u", &scenario_counter);

            switch (scenario_counter)
            {
                case 1:
                // apply pink shoe leather material to all faces with magenta materials 
                for(ii=0; ii<face_list_count;ii++)
                    UF_DISP_assign_material(pink_shoe_leather_material_tag, face_list[ii]); 
                UF_DISP_update_material_display_of_geometry(face_list_count , face_list);
                break;

                case 2:
                default:
                /*  Testing scenario:  apply webbing material to all facet_bodies list */
                list3[0] = facet_body_list[0];
                list3[1] = facet_body_list[1];
                list3[2] = facet_body_list[2];
                UF_DISP_assign_material(webbing_material_tag, list3[0]);
                UF_DISP_assign_material(webbing_material_tag, list3[1]);
                UF_DISP_assign_material(webbing_material_tag, list3[2]);
                UF_DISP_update_material_display_of_geometry(3, list3);
                break;

                case 3:
                // apply grid_black  material to all bodies with cyan materials 
                for(ii=0; ii<body_list_count;ii++)
                    UF_DISP_assign_material(grid_black_material_tag, body_list[ii]); 
                UF_DISP_update_material_display_of_geometry(body_list_count , body_list);
                break;
  
                case 4:
                // assign none to all bodies with original cyan_material
                for(ii=0; ii<body_list_count;ii++)
                    UF_DISP_remove_material_assignment(body_list[ii]); 
                UF_DISP_update_material_display_of_geometry(body_list_count , body_list);
                break;
            }

            input[0] = '\0';

        } /* end while() */
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
