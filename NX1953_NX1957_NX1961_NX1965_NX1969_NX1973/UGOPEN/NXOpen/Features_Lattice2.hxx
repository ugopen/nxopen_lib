#ifndef NXOpen_FEATURES_LATTICE2_HXX_INCLUDED
#define NXOpen_FEATURES_LATTICE2_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Lattice2.ja
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
        class Lattice2;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _Lattice2Builder;
        class Lattice2Impl;
        /** Represents a lattice utility  <br> To create or edit an instance of this class, use @link NXOpen::Features::Lattice2Builder  NXOpen::Features::Lattice2Builder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  Lattice2 : public NXOpen::Features::BodyFeature
        {
            private: Lattice2Impl * m_lattice2_impl;
            private: friend class  _Lattice2Builder;
            protected: Lattice2();
            public: ~Lattice2();
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
