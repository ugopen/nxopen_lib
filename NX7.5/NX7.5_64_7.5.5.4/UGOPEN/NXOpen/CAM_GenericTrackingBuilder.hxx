#ifndef NXOpen_CAM_GENERICTRACKINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_GENERICTRACKINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_GenericTrackingBuilder.ja
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
#include <NXOpen/CAM_SolidTrackingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class GenericTrackingBuilder;
    }
    namespace CAM
    {
        class SolidTrackingBuilder;
    }
    namespace CAM
    {
        class _GenericTrackingBuilderBuilder;
        class GenericTrackingBuilderImpl;
        /** Represents a GenericTracking Builder  <br> To create a new instance of this class, use @link CAM::Tool::CreateGenericTrackingBuilder CAM::Tool::CreateGenericTrackingBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  GenericTrackingBuilder : public CAM::SolidTrackingBuilder
        {
            private: GenericTrackingBuilderImpl * m_generictrackingbuilder_impl;
            private: friend class  _GenericTrackingBuilderBuilder;
            protected: GenericTrackingBuilder();
            public: ~GenericTrackingBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif