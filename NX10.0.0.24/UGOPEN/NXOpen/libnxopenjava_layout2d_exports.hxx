/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_LAYOUT2D library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_LAYOUT2D_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_LAYOUT2D_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_LAYOUT2DEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_LAYOUT2DGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_LAYOUT2DTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_LAYOUT2DEXPORT
#		   define NXOPENJAVA_LAYOUT2DGLOBAL	   extern
#		   define NXOPENJAVA_LAYOUT2DTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_LAYOUT2D_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
