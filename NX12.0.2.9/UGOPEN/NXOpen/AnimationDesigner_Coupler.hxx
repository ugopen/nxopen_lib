#ifndef NXOpen_ANIMATIONDESIGNER_COUPLER_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_COUPLER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_Coupler.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libanimationdesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AnimationDesigner
    {
        class Coupler;
    }
    class DisplayableObject;
    namespace AnimationDesigner
    {
        class _CouplerBuilder;
        class CouplerImpl;
        /** Represents the Animation Designer coupler class.  <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX12.0.2.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  Coupler : public NXOpen::DisplayableObject
        {
            private: CouplerImpl * m_coupler_impl;
            private: friend class  _CouplerBuilder;
            protected: Coupler();
            public: ~Coupler();
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
