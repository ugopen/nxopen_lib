/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_FACET library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_FACET_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_FACET_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_FACETEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_FACETGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_FACETTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_FACETEXPORT
#		   define NXOPENCPP_FACETGLOBAL	   extern
#		   define NXOPENCPP_FACETTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_FACET_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
