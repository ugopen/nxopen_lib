/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_GCTOOLS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_GCTOOLS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_GCTOOLS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_GCTOOLSEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_GCTOOLSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_GCTOOLSTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_GCTOOLSEXPORT
#		   define NXOPENCPP_GCTOOLSGLOBAL	   extern
#		   define NXOPENCPP_GCTOOLSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_GCTOOLS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
