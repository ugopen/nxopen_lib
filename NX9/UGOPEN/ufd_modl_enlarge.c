/*==================================================================================================

                    Copyright (c) 2000 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved
====================================================================================================*/

 /******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *      UF_MODL_create_enlarge()                                              *
 *      UF_MODL_edit_enlarge()                                                *
 *      UF_MODL_ask_enlarge()                                                 *
 *                                                                            *    
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates      *
 *   an enlarge feature, reads the data from it and then edits the enlarge    *
 *   type and size.                                                           *
 *                                                                            *
 *                *
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_modl_freeform.h>
#include <uf_ui_ugopen.h>

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
    int    knot_fixup, pole_fixup;
    tag_t  bsurf, feat_obj_tag, base_face, face;

    int    bsurf_idata[4]  = {4,4,4,4};
    double bsurf_uknot[8]  = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0};
    double bsurf_vknot[8]  = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0};
    double bsurf_poles[64] = {0.0,0.0,6.0,1.0,
                              2.0,2.0,6.0,1.0,
                              5.0,1.5,6.0,1.0,
                              8.0,3.0,6.0,1.0,
                              0.0,2.0,4.0,1.0,
                              2.0,4.0,4.0,1.0,
                              5.0,3.5,4.0,1.0,
                              8.0,5.0,4.0,1.0,
                              0.0,2.0,2.0,1.0,
                              2.0,4.0,2.0,1.0,
                              5.0,3.5,2.0,1.0,
                              8.0,5.0,2.0,1.0,
                              0.0,0.0,0.0,1.0,
                              2.0,2.0,0.0,1.0,
                              5.0,1.5,0.0,1.0,
                              8.0,3.0,0.0,1.0};
    int     type = 0, ask_type, edit_type = 1, idx = 0;
    double  tol = 0.001, ask_tol;
    char    *size[4] = {"80", "60", "80", "80"};
    char    *ask_size[4], *edit_size[4] = {"60", "50", "60", "60"}; 
    uf_list_p_t  face_list;
    char    message[133];

/*Initialization */
    face = NULL_TAG;
    ask_type = 0;
    ask_tol = 0;

/* Create the b-surface */
    UF_CALL(UF_MODL_create_bsurf(bsurf_idata[0],
                                 bsurf_idata[1],
                                 bsurf_idata[2],
                                 bsurf_idata[3],
                                 bsurf_uknot,
                                 bsurf_vknot,
                                 bsurf_poles,
                                 &bsurf,
                                 &knot_fixup,
                                 &pole_fixup));

/* Get face tag from body tag */
    UF_CALL(UF_MODL_ask_body_faces(bsurf, &face_list));
    UF_CALL(UF_MODL_ask_list_item (face_list, idx, &base_face));

/* Enlarge the sheet */
    UF_CALL(UF_MODL_create_enlarge(base_face, type, size, tol, &feat_obj_tag));

/* Ask the created data from the sheet */
    UF_CALL(UF_MODL_ask_enlarge(feat_obj_tag, &face, &ask_type, ask_size, &ask_tol));

/* Edit the enlarged sheet */
    UF_CALL(UF_MODL_edit_enlarge(feat_obj_tag, edit_type, edit_size, tol));
  
    if(ask_size[0] != NULL) UF_free(ask_size[0]);
    if(ask_size[1] != NULL) UF_free(ask_size[1]);
    if(ask_size[2] != NULL) UF_free(ask_size[2]);
    if(ask_size[3] != NULL) UF_free(ask_size[3]);

}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
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
