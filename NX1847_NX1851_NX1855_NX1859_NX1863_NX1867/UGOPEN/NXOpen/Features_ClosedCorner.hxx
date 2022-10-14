#ifndef NXOpen_FEATURES_CLOSEDCORNER_HXX_INCLUDED
#define NXOpen_FEATURES_CLOSEDCORNER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ClosedCorner.ja
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
        class ClosedCorner;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _ClosedCornerBuilder;
        class ClosedCornerImpl;
        /** Represents a ClosedCorner feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::SheetMetal::ClosedCornerBuilder  NXOpen::Features::SheetMetal::ClosedCornerBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  ClosedCorner : public NXOpen::Features::Feature
        {
            private: ClosedCornerImpl * m_closedcorner_impl;
            private: friend class  _ClosedCornerBuilder;
            protected: ClosedCorner();
            public: ~ClosedCorner();
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