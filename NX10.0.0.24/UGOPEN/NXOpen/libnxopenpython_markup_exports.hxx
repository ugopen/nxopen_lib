/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENPYTHON_MARKUP library.


  ==========================================================================*/
#ifndef LIBNXOPENPYTHON_MARKUP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENPYTHON_MARKUP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENPYTHON_MARKUPEXPORT	   __declspec(dllimport)
#		   define NXOPENPYTHON_MARKUPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENPYTHON_MARKUPTEMPLATE	 extern
#	   else
#		   define NXOPENPYTHON_MARKUPEXPORT
#		   define NXOPENPYTHON_MARKUPGLOBAL	   extern
#		   define NXOPENPYTHON_MARKUPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENPYTHON_MARKUP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
