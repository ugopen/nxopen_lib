/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_USERDEFINEDTEMPLATE library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_USERDEFINEDTEMPLATE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_USERDEFINEDTEMPLATE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_USERDEFINEDTEMPLATEEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_USERDEFINEDTEMPLATEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_USERDEFINEDTEMPLATETEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_USERDEFINEDTEMPLATEEXPORT
#		   define NXOPENJAVA_USERDEFINEDTEMPLATEGLOBAL	   extern
#		   define NXOPENJAVA_USERDEFINEDTEMPLATETEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_USERDEFINEDTEMPLATE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
