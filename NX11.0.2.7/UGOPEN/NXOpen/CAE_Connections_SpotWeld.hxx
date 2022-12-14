#ifndef NXOpen_CAE_CONNECTIONS_SPOTWELD_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_SPOTWELD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_SpotWeld.ja
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
#include <NXOpen/CAE_Connections_CoordinatesLocation.hxx>
#include <NXOpen/CAE_Connections_Location.hxx>
#include <NXOpen/CAE_Connections_NodeLocation.hxx>
#include <NXOpen/CAE_Connections_PointLocation.hxx>
#include <NXOpen/CAE_Connections_Types.hxx>
#include <NXOpen/CAE_FENode.hxx>
#include <NXOpen/CAE_Connections_IConnectionMod.hxx>
#include <NXOpen/CAE_Connections_IDiameterDefinition.hxx>
#include <NXOpen/CAE_Connections_IFlangeContainer.hxx>
#include <NXOpen/CAE_Connections_IHeightDefinition.hxx>
#include <NXOpen/CAE_Connections_ILocationContainer.hxx>
#include <NXOpen/CAE_Connections_ITolerance.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/ugmath.hxx>
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
            class SpotWeld;
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
            class CoordinatesLocation;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IConnectionMod;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IDiameterDefinition;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IFlangeContainer;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IHeightDefinition;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class ILocationContainer;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class ITolerance;
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
            class NodeLocation;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class PointLocation;
        }
    }
    namespace CAE
    {
        class FENode;
    }
    class Expression;
    class INXObject;
    class Point;
    class TaggedObject;
    namespace CAE
    {
        namespace Connections
        {
            class _SpotWeldBuilder;
            class SpotWeldImpl;
            /** Spot Weld connection. Use this interface to set/get properties and parameters of the spot weld connection.  
             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  SpotWeld : public NXOpen::CAE::Connections::IConnectionMod, public virtual NXOpen::CAE::Connections::ITolerance, public virtual NXOpen::CAE::Connections::IDiameterDefinition, public virtual NXOpen::CAE::Connections::IHeightDefinition, public virtual NXOpen::CAE::Connections::IFlangeContainer, public virtual NXOpen::CAE::Connections::ILocationContainer
            {
                private: SpotWeldImpl * m_spotweld_impl;
                private: friend class  _SpotWeldBuilder;
                protected: SpotWeld();
                public: ~SpotWeld();
                /**Returns  the maximum distance from definition point to center of support element 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * MaxDistCGToElemCG
                (
                );
                /**Returns  the maximum normal distance from definition point to center of element 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * MaxNormalDistCGToFlanges
                (
                );
                /**Returns  the maximum angle of normals with the projection surface 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * MaxAngleOfNormals
                (
                );
                /**Returns  the projection tolerance 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * ProjectTolerance
                (
                );
                /**Returns  the diameter type 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::DiameterType DiameterType
                (
                );
                /**Sets  the diameter type 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetDiameterType
                (
                    NXOpen::CAE::Connections::DiameterType diameterTypeType /** diametertypetype */ 
                );
                /**Returns  the connection diameter 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * Diameter
                (
                );
                /**Returns  the coefficient for formula defined diameter 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * Coefficient
                (
                );
                /**Returns  the height type 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::HeightType HeightType
                (
                );
                /**Sets  the height type 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetHeightType
                (
                    NXOpen::CAE::Connections::HeightType heightType /** Diameter type */
                );
                /**Returns  the height value 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * Height
                (
                );
                /** Gets entities from flange. These can be meshes, elements, groups.  @return  Flange entities 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::TaggedObject *> GetFlangeEntities
                (
                    int flangeIndex /** flangeindex */ 
                );
                /** Add entities to flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void AddFlangeEntities
                (
                    int flangeIndex /** flangeindex */ ,
                    const std::vector<NXOpen::TaggedObject *> & entities /** Flange entities */
                );
                /** Remove entities from flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void RemoveFlangeEntities
                (
                    int flangeIndex /** flangeindex */ ,
                    const std::vector<NXOpen::TaggedObject *> & entities /** Flange entities */
                );
                /**Returns  the number of flanges. When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual int NumberOfFlanges
                (
                );
                /**Sets  the number of flanges. When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetNumberOfFlanges
                (
                    int numberOfFlanges /** numberofflanges */ 
                );
                /** Adds a node location to connection location list  @return  The node type location 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::NodeLocation * AddLocationNode
                (
                    NXOpen::CAE::FENode * node /** Node used for location */
                );
                /** Adds a coordinates location to connection location list  @return  The created coordinates type location 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::CoordinatesLocation * AddLocationCoordinates
                (
                    const NXOpen::Point3d & coordinates /** Coordinates */
                );
                /** Adds a point location to connection location list  @return  The created point type location 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual NXOpen::CAE::Connections::PointLocation * AddLocationPoint
                (
                    NXOpen::Point * point /** Point used for location creation */
                );
                /** Get a node location to connection location list  @return  The location 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::Location * GetLocation
                (
                    int index /** The location index */
                );
                /** Remove a location from connection location list 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void RemoveLocation
                (
                    int index /** The location index */
                );
                /** Get a node location to connection location list  @return  The number of locations 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual int GetNumberOfLocations
                (
                );
                /** Convert a location to coordinates. The location is given by its index 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void ConvertLocationToCoordinatesType
                (
                    int index /** The location index */
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
