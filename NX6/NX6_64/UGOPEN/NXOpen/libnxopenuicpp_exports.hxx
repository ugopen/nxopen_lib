/*=============================================================================
            Copyright (c) 2003 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    NXOPENUICPP library


=============================================================================*/

#ifndef LIBNXOPENUICPP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENUICPP_EXPORTS_HXX_INCLUDED

/*==========================================================================

  ==========================================================================*/
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define NXOPENUICPPEXPORT       __declspec(dllimport)
#           define NXOPENUICPPGLOBAL       extern __declspec(dllimport)
#           define NXOPENUICPPTEMPLATE     extern
#       else
#           define NXOPENUICPPEXPORT
#           define NXOPENUICPPGLOBAL       extern
#           define NXOPENUICPPTEMPLATE
#       endif
/*==========================================================================

  ==========================================================================*/

#endif  /*  LIBNXOPENUICPP_EXPORTS_HXX_INCLUDED  */
