/*=============================================================================
            Copyright (c) 2003 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    NXOPENCPP library


=============================================================================*/

/*==========================================================================

  ==========================================================================*/
#ifndef LIBNXOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_EXPORTS_HXX_INCLUDED
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define NXOPENCPPEXPORT       __declspec(dllimport)
#           define NXOPENCPPGLOBAL       extern __declspec(dllimport)
#           define NXOPENCPPTEMPLATE     extern
#       else
#           define NXOPENCPPEXPORT
#           define NXOPENCPPGLOBAL       extern
#           define NXOPENCPPTEMPLATE
#       endif
/*==========================================================================
  ==========================================================================*/

#endif  /*  LIBNXOPENCPP_EXPORTS_HXX_INCLUDED  */
