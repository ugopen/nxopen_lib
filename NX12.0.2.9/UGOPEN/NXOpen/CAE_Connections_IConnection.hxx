#ifndef NXOpen_CAE_CONNECTIONS_ICONNECTION_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_ICONNECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_IConnection.ja
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
#include <NXOpen/DisplayableObject.hxx>
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
            class IConnection;
        }
    }
    class DisplayableObject;
    namespace CAE
    {
        namespace Connections
        {
            class _IConnectionBuilder;
            class IConnectionImpl;
            /**  @brief  This class represents an interface to a connection object.  

               <br> This is an abstract class, and cannot be created.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  IConnection : public NXOpen::DisplayableObject
            {
                private: IConnectionImpl * m_iconnection_impl;
                private: friend class  _IConnectionBuilder;
                protected: IConnection();
                public: ~IConnection();
                /**Returns  the connection user description 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString UserDescription
                (
                );
                /**Sets  the connection user description 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetUserDescription
                (
                    const NXString & description /** User description of the connection */
                );
                /**Sets  the connection user description 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                void SetUserDescription
                (
                    const char * description /** User description of the connection */
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
