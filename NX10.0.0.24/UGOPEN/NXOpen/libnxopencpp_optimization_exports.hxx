/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_OPTIMIZATION library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_OPTIMIZATION_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_OPTIMIZATION_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_OPTIMIZATIONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_OPTIMIZATIONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_OPTIMIZATIONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_OPTIMIZATIONEXPORT
#		   define NXOPENCPP_OPTIMIZATIONGLOBAL	   extern
#		   define NXOPENCPP_OPTIMIZATIONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_OPTIMIZATION_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
