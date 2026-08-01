/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBDSEPLATFORMOPENCPP library.


  ==========================================================================*/
#ifndef LIBDSEPLATFORMOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBDSEPLATFORMOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define DSEPLATFORMOPENCPPEXPORT	   __declspec(dllimport)
#		   define DSEPLATFORMOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define DSEPLATFORMOPENCPPTEMPLATE	 extern
#	   else
#		   define DSEPLATFORMOPENCPPEXPORT
#		   define DSEPLATFORMOPENCPPGLOBAL	   extern
#		   define DSEPLATFORMOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBDSEPLATFORMOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
