#ifndef NXOpen_CAM_TTOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TTOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TToolBuilder.ja
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
#include <NXOpen/CAM_MillingToolBuilder.hxx>
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
        class TToolBuilder;
    }
    namespace CAM
    {
        class MillingToolBuilder;
    }
    namespace CAM
    {
        class _TToolBuilderBuilder;
        class TToolBuilderImpl;
        /** Represents a T Tool Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateTToolBuilder  CAM::NCGroupCollection::CreateTToolBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TToolBuilder : public CAM::MillingToolBuilder
        {
            private: TToolBuilderImpl * m_ttoolbuilder_impl;
            private: friend class  _TToolBuilderBuilder;
            protected: TToolBuilder();
            public: ~TToolBuilder();
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
