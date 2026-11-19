/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBLINEDESIGNEROPENCPP library.


  ==========================================================================*/
#ifndef LIBLINEDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED
#define LIBLINEDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define LINEDESIGNEROPENCPPEXPORT	   __declspec(dllimport)
#		   define LINEDESIGNEROPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define LINEDESIGNEROPENCPPTEMPLATE	 extern
#	   else
#		   define LINEDESIGNEROPENCPPEXPORT
#		   define LINEDESIGNEROPENCPPGLOBAL	   extern
#		   define LINEDESIGNEROPENCPPTEMPLATE
#	   endif
#endif  /*  LIBLINEDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
