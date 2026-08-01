/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_WELD library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_WELD_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_WELD_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_WELDEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_WELDGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_WELDTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_WELDEXPORT
#		   define NXOPENCPP_WELDGLOBAL	   extern
#		   define NXOPENCPP_WELDTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_WELD_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
