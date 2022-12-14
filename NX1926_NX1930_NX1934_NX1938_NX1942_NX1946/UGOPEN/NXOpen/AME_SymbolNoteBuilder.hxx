#ifndef NXOpen_AME_SYMBOLNOTEBUILDER_HXX_INCLUDED
#define NXOpen_AME_SYMBOLNOTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_SymbolNoteBuilder.ja
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
#include <NXOpen/AME_SymbolAnnotationStyleBuilder.hxx>
#include <NXOpen/AME_SymbolAnnotations.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class SymbolNoteBuilder;
    }
    namespace AME
    {
        class SymbolAnnotationStyleBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    class Builder;
    class NXObject;
    namespace AME
    {
        class _SymbolNoteBuilderBuilder;
        class SymbolNoteBuilderImpl;
        /** Represents a Symbol Note creation class Builder   <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateSymbolNoteBuilder  NXOpen::AME::AMEManager::CreateSymbolNoteBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        SymbolAnnotationStyle.Anchor </term> <description> 
         
        BottomRight </description> </item> 

        <item><term> 
         
        SymbolAnnotationStyle.Height </term> <description> 
         
        Two </description> </item> 

        <item><term> 
         
        SymbolAnnotationStyle.Justification </term> <description> 
         
        Right </description> </item> 

        <item><term> 
         
        SymbolAnnotationStyle.LetteringAngle </term> <description> 
         
        Degree0 </description> </item> 

        </list> 

         <br>  Created in NX1847.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  SymbolNoteBuilder : public NXOpen::Builder
        {
            private: SymbolNoteBuilderImpl * m_symbolnotebuilder_impl;
            private: friend class  _SymbolNoteBuilderBuilder;
            protected: SymbolNoteBuilder();
            public: ~SymbolNoteBuilder();
            /**Returns  the Annotation type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::AmeSymbolAnnotationType Type
            (
            );
            /**Sets  the Annotation type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetType
            (
                NXOpen::AME::AmeSymbolAnnotationType type /** type */ 
            );
            /**Returns  the origin 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Annotations::OriginBuilder * Origin
            (
            );
            /** Add the attribute 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void AddAttribute
            (
                const NXString & propertyName /** propertyname */ ,
                NXOpen::NXObject * propertyReference /** propertyreference */ 
            );
            /** Add the attribute 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void AddAttribute
            (
                const char * propertyName /** propertyname */ ,
                NXOpen::NXObject * propertyReference /** propertyreference */ 
            );
            /** Reset the property list 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ResetPropertyList
            (
            );
            /**Returns  the symbolAnnotationStyle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SymbolAnnotationStyleBuilder * SymbolAnnotationStyle
            (
            );
            /** Resets the symbol annotation settings to default.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ResetToDefault
            (
            );
            /** Add the new attribute 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void AddNewAttribute
            (
                NXOpen::NXObject * attrOwner /** attrowner */ ,
                const NXString & attrTitle /** attrtitle */ ,
                NXOpen::AME::AmeSymbolAnnotationAttributesource attrCategory /** attrcategory */ 
            );
            /** Add the new attribute 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void AddNewAttribute
            (
                NXOpen::NXObject * attrOwner /** attrowner */ ,
                const char * attrTitle /** attrtitle */ ,
                NXOpen::AME::AmeSymbolAnnotationAttributesource attrCategory /** attrcategory */ 
            );
            /** Remove the attribute 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void RemoveAttribute
            (
                int attrIndex /** attrindex */ 
            );
            /** Move up attribute 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void MoveUpAttribute
            (
                int attrIndex /** attrindex */ 
            );
            /** Move down attribute 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void MoveDownAttribute
            (
                int attrIndex /** attrindex */ 
            );
            /**Returns  the contact block annotation type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::AmeSymbolAnnotationContactblock ContactBlock
            (
            );
            /**Sets  the contact block annotation type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetContactBlock
            (
                NXOpen::AME::AmeSymbolAnnotationContactblock type /** type */ 
            );
            /** Update attribute category 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void UpdateAttributeCategory
            (
                int attrIndex /** attrindex */ ,
                NXOpen::AME::AmeSymbolAnnotationAttributesource attrCategory /** attrcategory */ 
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
