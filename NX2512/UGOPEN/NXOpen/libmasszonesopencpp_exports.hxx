/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBMASSZONESOPENCPP library.


  ==========================================================================*/
#ifndef LIBMASSZONESOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBMASSZONESOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define MASSZONESOPENCPPEXPORT	   __declspec(dllimport)
#		   define MASSZONESOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define MASSZONESOPENCPPTEMPLATE	 extern
#	   else
#		   define MASSZONESOPENCPPEXPORT
#		   define MASSZONESOPENCPPGLOBAL	   extern
#		   define MASSZONESOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBMASSZONESOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
