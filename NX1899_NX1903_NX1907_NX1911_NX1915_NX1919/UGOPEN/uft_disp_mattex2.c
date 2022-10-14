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

These routines are used to query material/texture assigned to the bodies and 
apply them to the facetted bodies. 

The following program requires "glass_assembly.prt" to be opened.
The part has the following objects and materials:

   + material  "Ripple" is assigned to glass 1 at the component level
   + material  "Red glass" is assigned to glass 2 at the top assembly level
   no material is assigned to facetted body 

The test will show how material is obtained from assembly level and component
level so they can be applied to the facetted bodies in the corresponding levels.. 

Internal Functions:
   ufusr




==============================================================================*/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_cfi_types.h>
#include <uf_disp_ugopenint.h>
#include <uf_assem.h>

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
   tag_t part_tag;
}  UFT_DISP_MATTEX_materials_list_t, * UFT_DISP_MATTEX_materials_list_p_t;

static tag_t facet_body_list[20];

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
   bodies found in the same part. */ 

static void apply_mattex_to_faceted_bodies(
   UFT_DISP_MATTEX_materials_list_t * mat)
{
   int type;
   tag_t facet_body_tag = NULL_TAG;
   tag_t material_tag;
   int f_index = 0;
   tag_t part_tag;
   tag_t current_display_part_tag;
   int i;

   type = UF_faceted_model_type; /* same as RM_facet_topology_type*/
   current_display_part_tag = UF_PART_ask_display_part();

   if(current_display_part_tag != mat->part_tag)
   {
      /* make the material part the current_display display part*/ 
      UF_PART_set_display_part(mat->part_tag);
      UF_ASSEM_set_work_part(mat->part_tag);
   }

   part_tag = mat->part_tag;

   for ( UF_OBJ_cycle_objs_in_part(part_tag, type, &facet_body_tag);
          facet_body_tag != NULL_TAG && f_index <3;  
          UF_OBJ_cycle_objs_in_part(part_tag, type, &facet_body_tag))    
   {
         facet_body_list[f_index++] = facet_body_tag;
   }

   material_tag = mat->material_tag;

   for(i=0;i<f_index;i++)
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
    int type, status; 
    int debug = 0; 
    static UFT_DISP_MATTEX_materials_list_t materials_list[4];
    int m_index = 0;
    int material_found = false;
  

    printf ("================= do_it entered ================\n");
    printf ("part_tag = %d\n" , part_tag);


    type = UF_solid_type; 
 
    /* get all the materials textures assigned to UF_solid_type objects and 
    store them in the materials_list */ 


    /* material assigned at assembly level overrides material assigned at component level - 
    so look for material at top assembly level first.  If not found, then
    check for material at the component level */
    for ( UF_OBJ_cycle_objs_in_part(part_tag, type, &feature_tag);
          feature_tag != NULL_TAG && m_index <3;  
          UF_OBJ_cycle_objs_in_part(part_tag, type, &feature_tag))    
        
    { 
        char material_name[512];
        tag_t material_tag;
        logical is_occurrence;

        material_name[0] = '\0';
        UF_DISP_ask_material(feature_tag, &material_tag, material_name);

       if(material_tag == NULL_TAG)
       {
           tag_t proto_eid;
           tag_t component_part_tag;

           /* no material was found in the asembly level, check for component level*/
           is_occurrence = UF_ASSEM_is_occurrence(feature_tag);
           if(is_occurrence)
           {
               proto_eid = (tag_t) UF_ASSEM_ask_prototype_of_occ( feature_tag );
               UF_DISP_ask_material(proto_eid, &material_tag, material_name);
               UF_OBJ_ask_owning_part(proto_eid, &component_part_tag);
               materials_list[m_index].part_tag = component_part_tag;
           }
       }
       else
       {
          materials_list[m_index].part_tag = part_tag;
       }

       

        /* only interested in testing with these materials:
        "Ripple" is assigned to glass 1 at the component level
        "Red glass" is assigned to glass 2 at the top assembly level
        This test will demonstrate getting of material from top assembly
        body and component level and assign them to facetted body.
         */

        if(material_tag != 0 && ((!strcmp(material_name, "Ripple")) ||
             (!strcmp(material_name, "Red glass"))))
        {
           material_found = true;

           materials_list[m_index].material_tag = material_tag;
           strcpy(materials_list[m_index].material_name, material_name);

           m_index++;
        }
    } 

    if(material_found)
    {
       apply_mattex_to_faceted_bodies( &materials_list[0]);

       apply_mattex_to_faceted_bodies( &materials_list[1]);

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
