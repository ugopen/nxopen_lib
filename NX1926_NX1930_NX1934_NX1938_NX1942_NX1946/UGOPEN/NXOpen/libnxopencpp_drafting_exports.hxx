/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_DRAFTING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_DRAFTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_DRAFTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_DRAFTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_DRAFTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_DRAFTINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_DRAFTINGEXPORT
#		   define NXOPENCPP_DRAFTINGGLOBAL	   extern
#		   define NXOPENCPP_DRAFTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_DRAFTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
