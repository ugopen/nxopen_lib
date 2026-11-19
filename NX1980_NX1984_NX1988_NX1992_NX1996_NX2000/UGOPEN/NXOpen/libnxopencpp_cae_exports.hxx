/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_CAE library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_CAE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_CAE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_CAEEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_CAEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_CAETEMPLATE	 extern
#	   else
#		   define NXOPENCPP_CAEEXPORT
#		   define NXOPENCPP_CAEGLOBAL	   extern
#		   define NXOPENCPP_CAETEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_CAE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
