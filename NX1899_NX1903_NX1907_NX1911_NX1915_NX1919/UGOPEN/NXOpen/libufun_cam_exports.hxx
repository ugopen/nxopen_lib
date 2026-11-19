/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUFUN_CAM library.


  ==========================================================================*/
#ifndef LIBUFUN_CAM_EXPORTS_HXX_INCLUDED
#define LIBUFUN_CAM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UFUN_CAMEXPORT	   __declspec(dllimport)
#		   define UFUN_CAMGLOBAL	   extern __declspec(dllimport)
#		   define UFUN_CAMTEMPLATE	 extern
#	   else
#		   define UFUN_CAMEXPORT
#		   define UFUN_CAMGLOBAL	   extern
#		   define UFUN_CAMTEMPLATE
#	   endif
#endif  /*  LIBUFUN_CAM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
