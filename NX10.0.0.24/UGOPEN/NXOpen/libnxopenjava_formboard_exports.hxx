/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_FORMBOARD library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_FORMBOARD_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_FORMBOARD_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_FORMBOARDEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_FORMBOARDGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_FORMBOARDTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_FORMBOARDEXPORT
#		   define NXOPENJAVA_FORMBOARDGLOBAL	   extern
#		   define NXOPENJAVA_FORMBOARDTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_FORMBOARD_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
