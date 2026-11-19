/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_PDM library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_PDM_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_PDM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_PDMEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_PDMGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_PDMTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_PDMEXPORT
#		   define NXOPENJAVA_PDMGLOBAL	   extern
#		   define NXOPENJAVA_PDMTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_PDM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
