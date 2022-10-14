#ifndef NXOpen_ROUTING_EDITCHARACTERISTICSBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_EDITCHARACTERISTICSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_EditCharacteristicsBuilder.ja
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
        class EditCharacteristicsBuilder;
    }
    class Builder;
    class NXObject;
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
        class _EditCharacteristicsBuilderBuilder;
        class EditCharacteristicsBuilderImpl;
        /** Builder to edit required and optional characteristics of @link Routing::Stock Routing::Stock@endlink 
                or @link Assemblies::Component Assemblies::Component@endlink  as defined in the application view file.  <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateEditCharacteristicsBuilder  NXOpen::Routing::RouteManager::CreateEditCharacteristicsBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  EditCharacteristicsBuilder : public NXOpen::Builder
        {
            private: EditCharacteristicsBuilderImpl * m_editcharacteristicsbuilder_impl;
            private: friend class  _EditCharacteristicsBuilderBuilder;
            protected: EditCharacteristicsBuilder();
            public: ~EditCharacteristicsBuilder();
            /**Returns  the routing objects to edit characteristics. The objects should be either 
                        @link Routing::Stock Routing::Stock@endlink  or @link Assemblies::Component Assemblies::Component@endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::RouteObjectCollector * RouteObjectCollector
            (
            );
            /** Reset the characteristic values of the selected objects. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void ResetValues
            (
            );
            /** Clear the characteristic values of the selected objects. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void ClearValues
            (
            );
            /**Returns  the reference object to obtain the characteristic values 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::SelectNXObject * ReferenceObject
            (
            );
            /** Apply characteristics of the reference object to the selected objects. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void ApplyReferenceObjectCharx
            (
                NXOpen::NXObject * refObject /** refobject */ 
            );
            /**Returns  the Routing Level associated with selected objects. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString RoutingLevel
            (
            );
            /**Sets  the Routing Level associated with selected objects. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetRoutingLevel
            (
                const NXString & routeLevel /** routelevel */ 
            );
            /**Sets  the Routing Level associated with selected objects. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetRoutingLevel
            (
                const char * routeLevel /** routelevel */ 
            );
            /** Returns the editable @link Routing::CharacteristicList Routing::CharacteristicList@endlink  
                        that contains required characteristics common to all the selected objects.  @return The characteristics to edit.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::CharacteristicList * GetRequiredCharacteristicsToEdit
            (
            );
            /** Returns the editable @link Routing::CharacteristicList Routing::CharacteristicList@endlink  
                        that contains optional characteristics common to all the selected objects.  @return The characteristics to edit.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::CharacteristicList * GetOptionalCharacteristicsToEdit
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