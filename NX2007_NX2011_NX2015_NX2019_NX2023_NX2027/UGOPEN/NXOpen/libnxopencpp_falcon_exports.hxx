/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_FALCON library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_FALCON_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_FALCON_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_FALCONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_FALCONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_FALCONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_FALCONEXPORT
#		   define NXOPENCPP_FALCONGLOBAL	   extern
#		   define NXOPENCPP_FALCONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_FALCON_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
