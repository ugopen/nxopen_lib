/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENPYTHON_UFWRAPTEST library.


  ==========================================================================*/
#ifndef LIBNXOPENPYTHON_UFWRAPTEST_EXPORTS_HXX_INCLUDED
#define LIBNXOPENPYTHON_UFWRAPTEST_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENPYTHON_UFWRAPTESTEXPORT	   __declspec(dllimport)
#		   define NXOPENPYTHON_UFWRAPTESTGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENPYTHON_UFWRAPTESTTEMPLATE	 extern
#	   else
#		   define NXOPENPYTHON_UFWRAPTESTEXPORT
#		   define NXOPENPYTHON_UFWRAPTESTGLOBAL	   extern
#		   define NXOPENPYTHON_UFWRAPTESTTEMPLATE
#	   endif
#endif  /*  LIBNXOPENPYTHON_UFWRAPTEST_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
