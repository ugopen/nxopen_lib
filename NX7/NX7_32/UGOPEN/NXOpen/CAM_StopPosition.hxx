#ifndef NXOpen_CAM_STOPPOSITION_HXX_INCLUDED
#define NXOpen_CAM_STOPPOSITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_StopPosition.ja
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
#include <NXOpen/CAM_StopPosition.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class StopPosition;
    }
    class Point;
    namespace CAM
    {
        class _StopPositionBuilder;
        /** Represents a stop position */
        class NXOPENCPPEXPORT StopPosition : public TaggedObject
        {
            /** the stop at options */
            public: enum Types
            {
                TypesNone/** Stop At mode: Off */,
                TypesDistance/** Stop At mode: Distance */,
                TypesPercentage/** Stop At mode: Percentage */,
                TypesPoint/** Stop At mode: Point */
            };

            private: friend class  _StopPositionBuilder;
            protected: StopPosition();
            /**Returns  the stop at mode  <br> License requirements : None */
            public: NXOpen::CAM::StopPosition::Types Type
            (
            );
            /**Sets  the stop at mode  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetType
            (
                NXOpen::CAM::StopPosition::Types stopAtMode /** stopatmode */ 
            );
            /**Returns  the stop at distance  <br> License requirements : None */
            public: double Distance
            (
            );
            /**Sets  the stop at distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDistance
            (
                double stopAtDistance /** stopatdistance */ 
            );
            /**Returns  the stop at percentage  <br> License requirements : None */
            public: double Percentage
            (
            );
            /**Sets  the stop at percentage  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPercentage
            (
                double stopAtPercentage /** stopatpercentage */ 
            );
            /**Returns  the stop at point  <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the stop at point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPoint
            (
                NXOpen::Point * stopAtPoint /** the stop at point */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif