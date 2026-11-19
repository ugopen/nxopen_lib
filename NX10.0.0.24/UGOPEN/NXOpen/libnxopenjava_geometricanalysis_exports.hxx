/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_GEOMETRICANALYSIS library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_GEOMETRICANALYSIS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_GEOMETRICANALYSIS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_GEOMETRICANALYSISEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_GEOMETRICANALYSISGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_GEOMETRICANALYSISTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_GEOMETRICANALYSISEXPORT
#		   define NXOPENJAVA_GEOMETRICANALYSISGLOBAL	   extern
#		   define NXOPENJAVA_GEOMETRICANALYSISTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_GEOMETRICANALYSIS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
