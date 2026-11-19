/*=============================================================================

   Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
						All rights reserved

===============================================================================
File Description:

Header file that defines the export symbols for the LIBDESIGNSPACEEXPLOREROPENCPP library.


  ==========================================================================*/
#ifndef LIBDESIGNSPACEEXPLOREROPENCPP_EXPORTS_HXX_INCLUDED
#define LIBDESIGNSPACEEXPLOREROPENCPP_EXPORTS_HXX_INCLUDED
#	   if defined(_WIN32) && !defined(WNT_STATIC_LINK)
#		   define DESIGNSPACEEXPLOREROPENCPPEXPORT	   __declspec(dllimport)
#		   define DESIGNSPACEEXPLOREROPENCPPGLOBAL	   extern __declspec(dllimport)
#		   define DESIGNSPACEEXPLOREROPENCPPTEMPLATE	 extern
#	   else
#		   define DESIGNSPACEEXPLOREROPENCPPEXPORT
#		   define DESIGNSPACEEXPLOREROPENCPPGLOBAL	   extern
#		   define DESIGNSPACEEXPLOREROPENCPPTEMPLATE
#	   endif
#endif  /*  LIBDESIGNSPACEEXPLOREROPENCPP_EXPORTS_HXX_INCLUDED  */
/*==========================================================================
  ==========================================================================*/
/*  */
