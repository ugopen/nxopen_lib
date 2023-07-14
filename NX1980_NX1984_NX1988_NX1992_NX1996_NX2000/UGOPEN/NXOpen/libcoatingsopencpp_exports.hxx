/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCOATINGSOPENCPP library.


  ==========================================================================*/
#ifndef LIBCOATINGSOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCOATINGSOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define COATINGSOPENCPPEXPORT	   __declspec(dllimport)
#		   define COATINGSOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define COATINGSOPENCPPTEMPLATE	 extern
#	   else
#		   define COATINGSOPENCPPEXPORT
#		   define COATINGSOPENCPPGLOBAL	   extern
#		   define COATINGSOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCOATINGSOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
