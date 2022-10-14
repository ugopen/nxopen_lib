#ifndef NXOpen_CAM_CYCLECOOLANT_HXX_INCLUDED
#define NXOpen_CAM_CYCLECOOLANT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CycleCoolant.ja
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
        class CycleCoolant;
    }
    namespace CAM
    {
        class _CycleCoolantBuilder;
        class CycleCoolantImpl;
        /** Represets a User Defined Event 
         <br>  Created in NX10.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  CycleCoolant : public NXOpen::TaggedObject
        {
            /** Available types for coolant flow mode */
            public: enum Flow
            {
                FlowLow/** coolant flow low */,
                FlowMedium/** coolant flow medium */,
                FlowHight/** coolant flow high */
            };

            private: CycleCoolantImpl * m_cyclecoolant_impl;
            private: friend class  _CycleCoolantBuilder;
            protected: CycleCoolant();
            public: ~CycleCoolant();
            /**Returns  the coolant status 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: bool IsActive
            (
            );
            /**Sets  the coolant status 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetActive
            (
                bool bActive /** the coolant mode status */
            );
            /**Returns  the coolant mode 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXString Coolant
            (
            );
            /**Sets  the coolant mode 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCoolant
            (
                const NXString & strCoolant /** the coolant mode */
            );
            /**Sets  the coolant mode 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetCoolant
            (
                const char * strCoolant /** the coolant mode */
            );
            /**Returns  the flow status 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: bool FlowIsActive
            (
            );
            /**Sets  the flow status 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFlowIsActive
            (
                bool bActive /** the flow mode status */
            );
            /**Returns  the flow mode 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleCoolant::Flow FlowMode
            (
            );
            /**Sets  the flow mode 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFlowMode
            (
                NXOpen::CAM::CycleCoolant::Flow coolant /** the coolant flow */
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