#ifndef NXOpen_CAM_HOLEMACHININGCUTPARAMETERS_HXX_INCLUDED
#define NXOpen_CAM_HOLEMACHININGCUTPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_HoleMachiningCutParameters.ja
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
#include <NXOpen/CAM_CutParameters.hxx>
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
        class HoleMachiningCutParameters;
    }
    namespace CAM
    {
        class CutParameters;
    }
    namespace CAM
    {
        class _HoleMachiningCutParametersBuilder;
        class HoleMachiningCutParametersImpl;
        /** Represents a HoleMachiningCutParameters Builder  <br> This is an abstract class and cannot be instantiated.  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  HoleMachiningCutParameters : public CAM::CutParameters
        {
            private: HoleMachiningCutParametersImpl * m_holemachiningcutparameters_impl;
            private: friend class  _HoleMachiningCutParametersBuilder;
            protected: HoleMachiningCutParameters();
            public: ~HoleMachiningCutParameters();
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