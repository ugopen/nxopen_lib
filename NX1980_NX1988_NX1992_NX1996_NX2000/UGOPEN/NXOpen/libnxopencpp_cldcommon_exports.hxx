/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_CLDCOMMON library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_CLDCOMMON_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_CLDCOMMON_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_CLDCOMMONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_CLDCOMMONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_CLDCOMMONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_CLDCOMMONEXPORT
#		   define NXOPENCPP_CLDCOMMONGLOBAL	   extern
#		   define NXOPENCPP_CLDCOMMONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_CLDCOMMON_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
