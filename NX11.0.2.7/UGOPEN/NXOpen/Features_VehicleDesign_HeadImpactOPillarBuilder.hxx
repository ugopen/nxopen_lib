#ifndef NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTOPILLARBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTOPILLARBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_HeadImpactOPillarBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_HeadImpactBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactOPillarBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactOPillarDetailBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactOPillarWizardBuilder.hxx>
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
        namespace VehicleDesign
        {
            class HeadImpactOPillarBuilder;
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
            class HeadImpactBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class HeadImpactOPillarDetailBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class HeadImpactOPillarWizardBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class _HeadImpactOPillarBuilderBuilder;
            class HeadImpactOPillarBuilderImpl;
            /** Represents a @link NXOpen::Features::VehicleDesign::HeadImpactOPillarBuilder NXOpen::Features::VehicleDesign::HeadImpactOPillarBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Features::VehicleDesignCollection::CreateHeadImpactOpillarBuilder  NXOpen::Features::VehicleDesignCollection::CreateHeadImpactOpillarBuilder @endlink  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HeadImpactOPillarBuilder : public NXOpen::Features::FeatureBuilder
            {
                private: HeadImpactOPillarBuilderImpl * m_headimpactopillarbuilder_impl;
                private: friend class  _HeadImpactOPillarBuilderBuilder;
                protected: HeadImpactOPillarBuilder();
                public: ~HeadImpactOPillarBuilder();
                /**Returns  the Additional Pillar Geometry builder, which represents a @link NXOpen::Features::VehicleDesign::HeadImpactOPillarWizardBuilder NXOpen::Features::VehicleDesign::HeadImpactOPillarWizardBuilder@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactOPillarWizardBuilder * Geometry
                (
                );
                /**Returns  the Additional Pillar Parameters builder, which represents a @link NXOpen::Features::VehicleDesign::HeadImpactOPillarDetailBuilder NXOpen::Features::VehicleDesign::HeadImpactOPillarDetailBuilder@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactOPillarDetailBuilder * Parameters
                (
                );
                /** The Additional Pillar initialize method. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void Initialize
                (
                    NXOpen::Features::VehicleDesign::HeadImpactBuilder * parent /** parent */ ,
                    int row /** row */ 
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