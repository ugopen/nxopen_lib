/*=============================================================================

                                 Copyright (c) 2006 UGS Corp. 
                             Unpublished - All rights reserved
===============================================================================
File description:
This file demonstrates the use of the following UFUN APIs:
UF_DISP_update_material_display_of_geometry

These routines are used to just update the geometries that have been applied with
some material. The routines will not validate input objects that do not have material
applied.  It is up to the user to pass in a valid set of objects to be update.

Internal Functions:
   ufusr

The following program requires "ufun_update_mattex_test.prt". 

This user function comes with a test case of four different scenarios.  User will be prompted
to enter the scenario number to test.  Additional scenarios can be setup by the user by adding 
to the "switch" statement below depending on the individual testing preferences.



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
   char material_name[ MAX_FSPEC_BUFSIZE ];
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
    int blue_marble_material_index = 0;
  
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
           if(!strcmp(material_name, "blue marble"))
              blue_marble_material_index = material_found;
           material_found++;
        }
        
        UF_OBJ_cycle_objs_in_part(part_tag, type, &feature_tag);
    } 

    /* Go through some facetted_bodies & some faces of soild bodies (if existed). 
       Apply these materials textures to them one by one */
    if(material_found)
    {
        /* For faceted bodies */
        tag_t facet_body_tag = NULL_TAG;
        tag_t object_tag = NULL_TAG;
        int ii;
        int findex;
        int otype;
        int sindex;
        char    input[10] = {""};
        int     input_len, scenario_counter = 0;
        tag_t   list3[3];
        tag_t   *objects;
        int     object_count = 0;

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

        
        /* If "Ok" is selected, keep looping */
        while (uc1600("Please enter scenario number: 1 (retrieve objs), 2 (update objs), or 3 (update faces)", input, &input_len) == 5) 
        {
            sscanf(input, "%u", &scenario_counter);

            switch (scenario_counter)
            {
                case 1:
                /* Testing scenario: Retrieve objects with material2 applied to them -
                   and assign a different material 1 to them */
                UF_DISP_ask_geometry_of_material(materials_list[2].material_tag, &object_count, &objects);

                for (ii = 0; ii < object_count; ii++)
                {
                    UF_DISP_assign_material(materials_list[1].material_tag, objects[ii]);
                }

                if (object_count > 0)
                {
                    UF_DISP_update_material_display_of_geometry(object_count, objects);
                    UF_free(objects);
                }
                break;

                case 2:
                default:
                /*  Testing scenario: Update all objects in object list - 
                    We have applied three different materials, "clover", "gold", &
                    "blue_marble" to the three faceted bodies.
                 */  
                list3[0] = facet_body_list[0];
                list3[1] = facet_body_list[1];
                list3[2] = facet_body_list[2];
                UF_DISP_assign_material(materials_list[0].material_tag, list3[0]);
                UF_DISP_assign_material(materials_list[1].material_tag, list3[1]);
                UF_DISP_assign_material(materials_list[2].material_tag, list3[2]);
                UF_DISP_update_material_display_of_geometry(3, list3);
                break;

                case 3:
                // apply blue marble to all faces with magenta materials 
                for(ii=0; ii<face_list_count;ii++)
                    UF_DISP_assign_material(materials_list[blue_marble_material_index].material_tag, face_list[ii]); 
                UF_DISP_update_material_display_of_geometry(face_list_count , face_list);
                break;

                case 4:
                // apply blue_marble to all bodies  with cyan materials
                for(ii=0; ii<body_list_count;ii++)
                    UF_DISP_assign_material(materials_list[blue_marble_material_index].material_tag, body_list[ii]); 
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
