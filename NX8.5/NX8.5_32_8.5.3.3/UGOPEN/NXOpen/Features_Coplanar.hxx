#ifndef NXOpen_FEATURES_COPLANAR_HXX_INCLUDED
#define NXOpen_FEATURES_COPLANAR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Coplanar.ja
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
        class Coplanar;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _CoplanarBuilder;
        class CoplanarImpl;
        /** Represents a Coplanar feature  <br> To create or edit an instance of this class, use @link Features::CoplanarBuilder  Features::CoplanarBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  Coplanar : public Features::BodyFeature
        {
            private: CoplanarImpl * m_coplanar_impl;
            private: friend class  _CoplanarBuilder;
            protected: Coplanar();
            public: ~Coplanar();
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
