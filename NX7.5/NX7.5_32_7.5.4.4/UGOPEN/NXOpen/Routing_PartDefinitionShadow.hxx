#ifndef NXOpen_ROUTING_PARTDEFINITIONSHADOW_HXX_INCLUDED
#define NXOpen_ROUTING_PARTDEFINITIONSHADOW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_PartDefinitionShadow.ja
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
        class PartDefinitionShadow;
    }
    namespace Routing
    {
        class InterfaceTerminalShadow;
    }
    namespace Routing
    {
        class ItemDefinition;
    }
    namespace Routing
    {
        class _PartDefinitionShadowBuilder;
        class PartDefinitionShadowImpl;
        /**
                
                @link Routing::PartDefinitionShadow Routing::PartDefinitionShadow@endlink  contains the defining data for a
                logical part, such as an connector.
                @link Routing::PartDefinitionShadow Routing::PartDefinitionShadow@endlink s contains a list of
                @link Routing::InterfaceTerminalShadow Routing::InterfaceTerminalShadow@endlink s.  Component assignment
                associates the physical NX component to the logical component defined by this
                @link Routing::PartDefinitionShadow Routing::PartDefinitionShadow@endlink .
                
                 <br> 
                See NX Routing help for the Connectivity data model documentation.
                 <br> 
             <br> Creator not available in KF. <br> */
        class NXOPENCPPEXPORT  PartDefinitionShadow : public Routing::ItemDefinition
        {
            private: PartDefinitionShadowImpl * m_partdefinitionshadow_impl;
            private: friend class  _PartDefinitionShadowBuilder;
            protected: PartDefinitionShadow();
            public: ~PartDefinitionShadow();
            /** Returns the
                        @link Routing::PartDefinitionShadow Routing::PartDefinitionShadow@endlink 's associated
                        @link Routing::InterfaceTerminalShadow Routing::InterfaceTerminalShadow@endlink s.
                     @return  The @link Routing::InterfaceTerminalShadow Routing::InterfaceTerminalShadow@endlink s
                                                                for this @link Routing::PartDefinitionShadow Routing::PartDefinitionShadow@endlink   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::InterfaceTerminalShadow *> GetInterfaceTerminalShadows
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
