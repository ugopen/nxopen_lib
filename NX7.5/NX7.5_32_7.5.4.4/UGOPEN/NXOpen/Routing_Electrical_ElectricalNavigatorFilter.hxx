#ifndef NXOpen_ROUTING_ELECTRICAL_ELECTRICALNAVIGATORFILTER_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_ELECTRICALNAVIGATORFILTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_ElectricalNavigatorFilter.ja
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
#include <NXOpen/NavigatorFilter.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class ElectricalNavigatorFilter;
        }
    }
    class NavigatorFilter;
    namespace Routing
    {
        namespace Electrical
        {
            class _ElectricalNavigatorFilterBuilder;
            class ElectricalNavigatorFilterImpl;
            /** Represents a Routing Electrical Navigator Filter object.
                      <br> To create an  instance of this class use @link Routing::Electrical::ElectricalNavigatorFilterCollection Routing::Electrical::ElectricalNavigatorFilterCollection@endlink  <br> */
            class NXOPENCPPEXPORT  ElectricalNavigatorFilter : public NavigatorFilter
            {
                private: ElectricalNavigatorFilterImpl * m_electricalnavigatorfilter_impl;
                private: friend class  _ElectricalNavigatorFilterBuilder;
                protected: ElectricalNavigatorFilter();
                public: ~ElectricalNavigatorFilter();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
