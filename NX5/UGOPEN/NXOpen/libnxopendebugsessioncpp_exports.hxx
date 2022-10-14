/*=============================================================================
            Copyright (c) 2003 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    NXOPENDEBUGSESSIONCPP library


=============================================================================*/

#ifndef LIBNXOPENDEBUGSESSIONCPP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENDEBUGSESSIONCPP_EXPORTS_HXX_INCLUDED

/*==========================================================================

  ==========================================================================*/
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define NXOPENDEBUGSESSIONCPPEXPORT       __declspec(dllimport)
#           define NXOPENDEBUGSESSIONCPPGLOBAL       extern __declspec(dllimport)
#           define NXOPENDEBUGSESSIONCPPTEMPLATE     extern
#       else
#           define NXOPENDEBUGSESSIONCPPEXPORT
#           define NXOPENDEBUGSESSIONCPPGLOBAL       extern
#           define NXOPENDEBUGSESSIONCPPTEMPLATE
#       endif
/*==========================================================================

  ==========================================================================*/

#endif  /*  LIBNXOPENDEBUGSESSIONCPP_EXPORTS_HXX_INCLUDED  */
