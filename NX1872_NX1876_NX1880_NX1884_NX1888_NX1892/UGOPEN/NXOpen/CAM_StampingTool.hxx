#ifndef NXOpen_CAM_STAMPINGTOOL_HXX_INCLUDED
#define NXOpen_CAM_STAMPINGTOOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_StampingTool.ja
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
#include <NXOpen/CAM_SolidToolBuilder.hxx>
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
        class StampingTool;
    }
    namespace CAM
    {
        class SolidToolBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _StampingToolBuilder;
        class StampingToolImpl;
        /** Represents a stamping tool builder  <br> To create a new instance of this class, use @link NXOpen::CAM::NCGroupCollection::CreateStampingTool  NXOpen::CAM::NCGroupCollection::CreateStampingTool @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  StampingTool : public NXOpen::CAM::SolidToolBuilder
        {
            private: StampingToolImpl * m_stampingtool_impl;
            private: friend class  _StampingToolBuilder;
            protected: StampingTool();
            public: ~StampingTool();
            /** Adds one geometry element to the cutting geometry 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void AddCuttingGeometry
            (
                NXOpen::NXObject * geometry /** geometry */ 
            );
            /** Removes all geometry elements from of cutting geometry 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void RemoveAllCuttingGeometry
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
