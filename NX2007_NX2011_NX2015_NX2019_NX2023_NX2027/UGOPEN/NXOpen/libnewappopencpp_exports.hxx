/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNEWAPPOPENCPP library.


  ==========================================================================*/
#ifndef LIBNEWAPPOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBNEWAPPOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NEWAPPOPENCPPEXPORT	   __declspec(dllimport)
#		   define NEWAPPOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define NEWAPPOPENCPPTEMPLATE	 extern
#	   else
#		   define NEWAPPOPENCPPEXPORT
#		   define NEWAPPOPENCPPGLOBAL	   extern
#		   define NEWAPPOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBNEWAPPOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
