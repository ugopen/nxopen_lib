/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_DRAFTING library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_DRAFTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_DRAFTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_DRAFTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_DRAFTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_DRAFTINGTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_DRAFTINGEXPORT
#		   define NXOPENJAVA_DRAFTINGGLOBAL	   extern
#		   define NXOPENJAVA_DRAFTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_DRAFTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
