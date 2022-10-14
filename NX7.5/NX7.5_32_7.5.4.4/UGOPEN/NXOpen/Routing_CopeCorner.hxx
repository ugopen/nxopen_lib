#ifndef NXOpen_ROUTING_COPECORNER_HXX_INCLUDED
#define NXOpen_ROUTING_COPECORNER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_CopeCorner.ja
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
#include <NXOpen/Routing_Corner.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class CopeCorner;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Routing
    {
        class Corner;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        class _CopeCornerBuilder;
        class CopeCornerImpl;
        /** 
                The cope corner is a corenr that trims stocks at a junction.  Each stock in the cope 
                trims in successive order to all of the previous stocks.  The first stock in the
                cope is not trimmed.
              <br> To create a new instance of this class, use @link Routing::CopeCornerCollection::AssignCopeCorner Routing::CopeCornerCollection::AssignCopeCorner@endlink  <br> */
        class NXOPENCPPEXPORT  CopeCorner : public Routing::Corner
        {
            private: CopeCornerImpl * m_copecorner_impl;
            private: friend class  _CopeCornerBuilder;
            protected: CopeCorner();
            public: ~CopeCorner();
            /** Returns the list of ROUTE_COPE features created to trim stocks.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Features::Feature *> GetFeatures
            (
            );
            /** Get ROUTE_COPE feature applied the given stock at the cope corner  @return  Cope feature at the given stock.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Features::Feature * GetStockCopeFeature
            (
                NXOpen::Routing::Stock * stock /** stock */ 
            );
            /** Set the ordered list of stocks to cope.  The stocks must follow
                       segments which are attached the control point of this cope.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetCopeStocks
            (
                const std::vector<NXOpen::Routing::Stock *> & copeStocks /** cope stocks */ 
            );
            /** Returns the ordered list of stocks coped at this corner.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::Stock *> GetCopeStocks
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif