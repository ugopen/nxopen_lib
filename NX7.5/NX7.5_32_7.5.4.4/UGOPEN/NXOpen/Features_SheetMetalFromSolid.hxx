#ifndef NXOpen_FEATURES_SHEETMETALFROMSOLID_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETALFROMSOLID_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetalFromSolid.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class SheetMetalFromSolid;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _SheetMetalFromSolidBuilder;
        class SheetMetalFromSolidImpl;
        /** Represents a Sheet Metal from Solid feature */
        class NXOPENCPPEXPORT  SheetMetalFromSolid : public Features::BodyFeature
        {
            private: SheetMetalFromSolidImpl * m_sheetmetalfromsolid_impl;
            private: friend class  _SheetMetalFromSolidBuilder;
            protected: SheetMetalFromSolid();
            public: ~SheetMetalFromSolid();
        };
    }
}
#undef EXPORTLIBRARY
#endif