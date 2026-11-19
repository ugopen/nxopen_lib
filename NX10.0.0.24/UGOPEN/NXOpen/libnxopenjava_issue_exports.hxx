/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_ISSUE library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_ISSUE_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_ISSUE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_ISSUEEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_ISSUEGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_ISSUETEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_ISSUEEXPORT
#		   define NXOPENJAVA_ISSUEGLOBAL	   extern
#		   define NXOPENJAVA_ISSUETEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_ISSUE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
