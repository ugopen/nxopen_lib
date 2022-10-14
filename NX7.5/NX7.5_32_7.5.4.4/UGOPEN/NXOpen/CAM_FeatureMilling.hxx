#ifndef NXOpen_CAM_FEATUREMILLING_HXX_INCLUDED
#define NXOpen_CAM_FEATUREMILLING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FeatureMilling.ja
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
        class FeatureMilling;
    }
    namespace CAM
    {
        class PlanarOperation;
    }
    namespace CAM
    {
        class _FeatureMillingBuilder;
        class FeatureMillingImpl;
        /** Represents a Feature Milling Operation */
        class NXOPENCPPEXPORT  FeatureMilling : public CAM::PlanarOperation
        {
            private: FeatureMillingImpl * m_featuremilling_impl;
            private: friend class  _FeatureMillingBuilder;
            protected: FeatureMilling();
            public: ~FeatureMilling();
        };
    }
}
#undef EXPORTLIBRARY
#endif