/*=============================================================================
            Copyright (c) 2000 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    OPENINTPP library


=============================================================================*/

#ifndef LIBOPENINTPP_EXPORTS_HXX_INCLUDED
#define LIBOPENINTPP_EXPORTS_HXX_INCLUDED

/*==========================================================================

  ==========================================================================*/
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define OPENINTPPEXPORT       __declspec(dllimport)
#           define OPENINTPPGLOBAL       extern __declspec(dllimport)
#       else
#           define OPENINTPPEXPORT
#           define OPENINTPPGLOBAL       extern
#       endif
/*==========================================================================

  ==========================================================================*/

#endif  /*  LIBOPENINTPP_EXPORTS_HXX_INCLUDED  */
