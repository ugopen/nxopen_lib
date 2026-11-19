
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright 2012 Siemens Product Lifecycle Management Software Inc. *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support ask point containment:
 *
 *      UF_MODL_ask_point_containment
 *
 * ========================================================================== */


#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_evalsf.h>
#include <uf_ui.h>


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

  char    *edge_length[3] = {"5.0", "5.0", "5.0"};
  const char    *prtnam = "ask_uvpoint_containment"; 

  double  origin[3] = {0.0, 0.0, 0.0};
        
  tag_t   face_tag;
  tag_t   feat_tag;
  tag_t   part_tag;

  uf_list_p_t face_list;

  UF_EVALSF_p_t face_evaluator;
  int set_length = 10 ;
  double uvbox[4],*u_params,*v_params;
  int i,j=0,*points_containment,error_code;

  UF_FEATURE_SIGN create = UF_NULLSIGN;

  /* 
  Open a new part 
  */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /*
  Create a block of dimensions 5, 5, 5 
  */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_length, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_faces(feat_tag, &face_list));
  UF_CALL(UF_MODL_ask_list_item(face_list,1,&face_tag));

  /*
  Get the uv parameter box for the face.
  */
  UF_CALL(UF_EVALSF_initialize(face_tag,&face_evaluator));
  UF_CALL(UF_EVALSF_ask_face_uv_minmax(face_evaluator,uvbox));
  UF_CALL(UF_EVALSF_free(&face_evaluator));

  /* fill up array of u and v parameters to search*/
  u_params = (double *)UF_allocate_memory(set_length*sizeof(double),&error_code);
  v_params = (double *)UF_allocate_memory(set_length*sizeof(double),&error_code);
  points_containment = (int *)UF_allocate_memory(set_length*sizeof(int),&error_code);

  u_params[0] = uvbox[0] ;
  v_params[0] = uvbox[2] ;
  for (j = 1; j < set_length; j++)
  {
    u_params[j] = u_params[j-1] + ((uvbox[1] - uvbox[0])/(set_length - 1.0)) ;
    v_params[j] = v_params[j-1] + ((uvbox[3] - uvbox[2])/(set_length - 1.0)) ;
  }

  /*
  We are going to make multiple calls to the ask containment function - we get faster results
  if we initalize this face for that operation.
  */
  UF_CALL(UF_MODL_set_containment(face_tag) ) ; 

  /*
  Make the containment calls.
  */
  for (i = 0; i < set_length; i++)
  {
      /*
      Ask for containment
      */
      UF_CALL(UF_MODL_ask_uv_points_containment(1,&u_params[i],&v_params[i],face_tag,points_containment)) ;
  }

  /*
  Done with the memory used in containment checks - free it.
  */
  UF_free(u_params);
  UF_free(v_params);
  UF_free(points_containment);

  /*
  Done with this face, free the data generated to improve processing speed.
  */
  UF_CALL(UF_MODL_unset_containment(face_tag) ) ;

  return;
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

