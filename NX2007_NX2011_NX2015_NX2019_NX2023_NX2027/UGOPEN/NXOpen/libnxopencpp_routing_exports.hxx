/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_ROUTING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_ROUTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_ROUTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_ROUTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_ROUTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_ROUTINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_ROUTINGEXPORT
#		   define NXOPENCPP_ROUTINGGLOBAL	   extern
#		   define NXOPENCPP_ROUTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_ROUTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
