/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_FIELDS library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_FIELDS_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_FIELDS_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_FIELDSEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_FIELDSGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_FIELDSTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_FIELDSEXPORT
#		   define NXOPENJAVA_FIELDSGLOBAL	   extern
#		   define NXOPENJAVA_FIELDSTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_FIELDS_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
