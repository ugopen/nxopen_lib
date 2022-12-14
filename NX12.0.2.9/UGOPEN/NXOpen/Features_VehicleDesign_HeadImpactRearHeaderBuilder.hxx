#ifndef NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTREARHEADERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTREARHEADERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_HeadImpactRearHeaderBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_HeadImpactRearHeaderDetailBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_HeadImpactRearHeaderWizardBuilder.hxx>
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
            class HeadImpactRearHeaderBuilder;
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
            class HeadImpactRearHeaderDetailBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class HeadImpactRearHeaderWizardBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class _HeadImpactRearHeaderBuilderBuilder;
            class HeadImpactRearHeaderBuilderImpl;
            /** Represents a @link NXOpen::Features::VehicleDesign::HeadImpactRearHeaderBuilder NXOpen::Features::VehicleDesign::HeadImpactRearHeaderBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Features::VehicleDesignCollection::CreateHeadImpactRearHeaderBuilder  NXOpen::Features::VehicleDesignCollection::CreateHeadImpactRearHeaderBuilder @endlink  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HeadImpactRearHeaderBuilder : public NXOpen::Features::FeatureBuilder
            {
                private: HeadImpactRearHeaderBuilderImpl * m_headimpactrearheaderbuilder_impl;
                private: friend class  _HeadImpactRearHeaderBuilderBuilder;
                protected: HeadImpactRearHeaderBuilder();
                public: ~HeadImpactRearHeaderBuilder();
                /**Returns  the Rear Header Geometry builder, which represents a @link NXOpen::Features::VehicleDesign::HeadImpactRearHeaderWizardBuilder NXOpen::Features::VehicleDesign::HeadImpactRearHeaderWizardBuilder@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactRearHeaderWizardBuilder * Geometry
                (
                );
                /**Returns  the Rear Header Parameters builder, which represents a @link NXOpen::Features::VehicleDesign::HeadImpactRearHeaderDetailBuilder NXOpen::Features::VehicleDesign::HeadImpactRearHeaderDetailBuilder@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactRearHeaderDetailBuilder * Parameters
                (
                );
                /** The Rear Header initialize method. 
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
