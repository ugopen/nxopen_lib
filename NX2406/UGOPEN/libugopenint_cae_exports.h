/*=============================================================================
        Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
                      Unpublished - All rights reserved
===============================================================================


File description:

    This contains the export symbols for the LIBUGOPENINT_CAE library.

==============================================================================*/
#ifndef LIBUGOPENINT_CAE_EXPORTS_H_INCLUDED
#define LIBUGOPENINT_CAE_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/*  */
#      if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#          define UGOPENINT_CAEEXPORT       __declspec(dllimport)
#          define UGOPENINT_CAEGLOBAL       extern __declspec(dllimport)
#      else
#          define UGOPENINT_CAEEXPORT
#          define UGOPENINT_CAEGLOBAL       extern
#      endif
/*  */



#endif  /* LIBUGOPENINT_CAE_EXPORTS_H_INCLUDED */
