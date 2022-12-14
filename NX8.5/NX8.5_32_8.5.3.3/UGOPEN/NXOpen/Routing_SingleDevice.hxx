#ifndef NXOpen_ROUTING_SINGLEDEVICE_HXX_INCLUDED
#define NXOpen_ROUTING_SINGLEDEVICE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_SingleDevice.ja
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
#include <NXOpen/Routing_RouteObject.hxx>
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
        class SingleDevice;
    }
    class NXObject;
    namespace Routing
    {
        class DeviceRelationship;
    }
    namespace Routing
    {
        class ItemDefinition;
    }
    namespace Routing
    {
        class LogicalConnection;
    }
    namespace Routing
    {
        class RouteObject;
    }
    namespace Routing
    {
        class _SingleDeviceBuilder;
        class SingleDeviceImpl;
        /**
                The Routing SingleDevice corresponds to an abstract instance of @link Routing::ItemDefinition Routing::ItemDefinition@endlink .
             <br> Creator not available in KF.  <br> 
         <br>  Created in NX4.0.2.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  SingleDevice : public Routing::RouteObject
        {
            /** Deletion result */
            public: enum DeleteObjectResult
            {
                DeleteObjectResultOk/** Single Device deleted successfully. */,
                DeleteObjectResultStillRouted/** Routed connections will not be deleted.
                                                                                         Unroute before deleting. */,
                DeleteObjectResultStillAssigned/** Assigned components will not be deleted.
                                                                                           Unassign before deleting. */,
                DeleteObjectResultCantDeleteUnknown/** Unknown error occurred while deleting.
                                                                                               Please report this as an Incident Report. */
            };

            private: SingleDeviceImpl * m_singledevice_impl;
            private: friend class  _SingleDeviceBuilder;
            protected: SingleDevice();
            public: ~SingleDevice();
            /**Returns  the NX equivalent object. 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::NXObject * NxEquivalent
            (
            );
            /**Sets  the NX equivalent object. 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetNxEquivalent
            (
                NXOpen::NXObject * routeNxEquivalent /** route nx equivalent */ 
            );
            /** Gets referencing device relationships.  @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::DeviceRelationship *> GetReferencingDeviceRelshps
            (
            );
            /** Assuming this single device to be the relating single device in a
                    @link Routing::DeviceRelationship Routing::DeviceRelationship@endlink , get associated related single devices.  @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::SingleDevice *> GetRelatedSingleDevices
            (
            );
            /** Assuming this single device to be the related single device in a
                    @link Routing::DeviceRelationship Routing::DeviceRelationship@endlink , get associated relating single device.  @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::SingleDevice * GetRelatingSingleDevice
            (
            );
            /** Gets connections implemented on single device. @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::LogicalConnection *> GetImplementedConnections
            (
            );
            /**Returns  the part name 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXString PartName
            (
            );
            /**Sets  the part name 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetPartName
            (
                const NXString & routePartName /** route part name */ 
            );
            /**Sets  the part name 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            void SetPartName
            (
                const char * routePartName /** route part name */ 
            );
            /**Returns  the part number 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXString PartNumber
            (
            );
            /**Sets  the part number 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetPartNumber
            (
                const NXString & routePartNumber /** route part number */ 
            );
            /**Sets  the part number 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            void SetPartNumber
            (
                const char * routePartNumber /** route part number */ 
            );
            /** Deletes the single device.  @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::SingleDevice::DeleteObjectResult ManuallyDelete
            (
            );
            /** Get item definition.  @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::ItemDefinition * GetItemDefinition
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
