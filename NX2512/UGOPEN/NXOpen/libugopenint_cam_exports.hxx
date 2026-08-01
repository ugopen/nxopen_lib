/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUGOPENINT_CAM library.


  ==========================================================================*/
#ifndef LIBUGOPENINT_CAM_EXPORTS_HXX_INCLUDED
#define LIBUGOPENINT_CAM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UGOPENINT_CAMEXPORT	   __declspec(dllimport)
#		   define UGOPENINT_CAMGLOBAL	   extern __declspec(dllimport)
#		   define UGOPENINT_CAMTEMPLATE	 extern
#	   else
#		   define UGOPENINT_CAMEXPORT
#		   define UGOPENINT_CAMGLOBAL	   extern
#		   define UGOPENINT_CAMTEMPLATE
#	   endif
#endif  /*  LIBUGOPENINT_CAM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
