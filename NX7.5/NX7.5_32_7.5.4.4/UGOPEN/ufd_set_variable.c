/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_set_variable                                                    *
 *         UF_translate_variable                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following program does not require an open part. The program sets an *
 *   logical/environment variable name and then translates the variable and   *
 *   prints its value.                                                        *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf.h>
#include <stdio.h>

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
  char *ptr;
  
  
  UF_CALL(UF_set_variable("UGII_NEW_VARIABLE", "VALUE"));
  UF_CALL(UF_translate_variable("UGII_NEW_VARIABLE", &ptr));
  printf("Value of UGII_NEW_VARIABLE is : %s\n", ptr);
  
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
