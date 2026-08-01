/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_MIGRATIONMANAGER library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_MIGRATIONMANAGER_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_MIGRATIONMANAGER_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_MIGRATIONMANAGEREXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_MIGRATIONMANAGERGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_MIGRATIONMANAGERTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_MIGRATIONMANAGEREXPORT
#		   define NXOPENCPP_MIGRATIONMANAGERGLOBAL	   extern
#		   define NXOPENCPP_MIGRATIONMANAGERTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_MIGRATIONMANAGER_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
