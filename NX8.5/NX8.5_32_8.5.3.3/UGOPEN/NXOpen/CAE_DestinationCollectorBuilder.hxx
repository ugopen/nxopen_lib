#ifndef NXOpen_CAE_DESTINATIONCOLLECTORBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DESTINATIONCOLLECTORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DestinationCollectorBuilder.ja
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
#include <NXOpen/CAE_DestinationCollectorBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class DestinationCollectorBuilder;
    }
    namespace CAE
    {
        class MeshCollector;
    }
    namespace CAE
    {
        class _DestinationCollectorBuilderBuilder;
        class DestinationCollectorBuilderImpl;
        /** Represents a Element Collector Container (Ecc) selection
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DestinationCollectorBuilder : public TaggedObject
        {
            private: DestinationCollectorBuilderImpl * m_destinationcollectorbuilder_impl;
            private: friend class  _DestinationCollectorBuilderBuilder;
            protected: DestinationCollectorBuilder();
            public: ~DestinationCollectorBuilder();
            /**Returns  the Automatic Mode value
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool AutomaticMode
            (
            );
            /**Sets  the Automatic Mode value
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetAutomaticMode
            (
                bool fAutoMode /** fautomode */ 
            );
            /**Returns  the Element Collector object 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::MeshCollector * ElementContainer
            (
            );
            /**Sets  the Element Collector object 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetElementContainer
            (
                NXOpen::CAE::MeshCollector * pElementContainer /** pelementcontainer */ 
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
