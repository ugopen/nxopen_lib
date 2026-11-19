/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_PREFERENCES library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_PREFERENCES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_PREFERENCES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_PREFERENCESEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_PREFERENCESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_PREFERENCESTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_PREFERENCESEXPORT
#		   define NXOPENCPP_PREFERENCESGLOBAL	   extern
#		   define NXOPENCPP_PREFERENCESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_PREFERENCES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
