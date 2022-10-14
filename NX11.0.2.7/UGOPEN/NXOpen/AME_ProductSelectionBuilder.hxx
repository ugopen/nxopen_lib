#ifndef NXOpen_AME_PRODUCTSELECTIONBUILDER_HXX_INCLUDED
#define NXOpen_AME_PRODUCTSELECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ProductSelectionBuilder.ja
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
#include <NXOpen/AME_ProductSelectionBuilder.hxx>
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
        class ProductSelectionBuilder;
    }
    namespace AME
    {
        class ProductDefinition;
    }
    class Builder;
    class SelectNXObject;
    namespace AME
    {
        class _ProductSelectionBuilderBuilder;
        class ProductSelectionBuilderImpl;
        /** JA class for Product Selection dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateProductSelectionBuilder  NXOpen::AME::AMEManager::CreateProductSelectionBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ProductType </td> <td> 
         
        SameEngineeringObjectDefinition </td> </tr> 

        </table>  

         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ProductSelectionBuilder : public NXOpen::Builder
        {
            /** the product type for product selection*/
            public: enum Type
            {
                TypeSameEngineeringObjectDefinition/** same engineering object definition */ ,
                TypeSameClassificationAndMoreDetailedClassification/** same classification and more detailed classification */ 
            };

            private: ProductSelectionBuilderImpl * m_productselectionbuilder_impl;
            private: friend class  _ProductSelectionBuilderBuilder;
            protected: ProductSelectionBuilder();
            public: ~ProductSelectionBuilder();
            /**Returns  the selected device 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectNXObject * SelectDevice
            (
            );
            /**Returns  the product type for product selection
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::AME::ProductSelectionBuilder::Type ProductType
            (
            );
            /**Sets  the product type for product selection
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetProductType
            (
                NXOpen::AME::ProductSelectionBuilder::Type productType /** producttype */ 
            );
            /** Set Selected Product
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSelectedProduct
            (
                NXOpen::AME::ProductDefinition * selectedProduct /** selectedproduct */ 
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