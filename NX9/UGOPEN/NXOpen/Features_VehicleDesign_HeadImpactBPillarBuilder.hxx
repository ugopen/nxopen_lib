#ifndef NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTBPILLARBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTBPILLARBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_HeadImpactBPillarBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_HeadImpactBPillarBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactBPillarDetailBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactBPillarWizardBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactBuilder.hxx>
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
        namespace VehicleDesign
        {
            class HeadImpactBPillarBuilder;
        }
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class HeadImpactBPillarDetailBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class HeadImpactBPillarWizardBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class HeadImpactBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class _HeadImpactBPillarBuilderBuilder;
            class HeadImpactBPillarBuilderImpl;
            /** Represents a @link Features::VehicleDesign::HeadImpactBPillarBuilder Features::VehicleDesign::HeadImpactBPillarBuilder@endlink .  <br> To create a new instance of this class, use @link Features::VehicleDesignCollection::CreateHeadImpactBpillarBuilder  Features::VehicleDesignCollection::CreateHeadImpactBpillarBuilder @endlink  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HeadImpactBPillarBuilder : public Features::FeatureBuilder
            {
                private: HeadImpactBPillarBuilderImpl * m_headimpactbpillarbuilder_impl;
                private: friend class  _HeadImpactBPillarBuilderBuilder;
                protected: HeadImpactBPillarBuilder();
                public: ~HeadImpactBPillarBuilder();
                /**Returns  the B Pillar Geometry builder, which represents a @link Features::VehicleDesign::HeadImpactBPillarWizardBuilder Features::VehicleDesign::HeadImpactBPillarWizardBuilder@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactBPillarWizardBuilder * Geometry
                (
                );
                /**Returns  the B Pillar Parameters builder, which represents a @link Features::VehicleDesign::HeadImpactBPillarDetailBuilder Features::VehicleDesign::HeadImpactBPillarDetailBuilder@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactBPillarDetailBuilder * Parameters
                (
                );
                /** The B Pillar initialize method. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void Initialize
                (
                    NXOpen::Features::VehicleDesign::HeadImpactBuilder * parent /** parent */ 
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