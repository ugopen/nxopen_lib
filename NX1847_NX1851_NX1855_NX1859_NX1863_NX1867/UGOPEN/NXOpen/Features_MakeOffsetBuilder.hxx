#ifndef NXOpen_FEATURES_MAKEOFFSETBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_MAKEOFFSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MakeOffsetBuilder.ja
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
        class MakeOffsetBuilder;
    }
    class Expression;
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
        class _MakeOffsetBuilderBuilder;
        class MakeOffsetBuilderImpl;
        /**
            Represents a @link NXOpen::Features::MakeOffset NXOpen::Features::MakeOffset@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateMakeOffsetBuilder  NXOpen::Features::FeatureCollection::CreateMakeOffsetBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        OffsetValue.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        SaveRelation </td> <td> 
         
        False </td> </tr> 

        </table>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  MakeOffsetBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: MakeOffsetBuilderImpl * m_makeoffsetbuilder_impl;
            private: friend class  _MakeOffsetBuilderBuilder;
            protected: MakeOffsetBuilder();
            public: ~MakeOffsetBuilder();
            /**Returns  the motion face 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * MotionFace
            (
            );
            /**Returns  the stationary face 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * StationaryFace
            (
            );
            /**Returns  the offset value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValue
            (
            );
            /**Returns  the keep relation. If true the Make Offset relation will be saved, else the Make Offset relation will be removed.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool SaveRelation
            (
            );
            /**Sets  the keep relation. If true the Make Offset relation will be saved, else the Make Offset relation will be removed.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetSaveRelation
            (
                bool saveRelation /** saverelation */ 
            );
            /**Returns  the face change overflow behavior. Please refer @link NXOpen::GeometricUtilities::FaceChangeOverflowBehavior NXOpen::GeometricUtilities::FaceChangeOverflowBehavior@endlink  for details. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
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