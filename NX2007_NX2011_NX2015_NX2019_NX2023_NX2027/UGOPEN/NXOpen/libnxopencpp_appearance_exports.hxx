/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_APPEARANCE library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_APPEARANCE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_APPEARANCE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_APPEARANCEEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_APPEARANCEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_APPEARANCETEMPLATE	 extern
#	   else
#		   define NXOPENCPP_APPEARANCEEXPORT
#		   define NXOPENCPP_APPEARANCEGLOBAL	   extern
#		   define NXOPENCPP_APPEARANCETEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_APPEARANCE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
