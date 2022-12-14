#ifndef NXOpen_FEATURES_TRIMBODY2_HXX_INCLUDED
#define NXOpen_FEATURES_TRIMBODY2_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TrimBody2.ja
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
        class TrimBody2;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _TrimBody2Builder;
        class TrimBody2Impl;
        /** Represents a trim body feature. @link NXOpen::Features::TrimBody NXOpen::Features::TrimBody@endlink 
             * is obsolete. Use this class instead.  <br> To create or edit an instance of this class, use @link NXOpen::Features::TrimBody2Builder  NXOpen::Features::TrimBody2Builder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  TrimBody2 : public NXOpen::Features::BodyFeature
        {
            private: TrimBody2Impl * m_trimbody2_impl;
            private: friend class  _TrimBody2Builder;
            protected: TrimBody2();
            public: ~TrimBody2();
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
