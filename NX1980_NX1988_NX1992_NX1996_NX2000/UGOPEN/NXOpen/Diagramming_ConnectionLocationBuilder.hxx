#ifndef NXOpen_DIAGRAMMING_CONNECTIONLOCATIONBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_CONNECTIONLOCATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_ConnectionLocationBuilder.ja
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
#include <NXOpen/Diagramming_LocationBuilder.hxx>
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        class ConnectionLocationBuilder;
    }
    namespace Diagramming
    {
        class LocationBuilder;
    }
    namespace Diagramming
    {
        class _ConnectionLocationBuilderBuilder;
        class ConnectionLocationBuilderImpl;
        /**
            Represents a ConnectionLocationBuilder.
             <br> This is a sub-builder class and cannot be directly instantiated  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  ConnectionLocationBuilder : public NXOpen::Diagramming::LocationBuilder
        {
            private: ConnectionLocationBuilderImpl * m_connectionlocationbuilder_impl;
            private: friend class  _ConnectionLocationBuilderBuilder;
            protected: ConnectionLocationBuilder();
            public: ~ConnectionLocationBuilder();
            /**Returns  the segment identifier.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int SegmentIdentifier
            (
            );
            /**Sets  the segment identifier.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSegmentIdentifier
            (
                int segmentId /** segmentid */ 
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