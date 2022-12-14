#ifndef NXOpen_CAM_FACEMILLING_HXX_INCLUDED
#define NXOpen_CAM_FACEMILLING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FaceMilling.ja
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
        class FaceMilling;
    }
    namespace CAM
    {
        class PlanarOperation;
    }
    namespace CAM
    {
        class _FaceMillingBuilder;
        class FaceMillingImpl;
        /** Represents a Face Milling Operation */
        class NXOPENCPPEXPORT  FaceMilling : public CAM::PlanarOperation
        {
            private: FaceMillingImpl * m_facemilling_impl;
            private: friend class  _FaceMillingBuilder;
            protected: FaceMilling();
            public: ~FaceMilling();
        };
    }
}
#undef EXPORTLIBRARY
#endif
