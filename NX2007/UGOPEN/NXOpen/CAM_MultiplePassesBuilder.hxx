#ifndef NXOpen_CAM_MULTIPLEPASSESBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MULTIPLEPASSESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MultiplePassesBuilder.ja
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
        class MultiplePassesBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class InheritableIntBuilder;
    }
    namespace CAM
    {
        class _MultiplePassesBuilderBuilder;
        class MultiplePassesBuilderImpl;
        /** Represents a MultiplePassesBuilder 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MultiplePassesBuilder : public NXOpen::TaggedObject
        {
            /** Available types for Step Method */
            public: enum StepMethodTypes
            {
                StepMethodTypesIncrement/**Increment*/,
                StepMethodTypesPasses/**Passes*/
            };

            /** Available types for Order */
            public: enum OrderTypes
            {
                OrderTypesSidePassesFirst/**Side First*/,
                OrderTypesDepthPassesFirst/**Depth First*/
            };

            private: MultiplePassesBuilderImpl * m_multiplepassesbuilder_impl;
            private: friend class  _MultiplePassesBuilderBuilder;
            protected: MultiplePassesBuilder();
            public: ~MultiplePassesBuilder();
            /**Returns  the Do Side Passes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool DoSidePasses
            (
            );
            /**Sets  the Do Side Passes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDoSidePasses
            (
                bool doSidePasses /** the toggle value of Do Side Passes*/
            );
            /**Returns  the Total Thickness
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * TotalThickness
            (
            );
            /**Returns  the Side Step Method 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::MultiplePassesBuilder::StepMethodTypes SideStepMethod
            (
            );
            /**Sets  the Side Step Method 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSideStepMethod
            (
                NXOpen::CAM::MultiplePassesBuilder::StepMethodTypes sideStepMethod /** the value of Side Step Method */
            );
            /**Returns  the Side Increment 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * SideIncrement
            (
            );
            /**Returns  the Number of Side Passes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * NumberOfSidePasses
            (
            );
            /**Returns  the Do Depth Passes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: bool DoDepthPasses
            (
            );
            /**Sets  the Do Depth Passes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDoDepthPasses
            (
                bool doDepthPasses /** the toggle value of do depth passes*/
            );
            /**Returns  the Total Depth 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * TotalDepth
            (
            );
            /**Returns  the Depth Step Method
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::MultiplePassesBuilder::StepMethodTypes DepthStepMethod
            (
            );
            /**Sets  the Depth Step Method
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDepthStepMethod
            (
                NXOpen::CAM::MultiplePassesBuilder::StepMethodTypes depthStepMethod /** the value of Depth Step Method */
            );
            /**Returns  the Depth Increment 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DepthIncrement
            (
            );
            /**Returns  the Number of Depth Passes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * NumberOfDepthPasses
            (
            );
            /**Returns  the Order 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::MultiplePassesBuilder::OrderTypes Order
            (
            );
            /**Sets  the Order 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOrder
            (
                NXOpen::CAM::MultiplePassesBuilder::OrderTypes order /** the value of Order */
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