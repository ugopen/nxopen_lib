#ifndef NXOpen_FEATURES_FLEXIBLECABLE_HXX_INCLUDED
#define NXOpen_FEATURES_FLEXIBLECABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_FlexibleCable.ja
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
        class FlexibleCable;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _FlexibleCableBuilder;
        class FlexibleCableImpl;
        /** Represents a flexible cable <br> To create or edit an instance of this class, use @link Features::SheetMetal::FlexibleCableBuilder  Features::SheetMetal::FlexibleCableBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  FlexibleCable : public Features::Feature
        {
            private: FlexibleCableImpl * m_flexiblecable_impl;
            private: friend class  _FlexibleCableBuilder;
            protected: FlexibleCable();
            public: ~FlexibleCable();
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
