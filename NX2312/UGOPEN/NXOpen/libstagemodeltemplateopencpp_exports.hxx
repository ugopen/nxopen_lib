/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBSTAGEMODELTEMPLATEOPENCPP library.


  ==========================================================================*/
#ifndef LIBSTAGEMODELTEMPLATEOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBSTAGEMODELTEMPLATEOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define STAGEMODELTEMPLATEOPENCPPEXPORT	   __declspec(dllimport)
#		   define STAGEMODELTEMPLATEOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define STAGEMODELTEMPLATEOPENCPPTEMPLATE	 extern
#	   else
#		   define STAGEMODELTEMPLATEOPENCPPEXPORT
#		   define STAGEMODELTEMPLATEOPENCPPGLOBAL	   extern
#		   define STAGEMODELTEMPLATEOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBSTAGEMODELTEMPLATEOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
