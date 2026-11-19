/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUGOPENINT_CAE library.


  ==========================================================================*/
#ifndef LIBUGOPENINT_CAE_EXPORTS_HXX_INCLUDED
#define LIBUGOPENINT_CAE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UGOPENINT_CAEEXPORT	   __declspec(dllimport)
#		   define UGOPENINT_CAEGLOBAL	   extern __declspec(dllimport)
#		   define UGOPENINT_CAETEMPLATE	 extern
#	   else
#		   define UGOPENINT_CAEEXPORT
#		   define UGOPENINT_CAEGLOBAL	   extern
#		   define UGOPENINT_CAETEMPLATE
#	   endif
#endif  /*  LIBUGOPENINT_CAE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
