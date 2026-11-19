/*===================================================================

        Copyright (c) 1998 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_reparam_sheet                                       *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates two  *
 *   reparameterized B-surfaces. The smaller of the two surfaces uses a       *
 *   B-surface as a driver. The larger of the two surfaces uses four lines    *
 *   (a rectangle) as driver curves.                                          *
 *                                                                            *
                   
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include<math.h>
#include <uf_modl.h>
#include <uf.h>
#include <uf_curve.h>

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
  double pole1[64];
  double pole2[64];
  double pole3[64];
  double pole4[64];
  double pole5[64];
  double pt1[3] = {0.1,-2.9,1.5};
  double pt2[3] = {0.1,2.9,1.5};
  double pt3[3] = {6.0,2.9,1.5};
  double pt4[3] = {6.0,-2.9,1.5};
  double u_knot[9] = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0};
  double v_knot[9] = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0};
  double weight = 1.0;
  double proj_vec[3] = {0.0,0.0,-1.0};
  double tols1[5] = {0.01,90.0,0.001,90.0,0.0};
  double tols2[5] = {0.01,90.0,0.001,90.0,0.0};
  int num_pole_u = 4;
  int num_pole_v = 4;
  int u_ord = 4;
  int v_ord = 4;
  int knot1_fix;
  int pole1_fix;

  int i,j,k = 0,l = 0,m = 0,n = 0,p = 0;
  int proj_type1 = 1;
  int proj_type2 = 0;
  int drv_type1 = 1;
  int drv_type2 = 0;
  int check_overlap = 0;
  int num_primary = 2;
  int num_cross = 2;
  int num_fs = 4;
  int tol_achieved;
  int count[5];
  tag_t bsurf[4];
  tag_t driv_surf;
  tag_t faces[4];
  tag_t driver_face;
  tag_t prim_cvs[2];
  tag_t cros_cvs[2];
  tag_t new_face;
  uf_list_p_t face_list1;
  uf_list_p_t face_list2;
  uf_list_p_t face_list3;
  uf_list_p_t face_list4;
  uf_list_p_t face_list5;
  UF_CURVE_line_t line_coords;
/* Create and load the homogeneous arrays. */
     
  for(i = 0; i < 4; i++){
    for(j = 0; j < 4; j++){
      pole1[k++] = i;
      pole1[k++] = j;
      pole1[k++] = sin(i/(i+.9));
      pole1[k++] = weight;
    }
   }
  for(i= 0; i < 4; i++){
     for(j = 0; j < 4; j++){
      pole2[l++] = i+3.1;
      pole2[l++] = j;
      pole2[l++] = -cos(i/(i+.9)) + 1.695;
      pole2[l++] = weight;
    }
   }
 
  for(i= 0; i < 4; i++){
     for(j = 0; j < 4; j++){
      pole3[m++] = i;
      pole3[m++] = j+(-3.1);
      pole3[m++] = sin(i/(i+.9));
      pole3[m++] = weight;
    }
   }      
  for(i= 0; i < 4; i++){
     for(j = 0; j < 4; j++){
      pole4[n++] = i+3.1;
      pole4[n++] = j+(-3.1);
      pole4[n++] = -cos(i/(i+.9)) + 1.695;
      pole4[n++] = weight;
    }
   }
  for(i= 0; i < 4; i++){
     for(j = 0; j < 4; j++){
      pole5[p++] = i*1.4+0.9;
      pole5[p++] = j*(-1.6)+2.4;
      pole5[p++] = sin((i*i)/(i+.9)) + 3.0;
      pole5[p++] = weight;
    }
   }
 
/* Create linked lists for UF_MODL_ask_body_faces. */
  UF_CALL(UF_MODL_create_list(&face_list1));
  UF_CALL(UF_MODL_create_list(&face_list2));
  UF_CALL(UF_MODL_create_list(&face_list3));
  UF_CALL(UF_MODL_create_list(&face_list4));
  UF_CALL(UF_MODL_create_list(&face_list5));
