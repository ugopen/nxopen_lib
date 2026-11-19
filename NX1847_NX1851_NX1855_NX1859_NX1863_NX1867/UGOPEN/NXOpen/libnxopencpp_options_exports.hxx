/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_OPTIONS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_OPTIONS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_OPTIONS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_OPTIONSEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_OPTIONSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_OPTIONSTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_OPTIONSEXPORT
#		   define NXOPENCPP_OPTIONSGLOBAL	   extern
#		   define NXOPENCPP_OPTIONSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_OPTIONS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
