/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_CAEDSEWORKFLOW library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_CAEDSEWORKFLOW_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_CAEDSEWORKFLOW_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_CAEDSEWORKFLOWEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_CAEDSEWORKFLOWGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_CAEDSEWORKFLOWTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_CAEDSEWORKFLOWEXPORT
#		   define NXOPENCPP_CAEDSEWORKFLOWGLOBAL	   extern
#		   define NXOPENCPP_CAEDSEWORKFLOWTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_CAEDSEWORKFLOW_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
