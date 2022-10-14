/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MARKUP library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MARKUP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MARKUP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MARKUPEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MARKUPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MARKUPTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MARKUPEXPORT
#		   define NXOPENCPP_MARKUPGLOBAL	   extern
#		   define NXOPENCPP_MARKUPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MARKUP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
