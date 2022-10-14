#ifndef NXOpen_AME_EDITCLAUSEBUILDER_HXX_INCLUDED
#define NXOpen_AME_EDITCLAUSEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_EditClauseBuilder.ja
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
#include <NXOpen/AME_EditClauseBuilder.hxx>
#include <NXOpen/AME_SelectClassificationBuilder.hxx>
#include <NXOpen/AME_SelectionEngineeringObjectDefinitionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class EditClauseBuilder;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    namespace AME
    {
        class SelectClassificationBuilder;
    }
    namespace AME
    {
        class SelectionEngineeringObjectDefinitionBuilder;
    }
    class Builder;
    namespace AME
    {
        class _EditClauseBuilderBuilder;
        class EditClauseBuilderImpl;
        /** Naming Rule Builder  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateEditClauseBuilder  NXOpen::AME::AMEManager::CreateEditClauseBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AllAspects </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        AspectOperator </td> <td> 
         
        Under </td> </tr> 

        <tr><td> 
         
        ClassificationOperator </td> <td> 
         
        As </td> </tr> 

        <tr><td> 
         
        ReuseLibraryOperator </td> <td> 
         
        OfType </td> </tr> 

        </table>  

         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  EditClauseBuilder : public NXOpen::Builder
        {
            /** the type of object to be used for edit clause*/
            public: enum Types
            {
                TypesClassification/** classification */ ,
                TypesLibraryObject/** library object */ ,
                TypesAspect/** aspect */ 
            };

            /** the query operator */
            public: enum Operator
            {
                OperatorAs/** as */ ,
                OperatorUnder/** under */ ,
                OperatorOfType/** of type */ 
            };

            private: EditClauseBuilderImpl * m_editclausebuilder_impl;
            private: friend class  _EditClauseBuilderBuilder;
            protected: EditClauseBuilder();
            public: ~EditClauseBuilder();
            /**Returns  the selected classification 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectClassificationBuilder * SelectClassification
            (
            );
            /**Returns  the engineering object definition
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectionEngineeringObjectDefinitionBuilder * SelectFromMemberSelect
            (
            );
            /**Returns  the selected aspect 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNode * SelectAspect
            (
            );
            /**Returns  the query operator for Classification object
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::EditClauseBuilder::Operator ClassificationOperator
            (
            );
            /**Sets  the query operator for Classification object
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetClassificationOperator
            (
                NXOpen::AME::EditClauseBuilder::Operator classificationOperator /** classificationoperator */ 
            );
            /**Returns  the all aspects option status whether ON or OFF 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool AllAspects
            (
            );
            /**Sets  the all aspects option status whether ON or OFF 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetAllAspects
            (
                bool toggleAllAspects /** toggleallaspects */ 
            );
            /**Returns  the query operator for Aspect object 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::EditClauseBuilder::Operator AspectOperator
            (
            );
            /**Sets  the query operator for Aspect object 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetAspectOperator
            (
                NXOpen::AME::EditClauseBuilder::Operator aspectOperator /** aspectoperator */ 
            );
            /**Returns  the query operator for Reuse Library object
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::EditClauseBuilder::Operator ReuseLibraryOperator
            (
            );
            /**Sets  the query operator for Reuse Library object
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetReuseLibraryOperator
            (
                NXOpen::AME::EditClauseBuilder::Operator reuseLibraryOperator /** reuselibraryoperator */ 
            );
            /**Returns  the type of object to be used for edit clause
                        @link NXOpen::AME::EditClauseBuilder::Type NXOpen::AME::EditClauseBuilder::Type@endlink 
                    
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::EditClauseBuilder::Types Type
            (
            );
            /**Sets  the type of object to be used for edit clause
                        @link NXOpen::AME::EditClauseBuilder::Type NXOpen::AME::EditClauseBuilder::Type@endlink 
                    
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetType
            (
                NXOpen::AME::EditClauseBuilder::Types type /** type */ 
            );
            /** Set the property
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetProperty
            (
                int index /** index */ ,
                const NXString & propertyName /** propertyname */ 
            );
            /** Set the property
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetProperty
            (
                int index /** index */ ,
                const char * propertyName /** propertyname */ 
            );
            /** Set the property operator
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPropertyOperator
            (
                int index /** index */ ,
                const NXString & propertyOperator /** propertyoperator */ 
            );
            /** Set the property operator
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetPropertyOperator
            (
                int index /** index */ ,
                const char * propertyOperator /** propertyoperator */ 
            );
            /** Set the property value
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPropertyValue
            (
                int index /** index */ ,
                const NXString & propertyValue /** propertyvalue */ 
            );
            /** Set the property value
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetPropertyValue
            (
                int index /** index */ ,
                const char * propertyValue /** propertyvalue */ 
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