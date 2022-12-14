#ifndef NXOpen_FEATURES_SHIPDESIGN_SHIPTRIMBODY_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_SHIPTRIMBODY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_ShipTrimBody.ja
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
            class ShipTrimBody;
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
            class _ShipTrimBodyBuilder;
            class ShipTrimBodyImpl;
            /** Represents a ship trim body feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::ShipDesign::ShipTrimBodyBuilder  NXOpen::Features::ShipDesign::ShipTrimBodyBuilder @endlink  <br> 
             <br>  Created in NX9.0.1.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ShipTrimBody : public NXOpen::Features::BodyFeature
            {
                private: ShipTrimBodyImpl * m_shiptrimbody_impl;
                private: friend class  _ShipTrimBodyBuilder;
                protected: ShipTrimBody();
                public: ~ShipTrimBody();
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
