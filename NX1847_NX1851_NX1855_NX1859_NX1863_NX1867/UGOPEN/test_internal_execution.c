
/*===========================================================================

             Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

This is a very simple program, which is meant to test whether internal
NX Open access is working on a system.

  
===========================================================================*/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_ui.h>

#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133], messg[300];

        UF_get_fail_message(irc, err);
        sprintf(messg, "\n%s\nerror %d at line %d in %s\n%s",
            err, irc, line, file, call);
        printf("%s\n", messg);
        strcpy(&messg[129], "...");
        uc1601(messg, TRUE);  /* Internal only - remove for external */
    }
    return(irc);
}

static void do_it(void)
{
    uc1601("This is a test", 1);
}

void ufusr(char *param, int *retcode, int paramLen)
{
    if (UF_CALL(UF_initialize())) return;
    do_it();
    UF_terminate();
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}


