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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_Geometry.hxx>
#include <NXOpen/CAM_MillOperationBuilder.hxx>
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
        class PlanarOperationBuilder;
    }
    namespace CAM
    {
        class CutPatternBuilder;
    }
    namespace CAM
    {
        class Geometry;
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
        class StepoverBuilder;
    }
    namespace CAM
    {
        class ToolAxisFixed;
    }
    namespace CAM
    {
        class _PlanarOperationBuilderBuilder;
        class PlanarOperationBuilderImpl;
        /** Represents a PlanarOperation Builder  <br> This is an abstract class and cannot be instantiated.  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  PlanarOperationBuilder : public NXOpen::CAM::MillOperationBuilder
        {
            /** Available types for automatic part boundary method in planar mill operation */
            public: enum AutomaticPartBoundaryMethodTypes
            {
                AutomaticPartBoundaryMethodTypesFollowWallBottom/** Follow Bottom */,
                AutomaticPartBoundaryMethodTypesFollowWallTop/** Follow Top */
            };

            private: PlanarOperationBuilderImpl * m_planaroperationbuilder_impl;
            private: friend class  _PlanarOperationBuilderBuilder;
            protected: PlanarOperationBuilder();
            public: ~PlanarOperationBuilder();
            /**Returns  the non-cutting moves builder  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder * NonCuttingBuilder
            (
            );
            /**Returns  the Boundary Additional Passes 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int AdditionalPasses
            (
            );
            /**Sets  the Boundary Additional Passes 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAdditionalPasses
            (
                int numPasses /** the Boundary Additional Passes */
            );
            /**Returns  the corner loops value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool CornerLoops
            (
            );
            /**Sets  the corner loops value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCornerLoops
            (
                bool cornerLoops /** the corner loops value */
            );
            /**Returns  the defer cutting status value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool DeferCuttingStatus
            (
            );
            /**Sets  the defer cutting status value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDeferCuttingStatus
            (
                bool deferCuttingStatus /** the defer cutting status value */
            );
            /**Returns  the cut pattern builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CutPatternBuilder * CutPattern
            (
            );
            /**Returns  the depth per cut builder (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DepthPerCut
            (
            );
            /**Returns  the boundary stepover builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::StepoverBuilder * BndStepover
            (
            );
            /**Returns  the tool minimum length usage 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToolMinimumLengthUsage
            (
            );
            /**Sets  the tool minimum length usage 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolMinimumLengthUsage
            (
                bool toolMinUsage /** the tool minimum length usage */
            );
            /**Returns  the Automatic Part Boundary Method  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::PlanarOperationBuilder::AutomaticPartBoundaryMethodTypes AutomaticPartBoundaryMethod
            (
            );
            /**Sets  the Automatic Part Boundary Method  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAutomaticPartBoundaryMethod
            (
                NXOpen::CAM::PlanarOperationBuilder::AutomaticPartBoundaryMethodTypes automaticPartBoundary /** automaticpartboundary */ 
            );
            /**Returns  the pmop tool axis ci builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisFixed * ToolAxisFix
            (
            );
            /**Returns  the part geometry builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Geometry * PartGeometry
            (
            );
            /**Returns  the check geometry builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Geometry * CheckGeometry
            (
            );
            /**Returns  the cut area geometry builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Geometry * CutAreaGeometry
            (
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
