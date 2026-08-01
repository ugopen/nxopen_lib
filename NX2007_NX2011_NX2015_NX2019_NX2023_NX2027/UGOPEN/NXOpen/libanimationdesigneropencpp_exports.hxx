/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBANIMATIONDESIGNEROPENCPP library.


  ==========================================================================*/
#ifndef LIBANIMATIONDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED
#define LIBANIMATIONDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define ANIMATIONDESIGNEROPENCPPEXPORT	   __declspec(dllimport)
#		   define ANIMATIONDESIGNEROPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define ANIMATIONDESIGNEROPENCPPTEMPLATE	 extern
#	   else
#		   define ANIMATIONDESIGNEROPENCPPEXPORT
#		   define ANIMATIONDESIGNEROPENCPPGLOBAL	   extern
#		   define ANIMATIONDESIGNEROPENCPPTEMPLATE
#	   endif
#endif  /*  LIBANIMATIONDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
