/*=============================================================================

                                 Copyright (c) 2006 UGS Corp. 
                             Unpublished - All rights reserved
===============================================================================
File description:
This file demonstrates the use of the following UFUN APIs:
UF_DISP_ask_material
UF_DISP_copy_material
UF_DISP_ask_texture_space_info
UF_DISP_set_texture_space_info
UF_DISP_delete_material

These routines are used to query material/texture assigned to the bodies and 
apply them to the facetted bodies. 

Internal Functions:
   ufusr

The following program requires "facetted_hood.prt" and "ugdecal24.tif" to be opened.



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


typedef struct UFT_DISP_MATTEX_materials_list_s
{
   tag_t material_tag;
   char material_name[ MAX_FSPEC_BUFSIZE ];
}  UFT_DISP_MATTEX_materials_list_t, * UFT_DISP_MATTEX_materials_list_p_t;

static tag_t facet_body_list[3];

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


/* this routine applies the material texture to all the UF_facet_model_type
   bodies. After the assignment, a HQI is generated and graphics window 
   display is updated if running internally */

static void apply_mattex_to_faceted_bodies(
   tag_t part_tag,
   UFT_DISP_MATTEX_materials_list_t * mat)
{
   int type;
   tag_t facet_body_tag = NULL_TAG;
   tag_t material_tag;
   int first_time = 1;
   int i;

   type = UF_faceted_model_type; /* same as RM_facet_topology_type*/

   if(first_time)
   {
      int f_index = 0;

      for ( UF_OBJ_cycle_objs_in_part(part_tag, type, &facet_body_tag);
          facet_body_tag != NULL_TAG && f_index <3;  
          UF_OBJ_cycle_objs_in_part(part_tag, type, &facet_body_tag))    
      {
         facet_body_list[f_index++] = facet_body_tag;
      }
      first_time = 0;
   }

   material_tag = mat->material_tag;

   for(i=0;i<3;i++)
   {
      UF_DISP_assign_material(material_tag, facet_body_list[i]);
   } 

   /*regenerate the display */
   UF_DISP_regenerate_display();
}



static void do_it(void)
{
    tag_t  part_tag = UF_PART_ask_display_part(); 
    tag_t  feature_tag = NULL_TAG;
    int type;
    int debug = 0; 
    static UFT_DISP_MATTEX_materials_list_t materials_list[4];
    int ug_logo_index= 0;
    int m_index = 0;
    int material_found = false;
  
    type = UF_solid_type; 
 
    /* get all the materials textures assigned to UF_solid_type objects and 
    store them in the materials_list */ 

    for ( UF_OBJ_cycle_objs_in_part(part_tag, type, &feature_tag);
          feature_tag != NULL_TAG && m_index <3;  
          UF_OBJ_cycle_objs_in_part(part_tag, type, &feature_tag))    
        
    { 
        char material_name[512];
        tag_t material_tag;

        material_name[0] = '\0';
        UF_DISP_ask_material(feature_tag, &material_tag, material_name);

        /* only interested in testing with these materials:
        both gold and blue marble are materials that don't require setting
        of texture space information.  ug_logo material may require 
        readjusting texture space information so that the logo will 
        appear correctly on the object */

        if(material_tag != 0 && ((!strcmp(material_name, "ug_logo")) ||
             (!strcmp(material_name, "blue marble")) ||
             (!strcmp(material_name, "gold"))))
        {
           material_found = true;

           materials_list[m_index].material_tag = material_tag;
           strcpy(materials_list[m_index].material_name, material_name);

           if(!strcmp(material_name, "ug_logo"))
               ug_logo_index = m_index;
           m_index++;
        }
    } 

    /* go through all the facetted_bodies, assign these materials textures 
       to them one by one */

    if(material_found)
    {
       UF_DISP_texture_space_info_t ts_info;
       int ts_info_defined;

       /* apply first material texture to all facetted_bodies*/
       apply_mattex_to_faceted_bodies(part_tag, &materials_list[0]);

       /* apply second material  texture to all facetted_bodies*/
       apply_mattex_to_faceted_bodies(part_tag, &materials_list[1]);

       /* apply second material texture to all facetted_bodies*/
       apply_mattex_to_faceted_bodies(part_tag, &materials_list[2]);


       /* TEST change of texture space information */
       UF_DISP_ask_texture_space_info(materials_list[ug_logo_index].material_tag, 
            &ts_info, &ts_info_defined); 

       /* make sure this material texture contains texture space information*/
       if(ts_info_defined)
       {
          tag_t new_material_tag;
          char new_material_name[ MAX_FSPEC_BUFSIZE ];

          /* create new material for the facetted body 1*/
          UF_DISP_copy_material(materials_list[ug_logo_index].material_tag, 
                &new_material_tag, new_material_name);
          /* reajust origin, top left corner - so the logo will appear 
             on facetted body 1*/
          ts_info.origin[0] = 1221; 
          ts_info.origin[1] = -256; 
          ts_info.origin[2] = -177; 
          UF_DISP_set_texture_space_info(new_material_tag, &ts_info);
          UF_DISP_assign_material(new_material_tag, facet_body_list[0]);

          /* create another material for facetted body 2*/
          UF_DISP_copy_material(materials_list[ug_logo_index].material_tag, 
                &new_material_tag, new_material_name);
          /* increase the scale to make logo appear larger */
          ts_info.ts_scale = ts_info.ts_scale * 2; 
          /* reajust origin, top left corner - so it does not get clipped 
             at ll corner*/
          /* 1256 , 1444, -176*/ 
          ts_info.origin[0] = 1000; 
          ts_info.origin[1] = 1200; 
          UF_DISP_set_texture_space_info(new_material_tag, &ts_info);
          UF_DISP_assign_material(new_material_tag, facet_body_list[1]);

          /*regenerate the display */
          UF_DISP_regenerate_display();
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

#if 0
    UFT_DISP_test_material_texture(stdout);
#endif
    UF_terminate();
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
#endif /*BUILD_UFUSR */


#if 0
/****************************************************************************
 *
 *  FUNCTION:    UFT_DISP_test_material_texture(log)
 *
 *  DESCRIPTION: This function is the main test program used to test the
 *               material/texture APIs.
 *  INPUT:
 *               log    - output file
 *  RETURNS:
 *               0   => success
 *               > 0 => error code
 *
 ****************************************************************************/
extern int   UFT_DISP_test_material_texture (FILE *log)
{
    UF_PART_load_status_t load_status;
    tag_t                 part;
    int                   error_code = UFT_OBJ_NO_ERROR;

    error_code = UF_PART_open("facetted_hood.prt", &part, &load_status);
    PROCESS_ERROR(error_code);
    part_open = TRUE;
    do_it();
    return (UFT_OBJ_NO_ERROR);
}
#endif
