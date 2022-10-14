#ifndef NXOpen_FEATURES_IBOOLEAN_HXX_INCLUDED
#define NXOpen_FEATURES_IBOOLEAN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_IBoolean.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class IBoolean;
    }
    class Body;
    namespace Features
    {
        /** Base class for Unite, Intersect and Subtract features.
             <br> 
            Note that this class is now deprecated. Please use the 
            @link Features::BooleanFeature Features::BooleanFeature@endlink  instead.
             <br> 

         @deprecated Deprecated in NX4.0.0 <br> 
        */
        class NXOPENCPPEXPORT  NX_DEPRECATED("Deprecated in NX4.0.0")  IBoolean
        {
            virtual void EnsureVtableExists() {}
            public: virtual ~IBoolean() {}
            /**Returns  
                the target body
                
             @deprecated Deprecated in NX4.0.0 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX4.0.0") virtual NXOpen::Body * Target
            (
            ) = 0;
            /**Returns  
                the tool body
                
             @deprecated Deprecated in NX4.0.0 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX4.0.0") virtual NXOpen::Body * Tool
            (
            ) = 0;
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif