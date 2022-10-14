/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBALPOPENCPP library.


  ==========================================================================*/
#ifndef LIBALPOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBALPOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define ALPOPENCPPEXPORT	   __declspec(dllimport)
#		   define ALPOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define ALPOPENCPPTEMPLATE	 extern
#	   else
#		   define ALPOPENCPPEXPORT
#		   define ALPOPENCPPGLOBAL	   extern
#		   define ALPOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBALPOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
