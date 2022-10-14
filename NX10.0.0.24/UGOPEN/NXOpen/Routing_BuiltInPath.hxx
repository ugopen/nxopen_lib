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
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetCharacteristics
            (
                NXOpen::Routing::CharacteristicList * values /** values */ 
            );
            /** Get the value of an integer characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual int GetIntegerCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Get the value of an integer characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual int GetIntegerCharacteristic
            (
                const char * name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Set the value of an integer characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to integer if it's 
                        type is not integer. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int value /** value */ 
            );
            /** Set the value of an integer characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to integer if it's 
                        type is not integer. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic
            (
                const char * name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int value /** value */ 
            );
            /** Get the value of a real characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual double GetRealCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Get the value of a real characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual double GetRealCharacteristic
            (
                const char * name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Set the value of an real characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to real if it's 
                        type is not real. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                double value /** value */ 
            );
            /** Set the value of an real characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to real if it's 
                        type is not real. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic
            (
                const char * name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                double value /** value */ 
            );
            /** Get the value of a string characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual NXString GetStringCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Get the value of a string characteristic associated with the input name.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual NXString GetStringCharacteristic
            (
                const char * name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Set the value of an string characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to string if it's 
                        type is not string. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetCharacteristic
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Set the value of an string characteristic associated with the input name,
                        adds a new characteristic to the list if one doesn't exist already. Converts
                        the type of an existing characteristic with the same name to string if it's 
                        type is not string. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            virtual void SetCharacteristic
            (
                const char * name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * value /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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