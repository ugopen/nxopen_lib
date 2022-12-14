#ifndef NXOpen_FEATURES_PATCH_HXX_INCLUDED
#define NXOpen_FEATURES_PATCH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Patch.ja
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
#include <NXOpen/Features_CombineBodyFeature.hxx>
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
        class Patch;
    }
    namespace Features
    {
        class CombineBodyFeature;
    }
    namespace Features
    {
        class _PatchBuilder;
        class PatchImpl;
        /** Represents a Patch feature  <br> To create or edit an instance of this class, use @link Features::PatchBuilder  Features::PatchBuilder @endlink  <br> 
         <br>  Created in NX6.0.1.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  Patch : public Features::CombineBodyFeature
        {
            private: PatchImpl * m_patch_impl;
            private: friend class  _PatchBuilder;
            protected: Patch();
            public: ~Patch();
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
