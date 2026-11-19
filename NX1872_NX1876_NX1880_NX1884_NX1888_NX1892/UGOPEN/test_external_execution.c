/*===========================================================================

             Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

This is a very simple program, which is meant to test whether external
UG/Open access is working on a system.

  
===========================================================================*/

#include <stdio.h>
#include <uf.h>

#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133];

        UF_get_fail_message(irc, err);
        fprintf(stderr, "\n%s\nerror %d at line %d in %s\n%s\n",
            err, irc, line, file, call);
    }
    return(irc);
}

int main( int argc, char *argv[] )
{
    int status;

    status = UF_CALL(UF_initialize());
    if (!status)
    {
        printf("It works!\n");

        status = UF_CALL(UF_terminate());
    }
    return status;
}
