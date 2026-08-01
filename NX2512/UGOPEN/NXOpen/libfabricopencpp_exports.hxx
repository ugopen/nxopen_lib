/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBFABRICOPENCPP library.


  ==========================================================================*/
#ifndef LIBFABRICOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBFABRICOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define FABRICOPENCPPEXPORT	   __declspec(dllimport)
#		   define FABRICOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define FABRICOPENCPPTEMPLATE	 extern
#	   else
#		   define FABRICOPENCPPEXPORT
#		   define FABRICOPENCPPGLOBAL	   extern
#		   define FABRICOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBFABRICOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
