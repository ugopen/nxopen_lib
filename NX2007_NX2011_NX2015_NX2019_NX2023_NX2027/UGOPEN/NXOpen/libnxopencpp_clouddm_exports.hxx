/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_CLOUDDM library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_CLOUDDM_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_CLOUDDM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_CLOUDDMEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_CLOUDDMGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_CLOUDDMTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_CLOUDDMEXPORT
#		   define NXOPENCPP_CLOUDDMGLOBAL	   extern
#		   define NXOPENCPP_CLOUDDMTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_CLOUDDM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
