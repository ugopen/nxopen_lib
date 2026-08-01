/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCLDKINOPENCPP library.


  ==========================================================================*/
#ifndef LIBCLDKINOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCLDKINOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define CLDKINOPENCPPEXPORT	   __declspec(dllimport)
#		   define CLDKINOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define CLDKINOPENCPPTEMPLATE	 extern
#	   else
#		   define CLDKINOPENCPPEXPORT
#		   define CLDKINOPENCPPGLOBAL	   extern
#		   define CLDKINOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCLDKINOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
