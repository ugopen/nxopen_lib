#ifndef NXOpen_CAM_MOVETOPOINTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MOVETOPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MoveToPointBuilder.ja
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
#include <NXOpen/CAM_MoveToPointBuilder.hxx>
#include <NXOpen/CAM_RoundPointBuilder.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MoveToPointBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class RoundPointBuilder;
    }
    class Point;
    namespace CAM
    {
        class _MoveToPointBuilderBuilder;
        /** Represents the Move To Point Builder  <br> To create a new instance of this class, use @link CAM::MoveCollection::CreateMoveToPointBuilder CAM::MoveCollection::CreateMoveToPointBuilder@endlink  <br> */
        class NXOPENCPPEXPORT MoveToPointBuilder : public CAM::MoveBuilder
        {
            private: friend class  _MoveToPointBuilderBuilder;
            protected: MoveToPointBuilder();
            /**Returns  the location  <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the location  <br> License requirements : None */
            public: void SetPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the round point builder  <br> License requirements : None */
            public: NXOpen::CAM::RoundPointBuilder * RoundPoint
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
