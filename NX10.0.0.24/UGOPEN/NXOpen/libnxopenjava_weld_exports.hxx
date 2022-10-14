/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_WELD library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_WELD_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_WELD_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_WELDEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_WELDGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_WELDTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_WELDEXPORT
#		   define NXOPENJAVA_WELDGLOBAL	   extern
#		   define NXOPENJAVA_WELDTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_WELD_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
