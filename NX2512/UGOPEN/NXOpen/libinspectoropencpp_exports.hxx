/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBINSPECTOROPENCPP library.


  ==========================================================================*/
#ifndef LIBINSPECTOROPENCPP_EXPORTS_HXX_INCLUDED
#define LIBINSPECTOROPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define INSPECTOROPENCPPEXPORT	   __declspec(dllimport)
#		   define INSPECTOROPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define INSPECTOROPENCPPTEMPLATE	 extern
#	   else
#		   define INSPECTOROPENCPPEXPORT
#		   define INSPECTOROPENCPPGLOBAL	   extern
#		   define INSPECTOROPENCPPTEMPLATE
#	   endif
#endif  /*  LIBINSPECTOROPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
