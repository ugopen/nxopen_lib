/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MENDIXREPORTING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MENDIXREPORTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MENDIXREPORTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MENDIXREPORTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MENDIXREPORTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MENDIXREPORTINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MENDIXREPORTINGEXPORT
#		   define NXOPENCPP_MENDIXREPORTINGGLOBAL	   extern
#		   define NXOPENCPP_MENDIXREPORTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MENDIXREPORTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
