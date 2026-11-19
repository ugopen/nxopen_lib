/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_CAE library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_CAE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_CAE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_CAEEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_CAEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_CAETEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_CAEEXPORT
#		   define NXOPENJAVA_CAEGLOBAL	   extern
#		   define NXOPENJAVA_CAETEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_CAE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
