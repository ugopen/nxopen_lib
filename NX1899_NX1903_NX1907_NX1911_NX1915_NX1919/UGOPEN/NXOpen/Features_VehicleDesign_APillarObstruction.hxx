#ifndef NXOpen_FEATURES_VEHICLEDESIGN_APILLAROBSTRUCTION_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_APILLAROBSTRUCTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_APillarObstruction.ja
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
#include <NXOpen/Features_CurveFeature.hxx>
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
            class APillarObstruction;
        }
    }
    namespace Features
    {
        class CurveFeature;
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class _APillarObstructionBuilder;
            class APillarObstructionImpl;
            /** Represents an apillar obstruction feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::VehicleDesign::APillarObstructionBuilder  NXOpen::Features::VehicleDesign::APillarObstructionBuilder @endlink  <br> 
             <br>  Created in NX1899.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  APillarObstruction : public NXOpen::Features::CurveFeature
            {
                private: APillarObstructionImpl * m_apillarobstruction_impl;
                private: friend class  _APillarObstructionBuilder;
                protected: APillarObstruction();
                public: ~APillarObstruction();
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
