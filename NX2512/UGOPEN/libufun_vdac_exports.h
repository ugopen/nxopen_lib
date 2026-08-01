/*=============================================================================
                Copyright (c) 2014 Siemens Product Lifecycle Management Software Inc.
                      Unpublished - All rights reserved
===============================================================================


File description:

    This contains the export symbols for the LIBUFUN_VDAC library.

==============================================================================*/
#ifndef LIBUFUN_VDAC_EXPORTS_H_INCLUDED
#define LIBUFUN_VDAC_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/*  */
#   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#       define UFUN_VDACEXPORT       __declspec(dllimport)
#       define UFUN_VDACGLOBAL       extern __declspec(dllimport)
#   else
#       define UFUN_VDACEXPORT
#       define UFUN_VDACGLOBAL       extern
#   endif
/*  */

#endif  /* LIBUFUN_VDAC_EXPORTS_H_INCLUDED */
