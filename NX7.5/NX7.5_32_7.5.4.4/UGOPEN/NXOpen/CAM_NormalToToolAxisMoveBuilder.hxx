#ifndef NXOpen_CAM_NORMALTOTOOLAXISMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NORMALTOTOOLAXISMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NormalToToolAxisMoveBuilder.ja
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
#include <NXOpen/CAM_NormalToToolAxisMoveBuilder.hxx>
#include <NXOpen/CAM_RoundPointBuilder.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class NormalToToolAxisMoveBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class RoundPointBuilder;
    }
    class Direction;
    class Point;
    namespace CAM
    {
        class _NormalToToolAxisMoveBuilderBuilder;
        class NormalToToolAxisMoveBuilderImpl;
        /** Represents the Move To Point Builder  <br> To create a new instance of this class, use @link CAM::MoveCollection::CreateNormalToToolAxisMoveBuilder CAM::MoveCollection::CreateNormalToToolAxisMoveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  NormalToToolAxisMoveBuilder : public CAM::MoveBuilder
        {
            /** the normal orientation */
            public: enum Orientation
            {
                OrientationAlongVector/** Along Vector */,
                OrientationTowardsPoint/** Towards Point */
            };

            private: NormalToToolAxisMoveBuilderImpl * m_normaltotoolaxismovebuilder_impl;
            private: friend class  _NormalToToolAxisMoveBuilderBuilder;
            protected: NormalToToolAxisMoveBuilder();
            public: ~NormalToToolAxisMoveBuilder();
            /**Returns  the normal type  <br> License requirements : None */
            public: NXOpen::CAM::NormalToToolAxisMoveBuilder::Orientation MoveType
            (
            );
            /**Sets  the normal type  <br> License requirements : None */
            public: void SetMoveType
            (
                NXOpen::CAM::NormalToToolAxisMoveBuilder::Orientation normaltype /** normaltype */ 
            );
            /**Returns  the point in normal direction <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the point in normal direction <br> License requirements : None */
            public: void SetPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the vector  <br> License requirements : None */
            public: NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector  <br> License requirements : None */
            public: void SetVector
            (
                NXOpen::Direction * vec /** vec */ 
            );
            /**Returns  the distance  <br> License requirements : None */
            public: double Distance
            (
            );
            /**Sets  the distance  <br> License requirements : None */
            public: void SetDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the angle  <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the angle  <br> License requirements : None */
            public: void SetAngle
            (
                double distance /** distance */ 
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