/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_SHEETMETAL library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_SHEETMETAL_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_SHEETMETAL_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_SHEETMETALEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_SHEETMETALGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_SHEETMETALTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_SHEETMETALEXPORT
#		   define NXOPENCPP_SHEETMETALGLOBAL	   extern
#		   define NXOPENCPP_SHEETMETALTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_SHEETMETAL_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
