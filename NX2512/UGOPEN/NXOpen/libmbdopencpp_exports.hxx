/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBMBDOPENCPP library.


  ==========================================================================*/
#ifndef LIBMBDOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBMBDOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define MBDOPENCPPEXPORT	   __declspec(dllimport)
#		   define MBDOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define MBDOPENCPPTEMPLATE	 extern
#	   else
#		   define MBDOPENCPPEXPORT
#		   define MBDOPENCPPGLOBAL	   extern
#		   define MBDOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBMBDOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
