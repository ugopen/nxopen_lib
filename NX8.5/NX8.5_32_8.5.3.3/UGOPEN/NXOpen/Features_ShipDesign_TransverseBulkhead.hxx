#ifndef NXOpen_FEATURES_SHIPDESIGN_TRANSVERSEBULKHEAD_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_TRANSVERSEBULKHEAD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_TransverseBulkhead.ja
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
            class TransverseBulkhead;
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
            class _TransverseBulkheadBuilder;
            class TransverseBulkheadImpl;
            /** Represents a Transverse Bulkhead feature. The Transverse Bulkhead is used to represent
                    mostly vertical surface shapes that align with the port to starboard direction of the ship.  <br> To create or edit an instance of this class, use @link Features::ShipDesign::TransverseBulkheadBuilder  Features::ShipDesign::TransverseBulkheadBuilder @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  TransverseBulkhead : public Features::BodyFeature
            {
                private: TransverseBulkheadImpl * m_transversebulkhead_impl;
                private: friend class  _TransverseBulkheadBuilder;
                protected: TransverseBulkhead();
                public: ~TransverseBulkhead();
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
