/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MBD library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MBD_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MBD_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MBDEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MBDGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MBDTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MBDEXPORT
#		   define NXOPENCPP_MBDGLOBAL	   extern
#		   define NXOPENCPP_MBDTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MBD_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
