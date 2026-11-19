/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_FIELDS library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_FIELDS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_FIELDS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_FIELDSEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_FIELDSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_FIELDSTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_FIELDSEXPORT
#		   define NXOPENCPP_FIELDSGLOBAL	   extern
#		   define NXOPENCPP_FIELDSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_FIELDS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
