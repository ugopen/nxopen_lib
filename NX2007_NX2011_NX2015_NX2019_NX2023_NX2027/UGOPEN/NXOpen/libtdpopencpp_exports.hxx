/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBTDPOPENCPP library.


  ==========================================================================*/
#ifndef LIBTDPOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBTDPOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define TDPOPENCPPEXPORT	   __declspec(dllimport)
#		   define TDPOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define TDPOPENCPPTEMPLATE	 extern
#	   else
#		   define TDPOPENCPPEXPORT
#		   define TDPOPENCPPGLOBAL	   extern
#		   define TDPOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBTDPOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
