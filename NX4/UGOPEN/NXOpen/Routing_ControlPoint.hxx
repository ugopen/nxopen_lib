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
        class ControlPoint;
    }
    class BasePart;
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
    class SmartObject;
    namespace Routing
    {
        class _ControlPointBuilder;
        /** 
                Routing Control Points define a position in space, and are used to determine connections
                from segments to segments, and segments to ports.
            */
        class NXOPENCPPEXPORT ControlPoint : public SmartObject, public virtual Routing::IRoutePosition
        {
            /** User defined status for a @link ControlPoint ControlPoint@endlink . */
            public: enum DefinedStatus
            {
                DefinedStatusSystem/** Created automatically by the application. */,
                DefinedStatusUser/** Created by the user. */
            };

            private: friend class  _ControlPointBuilder;
            protected: ControlPoint();
            /** Returns whether this object is defined by a user or 
                        automatically by the Routing Application.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::ControlPoint::DefinedStatus GetIsUserDefined
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
