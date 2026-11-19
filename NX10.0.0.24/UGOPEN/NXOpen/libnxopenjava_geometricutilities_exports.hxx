/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_GEOMETRICUTILITIES library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_GEOMETRICUTILITIES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_GEOMETRICUTILITIES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_GEOMETRICUTILITIESEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_GEOMETRICUTILITIESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_GEOMETRICUTILITIESTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_GEOMETRICUTILITIESEXPORT
#		   define NXOPENJAVA_GEOMETRICUTILITIESGLOBAL	   extern
#		   define NXOPENJAVA_GEOMETRICUTILITIESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_GEOMETRICUTILITIES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
