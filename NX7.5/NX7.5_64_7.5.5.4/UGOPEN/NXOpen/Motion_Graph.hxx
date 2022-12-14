#ifndef NXOpen_MOTION_GRAPH_HXX_INCLUDED
#define NXOpen_MOTION_GRAPH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_Graph.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class Graph;
    }
    namespace Motion
    {
        class _GraphBuilder;
        class GraphImpl;
        /** Represents a graph, only creation is supported */
        class NXOPENCPPEXPORT  Graph : public TaggedObject
        {
            private: GraphImpl * m_graph_impl;
            private: friend class  _GraphBuilder;
            protected: Graph();
            public: ~Graph();
        };
    }
}
#undef EXPORTLIBRARY
#endif
