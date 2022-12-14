#ifndef NXOpen_FEATURES_PASTEFACE_HXX_INCLUDED
#define NXOpen_FEATURES_PASTEFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PasteFace.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class PasteFace;
    }
    namespace Features
    {
        class CombineBodyFeature;
    }
    namespace Features
    {
        class _PasteFaceBuilder;
        class PasteFaceImpl;
        /** Represents a paste face feature */
        class NXOPENCPPEXPORT  PasteFace : public Features::CombineBodyFeature
        {
            private: PasteFaceImpl * m_pasteface_impl;
            private: friend class  _PasteFaceBuilder;
            protected: PasteFace();
            public: ~PasteFace();
        };
    }
}
#undef EXPORTLIBRARY
#endif
