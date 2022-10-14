#ifndef NXOpen_CAM_ZLEVELMILLINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_ZLEVELMILLINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ZLevelMillingBuilder.ja
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
#include <NXOpen/CAM_PlanarOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ZLevelMillingBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class PlanarOperationBuilder;
    }
    namespace CAM
    {
        class _ZLevelMillingBuilderBuilder;
        /** Represents a ZLevelMilling Builder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreateZlevelMillingBuilder CAM::OperationCollection::CreateZlevelMillingBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ZLevelMillingBuilder : public CAM::PlanarOperationBuilder
        {
            /** Available types for level to level method in zlevel mill operation */
            public: enum LevelToLevelCutMethodTypes
            {
                LevelToLevelCutMethodTypesUseTransferMethod/** Use transfer method */,
                LevelToLevelCutMethodTypesDirectOnPart/** Direct on part */,
                LevelToLevelCutMethodTypesRampOnPart/** Ramp on part */,
                LevelToLevelCutMethodTypesStaggeredRampOnPart/** Staggered ramp on part */
            };

            private: friend class  _ZLevelMillingBuilderBuilder;
            protected: ZLevelMillingBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif