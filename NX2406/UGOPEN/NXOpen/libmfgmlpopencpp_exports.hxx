/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBMFGMLPOPENCPP library.


  ==========================================================================*/
#ifndef LIBMFGMLPOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBMFGMLPOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define MFGMLPOPENCPPEXPORT	   __declspec(dllimport)
#		   define MFGMLPOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define MFGMLPOPENCPPTEMPLATE	 extern
#	   else
#		   define MFGMLPOPENCPPEXPORT
#		   define MFGMLPOPENCPPGLOBAL	   extern
#		   define MFGMLPOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBMFGMLPOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
