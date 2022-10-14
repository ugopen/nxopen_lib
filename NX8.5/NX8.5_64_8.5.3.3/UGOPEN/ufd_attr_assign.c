/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_ATTR_assign                                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The code creates a point    *
 *   and assigns several attributes.                                          *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_attr.h>
#include <uf_cfi.h>
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

/*  Variable Declarations */
    tag_t       pnt;
    double    zero[3] = { 0,0,0 };
    UF_ATTR_value_t value;

/*  Create a point to assign the attributes to */
    UF_CALL(UF_CURVE_create_point(zero, &pnt));

/*  Assign an integer attribute to the point */
    value.type = UF_ATTR_integer;
    value.value.integer = 1;
    UF_CALL(UF_ATTR_assign(pnt, "INTEGER_ATTRIBUTE", value));

/*  Assign a real attribute to the point */
    value.type = UF_ATTR_real;
    value.value.real = 1.5;
    UF_CALL(UF_ATTR_assign(pnt, "REAL_ATTRIBUTE", value));

/*  Assign a date and time attribute to the point */
    value.type = UF_ATTR_time;

/* Init to current date and time */
    UF_CALL(uc4583("", "", value.value.time));  
    UF_CALL(UF_ATTR_assign(pnt, "DATE_AND_TIME_ATTRIBUTE", value));

/*  Assign a null attribute to the point */
    value.type = UF_ATTR_null;
    UF_CALL(UF_ATTR_assign(pnt, "NULL_ATTRIBUTE", value));

/*  Assign a string attribute to the point */
    value.type = UF_ATTR_string;
    value.value.string = "This is a string";
    UF_CALL(UF_ATTR_assign(pnt, "STRING_ATTRIBUTE", value));
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
