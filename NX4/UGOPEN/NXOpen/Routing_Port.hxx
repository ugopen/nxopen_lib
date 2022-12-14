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
#include <vector>
#include <NXOpen/NXString.hxx>
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
    class BasePart;
    class DisplayableObject;
    class INXObject;
    class NXObject;
    class Point;
    namespace Routing
    {
        class CharacteristicList;
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
    class SmartObject;
    namespace Routing
    {
        class _PortBuilder;
        /** Routing Port Object is a parent class for FixturePort, ExtractPort, FittingPort,
                Multiport, StockPort and TerminalPort <br> Creator not available in KF. <br> */
        class NXOPENCPPEXPORT Port : public SmartObject, public virtual Routing::IRoutePosition
        {
            private: friend class  _PortBuilder;
            protected: Port();
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
                NXOpen::Routing::CharacteristicList * values /** */
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
                int value /** */
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
                double value /** */
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
                NXOpen::Routing::CharacteristicList * values /** */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
