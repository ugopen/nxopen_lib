#ifndef NXOpen_CAM_MINCUTDEPTH_HXX_INCLUDED
#define NXOpen_CAM_MINCUTDEPTH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MinCutDepth.ja
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
        class MinCutDepth;
    }
    namespace CAM
    {
        class _MinCutDepthBuilder;
        class MinCutDepthImpl;
        /**
            Represents a @link NXOpen::CAM::MinCutDepth NXOpen::CAM::MinCutDepth@endlink 
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MinCutDepth : public NXOpen::TaggedObject
        {
            /** the mininmum cut depth options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum Types
            {
                TypesNone/** None */,
                TypesSpecify/** Specify */
            };

            private: MinCutDepthImpl * m_mincutdepth_impl;
            private: friend class  _MinCutDepthBuilder;
            protected: MinCutDepth();
            public: ~MinCutDepth();
            /**Returns  the Minimum Cut Depth status 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::MinCutDepth::Types Status
            (
            );
            /**Sets  the Minimum Cut Depth status 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStatus
            (
                NXOpen::CAM::MinCutDepth::Types status /** the Minimum Cut Depth status */
            );
            /**Returns  the distance of Minimum Cut Depth  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double Distance
            (
            );
            /**Sets  the distance of Minimum Cut Depth  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDistance
            (
                double distance /** the distance of Minimum Cut Depth */
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
