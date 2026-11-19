/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_SUSTAINABILITY library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_SUSTAINABILITY_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_SUSTAINABILITY_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_SUSTAINABILITYEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_SUSTAINABILITYGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_SUSTAINABILITYTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_SUSTAINABILITYEXPORT
#		   define NXOPENCPP_SUSTAINABILITYGLOBAL	   extern
#		   define NXOPENCPP_SUSTAINABILITYTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_SUSTAINABILITY_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
