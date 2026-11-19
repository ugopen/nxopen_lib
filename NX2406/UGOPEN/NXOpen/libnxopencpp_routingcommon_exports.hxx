/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_ROUTINGCOMMON library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_ROUTINGCOMMON_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_ROUTINGCOMMON_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_ROUTINGCOMMONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_ROUTINGCOMMONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_ROUTINGCOMMONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_ROUTINGCOMMONEXPORT
#		   define NXOPENCPP_ROUTINGCOMMONGLOBAL	   extern
#		   define NXOPENCPP_ROUTINGCOMMONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_ROUTINGCOMMON_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
