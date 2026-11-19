/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_ROUTING library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_ROUTING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_ROUTING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_ROUTINGEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_ROUTINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_ROUTINGTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_ROUTINGEXPORT
#		   define NXOPENJAVA_ROUTINGGLOBAL	   extern
#		   define NXOPENJAVA_ROUTINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_ROUTING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
