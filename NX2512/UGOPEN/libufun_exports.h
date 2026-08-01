/*=============================================================================
            Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    UFUN library


=============================================================================*/

#ifndef LIBUFUN_EXPORTS_H_INCLUDED
#define LIBUFUN_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif


/*  */
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define UFUNEXPORT       __declspec(dllimport)
#           define UFUNGLOBAL       extern __declspec(dllimport)
#       else
#           define UFUNEXPORT
#           define UFUNGLOBAL       extern
#       endif
/*  */


#endif  /*  LIBUFUN_EXPORTS_H_INCLUDED  */
