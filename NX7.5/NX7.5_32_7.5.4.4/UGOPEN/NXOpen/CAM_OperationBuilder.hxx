#ifndef NXOpen_CAM_OPERATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAM_OPERATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_OperationBuilder.ja
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
#include <NXOpen/CAM_UdeSet.hxx>
#include <NXOpen/CAM_ParamBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class OperationBuilder;
    }
    namespace CAM
    {
        class GeometryCiBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class OperationDisplayOptionsBuilder;
    }
    namespace CAM
    {
        class ParamBuilder;
    }
    namespace CAM
    {
        class PostEventsCiBuilder;
    }
    namespace CAM
    {
        class ToolChangeCiBuilder;
    }
    namespace CAM
    {
        class UdeSet;
    }
    namespace CAM
    {
        class _OperationBuilderBuilder;
        class OperationBuilderImpl;
        /** Represents a Opr Builder  <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT  OperationBuilder : public CAM::ParamBuilder
        {
            /** Available types for Hole Axis Type in feature milling and hole making */
            public: enum HoleAxisTypes
            {
                HoleAxisTypesVector/** Vector */,
                HoleAxisTypesRule/** Rule */,
                HoleAxisTypesRuleIfNoVector/** Rule if no vector */
            };

            /** Available types for Hole Depth Type in feature milling and hole making */
            public: enum HoleDepthTypes
            {
                HoleDepthTypesPoint/** Smart Point */,
                HoleDepthTypesRule/** Depth/Rule */
            };

            /** Available types for optimization level in operation */
            public: enum OptimizationLevelTypes
            {
                OptimizationLevelTypesStandard/** standard */,
                OptimizationLevelTypesAdvanced/** advanced */
            };

            /** Available types for optimization based on in operation */
            public: enum OptimizationBasedOnTypes
            {
                OptimizationBasedOnTypesDist/** dist */,
                OptimizationBasedOnTypesOrient/** orient */
            };

            /** Available types for optimization distance method in operation */
            public: enum OptimizationDistanceTypes
            {
                OptimizationDistanceTypesDirect/** direct */,
                OptimizationDistanceTypesTransition/** transition */
            };

            private: OperationBuilderImpl * m_operationbuilder_impl;
            private: friend class  _OperationBuilderBuilder;
            protected: OperationBuilder();
            public: ~OperationBuilder();
            /**Returns  the geometry builder   <br> License requirements : None */
            public: NXOpen::CAM::GeometryCiBuilder * Geometry
            (
            );
            /**Returns  the Retract Distance builder (inheritable double)  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * RetractDistance
            (
            );
            /**Returns  the tool change builder   <br> License requirements : None */
            public: NXOpen::CAM::ToolChangeCiBuilder * ToolChangeSetting
            (
            );
            /**Returns  the Retract Distance on Tool Axis Change builder (inheritable double)  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * RetractDistanceOnToolAxisChange
            (
            );
            /**Returns  the Hole Axis Type   <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::HoleAxisTypes HoleAxisType
            (
            );
            /**Sets  the Hole Axis Type   <br> License requirements : cam_base ("CAM BASE") */
            public: void SetHoleAxisType
            (
                NXOpen::CAM::OperationBuilder::HoleAxisTypes types /** the Hole Axis Type */
            );
            /** Get the Hole Axis values   @return  the Hole Axis values  <br> License requirements : None */
            public: std::vector<double> GetHoleAxisValues
            (
            );
            /** Set the Hole Axis values   <br> License requirements : cam_base ("CAM BASE") */
            public: void SetHoleAxisValues
            (
                const std::vector<double> & holeAxis /** the Hole Axis values  */
            );
            /**Returns  the Hole Depth Type   <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::HoleDepthTypes HoleDepthType
            (
            );
            /**Sets  the Hole Depth Type   <br> License requirements : cam_base ("CAM BASE") */
            public: void SetHoleDepthType
            (
                NXOpen::CAM::OperationBuilder::HoleDepthTypes types /** the Hole Depth Type */
            );
            /**Returns  the optimization level in operation  <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::OptimizationLevelTypes OptimizationLevel
            (
            );
            /**Sets  the optimization level in operation  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOptimizationLevel
            (
                NXOpen::CAM::OperationBuilder::OptimizationLevelTypes optimType /** optimtype */ 
            );
            /**Returns  the optimization based on in operation  <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::OptimizationBasedOnTypes OptimizationBasedOn
            (
            );
            /**Sets  the optimization based on in operation  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOptimizationBasedOn
            (
                NXOpen::CAM::OperationBuilder::OptimizationBasedOnTypes optimBasedOn /** optimbasedon */ 
            );
            /**Returns  the optimization distance method in operation  <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::OptimizationDistanceTypes OptimizationDistanceMethod
            (
            );
            /**Sets  the optimization distance method in operation  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOptimizationDistanceMethod
            (
                NXOpen::CAM::OperationBuilder::OptimizationDistanceTypes optimDistance /** optimdistance */ 
            );
            /**Returns  the max depth distance builder  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * HoleDepth
            (
            );
            /**Returns  the channel's index. This method has been deprecated, use channel_name instead.
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") int Channel
            (
            );
            /**Sets  the channel's index. This method has been deprecated, use channel_name instead.
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : cam_base ("CAM BASE") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetChannel
            (
                int channel /** the channel's index */
            );
            /**Returns  the channel's name  <br> License requirements : None */
            public: NXString ChannelName
            (
            );
            /**Sets  the channel's name  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetChannelName
            (
                const NXString & channel /** the channel's name */
            );
            /**Returns  the user selected tool  <br> License requirements : None */
            public: bool SelectToolFlag
            (
            );
            /**Sets  the user selected tool  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSelectToolFlag
            (
                bool selToolFlag /** the user selected tool */
            );
            /**Returns  the start event builder   <br> License requirements : None */
            public: NXOpen::CAM::PostEventsCiBuilder * StartOfPath
            (
            );
            /**Returns  the end event builder   <br> License requirements : None */
            public: NXOpen::CAM::PostEventsCiBuilder * EndOfPath
            (
            );
            /**Returns  the safe clearance builder   <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * SafeClearance
            (
            );
            /**Returns  the path display options builder   <br> License requirements : None */
            public: NXOpen::CAM::OperationDisplayOptionsBuilder * PathDisplayOptions
            (
            );
            /**Returns  the start ude set  <br> License requirements : None */
            public: NXOpen::CAM::UdeSet * StartUdeSet
            (
            );
            /**Returns  the end ude set  <br> License requirements : None */
            public: NXOpen::CAM::UdeSet * EndUdeSet
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
