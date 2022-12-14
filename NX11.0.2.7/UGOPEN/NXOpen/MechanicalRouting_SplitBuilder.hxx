#ifndef NXOpen_MECHANICALROUTING_SPLITBUILDER_HXX_INCLUDED
#define NXOpen_MECHANICALROUTING_SPLITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MechanicalRouting_SplitBuilder.ja
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
#include <NXOpen/MechanicalRouting_SplitBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Routing_RouteObjectCollector.hxx>
#include <NXOpen/libnxopencpp_mechanicalrouting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MechanicalRouting
    {
        class SplitBuilder;
    }
    namespace Assemblies
    {
        class Component;
    }
    class Builder;
    namespace PDM
    {
        class LogicalObject;
    }
    namespace Routing
    {
        class RouteObjectCollector;
    }
    namespace MechanicalRouting
    {
        class _SplitBuilderBuilder;
        class SplitBuilderImpl;
        /** the Builder to Assign Discontinuity for the stocks  <br> To create a new instance of this class, use @link NXOpen::MechanicalRouting::BuilderFactory::CreateSplitBuilder  NXOpen::MechanicalRouting::BuilderFactory::CreateSplitBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHANICALROUTINGEXPORT  SplitBuilder : public NXOpen::Builder
        {
            private: SplitBuilderImpl * m_splitbuilder_impl;
            private: friend class  _SplitBuilderBuilder;
            protected: SplitBuilder();
            public: ~SplitBuilder();
            /**Returns  the Rcp type of the selected object  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::RouteObjectCollector * ControlPointCollector
            (
            );
            /** Components created during Split operation.  @return  Components created during Split operation. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Assemblies::Component *> GetCreatedComponents
            (
            );
            /** Performs the operations needed prior to a commit. This method has to be called before invoking commit. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void PreCommit
            (
            );
            /** Returns the @link PDM::LogicalObject PDM::LogicalObject@endlink s that represent content that will be created by this builder. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void GetLogicalObjects
            (
                std::vector<NXOpen::PDM::LogicalObject *> & logicalObjects /** logicalobjects */ 
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
