/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBECLASSSTANDARDOPENCPP library.


  ==========================================================================*/
#ifndef LIBECLASSSTANDARDOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBECLASSSTANDARDOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define ECLASSSTANDARDOPENCPPEXPORT	   __declspec(dllimport)
#		   define ECLASSSTANDARDOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define ECLASSSTANDARDOPENCPPTEMPLATE	 extern
#	   else
#		   define ECLASSSTANDARDOPENCPPEXPORT
#		   define ECLASSSTANDARDOPENCPPGLOBAL	   extern
#		   define ECLASSSTANDARDOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBECLASSSTANDARDOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
