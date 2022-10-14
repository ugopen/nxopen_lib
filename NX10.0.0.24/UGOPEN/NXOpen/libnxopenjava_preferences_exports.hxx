/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_PREFERENCES library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_PREFERENCES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_PREFERENCES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_PREFERENCESEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_PREFERENCESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_PREFERENCESTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_PREFERENCESEXPORT
#		   define NXOPENJAVA_PREFERENCESGLOBAL	   extern
#		   define NXOPENJAVA_PREFERENCESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_PREFERENCES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
