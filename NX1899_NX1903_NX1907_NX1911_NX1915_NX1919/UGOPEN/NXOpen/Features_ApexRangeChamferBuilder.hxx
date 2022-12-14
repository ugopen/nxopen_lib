#ifndef NXOpen_FEATURES_APEXRANGECHAMFERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_APEXRANGECHAMFERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ApexRangeChamferBuilder.ja
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
#include <NXOpen/GeometricUtilities_ChamferEdgeManager.hxx>
#include <NXOpen/GeometricUtilities_LengthLimitsListBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class ApexRangeChamferBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class ChamferEdgeManager;
    }
    namespace GeometricUtilities
    {
        class LengthLimitsListBuilder;
    }
    namespace Features
    {
        class _ApexRangeChamferBuilderBuilder;
        class ApexRangeChamferBuilderImpl;
        /**
            Represents a @link Features::ApexRangeChamfer Features::ApexRangeChamfer@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::DetailFeatureCollection::CreateApexRangeChamferBuilder  NXOpen::Features::DetailFeatureCollection::CreateApexRangeChamferBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  ApexRangeChamferBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Chamfer offset method definitions */
            public: enum JaChamferBuilderOffsetmethod
            {
                JaChamferBuilderOffsetmethodApexRange/** apex range */ ,
                JaChamferBuilderOffsetmethodFaceOffset/** face offset */ 
            };

            private: ApexRangeChamferBuilderImpl * m_apexrangechamferbuilder_impl;
            private: friend class  _ApexRangeChamferBuilderBuilder;
            protected: ApexRangeChamferBuilder();
            public: ~ApexRangeChamferBuilder();
            /**Returns  the manager contains edges to do chamfer 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ChamferEdgeManager * EdgeManager
            (
            );
            /**Returns  the data contains length limits to limit chamfer result 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LengthLimitsListBuilder * LengthLimitsList
            (
            );
            /**Returns  the tolerance 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the offset method 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::ApexRangeChamferBuilder::JaChamferBuilderOffsetmethod OffsetMethod
            (
            );
            /**Sets  the offset method 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOffsetMethod
            (
                NXOpen::Features::ApexRangeChamferBuilder::JaChamferBuilderOffsetmethod offsetMethod /** offsetmethod */ 
            );
            /** Creates a Apex Range Chamfer feature Edge Chain Set List builder @return ChamferEdgeManager object 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricUtilities::ChamferEdgeManager * CreateEdgeManager
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
