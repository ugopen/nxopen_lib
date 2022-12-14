#ifndef NXOpen_CAM_THREADTURNINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_THREADTURNINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ThreadTurningBuilder.ja
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
#include <NXOpen/CAM_TurningOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ThreadTurningBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class NcmTurnThreadBuilder;
    }
    namespace CAM
    {
        class ThreadCutParameters;
    }
    namespace CAM
    {
        class TurningOperationBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _ThreadTurningBuilderBuilder;
        /** Represents a ThreadTurning Builder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreateThreadTurningBuilder CAM::OperationCollection::CreateThreadTurningBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ThreadTurningBuilder : public CAM::TurningOperationBuilder
        {
            /** the Depth Option types*/
            public: enum DepthOptionTypes
            {
                DepthOptionTypesRootLine/** Root Line */,
                DepthOptionTypesDepthAndAngle/** Depth and Angle */
            };

            private: friend class  _ThreadTurningBuilderBuilder;
            protected: ThreadTurningBuilder();
            /**Returns  the Crest Line  <br> License requirements : None */
            public: NXOpen::NXObject * CrestLine
            (
            );
            /**Sets  the Crest Line  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCrestLine
            (
                NXOpen::NXObject * crestLine /** the Crest Line tag*/
            );
            /**Returns  the Crest Line Direction(Start and End Points) <br> License requirements : None */
            public: bool CrestLineDirection
            (
            );
            /**Sets  the Crest Line Direction(Start and End Points) <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCrestLineDirection
            (
                bool crestLineDirection /** the Crest Line Direction tag*/
            );
            /**Returns  the Start Offset <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * StartOffset
            (
            );
            /**Returns  the End Offset <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * EndOffset
            (
            );
            /**Returns  the crest offset builder <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * CrestOffset
            (
            );
            /**Returns  the root offset <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * RootOffset
            (
            );
            /**Returns  the depth option  <br> License requirements : None */
            public: NXOpen::CAM::ThreadTurningBuilder::DepthOptionTypes DepthOption
            (
            );
            /**Sets  the depth option  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDepthOption
            (
                NXOpen::CAM::ThreadTurningBuilder::DepthOptionTypes depthOption /** the depth option */
            );
            /**Returns  the Root Line  <br> License requirements : None */
            public: NXOpen::NXObject * RootLine
            (
            );
            /**Sets  the Root Line  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRootLine
            (
                NXOpen::NXObject * rootLine /** the Root Line tag*/
            );
            /**Returns  the Total Depth <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * TotalDepth
            (
            );
            /**Returns  the thread angle  <br> License requirements : None */
            public: double ThreadAngle
            (
            );
            /**Sets  the thread angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetThreadAngle
            (
                double threadAngle /** the thread angle */
            );
            /**Returns  the End Line  <br> License requirements : None */
            public: NXOpen::NXObject * EndLine
            (
            );
            /**Sets  the End Line  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEndLine
            (
                NXOpen::NXObject * endLine /** the End Line tag*/
            );
            /**Returns  the non-cutting builder <br> License requirements : None */
            public: NXOpen::CAM::NcmTurnThreadBuilder * NonCuttingBuilder
            (
            );
            /**Returns  the cut parameter object <br> License requirements : None */
            public: NXOpen::CAM::ThreadCutParameters * CutParameters
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
