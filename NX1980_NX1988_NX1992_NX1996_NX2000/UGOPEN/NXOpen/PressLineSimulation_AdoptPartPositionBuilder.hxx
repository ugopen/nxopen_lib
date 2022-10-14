#ifndef NXOpen_PRESSLINESIMULATION_ADOPTPARTPOSITIONBUILDER_HXX_INCLUDED
#define NXOpen_PRESSLINESIMULATION_ADOPTPARTPOSITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PressLineSimulation_AdoptPartPositionBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
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
        class AdoptPartPositionBuilder;
    }
    namespace Assemblies
    {
        class Component;
    }
    namespace Assemblies
    {
        class SelectComponent;
    }
    class Builder;
    namespace PressLineSimulation
    {
        class IDynamicTransformProvider;
    }
    namespace PressLineSimulation
    {
        class _AdoptPartPositionBuilderBuilder;
        class AdoptPartPositionBuilderImpl;
        /** This is the AdoptPartPositionBuilder. In this application the part transport is simulated by blanking 
            and unblanking parts at the right time and right position. To easily adopt the position of a source component
            on a target component while taking into account the simulation state, this builder can be used.  <br> To create a new instance of this class, use @link NXOpen::PressLineSimulation::ApplicationManager::CreateAdoptPartPositionBuilder  NXOpen::PressLineSimulation::ApplicationManager::CreateAdoptPartPositionBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class PRESSLINESIMULOPENCPPEXPORT  AdoptPartPositionBuilder : public NXOpen::Builder
        {
            private: AdoptPartPositionBuilderImpl * m_adoptpartpositionbuilder_impl;
            private: friend class  _AdoptPartPositionBuilderBuilder;
            protected: AdoptPartPositionBuilder();
            public: ~AdoptPartPositionBuilder();
            /**Returns  the selector for the source component, whos position will be copied 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponent * SourceComponentSelection
            (
            );
            /**Returns  the target component, whos position will be modified 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::Component * TargetComponent
            (
            );
            /**Sets  the target component, whos position will be modified 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pls_line_setup (" NX Press Line Setup") */
            public: void SetTargetComponent
            (
                NXOpen::Assemblies::Component * targetComponent /** targetcomponent */ 
            );
            /**Returns  the dynamic position provider 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PressLineSimulation::IDynamicTransformProvider * DynamicTransformProvider
            (
            );
            /**Sets  the dynamic position provider 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pls_line_setup (" NX Press Line Setup") */
            public: void SetDynamicTransformProvider
            (
                NXOpen::PressLineSimulation::IDynamicTransformProvider * dynamicTransformProvider /** dynamictransformprovider */ 
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