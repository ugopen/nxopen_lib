/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJSON_ALP library.


  ==========================================================================*/
#ifndef LIBNXOPENJSON_ALP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJSON_ALP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJSON_ALPEXPORT	   __declspec(dllimport)
#		   define NXOPENJSON_ALPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJSON_ALPTEMPLATE	 extern
#	   else
#		   define NXOPENJSON_ALPEXPORT
#		   define NXOPENJSON_ALPGLOBAL	   extern
#		   define NXOPENJSON_ALPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJSON_ALP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
