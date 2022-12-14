#ifndef NXOpen_CAM_ALONGTOOLAXISMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_ALONGTOOLAXISMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_AlongToolAxisMoveBuilder.ja
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
#include <NXOpen/CAM_AlongToolAxisMoveBuilder.hxx>
#include <NXOpen/CAM_RoundPointBuilder.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class AlongToolAxisMoveBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class RoundPointBuilder;
    }
    namespace CAM
    {
        class _AlongToolAxisMoveBuilderBuilder;
        class AlongToolAxisMoveBuilderImpl;
        /** Represents the Move To Point Builder  <br> To create a new instance of this class, use @link CAM::MoveCollection::CreateAlongToolAxisMoveBuilder CAM::MoveCollection::CreateAlongToolAxisMoveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  AlongToolAxisMoveBuilder : public CAM::MoveBuilder
        {
            private: AlongToolAxisMoveBuilderImpl * m_alongtoolaxismovebuilder_impl;
            private: friend class  _AlongToolAxisMoveBuilderBuilder;
            protected: AlongToolAxisMoveBuilder();
            public: ~AlongToolAxisMoveBuilder();
            /**Returns  the location  <br> License requirements : None */
            public: double Distance
            (
            );
            /**Sets  the location  <br> License requirements : None */
            public: void SetDistance
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
