#ifndef NXOpen_CAM_MILLMACHINECONTROLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MILLMACHINECONTROLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillMachineControlBuilder.ja
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
#include <NXOpen/CAM_UdeSet.hxx>
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
        class MillMachineControlBuilder;
    }
    namespace CAM
    {
        class FeedsBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    namespace CAM
    {
        class UdeSet;
    }
    namespace CAM
    {
        class _MillMachineControlBuilderBuilder;
        class MillMachineControlBuilderImpl;
        /** Represents a MillMachineControl Builder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreateMillMachineControlBuilder  CAM::OperationCollection::CreateMillMachineControlBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MillMachineControlBuilder : public CAM::OperationBuilder
        {
            private: MillMachineControlBuilderImpl * m_millmachinecontrolbuilder_impl;
            private: friend class  _MillMachineControlBuilderBuilder;
            protected: MillMachineControlBuilder();
            public: ~MillMachineControlBuilder();
            /**Returns  the feeds and speeds builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::FeedsBuilder * FeedsBuilder
            (
            );
            /**Returns  the ude set 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::UdeSet * UdeSet
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