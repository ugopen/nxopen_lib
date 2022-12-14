#ifndef NXOpen_CAM_MILLOPERATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MILLOPERATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillOperationBuilder.ja
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
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MillOperationBuilder;
    }
    namespace CAM
    {
        class FeedsBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    namespace CAM
    {
        class _MillOperationBuilderBuilder;
        /** Represents a MillOperation Builder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT MillOperationBuilder : public CAM::OperationBuilder
        {
            /** Available types for Cut Wall Cleanup Status */
            public: enum CutWallCleanupStatusTypes
            {
                CutWallCleanupStatusTypesNone/** None */,
                CutWallCleanupStatusTypesBeforeCuttingRegion/** At Start */,
                CutWallCleanupStatusTypesAfterCuttingRegion/** At End */,
                CutWallCleanupStatusTypesAutomatic/** Automatic */
            };

            /** Available types for Edge Extension Type */
            public: enum EdgextTypeType
            {
                EdgextTypeTypeToolDiameter/**Tool Diameter*/,
                EdgextTypeTypeSpecify/**Specify*/
            };

            private: friend class  _MillOperationBuilderBuilder;
            protected: MillOperationBuilder();
            /**Returns  the feeds and speeds builder  <br> License requirements : None */
            public: NXOpen::CAM::FeedsBuilder * FeedsBuilder
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
