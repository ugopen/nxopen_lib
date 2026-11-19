/*=============================================================================
                Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
                      Unpublished - All rights reserved
===============================================================================


File description:

    This contains the export symbols for the LIBUFUN_CAM library.

==============================================================================*/
#ifndef LIBUFUN_CAM_EXPORTS_H_INCLUDED
#define LIBUFUN_CAM_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/*  */
#   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#       define UFUN_CAMEXPORT       __declspec(dllimport)
#       define UFUN_CAMGLOBAL       extern __declspec(dllimport)
#   else
#       define UFUN_CAMEXPORT
#       define UFUN_CAMGLOBAL       extern
#   endif
/*  */

#endif  /* LIBUFUN_CAM_EXPORTS_H_INCLUDED */

