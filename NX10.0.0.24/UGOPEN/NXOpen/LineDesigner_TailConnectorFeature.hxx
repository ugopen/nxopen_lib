#ifndef NXOpen_LINEDESIGNER_TAILCONNECTORFEATURE_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_TAILCONNECTORFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_TailConnectorFeature.ja
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
#include <NXOpen/LineDesigner_TypedConnectorFeature.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class TailConnectorFeature;
    }
    namespace LineDesigner
    {
        class TypedConnectorFeature;
    }
    namespace LineDesigner
    {
        class _TailConnectorFeatureBuilder;
        class TailConnectorFeatureImpl;
        /** Represents a typed connector feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::TypedConnectorFeatureBuilder  NXOpen::LineDesigner::TypedConnectorFeatureBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  TailConnectorFeature : public NXOpen::LineDesigner::TypedConnectorFeature
        {
            private: TailConnectorFeatureImpl * m_tailconnectorfeature_impl;
            private: friend class  _TailConnectorFeatureBuilder;
            protected: TailConnectorFeature();
            public: ~TailConnectorFeature();
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
