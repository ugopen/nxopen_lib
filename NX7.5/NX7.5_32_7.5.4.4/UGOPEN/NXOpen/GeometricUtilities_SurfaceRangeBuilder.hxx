#ifndef NXOpen_GEOMETRICUTILITIES_SURFACERANGEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_SURFACERANGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_SurfaceRangeBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/GeometricUtilities_SurfaceRangeBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class SurfaceRangeBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    namespace GeometricUtilities
    {
        class _SurfaceRangeBuilderBuilder;
        class SurfaceRangeBuilderImpl;
        /** Represents the surface range and anchor builder */
        class NXOPENCPPEXPORT  SurfaceRangeBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** Represents the anchor position type */
            public: enum AnchorPositionType
            {
                AnchorPositionTypeCenter/** Anchor at the center of the surface */,
                AnchorPositionTypeVertex1/** Anchor at the first corner of the surface */,
                AnchorPositionTypeVertex2/** Anchor at the second corner of the surface */,
                AnchorPositionTypeVertex3/** Anchor at the third corner of the surface */,
                AnchorPositionTypeVertex4/** Anchor at the fourth corner of the surface */
            };

            private: SurfaceRangeBuilderImpl * m_surfacerangebuilder_impl;
            private: friend class  _SurfaceRangeBuilderBuilder;
            protected: SurfaceRangeBuilder();
            public: ~SurfaceRangeBuilder();
            /**Sets  the anchor position  <br> License requirements : None */
            public: void SetAnchorPosition
            (
                NXOpen::GeometricUtilities::SurfaceRangeBuilder::AnchorPositionType anchorPosition /** anchorposition */ 
            );
            /**Returns  the anchor position  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::SurfaceRangeBuilder::AnchorPositionType AnchorPosition
            (
            );
            /**Returns  the u start  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * UStart
            (
            );
            /**Returns  the u end  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * UEnd
            (
            );
            /**Returns  the v start  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * VStart
            (
            );
            /**Returns  the v end  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * VEnd
            (
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
