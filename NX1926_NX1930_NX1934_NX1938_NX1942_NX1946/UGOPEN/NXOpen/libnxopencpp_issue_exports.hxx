/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_ISSUE library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_ISSUE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_ISSUE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_ISSUEEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_ISSUEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_ISSUETEMPLATE	 extern
#	   else
#		   define NXOPENCPP_ISSUEEXPORT
#		   define NXOPENCPP_ISSUEGLOBAL	   extern
#		   define NXOPENCPP_ISSUETEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_ISSUE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
