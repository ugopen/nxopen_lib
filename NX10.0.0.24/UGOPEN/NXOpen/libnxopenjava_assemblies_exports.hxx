/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_ASSEMBLIES library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_ASSEMBLIES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_ASSEMBLIES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_ASSEMBLIESEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_ASSEMBLIESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_ASSEMBLIESTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_ASSEMBLIESEXPORT
#		   define NXOPENJAVA_ASSEMBLIESGLOBAL	   extern
#		   define NXOPENJAVA_ASSEMBLIESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_ASSEMBLIES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
