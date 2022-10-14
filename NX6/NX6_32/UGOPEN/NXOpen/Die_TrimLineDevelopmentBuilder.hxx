#ifndef NXOpen_DIE_TRIMLINEDEVELOPMENTBUILDER_HXX_INCLUDED
#define NXOpen_DIE_TRIMLINEDEVELOPMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_TrimLineDevelopmentBuilder.ja
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
#include <NXOpen/Die_TrimLineDevelopmentBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class TrimLineDevelopmentBuilder;
    }
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    class ScCollector;
    namespace Die
    {
        class _TrimLineDevelopmentBuilderBuilder;
        /**
            Represents a @link Features::TrimLineDevelopment Features::TrimLineDevelopment@endlink  builder
             <br> To create a new instance of this class, use @link Die::DieCollection::CreateTrimLineDevelopmentBuilder Die::DieCollection::CreateTrimLineDevelopmentBuilder@endlink  <br> */
        class NXOPENCPPEXPORT TrimLineDevelopmentBuilder : public Features::FeatureBuilder
        {
            /** Indicates which trim curves to output */
            public: enum OutputMethodName
            {
                OutputMethodNameGeometric/** Geometric curve only */,
                OutputMethodNameCorrected/** Corrected curve only */,
                OutputMethodNameBoth/** Both geometric and corrected curves */
            };

            /** Indicates type of curve smoothing  */
            public: enum SmoothingName
            {
                SmoothingNameLinear/** Linear (no smoothing) */,
                SmoothingNameCubic/** Cubic approximation */,
                SmoothingNameQuintic/** Quintic approximation */
            };

            /** Indicates type of material */
            public: enum MaterialTypeName
            {
                MaterialTypeNameSteel/** Steel */,
                MaterialTypeNameAluminum/** Aluminum */
            };

            private: friend class  _TrimLineDevelopmentBuilderBuilder;
            protected: TrimLineDevelopmentBuilder();
            /**Returns  the collection of formed faces  <br> License requirements : None */
            public: NXOpen::ScCollector * Product
            (
            );
            /**Returns  the forming boundary  <br> License requirements : None */
            public: NXOpen::ScCollector * Boundary
            (
            );
            /**Returns  the collection of addendum faces  <br> License requirements : None */
            public: NXOpen::ScCollector * Addendum
            (
            );
            /**Returns  the point in product region  <br> License requirements : None */
            public: NXOpen::Point * RegionPoint
            (
            );
            /**Sets  the point in product region  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetRegionPoint
            (
                NXOpen::Point * regionPoint /** regionpoint */ 
            );
            /**Returns  the punch direction  <br> License requirements : None */
            public: NXOpen::Direction * PunchDirection
            (
            );
            /**Sets  the punch direction  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetPunchDirection
            (
                NXOpen::Direction * punchDirection /** punchdirection */ 
            );
            /** Creates a default punch vector by finding the least squares plane of the formed faces  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void DefaultPunch
            (
            );
            /**Returns  the spine string, which determines the orientation of the sample planes  <br> License requirements : None */
            public: NXOpen::ScCollector * Spine
            (
            );
            /** Creates a smoothed spine curve from the forming boundary using the spine radius value  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void CreateDefaultSpine
            (
            );
            /**Returns  the spine radius, used by JA_TRIM_LINE_DEVELOPMENT_BUILDER_CreateDefaultSpine  <br> License requirements : None */
            public: double SpineRadius
            (
            );
            /**Sets  the spine radius, used by JA_TRIM_LINE_DEVELOPMENT_BUILDER_CreateDefaultSpine  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSpineRadius
            (
                double spineRadius /** spineradius */ 
            );
            /**Returns  the curve output method - geometric, corrected or both  <br> License requirements : None */
            public: NXOpen::Die::TrimLineDevelopmentBuilder::OutputMethodName OutputMethod
            (
            );
            /**Sets  the curve output method - geometric, corrected or both  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetOutputMethod
            (
                NXOpen::Die::TrimLineDevelopmentBuilder::OutputMethodName outputMethod /** outputmethod */ 
            );
            /**Returns  the curve smoothing method - linear (none), cubic or quintic  <br> License requirements : None */
            public: NXOpen::Die::TrimLineDevelopmentBuilder::SmoothingName Smoothing
            (
            );
            /**Sets  the curve smoothing method - linear (none), cubic or quintic  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSmoothing
            (
                NXOpen::Die::TrimLineDevelopmentBuilder::SmoothingName smoothing /** smoothing */ 
            );
            /**Returns  the sample density index which controls the density of the sample planes.  Value should be between 1 and 9  <br> License requirements : None */
            public: int SampleDensityIndex
            (
            );
            /**Sets  the sample density index which controls the density of the sample planes.  Value should be between 1 and 9  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSampleDensityIndex
            (
                int sampleDensityIndex /** sampledensityindex */ 
            );
            /**Returns  the material type - steel or aluminum  <br> License requirements : None */
            public: NXOpen::Die::TrimLineDevelopmentBuilder::MaterialTypeName MaterialType
            (
            );
            /**Sets  the material type - steel or aluminum  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetMaterialType
            (
                NXOpen::Die::TrimLineDevelopmentBuilder::MaterialTypeName materialType /** materialtype */ 
            );
            /**Returns  the material thickness.  Value should be greater than zero.  <br> License requirements : None */
            public: NXOpen::Expression * Thickness
            (
            );
            /**Returns  the bend allowance formula.  Value should be between 0 and 1  <br> License requirements : None */
            public: NXOpen::Expression * BendAllowance
            (
            );
            /**Returns  the remove loops setting.  True indicates loops should be removed from the output curves  <br> License requirements : None */
            public: bool RemoveLoops
            (
            );
            /**Sets  the remove loops setting.  True indicates loops should be removed from the output curves  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetRemoveLoops
            (
                bool removeLoops /** removeloops */ 
            );
            /**Returns  the associative switch.  True indicates a feature should be output  <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative switch.  True indicates a feature should be output  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the distance tolerance.  Used for sewing sheet bodies and joining curves  <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance.  Used for sewing sheet bodies and joining curves  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetDistanceTolerance
            (
                double distTol /** disttol */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif