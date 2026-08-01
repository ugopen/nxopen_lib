/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_COLLABORATIONAPPLICATION library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_COLLABORATIONAPPLICATION_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_COLLABORATIONAPPLICATION_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_COLLABORATIONAPPLICATIONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_COLLABORATIONAPPLICATIONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_COLLABORATIONAPPLICATIONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_COLLABORATIONAPPLICATIONEXPORT
#		   define NXOPENCPP_COLLABORATIONAPPLICATIONGLOBAL	   extern
#		   define NXOPENCPP_COLLABORATIONAPPLICATIONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_COLLABORATIONAPPLICATION_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
