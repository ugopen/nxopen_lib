/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_DISPLAY library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_DISPLAY_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_DISPLAY_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_DISPLAYEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_DISPLAYGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_DISPLAYTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_DISPLAYEXPORT
#		   define NXOPENCPP_DISPLAYGLOBAL	   extern
#		   define NXOPENCPP_DISPLAYTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_DISPLAY_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
