/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENDEBUGSESSIONCPP library.


  ==========================================================================*/
#ifndef LIBNXOPENDEBUGSESSIONCPP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENDEBUGSESSIONCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENDEBUGSESSIONCPPEXPORT	   __declspec(dllimport)
#		   define NXOPENDEBUGSESSIONCPPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENDEBUGSESSIONCPPTEMPLATE	 extern
#	   else
#		   define NXOPENDEBUGSESSIONCPPEXPORT
#		   define NXOPENDEBUGSESSIONCPPGLOBAL	   extern
#		   define NXOPENDEBUGSESSIONCPPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENDEBUGSESSIONCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
