/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_GEOMETRICUTILITIES library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_GEOMETRICUTILITIES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_GEOMETRICUTILITIES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_GEOMETRICUTILITIESEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_GEOMETRICUTILITIESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_GEOMETRICUTILITIESTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_GEOMETRICUTILITIESEXPORT
#		   define NXOPENCPP_GEOMETRICUTILITIESGLOBAL	   extern
#		   define NXOPENCPP_GEOMETRICUTILITIESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_GEOMETRICUTILITIES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
