/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_TOOLING library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_TOOLING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_TOOLING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_TOOLINGEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_TOOLINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_TOOLINGTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_TOOLINGEXPORT
#		   define NXOPENJAVA_TOOLINGGLOBAL	   extern
#		   define NXOPENJAVA_TOOLINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_TOOLING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
