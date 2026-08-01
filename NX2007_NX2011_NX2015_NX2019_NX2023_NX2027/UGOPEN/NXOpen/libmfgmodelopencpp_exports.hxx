/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBMFGMODELOPENCPP library.


  ==========================================================================*/
#ifndef LIBMFGMODELOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBMFGMODELOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define MFGMODELOPENCPPEXPORT	   __declspec(dllimport)
#		   define MFGMODELOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define MFGMODELOPENCPPTEMPLATE	 extern
#	   else
#		   define MFGMODELOPENCPPEXPORT
#		   define MFGMODELOPENCPPGLOBAL	   extern
#		   define MFGMODELOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBMFGMODELOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
