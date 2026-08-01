/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_COPILOT library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_COPILOT_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_COPILOT_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_COPILOTEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_COPILOTGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_COPILOTTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_COPILOTEXPORT
#		   define NXOPENCPP_COPILOTGLOBAL	   extern
#		   define NXOPENCPP_COPILOTTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_COPILOT_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
