#ifndef NXOpen_ROUTING_TERMINALPORT_HXX_INCLUDED
#define NXOpen_ROUTING_TERMINALPORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_TerminalPort.ja
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
#include <NXOpen/Routing_Port.hxx>
#include <NXOpen/Routing_IAxisPort.hxx>
#include <NXOpen/Routing_ICharacteristic.hxx>
#include <NXOpen/Routing_IRoutePosition.hxx>
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class TerminalPort;
    }
    class BasePart;
    class DisplayableObject;
    class Expression;
    class INXObject;
    class NXObject;
    class Point;
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        class IAxisPort;
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
        class MultiPort;
    }
    namespace Routing
    {
        class Port;
    }
    namespace Routing
    {
        class _TerminalPortBuilder;
        /** Represents a Routing Terminal Port Object@link TerminalPort TerminalPort@endlink .
                These objects are ones to which segments are routed to or from when
                creating a routing path.
              */
        class NXOPENCPPEXPORT TerminalPort : public Routing::Port, public virtual Routing::IAxisPort
        {
            private: friend class  _TerminalPortBuilder;
            protected: TerminalPort();
            /**Returns  the associated multi port of the @link TerminalPort TerminalPort@endlink   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::MultiPort * MultiPort
            (
            );
            /**Returns  the pin identifier of the @link TerminalPort TerminalPort@endlink   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString PinIdentifier
            (
            );
            /**Sets  the pin identifier of the @link TerminalPort TerminalPort@endlink   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetPinIdentifier
            (
                const NXString & pin_identifier /** pin identifier */
            );
            /** Sets the align vector of Port  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetAlignVector
            (
                const NXOpen::Vector3d & vector /** Vector direction in absolute co-ordinate system */
            );
            /** Sets the rotation vector of Port  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetRotationVector
            (
                const NXOpen::Vector3d & vector /** Vector direction in absolute co-ordinate system */
            );
            /** Sets the object used to derive the rotation vector of Port  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetRotationObject
            (
                NXOpen::DisplayableObject * rotationObject /** Object used to derive the rotation vector */
            );
            /** Sets the forward extension value of a port, i.e. the minimum length that
                        a segment must remain straight coming out of a @link Port Port@endlink 
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetForwardExtension
            (
                double forwardExtension /** Port extension */
            );
            /**Returns  the forward extension object of a port, i.e. an expression representing the minimum
                        length that a segment must remain straight coming out of a @link Port Port@endlink 
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Expression * ForwardExtensionObject
            (
            );
            /**Sets  the forward extension object of a port, i.e. an expression representing the minimum
                        length that a segment must remain straight coming out of a @link Port Port@endlink 
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetForwardExtensionObject
            (
                NXOpen::Expression * forwardExtension /** Forward Extension Expression */
            );
            /** The engagment distance of a @link IAxisPort IAxisPort@endlink , i.e. the distance 
                        behind the port that another fitting or stock may engage
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetEngagement
            (
                double engagement /** Engagement distance */
            );
            /**Returns  the engagement object of a port, i.e. an expression representing the
                        distance behind the port that another fitting or stock may engage
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Expression * EngagementObject
            (
            );
            /**Sets  the engagement object of a port, i.e. an expression representing the
                        distance behind the port that another fitting or stock may engage
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetEngagementObject
            (
                NXOpen::Expression * engagement /** Engagement Expression */
            );
            /** Sets the cutback length of a port, i.e. the length along the wire from
                        the port where individual wires leave a bundle to attach to pins
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetCutbackLength
            (
                double cutbackLength /** Cutback Length */
            );
            /**Returns  the cutback length object of a port, i.e. an expression representing the length
                        along the wire from the port where individual wires leave a bundle to attach to pins
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Expression * CutbackLengthObject
            (
            );
            /**Sets  the cutback length object of a port, i.e. an expression representing the length
                        along the wire from the port where individual wires leave a bundle to attach to pins
                       <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetCutbackLengthObject
            (
                NXOpen::Expression * cutbackLength /** Cutback Length Expression */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
