/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_DIAGRAMMING library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_DIAGRAMMING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_DIAGRAMMING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_DIAGRAMMINGEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_DIAGRAMMINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_DIAGRAMMINGTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_DIAGRAMMINGEXPORT
#		   define NXOPENCPP_DIAGRAMMINGGLOBAL	   extern
#		   define NXOPENCPP_DIAGRAMMINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_DIAGRAMMING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
