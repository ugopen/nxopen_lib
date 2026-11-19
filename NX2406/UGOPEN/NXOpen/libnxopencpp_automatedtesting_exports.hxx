/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_AUTOMATEDTESTING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_AUTOMATEDTESTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_AUTOMATEDTESTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_AUTOMATEDTESTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_AUTOMATEDTESTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_AUTOMATEDTESTINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_AUTOMATEDTESTINGEXPORT
#		   define NXOPENCPP_AUTOMATEDTESTINGGLOBAL	   extern
#		   define NXOPENCPP_AUTOMATEDTESTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_AUTOMATEDTESTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
