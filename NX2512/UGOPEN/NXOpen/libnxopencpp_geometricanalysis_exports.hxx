/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_GEOMETRICANALYSIS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_GEOMETRICANALYSIS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_GEOMETRICANALYSIS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_GEOMETRICANALYSISEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_GEOMETRICANALYSISGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_GEOMETRICANALYSISTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_GEOMETRICANALYSISEXPORT
#		   define NXOPENCPP_GEOMETRICANALYSISGLOBAL	   extern
#		   define NXOPENCPP_GEOMETRICANALYSISTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_GEOMETRICANALYSIS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
