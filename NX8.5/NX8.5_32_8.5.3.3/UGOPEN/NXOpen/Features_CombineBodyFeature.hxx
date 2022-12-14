#ifndef NXOpen_FEATURES_COMBINEBODYFEATURE_HXX_INCLUDED
#define NXOpen_FEATURES_COMBINEBODYFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CombineBodyFeature.ja
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
#include <NXOpen/Features_IIsolateToolBodyOperation.hxx>
#include <NXOpen/INXObject.hxx>
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
        class CombineBodyFeature;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class IIsolateToolBodyOperation;
    }
    class INXObject;
    namespace Features
    {
        class _CombineBodyFeatureBuilder;
        class CombineBodyFeatureImpl;
        /** Represents a boolean feature.  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  CombineBodyFeature : public Features::BodyFeature, public virtual Features::IIsolateToolBodyOperation
        {
            private: CombineBodyFeatureImpl * m_combinebodyfeature_impl;
            private: friend class  _CombineBodyFeatureBuilder;
            protected: CombineBodyFeature();
            public: ~CombineBodyFeature();
            /** Isolates the tool bodies in boolean/sew/face-blend feature. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual void IsolateToolBodies
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
