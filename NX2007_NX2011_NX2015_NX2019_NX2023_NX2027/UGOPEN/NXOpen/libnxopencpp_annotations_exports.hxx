/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_ANNOTATIONS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_ANNOTATIONS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_ANNOTATIONS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_ANNOTATIONSEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_ANNOTATIONSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_ANNOTATIONSTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_ANNOTATIONSEXPORT
#		   define NXOPENCPP_ANNOTATIONSGLOBAL	   extern
#		   define NXOPENCPP_ANNOTATIONSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_ANNOTATIONS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
