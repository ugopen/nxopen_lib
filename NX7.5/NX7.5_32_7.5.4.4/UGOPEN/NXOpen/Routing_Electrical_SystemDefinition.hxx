#ifndef NXOpen_ROUTING_ELECTRICAL_SYSTEMDEFINITION_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_SYSTEMDEFINITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_SystemDefinition.ja
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
#include <NXOpen/Routing_Electrical_HarnessDefinition.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class SystemDefinition;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class HarnessDefinition;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class _SystemDefinitionBuilder;
            class SystemDefinitionImpl;
            /** Represents a @link Routing::Electrical::SystemDefinition Routing::Electrical::SystemDefinition@endlink   <br> Creator not available in KF. <br> */
            class NXOPENCPPEXPORT  SystemDefinition : public Routing::Electrical::HarnessDefinition
            {
                private: SystemDefinitionImpl * m_systemdefinition_impl;
                private: friend class  _SystemDefinitionBuilder;
                protected: SystemDefinition();
                public: ~SystemDefinition();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif