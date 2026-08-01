/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_DRAWINGS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_DRAWINGS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_DRAWINGS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_DRAWINGSEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_DRAWINGSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_DRAWINGSTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_DRAWINGSEXPORT
#		   define NXOPENCPP_DRAWINGSGLOBAL	   extern
#		   define NXOPENCPP_DRAWINGSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_DRAWINGS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
