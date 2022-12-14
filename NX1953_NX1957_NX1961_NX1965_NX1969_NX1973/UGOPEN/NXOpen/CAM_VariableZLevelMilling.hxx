#ifndef NXOpen_CAM_VARIABLEZLEVELMILLING_HXX_INCLUDED
#define NXOpen_CAM_VARIABLEZLEVELMILLING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_VariableZLevelMilling.ja
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
#include <NXOpen/CAM_PlanarOperation.hxx>
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
        class VariableZLevelMilling;
    }
    namespace CAM
    {
        class PlanarOperation;
    }
    namespace CAM
    {
        class _VariableZLevelMillingBuilder;
        class VariableZLevelMillingImpl;
        /** Represents a Variable Z Level Milling Operation  <br> To create or edit an instance of this class, use @link NXOpen::CAM::VazlMillingBuilder  NXOpen::CAM::VazlMillingBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  VariableZLevelMilling : public NXOpen::CAM::PlanarOperation
        {
            private: VariableZLevelMillingImpl * m_variablezlevelmilling_impl;
            private: friend class  _VariableZLevelMillingBuilder;
            protected: VariableZLevelMilling();
            public: ~VariableZLevelMilling();
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
