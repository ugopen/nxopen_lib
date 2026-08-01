/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_ATSCPPUNIT library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_ATSCPPUNIT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_ATSCPPUNIT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_ATSCPPUNITEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_ATSCPPUNITGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_ATSCPPUNITTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_ATSCPPUNITEXPORT
#		   define NXOPENCPP_ATSCPPUNITGLOBAL	   extern
#		   define NXOPENCPP_ATSCPPUNITTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_ATSCPPUNIT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
