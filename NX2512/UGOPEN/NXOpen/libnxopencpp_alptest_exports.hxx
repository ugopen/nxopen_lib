/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_ALPTEST library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_ALPTEST_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_ALPTEST_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_ALPTESTEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_ALPTESTGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_ALPTESTTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_ALPTESTEXPORT
#		   define NXOPENCPP_ALPTESTGLOBAL	   extern
#		   define NXOPENCPP_ALPTESTTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_ALPTEST_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
