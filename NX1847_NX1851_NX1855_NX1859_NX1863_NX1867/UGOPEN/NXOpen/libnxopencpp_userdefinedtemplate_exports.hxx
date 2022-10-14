/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_USERDEFINEDTEMPLATE library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_USERDEFINEDTEMPLATE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_USERDEFINEDTEMPLATE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_USERDEFINEDTEMPLATEEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_USERDEFINEDTEMPLATEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_USERDEFINEDTEMPLATETEMPLATE	 extern
#	   else
#		   define NXOPENCPP_USERDEFINEDTEMPLATEEXPORT
#		   define NXOPENCPP_USERDEFINEDTEMPLATEGLOBAL	   extern
#		   define NXOPENCPP_USERDEFINEDTEMPLATETEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_USERDEFINEDTEMPLATE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
