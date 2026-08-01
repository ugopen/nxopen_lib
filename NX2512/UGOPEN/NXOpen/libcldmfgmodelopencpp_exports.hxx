/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCLDMFGMODELOPENCPP library.


  ==========================================================================*/
#ifndef LIBCLDMFGMODELOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCLDMFGMODELOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define CLDMFGMODELOPENCPPEXPORT	   __declspec(dllimport)
#		   define CLDMFGMODELOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define CLDMFGMODELOPENCPPTEMPLATE	 extern
#	   else
#		   define CLDMFGMODELOPENCPPEXPORT
#		   define CLDMFGMODELOPENCPPGLOBAL	   extern
#		   define CLDMFGMODELOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCLDMFGMODELOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
