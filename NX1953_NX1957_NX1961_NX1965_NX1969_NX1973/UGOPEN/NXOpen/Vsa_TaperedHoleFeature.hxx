#ifndef NXOpen_VSA_TAPEREDHOLEFEATURE_HXX_INCLUDED
#define NXOpen_VSA_TAPEREDHOLEFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Vsa_TaperedHoleFeature.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_vsa_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Vsa
    {
        class TaperedHoleFeature;
    }
    class NXObject;
    namespace Vsa
    {
        class _TaperedHoleFeatureBuilder;
        class TaperedHoleFeatureImpl;
        /** Represents a Tapered Hole feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::TaperedHoleFeatureBuilder  NXOpen::Vsa::TaperedHoleFeatureBuilder @endlink  <br> 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_VSAEXPORT  TaperedHoleFeature : public NXOpen::NXObject
        {
            private: TaperedHoleFeatureImpl * m_taperedholefeature_impl;
            private: friend class  _TaperedHoleFeatureBuilder;
            protected: TaperedHoleFeature();
            public: ~TaperedHoleFeature();
        };
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