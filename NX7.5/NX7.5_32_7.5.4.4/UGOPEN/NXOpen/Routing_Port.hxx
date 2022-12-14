#ifndef NXOpen_ROUTING_PORT_HXX_INCLUDED
#define NXOpen_ROUTING_PORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Port.ja
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
#include <NXOpen/INXObject.hxx>
#include <NXOpen/Routing_ICharacteristic.hxx>
#include <NXOpen/Routing_IRoutePosition.hxx>
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class Port;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class DisplayableObject;
    class Expression;
    class INXObject;
    class Point;
    namespace Positioning
    {
        class Constraint;
    }
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        class FeaturePort;
    }
    namespace Routing
    {
        class ICharacteristic;
    }
    namespace Routing
    {
        class IRoutePosition;
    }
    namespace Routing
    {
        class ISegment;
    }
    namespace Routing
    {
        class PortConnection;
    }
    class SmartObject;
    namespace Routing
    {
        class _PortBuilder;
        class PortImpl;
        /** Routing Port Object is a parent class for FixturePort, ExtractPort, FittingPort,
                Multiport, StockPort and TerminalPort <br> Creator not available in KF. <br> */
        class NXOPENCPPEXPORT  Port : public SmartObject, public virtual Routing::IRoutePosition
        {
            /** Allowed types for ports */
            public: enum PortType
            {
                PortTypeUnknownPort/** Unknown Port*/,
                PortTypeFittingPort/** Fitting Port*/,
                PortTypeFixturePort/** Fixture Port*/,
                PortTypeMultiPort = 4/** Multi Port*/,
                PortTypeTerminalPort = 8/** Terminal Port*/,
                PortTypeStockPort = 16/** Stock Port*/
            };

            /** Allowed types for flow direction */
            public: enum FlowDirectionType
            {
                FlowDirectionTypeRouteFlowEither/** route flow either */ ,
                FlowDirectionTypeRouteFlowIn/** route flow in */ ,
                FlowDirectionTypeRouteFlowOut/** route flow out */ ,
                FlowDirectionTypeFlowNone/** flow none */ 
            };

            private: PortImpl * m_port_impl;
            private: friend class  _PortBuilder;
            protected: Port();
            public: ~Port();
            /** Get the type of Port  @return  Port Type  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::Port::PortType GetPortType
            (
            );
            /** Retrieves the alignment vector of Port  @return  Vector direction in absolute co-ordinate system  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Vector3d GetAlignmentVector
            (
            );
            /** The clock angle increment value of @link Port Port@endlink   @return  Clock increment value in degrees  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetClockIncrement
            (
            );
            /** The clock angle increment value of @link Port Port@endlink   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetClockIncrement
            (
                double increment /** Clock increment value in degrees */
            );
            /** Get the value of flow direction of @link Port Port@endlink   @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::Port::FlowDirectionType GetFlowDirection
            (
            );
            /** Set the flow direction value of @link Port Port@endlink   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFlowDirection
            (
                NXOpen::Routing::Port::FlowDirectionType flowDirection /** flow direction */ 
            );
            /** Retrieves the rotation vector of Port  @return  Vector direction in absolute co-ordinate system  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Vector3d GetRotationVector
            (
            );
            /** Retrieves the object used to derive the rotation vector of Port  @return  Object used to derive the rotation vector  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::DisplayableObject * GetRotationObject
            (
            );
            /** Return the segment the port position and alignment are derived from
                        Returns NULL if the port is not derived from segment  @return  ISegment from which the port is derived  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::ISegment * GetSegment
            (
            );
            /** Returns the forward extension value for a port i.e. the minimum length that
                      * a segment must remain straight coming out of a @link Port Port@endlink   @return  Port extension  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetForwardExtension
            (
            );
            /** Returns the engagement distance of a port, i.e. the distance
                      * behind the port that another fitting or stock may engage  @return  Engagement distance  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetEngagement
            (
            );
            /** Returns the cutback length of a port, i.e. the length along the wire from
                      * the port where individual wires leave a bundle to attach to pins  @return  Cutback length  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetCutbackLength
            (
            );
            /** Searches for an integer characteristics on the port, then on the ports component
                        and prototype port if the port is an occurrence.    @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: int FindPortIntegerCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Searches for a real characteristics on the port, then on the ports component
                        and prototype port if the port is an occurrence.    @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double FindPortRealCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Searches for a string characteristics on the port, then on the ports component
                        and prototype port if the port is an occurrence.    @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString FindPortStringCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the Allow Multiple Connections property for a @link Routing::Port Routing::Port@endlink .
                        The property controls the number of connections that can be routed to this
                        @link Routing::Port Routing::Port@endlink .  Although this can be specified in the
                        Mechanical application, the Electrical application is where this property is most
                        used.
                       <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: bool AllowMultipleConnections
            (
            );
            /**Sets  the Allow Multiple Connections property for a @link Routing::Port Routing::Port@endlink .
                        The property controls the number of connections that can be routed to this
                        @link Routing::Port Routing::Port@endlink .  Although this can be specified in the
                        Mechanical application, the Electrical application is where this property is most
                        used.
                       <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void SetAllowMultipleConnections
            (
                bool allowMultipleConnections /** Should the multiport allow multiple connections? */
            );
            /** Gets a reference characteristic from the port.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetReferenceCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets a reference characteristics on the port.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetReferenceCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Finds another @link Routing::Port Routing::Port@endlink  to connect this port to.  Builds a
                        @link Routing::PortConnection Routing::PortConnection@endlink  object if a connectable port is found.  See
                        @link Routing::PortConnectionCollection::CanPortsConnect Routing::PortConnectionCollection::CanPortsConnect@endlink . Does nothing if
                        this port already has a @link Routing::PortConnection Routing::PortConnection@endlink  object referencing it.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::PortConnection * Connect
            (
            );
            /** Deletes any @link Routing::PortConnection Routing::PortConnection@endlink  objects that reference this port.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void Disconnect
            (
            );
            /**Locks the port engagement using dcm3 constraints @return  Newly created port constraints  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Positioning::Constraint *> LockEngagement
            (
                NXOpen::Routing::Port * portToLock /** porttolock */ 
            );
            /**Locks the port rotation vector using dcm3 constraints @return  Newly created port constraints  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Positioning::Constraint *> LockRotation
            (
                NXOpen::Routing::Port * portToLock /** porttolock */ 
            );
            /**Unlocks the port engagement <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void UnlockEngagement
            (
                NXOpen::Routing::Port * portToUnlock /** porttounlock */ 
            );
            /**Unlocks the port rotation <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void UnlockRotation
            (
                NXOpen::Routing::Port * portToUnlock /** porttounlock */ 
            );
            /**Checks if ports have their rotation vectors locked.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool IsRotationLocked
            (
                NXOpen::Routing::Port * portToCheck /** porttocheck */ 
            );
            /**Checks to see if ports are engaged. @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool IsEngagementLocked
            (
                NXOpen::Routing::Port * portToCheck /** porttocheck */ 
            );
            /**Returns  the clock angle increment expression of a
                       @link Routing::Port Routing::Port@endlink , i.e. an expression
                       representing the minimum angle for clocking the
                       @link Routing::Port Routing::Port@endlink .  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Expression * ClockIncrementObject
            (
            );
            /**Sets  the clock angle increment expression of a
                       @link Routing::Port Routing::Port@endlink , i.e. an expression
                       representing the minimum angle for clocking the
                       @link Routing::Port Routing::Port@endlink .  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetClockIncrementObject
            (
                NXOpen::Expression * increment /** Clock increment expression */
            );
            /** Ask @link Routing::FeaturePort Routing::FeaturePort@endlink  object associated with
                       @link Routing::Port Routing::Port@endlink . Returns  NULL if the port was created
                       in preNX6 release and not converted to @link Routing::FeaturePort Routing::FeaturePort@endlink .
                       To convert @link Routing::Port Routing::Port@endlink  object to @link Routing::FeaturePort Routing::FeaturePort@endlink  object
                       use @link Routing::PortCollection::ConvertToFeatures Routing::PortCollection::ConvertToFeatures@endlink .  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::FeaturePort * AskFeature
            (
            );
            /** Reorders the @link Routing::FeaturePort Routing::FeaturePort@endlink  object associated with
                       @link Routing::Port Routing::Port@endlink  after all of the features on which the
                       port feature depends. Does nothing if the port was created
                       in preNX6 release and not converted to @link Routing::FeaturePort Routing::FeaturePort@endlink .
                       To convert @link Routing::Port Routing::Port@endlink  object to @link Routing::FeaturePort Routing::FeaturePort@endlink  object
                       use @link Routing::PortCollection::ConvertToFeatures Routing::PortCollection::ConvertToFeatures@endlink .  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void ReorderFeature
            (
            );
            /**Returns   the current location of the object in ABS coordinates.  This value is
                          overridden by the coordinates of the point associated with this object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Point3d Position
            (
            );
            /**Sets   the current location of the object in ABS coordinates.  This value is
                          overridden by the coordinates of the point associated with this object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetPosition
            (
                const NXOpen::Point3d & position /** New location of object in ABS coordinates */
            );
            /**Returns  the @link Point Point@endlink  that specifies the location of the
                        @link Routing::IRoutePosition Routing::IRoutePosition@endlink  object.  A NULL object indicates that this
                        object is not associated to any point.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Point * Point
            (
            );
            /**Sets  the @link Point Point@endlink  that specifies the location of the
                        @link Routing::IRoutePosition Routing::IRoutePosition@endlink  object.  A NULL object indicates that this
                        object is not associated to any point.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetPoint
            (
                NXOpen::Point * point /** New location of object in ABS coordinates */
            );
            /** Get all of the characteristics values on the this object.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Routing::CharacteristicList * GetCharacteristics
            (
            );
            /** Set all of the characteristics values on this object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetCharacteristics
            (
                NXOpen::Routing::CharacteristicList * values /** values */ 
            );
            /** Get the value of an integer characteristic associated with the input name.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual int GetIntegerCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Set the value of an integer characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to integer if it's 
                        type is not integer.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int value /** value */ 
            );
            /** Get the value of a real characteristic associated with the input name.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual double GetRealCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Set the value of an real characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to real if it's 
                        type is not real.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                double value /** value */ 
            );
            /** Get the value of a string characteristic associated with the input name.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXString GetStringCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Set the value of an string characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to string if it's 
                        type is not string.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Removes the input list of characteristics from this object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void DeleteCharacterstics
            (
                NXOpen::Routing::CharacteristicList * values /** values */ 
            );
            /**   Returns the destination characteristics from the input object.
                          Retrieves the description of which destination characteristics to read
                          from the application view and then reads those destination 
                          characteristics from the object
                          <ul>
                              <li>Ports: Reads characteristics from the port.</li>
                              <li>RCPs: Attempts to find a port at the RCP, reads characteristics from
                                          the port if it exists, otherwise reads from the
                                          stock associated with the rcp.</li>
                              <li>Segments: Reads characteristics from the stock associated with the segment.</li>
                              <li>Components: Reads characteristics directly from the component.</li>
                              <li>Stock: Reads characteristics from the stock or from the stock's data.</li>
                          </ul>
                     @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Routing::CharacteristicList * GetDestinationCharacteristics
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
