/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_LAYOUT2D library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_LAYOUT2D_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_LAYOUT2D_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_LAYOUT2DEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_LAYOUT2DGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_LAYOUT2DTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_LAYOUT2DEXPORT
#		   define NXOPENCPP_LAYOUT2DGLOBAL	   extern
#		   define NXOPENCPP_LAYOUT2DTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_LAYOUT2D_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
