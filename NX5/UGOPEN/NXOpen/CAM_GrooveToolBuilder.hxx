#ifndef NXOpen_CAM_GROOVETOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_GROOVETOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_GrooveToolBuilder.ja
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
#include <NXOpen/CAM_TurningToolBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class GrooveToolBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class TurningToolBuilder;
    }
    namespace CAM
    {
        class _GrooveToolBuilderBuilder;
        /** Represents a Groove tool builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateGrooveToolBuilder CAM::NCGroupCollection::CreateGrooveToolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT GrooveToolBuilder : public CAM::TurningToolBuilder
        {
            /** The available insert shapes for groove tools */
            public: enum InsertShapes
            {
                InsertShapesStd/** Standard groove tool */,
                InsertShapesFnr/** Full nose radius groove tool */,
                InsertShapesRtj/** Ring type joint groove tool */,
                InsertShapesUser/** user defined groove tool */
            };

            /** The available holder hand options for groove tools */
            public: enum HolderHands
            {
                HolderHandsLeft0/** Left hand, 0 degrees */,
                HolderHandsLeft90/** Left hand, 90 degrees */,
                HolderHandsRight0/** Right hand, 0 degrees */,
                HolderHandsRight90/** Right hand, 90 degrees */
            };

            private: friend class  _GrooveToolBuilderBuilder;
            protected: GrooveToolBuilder();
            /**Returns  the insert shape  <br> License requirements : None */
            public: NXOpen::CAM::GrooveToolBuilder::InsertShapes InsertShape
            (
            );
            /**Sets  the insert shape  <br> License requirements : None */
            public: void SetInsertShape
            (
                NXOpen::CAM::GrooveToolBuilder::InsertShapes insertShape /** insertshape */ 
            );
            /**Returns  the radius builder (inheritable double)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * RadiusBuilder
            (
            );
            /**Returns  the left radius builder (inheritable double)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * LeftRadiusBuilder
            (
            );
            /**Returns  the right radius builder (inheritable double)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * RightRadiusBuilder
            (
            );
            /**Returns  the side angle builder (inheritable double)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * SideAngleBuilder
            (
            );
            /**Returns  the tip angle builder (inheritable double)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * TipAngleBuilder
            (
            );
            /**Returns  the holder hand  <br> License requirements : None */
            public: NXOpen::CAM::GrooveToolBuilder::HolderHands HolderHand
            (
            );
            /**Sets  the holder hand  <br> License requirements : None */
            public: void SetHolderHand
            (
                NXOpen::CAM::GrooveToolBuilder::HolderHands holderHand /** holderhand */ 
            );
            /**Returns  the holder insert extension builder (inheritable double) for groove tools  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * HolderInsertExtensionBuilder
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif