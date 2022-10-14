#ifndef NXOpen_CAM_INSPECTIONGROUP_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionGroup.ja
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
#include <NXOpen/CAM_CAMObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionGroup;
    }
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class _InspectionGroupBuilder;
        class InspectionGroupImpl;
        /** Represents a group for CMM Inspection <br> To obtain an instance of this class us @link CAM::InspectionGroupCollection CAM::InspectionGroupCollection@endlink  <br> */
        class NXOPENCPPEXPORT  InspectionGroup : public CAM::CAMObject
        {
            private: InspectionGroupImpl * m_inspectiongroup_impl;
            private: friend class  _InspectionGroupBuilder;
            protected: InspectionGroup();
            public: ~InspectionGroup();
        };
    }
}
#undef EXPORTLIBRARY
#endif