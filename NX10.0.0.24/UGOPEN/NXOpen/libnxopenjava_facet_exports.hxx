/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_FACET library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_FACET_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_FACET_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_FACETEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_FACETGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_FACETTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_FACETEXPORT
#		   define NXOPENJAVA_FACETGLOBAL	   extern
#		   define NXOPENJAVA_FACETTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_FACET_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
