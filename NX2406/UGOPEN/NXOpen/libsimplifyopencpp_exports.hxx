/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBSIMPLIFYOPENCPP library.


  ==========================================================================*/
#ifndef LIBSIMPLIFYOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBSIMPLIFYOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define SIMPLIFYOPENCPPEXPORT	   __declspec(dllimport)
#		   define SIMPLIFYOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define SIMPLIFYOPENCPPTEMPLATE	 extern
#	   else
#		   define SIMPLIFYOPENCPPEXPORT
#		   define SIMPLIFYOPENCPPGLOBAL	   extern
#		   define SIMPLIFYOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBSIMPLIFYOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
