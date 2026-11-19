/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_USERDEFINEDOBJECTS library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_USERDEFINEDOBJECTS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_USERDEFINEDOBJECTS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_USERDEFINEDOBJECTSEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_USERDEFINEDOBJECTSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_USERDEFINEDOBJECTSTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_USERDEFINEDOBJECTSEXPORT
#		   define NXOPENJAVA_USERDEFINEDOBJECTSGLOBAL	   extern
#		   define NXOPENJAVA_USERDEFINEDOBJECTSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_USERDEFINEDOBJECTS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
