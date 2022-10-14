/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MFG library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MFG_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MFG_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MFGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MFGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MFGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MFGEXPORT
#		   define NXOPENCPP_MFGGLOBAL	   extern
#		   define NXOPENCPP_MFGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MFG_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
