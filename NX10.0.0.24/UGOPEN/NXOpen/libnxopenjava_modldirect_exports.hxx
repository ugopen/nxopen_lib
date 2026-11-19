/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_MODLDIRECT library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_MODLDIRECT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_MODLDIRECT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_MODLDIRECTEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_MODLDIRECTGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_MODLDIRECTTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_MODLDIRECTEXPORT
#		   define NXOPENJAVA_MODLDIRECTGLOBAL	   extern
#		   define NXOPENJAVA_MODLDIRECTTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_MODLDIRECT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
