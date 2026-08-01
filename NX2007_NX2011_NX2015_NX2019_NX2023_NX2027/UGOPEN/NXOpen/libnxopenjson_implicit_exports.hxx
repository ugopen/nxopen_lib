/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJSON_IMPLICIT library.


  ==========================================================================*/
#ifndef LIBNXOPENJSON_IMPLICIT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJSON_IMPLICIT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJSON_IMPLICITEXPORT	   __declspec(dllimport)
#		   define NXOPENJSON_IMPLICITGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJSON_IMPLICITTEMPLATE	 extern
#	   else
#		   define NXOPENJSON_IMPLICITEXPORT
#		   define NXOPENJSON_IMPLICITGLOBAL	   extern
#		   define NXOPENJSON_IMPLICITTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJSON_IMPLICIT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
