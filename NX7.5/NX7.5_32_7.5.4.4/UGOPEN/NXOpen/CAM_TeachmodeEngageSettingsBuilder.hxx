#ifndef NXOpen_CAM_TEACHMODEENGAGESETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TEACHMODEENGAGESETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TeachmodeEngageSettingsBuilder.ja
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
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class TeachmodeEngageSettingsBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class TurnEngageRetractBuilder;
    }
    namespace CAM
    {
        class _TeachmodeEngageSettingsBuilderBuilder;
        class TeachmodeEngageSettingsBuilderImpl;
        /** Represents a TeachmodeEngageSettingsBuilder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreateTeachmodeTurningBuilder CAM::OperationCollection::CreateTeachmodeTurningBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  TeachmodeEngageSettingsBuilder : public CAM::MoveBuilder
        {
            private: TeachmodeEngageSettingsBuilderImpl * m_teachmodeengagesettingsbuilder_impl;
            private: friend class  _TeachmodeEngageSettingsBuilderBuilder;
            protected: TeachmodeEngageSettingsBuilder();
            public: ~TeachmodeEngageSettingsBuilder();
            /**Returns  the engage parameters builder  <br> License requirements : None */
            public: NXOpen::CAM::TurnEngageRetractBuilder * EngageBuilder
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif