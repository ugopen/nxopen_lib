/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_DIE library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_DIE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_DIE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_DIEEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_DIEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_DIETEMPLATE	 extern
#	   else
#		   define NXOPENCPP_DIEEXPORT
#		   define NXOPENCPP_DIEGLOBAL	   extern
#		   define NXOPENCPP_DIETEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_DIE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
