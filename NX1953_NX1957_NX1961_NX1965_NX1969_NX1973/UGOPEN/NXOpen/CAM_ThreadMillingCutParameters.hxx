#ifndef NXOpen_CAM_THREADMILLINGCUTPARAMETERS_HXX_INCLUDED
#define NXOpen_CAM_THREADMILLINGCUTPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ThreadMillingCutParameters.ja
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
#include <NXOpen/CAM_CylindricalMillingCutParameters.hxx>
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
        class ThreadMillingCutParameters;
    }
    namespace CAM
    {
        class CylindricalMillingCutParameters;
    }
    namespace CAM
    {
        class _ThreadMillingCutParametersBuilder;
        class ThreadMillingCutParametersImpl;
        /** Represents a ThreadMillingCutParameters Builder 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ThreadMillingCutParameters : public NXOpen::CAM::CylindricalMillingCutParameters
        {
            /** cut direction options 
             <br>  Created in NX7.5.0.  <br>  
            */
            public: enum CutDirectionTypes
            {
                CutDirectionTypesClimb/** Climb cut */,
                CutDirectionTypesConventional/** Conventional cut */
            };

            private: ThreadMillingCutParametersImpl * m_threadmillingcutparameters_impl;
            private: friend class  _ThreadMillingCutParametersBuilder;
            protected: ThreadMillingCutParameters();
            public: ~ThreadMillingCutParameters();
            /**Returns  the cut direction 
             <br>  @deprecated Deprecated in NX9.0.2.  Use @link CAM::FeatureMillingCutParameters::CuttingDirection CAM::FeatureMillingCutParameters::CuttingDirection@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX9.0.2.  Use CAM::FeatureMillingCutParameters::CuttingDirection instead.") NXOpen::CAM::ThreadMillingCutParameters::CutDirectionTypes CutDirection
            (
            );
            /**Sets  the cut direction 
             <br>  @deprecated Deprecated in NX9.0.2.  Use @link CAM::FeatureMillingCutParameters::SetCuttingDirection CAM::FeatureMillingCutParameters::SetCuttingDirection@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NX_DEPRECATED("Deprecated in NX9.0.2.  Use CAM::FeatureMillingCutParameters::SetCuttingDirection instead.") void SetCutDirection
            (
                NXOpen::CAM::ThreadMillingCutParameters::CutDirectionTypes cutDir /** the cut directon type */
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