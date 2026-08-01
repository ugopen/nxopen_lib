/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBMFGAMOPENCPP library.


  ==========================================================================*/
#ifndef LIBMFGAMOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBMFGAMOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define MFGAMOPENCPPEXPORT	   __declspec(dllimport)
#		   define MFGAMOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define MFGAMOPENCPPTEMPLATE	 extern
#	   else
#		   define MFGAMOPENCPPEXPORT
#		   define MFGAMOPENCPPGLOBAL	   extern
#		   define MFGAMOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBMFGAMOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
