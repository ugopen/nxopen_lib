#ifndef NXOpen_CAM_CAVITYMILLING_HXX_INCLUDED
#define NXOpen_CAM_CAVITYMILLING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CavityMilling.ja
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
#include <NXOpen/CAM_PlanarOperation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class CavityMilling;
    }
    namespace CAM
    {
        class PlanarOperation;
    }
    namespace CAM
    {
        class _CavityMillingBuilder;
        class CavityMillingImpl;
        /** Represents a Cavity Milling Operation */
        class NXOPENCPPEXPORT  CavityMilling : public CAM::PlanarOperation
        {
            private: CavityMillingImpl * m_cavitymilling_impl;
            private: friend class  _CavityMillingBuilder;
            protected: CavityMilling();
            public: ~CavityMilling();
        };
    }
}
#undef EXPORTLIBRARY
#endif