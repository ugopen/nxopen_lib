/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBNXOPENDEBUGUICPP library.


  ==========================================================================*/
#ifndef LIBNXOPENDEBUGUICPP_EXPORTS_HXX_INCLUDED
#define LIBNXOPENDEBUGUICPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define NXOPENDEBUGUICPPEXPORT	   __declspec(dllimport)
#		   define NXOPENDEBUGUICPPGLOBAL	   extern __declspec(dllimport)
#		   define NXOPENDEBUGUICPPTEMPLATE	 extern
#	   else
#		   define NXOPENDEBUGUICPPEXPORT
#		   define NXOPENDEBUGUICPPGLOBAL	   extern
#		   define NXOPENDEBUGUICPPTEMPLATE
#	   endif
#endif  /*  LIBNXOPENDEBUGUICPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
