/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_VALIDATE library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_VALIDATE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_VALIDATE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_VALIDATEEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_VALIDATEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_VALIDATETEMPLATE	 extern
#	   else
#		   define NXOPENCPP_VALIDATEEXPORT
#		   define NXOPENCPP_VALIDATEGLOBAL	   extern
#		   define NXOPENCPP_VALIDATETEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_VALIDATE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
