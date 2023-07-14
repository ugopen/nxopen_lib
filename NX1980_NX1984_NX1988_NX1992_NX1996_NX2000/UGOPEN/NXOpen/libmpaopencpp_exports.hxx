/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBMPAOPENCPP library.


  ==========================================================================*/
#ifndef LIBMPAOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBMPAOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define MPAOPENCPPEXPORT	   __declspec(dllimport)
#		   define MPAOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define MPAOPENCPPTEMPLATE	 extern
#	   else
#		   define MPAOPENCPPEXPORT
#		   define MPAOPENCPPGLOBAL	   extern
#		   define MPAOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBMPAOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
