#ifndef NXOpen_VSA_PINFEATURE_HXX_INCLUDED
#define NXOpen_VSA_PINFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Vsa_PinFeature.ja
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
        class PinFeature;
    }
    class NXObject;
    namespace Vsa
    {
        class _PinFeatureBuilder;
        class PinFeatureImpl;
        /** Represents a Pin feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::PinFeatureBuilder  NXOpen::Vsa::PinFeatureBuilder @endlink  <br> 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_VSAEXPORT  PinFeature : public NXOpen::NXObject
        {
            private: PinFeatureImpl * m_pinfeature_impl;
            private: friend class  _PinFeatureBuilder;
            protected: PinFeature();
            public: ~PinFeature();
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
