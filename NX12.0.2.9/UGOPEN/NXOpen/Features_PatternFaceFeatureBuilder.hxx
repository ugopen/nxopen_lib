#ifndef NXOpen_FEATURES_PATTERNFACEFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_PATTERNFACEFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PatternFaceFeatureBuilder.ja
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
#include <NXOpen/GeometricUtilities_PatternReferencePointServiceBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
        class PatternFaceFeatureBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class PatternDefinition;
    }
    namespace GeometricUtilities
    {
        class PatternReferencePointServiceBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _PatternFaceFeatureBuilderBuilder;
        class PatternFaceFeatureBuilderImpl;
        /**
            Represents a builder for a pattern face feature, post NX9.
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreatePatternFaceFeatureBuilder  NXOpen::Features::FeatureCollection::CreatePatternFaceFeatureBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        CopyChamferLabels </td> <td> 
         
        false </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.XOnPathSpacing.NCopies.Value </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.XOnPathSpacing.SpaceType </td> <td> 
         
        Offset </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.XPathOption </td> <td> 
         
        Offset </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.YDirectionOption </td> <td> 
         
        Section </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.YOnPathSpacing.NCopies.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.YPathOption </td> <td> 
         
        Offset </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.YSpacing.NCopies.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.YSpacing.PitchDistance.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.YSpacing.SpaceType </td> <td> 
         
        Offset </td> </tr> 

        <tr><td> 
         
        PatternDefinition.AlongPathDefinition.YSpacing.SpanDistance.Value </td> <td> 
         
        100 (millimeters part), 10 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.AngularSpacing.NCopies.Value </td> <td> 
         
        12 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.AngularSpacing.PitchAngle.Value </td> <td> 
         
        30 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.AngularSpacing.PitchDistance.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.AngularSpacing.SpaceType </td> <td> 
         
        Offset </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.AngularSpacing.SpanAngle.Value </td> <td> 
         
        360 (millimeters part), 360 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.AngularSpacing.UsePitchOption </td> <td> 
         
        Angle </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.CreateLastStaggered </td> <td> 
         
        true </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.HorizontalRef.RotationAngle.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.IncludeSeedToggle </td> <td> 
         
        true </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.RadialSpacing.NCopies.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.CircularDefinition.StaggerType </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        PatternDefinition.HelixDefinition.AnglePitch.Value </td> <td> 
         
        30 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.HelixDefinition.CountOfInstances.Value </td> <td> 
         
        6 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.HelixDefinition.DirectionType </td> <td> 
         
        Righthand </td> </tr> 

        <tr><td> 
         
        PatternDefinition.HelixDefinition.DistancePitch.Value </td> <td> 
         
        10 (millimeters part), 0.4 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.HelixDefinition.HelixPitch.Value </td> <td> 
         
        50 (millimeters part), 2 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.HelixDefinition.HelixSpan.Value </td> <td> 
         
        100 (millimeters part), 4 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.HelixDefinition.NumberOfTurns.Value </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.HelixDefinition.SizeOption </td> <td> 
         
        CountAngleDistance </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternFill.FillMargin.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternFill.FillOptions </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternFill.SimplifiedBoundaryToggle </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.AlongOrientationOption </td> <td> 
         
        NormalToPath </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.CircularOrientationOption </td> <td> 
         
        FollowPattern </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.FollowFaceProjDirOption </td> <td> 
         
        PatternPlaneNormal </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.GeneralOrientationOption </td> <td> 
         
        Fixed </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.HelixOrientationOption </td> <td> 
         
        FollowPattern </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.LinearOrientationOption </td> <td> 
         
        Fixed </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.MirrorOrientationOption </td> <td> 
         
        FollowPattern </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.OrientationOption </td> <td> 
         
        Fixed </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.PolygonOrientationOption </td> <td> 
         
        FollowPattern </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternOrientation.SpiralOrientationOption </td> <td> 
         
        FollowPattern </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PatternType </td> <td> 
         
        Linear </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.NumberOfSides.Value </td> <td> 
         
        6 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.PolygonSizeOption </td> <td> 
         
        Inscribed </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.PolygonSpacing.NCopies.Value </td> <td> 
         
        4 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.PolygonSpacing.PitchDistance.Value </td> <td> 
         
        25 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.PolygonSpacing.SpaceType </td> <td> 
         
        Offset </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.PolygonSpacing.SpanAngle.Value </td> <td> 
         
        360 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.RadialSpacing.NCopies.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.RadialSpacing.PitchDistance.Value </td> <td> 
         
        25 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.PolygonDefinition.RadialSpacing.SpanDistance.Value </td> <td> 
         
        100 (millimeters part), 4 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.RectangularDefinition.CreateLastStaggered </td> <td> 
         
        true </td> </tr> 

        <tr><td> 
         
        PatternDefinition.RectangularDefinition.SimplifiedLayoutType </td> <td> 
         
        Square </td> </tr> 

        <tr><td> 
         
        PatternDefinition.RectangularDefinition.StaggerType </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        PatternDefinition.RectangularDefinition.XSpacing.NCopies.Value </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.RectangularDefinition.YSpacing.NCopies.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        PatternDefinition.SpiralDefinition.DirectionType </td> <td> 
         
        Lefthand </td> </tr> 

        <tr><td> 
         
        PatternDefinition.SpiralDefinition.NumberOfTurns.Value </td> <td> 
         
        1 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.SpiralDefinition.RadialPitch.Value </td> <td> 
         
        50 (millimeters part), 2 (inches part) </td> </tr> 

        <tr><td> 
         
        PatternDefinition.SpiralDefinition.SizeSpiralType </td> <td> 
         
        NumberOfTurns </td> </tr> 

        <tr><td> 
         
        PatternDefinition.SpiralDefinition.TotalAngle.Value </td> <td> 
         
        360 (millimeters part), 360 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  PatternFaceFeatureBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: PatternFaceFeatureBuilderImpl * m_patternfacefeaturebuilder_impl;
            private: friend class  _PatternFaceFeatureBuilderBuilder;
            protected: PatternFaceFeatureBuilder();
            public: ~PatternFaceFeatureBuilder();
            /**Returns  the face collector. 
                        Collects the input faces to pattern 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * FaceCollector
            (
            );
            /**Returns  the reference point service.
                        This contains the origin for creating pattern based transformations 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PatternReferencePointServiceBuilder * ReferencePoint
            (
            );
            /**Returns  the pattern definition service.
                        This is the object that determines the type of pattern
                        and holds the associated data that comes with it. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PatternDefinition * PatternDefinition
            (
            );
            /**Returns  the chamfer label options .
                        'true' if the chamfer faces should be labeled automatically
                        'false' if the chamfer faces should not be labeled automatically 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool CopyChamferLabels
            (
            );
            /**Sets  the chamfer label options .
                        'true' if the chamfer faces should be labeled automatically
                        'false' if the chamfer faces should not be labeled automatically 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCopyChamferLabels
            (
                bool shouldLabelChamfer /** shouldlabelchamfer */ 
            );
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
