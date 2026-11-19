/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MOTIONDSEWORKFLOW library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MOTIONDSEWORKFLOW_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MOTIONDSEWORKFLOW_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MOTIONDSEWORKFLOWEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MOTIONDSEWORKFLOWGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MOTIONDSEWORKFLOWTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MOTIONDSEWORKFLOWEXPORT
#		   define NXOPENCPP_MOTIONDSEWORKFLOWGLOBAL	   extern
#		   define NXOPENCPP_MOTIONDSEWORKFLOWTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MOTIONDSEWORKFLOW_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
