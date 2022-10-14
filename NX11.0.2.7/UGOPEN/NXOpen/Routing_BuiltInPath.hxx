#ifndef NXOpen_ROUTING_BUILTINPATH_HXX_INCLUDED
#define NXOpen_ROUTING_BUILTINPATH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_BuiltInPath.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_ICharacteristic.hxx>
#include <NXOpen/Routing_CharacteristicList.hxx>
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
        class BuiltInPath;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class Curve;
    class INXObject;
    class NXObject;
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
        class _BuiltInPathBuilder;
        class BuiltInPathImpl;
        /** 
                The Routing BuiltInPath object stores a set of curves.  Routing will attempt to create
                segments on top of these curves whenever an instance of the part containing the 
                BuiltInPath is added to the assembly.   
              <br> To create a new instance of this class, use @link NXOpen::Routing::BuiltInPathCollection::CreateBuiltInPath  NXOpen::Routing::BuiltInPathCollection::CreateBuiltInPath @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  BuiltInPath : public NXOpen::NXObject, public virtual NXOpen::Routing::ICharacteristic
        {
            private: BuiltInPathImpl * m_builtinpath_impl;
            private: friend class  _BuiltInPathBuilder;
            protected: BuiltInPath();
            public: ~BuiltInPath();
            /** Returns the array of curves referenced by the Built-In-Path object.  These curves
                     are in the same part as the Built-In-Path object, and are the curves extracted into the
                     Work Part for the @link Routing::BuiltInPath::CreateSegments Routing::BuiltInPath::CreateSegments@endlink  method.  @return  the array of Curves referenced by the Built-In-Path 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Curve *> GetCurves
            (
            );
            /** Sets the array of curves referenced by the Built-In-Path object.  These curves
                     are in the same part as the Built-In-Path object, and are the curves extracted into the
                     Work Part for the @link Routing::BuiltInPath::CreateSegments Routing::BuiltInPath::CreateSegments@endlink  method. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetCurves
            (
                const std::vector<NXOpen::Curve *> & curves /** the array of Curves to be referenced by the Built-In-Path */
            );
            /** Creates the segments in the work part to cover any curves referenced by the
                        Routing.BuiltInPath object in the component part file. 
                         <br> 
                          Finds the segments currently extracted from the part occurrence and
                          creates a new segment overy every Routing.BuiltInPath curve occurrence that doesn't
                          already have a segment.
                         <br>   @return  the array of Segments referenced by the BuiltInPath includes 
                                                        previously created segments as well. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Curve *> CreateSegments
            (
                NXOpen::Assemblies::Component * partOcc /** Component to extract segments from. */
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
            public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Routing::ICharacteristic::SetCharacteristics2 instead.") virtual void SetCharacteristics
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
            public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Routing::ICharacteristic::SetCharacteristic2 instead.") virtual void SetCharacteristic
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
            public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Routing::ICharacteristic::SetCharacteristic2 instead.") virtual void SetCharacteristic
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
            public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Routing::ICharacteristic::SetCharacteristic2 instead.") virtual void SetCharacteristic
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