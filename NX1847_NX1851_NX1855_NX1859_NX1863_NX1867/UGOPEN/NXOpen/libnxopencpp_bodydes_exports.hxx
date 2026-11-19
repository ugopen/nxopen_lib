/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_BODYDES library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_BODYDES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_BODYDES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_BODYDESEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_BODYDESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_BODYDESTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_BODYDESEXPORT
#		   define NXOPENCPP_BODYDESGLOBAL	   extern
#		   define NXOPENCPP_BODYDESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_BODYDES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
