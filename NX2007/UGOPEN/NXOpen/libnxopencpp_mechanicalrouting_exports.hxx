/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MECHANICALROUTING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MECHANICALROUTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MECHANICALROUTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MECHANICALROUTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MECHANICALROUTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MECHANICALROUTINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MECHANICALROUTINGEXPORT
#		   define NXOPENCPP_MECHANICALROUTINGGLOBAL	   extern
#		   define NXOPENCPP_MECHANICALROUTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MECHANICALROUTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
