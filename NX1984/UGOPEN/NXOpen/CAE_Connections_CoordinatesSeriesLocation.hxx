#ifndef NXOpen_CAE_CONNECTIONS_COORDINATESSERIESLOCATION_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_COORDINATESSERIESLOCATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_CoordinatesSeriesLocation.ja
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
            class CoordinatesSeriesLocation;
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
            class _CoordinatesSeriesLocationBuilder;
            class CoordinatesSeriesLocationImpl;
            /**  @brief  Location interface. This defines connection locations with common properties like coordinates.  

               <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  CoordinatesSeriesLocation : public NXOpen::CAE::Connections::Location
            {
                private: CoordinatesSeriesLocationImpl * m_coordinatesserieslocation_impl;
                private: friend class  _CoordinatesSeriesLocationBuilder;
                protected: CoordinatesSeriesLocation();
                public: ~CoordinatesSeriesLocation();
                /** Gets the coordinates from the specified location.
                                The location can be any type: coordinates, node or point.
                                Its coordinates will be returned.  @return  Location coordinates 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::Point3d> GetCoordinates
                (
                );
                /** Set the coordinates. Only for coordinates type location 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetCoordinates
                (
                    const std::vector<NXOpen::Point3d> & coordinates /** The location coordinates */
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