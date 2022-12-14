#ifndef NXOpen_ROUTING_DIVISIONSBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_DIVISIONSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_DivisionsBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Routing_Division.hxx>
#include <NXOpen/Routing_DivisionsBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class DivisionsBuilder;
    }
    class Builder;
    class Expression;
    namespace Routing
    {
        class Division;
    }
    class SelectNXObject;
    namespace Routing
    {
        class _DivisionsBuilderBuilder;
        class DivisionsBuilderImpl;
        /**
                Represents a @link Routing::DivisionsBuilder Routing::DivisionsBuilder@endlink 

                Builder for creating/editing splits at an end of a duct.
                Takes an end face of a rectangular stock and splits it into a pair of
                divisions based on the specified absolute flow percentage for each division.
             <br> To create a new instance of this class, use @link Routing::RouteManager::CreateDivisionsBuilder Routing::RouteManager::CreateDivisionsBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        LeftChildFlow.Value </td> <td> 
         
        50 </td> </tr> 

        <tr><td> 
         
        RightChildFlow.Value </td> <td> 
         
        50 </td> </tr> 

        <tr><td> 
         
        SplitDirection </td> <td> 
         
        SplitVertically </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  DivisionsBuilder : public Builder
        {
            /** The direction in which the cross-section is to be split */
            public: enum SplitDirectionType
            {
                SplitDirectionTypeSplitVertically/** Creates a vertical split */,
                SplitDirectionTypeSplitHorizontally/** Creates a horizontal split */
            };

            private: DivisionsBuilderImpl * m_divisionsbuilder_impl;
            private: friend class  _DivisionsBuilderBuilder;
            protected: DivisionsBuilder();
            public: ~DivisionsBuilder();
            /**Returns  the @link Routing::Port  Routing::Port @endlink  to identify the cross-section that is to be split  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::SelectNXObject * SelectedPort
            (
            );
            /**Returns  the value of percent absolute or relative flow in left (first) child division  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Expression * LeftChildFlow
            (
            );
            /**Returns  the value of percent absolute or relative flow in right (second) child division  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Expression * RightChildFlow
            (
            );
            /**Returns  the direction of split, either vertical or horizontal  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::DivisionsBuilder::SplitDirectionType SplitDirection
            (
            );
            /**Sets  the direction of split, either vertical or horizontal  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetSplitDirection
            (
                NXOpen::Routing::DivisionsBuilder::SplitDirectionType splitDirection /** splitdirection */ 
            );
            /** Creates two new divisions by splitting the parent division.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::Division * CreateDivisions
            (
            );
            /** Gets the division object, if any, associated with the division builder  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::Division * GetDivision
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
