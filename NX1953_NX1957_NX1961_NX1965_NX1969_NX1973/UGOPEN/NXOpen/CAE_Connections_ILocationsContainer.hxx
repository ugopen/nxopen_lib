#ifndef NXOpen_CAE_CONNECTIONS_ILOCATIONSCONTAINER_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_ILOCATIONSCONTAINER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_ILocationsContainer.ja
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
#include <NXOpen/CAE_Connections_Location.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace Connections
        {
            class ILocationsContainer;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class Location;
        }
    }
    class INXObject;
    namespace CAE
    {
        namespace Connections
        {
            /**  @brief  This class represents an Interface to the Locations parameters.  

              
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ILocationsContainer : public virtual NXOpen::INXObject
            {
                public: virtual ~ILocationsContainer() {}
                /** Get a node location to connection location list  @return  The location 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::Location * GetLocation
                (
                    int indexOfDefinition /** The index of definition  */,
                    int indexOfLocation /** The location index */
                ) = 0;
                /** Remove a location from connection location list 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void RemoveLocation
                (
                    int indexOfDefinition /** The index of definition  */,
                    int indexOfLocation /** The location index */
                ) = 0;
                /** Get a node location to connection location list  @return  The number of locations 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual int GetNumberOfLocations
                (
                    int indexOfDefinition /** The index of definition  */
                ) = 0;
                /** Convert a location to coordinates. The location is given by its index  @return  The created coordinates type location 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::Location * ConvertLocationToCoordinatesType
                (
                    int indexOfDefinition /** The index of definition  */,
                    int index /** The location index */
                ) = 0;
                /** Gets the number of line offset definitions  @return  The number of definitions 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual int GetNumberOfDefinitions
                (
                ) = 0;
                /** Move the location by number of positions  @return  The operation result 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool MoveLocation
                (
                    int indexOfDefinition /** The index of definition  */,
                    int indexOfLocation /** The index of location */,
                    int numberOfPositions /** The number of positions to move the location */
                ) = 0;
            };
        }
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
