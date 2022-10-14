#ifndef NXOpen_CAE_CAEREGION_HXX_INCLUDED
#define NXOpen_CAE_CAEREGION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CaeRegion.ja
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
#include <NXOpen/CAE_NamedPropTableWithTargetSet.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class CaeRegion;
    }
    namespace CAE
    {
        class NamedPropTableWithTargetSet;
    }
    namespace CAE
    {
        class _CaeRegionBuilder;
        class CaeRegionImpl;
        /**  @brief  Represents a cae region object  

          */
        class NXOPENCPPEXPORT  CaeRegion : public CAE::NamedPropTableWithTargetSet
        {
            private: CaeRegionImpl * m_caeregion_impl;
            private: friend class  _CaeRegionBuilder;
            protected: CaeRegion();
            public: ~CaeRegion();
            /**Returns  the name of the region descriptor  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString DescriptorName
            (
            );
            /** prints information for a @link CAE::CaeRegion CAE::CaeRegion@endlink   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Information
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif