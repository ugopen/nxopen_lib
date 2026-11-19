/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENCPP_REGIONRECOGNITION library.


  ==========================================================================*/
#ifndef LIBNXOPENCPP_REGIONRECOGNITION_EXPORTS_HXX_INCLUDED
#define LIBNXOPENCPP_REGIONRECOGNITION_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENCPP_REGIONRECOGNITIONEXPORT	   __declspec(dllimport)
#		   define NXOPENCPP_REGIONRECOGNITIONGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENCPP_REGIONRECOGNITIONTEMPLATE	 extern
#	   else
#		   define NXOPENCPP_REGIONRECOGNITIONEXPORT
#		   define NXOPENCPP_REGIONRECOGNITIONGLOBAL	   extern
#		   define NXOPENCPP_REGIONRECOGNITIONTEMPLATE
#	   endif
#endif  /*  LIBNXOPENCPP_REGIONRECOGNITION_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
