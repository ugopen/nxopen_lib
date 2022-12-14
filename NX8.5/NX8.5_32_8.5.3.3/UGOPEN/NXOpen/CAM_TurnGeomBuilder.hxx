#ifndef NXOpen_CAM_TURNGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TURNGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnGeomBuilder.ja
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
#include <NXOpen/CAM_FeatureGeomBuilder.hxx>
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
        class TurnGeomBuilder;
    }
    namespace CAM
    {
        class FeatureGeomBuilder;
    }
    namespace CAM
    {
        class _TurnGeomBuilderBuilder;
        class TurnGeomBuilderImpl;
        /** Represents a TurnGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateTurnGeomBuilder  CAM::NCGroupCollection::CreateTurnGeomBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TurnGeomBuilder : public CAM::FeatureGeomBuilder
        {
            private: TurnGeomBuilderImpl * m_turngeombuilder_impl;
            private: friend class  _TurnGeomBuilderBuilder;
            protected: TurnGeomBuilder();
            public: ~TurnGeomBuilder();
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
