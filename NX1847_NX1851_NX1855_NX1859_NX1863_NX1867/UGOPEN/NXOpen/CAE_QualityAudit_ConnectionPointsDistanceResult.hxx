#ifndef NXOpen_CAE_QUALITYAUDIT_CONNECTIONPOINTSDISTANCERESULT_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_CONNECTIONPOINTSDISTANCERESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_ConnectionPointsDistanceResult.ja
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
#include <NXOpen/CAE_Connections_IConnection.hxx>
#include <NXOpen/CAE_QualityAudit_Result.hxx>
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
        namespace QualityAudit
        {
            class ConnectionPointsDistanceResult;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IConnection;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class Result;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class _ConnectionPointsDistanceResultBuilder;
            class ConnectionPointsDistanceResultImpl;
            /**  @brief  The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection points checks on universal connections. 

               <br> To obtain this type of results see @link CAE::QualityAudit::ConnectionPointsDistanceCheck CAE::QualityAudit::ConnectionPointsDistanceCheck@endlink .  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ConnectionPointsDistanceResult : public NXOpen::CAE::QualityAudit::Result
            {
                private: ConnectionPointsDistanceResultImpl * m_connectionpointsdistanceresult_impl;
                private: friend class  _ConnectionPointsDistanceResultBuilder;
                protected: ConnectionPointsDistanceResult();
                public: ~ConnectionPointsDistanceResult();
                /**Returns  the connection. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::IConnection * Connection
                (
                );
                /**Returns  the definition index of the first point. See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int DefinitionIndex1
                (
                );
                /**Returns  the definition index of the second point. See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int DefinitionIndex2
                (
                );
                /**Returns  the location index of the first point. See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int LocationIndex1
                (
                );
                /**Returns  the location index of the second point. See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int LocationIndex2
                (
                );
                /**Returns  the coordinate index of the first point in the first location. See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int CoordinateIndex1
                (
                );
                /**Returns  the coordinate index of the second point in the second location. See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int CoordinateIndex2
                (
                );
                /**Returns  the distance between the two points.  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: double Distance
                (
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
