#ifndef NXOpen_CAE_CONNECTIONS_CURVELOCATION_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_CURVELOCATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_CurveLocation.ja
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
            class CurveLocation;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class Location;
        }
    }
    class IBaseCurve;
    namespace CAE
    {
        namespace Connections
        {
            class _CurveLocationBuilder;
            class CurveLocationImpl;
            /**  @brief  Location interface. This defines connection locations with common properties like coordinates.  

               <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  CurveLocation : public NXOpen::CAE::Connections::Location
            {
                private: CurveLocationImpl * m_curvelocation_impl;
                private: friend class  _CurveLocationBuilder;
                protected: CurveLocation();
                public: ~CurveLocation();
                /**Returns  the CURVE used for creating the location.
                                If the location type is not curve, this method will raise an error. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::IBaseCurve * Curve
                (
                );
                /**Sets  the CURVE used for creating the location.
                                If the location type is not curve, this method will raise an error. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetCurve
                (
                    NXOpen::IBaseCurve * curve /** Curve used for location */
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
