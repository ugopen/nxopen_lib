/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJSON_MENDIXREPORTING library.


  ==========================================================================*/
#ifndef LIBNXOPENJSON_MENDIXREPORTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJSON_MENDIXREPORTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJSON_MENDIXREPORTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENJSON_MENDIXREPORTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJSON_MENDIXREPORTINGTEMPLATE	 extern
#	   else
#		   define NXOPENJSON_MENDIXREPORTINGEXPORT
#		   define NXOPENJSON_MENDIXREPORTINGGLOBAL	   extern
#		   define NXOPENJSON_MENDIXREPORTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJSON_MENDIXREPORTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
