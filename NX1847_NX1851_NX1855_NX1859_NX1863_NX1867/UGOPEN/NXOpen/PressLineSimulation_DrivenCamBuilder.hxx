#ifndef NXOpen_PRESSLINESIMULATION_DRIVENCAMBUILDER_HXX_INCLUDED
#define NXOpen_PRESSLINESIMULATION_DRIVENCAMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PressLineSimulation_DrivenCamBuilder.ja
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
#include <NXOpen/libpresslinesimulopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PressLineSimulation
    {
        class DrivenCamBuilder;
    }
    class Builder;
    namespace PressLineSimulation
    {
        class _DrivenCamBuilderBuilder;
        class DrivenCamBuilderImpl;
        /** Represents a PressLineSimulation.DrivenCam builder. It is an abstract class
                and cannot be instantiated.  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class PRESSLINESIMULOPENCPPEXPORT  DrivenCamBuilder : public NXOpen::Builder
        {
            private: DrivenCamBuilderImpl * m_drivencambuilder_impl;
            private: friend class  _DrivenCamBuilderBuilder;
            protected: DrivenCamBuilder();
            public: ~DrivenCamBuilder();
            /**Returns  the cam collision faceting tolerance. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: double CamCollisionFacetingTolerance
            (
            );
            /**Sets  the cam collision faceting tolerance. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") OR nx_pls_line_setup (" NX Press Line Setup") */
            public: void SetCamCollisionFacetingTolerance
            (
                double camCollisionFacetingTolerance /** camcollisionfacetingtolerance */ 
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
