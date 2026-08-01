/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBDSEDESIGNWORKFLOWOPENCPP library.


  ==========================================================================*/
#ifndef LIBDSEDESIGNWORKFLOWOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBDSEDESIGNWORKFLOWOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define DSEDESIGNWORKFLOWOPENCPPEXPORT	   __declspec(dllimport)
#		   define DSEDESIGNWORKFLOWOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define DSEDESIGNWORKFLOWOPENCPPTEMPLATE	 extern
#	   else
#		   define DSEDESIGNWORKFLOWOPENCPPEXPORT
#		   define DSEDESIGNWORKFLOWOPENCPPGLOBAL	   extern
#		   define DSEDESIGNWORKFLOWOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBDSEDESIGNWORKFLOWOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
