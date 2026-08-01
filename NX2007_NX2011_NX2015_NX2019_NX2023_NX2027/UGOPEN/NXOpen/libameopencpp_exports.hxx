/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBAMEOPENCPP library.


  ==========================================================================*/
#ifndef LIBAMEOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBAMEOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define AMEOPENCPPEXPORT	   __declspec(dllimport)
#		   define AMEOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define AMEOPENCPPTEMPLATE	 extern
#	   else
#		   define AMEOPENCPPEXPORT
#		   define AMEOPENCPPGLOBAL	   extern
#		   define AMEOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBAMEOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
