#ifndef NXOpen_PDM_DBENTITYPROXY_HXX_INCLUDED
#define NXOpen_PDM_DBENTITYPROXY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_DBEntityProxy.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class DBEntityProxy;
    }
    class NXObject;
    namespace PDM
    {
        class _DBEntityProxyBuilder;
        class DBEntityProxyImpl;
        /** JA class for the DBEntityProxy object <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  DBEntityProxy : public NXOpen::NXObject
        {
            private: DBEntityProxyImpl * m_dbentityproxy_impl;
            private: friend class  _DBEntityProxyBuilder;
            protected: DBEntityProxy();
            public: ~DBEntityProxy();
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
