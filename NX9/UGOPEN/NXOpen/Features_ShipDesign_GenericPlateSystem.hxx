#ifndef NXOpen_FEATURES_SHIPDESIGN_GENERICPLATESYSTEM_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_GENERICPLATESYSTEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_GenericPlateSystem.ja
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
            class GenericPlateSystem;
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
            class _GenericPlateSystemBuilder;
            class GenericPlateSystemImpl;
            /** Represents a Generic Plate System feature. The Generic Plate System feature is used to 
                    represent surface shapes in the ship that do not conform to deck, bulkhead or hull 
                    categories.  <br> To create or edit an instance of this class, use @link Features::ShipDesign::GenericPlateSystemBuilder  Features::ShipDesign::GenericPlateSystemBuilder @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  GenericPlateSystem : public Features::BodyFeature
            {
                private: GenericPlateSystemImpl * m_genericplatesystem_impl;
                private: friend class  _GenericPlateSystemBuilder;
                protected: GenericPlateSystem();
                public: ~GenericPlateSystem();
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