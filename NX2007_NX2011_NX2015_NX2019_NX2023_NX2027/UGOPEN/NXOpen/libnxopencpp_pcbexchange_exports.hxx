/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_PCBEXCHANGE library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_PCBEXCHANGE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_PCBEXCHANGE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_PCBEXCHANGEEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_PCBEXCHANGEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_PCBEXCHANGETEMPLATE	 extern
#	   else
#		   define NXOPENCPP_PCBEXCHANGEEXPORT
#		   define NXOPENCPP_PCBEXCHANGEGLOBAL	   extern
#		   define NXOPENCPP_PCBEXCHANGETEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_PCBEXCHANGE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
