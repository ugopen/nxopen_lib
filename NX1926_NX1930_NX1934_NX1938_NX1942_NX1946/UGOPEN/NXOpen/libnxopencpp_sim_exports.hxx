/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_SIM library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_SIM_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_SIM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_SIMEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_SIMGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_SIMTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_SIMEXPORT
#		   define NXOPENCPP_SIMGLOBAL	   extern
#		   define NXOPENCPP_SIMTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_SIM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
