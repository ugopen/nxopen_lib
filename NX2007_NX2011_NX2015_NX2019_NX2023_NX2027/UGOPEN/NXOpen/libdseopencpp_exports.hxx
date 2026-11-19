/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBDSEOPENCPP library.


  ==========================================================================*/
#ifndef LIBDSEOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBDSEOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define DSEOPENCPPEXPORT	   __declspec(dllimport)
#		   define DSEOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define DSEOPENCPPTEMPLATE	 extern
#	   else
#		   define DSEOPENCPPEXPORT
#		   define DSEOPENCPPGLOBAL	   extern
#		   define DSEOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBDSEOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
