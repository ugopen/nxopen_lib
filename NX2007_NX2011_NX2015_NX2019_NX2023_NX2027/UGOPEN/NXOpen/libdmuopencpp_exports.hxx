/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBDMUOPENCPP library.


  ==========================================================================*/
#ifndef LIBDMUOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBDMUOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define DMUOPENCPPEXPORT	   __declspec(dllimport)
#		   define DMUOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define DMUOPENCPPTEMPLATE	 extern
#	   else
#		   define DMUOPENCPPEXPORT
#		   define DMUOPENCPPGLOBAL	   extern
#		   define DMUOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBDMUOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
