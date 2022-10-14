#ifndef NXOpen_ROUTING_UNIFYPATHBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_UNIFYPATHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_UnifyPathBuilder.ja
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
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/Routing_RouteObjectCollector.hxx>
#include <NXOpen/Routing_UnifyPathBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class UnifyPathBuilder;
    }
    class Builder;
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        class RouteObjectCollector;
    }
    class SelectNXObject;
    namespace Routing
    {
        class _UnifyPathBuilderBuilder;
        class UnifyPathBuilderImpl;
        /** Builder to unify @link Routing::Stock Routing::Stock@endlink  and @link Assemblies::Component Assemblies::Component@endlink 
                based on specified characteristic values.
                The builder takes a set of objects and replaces them with new objects that matches
                the given characterstics. <br> To create a new instance of this class, use @link Routing::RouteManager::CreateUnifyPathBuilder Routing::RouteManager::CreateUnifyPathBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  UnifyPathBuilder : public Builder
        {
            private: UnifyPathBuilderImpl * m_unifypathbuilder_impl;
            private: friend class  _UnifyPathBuilderBuilder;
            protected: UnifyPathBuilder();
            public: ~UnifyPathBuilder();
            /**Returns  the routing object collector to select objects to unify. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::RouteObjectCollector * RouteObjectCollector
            (
            );
            /**Returns  the reference object used to extract characteristics to unify. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::SelectNXObject * ReferenceObject
            (
            );
            /** Returns @link Routing::CharacteristicList Routing::CharacteristicList@endlink  to be used to find
                        matching @link Routing::Stock Routing::Stock@endlink  and @link Assemblies::Component Assemblies::Component@endlink 
                        to replace.  @return The characteristics to use in finding a replacement for the given object. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CharacteristicList * GetUnifyCharacteristics
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif