/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_GATEWAY library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_GATEWAY_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_GATEWAY_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_GATEWAYEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_GATEWAYGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_GATEWAYTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_GATEWAYEXPORT
#		   define NXOPENCPP_GATEWAYGLOBAL	   extern
#		   define NXOPENCPP_GATEWAYTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_GATEWAY_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
