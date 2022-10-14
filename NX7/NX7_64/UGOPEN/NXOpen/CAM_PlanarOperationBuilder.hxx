#ifndef NXOpen_CAM_PLANAROPERATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PLANAROPERATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_PlanarOperationBuilder.ja
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
#include <NXOpen/CAM_MillOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class PlanarOperationBuilder;
    }
    namespace CAM
    {
        class CutPatternBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class MillOperationBuilder;
    }
    namespace CAM
    {
        class NcmPlanarBuilder;
    }
    namespace CAM
    {
        class PmopToolAxisCiBuilder;
    }
    namespace CAM
    {
        class StepoverBuilder;
    }
    namespace CAM
    {
        class _PlanarOperationBuilderBuilder;
        /** Represents a PlanarOperation Builder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT PlanarOperationBuilder : public CAM::MillOperationBuilder
        {
            /** Available types for automatic part boundary method in planar mill operation */
            public: enum AutomaticPartBoundaryMethodTypes
            {
                AutomaticPartBoundaryMethodTypesFollowWallBottom/** Follow Bottom */,
                AutomaticPartBoundaryMethodTypesFollowWallTop/** Follow Top */
            };

            private: friend class  _PlanarOperationBuilderBuilder;
            protected: PlanarOperationBuilder();
            /**Returns  the non-cutting moves builder   <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder * NonCuttingBuilder
            (
            );
            /**Returns  the Gouge Checking Flag  <br> License requirements : None */
            public: bool GougeChecking
            (
            );
            /**Sets  the Gouge Checking Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetGougeChecking
            (
                bool gougeChecking /** the Gouge Checking Flag */
            );
            /**Returns  the Boundary Additional Passes  <br> License requirements : None */
            public: int AdditionalPasses
            (
            );
            /**Sets  the Boundary Additional Passes  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAdditionalPasses
            (
                int numPasses /** the Boundary Additional Passes */
            );
            /**Returns  the corner loops value  <br> License requirements : None */
            public: bool CornerLoops
            (
            );
            /**Sets  the corner loops value  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCornerLoops
            (
                bool cornerLoops /** the corner loops value */
            );
            /**Returns  the defer cutting status value  <br> License requirements : None */
            public: bool DeferCuttingStatus
            (
            );
            /**Sets  the defer cutting status value  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDeferCuttingStatus
            (
                bool deferCuttingStatus /** the defer cutting status value */
            );
            /**Returns  the cut pattern builder  <br> License requirements : None */
            public: NXOpen::CAM::CutPatternBuilder * CutPattern
            (
            );
            /**Returns  the depth per cut builder (inheritable double)  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DepthPerCut
            (
            );
            /**Returns  the boundary stepover builder  <br> License requirements : None */
            public: NXOpen::CAM::StepoverBuilder * BndStepover
            (
            );
            /**Returns  the tool minimum length usage  <br> License requirements : None */
            public: bool ToolMinimumLengthUsage
            (
            );
            /**Sets  the tool minimum length usage  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolMinimumLengthUsage
            (
                bool toolMinUsage /** the tool minimum length usage */
            );
            /**Returns  the Automatic Part Boundary Method   <br> License requirements : None */
            public: NXOpen::CAM::PlanarOperationBuilder::AutomaticPartBoundaryMethodTypes AutomaticPartBoundaryMethod
            (
            );
            /**Sets  the Automatic Part Boundary Method   <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAutomaticPartBoundaryMethod
            (
                NXOpen::CAM::PlanarOperationBuilder::AutomaticPartBoundaryMethodTypes automaticPartBoundary /** automaticpartboundary */ 
            );
            /**Returns  the pmop tool axis ci builder  <br> License requirements : None */
            public: NXOpen::CAM::PmopToolAxisCiBuilder * ToolAxis
            (
            );
            /**Returns  the cut level global cut depth builder  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * CutLevelGlobalCutDepth
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif