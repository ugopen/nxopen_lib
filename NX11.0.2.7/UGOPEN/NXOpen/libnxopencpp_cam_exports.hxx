/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_CAM library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_CAM_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_CAM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_CAMEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_CAMGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_CAMTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_CAMEXPORT
#		   define NXOPENCPP_CAMGLOBAL	   extern
#		   define NXOPENCPP_CAMTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_CAM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
