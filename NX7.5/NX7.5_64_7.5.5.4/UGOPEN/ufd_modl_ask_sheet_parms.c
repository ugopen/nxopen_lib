/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_thicken_sheet_parms                                    *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The example creates   *
 *   a thickened sheet and then queries its parameters.                       *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_curve.h>
#include <uf_part.h>

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

    int    arc_mode=1;
    int    align=1,end_point=0,body_type=0;

    char *first_offset,*second_offset;

    double tol[3]={0.1,0.1,0.1};
    double pt1[3],pt2[3],pt3[3];
    double value[6];

    UF_STRING_t   guide,spine;
    
    tag_t arc1_tag,arc2_tag,sheet_tag,thicken_tag;
    
/* create the first arc */
    pt1[0] =   0.0; pt1[1] =  0.0; pt1[2] =   0.0;
    pt2[0] =  50.0; pt2[1] = 10.0; pt2[2] =   0.0;
    pt3[0] = 100.0; pt3[1] =  0.0; pt3[2] =   0.0;
    FTN(uf5063) (&arc_mode,pt1,pt2,pt3,&arc1_tag);

/* create the second arc */
    pt1[0] =   0.0; pt1[1] =  0.0; pt1[2] = 100.0;
    pt2[0] =  50.0; pt2[1] = 10.0; pt2[2] = 100.0;
    pt3[0] = 100.0; pt3[1] =  0.0; pt3[2] = 100.0;
    FTN(uf5063) (&arc_mode,pt1,pt2,pt3,&arc2_tag);

/* create the ruled sheet body */
    UF_MODL_create_string_list(2,2,&guide);

    guide.num = 2;
    guide.string[0] = 1;
    guide.dir[0] = 1;
    guide.id[0] = arc1_tag;
    guide.string[1] = 1;
    guide.dir[1] = 1;
    guide.id[1] = arc2_tag;
    spine.num = 0;
    
    UF_CALL(UF_MODL_create_ruled(&guide,
                                 &spine,
                                 &align,
                                 value,
                                 &end_point,
                                 &body_type,
                                 UF_NULLSIGN,
                                 tol,
                                 &sheet_tag));

    UF_MODL_free_string_list(&guide);

/* create the thickened sheet solid */
    UF_CALL(UF_MODL_create_thicken_sheet(sheet_tag,
                                         "1.0",
                                         "0.0",
                                         UF_NULLSIGN,
                                         &thicken_tag));

/* retrieve the parameters of the thickened sheet */
    UF_CALL(UF_MODL_ask_thicken_sheet_parms(thicken_tag,
                                            &sheet_tag,
                                            &first_offset,
                                            &second_offset));
/* print output values */
    printf("First offset is %s\n",first_offset);
    printf("Second offset is %s\n",second_offset);

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
