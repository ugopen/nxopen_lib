/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBTOOLDESIGNEROPENCPP library.


  ==========================================================================*/
#ifndef LIBTOOLDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED
#define LIBTOOLDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define TOOLDESIGNEROPENCPPEXPORT	   __declspec(dllimport)
#		   define TOOLDESIGNEROPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define TOOLDESIGNEROPENCPPTEMPLATE	 extern
#	   else
#		   define TOOLDESIGNEROPENCPPEXPORT
#		   define TOOLDESIGNEROPENCPPGLOBAL	   extern
#		   define TOOLDESIGNEROPENCPPTEMPLATE
#	   endif
#endif  /*  LIBTOOLDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
