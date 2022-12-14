#ifndef NXOpen_CAM_CYCLENODRAGCLEARANCE_HXX_INCLUDED
#define NXOpen_CAM_CYCLENODRAGCLEARANCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CycleNodragClearance.ja
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
#include <NXOpen/CAM_CycleNodragClearance.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class CycleNodragClearance;
    }
    namespace CAM
    {
        class _CycleNodragClearanceBuilder;
        class CycleNodragClearanceImpl;
        /** Represets a User Defined Event 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  CycleNodragClearance : public NXOpen::TaggedObject
        {
            private: CycleNodragClearanceImpl * m_cyclenodragclearance_impl;
            private: friend class  _CycleNodragClearanceBuilder;
            protected: CycleNodragClearance();
            public: ~CycleNodragClearance();
            /**Returns  the Nodrag Clearance status 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: bool IsActive
            (
            );
            /**Sets  the Nodrag Clearance status 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetActive
            (
                bool bActive /** the Nodrag Clearance active status */
            );
            /**Returns  the Nodrag Clearance value 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: double NodragValue
            (
            );
            /**Sets  the Nodrag Clearance value 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetNodragValue
            (
                double doubleValue /** the Nodrag Clearance value */
            );
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
