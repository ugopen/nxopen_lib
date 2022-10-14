/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_DISPLAY library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_DISPLAY_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_DISPLAY_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_DISPLAYEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_DISPLAYGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_DISPLAYTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_DISPLAYEXPORT
#		   define NXOPENJAVA_DISPLAYGLOBAL	   extern
#		   define NXOPENJAVA_DISPLAYTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_DISPLAY_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
