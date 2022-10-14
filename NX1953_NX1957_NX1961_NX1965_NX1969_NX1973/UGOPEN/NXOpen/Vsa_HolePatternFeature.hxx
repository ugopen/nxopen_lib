#ifndef NXOpen_VSA_HOLEPATTERNFEATURE_HXX_INCLUDED
#define NXOpen_VSA_HOLEPATTERNFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Vsa_HolePatternFeature.ja
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
        class HolePatternFeature;
    }
    class NXObject;
    namespace Vsa
    {
        class _HolePatternFeatureBuilder;
        class HolePatternFeatureImpl;
        /** Represents a Hole pattern feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::HolePatternFeatureBuilder  NXOpen::Vsa::HolePatternFeatureBuilder @endlink  <br> 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_VSAEXPORT  HolePatternFeature : public NXOpen::NXObject
        {
            private: HolePatternFeatureImpl * m_holepatternfeature_impl;
            private: friend class  _HolePatternFeatureBuilder;
            protected: HolePatternFeature();
            public: ~HolePatternFeature();
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