/* Create driver Curves. */
   
  for ( i = 0 ; i < 3 ; i++ )
  {
      line_coords.start_point [ i ] = pt1 [ i ];
      line_coords.end_point [ i ] = pt2 [ i ];
  }
  UF_CURVE_create_line ( &line_coords , &prim_cvs[0] );
   
  for ( i = 0 ; i < 3 ; i++ )
  {
      line_coords.start_point [ i ] = pt2 [ i ];
      line_coords.end_point [ i ] = pt3 [ i ];
  }
  UF_CURVE_create_line ( &line_coords , &cros_cvs[0] );
   
  for ( i = 0 ; i < 3 ; i++ )
  {
      line_coords.start_point [ i ] = pt3 [ i ];
      line_coords.end_point [ i ] = pt4 [ i ];
  }
  UF_CURVE_create_line ( &line_coords , &prim_cvs[1] );
   
  for ( i = 0 ; i < 3 ; i++ )
  {
      line_coords.start_point [ i ] = pt4 [ i ];
      line_coords.end_point [ i ] = pt1 [ i ];
  }
  UF_CURVE_create_line ( &line_coords , &cros_cvs[1] );

/* Create target B-surfaces. */
  UF_CALL(UF_MODL_create_bsurf(num_pole_u,num_pole_v,
            u_ord,v_ord,u_knot,v_knot,pole1,
            &bsurf[0],&knot1_fix,&pole1_fix));

  UF_CALL(UF_MODL_create_bsurf(num_pole_u,num_pole_v,
            u_ord,v_ord,u_knot,v_knot,pole2,
            &bsurf[1],&knot1_fix,&pole1_fix));
 
  
  UF_CALL(UF_MODL_create_bsurf(num_pole_u,num_pole_v,
            u_ord,v_ord,u_knot,v_knot,pole3,
            &bsurf[2],&knot1_fix,&pole1_fix));

  UF_CALL(UF_MODL_create_bsurf(num_pole_u,num_pole_v,
            u_ord,v_ord,u_knot,v_knot,pole4,
            &bsurf[3],&knot1_fix,&pole1_fix));

/* Create driver B-surface */
  UF_CALL(UF_MODL_create_bsurf(num_pole_u,num_pole_v,
            u_ord,v_ord,u_knot,v_knot,pole5,&driv_surf,
            &knot1_fix,&pole1_fix));

/* Load the linked lists with face tags */
  UF_CALL(UF_MODL_ask_body_faces(bsurf[0],&face_list1));

  UF_CALL(UF_MODL_ask_body_faces(bsurf[1],&face_list2));

  UF_CALL(UF_MODL_ask_body_faces(bsurf[2],&face_list3));

  UF_CALL(UF_MODL_ask_body_faces(bsurf[3],&face_list4));

  UF_CALL(UF_MODL_ask_body_faces(driv_surf,&face_list5));

/* Error check the lists. */
  UF_CALL(UF_MODL_ask_list_count(face_list1,&count[0]));
  UF_CALL(UF_MODL_ask_list_count(face_list2,&count[1]));
  UF_CALL(UF_MODL_ask_list_count(face_list3,&count[2]));
  UF_CALL(UF_MODL_ask_list_count(face_list4,&count[3]));
  UF_CALL(UF_MODL_ask_list_count(face_list5,&count[4]));

/* Get the face tags */
  UF_CALL(UF_MODL_ask_list_item(face_list1,0,&faces[0]));
  UF_CALL(UF_MODL_ask_list_item(face_list2,0,&faces[1]));
  UF_CALL(UF_MODL_ask_list_item(face_list3,0,&faces[2]));
  UF_CALL(UF_MODL_ask_list_item(face_list4,0,&faces[3]));
  UF_CALL(UF_MODL_ask_list_item(face_list5,0,&driver_face));

/* Deallocate memory used by lists. */
  UF_MODL_delete_list(&face_list1);
  UF_MODL_delete_list(&face_list2);
  UF_MODL_delete_list(&face_list3);
  UF_MODL_delete_list(&face_list4);
  UF_MODL_delete_list(&face_list5);
/* Reparameterize using B-surface as a driver. */
  UF_CALL(UF_MODL_create_reparam_sheet(proj_type1,drv_type1,
             check_overlap,num_primary,&driver_face,
             num_cross,cros_cvs,proj_vec,num_fs,
             faces,tols1,&new_face,&tol_achieved));

/* Reparameterize using curves as a driver. */
  UF_CALL(UF_MODL_create_reparam_sheet(proj_type2,drv_type2,
             check_overlap,num_primary,prim_cvs,
             num_cross,cros_cvs,proj_vec,num_fs,
             faces,tols2,&new_face,&tol_achieved));

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
