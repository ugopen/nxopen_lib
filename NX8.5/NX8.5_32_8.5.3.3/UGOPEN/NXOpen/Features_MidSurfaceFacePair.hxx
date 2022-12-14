#ifndef NXOpen_FEATURES_MIDSURFACEFACEPAIR_HXX_INCLUDED
#define NXOpen_FEATURES_MIDSURFACEFACEPAIR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MidSurfaceFacePair.ja
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
        class MidSurfaceFacePair;
    }
    class Body;
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _MidSurfaceFacePairBuilder;
        class MidSurfaceFacePairImpl;
        /** Represents a mid surface by face pairs feature  <br> This is an abstract class  <br> 
         <br>  Created in NX8.0.1.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  MidSurfaceFacePair : public Features::BodyFeature
        {
            private: MidSurfaceFacePairImpl * m_midsurfacefacepair_impl;
            private: friend class  _MidSurfaceFacePairBuilder;
            protected: MidSurfaceFacePair();
            public: ~MidSurfaceFacePair();
            /**Returns  the face pair data 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: double AverageThickness
            (
            );
            /**Returns  the face pair data 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Body * SheetBody
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
