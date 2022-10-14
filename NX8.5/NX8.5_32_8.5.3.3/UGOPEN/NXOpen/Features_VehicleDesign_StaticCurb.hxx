#ifndef NXOpen_FEATURES_VEHICLEDESIGN_STATICCURB_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_STATICCURB_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_StaticCurb.ja
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
            class StaticCurb;
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
            class _StaticCurbBuilder;
            class StaticCurbImpl;
            /** Represents a static curb feature  <br> To create or edit an instance of this class, use @link Features::VehicleDesign::StaticCurbBuilder  Features::VehicleDesign::StaticCurbBuilder @endlink  <br> 
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  StaticCurb : public Features::BodyFeature
            {
                private: StaticCurbImpl * m_staticcurb_impl;
                private: friend class  _StaticCurbBuilder;
                protected: StaticCurb();
                public: ~StaticCurb();
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