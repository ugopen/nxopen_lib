/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_ASSEMBLIES library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_ASSEMBLIES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_ASSEMBLIES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_ASSEMBLIESEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_ASSEMBLIESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_ASSEMBLIESTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_ASSEMBLIESEXPORT
#		   define NXOPENCPP_ASSEMBLIESGLOBAL	   extern
#		   define NXOPENCPP_ASSEMBLIESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_ASSEMBLIES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
