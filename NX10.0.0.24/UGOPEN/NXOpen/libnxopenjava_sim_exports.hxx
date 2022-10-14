/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_SIM library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_SIM_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_SIM_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_SIMEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_SIMGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_SIMTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_SIMEXPORT
#		   define NXOPENJAVA_SIMGLOBAL	   extern
#		   define NXOPENJAVA_SIMTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_SIM_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
