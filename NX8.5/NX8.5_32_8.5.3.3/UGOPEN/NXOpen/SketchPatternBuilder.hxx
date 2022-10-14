#ifndef NXOpen_SKETCHPATTERNBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHPATTERNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchPatternBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/GeometricUtilities_PatternDefinition.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SketchPatternBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchPatternBuilder;
    class Builder;
    namespace GeometricUtilities
    {
        class PatternDefinition;
    }
    class NXObject;
    class Section;
    class _SketchPatternBuilderBuilder;
    class SketchPatternBuilderImpl;
    /**
        Represents a @link SketchPatternBuilder SketchPatternBuilder@endlink 
         <br> To create a new instance of this class, use @link SketchCollection::CreateSketchPatternBuilder  SketchCollection::CreateSketchPatternBuilder @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    CreateSpacingExp </td> <td> 
     
    True </td> </tr> 

    <tr><td> 
     
    LockOrientation </td> <td> 
     
    True </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.XOnPathSpacing.NCopies.Value </td> <td> 
     
    2 </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.XOnPathSpacing.SpaceType </td> <td> 
     
    Offset </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.XPathOption </td> <td> 
     
    Offset </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.YDirectionOption </td> <td> 
     
    Section </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.YOnPathSpacing.NCopies.Value </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.YPathOption </td> <td> 
     
    Offset </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.YSpacing.NCopies.Value </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.YSpacing.PitchDistance.Value </td> <td> 
     
    10 (millimeters part), 1 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.YSpacing.SpaceType </td> <td> 
     
    Offset </td> </tr> 

    <tr><td> 
     
    PatternService.AlongPathDefinition.YSpacing.SpanDistance.Value </td> <td> 
     
    100 (millimeters part), 10 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.AngularSpacing.NCopies.Value </td> <td> 
     
    12 </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.AngularSpacing.PitchAngle.Value </td> <td> 
     
    30 </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.AngularSpacing.PitchDistance.Value </td> <td> 
     
    10 (millimeters part), 1 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.AngularSpacing.SpaceType </td> <td> 
     
    Offset </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.AngularSpacing.SpanAngle.Value </td> <td> 
     
    360 (millimeters part), 360 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.AngularSpacing.UsePitchOption </td> <td> 
     
    Angle </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.CreateLastStaggered </td> <td> 
     
    true </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.HorizontalRef.RotationAngle.Value </td> <td> 
     
    0 (millimeters part), 0 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.IncludeSeedToggle </td> <td> 
     
    true </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.RadialSpacing.NCopies.Value </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    PatternService.CircularDefinition.StaggerType </td> <td> 
     
    None </td> </tr> 

    <tr><td> 
     
    PatternService.PatternFill.FillMargin.Value </td> <td> 
     
    0 (millimeters part), 0 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.PatternFill.FillOptions </td> <td> 
     
    None </td> </tr> 

    <tr><td> 
     
    PatternService.PatternFill.SimplifiedBoundaryToggle </td> <td> 
     
    False </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.AlongOrientationOption </td> <td> 
     
    NormalToPath </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.CircularOrientationOption </td> <td> 
     
    FollowPattern </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.FollowFaceProjDirOption </td> <td> 
     
    PatternPlaneNormal </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.GeneralOrientationOption </td> <td> 
     
    Fixed </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.LinearOrientationOption </td> <td> 
     
    Fixed </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.MirrorOrientationOption </td> <td> 
     
    FollowPattern </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.OrientationOption (deprecated) </td> <td> 
     
    Fixed </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.PolygonOrientationOption </td> <td> 
     
    FollowPattern </td> </tr> 

    <tr><td> 
     
    PatternService.PatternOrientation.SpiralOrientationOption </td> <td> 
     
    FollowPattern </td> </tr> 

    <tr><td> 
     
    PatternService.PatternType </td> <td> 
     
    Linear </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.NumberOfSides.Value </td> <td> 
     
    6 </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.PolygonSizeOption </td> <td> 
     
    Inscribed </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.PolygonSpacing.NCopies.Value </td> <td> 
     
    4 </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.PolygonSpacing.PitchDistance.Value </td> <td> 
     
    25 (millimeters part), 1 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.PolygonSpacing.SpaceType </td> <td> 
     
    Offset </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.PolygonSpacing.SpanAngle.Value </td> <td> 
     
    360 </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.RadialSpacing.NCopies.Value </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.RadialSpacing.PitchDistance.Value </td> <td> 
     
    25 (millimeters part), 1 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.PolygonDefinition.RadialSpacing.SpanDistance.Value </td> <td> 
     
    100 (millimeters part), 4 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.RectangularDefinition.CreateLastStaggered </td> <td> 
     
    true </td> </tr> 

    <tr><td> 
     
    PatternService.RectangularDefinition.SimplifiedLayoutType </td> <td> 
     
    Square </td> </tr> 

    <tr><td> 
     
    PatternService.RectangularDefinition.StaggerType </td> <td> 
     
    None </td> </tr> 

    <tr><td> 
     
    PatternService.RectangularDefinition.XSpacing.NCopies.Value </td> <td> 
     
    2 </td> </tr> 

    <tr><td> 
     
    PatternService.RectangularDefinition.YSpacing.NCopies.Value </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    PatternService.SpiralDefinition.DirectionType </td> <td> 
     
    Lefthand </td> </tr> 

    <tr><td> 
     
    PatternService.SpiralDefinition.NumberOfTurns.Value </td> <td> 
     
    1 (millimeters part), 1 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.SpiralDefinition.RadialPitch.Value </td> <td> 
     
    50 (millimeters part), 2 (inches part) </td> </tr> 

    <tr><td> 
     
    PatternService.SpiralDefinition.SizeSpiralType </td> <td> 
     
    NumberOfTurns </td> </tr> 

    <tr><td> 
     
    PatternService.SpiralDefinition.TotalAngle.Value </td> <td> 
     
    360 (millimeters part), 360 (inches part) </td> </tr> 

    </table>  

     <br>  Created in NX7.5.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchPatternBuilder : public Builder
    {
        private: SketchPatternBuilderImpl * m_sketchpatternbuilder_impl;
        private: friend class  _SketchPatternBuilderBuilder;
        protected: SketchPatternBuilder();
        public: ~SketchPatternBuilder();
        /**Returns  the pattern section 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Section * Section
        (
        );
        /**Returns  the pattern service 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::GeometricUtilities::PatternDefinition * PatternService
        (
        );
        /**Returns  the flag to indicate if a spacing expression needs to be created 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: bool CreateSpacingExp
        (
        );
        /**Sets  the flag to indicate if a spacing expression needs to be created 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void SetCreateSpacingExp
        (
            bool createSpacingExp /** createspacingexp */ 
        );
        /** This function removes end constraint from the given pattern 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetEndConstraint
        (
            NXOpen::NXObject * parent /** Parent object in base chain */,
            int inx /** Index of the pattern - starts from 0 */,
            bool isStart /** TRUE, if we want to remove the start end con */,
            bool constraint /** TRUE to add the con, false to remove */
        );
        /**Returns  the flag to indicate if a spacing expression needs to be created 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: bool LockOrientation
        (
        );
        /**Sets  the flag to indicate if a spacing expression needs to be created 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void SetLockOrientation
        (
            bool lockOrientation /** lockorientation */ 
        );
        /** This function updates the pattern constraint with the number of copies set in the builder 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void UpdateCopies
        (
        );
        /** This function updates the pattern constraint according to the data set in pattern section 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void UpdateInputSection
        (
        );
    };
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