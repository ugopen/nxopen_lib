/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBMFGVIEWMAKEROPENCPP library.


  ==========================================================================*/
#ifndef LIBMFGVIEWMAKEROPENCPP_EXPORTS_HXX_INCLUDED
#define LIBMFGVIEWMAKEROPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define MFGVIEWMAKEROPENCPPEXPORT	   __declspec(dllimport)
#		   define MFGVIEWMAKEROPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define MFGVIEWMAKEROPENCPPTEMPLATE	 extern
#	   else
#		   define MFGVIEWMAKEROPENCPPEXPORT
#		   define MFGVIEWMAKEROPENCPPGLOBAL	   extern
#		   define MFGVIEWMAKEROPENCPPTEMPLATE
#	   endif
#endif  /*  LIBMFGVIEWMAKEROPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
