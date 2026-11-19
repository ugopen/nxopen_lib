/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCAPITALOPENCPP library.


  ==========================================================================*/
#ifndef LIBCAPITALOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCAPITALOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define CAPITALOPENCPPEXPORT	   __declspec(dllimport)
#		   define CAPITALOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define CAPITALOPENCPPTEMPLATE	 extern
#	   else
#		   define CAPITALOPENCPPEXPORT
#		   define CAPITALOPENCPPGLOBAL	   extern
#		   define CAPITALOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCAPITALOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
