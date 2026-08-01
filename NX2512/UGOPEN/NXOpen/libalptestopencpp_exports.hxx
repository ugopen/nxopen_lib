/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBALPTESTOPENCPP library.


  ==========================================================================*/
#ifndef LIBALPTESTOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBALPTESTOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define ALPTESTOPENCPPEXPORT	   __declspec(dllimport)
#		   define ALPTESTOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define ALPTESTOPENCPPTEMPLATE	 extern
#	   else
#		   define ALPTESTOPENCPPEXPORT
#		   define ALPTESTOPENCPPGLOBAL	   extern
#		   define ALPTESTOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBALPTESTOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
