/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_IMPLICIT library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_IMPLICIT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_IMPLICIT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_IMPLICITEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_IMPLICITGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_IMPLICITTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_IMPLICITEXPORT
#		   define NXOPENCPP_IMPLICITGLOBAL	   extern
#		   define NXOPENCPP_IMPLICITTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_IMPLICIT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
