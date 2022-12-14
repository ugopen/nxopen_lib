#ifndef NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTAPILLARBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTAPILLARBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_HeadImpactAPillarBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_HeadImpactAPillarDetailBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactAPillarWizardBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactBuilder.hxx>
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
            class HeadImpactAPillarBuilder;
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
            class HeadImpactAPillarDetailBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class HeadImpactAPillarWizardBuilder;
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
            class _HeadImpactAPillarBuilderBuilder;
            class HeadImpactAPillarBuilderImpl;
            /** Represents a @link NXOpen::Features::VehicleDesign::HeadImpactAPillarBuilder NXOpen::Features::VehicleDesign::HeadImpactAPillarBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Features::VehicleDesignCollection::CreateHeadImpactApillarBuilder  NXOpen::Features::VehicleDesignCollection::CreateHeadImpactApillarBuilder @endlink  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HeadImpactAPillarBuilder : public NXOpen::Features::FeatureBuilder
            {
                private: HeadImpactAPillarBuilderImpl * m_headimpactapillarbuilder_impl;
                private: friend class  _HeadImpactAPillarBuilderBuilder;
                protected: HeadImpactAPillarBuilder();
                public: ~HeadImpactAPillarBuilder();
                /**Returns  the A Pillar Geometry builder, which represents a @link NXOpen::Features::VehicleDesign::HeadImpactAPillarWizardBuilder NXOpen::Features::VehicleDesign::HeadImpactAPillarWizardBuilder@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactAPillarWizardBuilder * Geometry
                (
                );
                /**Returns  the A Pillar Parameters builder, which represents a @link NXOpen::Features::VehicleDesign::HeadImpactAPillarDetailBuilder NXOpen::Features::VehicleDesign::HeadImpactAPillarDetailBuilder@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactAPillarDetailBuilder * Parameters
                (
                );
                /** The A Pillar initialize method. 
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
