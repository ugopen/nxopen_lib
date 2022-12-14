#ifndef NXOpen_CAM_TURNORIENTWCS_HXX_INCLUDED
#define NXOpen_CAM_TURNORIENTWCS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnOrientWcs.ja
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
        class TurnOrientWcs;
    }
    namespace CAM
    {
        class _TurnOrientWcsBuilder;
        class TurnOrientWcsImpl;
        /** Represents an Turn Orient Wcs Builder  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TurnOrientWcs : public NXOpen::TaggedObject
        {
            /** the XC mapping types*/
            public: enum XcMappingTypes
            {
                XcMappingTypesSpindleAxis/** Map XC to  ZM or  XM of the MCS */,
                XcMappingTypesReversedSpindleAxis/** Map XC to -ZM or -XM of the MCS */,
                XcMappingTypesRadialAxis/** Map XC to  XM or  YM of the MCS */,
                XcMappingTypesReversedRadialAxis/** Map XC to -XM or -YM of the MCS */
            };

            /** the YC mapping types*/
            public: enum YcMappingTypes
            {
                YcMappingTypesRadialAxis/** Map YC to  XM or  YM of the MCS */,
                YcMappingTypesReversedRadialAxis/** Map YC to -XM or -YM of the MCS */,
                YcMappingTypesSpindleAxis/** Map YC to  ZM or  XM of the MCS */,
                YcMappingTypesReversedSpindleAxis/** Map YC to -ZM or -XM of the MCS */
            };

            private: TurnOrientWcsImpl * m_turnorientwcs_impl;
            private: friend class  _TurnOrientWcsBuilder;
            protected: TurnOrientWcs();
            public: ~TurnOrientWcs();
            /**Returns  the offset of the WCS origin 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double WcsOffset
            (
            );
            /**Sets  the offset of the WCS origin 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetWcsOffset
            (
                double wcsOffset /** Offset of the WCS origin along the spindle axis*/
            );
            /**Returns  the XC mapping 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnOrientWcs::XcMappingTypes XcMapping
            (
            );
            /**Sets  the XC mapping 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetXcMapping
            (
                NXOpen::CAM::TurnOrientWcs::XcMappingTypes xcMapping /** XC mapping to an MCS axis */
            );
            /**Returns  the YC mapping 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnOrientWcs::YcMappingTypes YcMapping
            (
            );
            /**Sets  the YC mapping 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetYcMapping
            (
                NXOpen::CAM::TurnOrientWcs::YcMappingTypes ycMapping /** YC mapping to an MCS axis */
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
