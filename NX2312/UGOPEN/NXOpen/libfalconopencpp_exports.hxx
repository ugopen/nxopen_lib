/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBFALCONOPENCPP library.


  ==========================================================================*/
#ifndef LIBFALCONOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBFALCONOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define FALCONOPENCPPEXPORT	   __declspec(dllimport)
#		   define FALCONOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define FALCONOPENCPPTEMPLATE	 extern
#	   else
#		   define FALCONOPENCPPEXPORT
#		   define FALCONOPENCPPGLOBAL	   extern
#		   define FALCONOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBFALCONOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
