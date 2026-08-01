/*=============================================================================
        Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
                      Unpublished - All rights reserved
===============================================================================
File description:

    This contains the export symbols for the LIBUFUN_CAE library.


==============================================================================*/
#ifndef LIBUFUN_CAE_EXPORTS_H_INCLUDED
#define LIBUFUN_CAE_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/*  */
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define UFUN_CAEEXPORT       __declspec(dllimport)
#           define UFUN_CAEGLOBAL       extern __declspec(dllimport)
#      else
#          define UFUN_CAEEXPORT
#          define UFUN_CAEGLOBAL       extern
#      endif
/*  */

#endif  /* LIBUFUN_CAE_EXPORTS_H_INCLUDED */
