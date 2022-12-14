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
#include <NXOpen/CAM_Notes.hxx>
#include <NXOpen/CAM_UdeSet.hxx>
#include <NXOpen/CAM_ParamBuilder.hxx>
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
        class OperationBuilder;
    }
    namespace CAM
    {
        class ArcOutputTypeCiBuilder;
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
        class LayoutCiBuilder;
    }
    namespace CAM
    {
        class Notes;
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
        class ToolPathEditorBuilder;
    }
    namespace CAM
    {
        class ToolPathSplitParametersBuilder;
    }
    namespace CAM
    {
        class UdeSet;
    }
    namespace CAM
    {
        class _OperationBuilderBuilder;
        class OperationBuilderImpl;
        /** Represents a Opr Builder  <br> This is an abstract class, and cannot be instantiated.  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ToolPathEditor.DeltaXC </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ToolPathEditor.DeltaYC </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ToolPathEditor.DeltaZC </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ToolPathEditor.ExtendMethod </td> <td> 
         
        Linear </td> </tr> 

        <tr><td> 
         
        ToolPathEditor.GougeCheckClearanceMethod </td> <td> 
         
        Specify </td> </tr> 

        <tr><td> 
         
        ToolPathEditor.HolderCheck </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ToolPathEditor.MotionMethod </td> <td> 
         
        Delta </td> </tr> 

        <tr><td> 
         
        ToolPathEditor.MoveStartPoint </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ToolPathEditor.TransformCircles </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  OperationBuilder : public NXOpen::CAM::ParamBuilder
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
            /**Returns  the geometry builder  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::GeometryCiBuilder * Geometry
            (
            );
            /**Returns  the Retract Distance builder (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * RetractDistance
            (
            );
            /**Returns  the tool change builder  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolChangeCiBuilder * ToolChangeSetting
            (
            );
            /**Returns  the Retract Distance on Tool Axis Change builder (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * RetractDistanceOnToolAxisChange
            (
            );
            /**Returns  the Hole Axis Type  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::HoleAxisTypes HoleAxisType
            (
            );
            /**Sets  the Hole Axis Type  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetHoleAxisType
            (
                NXOpen::CAM::OperationBuilder::HoleAxisTypes types /** the Hole Axis Type */
            );
            /** Get the Hole Axis values   @return  the Hole Axis values 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetHoleAxisValues
            (
            );
            /** Set the Hole Axis values  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetHoleAxisValues
            (
                const std::vector<double> & holeAxis /** the Hole Axis values  */
            );
            /**Returns  the Hole Depth Type  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::HoleDepthTypes HoleDepthType
            (
            );
            /**Sets  the Hole Depth Type  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetHoleDepthType
            (
                NXOpen::CAM::OperationBuilder::HoleDepthTypes types /** the Hole Depth Type */
            );
            /**Returns  the optimization level in operation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::OptimizationLevelTypes OptimizationLevel
            (
            );
            /**Sets  the optimization level in operation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOptimizationLevel
            (
                NXOpen::CAM::OperationBuilder::OptimizationLevelTypes optimType /** optimtype */ 
            );
            /**Returns  the optimization based on in operation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::OptimizationBasedOnTypes OptimizationBasedOn
            (
            );
            /**Sets  the optimization based on in operation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOptimizationBasedOn
            (
                NXOpen::CAM::OperationBuilder::OptimizationBasedOnTypes optimBasedOn /** optimbasedon */ 
            );
            /**Returns  the optimization distance method in operation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::OperationBuilder::OptimizationDistanceTypes OptimizationDistanceMethod
            (
            );
            /**Sets  the optimization distance method in operation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOptimizationDistanceMethod
            (
                NXOpen::CAM::OperationBuilder::OptimizationDistanceTypes optimDistance /** optimdistance */ 
            );
            /**Returns  the max depth distance builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * HoleDepth
            (
            );
            /**Returns  the channel's name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ChannelName
            (
            );
            /**Sets  the channel's name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetChannelName
            (
                const NXString & channel /** the channel's name */
            );
            /**Sets  the channel's name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetChannelName
            (
                const char * channel /** the channel's name */
            );
            /**Returns  the user selected tool 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool SelectToolFlag
            (
            );
            /**Sets  the user selected tool 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSelectToolFlag
            (
                bool selToolFlag /** the user selected tool */
            );
            /**Returns  the start event builder  
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::PostEventsCiBuilder * StartOfPath
            (
            );
            /**Returns  the end event builder  
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::PostEventsCiBuilder * EndOfPath
            (
            );
            /**Returns  the safe clearance builder  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * SafeClearance
            (
            );
            /**Returns  the path display options builder  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::OperationDisplayOptionsBuilder * PathDisplayOptions
            (
            );
            /**Returns  the start ude set 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::UdeSet * StartUdeSet
            (
            );
            /**Returns  the end ude set 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::UdeSet * EndUdeSet
            (
            );
            /**Returns  the motion output builder 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ArcOutputTypeCiBuilder * MotionOutputBuilder
            (
            );
            /**Returns  the notes builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Notes * Notes
            (
            );
            /**Returns  the description  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXString Description
            (
            );
            /**Sets  the description  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDescription
            (
                const NXString & description /**  the description*/
            );
            /**Sets  the description  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetDescription
            (
                const char * description /**  the description*/
            );
            /**Returns  the tool path split Parameters  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolPathSplitParametersBuilder * ToolPathSplitParametersBuilder
            (
            );
            /**Returns  the gouge checking flag 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool GougeChecking
            (
            );
            /**Sets  the gouge checking flag 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetGougeChecking
            (
                bool gougeChecking /** the Gouge Checking Flag */
            );
            /**Returns  the Layer and Layout 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LayoutCiBuilder * LayoutAndLayer
            (
            );
            /**Returns  the environment variable that points to the post tool path generation library which has the exit 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXString PostToolPathExit
            (
            );
            /**Sets  the environment variable that points to the post tool path generation library which has the exit 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPostToolPathExit
            (
                const NXString & exitName /**  the environment variable that points to the post tool path generation library */
            );
            /**Sets  the environment variable that points to the post tool path generation library which has the exit 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetPostToolPathExit
            (
                const char * exitName /**  the environment variable that points to the post tool path generation library */
            );
            /**Returns  the Tool Path Editor Builder
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolPathEditorBuilder * ToolPathEditor
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
