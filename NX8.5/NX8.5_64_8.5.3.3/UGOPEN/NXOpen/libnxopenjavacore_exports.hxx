/*=============================================================================
       Copyright (c) 2010 Siemens Product Lifecycle Management Software Inc.
                            All rights reserved
===============================================================================
File Description:

    Header file that defines the export symbols for the LIBNXOPENJAVACORE library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVACORE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVACORE_EXPORTS_HXX_INCLUDED
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define NXOPENJAVACOREEXPORT       __declspec(dllimport)
#           define NXOPENJAVACOREGLOBAL       extern __declspec(dllimport)
#           define NXOPENJAVACORETEMPLATE     extern
#       else
#           define NXOPENJAVACOREEXPORT
#           define NXOPENJAVACOREGLOBAL       extern
#           define NXOPENJAVACORETEMPLATE
#       endif
#endif  /*  LIBNXOPENJAVACORE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
