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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class Graph;
    }
    namespace CAE
    {
        namespace FTK
        {
            class IApplicationData;
        }
    }
    class NXObject;
    namespace Motion
    {
        class _GraphBuilder;
        class GraphImpl;
        /** Represents a graph, only creation is supported  <br> To create or edit an instance of this class, use @link NXOpen::Motion::GraphObjectBuilder  NXOpen::Motion::GraphObjectBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  Graph : public NXOpen::NXObject
        {
            private: GraphImpl * m_graph_impl;
            private: friend class  _GraphBuilder;
            protected: Graph();
            public: ~Graph();
            /** Creates a @link CAE::FTK::IApplicationData CAE::FTK::IApplicationData@endlink    @return  IApplicationData object 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::CAE::FTK::IApplicationData * CreateGraphLegendData
            (
            );
            /**  @brief 
                        Sets the graph object as a temporary one. Temporary graph objects are used to create a plot
                        and are deleted after plotting.
                         

             
                        
                         <br> 
                        Plots are saved in Layout States/Snapshots.
                         <br> 
                         <br> 
                        If the plot is created from a graph object which is saved as part of the solution,
                        a reference to that graph object is kept and will ensure the plot can be refreshed or restored
                        using the Layout States/Snapshot functionality.
                         <br> 
                         <br> 
                        When plotting directly from the XY result view, a graph object is created to plot and then deleted.
                        In this case a reference to the graph object will not work and it is important to know during the plotting process
                        that alternative references are needed.
                         <br> 
                        
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetIsTemporary
            (
                bool isTemporary /** istemporary */ 
            );
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
