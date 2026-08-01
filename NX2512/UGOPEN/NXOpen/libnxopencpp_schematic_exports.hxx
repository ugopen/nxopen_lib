/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_SCHEMATIC library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_SCHEMATIC_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_SCHEMATIC_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_SCHEMATICEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_SCHEMATICGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_SCHEMATICTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_SCHEMATICEXPORT
#		   define NXOPENCPP_SCHEMATICGLOBAL	   extern
#		   define NXOPENCPP_SCHEMATICTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_SCHEMATIC_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
