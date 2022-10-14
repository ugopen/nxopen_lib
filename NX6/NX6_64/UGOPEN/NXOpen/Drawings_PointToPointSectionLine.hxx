#ifndef NXOpen_DRAWINGS_POINTTOPOINTSECTIONLINE_HXX_INCLUDED
#define NXOpen_DRAWINGS_POINTTOPOINTSECTIONLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_PointToPointSectionLine.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Drawings_SectionLine.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class PointToPointSectionLine;
    }
    namespace Drawings
    {
        class SectionLine;
    }
    namespace Drawings
    {
        class _PointToPointSectionLineBuilder;
        /** Point to Point Section Line lets you create a view with multiple
                segment cuts with no bends.  The section line is defined by
                a set of rotation points. */
        class NXOPENCPPEXPORT PointToPointSectionLine : public Drawings::SectionLine
        {
            private: friend class  _PointToPointSectionLineBuilder;
            protected: PointToPointSectionLine();
        };
    }
}
#undef EXPORTLIBRARY
#endif