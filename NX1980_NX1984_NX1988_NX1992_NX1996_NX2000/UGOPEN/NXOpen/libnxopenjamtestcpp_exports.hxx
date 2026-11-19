/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAMTESTCPP library.


  ==========================================================================*/
#ifndef LIBNXOPENJAMTESTCPP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAMTESTCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAMTESTCPPEXPORT	   __declspec(dllimport)
#		   define NXOPENJAMTESTCPPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAMTESTCPPTEMPLATE	 extern
#	   else
#		   define NXOPENJAMTESTCPPEXPORT
#		   define NXOPENJAMTESTCPPGLOBAL	   extern
#		   define NXOPENJAMTESTCPPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAMTESTCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
