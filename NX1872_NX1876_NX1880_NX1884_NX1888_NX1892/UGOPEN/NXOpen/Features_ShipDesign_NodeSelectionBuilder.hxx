#ifndef NXOpen_FEATURES_SHIPDESIGN_NODESELECTIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_NODESELECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_NodeSelectionBuilder.ja
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
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class NodeSelectionBuilder;
        }
    }
    class Builder;
    class SelectNXObjectList;
    namespace Features
    {
        namespace ShipDesign
        {
            class _NodeSelectionBuilderBuilder;
            class NodeSelectionBuilderImpl;
            /** Represents a @link NXOpen::Features::ShipDesign::SpatialBreakdownBuilder NXOpen::Features::ShipDesign::SpatialBreakdownBuilder@endlink .
                    This class defines ship breakdowns. 
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateNodeSelectionBuilder  NXOpen::Features::ShipCollection::CreateNodeSelectionBuilder @endlink  <br> 
             <br>  Created in NX1872.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  NodeSelectionBuilder : public NXOpen::Builder
            {
                private: NodeSelectionBuilderImpl * m_nodeselectionbuilder_impl;
                private: friend class  _NodeSelectionBuilderBuilder;
                protected: NodeSelectionBuilder();
                public: ~NodeSelectionBuilder();
                /**Returns  the nodes 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * Nodes
                (
                );
            };
        }
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
