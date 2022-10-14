#ifndef NXOpen_CAE_EDGESEPARATIONCONDITIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_EDGESEPARATIONCONDITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_EdgeSeparationConditionBuilder.ja
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
        class EdgeSeparationConditionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectCAEEdgeList;
    }
    namespace CAE
    {
        class _EdgeSeparationConditionBuilderBuilder;
        class EdgeSeparationConditionBuilderImpl;
        /** Represents Edge Separation Condition used to create a @link NXOpen::CAE::EdgeSeparationConditionBuilder NXOpen::CAE::EdgeSeparationConditionBuilder@endlink 
                which can be used to create @link NXOpen::CAE::EdgeSeparation NXOpen::CAE::EdgeSeparation@endlink  objects.  <br> To create a new instance of this class, use @link NXOpen::CAE::CAEConnectionCollection::CreateEdgeSeparationConditionBuilder  NXOpen::CAE::CAEConnectionCollection::CreateEdgeSeparationConditionBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  EdgeSeparationConditionBuilder : public NXOpen::Builder
        {
            private: EdgeSeparationConditionBuilderImpl * m_edgeseparationconditionbuilder_impl;
            private: friend class  _EdgeSeparationConditionBuilderBuilder;
            protected: EdgeSeparationConditionBuilder();
            public: ~EdgeSeparationConditionBuilder();
            /**Returns  the source edge selection for Edge Separation
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEEdgeList * EdgeSelection
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