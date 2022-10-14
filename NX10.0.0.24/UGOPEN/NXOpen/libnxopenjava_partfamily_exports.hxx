/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_PARTFAMILY library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_PARTFAMILY_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_PARTFAMILY_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_PARTFAMILYEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_PARTFAMILYGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_PARTFAMILYTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_PARTFAMILYEXPORT
#		   define NXOPENJAVA_PARTFAMILYGLOBAL	   extern
#		   define NXOPENJAVA_PARTFAMILYTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_PARTFAMILY_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
