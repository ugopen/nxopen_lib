/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBUFUN_DIE library.


  ==========================================================================*/
#ifndef LIBUFUN_DIE_EXPORTS_HXX_INCLUDED
#define LIBUFUN_DIE_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define UFUN_DIEEXPORT	   __declspec(dllimport)
#		   define UFUN_DIEGLOBAL	   extern __declspec(dllimport)
#		   define UFUN_DIETEMPLATE	 extern
#	   else
#		   define UFUN_DIEEXPORT
#		   define UFUN_DIEGLOBAL	   extern
#		   define UFUN_DIETEMPLATE
#	   endif
#endif  /*  LIBUFUN_DIE_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
