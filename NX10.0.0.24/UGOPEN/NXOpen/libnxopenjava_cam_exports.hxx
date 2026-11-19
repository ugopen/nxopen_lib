/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_CAM library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_CAM_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_CAM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_CAMEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_CAMGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_CAMTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_CAMEXPORT
#		   define NXOPENJAVA_CAMGLOBAL	   extern
#		   define NXOPENJAVA_CAMTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_CAM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
