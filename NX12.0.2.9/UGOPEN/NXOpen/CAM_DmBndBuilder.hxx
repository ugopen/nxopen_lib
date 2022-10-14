#ifndef NXOpen_CAM_DMBNDBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DMBNDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DmBndBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class DmBndBuilder;
    }
    namespace CAM
    {
        class CutAngle;
    }
    namespace CAM
    {
        class CutPatternBuilder;
    }
    namespace CAM
    {
        class StepoverBuilder;
    }
    class Point;
    namespace CAM
    {
        class _DmBndBuilderBuilder;
        class DmBndBuilderImpl;
        /** Represents a Boundary Drive Method Builder 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  DmBndBuilder : public NXOpen::TaggedObject
        {
            /** Available types for Boundary cut pattern in FASurfaceContour */
            public: enum BndCutPatternTypes
            {
                BndCutPatternTypesFollowPeriphery/** Follow Periphery */,
                BndCutPatternTypesProfile/** Profile */,
                BndCutPatternTypesSep1/** separate one */,
                BndCutPatternTypesParallelLines/** Parallel Lines */,
                BndCutPatternTypesRadialLines/** Radial Lines */,
                BndCutPatternTypesConcArcs/** Concentric Arcs */,
                BndCutPatternTypesSep2/** separate two */,
                BndCutPatternTypesStandardDrive/** Standard Drive */
            };

            /** Available types for Boundary cut traversal in FASurfaceContour */
            public: enum BndCutTraversalTypes
            {
                BndCutTraversalTypesZigZag/** Zig-Zag */,
                BndCutTraversalTypesZig/** Zig */,
                BndCutTraversalTypesZigContour/** Zig with Contour */,
                BndCutTraversalTypesStepover/** Zig with Stepover */
            };

            /** Available types for Boundary Pattern Center in FASurfaceContour */
            public: enum BndPatternCenterTypes
            {
                BndPatternCenterTypesMethodAutomatic/** Automatic */,
                BndPatternCenterTypesMethodSpecify/** Specify */
            };

            /** Available types for Boundary Pocketing Direction in FASurfaceContour */
            public: enum BndPocketDirTypes
            {
                BndPocketDirTypesOutward/** Outward */,
                BndPocketDirTypesInward/** Inward */
            };

            /** Available types for in FASurfaceContour */
            public: enum BndCustomStartTypes
            {
                BndCustomStartTypesCustom/** Boundary Milling Custom Start Custom */,
                BndCustomStartTypesAutomatic/** Boundary Milling Custom Start Automatic */
            };

            /** Available types for boundary use part cantainment Option*/
            public: enum UsePartTypes
            {
                UsePartTypesPartContainOff/** Part Containment Off */,
                UsePartTypesPartContainLargestLoop/** Part Containment Largest Loop */,
                UsePartTypesPartContainAllLoops/** Part Containment All Loops */
            };

            /** Available types for boundary Corner Control Option*/
            public: enum ApplyFilletAtTypes
            {
                ApplyFilletAtTypesBoundary/** Boundary */,
                ApplyFilletAtTypesSurface/** Part Surface */,
                ApplyFilletAtTypesBoundaryAndSurface/** Boundary and Part Surface */
            };

            private: DmBndBuilderImpl * m_dmbndbuilder_impl;
            private: friend class  _DmBndBuilderBuilder;
            protected: DmBndBuilder();
            public: ~DmBndBuilder();
            /** Get boundary intol outtol  @return  the boundary inside and outside tolerance values 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetDmBndIntolOuttol
            (
            );
            /** Set boundary intol outtol 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDmBndIntolOuttol
            (
                const std::vector<double> & values /** the boundary inside and outside tolerance values */
            );
            /**Returns  the Boundary Stock 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double DmBndStock
            (
            );
            /**Sets  the Boundary Stock 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDmBndStock
            (
                double stockValue /** the boundary stock value */
            );
            /**Returns  the Use Part 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::DmBndBuilder::UsePartTypes UsePart
            (
            );
            /**Sets  the Use Part 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUsePart
            (
                NXOpen::CAM::DmBndBuilder::UsePartTypes partContain /** the use part value */
            );
            /** Returns the Cut Pattern  @return  the Cut Pattern value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::DmBndBuilder::BndCutPatternTypes GetBndCutPattern
            (
            );
            /** Sets the Cut Pattern 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBndCutPattern
            (
                NXOpen::CAM::DmBndBuilder::BndCutPatternTypes bndCutPattern /** the Cut Pattern value */
            );
            /** Returns the Cut Traversal  @return  the Cut Traversal value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::DmBndBuilder::BndCutTraversalTypes GetBndCutTraversal
            (
            );
            /** Sets the Cut Traversal 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBndCutTraversal
            (
                NXOpen::CAM::DmBndBuilder::BndCutTraversalTypes bndCutTraversal /** the Cut Traversal value */
            );
            /**Returns  the Pattern Center 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::DmBndBuilder::BndPatternCenterTypes CutPatternCenter
            (
            );
            /**Sets  the Pattern Center 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCutPatternCenter
            (
                NXOpen::CAM::DmBndBuilder::BndPatternCenterTypes patternCenterValue /** patterncentervalue */ 
            );
            /**Returns  the Pattern Center Point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * PatternCenterPoint
            (
            );
            /**Sets  the Pattern Center Point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPatternCenterPoint
            (
                NXOpen::Point * centerPoint /** centerpoint */ 
            );
            /** Get boundary Cut Zig Dir   @return  the boundary cut zig dir values 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetDmBndCutZigDir
            (
            );
            /** Set boundary Zig Dir 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDmBndCutZigDir
            (
                const std::vector<double> & bndCutZigDir /** the boundary zig dir values */
            );
            /**Returns  the Pocketing Deriction 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::DmBndBuilder::BndPocketDirTypes BndPocketDir
            (
            );
            /**Sets  the Pocketing Deriction 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBndPocketDir
            (
                NXOpen::CAM::DmBndBuilder::BndPocketDirTypes pocketDirValue /** the Pocketing Deriction value */
            );
            /**Returns  the Additional Passes 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int BndAddPasses
            (
            );
            /**Sets  the Additional Passes 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBndAddPasses
            (
                int addPassesValue /** the Additional Passes value */
            );
            /**Returns  the Island Clean 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IslandCleanupStatus
            (
            );
            /**Sets  the Island Clean 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIslandCleanupStatus
            (
                bool islandClean /** the Island Clean */
            );
            /**Returns  the Profile Pass 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool BndProfilePass
            (
            );
            /**Sets  the Profile Pass 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBndProfilePass
            (
                bool bndProfilePass /** the Profile Pass */
            );
            /**Returns  the Profile Pass Stock 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double BndProfilePassStock
            (
            );
            /**Sets  the Profile Pass Stock 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBndProfilePassStock
            (
                double bndProfilePassStock /** the Profile Pass Stock */
            );
            /**Returns  the Region Connection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool RegionConnection
            (
            );
            /**Sets  the Region Connection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRegionConnection
            (
                bool regionCon /** the Region Connection */
            );
            /**Returns  the Apply at Boundary 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool ApplyAtBoundary
            (
            );
            /**Sets  the Apply at Boundary 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetApplyAtBoundary
            (
                bool applyBoundaryValue /** the Apply at Boundary */
            );
            /**Returns  the Apply at Part Surface 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool ApplyAtPartSurface
            (
            );
            /**Sets  the Apply at Part Surface 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetApplyAtPartSurface
            (
                bool applyPartSurface /** the Apply at Part Surface */
            );
            /**Returns  the Custom Start 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::DmBndBuilder::BndCustomStartTypes BndCustomStart
            (
            );
            /**Sets  the Custom Start 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBndCustomStart
            (
                NXOpen::CAM::DmBndBuilder::BndCustomStartTypes customStartValue /** the Custom Start */
            );
            /**Returns  the Display Tool End 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool DispToolEnd
            (
            );
            /**Sets  the Display Tool End 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDispToolEnd
            (
                bool dispToolEndValue /** the Display Tool End */
            );
            /**Returns  the Display Contact 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool DispContact
            (
            );
            /**Sets  the Display Contact 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDispContact
            (
                bool dispContactdValue /** the Display Contact */
            );
            /**Returns  the Display Contact Normal 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool DispContactNormal
            (
            );
            /**Sets  the Display Contact Normal 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDispContactNormal
            (
                bool dispContactNormalValue /** the Display Contact Normal */
            );
            /**Returns  the Display Tool End Projection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool DisToolEndProj
            (
            );
            /**Sets  the Display Tool End Projection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDisToolEndProj
            (
                bool dispToolEndProjValue /** the Display Tool End Projection */
            );
            /**Returns  the cut angle ci builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CutAngle * CutAngle
            (
            );
            /**Returns  the stepover builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::StepoverBuilder * StepoverBuilder
            (
            );
            /**Returns  the apply fillet 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::DmBndBuilder::ApplyFilletAtTypes ApplyFilletAt
            (
            );
            /**Sets  the apply fillet 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetApplyFilletAt
            (
                NXOpen::CAM::DmBndBuilder::ApplyFilletAtTypes applyFilletAt /** applyfilletat */ 
            );
            /**Returns  the cut pattern builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CutPatternBuilder * CutPatternBuilder
            (
            );
            /**Returns  the island cleanup status 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool IslandCleanup
            (
            );
            /**Sets  the island cleanup status 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIslandCleanup
            (
                bool status /** status */ 
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif