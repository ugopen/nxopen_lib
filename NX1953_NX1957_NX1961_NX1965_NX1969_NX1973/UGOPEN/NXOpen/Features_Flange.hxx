#ifndef NXOpen_FEATURES_FLANGE_HXX_INCLUDED
#define NXOpen_FEATURES_FLANGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Flange.ja
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
#include <NXOpen/Features_Feature.hxx>
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
        class Flange;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _FlangeBuilder;
        class FlangeImpl;
        /** Represents a Flange feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::SheetMetal::FlangeBuilder  NXOpen::Features::SheetMetal::FlangeBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  Flange : public NXOpen::Features::Feature
        {
            private: FlangeImpl * m_flange_impl;
            private: friend class  _FlangeBuilder;
            protected: Flange();
            public: ~Flange();
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
