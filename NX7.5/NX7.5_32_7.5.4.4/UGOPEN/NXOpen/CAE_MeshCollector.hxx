#ifndef NXOpen_CAE_MESHCOLLECTOR_HXX_INCLUDED
#define NXOpen_CAE_MESHCOLLECTOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshCollector.ja
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
#include <NXOpen/CAE_IMeshCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class MeshCollector;
    }
    namespace CAE
    {
        class IMeshCollector;
    }
    namespace CAE
    {
        class _MeshCollectorBuilder;
        class MeshCollectorImpl;
        /**  @brief  Represents a MeshCollector  

           <br> To obtain an instance of this object use @link CAE::MeshCollectorBuilder CAE::MeshCollectorBuilder@endlink . <br> */
        class NXOPENCPPEXPORT  MeshCollector : public CAE::IMeshCollector
        {
            private: MeshCollectorImpl * m_meshcollector_impl;
            private: friend class  _MeshCollectorBuilder;
            protected: MeshCollector();
            public: ~MeshCollector();
        };
    }
}
#undef EXPORTLIBRARY
#endif