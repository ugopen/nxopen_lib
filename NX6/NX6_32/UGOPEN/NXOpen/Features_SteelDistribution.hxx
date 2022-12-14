#ifndef NXOpen_FEATURES_STEELDISTRIBUTION_HXX_INCLUDED
#define NXOpen_FEATURES_STEELDISTRIBUTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SteelDistribution.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class SteelDistribution;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _SteelDistributionBuilder;
        /** Represents a steel distribution feature */
        class NXOPENCPPEXPORT SteelDistribution : public Features::BodyFeature
        {
            private: friend class  _SteelDistributionBuilder;
            protected: SteelDistribution();
        };
    }
}
#undef EXPORTLIBRARY
#endif
