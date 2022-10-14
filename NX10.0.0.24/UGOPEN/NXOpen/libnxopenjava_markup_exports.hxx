/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_MARKUP library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_MARKUP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_MARKUP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_MARKUPEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_MARKUPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_MARKUPTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_MARKUPEXPORT
#		   define NXOPENJAVA_MARKUPGLOBAL	   extern
#		   define NXOPENJAVA_MARKUPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_MARKUP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
