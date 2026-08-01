
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support mirror of data about a plane:
 *
 *      UF_MTX4_mirror
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

  char    *prtnam = "mirror"; 

  double   normal[3] = { 0.0, 0.0, 1.0 };
  double   origin[3] = { 0.0, 0.0, 0.0};
  double   new_target[3];
  double   target[3] = { 10.0, 10.0, 10.0};

  double   transform[16];
        
  tag_t    part_tag;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* fetch the matrix containing mirror information to move an */
  /* object around X-Y mirror plane  */
  UF_CALL(UF_MTX4_mirror( origin, normal, transform )); 

  /* mirror the target using the returned matrix */
  UF_MTX4_vec3_multiply( target, transform, new_target );
  
  if (new_target[0] != 10.0 && new_target[1] != 10.0 && new_target[2] != -10.0)
     printf("*** ERROR from UF_MTX4_mirror ***\n");

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



