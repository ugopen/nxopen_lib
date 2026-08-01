/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUFUN_VDAC library.


  ==========================================================================*/
#ifndef LIBUFUN_VDAC_EXPORTS_HXX_INCLUDED
#define LIBUFUN_VDAC_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UFUN_VDACEXPORT	   __declspec(dllimport)
#		   define UFUN_VDACGLOBAL	   extern __declspec(dllimport)
#		   define UFUN_VDACTEMPLATE	 extern
#	   else
#		   define UFUN_VDACEXPORT
#		   define UFUN_VDACGLOBAL	   extern
#		   define UFUN_VDACTEMPLATE
#	   endif
#endif  /*  LIBUFUN_VDAC_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
