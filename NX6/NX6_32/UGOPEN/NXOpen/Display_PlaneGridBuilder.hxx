#ifndef NXOpen_DISPLAY_PLANEGRIDBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_PLANEGRIDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_PlaneGridBuilder.ja
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
#include <NXOpen/Display_BoundedGridBuilder.hxx>
#include <NXOpen/Display_PlaneGridBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class PlaneGridBuilder;
    }
    namespace Display
    {
        class BoundedGridBuilder;
    }
    class Plane;
    namespace Display
    {
        class _PlaneGridBuilderBuilder;
        /** Represents the builder for adding a bounded grid @link Display::PlaneGrid Display::PlaneGrid@endlink  
                to a plane.
             <br> To create a new instance of this class, use @link Display::GridCollection::CreatePlaneGridBuilder Display::GridCollection::CreatePlaneGridBuilder@endlink  <br> 
        Default values:
        Associative: 1
        LabelReference: Local
        MajorLineSpacing: 100 (millimeters part), 1 (inches part)
        MajorLineStyle: Solid
        MajorLineWeight: Normal
        MinorLineStyle: Dashed
        MinorLineWeight: Thin
        MinorLinesPerMajor: 1
        Show: 1
        ShowLabel: Always
        ShowMajorLines: 1
        ShowOnTop: 0
        SnapPointsPerMinor: 1
        SnapToGrid: 0
        */
        class NXOPENCPPEXPORT PlaneGridBuilder : public Display::BoundedGridBuilder
        {
            private: friend class  _PlaneGridBuilderBuilder;
            protected: PlaneGridBuilder();
            /**Returns  the plane  <br> License requirements : None */
            public: NXOpen::Plane * Plane
            (
            );
            /**Sets  the plane  <br> License requirements : None */
            public: void SetPlane
            (
                NXOpen::Plane * plane /** plane */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
