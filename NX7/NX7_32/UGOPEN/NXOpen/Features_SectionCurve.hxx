#ifndef NXOpen_FEATURES_SECTIONCURVE_HXX_INCLUDED
#define NXOpen_FEATURES_SECTIONCURVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SectionCurve.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class SectionCurve;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _SectionCurveBuilder;
        /** Represents a section curves feature */
        class NXOPENCPPEXPORT SectionCurve : public Features::Feature
        {
            private: friend class  _SectionCurveBuilder;
            protected: SectionCurve();
        };
    }
}
#undef EXPORTLIBRARY
#endif
