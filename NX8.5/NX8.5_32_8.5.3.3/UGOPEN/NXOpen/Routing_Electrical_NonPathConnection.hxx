#ifndef NXOpen_ROUTING_ELECTRICAL_NONPATHCONNECTION_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_NONPATHCONNECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_NonPathConnection.ja
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
#include <NXOpen/Routing_Electrical_Connection.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class NonPathConnection;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class Connection;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class _NonPathConnectionBuilder;
            class NonPathConnectionImpl;
            /**  @brief 
                        Describes a connection that does not have a path
                         

             
                         <br> 
                        A pathless connection represents the abilitiy for objects to be 
                        connected even though there is not an explicit path between them.
                        See NX Open Routing help for detailed information on the Connection data model.
                         <br> 
                     <br> To create a new instance of this class, use @link Routing::Electrical::NonPathConnectionCollection::CreateNonPathConnection  Routing::Electrical::NonPathConnectionCollection::CreateNonPathConnection @endlink  <br> 
             <br>  Created in NX4.0.2.  <br>  
            */
            class NXOPENCPP_ROUTINGEXPORT  NonPathConnection : public Routing::Electrical::Connection
            {
                private: NonPathConnectionImpl * m_nonpathconnection_impl;
                private: friend class  _NonPathConnectionBuilder;
                protected: NonPathConnection();
                public: ~NonPathConnection();
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
