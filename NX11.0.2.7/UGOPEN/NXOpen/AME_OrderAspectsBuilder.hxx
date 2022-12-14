#ifndef NXOpen_AME_ORDERASPECTSBUILDER_HXX_INCLUDED
#define NXOpen_AME_ORDERASPECTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_OrderAspectsBuilder.ja
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
#include <NXOpen/AME_OrderAspectsBuilder.hxx>
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
        class OrderAspectsBuilder;
    }
    class Builder;
    namespace AME
    {
        class _OrderAspectsBuilderBuilder;
        class OrderAspectsBuilderImpl;
        /**
            Represents a @link OrderAspectsBuilder OrderAspectsBuilder@endlink  for changing the order of Navigator
             <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateOrderAspectsBuilder  NXOpen::AME::AMEManager::CreateOrderAspectsBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  OrderAspectsBuilder : public NXOpen::Builder
        {
            /** possible choices for order of navigator objects */
            public: enum OrderType
            {
                OrderTypeEngineeringObjects/** engineering objects */ ,
                OrderTypeTag/** tag */ ,
                OrderTypeChannel/** channel */ ,
                OrderTypeUpstreamObjects/** upstream objects */ ,
                OrderTypePage/** page */ ,
                OrderTypeFragment/** fragment */ ,
                OrderTypeDocumentStructureNode/** document structure node */ 
            };

            /** possible choices for sorting of navigator objects in a set */
            public: enum SortType
            {
                SortTypeSortbyCreation/** sortby creation */ ,
                SortTypeSortbyName/** sortby name */ 
            };

            private: OrderAspectsBuilderImpl * m_orderaspectsbuilder_impl;
            private: friend class  _OrderAspectsBuilderBuilder;
            protected: OrderAspectsBuilder();
            public: ~OrderAspectsBuilder();
            /** The order for the aspects  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: std::vector<NXOpen::AME::OrderAspectsBuilder::OrderType> GetOrder
            (
            );
            /** The order for the aspects 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetOrder
            (
                const std::vector<NXOpen::AME::OrderAspectsBuilder::OrderType> & order /** order */ 
            );
            /**Sets  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSortFunctionMode
            (
                NXOpen::AME::OrderAspectsBuilder::SortType sort /** sort */ 
            );
            /**Returns  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::OrderAspectsBuilder::SortType SortFunctionMode
            (
            );
            /**Sets  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSortLocationMode
            (
                NXOpen::AME::OrderAspectsBuilder::SortType sort /** sort */ 
            );
            /**Returns  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::OrderAspectsBuilder::SortType SortLocationMode
            (
            );
            /**Sets  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSortProductMode
            (
                NXOpen::AME::OrderAspectsBuilder::SortType sort /** sort */ 
            );
            /**Returns  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::OrderAspectsBuilder::SortType SortProductMode
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
