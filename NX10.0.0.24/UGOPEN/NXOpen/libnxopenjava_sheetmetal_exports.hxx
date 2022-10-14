/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_SHEETMETAL library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_SHEETMETAL_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_SHEETMETAL_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_SHEETMETALEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_SHEETMETALGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_SHEETMETALTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_SHEETMETALEXPORT
#		   define NXOPENJAVA_SHEETMETALGLOBAL	   extern
#		   define NXOPENJAVA_SHEETMETALTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_SHEETMETAL_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
