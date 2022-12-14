#ifndef NXOpen_AME_CREATEPRODUCTBUILDER_HXX_INCLUDED
#define NXOpen_AME_CREATEPRODUCTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_CreateProductBuilder.ja
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
#include <NXOpen/AME_SelectClassificationFromTreeBuilder.hxx>
#include <NXOpen/AME_SelectionEngineeringObjectDefinitionBuilder.hxx>
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
        class CreateProductBuilder;
    }
    namespace AME
    {
        class SelectClassificationFromTreeBuilder;
    }
    namespace AME
    {
        class SelectionEngineeringObjectDefinitionBuilder;
    }
    class Builder;
    class NXObject;
    namespace AME
    {
        class _CreateProductBuilderBuilder;
        class CreateProductBuilderImpl;
        /** Create and classify product  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateProductBuilder  NXOpen::AME::AMEManager::CreateProductBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  CreateProductBuilder : public NXOpen::Builder
        {
            private: CreateProductBuilderImpl * m_createproductbuilder_impl;
            private: friend class  _CreateProductBuilderBuilder;
            protected: CreateProductBuilder();
            public: ~CreateProductBuilder();
            /**Returns  the engineering object definition
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectionEngineeringObjectDefinitionBuilder * SelectionEngObjectDefinition
            (
            );
            /**Returns  the select classification from tree builder.
             <br>  @deprecated Deprecated in NX12.0.0.  The newly created product is placed under the product library node which corresponds to the Type Library path of the selected Device Type. If the selected type has no counterpart in the Product structure, system automatically places those directly under Device Product Library node. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  The newly created product is placed under the product library node which corresponds to the Type Library path of the selected Device Type. If the selected type has no counterpart in the Product structure, system automatically places those directly under Device Product Library node.") NXOpen::AME::SelectClassificationFromTreeBuilder * SelectClassificationFromTree
            (
            );
            /** Creates a new type attribute object  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::NXObject * CreateTypeAttribute
            (
            );
            /** Sets the Object Name on Type Attribute Object.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetObjectNameOnTypeAttr
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
