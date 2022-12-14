#ifndef NXOpen_AME_INSTANCEDATABLOCKBUILDER_HXX_INCLUDED
#define NXOpen_AME_INSTANCEDATABLOCKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_InstanceDataBlockBuilder.ja
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
#include <NXOpen/AME_EODataItemAttributeHolder.hxx>
#include <NXOpen/AME_InstanceDataBlockBuilder.hxx>
#include <NXOpen/AME_PlcBlock.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class InstanceDataBlockBuilder;
    }
    namespace AME
    {
        class EODataItemAttributeHolder;
    }
    namespace AME
    {
        class PlcBlock;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    namespace AME
    {
        class SelectAspectNode;
    }
    class Builder;
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _InstanceDataBlockBuilderBuilder;
        class InstanceDataBlockBuilderImpl;
        /** JA class for the reuse rule dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateInstanceDataBlockBuilder  NXOpen::AME::AMEManager::CreateInstanceDataBlockBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  InstanceDataBlockBuilder : public NXOpen::Builder
        {
            /** the idb scope */
            public: enum ActionType
            {
                ActionTypeGlobal/** global */ ,
                ActionTypeLocal/** local */ 
            };

            /** the idb create mode */
            public: enum CreateMode
            {
                CreateModeAspect/** aspect */ ,
                CreateModeLibrary/** library */ 
            };

            private: InstanceDataBlockBuilderImpl * m_instancedatablockbuilder_impl;
            private: friend class  _InstanceDataBlockBuilderBuilder;
            protected: InstanceDataBlockBuilder();
            public: ~InstanceDataBlockBuilder();
            /**Returns  the PlcBlock selection 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNode * SelectedBlock
            (
            );
            /**Returns  the EngObject selection 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAspectNode * SelectedEngObject
            (
            );
            /**Returns  the defined idb text name
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString InstanceName
            (
            );
            /**Sets  the defined idb text name
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetInstanceName
            (
                const NXString & resultText /** resulttext */ 
            );
            /**Sets  the defined idb text name
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetInstanceName
            (
                const char * resultText /** resulttext */ 
            );
            /**Returns  the defined idb text description
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString InstanceDescription
            (
            );
            /**Sets  the defined idb text description
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetInstanceDescription
            (
                const NXString & resultText /** resulttext */ 
            );
            /**Sets  the defined idb text description
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetInstanceDescription
            (
                const char * resultText /** resulttext */ 
            );
            /**Returns  the defined rule type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::InstanceDataBlockBuilder::ActionType TypeOfIDB
            (
            );
            /**Sets  the defined rule type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetTypeOfIDB
            (
                NXOpen::AME::InstanceDataBlockBuilder::ActionType type /** type */ 
            );
            /**Returns  the data item 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::EODataItemAttributeHolder * EoDataItemAttributeHolder
            (
            );
            /** Updates the source block selection
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void UpdateSourceBlock
            (
                NXOpen::AME::PlcBlock * selBlock /** selblock */ 
            );
            /**Returns  the library pou selection
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * SelectedFBFromLibrary
            (
            );
            /** Updates the source block by using given file name of reuse library item 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void UpdateSourceBlockByName
            (
                const NXString & fileName /** filename */ 
            );
            /** Updates the source block by using given file name of reuse library item 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void UpdateSourceBlockByName
            (
                const char * fileName /** filename */ 
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
