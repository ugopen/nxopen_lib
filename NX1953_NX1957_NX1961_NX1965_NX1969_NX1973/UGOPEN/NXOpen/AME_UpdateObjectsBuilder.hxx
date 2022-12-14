#ifndef NXOpen_AME_UPDATEOBJECTSBUILDER_HXX_INCLUDED
#define NXOpen_AME_UPDATEOBJECTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_UpdateObjectsBuilder.ja
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
#include <NXOpen/AME_AMEQuery.hxx>
#include <NXOpen/AME_SelectionBaseDefinitionBuilder.hxx>
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
        class UpdateObjectsBuilder;
    }
    namespace AME
    {
        class AMEExtendedObject;
    }
    namespace AME
    {
        class AMEQuery;
    }
    namespace AME
    {
        class SelectionBaseDefinitionBuilder;
    }
    class Builder;
    class NXObject;
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _UpdateObjectsBuilderBuilder;
        class UpdateObjectsBuilderImpl;
        /** Class to define Update Objects  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateUpdateObjectsBuilder  NXOpen::AME::AMEManager::CreateUpdateObjectsBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  UpdateObjectsBuilder : public NXOpen::Builder
        {
            /** Represents the type of input */
            public: enum Types
            {
                TypesDefinition/** definition */ ,
                TypesQuery/** query */ 
            };

            /** Represents the type of input objects */
            public: enum ObjectType
            {
                ObjectTypeEngobject/** engobject */ ,
                ObjectTypeProduct/** product */ ,
                ObjectTypeSymbol/** symbol */ 
            };

            private: UpdateObjectsBuilderImpl * m_updateobjectsbuilder_impl;
            private: friend class  _UpdateObjectsBuilderBuilder;
            protected: UpdateObjectsBuilder();
            public: ~UpdateObjectsBuilder();
            /**Returns  the selection update objects builder
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectionBaseDefinitionBuilder * SelectionBaseDefinition
            (
            );
            /**Returns  the selection update objects builder
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * ReuseLibraryItem
            (
            );
            /**Returns  the target revision of update objects builder
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString TargetRevision
            (
            );
            /**Sets  the target revision of update objects builder
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetTargetRevision
            (
                const NXString & targetRevisionName /** targetrevisionname */ 
            );
            /**Sets  the target revision of update objects builder
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetTargetRevision
            (
                const char * targetRevisionName /** targetrevisionname */ 
            );
            /**Sets  the select all option of update objects builder
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSelectAll
            (
                bool selectAll /** selectall */ 
            );
            /**Returns  the select all option of update objects builder
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool SelectAll
            (
            );
            /** Add the object to update
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void AddObjectToUpdate
            (
                NXOpen::NXObject * objectToUpdate /** objecttoupdate */ 
            );
            /**Returns  the input type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::UpdateObjectsBuilder::Types Type
            (
            );
            /**Sets  the input type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetType
            (
                NXOpen::AME::UpdateObjectsBuilder::Types type /** type */ 
            );
            /** Load all objects of selected type 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void LoadAllObjectsUsingType
            (
                const NXString & selectionType /** selectiontype */ ,
                std::vector<NXOpen::AME::AMEExtendedObject *> & loadedObjects /** loadedobjects */ 
            );
            /** Load all objects of selected type 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void LoadAllObjectsUsingType
            (
                const char * selectionType /** selectiontype */ ,
                std::vector<NXOpen::AME::AMEExtendedObject *> & loadedObjects /** loadedobjects */ 
            );
            /** Load all objects of selected query 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void LoadAllObjectsUsingQuery
            (
                NXOpen::AME::AMEQuery * queryObject /** queryobject */ ,
                std::vector<NXOpen::AME::AMEExtendedObject *> & loadedObjects /** loadedobjects */ 
            );
            /**Sets the source eo def
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSourceEngineeringObjectDefinition
            (
                const NXString & sourceDefinition /** sourcedefinition */ 
            );
            /**Sets the source eo def
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetSourceEngineeringObjectDefinition
            (
                const char * sourceDefinition /** sourcedefinition */ 
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
