/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_TOOLING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_TOOLING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_TOOLING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_TOOLINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_TOOLINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_TOOLINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_TOOLINGEXPORT
#		   define NXOPENCPP_TOOLINGGLOBAL	   extern
#		   define NXOPENCPP_TOOLINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_TOOLING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
