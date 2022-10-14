#ifndef NXOpen_ROUTING_FORMBOARDPLACEMENTCOORDINATESYSTEMBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_FORMBOARDPLACEMENTCOORDINATESYSTEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_FormboardPlacementCoordinateSystemBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
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
        class FormboardPlacementCoordinateSystemBuilder;
    }
    class Builder;
    class CoordinateSystem;
    class SelectNXObjectList;
    namespace Routing
    {
        class _FormboardPlacementCoordinateSystemBuilderBuilder;
        class FormboardPlacementCoordinateSystemBuilderImpl;
        /** Builder for Creating/Editing the Formboard Placement Coordinate Systems. <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateFormboardPlacementCoordinateSystemBuilder  NXOpen::Routing::RouteManager::CreateFormboardPlacementCoordinateSystemBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  FormboardPlacementCoordinateSystemBuilder : public NXOpen::Builder
        {
            /** Determines the method to qualify the csys */
            public: enum Method
            {
                MethodSpecify/** Specify Csys. */,
                MethodSelect/** Select Csys. */
            };

            private: FormboardPlacementCoordinateSystemBuilderImpl * m_formboardplacementcoordinatesystembuilder_impl;
            private: friend class  _FormboardPlacementCoordinateSystemBuilderBuilder;
            protected: FormboardPlacementCoordinateSystemBuilder();
            public: ~FormboardPlacementCoordinateSystemBuilder();
            /**Returns  the Qualify Method enum 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::FormboardPlacementCoordinateSystemBuilder::Method QualifyMethod
            (
            );
            /**Sets  the Qualify Method enum 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetQualifyMethod
            (
                NXOpen::Routing::FormboardPlacementCoordinateSystemBuilder::Method qualifyGroup /** qualifygroup */ 
            );
            /**Returns  the specified csys 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::CoordinateSystem * SpecifiedCSYS
            (
            );
            /**Sets  the specified csys 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetSpecifiedCSYS
            (
                NXOpen::CoordinateSystem * specifiedCSYS /** specifiedcsys */ 
            );
            /**Returns  the selected csys 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::SelectNXObjectList * SelectedCSYS
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