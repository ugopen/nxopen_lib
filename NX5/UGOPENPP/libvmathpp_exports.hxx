/*=============================================================================
            Copyright (c) 2000 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
===============================================================================
File Description:

    The header file that defines the export symbols for the
    VMATHPP library


=============================================================================*/

#ifndef LIBVMATHPP_EXPORTS_HXX_INCLUDED
#define LIBVMATHPP_EXPORTS_HXX_INCLUDED

/*==========================================================================

  ==========================================================================*/
#       if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#           define VMATHPPEXPORT       __declspec(dllimport)
#           define VMATHPPGLOBAL       extern __declspec(dllimport)
#       else
#           define VMATHPPEXPORT
#           define VMATHPPGLOBAL       extern
#       endif
/*==========================================================================

  ==========================================================================*/

#endif  /*  LIBVMATHPP_EXPORTS_HXX_INCLUDED  */
