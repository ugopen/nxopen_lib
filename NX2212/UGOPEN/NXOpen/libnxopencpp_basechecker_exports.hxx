/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_BASECHECKER library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_BASECHECKER_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_BASECHECKER_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_BASECHECKEREXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_BASECHECKERGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_BASECHECKERTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_BASECHECKEREXPORT
#		   define NXOPENCPP_BASECHECKERGLOBAL	   extern
#		   define NXOPENCPP_BASECHECKERTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_BASECHECKER_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
