#ifndef NXOpen_CAE_CONNECTIONS_CONNECTIONDBDATA_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_CONNECTIONDBDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_ConnectionDBData.ja
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
#include <NXOpen/CAE_Connections_ConnectionDBItemData.hxx>
#include <NXOpen/TaggedObject.hxx>
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
            class ConnectionDBData;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class ConnectionDBItemData;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class _ConnectionDBDataBuilder;
            class ConnectionDBDataImpl;
            /** Connection DB data. Use this interface to set/get properties and parameters of the connection DB data.  
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ConnectionDBData : public NXOpen::TaggedObject
            {
                private: ConnectionDBDataImpl * m_connectiondbdata_impl;
                private: friend class  _ConnectionDBDataBuilder;
                protected: ConnectionDBData();
                public: ~ConnectionDBData();
                /** Gets connection DB item datas.  @return  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Connections::ConnectionDBItemData *> GetConnectionDBItemDatas
                (
                );
                /** Sets connection DB item datas. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetConnectionDBItemDatas
                (
                    const std::vector<NXOpen::CAE::Connections::ConnectionDBItemData *> & components /** components */ 
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
