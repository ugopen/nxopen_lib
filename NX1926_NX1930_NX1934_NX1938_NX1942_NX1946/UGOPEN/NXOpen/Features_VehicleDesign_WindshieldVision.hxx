#ifndef NXOpen_FEATURES_VEHICLEDESIGN_WINDSHIELDVISION_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_WINDSHIELDVISION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_WindshieldVision.ja
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
            class WindshieldVision;
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
            class _WindshieldVisionBuilder;
            class WindshieldVisionImpl;
            /** Represents a windshield vision feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::VehicleDesign::WindshieldVisionBuilder  NXOpen::Features::VehicleDesign::WindshieldVisionBuilder @endlink  <br> 
             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  WindshieldVision : public NXOpen::Features::BodyFeature
            {
                private: WindshieldVisionImpl * m_windshieldvision_impl;
                private: friend class  _WindshieldVisionBuilder;
                protected: WindshieldVision();
                public: ~WindshieldVision();
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
