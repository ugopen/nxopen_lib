#ifndef NXOpen_DIE_FILLAREA_HXX_INCLUDED
#define NXOpen_DIE_FILLAREA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_FillArea.ja
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
    namespace Die
    {
        class FillArea;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Die
    {
        class _FillAreaBuilder;
        class FillAreaImpl;
        /** Represents a die design fill area feature. */
        class NXOPENCPPEXPORT  FillArea : public Features::BodyFeature
        {
            private: FillAreaImpl * m_fillarea_impl;
            private: friend class  _FillAreaBuilder;
            protected: FillArea();
            public: ~FillArea();
        };
    }
}
#undef EXPORTLIBRARY
#endif
