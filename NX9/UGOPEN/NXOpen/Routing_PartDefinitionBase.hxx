#ifndef NXOpen_ROUTING_PARTDEFINITIONBASE_HXX_INCLUDED
#define NXOpen_ROUTING_PARTDEFINITIONBASE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_PartDefinitionBase.ja
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
#include <NXOpen/Routing_ItemDefinition.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class PartDefinitionBase;
    }
    namespace Routing
    {
        class ItemDefinition;
    }
    namespace Routing
    {
        class _PartDefinitionBaseBuilder;
        class PartDefinitionBaseImpl;
        /**
                
                The abstract class @link Routing::PartDefinitionBase Routing::PartDefinitionBase@endlink  contains
                information defining a logical part.
                
                 <br> 
                See NX Routing help for the Connectivity data model documentation.
                 <br> 
             <br> Creator not available in KF.  <br> 
         <br>  Created in NX4.0.2.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  PartDefinitionBase : public Routing::ItemDefinition
        {
            private: PartDefinitionBaseImpl * m_partdefinitionbase_impl;
            private: friend class  _PartDefinitionBaseBuilder;
            protected: PartDefinitionBase();
            public: ~PartDefinitionBase();
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