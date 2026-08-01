/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_VSA library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_VSA_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_VSA_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_VSAEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_VSAGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_VSATEMPLATE	 extern
#	   else
#		   define NXOPENCPP_VSAEXPORT
#		   define NXOPENCPP_VSAGLOBAL	   extern
#		   define NXOPENCPP_VSATEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_VSA_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
