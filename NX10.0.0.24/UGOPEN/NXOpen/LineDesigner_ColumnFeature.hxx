#ifndef NXOpen_LINEDESIGNER_COLUMNFEATURE_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_COLUMNFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_ColumnFeature.ja
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
#include <NXOpen/Features_Feature.hxx>
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
        class ColumnFeature;
    }
    namespace Features
    {
        class Feature;
    }
    namespace LineDesigner
    {
        class _ColumnFeatureBuilder;
        class ColumnFeatureImpl;
        /** Represents a column feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::ColumnFeatureBuilder  NXOpen::LineDesigner::ColumnFeatureBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  ColumnFeature : public NXOpen::Features::Feature
        {
            private: ColumnFeatureImpl * m_columnfeature_impl;
            private: friend class  _ColumnFeatureBuilder;
            protected: ColumnFeature();
            public: ~ColumnFeature();
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