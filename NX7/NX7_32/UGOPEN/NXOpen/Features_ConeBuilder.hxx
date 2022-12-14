#ifndef NXOpen_FEATURES_CONEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_CONEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ConeBuilder.ja
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
#include <NXOpen/Features_ConeBuilder.hxx>
#include <NXOpen/GeometricUtilities_BooleanOperation.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ConeBuilder;
    }
    class Axis;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class BooleanOperation;
    }
    class SelectICurve;
    namespace Features
    {
        class _ConeBuilderBuilder;
        /**
            Represents a builder for a cone feature. 
            This allows creation and editing of a cone feature.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateConeBuilder Features::FeatureCollection::CreateConeBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        BaseDiameter.Value </td> <td> 
         
        50 (millimeters part), 50 (inches part) </td> </tr> 

        <tr><td> 
         
        HalfAngle.Value </td> <td> 
         
        45 </td> </tr> 

        <tr><td> 
         
        Height.Value </td> <td> 
         
        25 (millimeters part), 25 (inches part) </td> </tr> 

        <tr><td> 
         
        TopDiameter.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        Type </td> <td> 
         
        DiametersAndHeight </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT ConeBuilder : public Features::FeatureBuilder
        {
            /** Represents the Cone type */
            public: enum Types
            {
                TypesDiametersAndHeight/** Represents type of cone created by providing Diameters and Height */,
                TypesDiametersAndHalfAngle/** Represents type of cone created by providing Diameters and Half Angle */,
                TypesBaseDiameterHeightAndHalfAngle/** Represents type of cone created by providing Base Diameter, Height and Half Angle */,
                TypesTopDiameterHeightAndHalfAngle/** Represents type of cone created by providing Top Diameter, Height and Half Angle */,
                TypesTwoCoaxialArcs/** Represents type of cone created by providing Two Coaxial Arcs */
            };

            private: friend class  _ConeBuilderBuilder;
            protected: ConeBuilder();
            /**Returns  the axis  <br> License requirements : None */
            public: NXOpen::Axis * Axis
            (
            );
            /**Sets  the axis  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAxis
            (
                NXOpen::Axis * axis /** axis */ 
            );
            /**Returns  the base diameter  <br> License requirements : None */
            public: NXOpen::Expression * BaseDiameter
            (
            );
            /**Returns  the top diameter  <br> License requirements : None */
            public: NXOpen::Expression * TopDiameter
            (
            );
            /**Returns  the height  <br> License requirements : None */
            public: NXOpen::Expression * Height
            (
            );
            /**Returns  the half angle  <br> License requirements : None */
            public: NXOpen::Expression * HalfAngle
            (
            );
            /**Returns  the base arc  <br> License requirements : None */
            public: NXOpen::SelectICurve * BaseArc
            (
            );
            /**Returns  the top arc  <br> License requirements : None */
            public: NXOpen::SelectICurve * TopArc
            (
            );
            /**Returns  the boolean option  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BooleanOperation * BooleanOption
            (
            );
            /**Returns  the type represented by @link Features::ConeBuilder::Types Features::ConeBuilder::Types@endlink   <br> License requirements : None */
            public: NXOpen::Features::ConeBuilder::Types Type
            (
            );
            /**Sets  the type represented by @link Features::ConeBuilder::Types Features::ConeBuilder::Types@endlink   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::ConeBuilder::Types type /** type */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
