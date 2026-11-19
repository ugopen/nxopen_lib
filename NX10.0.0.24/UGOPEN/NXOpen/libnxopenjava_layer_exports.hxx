/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_LAYER library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_LAYER_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_LAYER_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_LAYEREXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_LAYERGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_LAYERTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_LAYEREXPORT
#		   define NXOPENJAVA_LAYERGLOBAL	   extern
#		   define NXOPENJAVA_LAYERTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_LAYER_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
