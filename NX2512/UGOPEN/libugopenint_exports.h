/*=============================================================================
            Copyright (c) 2000 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    UGOPENINT library


=============================================================================*/

#ifndef LIBUGOPENINT_EXPORTS_H_INCLUDED
#define LIBUGOPENINT_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif


/*  */
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define UGOPENINTEXPORT       __declspec(dllimport)
#           define UGOPENINTGLOBAL       extern __declspec(dllimport)
#       else
#           define UGOPENINTEXPORT
#           define UGOPENINTGLOBAL       extern
#       endif
/*  */


#endif  /*  LIBUGOPENINT_EXPORTS_H_INCLUDED  */
