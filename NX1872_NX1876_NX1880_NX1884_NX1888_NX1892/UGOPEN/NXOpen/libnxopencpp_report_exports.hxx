/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_REPORT library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_REPORT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_REPORT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_REPORTEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_REPORTGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_REPORTTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_REPORTEXPORT
#		   define NXOPENCPP_REPORTGLOBAL	   extern
#		   define NXOPENCPP_REPORTTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_REPORT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
