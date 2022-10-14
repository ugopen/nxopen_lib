#ifndef NXOpen_CAM_CIRCULARABOUTAXISMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CIRCULARABOUTAXISMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CircularAboutAxisMoveBuilder.ja
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
#include <NXOpen/CAM_CircularAboutAxisMoveBuilder.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class CircularAboutAxisMoveBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    class Direction;
    class Point;
    namespace CAM
    {
        class _CircularAboutAxisMoveBuilderBuilder;
        /** Represents the Circular Move To Point Builder  <br> To create a new instance of this class, use @link CAM::MoveCollection::CreateCircularAboutAxisMoveBuilder CAM::MoveCollection::CreateCircularAboutAxisMoveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CircularAboutAxisMoveBuilder : public CAM::MoveBuilder
        {
            /** the axis type */
            public: enum AxisType
            {
                AxisTypeTool/** Tool Axis */,
                AxisTypeVector/** Vector */
            };

            /** the motion end type */
            public: enum EndType
            {
                EndTypeAngle/** Angle */,
                EndTypePoint/** Point */
            };

            /** the extension type */
            public: enum ExtensionType
            {
                ExtensionTypeAngle/** Angle */,
                ExtensionTypeDistance/** Distance */
            };

            private: friend class  _CircularAboutAxisMoveBuilderBuilder;
            protected: CircularAboutAxisMoveBuilder();
            /**Returns  the center  <br> License requirements : None */
            public: NXOpen::Point * CenterPoint
            (
            );
            /**Sets  the center  <br> License requirements : None */
            public: void SetCenterPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the axis type  <br> License requirements : None */
            public: NXOpen::CAM::CircularAboutAxisMoveBuilder::AxisType ArcAxisType
            (
            );
            /**Sets  the axis type  <br> License requirements : None */
            public: void SetArcAxisType
            (
                NXOpen::CAM::CircularAboutAxisMoveBuilder::AxisType axisType /** axistype */ 
            );
            /**Returns  the arc axis  <br> License requirements : None */
            public: NXOpen::Direction * ArcAxis
            (
            );
            /**Sets  the arc axis  <br> License requirements : None */
            public: void SetArcAxis
            (
                NXOpen::Direction * vec /** vec */ 
            );
            /**Returns  the arc end type   <br> License requirements : None */
            public: NXOpen::CAM::CircularAboutAxisMoveBuilder::EndType MotionEndType
            (
            );
            /**Sets  the arc end type   <br> License requirements : None */
            public: void SetMotionEndType
            (
                NXOpen::CAM::CircularAboutAxisMoveBuilder::EndType arcEndType /** arcendtype */ 
            );
            /**Returns  the sweep angle  <br> License requirements : None */
            public: double SweepAngle
            (
            );
            /**Sets  the sweep angle  <br> License requirements : None */
            public: void SetSweepAngle
            (
                double sweepAngle /** sweepangle */ 
            );
            /**Returns  the arc end point  <br> License requirements : None */
            public: NXOpen::Point * EndPoint
            (
            );
            /**Sets  the arc end point  <br> License requirements : None */
            public: void SetEndPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the arc extension type   <br> License requirements : None */
            public: NXOpen::CAM::CircularAboutAxisMoveBuilder::ExtensionType ArcExtendMethod
            (
            );
            /**Sets  the arc extension type   <br> License requirements : None */
            public: void SetArcExtendMethod
            (
                NXOpen::CAM::CircularAboutAxisMoveBuilder::ExtensionType arcExtendMethod /** arcextendmethod */ 
            );
            /**Returns  the extend angle  <br> License requirements : None */
            public: double ExtendAngle
            (
            );
            /**Sets  the extend angle  <br> License requirements : None */
            public: void SetExtendAngle
            (
                double extendAngle /** extendangle */ 
            );
            /**Returns  the extend distance  <br> License requirements : None */
            public: double ExtendDistance
            (
            );
            /**Sets  the extend distance  <br> License requirements : None */
            public: void SetExtendDistance
            (
                double extendDistance /** extenddistance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif