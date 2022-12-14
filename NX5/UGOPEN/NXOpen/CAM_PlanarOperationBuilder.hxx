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
        class AmStepoverCiBuilder;
    }
    namespace CAM
    {
        class ArcOutputTypeCiBuilder;
    }
    namespace CAM
    {
        class BndCutAngleCiBuilder;
    }
    namespace CAM
    {
        class BndCutDirCiBuilder;
    }
    namespace CAM
    {
        class BndStepoverCiBuilder;
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
        class MillOperationBuilder;
    }
    namespace CAM
    {
        class PmopCutMethodCiBuilder;
    }
    namespace CAM
    {
        class PmopToolAxisCiBuilder;
    }
    namespace CAM
    {
        class RoundPointBuilder;
    }
    namespace CAM
    {
        class _PlanarOperationBuilderBuilder;
        /** Represents a PlanarOperation Builder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT PlanarOperationBuilder : public CAM::MillOperationBuilder
        {
            /** Available types for options that can only be turned on or off */
            public: enum SimpleOptionTypes
            {
                SimpleOptionTypesOff/** The option is is turned off */,
                SimpleOptionTypesOn/** The option is turned off */
            };

            /** Available types for Follow Progression in planar mill operation */
            public: enum CutFollowProgressionTypes
            {
                CutFollowProgressionTypesOutward/** Outward */,
                CutFollowProgressionTypesInward/** Inward */
            };

            /** Available types for resequence region method in planar mill operation */
            public: enum ReseqRegionMethodTypes
            {
                ReseqRegionMethodTypesStandard/** standard */,
                ReseqRegionMethodTypesOptimize/** Optimize */,
                ReseqRegionMethodTypesRegionPoints/** Follow Start Points */,
                ReseqRegionMethodTypesPredrillPoints/** Follow Predrill Points */
            };

            /** Available types for cut pattern secondary in planar mill operation */
            public: enum PatternSecondaryTypes
            {
                PatternSecondaryTypesZig/** Maintain cut direction */,
                PatternSecondaryTypesZigZag/** Alternate cut direction */
            };

            /** Available types for Across Voids Method in planar mill operation */
            public: enum AcrossVoidsMethodTypes
            {
                AcrossVoidsMethodTypesFollow/** Follow */,
                AcrossVoidsMethodTypesCut/** Cut */,
                AcrossVoidsMethodTypesTraverse/** Traverse */
            };

            /** Available types for simplify shapes method in planar mill operation */
            public: enum SimplifyShapesMethodTypes
            {
                SimplifyShapesMethodTypesNone/** none */,
                SimplifyShapesMethodTypesConvexHull/** convex hull */,
                SimplifyShapesMethodTypesMinimumBox/** minumum box */
            };

            /** The available types for slowdown method in planar mill operation */
            public: enum SlowdownMethodTypes
            {
                SlowdownMethodTypesPreviousTool/** previous tool */,
                SlowdownMethodTypesPercentTool/** percent tool */
            };

            /** Available types for Trochoidal Path Width Types in planar mill operation */
            public: enum TrochoidalPathWidthTypes
            {
                TrochoidalPathWidthTypesDistance/** distance */,
                TrochoidalPathWidthTypesPercentToolDiameter/** percent tool diameter */
            };

            /** Available types for trochoidal path min width types in planar mill operation */
            public: enum TrochoidalPathMinWidthTypes
            {
                TrochoidalPathMinWidthTypesDistance/** distance */,
                TrochoidalPathMinWidthTypesPercentToolDiameter/** percent tool diameter */
            };

            /** Available types for trochoidal path stepover in planar mill operation */
            public: enum TrochoidalPathStepoverTypes
            {
                TrochoidalPathStepoverTypesDistance/** distance */,
                TrochoidalPathStepoverTypesPercentToolDiameter/** percent tool diameter */
            };

            /** Available types for max cut traverse in planar mill operation */
            public: enum MaxCutTraverseTypes
            {
                MaxCutTraverseTypesInactive/** inactive */,
                MaxCutTraverseTypesDistance/** distance */,
                MaxCutTraverseTypesPercentToolDiameter/** percent tool diameter */
            };

            /** Available types for corner fillet */
            public: enum CornerFilletTypes
            {
                CornerFilletTypesNone/** none */,
                CornerFilletTypesOnWall/** on wall */,
                CornerFilletTypesAllPasses/** all passes */
            };

            /** Available types for range subdivision type in planar mill operation */
            public: enum RangeSubdivisonTypes
            {
                RangeSubdivisonTypesEqualise/** subdivide cut range into equal steps */,
                RangeSubdivisonTypesBottomsOnly/** cut at range bottoms only */,
                RangeSubdivisonTypesOptimal/** subdivide cut range in an optimal
                                                                                                       * way such that max distance on part
                                                                                                       * between cuts is approximately the
                                                                                                       * same. */
            };

            /** Available types for cut level order type in planar mill operation */
            public: enum CutLevelOrderTypes
            {
                CutLevelOrderTypesLevelFirst/** level first type */,
                CutLevelOrderTypesDepthFirst/** depth first type */
            };

            /** Available types for cut control trim method type in planar mill operation */
            public: enum CutCtrlTrimMethodTypes
            {
                CutCtrlTrimMethodTypesNone/** none */,
                CutCtrlTrimMethodTypesSilhoutte/** silhoutte type */,
                CutCtrlTrimMethodTypesExteriorEdges/** exterior edges */
            };

            private: friend class  _PlanarOperationBuilderBuilder;
            protected: PlanarOperationBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
