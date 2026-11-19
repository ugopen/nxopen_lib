/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_SHAPESEARCH library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_SHAPESEARCH_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_SHAPESEARCH_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_SHAPESEARCHEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_SHAPESEARCHGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_SHAPESEARCHTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_SHAPESEARCHEXPORT
#		   define NXOPENJAVA_SHAPESEARCHGLOBAL	   extern
#		   define NXOPENJAVA_SHAPESEARCHTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_SHAPESEARCH_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
