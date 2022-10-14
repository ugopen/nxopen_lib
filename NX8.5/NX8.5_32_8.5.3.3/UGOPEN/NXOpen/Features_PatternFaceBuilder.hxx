#ifndef NXOpen_FEATURES_PATTERNFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_PATTERNFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PatternFaceBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_PatternFaceBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
        class PatternFaceBuilder;
    }
    class Axis;
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    class SelectTaggedObject;
    namespace Features
    {
        class _PatternFaceBuilderBuilder;
        class PatternFaceBuilderImpl;
        /**
            Represents a builder for a pattern face feature, don't use it until nx502.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreatePatternFaceBuilder  Features::FeatureCollection::CreatePatternFaceBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Angle.Value </td> <td> 
         
        90.0 </td> </tr> 

        <tr><td> 
         
        CircularCount.Value </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        RestoreOption </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        XCount.Value </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        XDistance.Value </td> <td> 
         
        10.0 (millimeters part), 0.5 (inches part) </td> </tr> 

        <tr><td> 
         
        YCount.Value </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        YDistance.Value </td> <td> 
         
        10.0 (millimeters part), 0.5 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX5.0.2.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  PatternFaceBuilder : public Features::FeatureBuilder
        {
            /** Enumeration of pattern type, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
            */
            public: enum PatternTypes
            {
                PatternTypesRectangular/** This stands for rectangular pattern type. */,
                PatternTypesCircular/** This stands for circular pattern type. */,
                PatternTypesMirror/** This stands for mirror pattern type. */
            };

            private: PatternFaceBuilderImpl * m_patternfacebuilder_impl;
            private: friend class  _PatternFaceBuilderBuilder;
            protected: PatternFaceBuilder();
            public: ~PatternFaceBuilder();
            /**Returns  the pattern face type, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::PatternFaceBuilder::PatternTypes Type
            (
            );
            /**Sets  the pattern face type, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::PatternFaceBuilder::PatternTypes patternType /** the pattern face type */
            );
            /**Returns  the faces to pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * Face
            (
            );
            /**Returns  the X direction of rectangular pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * XVector
            (
            );
            /**Sets  the X direction of rectangular pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetXVector
            (
                NXOpen::Direction * xVector /** the x direction */
            );
            /**Returns  the Y direction of rectangular pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * YVector
            (
            );
            /**Sets  the Y direction of rectangular pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetYVector
            (
                NXOpen::Direction * yVector /** the y direction */
            );
            /**Returns  the distance between rectangular pattern along X direction, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * XDistance
            (
            );
            /**Returns  the distance between rectangular pattern along Y direction, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * YDistance
            (
            );
            /**Returns  the count of rectangular pattern along X direction, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * XCount
            (
            );
            /**Returns  the count of rectangular pattern along Y direction, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * YCount
            (
            );
            /**Returns  the axis of circular pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Axis * Axis
            (
            );
            /**Sets  the axis of circular pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAxis
            (
                NXOpen::Axis * axis /** the circular axis */
            );
            /**Returns  the angle between circular pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns  the count of circular pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * CircularCount
            (
            );
            /**Returns  the mirror plane of mirror pattern, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObject * Plane
            (
            );
            /**Returns  the restore option for absent members. 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool RestoreOption
            (
            );
            /**Sets  the restore option for absent members. 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRestoreOption
            (
                bool restoreOption /** the restore option */
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