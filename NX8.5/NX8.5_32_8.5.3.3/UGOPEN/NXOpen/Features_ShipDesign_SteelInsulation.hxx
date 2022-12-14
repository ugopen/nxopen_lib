#ifndef NXOpen_FEATURES_SHIPDESIGN_STEELINSULATION_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_STEELINSULATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_SteelInsulation.ja
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
        namespace ShipDesign
        {
            class SteelInsulation;
        }
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _SteelInsulationBuilder;
            class SteelInsulationImpl;
            /** Represents a steel insulation feature.  <br> To create or edit an instance of this class, use @link Features::ShipDesign::SteelInsulationBuilder  Features::ShipDesign::SteelInsulationBuilder @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SteelInsulation : public Features::BodyFeature
            {
                private: SteelInsulationImpl * m_steelinsulation_impl;
                private: friend class  _SteelInsulationBuilder;
                protected: SteelInsulation();
                public: ~SteelInsulation();
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
