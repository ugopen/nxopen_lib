/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_OPTIMIZATION library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_OPTIMIZATION_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_OPTIMIZATION_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_OPTIMIZATIONEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_OPTIMIZATIONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_OPTIMIZATIONTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_OPTIMIZATIONEXPORT
#		   define NXOPENJAVA_OPTIMIZATIONGLOBAL	   extern
#		   define NXOPENJAVA_OPTIMIZATIONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_OPTIMIZATION_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
