
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support ask default density:
 *
 *      UF_MODL_ask_default_density
 *
 * ========================================================================== */


#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf_modl.h>


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

  char    *prtnam = "default_density"; 

  double  old_density;
  double  new_density = 1.0;
        
  tag_t   part_tag;

  UF_MODL_density_units_t   units = UF_MODL_pounds_inches;
  
  /* Open a new part */
  UF_CALL(UF_PART_new(prtnam, METRIC, &part_tag));

  /* fetch current default density */
  UF_CALL(UF_MODL_ask_default_density(units, &old_density)); 
    
  /* change the default density */
  UF_CALL(UF_MODL_set_default_density(new_density, units)); 

  /* fetch the default density again and validate */
  UF_CALL(UF_MODL_ask_default_density(units, &old_density)); 

  if ( old_density != new_density )
     printf("***ERROR setting or asking default density ***\n");
  
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



