#ifndef NXOpen_CAE_MESHCOLLECTORBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MESHCOLLECTORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshCollectorBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_MeshCollectorBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class MeshCollectorBuilder;
    }
    class Builder;
    namespace CAE
    {
        class PropertyTable;
    }
    namespace CAE
    {
        class _MeshCollectorBuilderBuilder;
        class MeshCollectorBuilderImpl;
        /**
            Represents a @link CAE::MeshCollectorBuilder CAE::MeshCollectorBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::MeshManager::CreateCollectorBuilder CAE::MeshManager::CreateCollectorBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  MeshCollectorBuilder : public Builder
        {
            /** Indicates the different element dimensions */
            public: enum ElementDimensionOption
            {
                ElementDimensionOptionPoint/** 0-d */,
                ElementDimensionOptionBeam/** 1-d */,
                ElementDimensionOptionShell/** 2-d */,
                ElementDimensionOptionSolid/** 3-d */,
                ElementDimensionOptionContactEdge/** edge contact */,
                ElementDimensionOptionContactFace/** face contact */
            };

            private: MeshCollectorBuilderImpl * m_meshcollectorbuilder_impl;
            private: friend class  _MeshCollectorBuilderBuilder;
            protected: MeshCollectorBuilder();
            public: ~MeshCollectorBuilder();
            /**Returns  the Mesh Collector's Property Table  <br> License requirements : None */
            public: NXOpen::CAE::PropertyTable * PropertyTable
            (
            );
            /**Returns  the collector name  <br> License requirements : None */
            public: NXString CollectorName
            (
            );
            /**Sets  the collector name  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCollectorName
            (
                const NXString & collectorName /** collectorname */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif