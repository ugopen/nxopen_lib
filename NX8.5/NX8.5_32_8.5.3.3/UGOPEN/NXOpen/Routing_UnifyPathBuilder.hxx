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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/Routing_RouteObjectCollector.hxx>
#include <NXOpen/Routing_UnifyPathBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
                the given characterstics. <br> To create a new instance of this class, use @link Routing::RouteManager::CreateUnifyPathBuilder  Routing::RouteManager::CreateUnifyPathBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  UnifyPathBuilder : public Builder
        {
            private: UnifyPathBuilderImpl * m_unifypathbuilder_impl;
            private: friend class  _UnifyPathBuilderBuilder;
            protected: UnifyPathBuilder();
            public: ~UnifyPathBuilder();
            /**Returns  the routing object collector to select objects to unify.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::RouteObjectCollector * RouteObjectCollector
            (
            );
            /**Returns  the reference object used to extract characteristics to unify.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::SelectNXObject * ReferenceObject
            (
            );
            /** Returns @link Routing::CharacteristicList Routing::CharacteristicList@endlink  to be used to find
                        matching @link Routing::Stock Routing::Stock@endlink  and @link Assemblies::Component Assemblies::Component@endlink 
                        to replace.  @return The characteristics to use in finding a replacement for the given object.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::CharacteristicList * GetUnifyCharacteristics
            (
            );
            /** Sets the characteristics to be applied
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetUnifyCharacteristics
            (
                NXOpen::NXObject::AttributeType charxType /** charxtype */ ,
                const NXString & charxName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & charxValue /**The characteristics to use in finding a replacement for the given object.  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the characteristics to be applied
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            void SetUnifyCharacteristics
            (
                NXOpen::NXObject::AttributeType charxType /** charxtype */ ,
                const char * charxName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * charxValue /**The characteristics to use in finding a replacement for the given object.  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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
