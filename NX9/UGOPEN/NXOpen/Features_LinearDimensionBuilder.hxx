#ifndef NXOpen_FEATURES_LINEARDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_LINEARDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_LinearDimensionBuilder.ja
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
#include <NXOpen/Features_DimensionBuilder.hxx>
#include <NXOpen/Features_LinearDimensionBuilder.hxx>
#include <NXOpen/GeometricUtilities_OrientXpressBuilder.hxx>
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
        class LinearDimensionBuilder;
    }
    class Direction;
    class Face;
    namespace Features
    {
        class DimensionBuilder;
    }
    namespace GeometricUtilities
    {
        class OrientXpressBuilder;
    }
    class SelectNXObject;
    namespace Features
    {
        class _LinearDimensionBuilderBuilder;
        class LinearDimensionBuilderImpl;
        /**
            Represents a @link Features::LinearDimension Features::LinearDimension@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateLinearDimensionBuilder  Features::FeatureCollection::CreateLinearDimensionBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        OrientationOption </td> <td> 
         
        OrientXpress </td> </tr> 

        <tr><td> 
         
        Value.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  LinearDimensionBuilder : public Features::DimensionBuilder
        {
            /** the option that controls whether the OrientXpress or whether the vector block
                    Controls the orientation of the Linear Dimension */
            public: enum OrientationOptionType
            {
                OrientationOptionTypeOrientXpress/** Orientation option using Orient Xpress */,
                OrientationOptionTypeVector/** Orientation option using vector */
            };

            private: LinearDimensionBuilderImpl * m_lineardimensionbuilder_impl;
            private: friend class  _LinearDimensionBuilderBuilder;
            protected: LinearDimensionBuilder();
            public: ~LinearDimensionBuilder();
            /**Returns  the origin object from which the ADM Linear dimension is measured from 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * OriginObject
            (
            );
            /**Returns  the measurement object to which the ADM Linear Dimension is measured to 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * MeasurementObject
            (
            );
            /**Returns  the option that controls whether the OrientXpress or whether the vector block
                    Controls the orientation of the Linear Dimension 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::LinearDimensionBuilder::OrientationOptionType OrientationOption
            (
            );
            /**Sets  the option that controls whether the OrientXpress or whether the vector block
                    Controls the orientation of the Linear Dimension 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetOrientationOption
            (
                NXOpen::Features::LinearDimensionBuilder::OrientationOptionType orientationOption /** orientationoption */ 
            );
            /**Returns  the dimension orientation vector for the Linear Dimension 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * DimensionOrientationVector
            (
            );
            /**Sets  the dimension orientation vector for the Linear Dimension 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetDimensionOrientationVector
            (
                NXOpen::Direction * dimensionOrientationVector /** dimensionorientationvector */ 
            );
            /**Returns  the OrientXpress that is employed in the ADM Linear Dimension Feature 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OrientXpressBuilder * DimensionOrientation
            (
            );
            /** The important face that is being moved through the ADM Linear Dimension Feature.
                   The system will try to silently infer one. But if the user wants to provide one, then
                   he/she needs to pass in the face through this command 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetFaceToMove
            (
                NXOpen::Face * face /** face */ 
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
