#ifndef NXOpen_CAM_MILLTOOLPROBINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MILLTOOLPROBINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillToolProbingBuilder.ja
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
        class MillToolProbingBuilder;
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
        class ProbeParamsBuilder;
    }
    namespace CAM
    {
        class _MillToolProbingBuilderBuilder;
        class MillToolProbingBuilderImpl;
        /** Represents a Mill Tool Probing Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::OperationCollection::CreateMillToolProbingBuilder  NXOpen::CAM::OperationCollection::CreateMillToolProbingBuilder @endlink  <br> 
         <br>  Created in NX8.5.1.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MillToolProbingBuilder : public NXOpen::CAM::OperationBuilder
        {
            private: MillToolProbingBuilderImpl * m_milltoolprobingbuilder_impl;
            private: friend class  _MillToolProbingBuilderBuilder;
            protected: MillToolProbingBuilder();
            public: ~MillToolProbingBuilder();
            /**Returns  the feeds and speeds builder 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::FeedsBuilder * FeedsBuilder
            (
            );
            /**Returns  the probe parameter builder 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeParamsBuilder * ProbeParamsBuilder
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
