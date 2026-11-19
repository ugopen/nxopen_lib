/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_MOTION library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_MOTION_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_MOTION_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_MOTIONEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_MOTIONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_MOTIONTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_MOTIONEXPORT
#		   define NXOPENJAVA_MOTIONGLOBAL	   extern
#		   define NXOPENJAVA_MOTIONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_MOTION_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
