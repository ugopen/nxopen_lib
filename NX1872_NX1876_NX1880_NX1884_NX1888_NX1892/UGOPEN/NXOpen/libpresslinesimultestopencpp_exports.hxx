/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBPRESSLINESIMULTESTOPENCPP library.


  ==========================================================================*/
#ifndef LIBPRESSLINESIMULTESTOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBPRESSLINESIMULTESTOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define PRESSLINESIMULTESTOPENCPPEXPORT	   __declspec(dllimport)
#		   define PRESSLINESIMULTESTOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define PRESSLINESIMULTESTOPENCPPTEMPLATE	 extern
#	   else
#		   define PRESSLINESIMULTESTOPENCPPEXPORT
#		   define PRESSLINESIMULTESTOPENCPPGLOBAL	   extern
#		   define PRESSLINESIMULTESTOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBPRESSLINESIMULTESTOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
