/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCOMPOSITESOPENCPP library.


  ==========================================================================*/
#ifndef LIBCOMPOSITESOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCOMPOSITESOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define COMPOSITESOPENCPPEXPORT	   __declspec(dllimport)
#		   define COMPOSITESOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define COMPOSITESOPENCPPTEMPLATE	 extern
#	   else
#		   define COMPOSITESOPENCPPEXPORT
#		   define COMPOSITESOPENCPPGLOBAL	   extern
#		   define COMPOSITESOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCOMPOSITESOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
