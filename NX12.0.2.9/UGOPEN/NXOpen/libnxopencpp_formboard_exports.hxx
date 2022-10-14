/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_FORMBOARD library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_FORMBOARD_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_FORMBOARD_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_FORMBOARDEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_FORMBOARDGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_FORMBOARDTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_FORMBOARDEXPORT
#		   define NXOPENCPP_FORMBOARDGLOBAL	   extern
#		   define NXOPENCPP_FORMBOARDTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_FORMBOARD_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
