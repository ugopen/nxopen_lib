/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_KDPACKAGING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_KDPACKAGING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_KDPACKAGING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_KDPACKAGINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_KDPACKAGINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_KDPACKAGINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_KDPACKAGINGEXPORT
#		   define NXOPENCPP_KDPACKAGINGGLOBAL	   extern
#		   define NXOPENCPP_KDPACKAGINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_KDPACKAGING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
