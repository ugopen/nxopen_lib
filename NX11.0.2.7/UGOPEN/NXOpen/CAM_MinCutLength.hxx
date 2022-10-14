#ifndef NXOpen_CAM_MINCUTLENGTH_HXX_INCLUDED
#define NXOpen_CAM_MINCUTLENGTH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MinCutLength.ja
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
#include <NXOpen/CAM_MinCutLength.hxx>
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
        class MinCutLength;
    }
    namespace CAM
    {
        class _MinCutLengthBuilder;
        class MinCutLengthImpl;
        /**
            Represents a @link NXOpen::CAM::MinCutLength NXOpen::CAM::MinCutLength@endlink 
            */
        class NXOPENCPP_CAMEXPORT  MinCutLength : public NXOpen::TaggedObject
        {
            /** the mininmum cut length options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum Types
            {
                TypesNone/** None */,
                TypesSpecify/** Specify */
            };

            private: MinCutLengthImpl * m_mincutlength_impl;
            private: friend class  _MinCutLengthBuilder;
            protected: MinCutLength();
            public: ~MinCutLength();
            /**Returns  the status of Minimum Cut Length 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::MinCutLength::Types Status
            (
            );
            /**Sets  the status of Minimum Cut Length 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStatus
            (
                NXOpen::CAM::MinCutLength::Types minLength /** the the status of Minimum Cut Length */
            );
            /**Returns  the distance of Minimum Cut Length  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double Distance
            (
            );
            /**Sets  the distance of Minimum Cut Length  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDistance
            (
                double minLength /** the distance of Minimum Cut Length */
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