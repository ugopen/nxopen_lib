/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_CADCAEPREP library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_CADCAEPREP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_CADCAEPREP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_CADCAEPREPEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_CADCAEPREPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_CADCAEPREPTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_CADCAEPREPEXPORT
#		   define NXOPENCPP_CADCAEPREPGLOBAL	   extern
#		   define NXOPENCPP_CADCAEPREPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_CADCAEPREP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
