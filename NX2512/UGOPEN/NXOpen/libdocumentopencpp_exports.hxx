/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBDOCUMENTOPENCPP library.


  ==========================================================================*/
#ifndef LIBDOCUMENTOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBDOCUMENTOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define DOCUMENTOPENCPPEXPORT	   __declspec(dllimport)
#		   define DOCUMENTOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define DOCUMENTOPENCPPTEMPLATE	 extern
#	   else
#		   define DOCUMENTOPENCPPEXPORT
#		   define DOCUMENTOPENCPPGLOBAL	   extern
#		   define DOCUMENTOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBDOCUMENTOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
