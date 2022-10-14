/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MECHATRONICS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MECHATRONICS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MECHATRONICS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MECHATRONICSEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MECHATRONICSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MECHATRONICSTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MECHATRONICSEXPORT
#		   define NXOPENCPP_MECHATRONICSGLOBAL	   extern
#		   define NXOPENCPP_MECHATRONICSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MECHATRONICS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
