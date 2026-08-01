/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBAMMATERIALSOPENCPP library.


  ==========================================================================*/
#ifndef LIBAMMATERIALSOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBAMMATERIALSOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define AMMATERIALSOPENCPPEXPORT	   __declspec(dllimport)
#		   define AMMATERIALSOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define AMMATERIALSOPENCPPTEMPLATE	 extern
#	   else
#		   define AMMATERIALSOPENCPPEXPORT
#		   define AMMATERIALSOPENCPPGLOBAL	   extern
#		   define AMMATERIALSOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBAMMATERIALSOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
