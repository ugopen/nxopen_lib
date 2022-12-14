#ifndef NXOpen_CAM_TEACHMODETURNING_HXX_INCLUDED
#define NXOpen_CAM_TEACHMODETURNING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TeachmodeTurning.ja
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
#include <NXOpen/CAM_TurningOperation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class TeachmodeTurning;
    }
    namespace CAM
    {
        class TurningOperation;
    }
    namespace CAM
    {
        class _TeachmodeTurningBuilder;
        class TeachmodeTurningImpl;
        /** Represents a Turning Teachmode operation */
        class NXOPENCPPEXPORT  TeachmodeTurning : public CAM::TurningOperation
        {
            private: TeachmodeTurningImpl * m_teachmodeturning_impl;
            private: friend class  _TeachmodeTurningBuilder;
            protected: TeachmodeTurning();
            public: ~TeachmodeTurning();
        };
    }
}
#undef EXPORTLIBRARY
#endif
