/*=============================================================================
            Copyright (c) 2003 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    NXOPENJAMTESTCPP library


=============================================================================*/

#ifndef LIBNXOPENJAMTESTCPP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAMTESTCPP_EXPORTS_HXX_INCLUDED

/*==========================================================================

  ==========================================================================*/
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define NXOPENJAMTESTCPPEXPORT       __declspec(dllimport)
#           define NXOPENJAMTESTCPPGLOBAL       extern __declspec(dllimport)
#           define NXOPENJAMTESTCPPTEMPLATE     extern
#       else
#           define NXOPENJAMTESTCPPEXPORT
#           define NXOPENJAMTESTCPPGLOBAL       extern
#           define NXOPENJAMTESTCPPTEMPLATE
#       endif
/*==========================================================================

  ==========================================================================*/

#endif  /*  LIBNXOPENJAMTESTCPP_EXPORTS_HXX_INCLUDED  */
