/*=============================================================================
            Copyright (c) 2000 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    OPENPP library


=============================================================================*/

/*==========================================================================

  ==========================================================================*/
#ifndef LIBOPENPP_EXPORTS_HXX_INCLUDED
#define LIBOPENPP_EXPORTS_HXX_INCLUDED
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define OPENPPEXPORT       __declspec(dllimport)
#           define OPENPPGLOBAL       extern __declspec(dllimport)
#           define OPENPPTEMPLATE     extern
#       else
#           define OPENPPEXPORT
#           define OPENPPGLOBAL       extern
#           define OPENPPTEMPLATE
#       endif
/*==========================================================================
  ==========================================================================*/

#endif  /*  LIBOPENPP_EXPORTS_HXX_INCLUDED  */
