/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENJAVA_BODYDES library.


  ==========================================================================*/
#ifndef LIBNXOPENJAVA_BODYDES_EXPORTS_HXX_INCLUDED
#define LIBNXOPENJAVA_BODYDES_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENJAVA_BODYDESEXPORT	   __declspec(dllimport)
#		   define NXOPENJAVA_BODYDESGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENJAVA_BODYDESTEMPLATE	 extern
#	   else
#		   define NXOPENJAVA_BODYDESEXPORT
#		   define NXOPENJAVA_BODYDESGLOBAL	   extern
#		   define NXOPENJAVA_BODYDESTEMPLATE
#	   endif
#endif  /*  LIBNXOPENJAVA_BODYDES_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
