/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_GATEWAY library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_GATEWAY_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_GATEWAY_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_GATEWAYEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_GATEWAYGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_GATEWAYTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_GATEWAYEXPORT
#		   define NXOPENJAVA_GATEWAYGLOBAL	   extern
#		   define NXOPENJAVA_GATEWAYTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_GATEWAY_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
