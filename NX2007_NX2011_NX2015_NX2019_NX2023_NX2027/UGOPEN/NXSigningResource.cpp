/*==================================================================================================

              Copyright (c) 2008 Unigraphics Solutions Inc.
                        Unpublished - All rights reserved
====================================================================================================
File description:

    File to be used in native signing


==================================================================================================*/

#include <uf_defs.h>

static unsigned char nxauthblock[] = "NXAUTHBLOCK      "
                                     "                                                  "
                                     "                                                  "
                                     "                                                  "
                                     "                                                  "
                                     "                                                  "
                                     "                                                  "
                                     "                                                  "
                                     "                                                  "
                                     "                                                  "
                                     "                                                  "
                                     "      NXAUTHBLOCK";


// This function used to be empty. The code in this function should never be executed.
// It is here because if nxauthblock is never used somewhere, it will be removed by the compiler
// during code optimization, preventing the signing of DLLs.
extern DllExport void NXSigningResource(void)
{
    static bool doNothing = false;
    if (doNothing)
        nxauthblock[0] = 'N';
}
