#ifndef NXOpen_CAM_TOOLAXISTILTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TOOLAXISTILTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolAxisTiltBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ToolAxisTiltBuilder;
    }
    class Builder;
    class Curve;
    class Point;
    namespace CAM
    {
        class _ToolAxisTiltBuilderBuilder;
        /** Represents a builder for an inheritable double value in of a CAM.CAMObject  <br> This builder can not be instantiated separately. <br> */
        class NXOPENCPPEXPORT ToolAxisTiltBuilder : public Builder
        {
            /** Available types for tool axis tilt control in variable axis z level */
            public: enum TlaxisTypes
            {
                TlaxisTypesNone/** No tilting */,
                TlaxisTypesAwayFromPart = 7/** Tilt away from part */,
                TlaxisTypesAwayFromPoint = 9/** Tilt away from point */,
                TlaxisTypesTowardPoint/** Tilt tpward point */,
                TlaxisTypesAwayFromCurve = 13/** Tilt away from curve */,
                TlaxisTypesTowardCurve/** Tilt toward curve */
            };

            /** Available types for auto tilt */
            public: enum AutoTiltTypes
            {
                AutoTiltTypesAutomatic/** Automatically calculate tilt angle */,
                AutoTiltTypesSpecify/** User specifies the tilt angle */
            };

            private: friend class  _ToolAxisTiltBuilderBuilder;
            protected: ToolAxisTiltBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
