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
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Represents a T Tool Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateTToolBuilder CAM::NCGroupCollection::CreateTToolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  TToolBuilder : public CAM::MillingToolBuilder
        {
            private: TToolBuilderImpl * m_ttoolbuilder_impl;
            private: friend class  _TToolBuilderBuilder;
            protected: TToolBuilder();
            public: ~TToolBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif