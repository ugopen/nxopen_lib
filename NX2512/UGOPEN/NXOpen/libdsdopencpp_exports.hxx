/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBDSDOPENCPP library.


  ==========================================================================*/
#ifndef LIBDSDOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBDSDOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define DSDOPENCPPEXPORT	   __declspec(dllimport)
#		   define DSDOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define DSDOPENCPPTEMPLATE	 extern
#	   else
#		   define DSDOPENCPPEXPORT
#		   define DSDOPENCPPGLOBAL	   extern
#		   define DSDOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBDSDOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
