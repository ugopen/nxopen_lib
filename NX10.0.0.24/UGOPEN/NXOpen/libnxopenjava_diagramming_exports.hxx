/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_DIAGRAMMING library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_DIAGRAMMING_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_DIAGRAMMING_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_DIAGRAMMINGEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_DIAGRAMMINGGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_DIAGRAMMINGTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_DIAGRAMMINGEXPORT
#		   define NXOPENJAVA_DIAGRAMMINGGLOBAL	   extern
#		   define NXOPENJAVA_DIAGRAMMINGTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_DIAGRAMMING_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
