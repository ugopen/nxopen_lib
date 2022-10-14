#ifndef NXOpen_FEATURES_RADIATEFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_RADIATEFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_RadiateFaceBuilder.ja
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
#include <NXOpen/Features_FaceRecognitionBuilder.hxx>
#include <NXOpen/GeometricUtilities_FaceChangeOverflowBehavior.hxx>
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
        class RadiateFaceBuilder;
    }
    class Expression;
    namespace Features
    {
        class FaceRecognitionBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class FaceChangeOverflowBehavior;
    }
    class SelectFace;
    namespace Features
    {
        class _RadiateFaceBuilderBuilder;
        class RadiateFaceBuilderImpl;
        /** Represents a @link NXOpen::Features::RadiateFace NXOpen::Features::RadiateFace@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateRadiateFaceBuilder  NXOpen::Features::FeatureCollection::CreateRadiateFaceBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DimensionType </td> <td> 
         
        Offset </td> </tr> 

        <tr><td> 
         
        Distance.Value </td> <td> 
         
        0.0 (millimeters part), 0.0 (inches part) </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.CoaxialEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.CoplanarAxesEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.CoplanarEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.EqualDiameterEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.OffsetEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.ParallelEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.PerpendicularEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.SameOrbitEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.SymmetricEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.TangentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.ThicknessChainEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToRadiate.UseFaceBrowse </td> <td> 
         
        1 </td> </tr> 

        </table>  

         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  RadiateFaceBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Represents the radiate face dimension type */
            public: enum DimensionTypes
            {
                DimensionTypesOffset/** Adds radiate face with a delta radius value.*/,
                DimensionTypesDiameter/** Adds radiate face with an absolute diameter value.*/,
                DimensionTypesRadius/** Adds radiate face with an absolute radius value.*/
            };

            private: RadiateFaceBuilderImpl * m_radiatefacebuilder_impl;
            private: friend class  _RadiateFaceBuilderBuilder;
            protected: RadiateFaceBuilder();
            public: ~RadiateFaceBuilder();
            /**Returns  the radiate face dimension type 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::RadiateFaceBuilder::DimensionTypes DimensionType
            (
            );
            /**Sets  the radiate face dimension type 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDimensionType
            (
                NXOpen::Features::RadiateFaceBuilder::DimensionTypes type /** type */ 
            );
            /**Returns  the face to radiate 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::FaceRecognitionBuilder * FaceToRadiate
            (
            );
            /**Returns  the offset distance 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Distance
            (
            );
            /**Returns  the reverse offset direction 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse offset direction 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** the flag of reverse direction */
            );
            /**Returns  the referenced face or edge 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * Reference
            (
            );
            /**Returns  the axial face 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * AxisSel
            (
            );
            /**Returns  the diameter 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Diameter
            (
            );
            /**Returns  the radius 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Radius
            (
            );
            /**Returns  the face change overflow behavior. Please refer @link NXOpen::GeometricUtilities::FaceChangeOverflowBehavior NXOpen::GeometricUtilities::FaceChangeOverflowBehavior@endlink  for details. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FaceChangeOverflowBehavior * FaceChangeOverflowBehavior
            (
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