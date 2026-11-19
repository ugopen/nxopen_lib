/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBPLASTICDESIGNEROPENCPP library.


  ==========================================================================*/
#ifndef LIBPLASTICDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED
#define LIBPLASTICDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define PLASTICDESIGNEROPENCPPEXPORT	   __declspec(dllimport)
#		   define PLASTICDESIGNEROPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define PLASTICDESIGNEROPENCPPTEMPLATE	 extern
#	   else
#		   define PLASTICDESIGNEROPENCPPEXPORT
#		   define PLASTICDESIGNEROPENCPPGLOBAL	   extern
#		   define PLASTICDESIGNEROPENCPPTEMPLATE
#	   endif
#endif  /*  LIBPLASTICDESIGNEROPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
