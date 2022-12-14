#ifndef NXOpen_ROUTING_PORTARRAYSBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_PORTARRAYSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_PortArraysBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/Routing_NamingPatternBuilder.hxx>
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
        class PortArraysBuilder;
    }
    class Builder;
    namespace Routing
    {
        class NamingPatternBuilder;
    }
    namespace Routing
    {
        class PortArrayListItemBuilderList;
    }
    namespace Routing
    {
        class _PortArraysBuilderBuilder;
        class PortArraysBuilderImpl;
        /** Builder for creating terminal arrays in multiports.  <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreatePortArraysBuilder  NXOpen::Routing::RouteManager::CreatePortArraysBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  PortArraysBuilder : public NXOpen::Builder
        {
            /** Determines the array type that will be selected */
            public: enum ArrayTypes
            {
                ArrayTypesRectangular/** rectangular */ ,
                ArrayTypesCircular/** circular */ 
            };

            /** Determines the naming method for the terminal ports */
            public: enum NamingMethods
            {
                NamingMethodsClockwise/** clockwise */ ,
                NamingMethodsCounterclockwise/** counterclockwise */ ,
                NamingMethodsAcross/** across */ ,
                NamingMethodsContinuous/** continuous */ ,
                NamingMethodsRowCol/** row col */ 
            };

            /** Determines the starting location for naming terminal ports */
            public: enum StartingCorners
            {
                StartingCornersBottomLeft/** bottom left */ ,
                StartingCornersBottomRight/** bottom right */ ,
                StartingCornersUpperLeft/** upper left */ ,
                StartingCornersUpperRight/** upper right */ 
            };

            /** Determines the starting direction for naming terminal ports */
            public: enum StartingDirections
            {
                StartingDirectionsHorizontal/** horizontal */ ,
                StartingDirectionsVertical/** vertical */ 
            };

            private: PortArraysBuilderImpl * m_portarraysbuilder_impl;
            private: friend class  _PortArraysBuilderBuilder;
            protected: PortArraysBuilder();
            public: ~PortArraysBuilder();
            /**Returns  the array type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Routing::PortArraysBuilder::ArrayTypes ArrayType
            (
            );
            /**Sets  the array type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetArrayType
            (
                NXOpen::Routing::PortArraysBuilder::ArrayTypes arrayType /** arraytype */ 
            );
            /**Returns  the array pattern list 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::PortArrayListItemBuilderList * ArrayPatternList
            (
            );
            /**Returns  the naming method 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::PortArraysBuilder::NamingMethods NamingMethod
            (
            );
            /**Sets  the naming method 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetNamingMethod
            (
                NXOpen::Routing::PortArraysBuilder::NamingMethods namingMethod /** namingmethod */ 
            );
            /**Returns  the starting corner 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Routing::PortArraysBuilder::StartingCorners StartingCorner
            (
            );
            /**Sets  the starting corner 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStartingCorner
            (
                NXOpen::Routing::PortArraysBuilder::StartingCorners startingCorner /** startingcorner */ 
            );
            /**Returns  the starting direction 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Routing::PortArraysBuilder::StartingDirections StartingDirection
            (
            );
            /**Sets  the starting direction 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStartingDirection
            (
                NXOpen::Routing::PortArraysBuilder::StartingDirections startingDirection /** startingdirection */ 
            );
            /**Returns  the reuse suppressed names 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReuseSuppressedNames
            (
            );
            /**Sets  the reuse suppressed names 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetReuseSuppressedNames
            (
                bool reuseSuppressedNames /** reusesuppressednames */ 
            );
            /**Returns  the naming pattern for the rows of Column/Row rectangular terminal port arrays 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::NamingPatternBuilder * PatternRow
            (
            );
            /**Sets  the naming pattern for the rows of Column/Row rectangular terminal port arrays 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPatternRow
            (
                NXOpen::Routing::NamingPatternBuilder * patternRow /** patternrow */ 
            );
            /**Returns  the naming pattern for the columns of Column/Row rectangular terminal port arrays 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::NamingPatternBuilder * PatternCol
            (
            );
            /**Sets  the naming pattern for the columns of Column/Row rectangular terminal port arrays 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPatternCol
            (
                NXOpen::Routing::NamingPatternBuilder * patternCol /** patterncol */ 
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
