#ifndef NXOpen_CAM_WEDMSTATUSCONTROLCIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMSTATUSCONTROLCIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmStatusControlCiBuilder.ja
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
        class WedmStatusControlCiBuilder;
    }
    namespace CAM
    {
        class _WedmStatusControlCiBuilderBuilder;
        class WedmStatusControlCiBuilderImpl;
        /** Represents a WedmStatusControlCiBuilder 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  WedmStatusControlCiBuilder : public NXOpen::TaggedObject
        {
            /** Available types for status control */
            public: enum StatusTypes
            {
                StatusTypesNone/** no control */,
                StatusTypesApproachOnly/** approach only */,
                StatusTypesDepartureOnly/** departure only */,
                StatusTypesApproachAndDeparture/** approach and departure */
            };

            private: WedmStatusControlCiBuilderImpl * m_wedmstatuscontrolcibuilder_impl;
            private: friend class  _WedmStatusControlCiBuilderBuilder;
            protected: WedmStatusControlCiBuilder();
            public: ~WedmStatusControlCiBuilder();
            /**Returns  the Wedm Status Control  Type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::WedmStatusControlCiBuilder::StatusTypes StatusControl
            (
            );
            /**Sets  the Wedm Status Control  Type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStatusControl
            (
                NXOpen::CAM::WedmStatusControlCiBuilder::StatusTypes statusType /** the wedm status control type */
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