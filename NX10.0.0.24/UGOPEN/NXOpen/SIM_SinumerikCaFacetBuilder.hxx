#ifndef NXOpen_SIM_SINUMERIKCAFACETBUILDER_HXX_INCLUDED
#define NXOpen_SIM_SINUMERIKCAFACETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_SinumerikCaFacetBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SIM_SinumerikCaFacetBuilder.hxx>
#include <NXOpen/libnxopencpp_sim_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace SIM
    {
        class SinumerikCaFacetBuilder;
    }
    class Builder;
    namespace SIM
    {
        class _SinumerikCaFacetBuilderBuilder;
        class SinumerikCaFacetBuilderImpl;
        /** This class is used for set the facet tolerance.
                A call to @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
             <br> Use the @link Part Part@endlink  class to create a SinumerikCaFacetBuilder object.  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_SIMEXPORT  SinumerikCaFacetBuilder : public NXOpen::Builder
        {
            private: SinumerikCaFacetBuilderImpl * m_sinumerikcafacetbuilder_impl;
            private: friend class  _SinumerikCaFacetBuilderBuilder;
            protected: SinumerikCaFacetBuilder();
            public: ~SinumerikCaFacetBuilder();
            /**Returns  the facet tolerance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double FacetTolerance
            (
            );
            /**Sets  the facet tolerance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_sinumerik_ca ("Sinumerik Collision Avoidance") */
            public: void SetFacetTolerance
            (
                double tolerance /** tolerance */ 
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