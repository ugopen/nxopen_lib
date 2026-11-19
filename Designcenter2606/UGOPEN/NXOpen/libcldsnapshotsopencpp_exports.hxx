/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCLDSNAPSHOTSOPENCPP library.


  ==========================================================================*/
#ifndef LIBCLDSNAPSHOTSOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCLDSNAPSHOTSOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define CLDSNAPSHOTSOPENCPPEXPORT	   __declspec(dllimport)
#		   define CLDSNAPSHOTSOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define CLDSNAPSHOTSOPENCPPTEMPLATE	 extern
#	   else
#		   define CLDSNAPSHOTSOPENCPPEXPORT
#		   define CLDSNAPSHOTSOPENCPPGLOBAL	   extern
#		   define CLDSNAPSHOTSOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCLDSNAPSHOTSOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
