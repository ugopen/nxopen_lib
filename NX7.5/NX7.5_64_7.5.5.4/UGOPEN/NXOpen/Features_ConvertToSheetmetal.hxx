#ifndef NXOpen_FEATURES_CONVERTTOSHEETMETAL_HXX_INCLUDED
#define NXOpen_FEATURES_CONVERTTOSHEETMETAL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ConvertToSheetmetal.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ConvertToSheetmetal;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _ConvertToSheetmetalBuilder;
        class ConvertToSheetmetalImpl;
        /** Represents a ConvertToSheetmetal feature */
        class NXOPENCPPEXPORT  ConvertToSheetmetal : public Features::Feature
        {
            private: ConvertToSheetmetalImpl * m_converttosheetmetal_impl;
            private: friend class  _ConvertToSheetmetalBuilder;
            protected: ConvertToSheetmetal();
            public: ~ConvertToSheetmetal();
        };
    }
}
#undef EXPORTLIBRARY
#endif
