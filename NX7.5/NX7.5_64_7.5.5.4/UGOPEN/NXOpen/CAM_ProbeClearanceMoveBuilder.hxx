#ifndef NXOpen_CAM_PROBECLEARANCEMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PROBECLEARANCEMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ProbeClearanceMoveBuilder.ja
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
#include <NXOpen/CAM_ProbeClearanceMoveBuilder.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ProbeClearanceMoveBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class NcmClearanceBuilder;
    }
    namespace CAM
    {
        class _ProbeClearanceMoveBuilderBuilder;
        class ProbeClearanceMoveBuilderImpl;
        /** Represents the Probe Clearance Move Builder  <br> To create a new instance of this class, use @link CAM::MoveCollection::CreateProbeClearanceMoveBuilder CAM::MoveCollection::CreateProbeClearanceMoveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ProbeClearanceMoveBuilder : public CAM::MoveBuilder
        {
            private: ProbeClearanceMoveBuilderImpl * m_probeclearancemovebuilder_impl;
            private: friend class  _ProbeClearanceMoveBuilderBuilder;
            protected: ProbeClearanceMoveBuilder();
            public: ~ProbeClearanceMoveBuilder();
            /**Returns  the NCM clearance builder  <br> License requirements : None */
            public: NXOpen::CAM::NcmClearanceBuilder * ClearanceBuilder
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif