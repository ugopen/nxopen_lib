/*=============================================================================
                Copyright (c) 2014 Siemens Product Lifecycle Management Software Inc.
                      Unpublished - All rights reserved
===============================================================================


File description:

    This contains the export symbols for the LIBUFUN_VDAC library.

==============================================================================*/
#ifndef LIBUFUN_WELD_EXPORTS_H_INCLUDED
#define LIBUFUN_WELD_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/*  */
#   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#       define UFUN_WELDEXPORT       __declspec(dllimport)
#       define UFUN_WELDGLOBAL       extern __declspec(dllimport)
#   else
#       define UFUN_WELDEXPORT
#       define UFUN_WELDGLOBAL       extern
#   endif
/*  */

#endif  /* LIBUFUN_WELD_EXPORTS_H_INCLUDED */
