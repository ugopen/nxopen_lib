#ifndef NXOpen_ROUTING_ELECTRICAL_SYSTEMDEVICE_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_SYSTEMDEVICE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_SystemDevice.ja
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
#include <NXOpen/Routing_Electrical_HarnessDevice.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class SystemDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class HarnessDevice;
        }
    }
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
            class _SystemDeviceBuilder;
            class SystemDeviceImpl;
            /**
                        The Electrical SystemDevice corresponds to a system instance of the 
                        @link NXOpen::Routing::SingleDevice NXOpen::Routing::SingleDevice@endlink .
                     <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::SystemDeviceCollection::CreateSystemDevice  NXOpen::Routing::Electrical::SystemDeviceCollection::CreateSystemDevice @endlink  <br> 
             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_ROUTINGEXPORT  SystemDevice : public NXOpen::Routing::Electrical::HarnessDevice
            {
                private: SystemDeviceImpl * m_systemdevice_impl;
                private: friend class  _SystemDeviceBuilder;
                protected: SystemDevice();
                public: ~SystemDevice();
                /** Returns the @link NXOpen::Routing::Electrical::SystemDefinition NXOpen::Routing::Electrical::SystemDefinition@endlink 
                                used by this @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink .  @return  The @link NXOpen::Routing::Electrical::SystemDefinition NXOpen::Routing::Electrical::SystemDefinition@endlink  used by this @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink . 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: NXOpen::Routing::Electrical::SystemDefinition * GetSystemDefinition
                (
                );
            };
        }
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
