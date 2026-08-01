/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBSTAGEMODELOPENCPP library.


  ==========================================================================*/
#ifndef LIBSTAGEMODELOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBSTAGEMODELOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define STAGEMODELOPENCPPEXPORT	   __declspec(dllimport)
#		   define STAGEMODELOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define STAGEMODELOPENCPPTEMPLATE	 extern
#	   else
#		   define STAGEMODELOPENCPPEXPORT
#		   define STAGEMODELOPENCPPGLOBAL	   extern
#		   define STAGEMODELOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBSTAGEMODELOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
