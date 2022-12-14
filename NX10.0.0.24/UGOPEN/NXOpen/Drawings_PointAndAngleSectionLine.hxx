#ifndef NXOpen_DRAWINGS_POINTANDANGLESECTIONLINE_HXX_INCLUDED
#define NXOpen_DRAWINGS_POINTANDANGLESECTIONLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_PointAndAngleSectionLine.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Drawings_SectionLine.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class PointAndAngleSectionLine;
    }
    namespace Drawings
    {
        class SectionLine;
    }
    namespace Drawings
    {
        class _PointAndAngleSectionLineBuilder;
        class PointAndAngleSectionLineImpl;
        /** Point and Angle Section Line lets you create a view with multiple
                segment cuts with no bends. The section line is defined by a
                set of rotation points and angles.  <br> To create or edit an instance of this class, use @link NXOpen::Drawings::SectionLineBuilder  NXOpen::Drawings::SectionLineBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  PointAndAngleSectionLine : public NXOpen::Drawings::SectionLine
        {
            private: PointAndAngleSectionLineImpl * m_pointandanglesectionline_impl;
            private: friend class  _PointAndAngleSectionLineBuilder;
            protected: PointAndAngleSectionLine();
            public: ~PointAndAngleSectionLine();
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
