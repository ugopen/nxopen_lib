#ifndef NXOpen_CAM_ARCOUTPUTTYPECIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_ARCOUTPUTTYPECIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ArcOutputTypeCiBuilder.ja
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
        class ArcOutputTypeCiBuilder;
    }
    class Builder;
    namespace CAM
    {
        class _ArcOutputTypeCiBuilderBuilder;
        /** Represents a ArcOutputTypeCiBuilder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT ArcOutputTypeCiBuilder : public Builder
        {
            /** Available types for output*/
            public: enum OutputTypes
            {
                OutputTypesLinearOnly/** linear only */,
                OutputTypesCirPerpToTaxis/** cir perp to taxis */,
                OutputTypesCirPerpParallelToTaxis/** cir perp parallel to taxis */,
                OutputTypesNurbs/** nurbs */
            };

            private: friend class  _ArcOutputTypeCiBuilderBuilder;
            protected: ArcOutputTypeCiBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif