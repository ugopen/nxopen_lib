/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_DESIGNSIMULATION library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_DESIGNSIMULATION_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_DESIGNSIMULATION_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_DESIGNSIMULATIONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_DESIGNSIMULATIONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_DESIGNSIMULATIONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_DESIGNSIMULATIONEXPORT
#		   define NXOPENCPP_DESIGNSIMULATIONGLOBAL	   extern
#		   define NXOPENCPP_DESIGNSIMULATIONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_DESIGNSIMULATION_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
