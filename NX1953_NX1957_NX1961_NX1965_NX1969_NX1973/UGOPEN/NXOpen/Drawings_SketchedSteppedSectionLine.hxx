#ifndef NXOpen_DRAWINGS_SKETCHEDSTEPPEDSECTIONLINE_HXX_INCLUDED
#define NXOpen_DRAWINGS_SKETCHEDSTEPPEDSECTIONLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SketchedSteppedSectionLine.ja
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
#include <NXOpen/Drawings_BaseSteppedSectionLine.hxx>
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
        class SketchedSteppedSectionLine;
    }
    namespace Drawings
    {
        class BaseSteppedSectionLine;
    }
    namespace Drawings
    {
        class _SketchedSteppedSectionLineBuilder;
        class SketchedSteppedSectionLineImpl;
        /** A Sketched Simple or Stepped Section Line is sketch based section line.

                Sketched Simple Section Line provides one cut to form a view that allows you
                to see the inside of a part. The view is created by dividing the part
                with a single cutting plane.

                Stepped Section Line lets you create a section view which contains
                linear steps. You can make these steps by indicating multiple cuts,
                bends, and arrow segments. All bend and arrow segments are created
                perpendicular to cut segments.  <br> To create or edit an instance of this class, use @link NXOpen::Drawings::SketchSectionLineBuilder  NXOpen::Drawings::SketchSectionLineBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SketchedSteppedSectionLine : public NXOpen::Drawings::BaseSteppedSectionLine
        {
            private: SketchedSteppedSectionLineImpl * m_sketchedsteppedsectionline_impl;
            private: friend class  _SketchedSteppedSectionLineBuilder;
            protected: SketchedSteppedSectionLine();
            public: ~SketchedSteppedSectionLine();
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
