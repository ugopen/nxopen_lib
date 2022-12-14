#ifndef NXOpen_FEATURES_RIBBONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_RIBBONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_RibbonBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_RibbonBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class RibbonBuilder;
    }
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Section;
    namespace Features
    {
        class _RibbonBuilderBuilder;
        /**
            Represents a @link Features::Ribbon Features::Ribbon@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateRibbonBuilder Features::FeatureCollection::CreateRibbonBuilder@endlink  <br> 
        Default values:
        Angle.RightHandSide: 0
        AngleTolerance: 0.5
        DistanceTolerance: 0.0254 (millimeters part), 0.01 (inches part)
        OffsetDistance.RightHandSide: 1 (millimeters part), 0.04 (inches part)
        */
        class NXOPENCPPEXPORT RibbonBuilder : public Features::FeatureBuilder
        {
            private: friend class  _RibbonBuilderBuilder;
            protected: RibbonBuilder();
            /**Returns  the profile to offset  <br> License requirements : None */
            public: NXOpen::Section * Profile
            (
            );
            /**Returns  the direction normal to the offset  <br> License requirements : None */
            public: NXOpen::Direction * OffsetView
            (
            );
            /**Sets  the direction normal to the offset  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOffsetView
            (
                NXOpen::Direction * offsetView /** offsetview */ 
            );
            /**Returns  the distance to offset the profile  <br> License requirements : None */
            public: NXOpen::Expression * OffsetDistance
            (
            );
            /**Returns  the flag indicating that the offset direction should be reversed  <br> License requirements : None */
            public: bool ReverseOffset
            (
            );
            /**Sets  the flag indicating that the offset direction should be reversed  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReverseOffset
            (
                bool reverseOffset /** reverseoffset */ 
            );
            /**Returns  the angle to offset measured from the offset view  <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns  the distance tolerance  <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  the angle tolerance  <br> License requirements : None */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angletolerance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
