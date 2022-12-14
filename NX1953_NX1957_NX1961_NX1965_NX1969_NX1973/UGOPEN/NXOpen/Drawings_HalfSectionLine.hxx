#ifndef NXOpen_DRAWINGS_HALFSECTIONLINE_HXX_INCLUDED
#define NXOpen_DRAWINGS_HALFSECTIONLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_HalfSectionLine.ja
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
#include <NXOpen/Drawings_BaseHalfSectionLine.hxx>
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
        class HalfSectionLine;
    }
    namespace Drawings
    {
        class BaseHalfSectionLine;
    }
    namespace Drawings
    {
        class _HalfSectionLineBuilder;
        class HalfSectionLineImpl;
        /** Half Section Line is used to create a view with half of the part
                sectioned and the other half un-sectioned. Half sections are similar
                to simple and stepped sections in that the cut segment is parallel
                to the defined hinge line. Note that the Half Section Line contains
                only one arrow, one bend, and one cut segment.  <br> To create or edit an instance of this class, use @link NXOpen::Drawings::SectionViewBuilder  NXOpen::Drawings::SectionViewBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  HalfSectionLine : public NXOpen::Drawings::BaseHalfSectionLine
        {
            private: HalfSectionLineImpl * m_halfsectionline_impl;
            private: friend class  _HalfSectionLineBuilder;
            protected: HalfSectionLine();
            public: ~HalfSectionLine();
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
