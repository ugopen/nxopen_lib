/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_VALIDATE library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_VALIDATE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_VALIDATE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_VALIDATEEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_VALIDATEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_VALIDATETEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_VALIDATEEXPORT
#		   define NXOPENJAVA_VALIDATEGLOBAL	   extern
#		   define NXOPENJAVA_VALIDATETEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_VALIDATE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
