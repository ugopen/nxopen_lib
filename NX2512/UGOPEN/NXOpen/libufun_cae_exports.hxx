/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUFUN_CAE library.


  ==========================================================================*/
#ifndef LIBUFUN_CAE_EXPORTS_HXX_INCLUDED
#define LIBUFUN_CAE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UFUN_CAEEXPORT	   __declspec(dllimport)
#		   define UFUN_CAEGLOBAL	   extern __declspec(dllimport)
#		   define UFUN_CAETEMPLATE	 extern
#	   else
#		   define UFUN_CAEEXPORT
#		   define UFUN_CAEGLOBAL	   extern
#		   define UFUN_CAETEMPLATE
#	   endif
#endif  /*  LIBUFUN_CAE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
