/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_DIE library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_DIE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_DIE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_DIEEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_DIEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_DIETEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_DIEEXPORT
#		   define NXOPENJAVA_DIEGLOBAL	   extern
#		   define NXOPENJAVA_DIETEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_DIE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
