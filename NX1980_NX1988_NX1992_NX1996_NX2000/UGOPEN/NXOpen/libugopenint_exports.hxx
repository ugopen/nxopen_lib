/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUGOPENINT library.


  ==========================================================================*/
#ifndef LIBUGOPENINT_EXPORTS_HXX_INCLUDED
#define LIBUGOPENINT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UGOPENINTEXPORT	   __declspec(dllimport)
#		   define UGOPENINTGLOBAL	   extern __declspec(dllimport)
#		   define UGOPENINTTEMPLATE	 extern
#	   else
#		   define UGOPENINTEXPORT
#		   define UGOPENINTGLOBAL	   extern
#		   define UGOPENINTTEMPLATE
#	   endif
#endif  /*  LIBUGOPENINT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
