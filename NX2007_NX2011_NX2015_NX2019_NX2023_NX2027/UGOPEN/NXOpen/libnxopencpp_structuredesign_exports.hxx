/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_STRUCTUREDESIGN library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_STRUCTUREDESIGN_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_STRUCTUREDESIGN_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_STRUCTUREDESIGNEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_STRUCTUREDESIGNGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_STRUCTUREDESIGNTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_STRUCTUREDESIGNEXPORT
#		   define NXOPENCPP_STRUCTUREDESIGNGLOBAL	   extern
#		   define NXOPENCPP_STRUCTUREDESIGNTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_STRUCTUREDESIGN_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
