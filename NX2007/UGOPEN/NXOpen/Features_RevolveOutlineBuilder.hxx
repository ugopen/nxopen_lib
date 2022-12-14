#ifndef NXOpen_FEATURES_REVOLVEOUTLINEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_REVOLVEOUTLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_RevolveOutlineBuilder.ja
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
#include <NXOpen/Features_ServiceOrientedFeatureCurveBuilder.hxx>
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
        class RevolveOutlineBuilder;
    }
    class Direction;
    namespace Features
    {
        class ServiceOrientedFeatureCurveBuilder;
    }
    class ScCollector;
    class SelectFace;
    namespace Features
    {
        class _RevolveOutlineBuilderBuilder;
        class RevolveOutlineBuilderImpl;
        /** Represents a @link Features::RevolveOutline Features::RevolveOutline@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::CurveFeatureCollection::CreateRevolveOutlineBuilder  NXOpen::Features::CurveFeatureCollection::CreateRevolveOutlineBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  RevolveOutlineBuilder : public NXOpen::Features::ServiceOrientedFeatureCurveBuilder
        {
            private: RevolveOutlineBuilderImpl * m_revolveoutlinebuilder_impl;
            private: friend class  _RevolveOutlineBuilderBuilder;
            protected: RevolveOutlineBuilder();
            public: ~RevolveOutlineBuilder();
            /**Returns  the body select 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * TargetBodies
            (
            );
            /**Returns  the axial face 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * AxisFace
            (
            );
            /**Returns  the plane normal 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * PlaneNormal
            (
            );
            /**Sets  the plane normal 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPlaneNormal
            (
                NXOpen::Direction * planeNormal /** planenormal */ 
            );
            /**Returns  the plane side 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseSide
            (
            );
            /**Sets  the plane side 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReverseSide
            (
                bool reverseSide /** reverseside */ 
            );
            /**Returns  the excluded faces 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * ExcludedFaces
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
