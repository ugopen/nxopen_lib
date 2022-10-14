#ifndef NXOpen_CAM_FINISHTURNING_HXX_INCLUDED
#define NXOpen_CAM_FINISHTURNING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FinishTurning.ja
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
#include <NXOpen/CAM_RoughFinishTurning.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class FinishTurning;
    }
    namespace CAM
    {
        class RoughFinishTurning;
    }
    namespace CAM
    {
        class _FinishTurningBuilder;
        class FinishTurningImpl;
        /** Represents a Turn Finishing operation */
        class NXOPENCPPEXPORT  FinishTurning : public CAM::RoughFinishTurning
        {
            private: FinishTurningImpl * m_finishturning_impl;
            private: friend class  _FinishTurningBuilder;
            protected: FinishTurning();
            public: ~FinishTurning();
        };
    }
}
#undef EXPORTLIBRARY
#endif