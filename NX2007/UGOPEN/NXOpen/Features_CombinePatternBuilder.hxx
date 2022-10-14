#ifndef NXOpen_FEATURES_COMBINEPATTERNBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_COMBINEPATTERNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CombinePatternBuilder.ja
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
#include <NXOpen/GeometricUtilities_PatternDefinition.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class CombinePatternBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class PatternDefinition;
    }
    class SelectBody;
    namespace Features
    {
        class _CombinePatternBuilderBuilder;
        class CombinePatternBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link Features::CombinePattern Features::CombinePattern@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateCombinePatternBuilder  NXOpen::Features::FeatureCollection::CreateCombinePatternBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.XOnPathSpacing.NCopies.Value </term> <description> 
         
        2 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.XOnPathSpacing.SpaceType </term> <description> 
         
        Offset </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.XPathOption </term> <description> 
         
        Offset </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.YDirectionOption </term> <description> 
         
        Section </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.YOnPathSpacing.NCopies.Value </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.YPathOption </term> <description> 
         
        Offset </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.YSpacing.NCopies.Value </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.YSpacing.PitchDistance.Value </term> <description> 
         
        10 (millimeters part), 1 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.YSpacing.SpaceType </term> <description> 
         
        Offset </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.AlongPathDefinition.YSpacing.SpanDistance.Value </term> <description> 
         
        100 (millimeters part), 10 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.AngularSpacing.NCopies.Value </term> <description> 
         
        12 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.AngularSpacing.PitchAngle.Value </term> <description> 
         
        30 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.AngularSpacing.PitchDistance.Value </term> <description> 
         
        10 (millimeters part), 1 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.AngularSpacing.SpaceType </term> <description> 
         
        Offset </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.AngularSpacing.SpanAngle.Value </term> <description> 
         
        360 (millimeters part), 360 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.AngularSpacing.UsePitchOption </term> <description> 
         
        Angle </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.CreateLastStaggered </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.HorizontalRef.RotationAngle.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.IncludeSeedToggle </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.RadialSpacing.NCopies.Value </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.CircularDefinition.StaggerType </term> <description> 
         
        None </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.HelixDefinition.AnglePitch.Value </term> <description> 
         
        30 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.HelixDefinition.CountOfInstances.Value </term> <description> 
         
        6 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.HelixDefinition.DirectionType </term> <description> 
         
        Righthand </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.HelixDefinition.DistancePitch.Value </term> <description> 
         
        10 (millimeters part), 0.4 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.HelixDefinition.HelixPitch.Value </term> <description> 
         
        50 (millimeters part), 2 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.HelixDefinition.HelixSpan.Value </term> <description> 
         
        100 (millimeters part), 4 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.HelixDefinition.NumberOfTurns.Value </term> <description> 
         
        2 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.HelixDefinition.SizeOption </term> <description> 
         
        CountAngleDistance </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternFill.FillMargin.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternFill.FillOptions </term> <description> 
         
        None </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternFill.SimplifiedBoundaryToggle </term> <description> 
         
        False </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.AlongOrientationOption </term> <description> 
         
        NormalToPath </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.CircularOrientationOption </term> <description> 
         
        FollowPattern </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.FollowFaceProjDirOption </term> <description> 
         
        PatternPlaneNormal </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.GeneralOrientationOption </term> <description> 
         
        Fixed </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.HelixOrientationOption </term> <description> 
         
        FollowPattern </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.LinearOrientationOption </term> <description> 
         
        Fixed </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.MirrorOrientationOption </term> <description> 
         
        FollowPattern </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.OrientationOption </term> <description> 
         
        Fixed </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.PolygonOrientationOption </term> <description> 
         
        FollowPattern </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternOrientation.SpiralOrientationOption </term> <description> 
         
        FollowPattern </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PatternType </term> <description> 
         
        Linear </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.NumberOfSides.Value </term> <description> 
         
        6 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.PolygonSizeOption </term> <description> 
         
        Inscribed </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.PolygonSpacing.NCopies.Value </term> <description> 
         
        4 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.PolygonSpacing.PitchDistance.Value </term> <description> 
         
        25 (millimeters part), 1 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.PolygonSpacing.SpaceType </term> <description> 
         
        Offset </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.PolygonSpacing.SpanAngle.Value </term> <description> 
         
        360 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.RadialSpacing.NCopies.Value </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.RadialSpacing.PitchDistance.Value </term> <description> 
         
        25 (millimeters part), 1 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.PolygonDefinition.RadialSpacing.SpanDistance.Value </term> <description> 
         
        100 (millimeters part), 4 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.RectangularDefinition.CreateLastStaggered </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.RectangularDefinition.SimplifiedLayoutType </term> <description> 
         
        Square </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.RectangularDefinition.StaggerType </term> <description> 
         
        None </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.RectangularDefinition.XSpacing.NCopies.Value </term> <description> 
         
        2 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.RectangularDefinition.YSpacing.NCopies.Value </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.SpiralDefinition.DirectionType </term> <description> 
         
        Lefthand </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.SpiralDefinition.NumberOfTurns.Value </term> <description> 
         
        1 (millimeters part), 1 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.SpiralDefinition.RadialPitch.Value </term> <description> 
         
        50 (millimeters part), 2 (inches part) </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.SpiralDefinition.SizeSpiralType </term> <description> 
         
        NumberOfTurns </description> </item> 

        <item><term> 
         
        LinearPatternDefinition.SpiralDefinition.TotalAngle.Value </term> <description> 
         
        360 (millimeters part), 360 (inches part) </description> </item> 

        <item><term> 
         
        PatternType </term> <description> 
         
        LinearAndCircular </description> </item> 

        </list> 

         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  CombinePatternBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** This attribute represents two combined pattern types */
            public: enum PatternTypeEnum
            {
                PatternTypeEnumLinearAndCircular/** linear and circular */ ,
                PatternTypeEnumLinearAndHelix/** linear and helix */ 
            };

            private: CombinePatternBuilderImpl * m_combinepatternbuilder_impl;
            private: friend class  _CombinePatternBuilderBuilder;
            protected: CombinePatternBuilder();
            public: ~CombinePatternBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the select body 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * SelectBody
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the pattern type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::CombinePatternBuilder::PatternTypeEnum PatternType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the pattern type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPatternType
            (
                NXOpen::Features::CombinePatternBuilder::PatternTypeEnum patternType /** patterntype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the pattern definition 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricUtilities::PatternDefinition * PatternDefinition
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the linear pattern definition 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricUtilities::PatternDefinition * LinearPatternDefinition
            (
            );

            /// \endcond 
        };

        /// \endcond 
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