#ifndef NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_CONTAINER_HXX_INCLUDED
#define NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_CONTAINER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TopologyOptimization_Container.ja
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
        namespace TopologyOptimization
        {
            class Container;
        }
    }
    class NXObject;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class _ContainerBuilder;
            class ContainerImpl;

            /// \cond NX_NO_DOC 
            /** Represents a Topology Optimization Container object <br> A @link Features::TopologyOptimization::Container Features::TopologyOptimization::Container@endlink  cannot be created independently. @link Features::TopologyOptimization::Study Features::TopologyOptimization::Study@endlink  and @link Features::TopologyOptimization::Subcase Features::TopologyOptimization::Subcase@endlink  are types of containers that can be created and deleted by the user.  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  Container : public NXOpen::NXObject
            {
                /** Reorder operation type. */
                public: enum ReorderType
                {
                    ReorderTypeBefore/** Reorder an object before another object in the same container */,
                    ReorderTypeAfter/** Reorder an object after another object in the same container */,
                    ReorderTypeInto/** Reorder an object into the container which does not have it */
                };

                private: ContainerImpl * m_container_impl;
                private: friend class  _ContainerBuilder;
                protected: Container();
                public: ~Container();

                /// \cond NX_NO_DOC 
                /** Gets all @link NXOpen::NXObject NXOpen::NXObject@endlink  members in the order they are referenced. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") OR features_modeling ("FEATURES MODELING") */
                public: void GetMembers
                (
                    std::vector<NXOpen::NXObject *> & members /** members */ 
                );

                /// \endcond 

                /// \cond NX_NO_DOC 
                /** Reorders a child object 'before' or 'after' another child object belonging to the same @link NXOpen::Features::TopologyOptimization::Container NXOpen::Features::TopologyOptimization::Container@endlink .
                                Reordering an object 'into' the @link NXOpen::Features::TopologyOptimization::Container NXOpen::Features::TopologyOptimization::Container@endlink  that does not have it will be implemented in the future. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("TOPOLOGY OPTIMIZATION FOR DESIGNERS") */
                public: void Reorder
                (
                    NXOpen::NXObject * source /** source */ ,
                    NXOpen::NXObject * target /** target */ ,
                    NXOpen::Features::TopologyOptimization::Container::ReorderType type /** type */ 
                );

                /// \endcond 
            };

            /// \endcond 
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