#ifndef NXOpen_LINEDESIGNER_ADDTYPEATTRIBUTEBUILDER_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_ADDTYPEATTRIBUTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_AddTypeAttributeBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class AddTypeAttributeBuilder;
    }
    class Builder;
    class SelectDisplayableObject;
    namespace LineDesigner
    {
        class _AddTypeAttributeBuilderBuilder;
        class AddTypeAttributeBuilderImpl;
        /**Class for assignment of mapped type <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateAddTypeAttributeBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateAddTypeAttributeBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Type </term> <description> 
         
        Mfg0MEEqupment </description> </item> 

        </list> 

         <br>  Created in NX1938.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  AddTypeAttributeBuilder : public NXOpen::Builder
        {
            /** This enum is providing possible mapped types */
            public: enum MappedType
            {
                MappedTypeMfg0MEEqupment/** mfg0meequpment */ 
            };

            private: AddTypeAttributeBuilderImpl * m_addtypeattributebuilder_impl;
            private: friend class  _AddTypeAttributeBuilderBuilder;
            protected: AddTypeAttributeBuilder();
            public: ~AddTypeAttributeBuilder();
            /**Returns  the component selection 
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::SelectDisplayableObject * ComponentSelection
            (
            );
            /**Returns  the mapped type 
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::LineDesigner::AddTypeAttributeBuilder::MappedType Type
            (
            );
            /**Sets  the mapped type 
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetType
            (
                NXOpen::LineDesigner::AddTypeAttributeBuilder::MappedType type /** type */ 
            );
            /**Returns  the mapped type name 
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXString MappedTypeName
            (
            );
            /**Sets  the mapped type name 
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetMappedTypeName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the mapped type name 
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            void SetMappedTypeName
            (
                const char * name /** name */ 
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
