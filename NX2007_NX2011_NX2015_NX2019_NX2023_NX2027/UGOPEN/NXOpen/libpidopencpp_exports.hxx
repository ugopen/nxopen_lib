/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBPIDOPENCPP library.


  ==========================================================================*/
#ifndef LIBPIDOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBPIDOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define PIDOPENCPPEXPORT	   __declspec(dllimport)
#		   define PIDOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define PIDOPENCPPTEMPLATE	 extern
#	   else
#		   define PIDOPENCPPEXPORT
#		   define PIDOPENCPPGLOBAL	   extern
#		   define PIDOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBPIDOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
