#ifndef NXOpen_FEATURES_VEHICLEDESIGN_INSTRUMENTPANELVISIBILITY_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_INSTRUMENTPANELVISIBILITY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_InstrumentPanelVisibility.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
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
            class InstrumentPanelVisibility;
        }
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class _InstrumentPanelVisibilityBuilder;
            class InstrumentPanelVisibilityImpl;
            /** Represents a instrument panel visibility feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::VehicleDesign::InstrumentPanelVisibilityBuilder  NXOpen::Features::VehicleDesign::InstrumentPanelVisibilityBuilder @endlink  <br> 
             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  InstrumentPanelVisibility : public NXOpen::Features::BodyFeature
            {
                private: InstrumentPanelVisibilityImpl * m_instrumentpanelvisibility_impl;
                private: friend class  _InstrumentPanelVisibilityBuilder;
                protected: InstrumentPanelVisibility();
                public: ~InstrumentPanelVisibility();
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
