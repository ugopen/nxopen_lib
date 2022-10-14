/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_MECHATRONICS library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_MECHATRONICS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_MECHATRONICS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_MECHATRONICSEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_MECHATRONICSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_MECHATRONICSTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_MECHATRONICSEXPORT
#		   define NXOPENJAVA_MECHATRONICSGLOBAL	   extern
#		   define NXOPENJAVA_MECHATRONICSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_MECHATRONICS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
