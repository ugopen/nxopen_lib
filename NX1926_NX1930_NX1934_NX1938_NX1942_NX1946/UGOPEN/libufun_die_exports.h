/*=============================================================================
                Copyright (c) 2014 Siemens Product Lifecycle Management Software Inc.
                      Unpublished - All rights reserved
===============================================================================


File description:

    This contains the export symbols for the LIBUFUN_DIE library.

==============================================================================*/
#ifndef LIBUFUN_DIE_EXPORTS_H_INCLUDED
#define LIBUFUN_DIE_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/*  */
#   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#       define UFUN_DIEEXPORT       __declspec(dllimport)
#       define UFUN_DIEGLOBAL       extern __declspec(dllimport)
#   else
#       define UFUN_DIEEXPORT
#       define UFUN_DIEGLOBAL       extern
#   endif
/*  */

#endif  /* LIBUFUN_DIE_EXPORTS_H_INCLUDED */
