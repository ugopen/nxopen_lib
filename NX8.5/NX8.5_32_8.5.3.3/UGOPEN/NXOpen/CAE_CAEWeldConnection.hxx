#ifndef NXOpen_CAE_CAEWELDCONNECTION_HXX_INCLUDED
#define NXOpen_CAE_CAEWELDCONNECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CAEWeldConnection.ja
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
#include <NXOpen/CAE_CAEConnection.hxx>
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
        class CAEWeldConnection;
    }
    namespace CAE
    {
        class CAEConnection;
    }
    namespace CAE
    {
        class _CAEWeldConnectionBuilder;
        class CAEWeldConnectionImpl;
        /** Represents WeldConnection Recipe  <br> To create or edit an instance of this class, use @link CAE::CAEWeldConnectionBuilder  CAE::CAEWeldConnectionBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CAEWeldConnection : public CAE::CAEConnection
        {
            private: CAEWeldConnectionImpl * m_caeweldconnection_impl;
            private: friend class  _CAEWeldConnectionBuilder;
            protected: CAEWeldConnection();
            public: ~CAEWeldConnection();
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
