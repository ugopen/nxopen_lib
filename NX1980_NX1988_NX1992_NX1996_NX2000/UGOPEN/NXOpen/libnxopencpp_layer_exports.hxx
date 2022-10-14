/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_LAYER library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_LAYER_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_LAYER_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_LAYEREXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_LAYERGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_LAYERTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_LAYEREXPORT
#		   define NXOPENCPP_LAYERGLOBAL	   extern
#		   define NXOPENCPP_LAYERTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_LAYER_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
