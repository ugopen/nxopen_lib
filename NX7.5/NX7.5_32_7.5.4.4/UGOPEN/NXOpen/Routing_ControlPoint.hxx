#ifndef NXOpen_ROUTING_CONTROLPOINT_HXX_INCLUDED
#define NXOpen_ROUTING_CONTROLPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_ControlPoint.ja
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
        class ControlPoint;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    class NXObject;
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
        class _ControlPointBuilder;
        class ControlPointImpl;
        /** 
                Routing Control Points define a position in space, and are used to determine connections
                from segments to segments, and segments to ports.
             <br> To create an instace of this object use @link Routing::ControlPointCollection::CreateControlPoint Routing::ControlPointCollection::CreateControlPoint@endlink  <br> */
        class NXOPENCPPEXPORT  ControlPoint : public SmartObject, public virtual Routing::IRoutePosition
        {
            /** User defined status for a @link ControlPoint ControlPoint@endlink . */
            public: enum DefinedStatus
            {
                DefinedStatusSystem/** Created automatically by the application. */,
                DefinedStatusUser/** Created by the user. */
            };

            private: ControlPointImpl * m_controlpoint_impl;
            private: friend class  _ControlPointBuilder;
            protected: ControlPoint();
            public: ~ControlPoint();
            /** Returns whether this object is defined by a user or 
                        automatically by the Routing Application.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::ControlPoint::DefinedStatus GetIsUserDefined
            (
            );
            /** Returns all segments whose start or end Control Point is this Control Point.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::ISegment *> GetRcpSegments
            (
            );
            /** Remove the assigned corner.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void RemoveCorner
            (
            );
            /** Places the default elbow at this object.  
                     
                        Finds the default elbow by searching through the default elbow part
                        table (see @link Preferences::RoutingPart Preferences::RoutingPart@endlink  using the destination
                        characteristics assigned to the stock on this object.
                     
                        Uses the ALLOW_DEFAULT_ELBOW_PLACEMENT plugin to determine if an elbow can be 
                        placed at this object.
                     @return  the placed elbow component, NULL if
                                                            placement fails.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Assemblies::Component * AssignDefaultElbow
            (
            );
            /** Ensures that a touch constraint exists between this 
                        control point and the input object.  Creates a constraint if one 
                        doesn't exist already.

                        This control point must not be an occurrence, the input object may
                        be an occurrence.

                        See @link Positioning::Constraint Positioning::Constraint@endlink  for a description of 
                        touch constraints.

                        Do not attempt to lock control points to @link Routing::ISegment Routing::ISegment@endlink 
                        or @link Routing::Stock Routing::Stock@endlink  objects, this will result in 
                        upredictable behavior.
                     @return  The new or existing touch constraint.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Positioning::Constraint * LockToObject
            (
                NXOpen::NXObject * object /** Object to constraint to control point. */
            );
            /**  Removes the touch constraint that exists between the 
                         control point and the input object.  This control point must not be 
                         an occurrence, the input object may be an occurrence.

                         Call @link Update::DoUpdate Update::DoUpdate@endlink  afterwards to ensure that
                         the constraint is fully deleted.
                      <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void UnlockFromObject
            (
                NXOpen::NXObject * object /** Object constrained to control point. */
            );
            /**  Returns whether or not a touch constraint exists between the 
                         control point and the input object.  

                         This control point must not be an occurrence, the input object may
                         be an occurrence.
                      @return  Whether or not the 
                                                                        control point is 
                                                                        constained to the object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool IsLockedToObject
            (
                NXOpen::NXObject * object /** Object constrained to control point. */
            );
            /** Returns defining object for this @link ControlPoint ControlPoint@endlink .  @return  Object defining control point.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::NXObject * GetDefiningObject
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
