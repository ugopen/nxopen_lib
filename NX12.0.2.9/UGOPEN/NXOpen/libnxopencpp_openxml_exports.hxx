/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_OPENXML library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_OPENXML_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_OPENXML_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_OPENXMLEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_OPENXMLGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_OPENXMLTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_OPENXMLEXPORT
#		   define NXOPENCPP_OPENXMLGLOBAL	   extern
#		   define NXOPENCPP_OPENXMLTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_OPENXML_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
