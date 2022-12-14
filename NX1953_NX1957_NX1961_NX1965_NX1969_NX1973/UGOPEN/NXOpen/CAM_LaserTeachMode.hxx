#ifndef NXOpen_CAM_LASERTEACHMODE_HXX_INCLUDED
#define NXOpen_CAM_LASERTEACHMODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_LaserTeachMode.ja
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
#include <NXOpen/CAM_OperationBuilder.hxx>
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
        class LaserTeachMode;
    }
    namespace CAM
    {
        class FeedsBuilder;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class NcmLaserEngage;
    }
    namespace CAM
    {
        class NcmLaserRetract;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    namespace CAM
    {
        class _LaserTeachModeBuilder;
        class LaserTeachModeImpl;
        /** Represents a Laser TeachMode  <br> To create a new instance of this class, use @link NXOpen::CAM::OperationCollection::CreateLaserTeachMode  NXOpen::CAM::OperationCollection::CreateLaserTeachMode @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  LaserTeachMode : public NXOpen::CAM::OperationBuilder
        {
            private: LaserTeachModeImpl * m_laserteachmode_impl;
            private: friend class  _LaserTeachModeBuilder;
            protected: LaserTeachMode();
            public: ~LaserTeachMode();
            /**Returns  the feeds and speeds 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::FeedsBuilder * Feeds
            (
            );
            /**Returns  the ncm engage 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmLaserEngage * NcmEngage
            (
            );
            /**Returns  the ncm retract 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmLaserRetract * NcmRetract
            (
            );
            /**Returns  the Overlap Distance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * OverlapDistance
            (
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
