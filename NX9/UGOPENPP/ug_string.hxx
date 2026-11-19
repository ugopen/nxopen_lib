/*
===============================================================================

           Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

===============================================================================
  File description:

    This header file provides a platform-independent method of including
    the platform-specific header file that defines the STL class "string".

================================================================================

*/

#ifndef UG_STRING_INCLUDED
#define UG_STRING_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>

#include <string>

#if defined(__hpux) && !defined(_HP_NAMESPACE_STD) && !defined(__GNUG__)
#   define std
#endif

#include <libopenpp_exports.hxx>

// ****************************************************************************
// Global functions that return a std::string
// ****************************************************************************
        
// Convert a double value into a string.
OPENPPEXPORT const std::string createString
( 
     double value  // <I>
                   // The double to create a string from
);

#undef EXPORTLIBRARY

#endif  // UG_STRING_INCLUDED
