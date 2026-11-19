/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_AECDESIGN library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_AECDESIGN_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_AECDESIGN_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_AECDESIGNEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_AECDESIGNGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_AECDESIGNTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_AECDESIGNEXPORT
#		   define NXOPENCPP_AECDESIGNGLOBAL	   extern
#		   define NXOPENCPP_AECDESIGNTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_AECDESIGN_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
