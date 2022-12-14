#ifndef NXOpen_CAE_ADAPTIVITYEXCLUSIONZONEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ADAPTIVITYEXCLUSIONZONEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AdaptivityExclusionZoneBuilder.ja
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
#include <NXOpen/CAE_AdaptivityExclusionZoneBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class AdaptivityExclusionZoneBuilder;
    }
    class Builder;
    namespace CAE
    {
        class PropertyTable;
    }
    namespace CAE
    {
        class _AdaptivityExclusionZoneBuilderBuilder;
        class AdaptivityExclusionZoneBuilderImpl;
        /**
            Builds a @link NXOpen::CAE::AdaptivityExclusionZone NXOpen::CAE::AdaptivityExclusionZone@endlink  object which 
            represets adaptivity meta solution related exclusion zones. 
             <br> To create a new instance of this class, use @link NXOpen::CAE::AdaptivityExclusionZoneCollection::CreateExclusionZoneBuilder  NXOpen::CAE::AdaptivityExclusionZoneCollection::CreateExclusionZoneBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AdaptivityExclusionZoneBuilder : public NXOpen::Builder
        {
            private: AdaptivityExclusionZoneBuilderImpl * m_adaptivityexclusionzonebuilder_impl;
            private: friend class  _AdaptivityExclusionZoneBuilderBuilder;
            protected: AdaptivityExclusionZoneBuilder();
            public: ~AdaptivityExclusionZoneBuilder();
            /**Returns  the adaptivity property table 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PropertyTable * PropertyTable
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
