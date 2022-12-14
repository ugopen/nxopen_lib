#ifndef NXOpen_ROUTING_TANGENCYGROUPBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_TANGENCYGROUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_TangencyGroupBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
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
        class TangencyGroupBuilder;
    }
    class Builder;
    class SelectNXObjectList;
    namespace Routing
    {
        class _TangencyGroupBuilderBuilder;
        class TangencyGroupBuilderImpl;
        /** Represents a @link NXOpen::Routing::TangencyGroupBuilder NXOpen::Routing::TangencyGroupBuilder@endlink 
            Assign tangency for segments connected with current editing spline.
             <br> To create a new instance of this class, use @link NXOpen::Routing::AssignTangencyBuilder::CreateTangencyGroupBuilder  NXOpen::Routing::AssignTangencyBuilder::CreateTangencyGroupBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  TangencyGroupBuilder : public NXOpen::Builder
        {
            private: TangencyGroupBuilderImpl * m_tangencygroupbuilder_impl;
            private: friend class  _TangencyGroupBuilderBuilder;
            protected: TangencyGroupBuilder();
            public: ~TangencyGroupBuilder();
            /**Returns  the segment current editing. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::SelectNXObjectList * SegmentList
            (
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
