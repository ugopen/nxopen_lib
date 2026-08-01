/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_PDM library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_PDM_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_PDM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_PDMEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_PDMGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_PDMTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_PDMEXPORT
#		   define NXOPENCPP_PDMGLOBAL	   extern
#		   define NXOPENCPP_PDMTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_PDM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
