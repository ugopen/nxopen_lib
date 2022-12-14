#ifndef NXOpen_CAM_INSPECTIONMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionMoveBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAM_InspectionMoveBuilder.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionMoveBuilder;
    }
    class Builder;
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class _InspectionMoveBuilderBuilder;
        /** Represents CMM Inspection Move Builder  <br> This cannot be instantiated <br> */
        class NXOPENCPPEXPORT InspectionMoveBuilder : public Builder
        {
            /** the tip angle selection mode */
            public: enum TipAngleEnum
            {
                TipAngleEnumAuto/** Auto specify */,
                TipAngleEnumSpecify/** Manual specify*/
            };

            private: friend class  _InspectionMoveBuilderBuilder;
            protected: InspectionMoveBuilder();
            /** Set parent  <br> License requirements : None */
            public: void SetParent
            (
                NXOpen::CAM::CAMObject * parent /** the parent object */
            );
            /** Set sibling  <br> License requirements : None */
            public: void SetSibling
            (
                NXOpen::CAM::CAMObject * sibling /** the sibling object */
            );
            /**Returns  the motion type  <br> License requirements : None */
            public: NXOpen::CAM::MoveBuilder::Motion MotionType
            (
            );
            /**Sets  the motion type  <br> License requirements : None */
            public: void SetMotionType
            (
                NXOpen::CAM::MoveBuilder::Motion motionType /** motion type */ 
            );
            /**Returns  the probe tip number  <br> License requirements : None */
            public: int TipNumber
            (
            );
            /**Sets  the probe tip number  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetTipNumber
            (
                int tipNumber /** tipnumber */ 
            );
            /**Returns  the tip angle selection mode  <br> License requirements : None */
            public: NXOpen::CAM::InspectionMoveBuilder::TipAngleEnum TipAngleMode
            (
            );
            /**Sets  the tip angle selection mode  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetTipAngleMode
            (
                NXOpen::CAM::InspectionMoveBuilder::TipAngleEnum tipAngleMode /** tipanglemode */ 
            );
            /**Returns  the A angle for an indexable head  <br> License requirements : None */
            public: double AngleA
            (
            );
            /**Sets  the A angle for an indexable head  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngleA
            (
                double angle /** angle */ 
            );
            /**Returns  the B angle for an indexable head  <br> License requirements : None */
            public: double AngleB
            (
            );
            /**Sets  the B angle for an indexable head  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngleB
            (
                double angle /** angle */ 
            );
            /**Returns  the approach distance  <br> License requirements : None */
            public: double ApproachDistance
            (
            );
            /**Sets  the approach distance  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetApproachDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the retract distance  <br> License requirements : None */
            public: double RetractDistance
            (
            );
            /**Sets  the retract distance  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetRetractDistance
            (
                double distance /** distance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
