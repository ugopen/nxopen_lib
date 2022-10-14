#ifndef NXOpen_ROUTING_SPLITDUCTBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_SPLITDUCTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_SplitDuctBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/Routing_DivisionsBuilder.hxx>
#include <NXOpen/Routing_SplitDuctBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class SplitDuctBuilder;
    }
    class Builder;
    namespace Routing
    {
        class DivisionsBuilder;
    }
    namespace Routing
    {
        class Port;
    }
    class TaggedObjectList;
    namespace Routing
    {
        class _SplitDuctBuilderBuilder;
        class SplitDuctBuilderImpl;
        /**
                Represents a @link Routing::SplitDuctBuilder Routing::SplitDuctBuilder@endlink 
                
                Builder for creating/editing splits at an end of a duct.
                Takes an end face of a rectangular stock and splits it into a pair of
                divisions based on the specified absolute flow percentage for each division.
             <br> To create a new instance of this class, use @link Routing::RouteManager::CreateSplitDuctBuilder Routing::RouteManager::CreateSplitDuctBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        FlowType </td> <td> 
         
        AbsoluteFlow </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  SplitDuctBuilder : public Builder
        {
            /**
                        The type of flow, whether Absolute or Relative, to be displayed in the %Flow
                        column in the list.  This also controls the type of flow based on which
                        divisions can be created or edited
                    */
            public: enum FlowTypes
            {
                FlowTypesAbsoluteFlow/** Absolute flow */,
                FlowTypesRelativeFlow/** Relative flow */
            };

            private: SplitDuctBuilderImpl * m_splitductbuilder_impl;
            private: friend class  _SplitDuctBuilderBuilder;
            protected: SplitDuctBuilder();
            public: ~SplitDuctBuilder();
            /**Returns  the divisions list  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::TaggedObjectList * DivisionsList
            (
            );
            /**Returns  the type of flow to be displayed in the list flow column  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SplitDuctBuilder::FlowTypes FlowType
            (
            );
            /**Sets  the type of flow to be displayed in the list flow column  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFlowType
            (
                NXOpen::Routing::SplitDuctBuilder::FlowTypes flowType /** flowtype */ 
            );
            /** Creates a new item for the divisions list in Split Duct dialog  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::DivisionsBuilder * CreateNewDivisionsListItem
            (
                NXOpen::Routing::Port * selectedPort /** Selected port */,
                bool isAbsoluteFlow /** if TRUE: displays absolute flow percentage for each division,
                                                                                                 else displays relative flow percentage */
            );
            /** Creates divisions builders for all the divisions, if any, associated with
                        the cross-section to which the input port belongs and adds them to the list
                        of divisions.
                     <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void AddDivisionsBuilderToList
            (
                NXOpen::Routing::Port * selectedPort /** Selected port */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif