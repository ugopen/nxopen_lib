#ifndef NXOpen_AME_PORTBUILDER_HXX_INCLUDED
#define NXOpen_AME_PORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PortBuilder.ja
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
#include <NXOpen/AME_PortAttributeHolder.hxx>
#include <NXOpen/AME_SelectionEngineeringObjectDefinitionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Tooling_SelectReuseLibraryItemBuilder.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class PortBuilder;
    }
    namespace AME
    {
        class PortAttributeHolder;
    }
    namespace AME
    {
        class SelectionEngineeringObjectDefinitionBuilder;
    }
    class Builder;
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _PortBuilderBuilder;
        class PortBuilderImpl;
        /** builder for the software block properties dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreatePortBuilder  NXOpen::AME::AMEManager::CreatePortBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  PortBuilder : public NXOpen::Builder
        {
            /** the type of a port */
            public: enum Type
            {
                TypeAll/** all */ ,
                TypeCaller/** caller */ ,
                TypeOperand/** operand */ ,
                TypeMethod/** method */ ,
                TypeBlock/** block */ 
            };

            /** Represents the type of creation mode */
            public: enum CreationModeType
            {
                CreationModeTypeNew/** new */ ,
                CreationModeTypeLibrary/** library */ 
            };

            /** Represents the type of connectable attribute proxy object for typed port*/
            public: enum ConnectableAttrProxyObjectType
            {
                ConnectableAttrProxyObjectTypeAll/** all */ ,
                ConnectableAttrProxyObjectTypeLibrary/** library */ ,
                ConnectableAttrProxyObjectTypeTag/** tag */ 
            };

            private: PortBuilderImpl * m_portbuilder_impl;
            private: friend class  _PortBuilderBuilder;
            protected: PortBuilder();
            public: ~PortBuilder();
            /**Returns  the type of port 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString PortType
            (
            );
            /**Sets  the type of port 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPortType
            (
                const NXString & type /** type */ 
            );
            /**Sets  the type of port 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetPortType
            (
                const char * type /** type */ 
            );
            /**Returns  the name of port 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString PortName
            (
            );
            /**Sets  the name of port 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPortName
            (
                const NXString & portName /** portname */ 
            );
            /**Sets  the name of port 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetPortName
            (
                const char * portName /** portname */ 
            );
            /** Set the direction 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPortDirection
            (
                const NXString & portDirection /** portdirection */ 
            );
            /** Set the direction 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetPortDirection
            (
                const char * portDirection /** portdirection */ 
            );
            /** Set the cardinality 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPortCardinality
            (
                const NXString & portCardinality /** portcardinality */ 
            );
            /** Set the cardinality 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetPortCardinality
            (
                const char * portCardinality /** portcardinality */ 
            );
            /**Returns  the creation mode 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::PortBuilder::CreationModeType CreationMode
            (
            );
            /**Sets  the creation mode 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCreationMode
            (
                NXOpen::AME::PortBuilder::CreationModeType creationMode /** creationmode */ 
            );
            /**Returns  the reuse library item 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * ReuseLibraryItem
            (
            );
            /**Returns  the engineering object type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectionEngineeringObjectDefinitionBuilder * EngObjectType
            (
            );
            /**Returns  the connectable object type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::PortBuilder::ConnectableAttrProxyObjectType ConnectableProxyObjectType
            (
            );
            /**Sets  the connectable object type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetConnectableProxyObjectType
            (
                NXOpen::AME::PortBuilder::ConnectableAttrProxyObjectType connectableAttrObjectType /** connectableattrobjecttype */ 
            );
            /**Returns  the port attribute holder 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::PortAttributeHolder * PortAttributeHolder
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
