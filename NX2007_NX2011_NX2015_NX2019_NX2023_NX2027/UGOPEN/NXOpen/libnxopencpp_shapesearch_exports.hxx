/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_SHAPESEARCH library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_SHAPESEARCH_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_SHAPESEARCH_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_SHAPESEARCHEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_SHAPESEARCHGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_SHAPESEARCHTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_SHAPESEARCHEXPORT
#		   define NXOPENCPP_SHAPESEARCHGLOBAL	   extern
#		   define NXOPENCPP_SHAPESEARCHTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_SHAPESEARCH_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
