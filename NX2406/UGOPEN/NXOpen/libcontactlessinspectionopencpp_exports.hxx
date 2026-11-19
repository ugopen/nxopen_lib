/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBCONTACTLESSINSPECTIONOPENCPP library.


  ==========================================================================*/
#ifndef LIBCONTACTLESSINSPECTIONOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBCONTACTLESSINSPECTIONOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define CONTACTLESSINSPECTIONOPENCPPEXPORT	   __declspec(dllimport)
#		   define CONTACTLESSINSPECTIONOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define CONTACTLESSINSPECTIONOPENCPPTEMPLATE	 extern
#	   else
#		   define CONTACTLESSINSPECTIONOPENCPPEXPORT
#		   define CONTACTLESSINSPECTIONOPENCPPGLOBAL	   extern
#		   define CONTACTLESSINSPECTIONOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBCONTACTLESSINSPECTIONOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
