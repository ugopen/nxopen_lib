#ifndef NXOpen_FEATURES_SHIPDESIGN_DVTOMVMAPPINGBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_DVTOMVMAPPINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_DvToMvMappingBuilder.ja
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
        namespace ShipDesign
        {
            class DvToMvMappingBuilder;
        }
    }
    class Body;
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _DvToMvMappingBuilderBuilder;
            class DvToMvMappingBuilderImpl;
            /**
                    Represents a @link NXOpen::Features::ShipDesign::DvToMvMapping NXOpen::Features::ShipDesign::DvToMvMapping@endlink  builder. This builder is used to
                    create ship version-up design view to manufacturing view mapping feature.
                    The mapping feature is created during a special version-up process, and will be used to drive NX to propagate
                    changes from design body to manufacturing body automatically.
                     <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateDvToMvMappingBuilder  NXOpen::Features::ShipCollection::CreateDvToMvMappingBuilder @endlink  <br> 
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  DvToMvMappingBuilder : public NXOpen::Features::FeatureBuilder
            {
                private: DvToMvMappingBuilderImpl * m_dvtomvmappingbuilder_impl;
                private: friend class  _DvToMvMappingBuilderBuilder;
                protected: DvToMvMappingBuilder();
                public: ~DvToMvMappingBuilder();
                /**Returns  the original design body. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Body * OriginalDesignBody
                (
                );
                /**Sets  the original design body. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetOriginalDesignBody
                (
                    NXOpen::Body * originalDesignBody /** originaldesignbody */ 
                );
                /**Returns  the original manufacturing body. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Body * OriginalMfgBody
                (
                );
                /**Sets  the original manufacturing body. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetOriginalMfgBody
                (
                    NXOpen::Body * originalMfgBody /** originalmfgbody */ 
                );
                /**Returns  the adopted design body. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Body * AdoptedDesignBody
                (
                );
                /**Sets  the adopted design body. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetAdoptedDesignBody
                (
                    NXOpen::Body * adoptedDesignBody /** adopteddesignbody */ 
                );
                /**Returns  the adopted manufacturing body. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Body * AdoptedMfgBody
                (
                );
                /**Sets  the adopted manufacturing body. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetAdoptedMfgBody
                (
                    NXOpen::Body * adoptedMfgBody /** adoptedmfgbody */ 
                );
                /**Returns  the design feature group. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Features::Feature * DesignFeatureGroup
                (
                );
                /**Sets  the design feature group. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetDesignFeatureGroup
                (
                    NXOpen::Features::Feature * designFeatureGroup /** designfeaturegroup */ 
                );
                /**Returns  the mfg feature group. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Features::Feature * MfgFeatureGroup
                (
                );
                /**Sets  the mfg feature group. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetMfgFeatureGroup
                (
                    NXOpen::Features::Feature * mfgFeatureGroup /** mfgfeaturegroup */ 
                );
            };
        }
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
