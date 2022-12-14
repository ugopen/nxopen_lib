#ifndef NXOpen_MOTION_ADVANCEDSOLUTION_HXX_INCLUDED
#define NXOpen_MOTION_ADVANCEDSOLUTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_AdvancedSolution.ja
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
#include <NXOpen/Motion_MotionSolution.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class AdvancedSolution;
    }
    namespace Motion
    {
        class MotionSolution;
    }
    namespace Motion
    {
        class _AdvancedSolutionBuilder;
        class AdvancedSolutionImpl;
        /** Represents a @link Motion::AdvancedSolution Motion::AdvancedSolution@endlink . This class
                exposes the Advanced Solution Element.  <br> To create or edit an instance of this class, use @link NXOpen::Motion::AdvancedSolutionBuilder  NXOpen::Motion::AdvancedSolutionBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  AdvancedSolution : public NXOpen::Motion::MotionSolution
        {
            private: AdvancedSolutionImpl * m_advancedsolution_impl;
            private: friend class  _AdvancedSolutionBuilder;
            protected: AdvancedSolution();
            public: ~AdvancedSolution();
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
