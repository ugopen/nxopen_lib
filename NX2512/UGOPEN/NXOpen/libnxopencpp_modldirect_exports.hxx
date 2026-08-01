/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MODLDIRECT library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MODLDIRECT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MODLDIRECT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MODLDIRECTEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MODLDIRECTGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MODLDIRECTTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MODLDIRECTEXPORT
#		   define NXOPENCPP_MODLDIRECTGLOBAL	   extern
#		   define NXOPENCPP_MODLDIRECTTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MODLDIRECT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
