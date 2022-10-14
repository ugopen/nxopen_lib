#ifndef NXOpen_ROUTING_STOCKDEFINITION_HXX_INCLUDED
#define NXOpen_ROUTING_STOCKDEFINITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_StockDefinition.ja
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
#include <NXOpen/Routing_ItemDefinition.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class StockDefinition;
    }
    namespace Routing
    {
        class ItemDefinition;
    }
    namespace Routing
    {
        class _StockDefinitionBuilder;
        class StockDefinitionImpl;
        /** Represents Routing StockDefinition object  <br> Creator not available in KF. <br> */
        class NXOPENCPPEXPORT  StockDefinition : public Routing::ItemDefinition
        {
            private: StockDefinitionImpl * m_stockdefinition_impl;
            private: friend class  _StockDefinitionBuilder;
            protected: StockDefinition();
            public: ~StockDefinition();
            /**Returns  the outer diameter  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double OuterDiameter
            (
            );
            /**Sets  the outer diameter  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetOuterDiameter
            (
                double diameter /** diameter */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif