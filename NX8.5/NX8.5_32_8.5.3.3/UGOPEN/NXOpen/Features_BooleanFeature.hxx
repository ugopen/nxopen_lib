#ifndef NXOpen_FEATURES_BOOLEANFEATURE_HXX_INCLUDED
#define NXOpen_FEATURES_BOOLEANFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_BooleanFeature.ja
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
#include <NXOpen/Features_IBoolean.hxx>
#include <NXOpen/Features_Intersect.hxx>
#include <NXOpen/Features_Subtract.hxx>
#include <NXOpen/Features_Unite.hxx>
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
        class BooleanFeature;
    }
    class Body;
    namespace Features
    {
        class CombineBodyFeature;
    }
    namespace Features
    {
        class IBoolean;
    }
    namespace Features
    {
        class Intersect;
    }
    namespace Features
    {
        class Subtract;
    }
    namespace Features
    {
        class Unite;
    }
    namespace Features
    {
        class _BooleanFeatureBuilder;
        class BooleanFeatureImpl;
        /** Represents a boolean feature.  <br> To create or edit an instance of this class, use @link Features::BooleanBuilder  Features::BooleanBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  BooleanFeature : public Features::CombineBodyFeature, public virtual Features::Unite, public virtual Features::Intersect, public virtual Features::Subtract
        {
            private: BooleanFeatureImpl * m_booleanfeature_impl;
            private: friend class  _BooleanFeatureBuilder;
            protected: BooleanFeature();
            public: ~BooleanFeature();
            /**Returns  
                the target body
                
             <br>  @deprecated Deprecated in NX4.0.0.  Use @link Features::BooleanFeature Features::BooleanFeature@endlink  instead. <br>  

             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX4.0.0.  Use Features::BooleanFeature instead.") virtual NXOpen::Body * Target
            (
            );
            /**Returns  
                the tool body
                
             <br>  @deprecated Deprecated in NX4.0.0.  Use @link Features::BooleanFeature Features::BooleanFeature@endlink  instead. <br>  

             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX4.0.0.  Use Features::BooleanFeature instead.") virtual NXOpen::Body * Tool
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
