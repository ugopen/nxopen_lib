#ifndef NXOpen_FEATURES_CONTOURFLANGE_HXX_INCLUDED
#define NXOpen_FEATURES_CONTOURFLANGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ContourFlange.ja
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
        class ContourFlange;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _ContourFlangeBuilder;
        class ContourFlangeImpl;
        /** Represents a Contour Flange feature */
        class NXOPENCPPEXPORT  ContourFlange : public Features::Feature
        {
            private: ContourFlangeImpl * m_contourflange_impl;
            private: friend class  _ContourFlangeBuilder;
            protected: ContourFlange();
            public: ~ContourFlange();
        };
    }
}
#undef EXPORTLIBRARY
#endif
