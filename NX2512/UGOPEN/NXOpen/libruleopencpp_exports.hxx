/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBRULEOPENCPP library.


  ==========================================================================*/
#ifndef LIBRULEOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBRULEOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define RULEOPENCPPEXPORT	   __declspec(dllimport)
#		   define RULEOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define RULEOPENCPPTEMPLATE	 extern
#	   else
#		   define RULEOPENCPPEXPORT
#		   define RULEOPENCPPGLOBAL	   extern
#		   define RULEOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBRULEOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
