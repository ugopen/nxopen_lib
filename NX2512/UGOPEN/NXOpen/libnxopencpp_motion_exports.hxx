/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MOTION library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MOTION_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MOTION_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MOTIONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MOTIONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MOTIONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MOTIONEXPORT
#		   define NXOPENCPP_MOTIONGLOBAL	   extern
#		   define NXOPENCPP_MOTIONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MOTION_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
