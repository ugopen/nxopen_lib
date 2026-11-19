/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUFUN_RULE_NXOPEN library.


  ==========================================================================*/
#ifndef LIBUFUN_RULE_NXOPEN_EXPORTS_HXX_INCLUDED
#define LIBUFUN_RULE_NXOPEN_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UFUN_RULE_NXOPENEXPORT	   __declspec(dllimport)
#		   define UFUN_RULE_NXOPENGLOBAL	   extern __declspec(dllimport)
#		   define UFUN_RULE_NXOPENTEMPLATE	 extern
#	   else
#		   define UFUN_RULE_NXOPENEXPORT
#		   define UFUN_RULE_NXOPENGLOBAL	   extern
#		   define UFUN_RULE_NXOPENTEMPLATE
#	   endif
#endif  /*  LIBUFUN_RULE_NXOPEN_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
