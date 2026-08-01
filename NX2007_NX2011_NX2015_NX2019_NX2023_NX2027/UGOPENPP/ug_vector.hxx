/*
===============================================================================

          Copyright (c) 2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===============================================================================
  File description:

    This header file provides a platform-independent method of including
    the platform-specific header file that defines the STL class "vector".

================================================================================

*/

#ifndef UG_VECTOR_INCLUDED
#define UG_VECTOR_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>

#include <vector>

#if defined(__hpux) && !defined(_HP_NAMESPACE_STD) && !defined(__GNUG__)
#   define std
#endif

#include <libopenpp_exports.hxx>

#if defined ( WIN32 )

//  Because the Loop class has a std::vector < UgEdge * > as a member variable,
//  Windows NT requires that the template std::vector < UgEdge * > be fully
//  instantiated and given a dll interface because the Loop class has
//  a dll interface.  Without the following statement, the following
//  warning will occur:
//
//  warning C4251: 'm_edges' : class 'std::vector < class UgEdge * >' needs to
//                  have dll-interface to be used by clients of class 'Loop'
//    OPENPPTEMPLATE template class OPENPPEXPORT std::vector < class UgEdge * >;

//  Because the UgSpline class has a std::vector < double > as a member constant,
//  Windows NT requires that the template std::vector < double > be fully
//  instantiated and given a dll interface because the UgSpline class has
//  a dll interface.  Without the following statement, the following
//  warning will occur:
//
//  warning C4251: 'NoParameters' : class 'std::vector < double >' needs to
//                  have dll-interface to be used by clients of class 'UgSpline'
//    OPENPPTEMPLATE template class OPENPPEXPORT std::vector < double >;

#endif

#undef EXPORTLIBRARY

#endif  // UG_VECTOR_INCLUDED
