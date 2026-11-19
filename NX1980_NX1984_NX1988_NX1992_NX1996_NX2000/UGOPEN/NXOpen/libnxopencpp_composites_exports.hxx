/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_COMPOSITES library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_COMPOSITES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_COMPOSITES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_COMPOSITESEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_COMPOSITESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_COMPOSITESTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_COMPOSITESEXPORT
#		   define NXOPENCPP_COMPOSITESGLOBAL	   extern
#		   define NXOPENCPP_COMPOSITESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_COMPOSITES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
