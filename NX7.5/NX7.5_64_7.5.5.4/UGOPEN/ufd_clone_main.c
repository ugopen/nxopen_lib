/* 
===============================================================================

 Copyright (c) 1992 - 1998,1999,2000 Unigraphics Solutions Inc.
                       Unpublished - All rights reserved

===============================================================================

File description:

===========================================================================*/

#include <uf.h>
#include <ufd_clone.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    if (UF_initialize() != 0)
    {
        fprintf(stderr,"Error: Couldn't initialise Unigraphics");
        exit(EXIT_FAILURE);
    }
    UFD_clone_main(argc,argv);

    UF_terminate();

    return(EXIT_SUCCESS);
}
