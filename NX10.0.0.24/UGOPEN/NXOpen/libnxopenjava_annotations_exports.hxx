/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_ANNOTATIONS library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_ANNOTATIONS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_ANNOTATIONS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_ANNOTATIONSEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_ANNOTATIONSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_ANNOTATIONSTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_ANNOTATIONSEXPORT
#		   define NXOPENJAVA_ANNOTATIONSGLOBAL	   extern
#		   define NXOPENJAVA_ANNOTATIONSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_ANNOTATIONS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
