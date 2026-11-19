/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_FEATURES library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_FEATURES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_FEATURES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_FEATURESEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_FEATURESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_FEATURESTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_FEATURESEXPORT
#		   define NXOPENCPP_FEATURESGLOBAL	   extern
#		   define NXOPENCPP_FEATURESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_FEATURES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
