#ifndef NXOpen_FEATURES_BREP_HXX_INCLUDED
#define NXOpen_FEATURES_BREP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Brep.ja
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
        class Brep;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _BrepBuilder;
        class BrepImpl;
        /** Represents an unparameterized feature  <br> An unparameterized feature is obtained from an existing feature.  <br> 
         <br>  Created in NX6.0.2.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  Brep : public Features::BodyFeature
        {
            private: BrepImpl * m_brep_impl;
            private: friend class  _BrepBuilder;
            protected: Brep();
            public: ~Brep();
            /** Converts unparameterized feature to linked body 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void ConvertToLinkedBody
            (
            );
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
