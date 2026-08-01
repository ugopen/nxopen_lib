/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUFUN_WELD library.


  ==========================================================================*/
#ifndef LIBUFUN_WELD_EXPORTS_HXX_INCLUDED
#define LIBUFUN_WELD_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UFUN_WELDEXPORT	   __declspec(dllimport)
#		   define UFUN_WELDGLOBAL	   extern __declspec(dllimport)
#		   define UFUN_WELDTEMPLATE	 extern
#	   else
#		   define UFUN_WELDEXPORT
#		   define UFUN_WELDGLOBAL	   extern
#		   define UFUN_WELDTEMPLATE
#	   endif
#endif  /*  LIBUFUN_WELD_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
