#ifndef NXOpen_CAM_CUTVOLUME_HXX_INCLUDED
#define NXOpen_CAM_CUTVOLUME_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CutVolume.ja
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
#include <NXOpen/SelectObjectList.hxx>
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
        class CutVolume;
    }
    namespace CAM
    {
        class SelectCAMFeatureList;
    }
    namespace CAM
    {
        class _CutVolumeBuilder;
        class CutVolumeImpl;
        /** The classs represent the sub builder for creating cut volume feature items  <br> To create a new instance of this class, use @link NXOpen::CAM::CutVolumeGeom::CreateCutVolume  NXOpen::CAM::CutVolumeGeom::CreateCutVolume @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  CutVolume : public NXOpen::TaggedObject
        {
            private: CutVolumeImpl * m_cutvolume_impl;
            private: friend class  _CutVolumeBuilder;
            protected: CutVolume();
            public: ~CutVolume();
            /**Returns  the selection 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::SelectCAMFeatureList * Selection
            (
            );
            /**Returns  the floor stock 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double FloorStock
            (
            );
            /**Sets  the floor stock 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFloorStock
            (
                double floorStock /** floorstock */ 
            );
            /**Returns  the wall stock 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double WallStock
            (
            );
            /**Sets  the wall stock 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetWallStock
            (
                double wallStock /** wallstock */ 
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
