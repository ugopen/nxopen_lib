/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_get_customer_default                                            *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example reads the Y grid spacing. For more information on  *
 *   customer defaults please see the UG_Essentials manual or interactively   *
 *   within UG select File->Utilities->Customer Defaults.                     *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>

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

  char name[]="UG_gridSpacingY";
  int units=METRIC;
  char *default_value=NULL;
  int status=0;
  char message[133];

  status = UF_get_customer_default(name,units,&default_value);

  switch (status)
  {
    case 0:
	printf("Default value for %s is %s\n",name,default_value);
	break;
    case 1:
	printf("Default value for %s is not found\n",name);
	break;
    default:
	UF_get_fail_message(status,message);
	printf("ERROR: %s\n",message);
	break;
  }

UF_free(default_value);

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
