#ifndef NXOpen_CAM_INSPECTIONTOOL_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONTOOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionTool.ja
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
#include <NXOpen/CAM_InspectionGroup.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class InspectionTool;
    }
    namespace CAM
    {
        class InspectionGroup;
    }
    namespace CAM
    {
        class InspectionProbeTrackingBuilder;
    }
    namespace CAM
    {
        class InspectionTrackPointCollection;
    }
    namespace CAM
    {
        class ProbeTrackPoint;
    }
    namespace CAM
    {
        class ProbeTrackingBuilder;
    }
    namespace CAM
    {
        class _InspectionToolBuilder;
        class InspectionToolImpl;
        /** Represents an Inspection group  <br> To obtain an instance of this class use @link CAM::InspectionGroupCollection CAM::InspectionGroupCollection@endlink   <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionTool : public NXOpen::CAM::InspectionGroup
        {
            private: InspectionToolImpl * m_inspectiontool_impl;
            private: friend class  _InspectionToolBuilder;
            protected: InspectionTool();
            public: ~InspectionTool();
            /** Creates a Probe Trackpoint builder  @return  probe trackpoint builder created 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::ProbeTrackingBuilder * CreateProbeTrackingBuilder
            (
                NXOpen::CAM::ProbeTrackPoint * csoObject /** probe tracking point to be edited */
            );
            /** Creates a Probe Trackpoint builder  @return  probe trackpoint builder created 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionProbeTrackingBuilder * CreateInspectionProbeTrackingBuilder
            (
                NXOpen::CAM::ProbeTrackPoint * csoObject /** probe tracking point to be edited */
            );


            /** Returns the CMMInspectionTrackPointCollection 
             <br>  Created in NX7.0.0.  <br>  
            */
            public: NXOpen::CAM::InspectionTrackPointCollection *CMMInspectionTrackPointCollection();
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif