#ifndef NXOpen_CAM_NCMHOLEMACHININGENGRET_HXX_INCLUDED
#define NXOpen_CAM_NCMHOLEMACHININGENGRET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmHoleMachiningEngRet.ja
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
#include <NXOpen/CAM_NcmHoleMachiningEngRet.hxx>
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
        class NcmHoleMachiningEngRet;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class _NcmHoleMachiningEngRetBuilder;
        class NcmHoleMachiningEngRetImpl;
        /** Represents a builder for an inheritable double value in of a CAM.CAMObject 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NcmHoleMachiningEngRet : public NXOpen::TaggedObject
        {
            /** Available types for engage/retract in Planar Milling */
            public: enum EngRetTypes
            {
                EngRetTypesSameAsDefault/** Same as Default (Inherit) */,
                EngRetTypesSameAsEngage/** Same as Engage*/,
                EngRetTypesHelical/** Helical */,
                EngRetTypesLinear/** Linear */,
                EngRetTypesCircular/** Circular */,
                EngRetTypesNone/** None */,
                EngRetTypesMinimumClearance/** Minimum Clearance */
            };

            private: NcmHoleMachiningEngRetImpl * m_ncmholemachiningengret_impl;
            private: friend class  _NcmHoleMachiningEngRetBuilder;
            protected: NcmHoleMachiningEngRet();
            public: ~NcmHoleMachiningEngRet();
            /**Returns  the type of engage/retract 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachiningEngRet::EngRetTypes EngRetType
            (
            );
            /**Sets  the type of engage/retract 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngRetType
            (
                NXOpen::CAM::NcmHoleMachiningEngRet::EngRetTypes engRetType /** the new value */
            );
            /**Returns  the engage/retract height builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * Height
            (
            );
            /**Returns  the engage/retract min clearance builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * MinClearance
            (
            );
            /**Returns  the engage/retract start at arc center 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool StartFromCenter
            (
            );
            /**Sets  the engage/retract start at arc center 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStartFromCenter
            (
                bool startFromCenter /** the start from center */
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
