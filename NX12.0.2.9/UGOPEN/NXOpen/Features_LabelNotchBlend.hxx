#ifndef NXOpen_FEATURES_LABELNOTCHBLEND_HXX_INCLUDED
#define NXOpen_FEATURES_LABELNOTCHBLEND_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_LabelNotchBlend.ja
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
        class LabelNotchBlend;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _LabelNotchBlendBuilder;
        class LabelNotchBlendImpl;
        /** Represents a label notch blend feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::LabelNotchBlendBuilder  NXOpen::Features::LabelNotchBlendBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  LabelNotchBlend : public NXOpen::Features::BodyFeature
        {
            private: LabelNotchBlendImpl * m_labelnotchblend_impl;
            private: friend class  _LabelNotchBlendBuilder;
            protected: LabelNotchBlend();
            public: ~LabelNotchBlend();
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