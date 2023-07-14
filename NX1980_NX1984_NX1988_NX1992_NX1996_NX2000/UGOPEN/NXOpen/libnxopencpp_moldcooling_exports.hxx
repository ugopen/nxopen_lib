/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MOLDCOOLING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MOLDCOOLING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MOLDCOOLING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MOLDCOOLINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MOLDCOOLINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MOLDCOOLINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MOLDCOOLINGEXPORT
#		   define NXOPENCPP_MOLDCOOLINGGLOBAL	   extern
#		   define NXOPENCPP_MOLDCOOLINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MOLDCOOLING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
