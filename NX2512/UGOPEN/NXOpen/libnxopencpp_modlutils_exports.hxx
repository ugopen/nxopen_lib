/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MODLUTILS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MODLUTILS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MODLUTILS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MODLUTILSEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MODLUTILSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MODLUTILSTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MODLUTILSEXPORT
#		   define NXOPENCPP_MODLUTILSGLOBAL	   extern
#		   define NXOPENCPP_MODLUTILSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MODLUTILS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
