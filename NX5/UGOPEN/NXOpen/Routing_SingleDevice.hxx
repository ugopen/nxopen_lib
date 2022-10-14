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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Routing_RouteObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /**
                The Routing SingleDevice corresponds to an abstract instance of @link Routing::ItemDefinition Routing::ItemDefinition@endlink .
             <br> Creator not available in KF. <br> */
        class NXOPENCPPEXPORT SingleDevice : public Routing::RouteObject
        {
            /** Deletion result */
            public: enum DeleteObjectResult
            {
                DeleteObjectResultOk/** ok */ ,
                DeleteObjectResultStillRouted/** still routed */ ,
                DeleteObjectResultCantDeleteImported/** cant delete imported */ ,
                DeleteObjectResultStillAssigned/** still assigned */ ,
                DeleteObjectResultDeviceHasRelated/** device has related */ ,
                DeleteObjectResultCantDeleteUnknown/** cant delete unknown */ 
            };

            private: friend class  _SingleDeviceBuilder;
            protected: SingleDevice();
            /**Returns  the NX equivalent object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::NXObject * NxEquivalent
            (
            );
            /**Sets  the NX equivalent object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetNxEquivalent
            (
                NXOpen::NXObject * route_nx_equivalent /** route nx equivalent */ 
            );
            /** Gets referencing device relationships.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::DeviceRelationship *> GetReferencingDeviceRelshps
            (
            );
            /** Assuming this single device to be the relating single device in a
                    @link Routing::DeviceRelationship Routing::DeviceRelationship@endlink , get associated related single devices.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::SingleDevice *> GetRelatedSingleDevices
            (
            );
            /** Assuming this single device to be the related single device in a
                    @link Routing::DeviceRelationship Routing::DeviceRelationship@endlink , get associated relating single device.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SingleDevice * GetRelatingSingleDevice
            (
            );
            /** Gets connections implemented on single device. @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::LogicalConnection *> GetImplementedConnections
            (
            );
            /**Returns  the part name  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString PartName
            (
            );
            /**Sets  the part name  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetPartName
            (
                const NXString & route_part_name /** route part name */ 
            );
            /**Returns  the part number  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString PartNumber
            (
            );
            /**Sets  the part number  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetPartNumber
            (
                const NXString & route_part_number /** route part number */ 
            );
            /** Deletes the single device.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SingleDevice::DeleteObjectResult ManuallyDelete
            (
            );
            /** Get item definition.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: NXOpen::Routing::ItemDefinition * GetItemDefinition
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif