/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBPRESSLINESIMULOPENCPP library.


  ==========================================================================*/
#ifndef LIBPRESSLINESIMULOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBPRESSLINESIMULOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define PRESSLINESIMULOPENCPPEXPORT	   __declspec(dllimport)
#		   define PRESSLINESIMULOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define PRESSLINESIMULOPENCPPTEMPLATE	 extern
#	   else
#		   define PRESSLINESIMULOPENCPPEXPORT
#		   define PRESSLINESIMULOPENCPPGLOBAL	   extern
#		   define PRESSLINESIMULOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBPRESSLINESIMULOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
