#ifndef NXOpen_CAM_DPMITPBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DPMITPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DPMItpBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/CAM_ParamBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class DPMItpBuilder;
    }
    namespace CAM
    {
        class CutPatternBuilder;
    }
    namespace CAM
    {
        class ParamBuilder;
    }
    namespace CAM
    {
        class StepoverBuilder;
    }
    class SectionList;
    namespace CAM
    {
        class _DPMItpBuilderBuilder;
        /** Represents an DPMItp Builder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreateDpmitpBuilder CAM::OperationCollection::CreateDpmitpBuilder@endlink  <br> */
        class NXOPENCPPEXPORT DPMItpBuilder : public CAM::ParamBuilder
        {
            /** Enum of selection method */
            public: enum SelectionMethodOption
            {
                SelectionMethodOptionAutomatic/** automatic  */,
                SelectionMethodOptionSpecify/** specify */
            };

            /** Enum of tool position */
            public: enum ToolPositionOption
            {
                ToolPositionOptionOn/** On position */,
                ToolPositionOptionTanto/** Tanto position */,
                ToolPositionOptionContact/** Contact position */
            };

            /** Enum of cut type */
            public: enum CutTypeOption
            {
                CutTypeOptionZig/** Zig cut type */,
                CutTypeOptionZigzag/** Zigzag cut type */,
                CutTypeOptionZigzagWithLifts/** Zigzag with lift cut type */,
                CutTypeOptionSpiralHelix/** Spiral/helix cut type */
            };

            /** Enum of step method */
            public: enum StepMethodOption
            {
                StepMethodOptionPoints/** points */ ,
                StepMethodOptionTolerance/** tolerance */ 
            };

            /** Enum of stepover type */
            public: enum StepoverTypeOption
            {
                StepoverTypeOptionNumber/** stepover number */,
                StepoverTypeOptionDistance/** stepover distance */,
                StepoverTypeOptionScallop/** stepover scallop height */
            };

            private: friend class  _DPMItpBuilderBuilder;
            protected: DPMItpBuilder();
            /**Returns  the flow and cross selection method  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::DPMItpBuilder::SelectionMethodOption SelectionMethod
            (
            );
            /**Sets  the flow and cross selection method  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSelectionMethod
            (
                NXOpen::CAM::DPMItpBuilder::SelectionMethodOption selectionMethod /** the selection method value */
            );
            /**Returns  the tool position  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::DPMItpBuilder::ToolPositionOption ToolPosition
            (
            );
            /**Sets  the tool position  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolPosition
            (
                NXOpen::CAM::DPMItpBuilder::ToolPositionOption toolPosition /** the tool position value */
            );
            /**Returns  the cut type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::DPMItpBuilder::CutTypeOption CutType
            (
            );
            /**Sets  the cut type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutType
            (
                NXOpen::CAM::DPMItpBuilder::CutTypeOption cutType /** the cut type value */
            );
            /**Returns  the stepover type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::DPMItpBuilder::StepoverTypeOption StepoverType
            (
            );
            /**Sets  the stepover type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepoverType
            (
                NXOpen::CAM::DPMItpBuilder::StepoverTypeOption stepoverType /** the stepover type value */
            );
            /**Returns  the stepover number  <br> License requirements : cam_base ("CAM BASE") */
            public: int StepoverNum
            (
            );
            /**Sets  the stepover number  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepoverNum
            (
                int stepoverNum /** the stepover number value */
            );
            /**Returns  the stepover distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double StepoverDis
            (
            );
            /**Sets  the stepover distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepoverDis
            (
                double stepoverDis /** the stepover distance value */
            );
            /**Returns  the stepover scallop height  <br> License requirements : cam_base ("CAM BASE") */
            public: double StepoverScallopHeight
            (
            );
            /**Sets  the stepover scallop height  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepoverScallopHeight
            (
                double stepoverScallopHeight /** the stepover scallop height value */
            );
            /**Returns  the stepover builder  <br> License requirements : None */
            public: NXOpen::CAM::StepoverBuilder * StepoverBuilder
            (
            );
            /**Returns  the cut pattern builder  <br> License requirements : None */
            public: NXOpen::CAM::CutPatternBuilder * CutPatternBuilder
            (
            );
            /** Get the extend values  @return  the extend values  <br> License requirements : cam_base ("CAM BASE") */
            public: std::vector<double> GetExtendValues
            (
            );
            /** Set the extend values  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetExtendValues
            (
                const std::vector<double> & values /** the extend value */
            );
            /** Preview drive path  <br> License requirements : cam_base ("CAM BASE") */
            public: void MPreview
            (
            );
            /**Returns  the Flow Curve List <br> License requirements : None */
            public: NXOpen::SectionList * FlowCurveList
            (
            );
            /**Returns  the Cross Curve List  <br> License requirements : None */
            public: NXOpen::SectionList * CrossCurveList
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
