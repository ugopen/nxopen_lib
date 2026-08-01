/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_SHIPDESIGN library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_SHIPDESIGN_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_SHIPDESIGN_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_SHIPDESIGNEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_SHIPDESIGNGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_SHIPDESIGNTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_SHIPDESIGNEXPORT
#		   define NXOPENCPP_SHIPDESIGNGLOBAL	   extern
#		   define NXOPENCPP_SHIPDESIGNTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_SHIPDESIGN_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
