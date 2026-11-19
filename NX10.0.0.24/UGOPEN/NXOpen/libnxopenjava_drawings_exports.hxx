/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_DRAWINGS library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_DRAWINGS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_DRAWINGS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_DRAWINGSEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_DRAWINGSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_DRAWINGSTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_DRAWINGSEXPORT
#		   define NXOPENJAVA_DRAWINGSGLOBAL	   extern
#		   define NXOPENJAVA_DRAWINGSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_DRAWINGS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
