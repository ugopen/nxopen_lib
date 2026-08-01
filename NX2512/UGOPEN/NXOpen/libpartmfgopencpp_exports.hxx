/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBPARTMFGOPENCPP library.


  ==========================================================================*/
#ifndef LIBPARTMFGOPENCPP_EXPORTS_HXX_INCLUDED
#define LIBPARTMFGOPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define PARTMFGOPENCPPEXPORT	   __declspec(dllimport)
#		   define PARTMFGOPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define PARTMFGOPENCPPTEMPLATE	 extern
#	   else
#		   define PARTMFGOPENCPPEXPORT
#		   define PARTMFGOPENCPPGLOBAL	   extern
#		   define PARTMFGOPENCPPTEMPLATE
#	   endif
#endif  /*  LIBPARTMFGOPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
