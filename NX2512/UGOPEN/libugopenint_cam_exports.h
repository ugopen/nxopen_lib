/*=============================================================================
                Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
                      Unpublished - All rights reserved
===============================================================================


File description:

    This contains the export symbols for the UGOPENINT_CAM library.

==============================================================================*/
#ifndef LIBUGOPENINT_CAM_EXPORTS_H_INCLUDED
#define LIBUGOPENINT_CAM_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/*  */
#   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#       define UGOPENINT_CAMEXPORT       __declspec(dllimport)
#       define UGOPENINT_CAMGLOBAL       extern __declspec(dllimport)
#   else
#       define UGOPENINT_CAMEXPORT
#       define UGOPENINT_CAMGLOBAL       extern
#   endif
/*  */

#endif  /* LIBUGOPENINT_CAM_EXPORTS_H_INCLUDED */

