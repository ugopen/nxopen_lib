#ifndef NXOpen_CAM_DRILLCHAMFERBORINGBARTOOL_HXX_INCLUDED
#define NXOpen_CAM_DRILLCHAMFERBORINGBARTOOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DrillChamferBoringBarTool.ja
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
#include <NXOpen/CAM_DrillChamferBoringBarTool.hxx>
#include <NXOpen/CAM_DrillBoringBarTool.hxx>
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
        class DrillChamferBoringBarTool;
    }
    namespace CAM
    {
        class DrillBoringBarTool;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class _DrillChamferBoringBarToolBuilder;
        class DrillChamferBoringBarToolImpl;
        /** Represents a Chamfer Boring Bar Tool Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::NCGroupCollection::CreateDrillChamferBoringBarTool  NXOpen::CAM::NCGroupCollection::CreateDrillChamferBoringBarTool @endlink  <br> 
         <br>  Created in NX11.0.1.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  DrillChamferBoringBarTool : public NXOpen::CAM::DrillBoringBarTool
        {
            private: DrillChamferBoringBarToolImpl * m_drillchamferboringbartool_impl;
            private: friend class  _DrillChamferBoringBarToolBuilder;
            protected: DrillChamferBoringBarTool();
            public: ~DrillChamferBoringBarTool();
            /**Returns  the Upper Corner Radius  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * UpperCornerRadius
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