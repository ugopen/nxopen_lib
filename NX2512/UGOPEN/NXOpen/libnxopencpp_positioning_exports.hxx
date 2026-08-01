/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_POSITIONING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_POSITIONING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_POSITIONING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_POSITIONINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_POSITIONINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_POSITIONINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_POSITIONINGEXPORT
#		   define NXOPENCPP_POSITIONINGGLOBAL	   extern
#		   define NXOPENCPP_POSITIONINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_POSITIONING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
