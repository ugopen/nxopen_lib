/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_PARTFAMILY library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_PARTFAMILY_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_PARTFAMILY_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_PARTFAMILYEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_PARTFAMILYGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_PARTFAMILYTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_PARTFAMILYEXPORT
#		   define NXOPENCPP_PARTFAMILYGLOBAL	   extern
#		   define NXOPENCPP_PARTFAMILYTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_PARTFAMILY_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
