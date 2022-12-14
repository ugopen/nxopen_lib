#ifndef NXOpen_FEATURES_LABELCHAMFER_HXX_INCLUDED
#define NXOpen_FEATURES_LABELCHAMFER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_LabelChamfer.ja
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
        class LabelChamfer;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _LabelChamferBuilder;
        /** Represents a label chamfer feature */
        class NXOPENCPPEXPORT LabelChamfer : public Features::BodyFeature
        {
            private: friend class  _LabelChamferBuilder;
            protected: LabelChamfer();
        };
    }
}
#undef EXPORTLIBRARY
#endif
