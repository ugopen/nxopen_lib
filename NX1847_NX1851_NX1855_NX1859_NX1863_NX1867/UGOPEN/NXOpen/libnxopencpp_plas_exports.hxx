/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_PLAS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_PLAS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_PLAS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_PLASEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_PLASGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_PLASTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_PLASEXPORT
#		   define NXOPENCPP_PLASGLOBAL	   extern
#		   define NXOPENCPP_PLASTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_PLAS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
