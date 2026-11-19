/*==================================================================================================

                    Copyright (c) 2000 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved
===================================================================================================*/

 /******************************************************************************
 *                                                                             *
 * DESCRIPTION -                                                               *
 *   This program shows how to use the following UG/Open API routine(s):       *
 *                                                                             *
 *     UF_MODL_create_thru_curves1 without template curve                      *
 *     UF_MODL_create_thru_curves1 with the supplied template curve            *
 *                                                                             *    
 *                                                                             *
 * PROGRAM DESCRIPTION -                                                       *
 *   The following example requires a blank, open part. The code first creates *
 *   a through curve surface without template string, and then creates a       * 
 *   through curve surface with one template string.                           *
 *                                                                             *
 *                 *
 *                                                                             *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_modl_types.h>
#include <uf_modl_freeform.h>
#include <uf_modl_curves.h>

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
    int knot_fix, pole_fix, i;
    tag_t str1_tag, str2_tag, str3_tag, str4_tag;
    double str1_poles[] = {-2.5, 1.8, 0.8, 1.0,
                           -1.0, 1.9, 0.5, 1.0,
                            0.5, 2.0, 0.5, 1.0,
                            2.0, 1.6, 0.0, 1.0};

    double str1_knots[] = {0.0, 0.0, 0.0, 0.0, 
                           1.0, 1.0, 1.0, 1.0};

    double str2_poles[] = {-2.5, 0.5, 0.0, 1.0,
                           -1.0, 0.7, 1.0, 1.0,
                            0.5, 1.0, 0.5, 1.0,
                            2.0, 0.4, 0.0, 1.0};

    double str2_knots[] = {0.0, 0.0, 0.0, 0.0, 
                           1.0, 1.0, 1.0, 1.0};

    double str3_poles[] = {-2.5, -0.7, 0.5, 1.0,
                           -0.8, -0.6, 0.0, 1.0,
                            0.7, -0.5, 0.0, 1.0,
                            2.0, -0.8, 0.5, 1.0};

    double str3_knots[] = {0.0, 0.0, 0.0, 0.0,
                           1.0, 1.0, 1.0, 1.0};

    double str4_poles[] = {-2.5, -2.0, 0.0, 1.0,
                           -0.8, -1.8, 0.5, 1.0,
                            0.7, -1.7, 0.5, 1.0,
                            2.0, -2.1, 0.0, 1.0};

    double str4_knots[] = {0.0, 0.0, 0.0, 0.0,
                           1.0, 1.0, 1.0, 1.0};

    int  patch = 2, alignment = 2, degree = 3, status = 0;
    int  simple, body_type = 0;	
    double  tol[3], value[6];
    UF_STRING_t      generator, spine;
    UF_STRING_p_t    ge = &generator,  sp = &spine;
    UF_FEATURE_SIGN  boolean;
    tag_t  target_body, *c_face_id[2] = {NULL,NULL};
    tag_t  body_id = NULL_TAG;
    int    c_num[2] = {0,0}, c_flag[2] = {0,0};
    int    c_dir = 0;

/* Initialization */
    tol[0] = 0.1;	/* distance tolerance     */ 
    tol[1] = 0.5;	/* angle tolerance */ 
    tol[2] = 0.02;	/* Intersection tolerance */
    boolean = UF_NULLSIGN;
    sp = NULL;
    target_body = NULL_TAG;

    for (i=0; i<6; i++) 
    {
	value[i] = 0.0;
    }

/* Create the input curves. */
    UF_CALL(UF_MODL_create_spline (4, 4, str1_knots, str1_poles, 
                                   &str1_tag, &knot_fix, &pole_fix));
    UF_CALL(UF_MODL_create_spline (4, 4, str2_knots, str2_poles, 
                                   &str2_tag, &knot_fix, &pole_fix));
    UF_CALL(UF_MODL_create_spline (4, 4, str3_knots, str3_poles, 
                                   &str3_tag, &knot_fix, &pole_fix ));
    UF_CALL(UF_MODL_create_spline (4, 4, str4_knots, str4_poles, 
                                   &str4_tag, &knot_fix, &pole_fix ));

/* Create Strings from 4 curves. Each string contains 1 curve */
    simple = 0;
    UF_MODL_init_string_list(ge);
    UF_MODL_create_string_list(5, 100, ge);
    ge->num = 4; 
    ge->id[0] = str1_tag;
    ge->string[0] = 1;
    ge->dir[0] = 1;

    ge->id[1] = str2_tag;
    ge->string[1] = 1;
    ge->dir[1] = 1;
  
    ge->id[2] = str3_tag;
    ge->string[2] = 1;
    ge->dir[2] = 1;

    ge->id[3] = str4_tag;
    ge->string[3] = 1;
    ge->dir[3] = 1;

    /* Use str1_tag as a template curve */
    ge->id[4] = str1_tag;
    ge->string[4] = 1;
    ge->dir[4] = 1;

/* Create a through curve surface without template */
    UF_CALL(UF_MODL_create_thru_curves1 (ge, sp, &patch, &alignment, value, &degree, &status,
                                         simple, &body_type, boolean, target_body, tol, c_num, c_face_id, c_flag, c_dir, &body_id)); 
    
/* Create a through curve surface with template */
    simple = 2;

    UF_CALL(UF_MODL_create_thru_curves1 (ge, sp, &patch, &alignment, value, &degree, &status,
                                         simple, &body_type, boolean, target_body, tol, c_num, c_face_id, c_flag, c_dir, &body_id));
/* Free the list */
    UF_MODL_free_string_list(ge); 
   
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



