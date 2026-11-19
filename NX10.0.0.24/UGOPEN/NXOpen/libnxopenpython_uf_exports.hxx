/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENPYTHON_UF library.


  ==========================================================================*/
#ifndef LIBNXOPENPYTHON_UF_EXPORTS_HXX_INCLUDED
#define LIBNXOPENPYTHON_UF_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENPYTHON_UFEXPORT	   __declspec(dllimport)
#		   define NXOPENPYTHON_UFGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENPYTHON_UFTEMPLATE	 extern
#	   else
#		   define NXOPENPYTHON_UFEXPORT
#		   define NXOPENPYTHON_UFGLOBAL	   extern
#		   define NXOPENPYTHON_UFTEMPLATE
#	   endif
#endif  /*  LIBNXOPENPYTHON_UF_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
