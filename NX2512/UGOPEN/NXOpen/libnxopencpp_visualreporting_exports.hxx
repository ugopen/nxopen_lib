/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_VISUALREPORTING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_VISUALREPORTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_VISUALREPORTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_VISUALREPORTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_VISUALREPORTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_VISUALREPORTINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_VISUALREPORTINGEXPORT
#		   define NXOPENCPP_VISUALREPORTINGGLOBAL	   extern
#		   define NXOPENCPP_VISUALREPORTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_VISUALREPORTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
