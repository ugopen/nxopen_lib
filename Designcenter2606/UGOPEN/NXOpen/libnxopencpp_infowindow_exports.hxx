/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_INFOWINDOW library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_INFOWINDOW_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_INFOWINDOW_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_INFOWINDOWEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_INFOWINDOWGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_INFOWINDOWTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_INFOWINDOWEXPORT
#		   define NXOPENCPP_INFOWINDOWGLOBAL	   extern
#		   define NXOPENCPP_INFOWINDOWTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_INFOWINDOW_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
