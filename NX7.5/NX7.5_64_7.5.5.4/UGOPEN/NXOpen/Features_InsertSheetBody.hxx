#ifndef NXOpen_FEATURES_INSERTSHEETBODY_HXX_INCLUDED
#define NXOpen_FEATURES_INSERTSHEETBODY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_InsertSheetBody.ja
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
        class InsertSheetBody;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _InsertSheetBodyBuilder;
        class InsertSheetBodyImpl;
        /** Represents a insert sheet body feature */
        class NXOPENCPPEXPORT  InsertSheetBody : public Features::BodyFeature
        {
            private: InsertSheetBodyImpl * m_insertsheetbody_impl;
            private: friend class  _InsertSheetBodyBuilder;
            protected: InsertSheetBody();
            public: ~InsertSheetBody();
        };
    }
}
#undef EXPORTLIBRARY
#endif
