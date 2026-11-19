/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_ELECTRICALROUTING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_ELECTRICALROUTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_ELECTRICALROUTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_ELECTRICALROUTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_ELECTRICALROUTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_ELECTRICALROUTINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_ELECTRICALROUTINGEXPORT
#		   define NXOPENCPP_ELECTRICALROUTINGGLOBAL	   extern
#		   define NXOPENCPP_ELECTRICALROUTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_ELECTRICALROUTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
