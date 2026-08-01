/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBAUTOMATIONEXAMPLE library.


  ==========================================================================*/
#ifndef LIBAUTOMATIONEXAMPLE_EXPORTS_HXX_INCLUDED
#define LIBAUTOMATIONEXAMPLE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define AUTOMATIONEXAMPLEEXPORT	   __declspec(dllimport)
#		   define AUTOMATIONEXAMPLEGLOBAL	   extern __declspec(dllimport)
#		   define AUTOMATIONEXAMPLETEMPLATE	 extern
#	   else
#		   define AUTOMATIONEXAMPLEEXPORT
#		   define AUTOMATIONEXAMPLEGLOBAL	   extern
#		   define AUTOMATIONEXAMPLETEMPLATE
#	   endif
#endif  /*  LIBAUTOMATIONEXAMPLE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
