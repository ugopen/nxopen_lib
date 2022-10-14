#ifndef NXOpen_MECHATRONICS_EXTERNALCONNECTION_HXX_INCLUDED
#define NXOpen_MECHATRONICS_EXTERNALCONNECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ExternalConnection.ja
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
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class ExternalConnection;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _ExternalConnectionBuilder;
        class ExternalConnectionImpl;
        /** Represents the External Connection class.  External Connection objects are
                able to connect physics runtime properties to OPC signals.  <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::ExternalConnectionBuilder  NXOpen::Mechatronics::ExternalConnectionBuilder @endlink  <br> 
         <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnection NXOpen::Mechatronics::SignalMappingConnection@endlink  instead. <br>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnection instead.") NXOPENCPP_MECHATRONICSEXPORT  ExternalConnection : public NXOpen::DisplayableObject
        {
            private: ExternalConnectionImpl * m_externalconnection_impl;
            private: friend class  _ExternalConnectionBuilder;
            protected: ExternalConnection();
            public: ~ExternalConnection();
        };
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