#ifndef NXOpen_CAE_QUALITYAUDIT_NONMODELEDCONNECTIONRESULT_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_NONMODELEDCONNECTIONRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_NonModeledConnectionResult.ja
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
            class NonModeledConnectionResult;
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
            class _NonModeledConnectionResultBuilder;
            class NonModeledConnectionResultImpl;
            /**  @brief  This is a class containing information about the non modeled universal connections. It is in the results of @link NXOpen::CAE::QualityAudit::ListNonModeledConnections NXOpen::CAE::QualityAudit::ListNonModeledConnections@endlink  

               <br> To obtain this type of results see @link CAE::QualityAudit::ListNonModeledConnections CAE::QualityAudit::ListNonModeledConnections@endlink .  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  NonModeledConnectionResult : public NXOpen::CAE::QualityAudit::Result
            {
                private: NonModeledConnectionResultImpl * m_nonmodeledconnectionresult_impl;
                private: friend class  _NonModeledConnectionResultBuilder;
                protected: NonModeledConnectionResult();
                public: ~NonModeledConnectionResult();
                /**Returns  the connection not being modeled 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::IConnection * Connection
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