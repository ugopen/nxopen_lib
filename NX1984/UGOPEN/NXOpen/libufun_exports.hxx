/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUFUN library.


  ==========================================================================*/
#ifndef LIBUFUN_EXPORTS_HXX_INCLUDED
#define LIBUFUN_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UFUNEXPORT	   __declspec(dllimport)
#		   define UFUNGLOBAL	   extern __declspec(dllimport)
#		   define UFUNTEMPLATE	 extern
#	   else
#		   define UFUNEXPORT
#		   define UFUNGLOBAL	   extern
#		   define UFUNTEMPLATE
#	   endif
#endif  /*  LIBUFUN_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
