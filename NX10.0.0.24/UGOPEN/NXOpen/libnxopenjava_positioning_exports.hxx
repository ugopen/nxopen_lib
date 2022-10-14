/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_POSITIONING library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_POSITIONING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_POSITIONING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_POSITIONINGEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_POSITIONINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_POSITIONINGTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_POSITIONINGEXPORT
#		   define NXOPENJAVA_POSITIONINGGLOBAL	   extern
#		   define NXOPENJAVA_POSITIONINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_POSITIONING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
