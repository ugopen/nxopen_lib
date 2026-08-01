/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_SELECT library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_SELECT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_SELECT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_SELECTEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_SELECTGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_SELECTTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_SELECTEXPORT
#		   define NXOPENCPP_SELECTGLOBAL	   extern
#		   define NXOPENCPP_SELECTTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_SELECT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
