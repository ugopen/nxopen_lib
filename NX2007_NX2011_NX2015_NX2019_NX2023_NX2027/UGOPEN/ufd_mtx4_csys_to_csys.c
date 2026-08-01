
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support transform from one coordinate system to another:
 *
 *      UF_MTX4_csys_to_csys
 *
 * ========================================================================== */


#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_mtx.h>


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

  char    *prtnam = "csys_to_csys"; 

  double  from_origin[3] = {0.0, 0.0, 0.0};
  double  from_x_axis[3] = {1.0, 0.0, 0.0};
  double  from_y_axis[3] = {0.0, 1.0, 0.0};
  double  to_origin[3] = {10.0, 10.0, 10.0};
  double  to_x_axis[3] = {0.0, 1.0, 0.0};
  double  to_y_axis[3] = {1.0, 0.0, 0.0};
  double  new_target[3];
  double  target[3] = { 20.0, 10.0, 5.0};

  double  transform[16];
        
  tag_t   part_tag;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* fetch the matrix containing mirro information to move an */
  /* object around X-Y mirror plane  */
  UF_CALL( UF_MTX4_csys_to_csys( from_origin, from_x_axis, from_y_axis,
                                 to_origin, to_x_axis, to_y_axis, 
                                 transform ) ); 

  /* transform the target using the returned matrix */
  UF_MTX4_vec3_multiply( target, transform, new_target );
  
  if (new_target[0] != 20.0 && new_target[1] != 30.0 && new_target[2] != 15.0)
     printf("*** ERROR from UF_MTX4_csys_to_csys ***\n");
  
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



