/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_CAPITALINTEGRATION library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_CAPITALINTEGRATION_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_CAPITALINTEGRATION_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_CAPITALINTEGRATIONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_CAPITALINTEGRATIONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_CAPITALINTEGRATIONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_CAPITALINTEGRATIONEXPORT
#		   define NXOPENCPP_CAPITALINTEGRATIONGLOBAL	   extern
#		   define NXOPENCPP_CAPITALINTEGRATIONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_CAPITALINTEGRATION_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
