/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_VISUALREPORTING library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_VISUALREPORTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_VISUALREPORTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_VISUALREPORTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_VISUALREPORTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_VISUALREPORTINGTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_VISUALREPORTINGEXPORT
#		   define NXOPENJAVA_VISUALREPORTINGGLOBAL	   extern
#		   define NXOPENJAVA_VISUALREPORTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_VISUALREPORTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
