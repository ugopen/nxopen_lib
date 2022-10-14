/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENUICPP library.


  ==========================================================================*/
#ifndef LIBNXOPENUICPP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENUICPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENUICPPEXPORT	   __declspec(dllimport)
#		   define NXOPENUICPPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENUICPPTEMPLATE	 extern
#	   else
#		   define NXOPENUICPPEXPORT
#		   define NXOPENUICPPGLOBAL	   extern
#		   define NXOPENUICPPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENUICPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
