/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_PHYSMAT library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_PHYSMAT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_PHYSMAT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_PHYSMATEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_PHYSMATGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_PHYSMATTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_PHYSMATEXPORT
#		   define NXOPENCPP_PHYSMATGLOBAL	   extern
#		   define NXOPENCPP_PHYSMATTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_PHYSMAT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
