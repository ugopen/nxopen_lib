/*===================================================================

        Copyright (c) 2002  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routines:        *
 *                                                                            *
 *         UF_DIE_ask_draw_faces                                              *
 *         UF_DIE_ask_material_properties                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part containing one of each of    *
 *   the following features:                                                  *
 *       DIE_BINDER_RING                                                      *
 *       DIE_FACE                                                             *
 *   and a product sheet body with material properites associated.            *
 *                                                                            *
 *   This function will make three calls to UF_DIE_ask_draw_faces,            *                                                    
 *   one for each of the types of faces we want to find and highlight         *
 *   each set of faces with an informational message.  Finally, it            * 
 *   will make a call to UF_DIE_ask_material_properties to find the sheet     *
 *   metal thickness and material properties and display the thickness        *
 *   and material name in an infomrational message.                           *
 *                                                                            *
                   *
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>

#include <uf.h>
#include <uf_defs.h>
#include <uf_dieeng.h>
#include <uf_disp.h>
#include <uf_ui.h>
#include <uf_sf.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char    messg[133];
        printf("%s, line %d:  %s\n", file, line, call);
        (UF_get_fail_message(irc, messg)) ?
            printf("    returned a %d\n", irc) :
            printf("    returned error %d:  %s\n", irc, messg);
    }
    return(irc);
}

static void do_ugopen_api(void)
{

  tag_t material_type_tag, *faces;
  double metal_thickness;

  int num_faces, response, ii;  
  int highlight = 1, unhighlight = 0;

  char *binder_faces_msg = "Binder Ring faces are highlighted";
  char *punch_faces_msg = "Die Punch faces are highlighted";
  char *die_face_faces_msg = "Die Face faces are highlighted";
  char material_msg[ MAX_LINE_BUFSIZE ], *string_msg;
  char *material_name;

  UF_SF_material_prop_t material_properties;

  /* Find faces for binder ring */
  UF_CALL(UF_DIE_ask_draw_faces(0,  /* ask for binder ring faces */
                                &num_faces,
                                &faces));
  
  /* Highlight faces for binder ring */
  for (ii=0; ii<num_faces; ii++)
      UF_DISP_set_highlight(faces[ii],highlight);
  UF_UI_message_dialog( "", UF_UI_MESSAGE_INFORMATION, &binder_faces_msg, 1, TRUE, NULL, &response );
  for (ii=0; ii<num_faces; ii++)
      UF_DISP_set_highlight(faces[ii],unhighlight);  
  
  if (faces)
      UF_free(faces);
  
  /* Find faces for punch */
  UF_CALL(UF_DIE_ask_draw_faces(1,  /* ask for die punch faces */
                                &num_faces,
                                &faces));

  /* Highlight faces for punch */
  for (ii=0; ii<num_faces; ii++)
      UF_DISP_set_highlight(faces[ii],highlight);
  UF_UI_message_dialog( "", UF_UI_MESSAGE_INFORMATION, &punch_faces_msg, 1, TRUE, NULL, &response );
  for (ii=0; ii<num_faces; ii++)
      UF_DISP_set_highlight(faces[ii],unhighlight);

  if (faces)
      UF_free(faces);
  
  /* Find faces for die face */
  UF_CALL(UF_DIE_ask_draw_faces(2,  /* ask for die face faces */
                                &num_faces,
                                &faces));

  /* Highlight faces for die face */
  for (ii=0; ii<num_faces; ii++)
      UF_DISP_set_highlight(faces[ii],highlight);
  UF_UI_message_dialog( "", UF_UI_MESSAGE_INFORMATION, &die_face_faces_msg, 1, TRUE, NULL, &response );
  for (ii=0; ii<num_faces; ii++)
      UF_DISP_set_highlight(faces[ii],unhighlight);

  if (faces)
      UF_free(faces);
  
  /* Find part thickness and material properties */
  UF_CALL(UF_DIE_ask_material_properties(&metal_thickness,  /* ask for die face faces */
                                         &material_type_tag));

  /* Display message with thickness and material property name */
  if (material_type_tag)
  {
      UF_SF_ask_material(material_type_tag,
                         &material_name,
                         &material_properties);

      UF_SF_free_matl_prop(&material_properties);

      sprintf(material_msg,"Metal Thickness %f, Material Name %s",
              metal_thickness, material_name);
      string_msg = material_msg;
      UF_UI_message_dialog( "", 
                            UF_UI_MESSAGE_INFORMATION, 
                            &string_msg, 
                            1, 
                            TRUE, 
                            NULL, 
                            &response );
      UF_free(material_name);
  }
  /* No material property, just display message with thickness */
  else
  {
      sprintf (material_msg,"Metal Thickness %f",
               metal_thickness);
      string_msg = material_msg;
      UF_UI_message_dialog( "", 
                            UF_UI_MESSAGE_INFORMATION, 
                            &string_msg, 
                            1, 
                            TRUE, 
                            NULL, 
                            &response );      
  }
                     
  
}
/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
{
    if (!UF_CALL(UF_initialize()))
    {
        do_ugopen_api();
        UF_CALL(UF_terminate());
    }
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
