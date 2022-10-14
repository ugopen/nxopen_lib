#ifndef NXOpen_ROUTING_WATERTIGHTFITTINGSBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_WATERTIGHTFITTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_WatertightFittingsBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/Routing_RouteObjectCollector.hxx>
#include <NXOpen/Routing_WatertightFittingsBuilder.hxx>
#include <NXOpen/Section.hxx>
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
        class WatertightFittingsBuilder;
    }
    class Builder;
    class Expression;
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        class RouteObjectCollector;
    }
    class Section;
    namespace Routing
    {
        class _WatertightFittingsBuilderBuilder;
        class WatertightFittingsBuilderImpl;
        /**  Represents a @link NXOpen::Routing::WatertightFittingsBuilder NXOpen::Routing::WatertightFittingsBuilder@endlink    <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateWatertightFittingsBuilder  NXOpen::Routing::RouteManager::CreateWatertightFittingsBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  WatertightFittingsBuilder : public NXOpen::Builder
        {
            private: WatertightFittingsBuilderImpl * m_watertightfittingsbuilder_impl;
            private: friend class  _WatertightFittingsBuilderBuilder;
            protected: WatertightFittingsBuilder();
            public: ~WatertightFittingsBuilder();
            /**Returns  the section used for creating penetration extrude. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Section * FlangeSketch
            (
            );
            /**Returns  the offset value for flange creation 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Expression * FlangeOffset
            (
            );
            /**Returns  the thickness value for flange creation 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Expression * FlangeThickness
            (
            );
            /**Returns  the direction of flange thickness 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: bool FlangeDirection
            (
            );
            /**Sets  the direction of flange thickness 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetFlangeDirection
            (
                bool flangeDirection /** flangedirection */ 
            );
            /**Returns  the Routing Object Collector builder that stores selected routing members   
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::RouteObjectCollector * FittingMembers
            (
            );
            /**Returns  the name of new part file containing watertight fittings assembly which includes the full path. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXString Filename
            (
            );
            /**Sets  the name of new part file containing watertight fittings assembly which includes the full path. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetFilename
            (
                const NXString & fileName /** filename */ 
            );
            /**Sets  the name of new part file containing watertight fittings assembly which includes the full path. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            void SetFilename
            (
                const char * fileName /** filename */ 
            );
            /** Get required attributes for Watertight Fittings.  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::CharacteristicList * GetRequiredAttributes
            (
            );
            /** Set required attributes for Watertight Fittings. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetRequiredAttributes
            (
                NXOpen::Routing::CharacteristicList * charxData /** charx data */ 
            );
            /** Get optional attributes for Watertight Fittings.  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::CharacteristicList * GetOptionalAttributes
            (
            );
            /** Set optional attributes for Watertight Fittings. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetOptionalAttributes
            (
                NXOpen::Routing::CharacteristicList * charxData /** charx data */ 
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