#ifndef NXOpen_AME_PROJECTENGINEERINGOBJECTBUILDER_HXX_INCLUDED
#define NXOpen_AME_PROJECTENGINEERINGOBJECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ProjectEngineeringObjectBuilder.ja
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
#include <NXOpen/AME_AspectDetailsBuilder.hxx>
#include <NXOpen/AME_EODefAttributeHolder.hxx>
#include <NXOpen/AME_ObjectNameIndexBuilder.hxx>
#include <NXOpen/AME_ProjectEngineeringObjectBuilder.hxx>
#include <NXOpen/Diagramming_Node.hxx>
#include <NXOpen/AME_EngineeringObjectBaseBuilder.hxx>
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
        class ProjectEngineeringObjectBuilder;
    }
    namespace AME
    {
        class AspectDetailsBuilder;
    }
    namespace AME
    {
        class EODefAttributeHolder;
    }
    namespace AME
    {
        class EngineeringObjectBaseBuilder;
    }
    namespace AME
    {
        class ObjectNameIndexBuilder;
    }
    namespace Diagramming
    {
        class Node;
    }
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _ProjectEngineeringObjectBuilderBuilder;
        class ProjectEngineeringObjectBuilderImpl;
        /** JA class for the insert Project Eng object dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateProjectEngineeringObjectBuilder  NXOpen::AME::AMEManager::CreateProjectEngineeringObjectBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ProjectEngineeringObjectBuilder : public NXOpen::AME::EngineeringObjectBaseBuilder
        {
            private: ProjectEngineeringObjectBuilderImpl * m_projectengineeringobjectbuilder_impl;
            private: friend class  _ProjectEngineeringObjectBuilderBuilder;
            protected: ProjectEngineeringObjectBuilder();
            public: ~ProjectEngineeringObjectBuilder();
            /**Returns  the aspect detail ui block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::AspectDetailsBuilder * AspectDetails
            (
            );
            /**Returns  the eo name index and description ui block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ObjectNameIndexBuilder * EoNameIndex
            (
            );
            /**Returns  the select eo symbol
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * SelectSymbolDefinition
            (
            );
            /**Returns  the def 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::EODefAttributeHolder * EoDefAttributeHolder
            (
            );
            /**Returns  the preview node on the page 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Diagramming::Node * PreviewNodeObject
            (
            );
            /**Sets  the preview node on the page 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPreviewNodeObject
            (
                NXOpen::Diagramming::Node * previewNodeObject /** previewnodeobject */ 
            );
            /** The preview node location on page. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void PreviewNodeLocation
            (
                double locationX /** locationx */ ,
                double locationY /** locationy */ ,
                bool nodePlaced /** nodeplaced */ 
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
