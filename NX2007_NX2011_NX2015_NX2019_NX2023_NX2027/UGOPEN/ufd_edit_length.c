
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support edit length:
 *
 *      UF_CURVE_edit_length
 *
 * ========================================================================== */


#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_csys.h>


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

  char    *prtnam = "curve_edit_length"; 

  double  o_arclen, inc_len, m_arclen;

  tag_t   part_tag;
  tag_t   arc_tag;
  tag_t   wcs_tag;
  
  int     method, location, ext_type;
  
  UF_CURVE_arc_t  arc_coords;  

  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );


  /* Fill out the data structure to create an arc */
  arc_coords.start_angle = 0.0;
  arc_coords.end_angle = 180.0 * DEGRA;
  arc_coords.arc_center[0] = 0.0;
  arc_coords.arc_center[1] = 0.0;
  arc_coords.arc_center[2] = 1.0;
  arc_coords.radius = 2.0;
  
  UF_CALL(UF_CSYS_ask_wcs(&wcs_tag));
  UF_CALL(UF_CSYS_ask_matrix_of_object(wcs_tag,
                                       &arc_coords.matrix_tag));

  UF_CALL(UF_CURVE_create_arc(&arc_coords,&arc_tag));

  UF_CALL(UF_CURVE_ask_arc_length(arc_tag, 0.0, 1.0, UF_MODL_UNITS_PART, &o_arclen));

  printf("*** Extending arc at the start point ***\n");  

  method = 1;     /* incremental */
  location = 1;   /* start of curve */
  inc_len = 20;   /* incremental length */
  ext_type = UF_CURVE_NATURAL_SHAPE;

  UF_CALL(UF_CURVE_edit_length( arc_tag, method, inc_len, location, ext_type ));

  UF_CALL(UF_CURVE_ask_arc_length(arc_tag, 0.0, 1.0, UF_MODL_UNITS_PART, &m_arclen));
  

  if ( (o_arclen + inc_len) != m_arclen )
  {
     printf("*** ERROR editing length of the arc ***\n");  
  }    

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



