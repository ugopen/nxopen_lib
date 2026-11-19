/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_PHYSMAT library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_PHYSMAT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_PHYSMAT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_PHYSMATEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_PHYSMATGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_PHYSMATTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_PHYSMATEXPORT
#		   define NXOPENJAVA_PHYSMATGLOBAL	   extern
#		   define NXOPENJAVA_PHYSMATTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_PHYSMAT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
