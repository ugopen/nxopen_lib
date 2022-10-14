/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_OPTIONS library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_OPTIONS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_OPTIONS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_OPTIONSEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_OPTIONSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_OPTIONSTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_OPTIONSEXPORT
#		   define NXOPENJAVA_OPTIONSGLOBAL	   extern
#		   define NXOPENJAVA_OPTIONSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_OPTIONS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
