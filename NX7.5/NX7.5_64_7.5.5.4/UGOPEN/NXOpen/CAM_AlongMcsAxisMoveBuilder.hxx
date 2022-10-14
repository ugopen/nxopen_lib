#ifndef NXOpen_CAM_ALONGMCSAXISMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_ALONGMCSAXISMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_AlongMcsAxisMoveBuilder.ja
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
#include <NXOpen/CAM_AlongMcsAxisMoveBuilder.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class AlongMcsAxisMoveBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class _AlongMcsAxisMoveBuilderBuilder;
        class AlongMcsAxisMoveBuilderImpl;
        /** Represents Along MCS Axis Move Builder  <br> To create a new instance of this class, use @link CAM::MoveCollection::CreateAlongMcsAxisMoveBuilder CAM::MoveCollection::CreateAlongMcsAxisMoveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  AlongMcsAxisMoveBuilder : public CAM::MoveBuilder
        {
            private: AlongMcsAxisMoveBuilderImpl * m_alongmcsaxismovebuilder_impl;
            private: friend class  _AlongMcsAxisMoveBuilderBuilder;
            protected: AlongMcsAxisMoveBuilder();
            public: ~AlongMcsAxisMoveBuilder();
            /**Returns  the delta x  <br> License requirements : None */
            public: double XAxis
            (
            );
            /**Sets  the delta x  <br> License requirements : None */
            public: void SetXAxis
            (
                double axisPosition /** axis position */ 
            );
            /**Returns  the delta y  <br> License requirements : None */
            public: double YAxis
            (
            );
            /**Sets  the delta y  <br> License requirements : None */
            public: void SetYAxis
            (
                double axisPosition /** axis position */ 
            );
            /**Returns  the delta z  <br> License requirements : None */
            public: double ZAxis
            (
            );
            /**Sets  the delta z  <br> License requirements : None */
            public: void SetZAxis
            (
                double axisPosition /** axis position */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif