/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCLDREPORTOPENCPP library.


  ==========================================================================*/
#ifndef LIBCLDREPORTOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCLDREPORTOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define CLDREPORTOPENCPPEXPORT	   __declspec(dllimport)
#		   define CLDREPORTOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define CLDREPORTOPENCPPTEMPLATE	 extern
#	   else
#		   define CLDREPORTOPENCPPEXPORT
#		   define CLDREPORTOPENCPPGLOBAL	   extern
#		   define CLDREPORTOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCLDREPORTOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
