/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_FEATURES library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_FEATURES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_FEATURES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_FEATURESEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_FEATURESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_FEATURESTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_FEATURESEXPORT
#		   define NXOPENJAVA_FEATURESGLOBAL	   extern
#		   define NXOPENJAVA_FEATURESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_FEATURES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
