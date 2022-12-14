#ifndef NXOpen_CAE_CONNECTIONS_ICONNECTIONMOD_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_ICONNECTIONMOD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_IConnectionMod.ja
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
#include <NXOpen/CAE_Connections_IConnection.hxx>
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
            class IConnectionMod;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IConnection;
        }
    }
    class PhysicalMaterial;
    namespace CAE
    {
        namespace Connections
        {
            class _IConnectionModBuilder;
            class IConnectionModImpl;
            /**  @brief  This class represents an interface to a connection object.  

               <br> This is an abstract class, and cannot be created.  <br> 
             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  IConnectionMod : public NXOpen::CAE::Connections::IConnection
            {
                private: IConnectionModImpl * m_iconnectionmod_impl;
                private: friend class  _IConnectionModBuilder;
                protected: IConnectionMod();
                public: ~IConnectionMod();
                /** Use this function to set the connection material. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetMaterial
                (
                    NXOpen::PhysicalMaterial * material /** The connection material */
                );
                /** Use this function to set the connection material to be inherited from support. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetInheritedMaterial
                (
                );
                /** Use this function to set the connection description. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetUserDescription
                (
                    const NXString & description /** User description of the connection */
                );
                /** Use this function to set the connection description. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
                 <br>  Created in NX11.0.0.  <br>  
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
