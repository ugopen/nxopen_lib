#ifndef NXOpen_ROUTING_ARCSEGMENT_HXX_INCLUDED
#define NXOpen_ROUTING_ARCSEGMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_ArcSegment.ja
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
#include <NXOpen/Arc.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/Routing_ICharacteristic.hxx>
#include <NXOpen/Routing_ISegment.hxx>
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/Routing_SegmentManager.hxx>
#include <NXOpen/ugmath.hxx>
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
        class ArcSegment;
    }
    class Arc;
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class Curve;
    class INXObject;
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        class Corner;
    }
    namespace Routing
    {
        namespace Electrical
        {
            class CableDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class CablewaysLayoutView;
        }
    }
    namespace Routing
    {
        class ICharacteristic;
    }
    namespace Routing
    {
        class ISegment;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        class _ArcSegmentBuilder;
        class ArcSegmentImpl;
        /** Represents a arc segment.  <br> To obtain an instance of this class use @link NXOpen::Routing::SegmentManager NXOpen::Routing::SegmentManager@endlink   <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  ArcSegment : public NXOpen::Arc, public virtual NXOpen::Routing::ISegment
        {
            private: ArcSegmentImpl * m_arcsegment_impl;
            private: friend class  _ArcSegmentBuilder;
            protected: ArcSegment();
            public: ~ArcSegment();
            /** Returns the Globally Unique Identifier (GUID) for this segment.  @return  The GUID for this segment. 
             <br>  Created in NX8.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString GetGuid
            (
            );
            /** Returns the corner that controls this arc segment, if any.
                        Returns NULL if this segment was created as a connected curve rather than
                        from a corner.
                    
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::Corner * GetCorner
            (
            );
            /**  Return of segment end control points.
                         The @link NXOpen::Routing::ControlPoint NXOpen::Routing::ControlPoint@endlink  defines an end of a segment 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual void GetEndRcps
            (
                NXOpen::Routing::ControlPoint ** startRcp /** RCP defining start of segment */,
                NXOpen::Routing::ControlPoint ** endRcp /** RCP defining end of segment */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual void SetEndRcps
            (
                NXOpen::Routing::ControlPoint * startRcp /** RCP defining start of segment */,
                NXOpen::Routing::ControlPoint * endRcp /** RCP defining end of segment */
            );
            /**  Get the current location of the segment ends in ABS coordinates.  This value is
                         overridden by the coordinates of the end RCPs associated with this segment. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual void GetEndPoints
            (
                NXOpen::Point3d* startPoint /** Location of end 0 in ABS coordinates */,
                NXOpen::Point3d* endPoint /** Location of end 1 in ABS coordinates */
            );
            /**  Set the current location of the segment ends in ABS coordinates.  This value is
                         overridden by the coordinates of the end RCPs associated with this segment. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual void SetEndPoints
            (
                const NXOpen::Point3d & startPoint /** New location of end 0 in ABS coordinates */,
                const NXOpen::Point3d & endPoint /** New location of end 1 in ABS coordinates */
            );
            /**Returns   the segment follow curve.  NULL object indicates segment has no follow curve 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual NXOpen::Curve * FollowCurve
            (
            );
            /** Is given segment a terminal segment?  @return  Is segment a terminal segment? 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual NXOpen::Routing::Terminal GetIsTerminalSegment
            (
            );
            /** Set given segment to be a terminal segment? 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual void SetIsTerminalSegment
            (
                NXOpen::Routing::Terminal isTerminal /** Set as terminal segment? */
            );
            /** Query if a segment is interior to any part  @return  Is segment interior? 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual NXOpen::Routing::Interior GetIsSegmentInterior
            (
            );
            /** Set a segment to be interior to supplied part 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual void SetSegmentInteriorPart
            (
                NXOpen::Assemblies::Component * interiorPart /** Part segment interior? */
            );
            /** Returns all stocks that directly reference this segment as part of the path defining the stock.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual std::vector<NXOpen::Routing::Stock *> GetSegmentStock
            (
            );
            /** Returns @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  as well as @link NXOpen::Routing::Overstock NXOpen::Routing::Overstock@endlink 
                        objects from the @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink .  @return  Array of stocks/overstocks. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual std::vector<NXOpen::Routing::Stock *> GetSegmentAllStocks
            (
            );
            /** Returns @link NXOpen::Routing::Electrical::CablewaysLayoutView NXOpen::Routing::Electrical::CablewaysLayoutView@endlink  objects
                        from the @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink .  @return  Array of cableways layout views. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual std::vector<NXOpen::Routing::Electrical::CablewaysLayoutView *> GetCablewaysLayoutViews
            (
            );
            /** Returns @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink  objects
                           from @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink .  @return  Array of cable devices. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual std::vector<NXOpen::Routing::Electrical::CableDevice *> GetCableDevices
            (
            );
            /** Is given segment a eccentric segment?  @return  Is segment a eccentric segment? 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual NXOpen::Routing::Eccentric GetIsEccentricSegment
            (
            );
            /** Is line segment converted to eccentric line segment?  @return  Is line segment converted to eccentric line segment? 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual NXOpen::Routing::ConvertLinearToEccentricLinear ConvertLinearToEccentricLinear
            (
            );
            /** Is line segment eccentric converted to line segment?  @return  Is line segment eccentric converted to line segment? 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual NXOpen::Routing::ConvertEccentricLinearToLinear ConvertEccentricLinearToLinear
            (
            );
            /**Returns   the length of the segment. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: virtual double Length
            (
            );
            /** Get all of the characteristics values on the this object.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual NXOpen::Routing::CharacteristicList * GetCharacteristics
            (
            );
            /** Set all of the characteristics values on this object. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Routing::ICharacteristic::SetCharacteristics2 NXOpen::Routing::ICharacteristic::SetCharacteristics2@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Routing::ICharacteristic::SetCharacteristics2 instead.") virtual void SetCharacteristics
            (
                NXOpen::Routing::CharacteristicList * values /** values */ 
            );
            /** Get the value of an integer characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual int GetIntegerCharacteristic
            (
                const NXString & name /** name */ 
            );
            /** Get the value of an integer characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual int GetIntegerCharacteristic
            (
                const char * name /** name */ 
            );
            /** Set the value of an integer characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to integer if it's 
                        type is not integer. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Routing::ICharacteristic::SetCharacteristic2 NXOpen::Routing::ICharacteristic::SetCharacteristic2@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Routing::ICharacteristic::SetCharacteristic2 instead.") virtual void SetCharacteristic
            (
                const NXString & name /** name */ ,
                int value /** value */ 
            );
            /** Set the value of an integer characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to integer if it's 
                        type is not integer. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Routing::ICharacteristic::SetCharacteristic2 NXOpen::Routing::ICharacteristic::SetCharacteristic2@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic
            (
                const char * name /** name */ ,
                int value /** value */ 
            );
            /** Get the value of a real characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual double GetRealCharacteristic
            (
                const NXString & name /** name */ 
            );
            /** Get the value of a real characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual double GetRealCharacteristic
            (
                const char * name /** name */ 
            );
            /** Set the value of an real characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to real if it's 
                        type is not real. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Routing::ICharacteristic::SetCharacteristic2 NXOpen::Routing::ICharacteristic::SetCharacteristic2@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Routing::ICharacteristic::SetCharacteristic2 instead.") virtual void SetCharacteristic
            (
                const NXString & name /** name */ ,
                double value /** value */ 
            );
            /** Set the value of an real characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to real if it's 
                        type is not real. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Routing::ICharacteristic::SetCharacteristic2 NXOpen::Routing::ICharacteristic::SetCharacteristic2@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic
            (
                const char * name /** name */ ,
                double value /** value */ 
            );
            /** Get the value of a string characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual NXString GetStringCharacteristic
            (
                const NXString & name /** name */ 
            );
            /** Get the value of a string characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual NXString GetStringCharacteristic
            (
                const char * name /** name */ 
            );
            /** Set the value of an string characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to string if it's 
                        type is not string. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Routing::ICharacteristic::SetCharacteristic2 NXOpen::Routing::ICharacteristic::SetCharacteristic2@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Routing::ICharacteristic::SetCharacteristic2 instead.") virtual void SetCharacteristic
            (
                const NXString & name /** name */ ,
                const NXString & value /** value */ 
            );
            /** Set the value of an string characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to string if it's 
                        type is not string. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Routing::ICharacteristic::SetCharacteristic2 NXOpen::Routing::ICharacteristic::SetCharacteristic2@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic
            (
                const char * name /** name */ ,
                const char * value /** value */ 
            );
            /** Removes the input list of characteristics from this object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
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
                     @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual NXOpen::Routing::CharacteristicList * GetDestinationCharacteristics
            (
            );
            /** Sets or creates an integer type attribute associated with the input title. 
                    creating a new attribute if one doesn't exist already. 

                    If the method is called on a stock @link Assemblies::Component Assemblies::Component@endlink , the 
                    method will create or edit a part attribute on the stock part. For legacy parts 
                    where the attribute is on the stock component, the attribute will be moved 
                    to the stock part. 

                    If the method is called on a non-stock @link Assemblies::Component Assemblies::Component@endlink , 
                    the method will create or edit an attribute on the corresponding instance. For 
                    legacy parts where the attribute is on the component, the attribute will be moved 
                    to the corresponding instance. 

                    If the method is called on any non-component object, the method will 
                    access or create an attribute on the object itself. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetCharacteristic2
            (
                const NXString & title /** Unique title for the Attribute or Characteristic */,
                int value /** New Value to be set on the Attribute */
            );
            /** Sets or creates an integer type attribute associated with the input title. 
                    creating a new attribute if one doesn't exist already. 

                    If the method is called on a stock @link Assemblies::Component Assemblies::Component@endlink , the 
                    method will create or edit a part attribute on the stock part. For legacy parts 
                    where the attribute is on the stock component, the attribute will be moved 
                    to the stock part. 

                    If the method is called on a non-stock @link Assemblies::Component Assemblies::Component@endlink , 
                    the method will create or edit an attribute on the corresponding instance. For 
                    legacy parts where the attribute is on the component, the attribute will be moved 
                    to the corresponding instance. 

                    If the method is called on any non-component object, the method will 
                    access or create an attribute on the object itself. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic2
            (
                const char * title /** Unique title for the Attribute or Characteristic */,
                int value /** New Value to be set on the Attribute */
            );
            /** Sets or creates a double type attribute associated with the input title. 
                    creating a new attribute if one doesn't exist already. 

                    If the method is called on a stock @link Assemblies::Component Assemblies::Component@endlink , the 
                    method will create or edit a part attribute on the stock part. For legacy parts 
                    where the attribute is on the stock component, the attribute will be moved 
                    to the stock part. 

                    If the method is called on a non-stock @link Assemblies::Component Assemblies::Component@endlink , 
                    the method will create or edit an attribute on the corresponding instance. For 
                    legacy parts where the attribute is on the component, the attribute will be moved 
                    to the corresponding instance. 

                    If the method is called on any non-component object, the method will 
                    access or create an attribute on the object itself. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetCharacteristic2
            (
                const NXString & title /** Unique title for the Attribute or Characteristic */,
                double value /** New Value to be set on the Attribute */
            );
            /** Sets or creates a double type attribute associated with the input title. 
                    creating a new attribute if one doesn't exist already. 

                    If the method is called on a stock @link Assemblies::Component Assemblies::Component@endlink , the 
                    method will create or edit a part attribute on the stock part. For legacy parts 
                    where the attribute is on the stock component, the attribute will be moved 
                    to the stock part. 

                    If the method is called on a non-stock @link Assemblies::Component Assemblies::Component@endlink , 
                    the method will create or edit an attribute on the corresponding instance. For 
                    legacy parts where the attribute is on the component, the attribute will be moved 
                    to the corresponding instance. 

                    If the method is called on any non-component object, the method will 
                    access or create an attribute on the object itself. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic2
            (
                const char * title /** Unique title for the Attribute or Characteristic */,
                double value /** New Value to be set on the Attribute */
            );
            /** Sets or creates a string type type attribute associated with the input title. 
                    creating a new attribute if one doesn't exist already. 

                    If the method is called on a stock @link Assemblies::Component Assemblies::Component@endlink , the 
                    method will create or edit a part attribute on the stock part. For legacy parts 
                    where the attribute is on the stock component, the attribute will be moved 
                    to the stock part. 

                    If the method is called on a non-stock @link Assemblies::Component Assemblies::Component@endlink , 
                    the method will create or edit an attribute on the corresponding instance. For 
                    legacy parts where the attribute is on the component, the attribute will be moved 
                    to the corresponding instance. 

                    If the method is called on any non-component object, the method will 
                    access or create an attribute on the object itself. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetCharacteristic2
            (
                const NXString & title /** Unique title for the Attribute or Characteristic */,
                const NXString & value /** New Value to be set on the Attribute */
            );
            /** Sets or creates a string type type attribute associated with the input title. 
                    creating a new attribute if one doesn't exist already. 

                    If the method is called on a stock @link Assemblies::Component Assemblies::Component@endlink , the 
                    method will create or edit a part attribute on the stock part. For legacy parts 
                    where the attribute is on the stock component, the attribute will be moved 
                    to the stock part. 

                    If the method is called on a non-stock @link Assemblies::Component Assemblies::Component@endlink , 
                    the method will create or edit an attribute on the corresponding instance. For 
                    legacy parts where the attribute is on the component, the attribute will be moved 
                    to the corresponding instance. 

                    If the method is called on any non-component object, the method will 
                    access or create an attribute on the object itself. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic2
            (
                const char * title /** Unique title for the Attribute or Characteristic */,
                const char * value /** New Value to be set on the Attribute */
            );
            /** Sets all attributes associated with the titles from the input list, 
                    creating new attributes for the ones that don't exist already. 

                    If the method is called on a stock @link Assemblies::Component Assemblies::Component@endlink , the 
                    method will create or edit part attributes on the stock part. For legacy parts 
                    where the attributes are on the stock component, the attributes will be moved 
                    to the stock part. 

                    If the method is called on a non-stock @link Assemblies::Component Assemblies::Component@endlink , 
                    the method will create or edit attributes on the corresponding instance. For 
                    legacy parts where the attribute is on the component, the attributes will be moved 
                    to the corresponding instance. 

                    If the method is called on any non-component object, the method will 
                    access or create attributes on the object itself. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetCharacteristics2
            (
                NXOpen::Routing::CharacteristicList * values /** @link NXOpen::Routing::CharacteristicList NXOpen::Routing::CharacteristicList@endlink  having the titles, types and values of Attributes to be set */
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