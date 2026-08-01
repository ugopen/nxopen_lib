/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_PLACEMENT library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_PLACEMENT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_PLACEMENT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_PLACEMENTEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_PLACEMENTGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_PLACEMENTTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_PLACEMENTEXPORT
#		   define NXOPENCPP_PLACEMENTGLOBAL	   extern
#		   define NXOPENCPP_PLACEMENTTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_PLACEMENT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
