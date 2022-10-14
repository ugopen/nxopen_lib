#ifndef NXOpen_CAE_CONNECTIONS_BOLT_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_BOLT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_Bolt.ja
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
#include <NXOpen/CAE_Connections_LocationWithDir.hxx>
#include <NXOpen/CAE_Connections_SelectionRecipeLocation.hxx>
#include <NXOpen/CAE_Connections_Types.hxx>
#include <NXOpen/CAE_SelectionRecipe.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/CAE_Connections_IConnection.hxx>
#include <NXOpen/CAE_Connections_IDiameter.hxx>
#include <NXOpen/CAE_Connections_IFlangesContainer.hxx>
#include <NXOpen/CAE_Connections_ILocationsContainer.hxx>
#include <NXOpen/CAE_Connections_ILocationsMultiPointContainer.hxx>
#include <NXOpen/CAE_Connections_ILocationsWithDirContainer.hxx>
#include <NXOpen/CAE_Connections_IMaterial.hxx>
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
            class Bolt;
        }
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace CAE
    {
        namespace Connections
        {
            class IConnection;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IDiameter;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IFlangesContainer;
        }
    }
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
            class ILocationsMultiPointContainer;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class ILocationsWithDirContainer;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IMaterial;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class Location;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LocationWithDir;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class SelectionRecipeLocation;
        }
    }
    namespace CAE
    {
        class SelectionRecipe;
    }
    class Direction;
    class Expression;
    class INXObject;
    class PhysicalMaterial;
    class Point;
    class TaggedObject;
    namespace CAE
    {
        namespace Connections
        {
            class _BoltBuilder;
            class BoltImpl;
            /** Bolt connection. Use this interface to set/get properties and parameters of the spot weld connection.   <br> To obtain an instance of this object use the connection creators on the @link CAE::Connections::Folder CAE::Connections::Folder@endlink   <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  Bolt : public NXOpen::CAE::Connections::IConnection, public virtual NXOpen::CAE::Connections::IMaterial, public virtual NXOpen::CAE::Connections::IFlangesContainer, public virtual NXOpen::CAE::Connections::ILocationsContainer, public virtual NXOpen::CAE::Connections::IDiameter, public virtual NXOpen::CAE::Connections::ILocationsWithDirContainer, public virtual NXOpen::CAE::Connections::ILocationsMultiPointContainer
            {
                private: BoltImpl * m_bolt_impl;
                private: friend class  _BoltBuilder;
                protected: Bolt();
                public: ~Bolt();
                /**Returns  the maximum bolt length 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * MaxBoltLength
                (
                );
                /**Returns  the head diameter  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HeadDiameter
                (
                );
                /**Returns  the head diameter coefficient 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HeadDiameterCoefficient
                (
                );
                /**Returns  the head diameter type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::HeadDiameterType HeadDiameterType
                (
                );
                /**Sets  the head diameter type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetHeadDiameterType
                (
                    NXOpen::CAE::Connections::HeadDiameterType param /** Head diameter type */
                );
                /**Returns  the limit bolt length to curve length 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool LimitCurveLength
                (
                );
                /**Sets  the limit bolt length to curve length 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetLimitCurveLength
                (
                    bool param /** Limit curve length*/
                );
                /**Returns  the connection material 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::PhysicalMaterial * Material
                (
                );
                /**Sets  the connection material 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetMaterial
                (
                    NXOpen::PhysicalMaterial * material /** The connection material */
                );
                /** Use this function to check if the connection inherits material from flanges 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool IsInheritedMaterial
                (
                );
                /** Use this function to set inherited material to connection 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetInheritedMaterial
                (
                );
                /** Use this function to check if the connection supports inherited material 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool CanInheritMaterial
                (
                );
                /** Use this function to check if the connection supports having no material 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool CanHaveNoMaterial
                (
                );
                /** Gets entities from flange. These can be meshes, elements, groups.  @return  Flange entities 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::TaggedObject *> GetFlangeEntities
                (
                    int flangeIndex /** flangeindex */ 
                );
                /** Add entities to flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void AddFlangeEntities
                (
                    int flangeIndex /** flangeindex */ ,
                    const std::vector<NXOpen::TaggedObject *> & entities /** Flange entities */
                );
                /** Remove entities from flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void RemoveFlangeEntities
                (
                    int flangeIndex /** flangeindex */ ,
                    const std::vector<NXOpen::TaggedObject *> & entities /** Flange entities */
                );
                /**Returns  the number of flanges. When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual int NumberOfFlanges
                (
                );
                /**Sets  the number of flanges. When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetNumberOfFlanges
                (
                    int numberOfFlanges /** numberofflanges */ 
                );
                /** Retrieve the max number of flanges supported by this connection 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual int GetMaxNumberOfFlanges
                (
                );
                /** Retrieve the minimum number of flanges supported by this connection 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual int GetMinNumberOfFlanges
                (
                );
                /** Get a node location to connection location list  @return  The location 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::Location * GetLocation
                (
                    int indexOfDefinition /** The index of definition  */,
                    int indexOfLocation /** The location index */
                );
                /** Remove a location from connection location list 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void RemoveLocation
                (
                    int indexOfDefinition /** The index of definition  */,
                    int indexOfLocation /** The location index */
                );
                /** Get a node location to connection location list  @return  The number of locations 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual int GetNumberOfLocations
                (
                    int indexOfDefinition /** The index of definition  */
                );
                /** Convert a location to coordinates. The location is given by its index  @return  The created coordinates type location 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::Location * ConvertLocationToCoordinatesType
                (
                    int indexOfDefinition /** The index of definition  */,
                    int index /** The location index */
                );
                /** Gets the number of line offset definitions  @return  The number of definitions 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual int GetNumberOfDefinitions
                (
                );
                /** Move the location by number of positions  @return  The operation result 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool MoveLocation
                (
                    int indexOfDefinition /** The index of definition  */,
                    int indexOfLocation /** The index of location */,
                    int numberOfPositions /** The number of positions to move the location */
                );
                /**Returns  the connection diameter type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::DiameterType DiameterType
                (
                );
                /**Sets  the connection diameter type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetDiameterType
                (
                    NXOpen::CAE::Connections::DiameterType diameterType /** diametertype */ 
                );
                /**Returns  the connection diameter 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * Diameter
                (
                );
                /**Returns  the coefficient for formula defined diameter 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * Coefficient
                (
                );
                /**Returns  the table file used to compute the diameter 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXString TableFile
                (
                );
                /**Sets  the table file used to compute the diameter 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetTableFile
                (
                    const NXString & tableFile /** Full path to the diameter table file. */
                );
                /**Sets  the table file used to compute the diameter 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                virtual void SetTableFile
                (
                    const char * tableFile /** Full path to the diameter table file. */
                );
                /** Gets supported diameter types of connection.  @return  Supported CSys Types 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::CAE::Connections::DiameterType> GetSupportedDiameterTypes
                (
                );
                /** Adds a coordinates location with direction definited by coordinates to connection location list  @return  The created coordinates with direction type location 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::LocationWithDir * AddLocationCoordinatesWithDirectionCoordinates
                (
                    int indexOfDefinition /** The index of definition  */,
                    NXOpen::Point * point /** Location Coordinates */,
                    NXOpen::Point * direction /** Direction Point */
                );
                /** Adds a coordinates location with direction definited by vector to connection location list  @return  The created point with direction type location 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::LocationWithDir * AddLocationCoordinatesWithDirectionVector
                (
                    int indexOfDefinition /** The index of definition  */,
                    NXOpen::Point * masterPoint /** Location Coordinates */,
                    NXOpen::Direction * direction /** Direction direction */
                );
                /** Adds a coordinates location with direction definited by vector to connection location list  @return  The created point with direction type location 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::LocationWithDir * AddLocationCoordinatesWithDirectionSelectionRecipes
                (
                    int indexOfDefinition /** The index of definition  */,
                    NXOpen::CAE::SelectionRecipe * startSelectionRecipe /** The start Selection Recipe */,
                    NXOpen::CAE::SelectionRecipe * endSelectionRecipe /** The end Selection Recipe */
                );
                /** Adds a Selection Recipe to connection location list  @return  The created selection recipe type location 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::SelectionRecipeLocation * AddLocationSelectionRecipe
                (
                    int indexOfDefinition /** The index of definition  */,
                    NXOpen::CAE::SelectionRecipe * selectionRecipe /** Selection Recipe used for location creation */
                );
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