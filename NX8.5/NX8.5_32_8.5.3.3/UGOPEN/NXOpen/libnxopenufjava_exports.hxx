/*=============================================================================
       Copyright (c) 2010 Siemens Product Lifecycle Management Software Inc.
                            All rights reserved
===============================================================================
File Description:

    Header file that defines the export symbols for the LIBNXOPENUFJAVA library.


  ==========================================================================*/
#ifndef LIBNXOPENUFJAVA_EXPORTS_HXX_INCLUDED
#define LIBNXOPENUFJAVA_EXPORTS_HXX_INCLUDED
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define NXOPENUFJAVAEXPORT       __declspec(dllimport)
#           define NXOPENUFJAVAGLOBAL       extern __declspec(dllimport)
#           define NXOPENUFJAVATEMPLATE     extern
#       else
#           define NXOPENUFJAVAEXPORT
#           define NXOPENUFJAVAGLOBAL       extern
#           define NXOPENUFJAVATEMPLATE
#       endif
#endif  /*  LIBNXOPENUFJAVA_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
