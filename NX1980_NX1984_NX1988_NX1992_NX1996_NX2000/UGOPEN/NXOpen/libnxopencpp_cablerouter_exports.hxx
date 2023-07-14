/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_CABLEROUTER library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_CABLEROUTER_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_CABLEROUTER_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_CABLEROUTEREXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_CABLEROUTERGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_CABLEROUTERTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_CABLEROUTEREXPORT
#		   define NXOPENCPP_CABLEROUTERGLOBAL	   extern
#		   define NXOPENCPP_CABLEROUTERTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_CABLEROUTER_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
