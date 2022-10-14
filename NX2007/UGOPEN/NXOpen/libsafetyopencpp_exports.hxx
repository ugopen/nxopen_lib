/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBSAFETYOPENCPP library.


  ==========================================================================*/
#ifndef LIBSAFETYOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBSAFETYOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define SAFETYOPENCPPEXPORT	   __declspec(dllimport)
#		   define SAFETYOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define SAFETYOPENCPPTEMPLATE	 extern
#	   else
#		   define SAFETYOPENCPPEXPORT
#		   define SAFETYOPENCPPGLOBAL	   extern
#		   define SAFETYOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBSAFETYOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
