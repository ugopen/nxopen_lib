/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_USERDEFINEDOBJECTS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_USERDEFINEDOBJECTS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_USERDEFINEDOBJECTS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_USERDEFINEDOBJECTSEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_USERDEFINEDOBJECTSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_USERDEFINEDOBJECTSTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_USERDEFINEDOBJECTSEXPORT
#		   define NXOPENCPP_USERDEFINEDOBJECTSGLOBAL	   extern
#		   define NXOPENCPP_USERDEFINEDOBJECTSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_USERDEFINEDOBJECTS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
