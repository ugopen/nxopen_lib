#ifndef NXOpen_CAM_FLOWBUILDER_HXX_INCLUDED
#define NXOpen_CAM_FLOWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FlowBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class FlowBuilder;
    }
    namespace CAM
    {
        class CutPatternBuilder;
    }
    namespace CAM
    {
        class FlowCutSteepContainment;
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
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class StepoverBuilder;
    }
    namespace CAM
    {
        class _FlowBuilderBuilder;
        class FlowBuilderImpl;
        /** Represents a FlowBuilder Builder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT  FlowBuilder : public TaggedObject
        {
            /** Available types for Flow Cut/Sequencing in scop  
             @deprecated Deprecated in NX7.5.0 <br> 
            */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") enum FlowSequenceType
            {
                FlowSequenceTypeInsideOut/**Inside-Out*/,
                FlowSequenceTypeOutsideIn/**Outside-In*/,
                FlowSequenceTypeSteepLast/**STEEP Last*/,
                FlowSequenceTypeSteepFirst/**STEEP First*/,
                FlowSequenceTypeInsideOutAlternate/**Inside-Out Alternate*/,
                FlowSequenceTypeOutsideInAlternate/**Outside-In Alternate*/
            };

            /** Available types for Flow Cut/Offset Mode in scop  */
            public: enum FlowOffsetModeType
            {
                FlowOffsetModeTypeSingle/**Single Pass*/,
                FlowOffsetModeTypeMultiple/**Multiple Offsets*/,
                FlowOffsetModeTypeReftool/**Reference Tool Offsets*/
            };

            /** Available types for Flow Cut/Cut Method in scop  
             @deprecated Deprecated in NX7.5.0 <br> 
            */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") enum FlowCutMethodType
            {
                FlowCutMethodTypeZigzag/**Zig-Zag*/,
                FlowCutMethodTypeZig/**Zig*/,
                FlowCutMethodTypeZigzagWithLift/**Zig-Zag with Lifts*/
            };

            /** Available types for Flow Cut/Cut Direction in scop  
             @deprecated Deprecated in NX7.5.0 <br> 
            */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") enum FlowCutDirectionType
            {
                FlowCutDirectionTypeMixed/**Mixed*/,
                FlowCutDirectionTypeClimb/**Climb*/,
                FlowCutDirectionTypeConventional/**Conventional*/
            };

            /** Available types for Steep Steep Containment in scop  
             @deprecated Deprecated in NX7.5.0 <br> 
            */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") enum FlowSteepContainmentTypes
            {
                FlowSteepContainmentTypesNone/**None*/,
                FlowSteepContainmentTypesSteep/**Steep*/,
                FlowSteepContainmentTypesNoneSteep/**None Steep*/
            };

            /** Available types for Flow Cut/Steep Cut Direct in scop  
             @deprecated Deprecated in NX7.5.0 <br> 
            */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") enum FlowSteepCutDirectType
            {
                FlowSteepCutDirectTypeMixed/**Mixed*/,
                FlowSteepCutDirectTypeHighToLow/**High to Low*/,
                FlowSteepCutDirectTypeLowToHigh/**Low to High*/
            };

            /** Available types for Flow Cut/Manual Assembly in scop  */
            public: enum FlowEditTypes
            {
                FlowEditTypesAutomatic/** Automatic */,
                FlowEditTypesUserDefined/** User Defined*/
            };

            private: FlowBuilderImpl * m_flowbuilder_impl;
            private: friend class  _FlowBuilderBuilder;
            protected: FlowBuilder();
            public: ~FlowBuilder();
            /**Returns  the flow max concavity  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * MaxConcavityAngleBuilder
            (
            );
            /**Returns  the flow min cut length  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * MinCutLengthBuilder
            (
            );
            /**Returns  the builder of flow merge distance <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * MergeDistBuilder
            (
            );
            /**Returns  the Flow Cut/Cut Method 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::FlowBuilder::FlowCutMethodType FlowCutMethod
            (
            );
            /**Sets  the Flow Cut/Cut Method 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetFlowCutMethod
            (
                NXOpen::CAM::FlowBuilder::FlowCutMethodType flowCutMethod /** the Flow Cut/Offset Mode value */
            );
            /**Returns  the builder of flow stepover distance which is obsolete
             @deprecated Deprecated in NX6.0.0 <br> 
             <br> License requirements : cam_base ("CAM BASE") */
            public:  NX_DEPRECATED("Deprecated in NX6.0.0") NXOpen::CAM::InheritableDoubleBuilder * StepoverDistBuilder
            (
            );
            /**Returns  the builder of flow cut stepover
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::StepoverBuilder * StepoverBuilder
            (
            );
            /**Returns  the flow number of offset builder (inheritable int) 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::InheritableIntBuilder * OffsetsNumBuilder
            (
            );
            /**Returns  the Flow Cut/Sequencing 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::FlowBuilder::FlowSequenceType FlowSequence
            (
            );
            /**Sets  the Flow Cut/Sequencing 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetFlowSequence
            (
                NXOpen::CAM::FlowBuilder::FlowSequenceType flowSequence /** the Flow Cut/Sequencing value */
            );
            /**Returns  the Flow Cut/Offset Mode  <br> License requirements : None */
            public: NXOpen::CAM::FlowBuilder::FlowOffsetModeType FlowOffsetMode
            (
            );
            /**Sets  the Flow Cut/Offset Mode  <br> License requirements : None */
            public: void SetFlowOffsetMode
            (
                NXOpen::CAM::FlowBuilder::FlowOffsetModeType flowOffsetMode /** the Flow Cut/Offset Mode value */
            );
            /**Returns  the Flow Cut/Cut Direction 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::FlowBuilder::FlowCutDirectionType FlowCutDirection
            (
            );
            /**Sets  the Flow Cut/Cut Direction 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetFlowCutDirection
            (
                NXOpen::CAM::FlowBuilder::FlowCutDirectionType flowCutDirection /** the Flow Cut/Offset Mode value */
            );
            /**Returns  the Cleanup Output, Contact Boundary   <br> License requirements : None */
            public: bool ContactBnd
            (
            );
            /**Sets  the Cleanup Output, Contact Boundary   <br> License requirements : None */
            public: void SetContactBnd
            (
                bool contactBnd /** the Contact Boundary value */
            );
            /**Returns  the Cleanup Output, Tool End Boundary   <br> License requirements : None */
            public: bool CenterCurve
            (
            );
            /**Sets  the Cleanup Output, Tool End Boundary   <br> License requirements : None */
            public: void SetCenterCurve
            (
                bool centerCurve /** the Tool End Boundary value */
            );
            /**Returns  the flow reference tool diameter  <br> License requirements : None */
            public: double TlDiameter
            (
            );
            /**Sets  the flow reference tool diameter  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTlDiameter
            (
                double tlDiameter /** The flow reference tool diameter */
            );
            /**Returns  the flow overlap distance  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * FlowOverlapDistBuilder
            (
            );
            /**Returns  the Manual Assembly  <br> License requirements : None */
            public: NXOpen::CAM::FlowBuilder::FlowEditTypes FlowEdit
            (
            );
            /**Sets  the Manual Assembly  <br> License requirements : None */
            public: void SetFlowEdit
            (
                NXOpen::CAM::FlowBuilder::FlowEditTypes flowEdit /** the Manual Assembly value */
            );
            /**Returns  the option,  Flow Cut: Steep Containment
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::FlowBuilder::FlowSteepContainmentTypes FlowcutSteepOpt
            (
            );
            /**Sets  the option,  Flow Cut: Steep Containment
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetFlowcutSteepOpt
            (
                NXOpen::CAM::FlowBuilder::FlowSteepContainmentTypes flowcutSteepOpt /** the value of  Steep Containment */
            );
            /**Returns  the Steep Angle  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * SteepAngleBuilder
            (
            );
            /**Returns  the Flow Cut/Steep Cut Direct 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::FlowBuilder::FlowSteepCutDirectType FlowSteepCutDirect
            (
            );
            /**Sets  the Flow Cut/Steep Cut Direct 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetFlowSteepCutDirect
            (
                NXOpen::CAM::FlowBuilder::FlowSteepCutDirectType flowSteepCutDirect /** the Flow Cut/Steep Cut Direct value */
            );
            /**Returns  the cut pattern builder 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::CutPatternBuilder * CutPatternBuilder
            (
            );
            /**Returns  the Non-steep Cutting Builder  <br> License requirements : None */
            public: NXOpen::CAM::FlowCutSteepContainment * NonSteepCutting
            (
            );
            /**Returns  the Steep Cutting Builder  <br> License requirements : None */
            public: NXOpen::CAM::FlowCutSteepContainment * SteepCutting
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif