/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCLDCOMMONOPENCPP library.


  ==========================================================================*/
#ifndef LIBCLDCOMMONOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCLDCOMMONOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define CLDCOMMONOPENCPPEXPORT	   __declspec(dllimport)
#		   define CLDCOMMONOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define CLDCOMMONOPENCPPTEMPLATE	 extern
#	   else
#		   define CLDCOMMONOPENCPPEXPORT
#		   define CLDCOMMONOPENCPPGLOBAL	   extern
#		   define CLDCOMMONOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCLDCOMMONOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
