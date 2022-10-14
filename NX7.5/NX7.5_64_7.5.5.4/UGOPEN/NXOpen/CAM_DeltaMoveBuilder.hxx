#ifndef NXOpen_CAM_DELTAMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DELTAMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DeltaMoveBuilder.ja
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
#include <NXOpen/CAM_DeltaMoveBuilder.hxx>
#include <NXOpen/CAM_RoundPointBuilder.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class DeltaMoveBuilder;
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
        class _DeltaMoveBuilderBuilder;
        class DeltaMoveBuilderImpl;
        /** Represents the Delta Move Builder  <br> To create a new instance of this class, use @link CAM::MoveCollection::CreateDeltaMoveBuilder CAM::MoveCollection::CreateDeltaMoveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  DeltaMoveBuilder : public CAM::MoveBuilder
        {
            /** Move Intent */
            public: enum IntentType
            {
                IntentTypeWcs/** WCS */,
                IntentTypeMcs/** MCS */
            };

            private: DeltaMoveBuilderImpl * m_deltamovebuilder_impl;
            private: friend class  _DeltaMoveBuilderBuilder;
            protected: DeltaMoveBuilder();
            public: ~DeltaMoveBuilder();
            /**Returns  the delta x  <br> License requirements : None */
            public: double DeltaX
            (
            );
            /**Sets  the delta x  <br> License requirements : None */
            public: void SetDeltaX
            (
                double deltaValue /** delta value */ 
            );
            /**Returns  the delta y  <br> License requirements : None */
            public: double DeltaY
            (
            );
            /**Sets  the delta y  <br> License requirements : None */
            public: void SetDeltaY
            (
                double deltaValue /** delta value */ 
            );
            /**Returns  the delta z  <br> License requirements : None */
            public: double DeltaZ
            (
            );
            /**Sets  the delta z  <br> License requirements : None */
            public: void SetDeltaZ
            (
                double deltaValue /** delta value */ 
            );
            /**Returns  the intent  <br> License requirements : None */
            public: NXOpen::CAM::DeltaMoveBuilder::IntentType Intent
            (
            );
            /**Sets  the intent  <br> License requirements : None */
            public: void SetIntent
            (
                NXOpen::CAM::DeltaMoveBuilder::IntentType intent /** intent */ 
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